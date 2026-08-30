import "jsr:@supabase/functions-js/edge-runtime.d.ts";

const jsonHeaders = { "content-type": "application/json; charset=utf-8" };

function reply(status: number, body: unknown): Response {
  return new Response(JSON.stringify(body), { status, headers: jsonHeaders });
}

function requireControlAuth(req: Request): Response | null {
  const expected = Deno.env.get("GPP_CONTROL_TOKEN");
  if (!expected) return reply(503, { ok: false, error: "control_auth_not_configured" });
  const supplied = req.headers.get("x-gpp-control-token") ?? "";
  if (supplied !== expected) return reply(401, { ok: false, error: "unauthorized" });
  return null;
}

function b64url(bytes: Uint8Array): string {
  let s = "";
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s).replaceAll("+", "-").replaceAll("/", "_").replace(/=+$/g, "");
}

function textB64url(text: string): string {
  return b64url(new TextEncoder().encode(text));
}

function pemToDer(pem: string): Uint8Array {
  const body = pem
    .replace(/-----BEGIN PRIVATE KEY-----/g, "")
    .replace(/-----END PRIVATE KEY-----/g, "")
    .replace(/\s+/g, "");
  const raw = atob(body);
  return Uint8Array.from(raw, (c) => c.charCodeAt(0));
}

type ServiceAccount = {
  client_email: string;
  private_key: string;
  token_uri?: string;
  project_id?: string;
};

async function googleAccessToken(): Promise<string> {
  const raw = Deno.env.get("GOOGLE_SERVICE_ACCOUNT_JSON");
  if (!raw) throw new Error("GOOGLE_SERVICE_ACCOUNT_JSON is not configured");
  const sa = JSON.parse(raw) as ServiceAccount;
  if (!sa.client_email || !sa.private_key) throw new Error("invalid service account JSON");

  const now = Math.floor(Date.now() / 1000);
  const tokenUri = sa.token_uri ?? "https://oauth2.googleapis.com/token";
  const header = { alg: "RS256", typ: "JWT" };
  const claims = {
    iss: sa.client_email,
    scope: "https://www.googleapis.com/auth/cloud-platform",
    aud: tokenUri,
    iat: now,
    exp: now + 3600,
  };

  const signingInput = `${textB64url(JSON.stringify(header))}.${textB64url(JSON.stringify(claims))}`;
  const key = await crypto.subtle.importKey(
    "pkcs8",
    pemToDer(sa.private_key),
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = new Uint8Array(
    await crypto.subtle.sign(
      { name: "RSASSA-PKCS1-v1_5" },
      key,
      new TextEncoder().encode(signingInput),
    ),
  );
  const assertion = `${signingInput}.${b64url(signature)}`;

  const body = new URLSearchParams({
    grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer",
    assertion,
  });
  const res = await fetch(tokenUri, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`google_oauth_failed:${res.status}:${text.slice(0, 500)}`);
  }
  const data = await res.json();
  if (!data.access_token) throw new Error("google_oauth_missing_access_token");
  return data.access_token as string;
}

function assertGoogleUrl(raw: string): URL {
  const url = new URL(raw);
  if (url.protocol !== "https:") throw new Error("https_required");
  const h = url.hostname.toLowerCase();
  if (!(h === "googleapis.com" || h.endsWith(".googleapis.com"))) {
    throw new Error("google_api_host_required");
  }
  return url;
}

function assertSupabaseManagementUrl(raw: string): URL {
  const url = new URL(raw);
  if (url.protocol !== "https:" || url.hostname !== "api.supabase.com") {
    throw new Error("supabase_management_host_required");
  }
  return url;
}

async function readJson(req: Request): Promise<Record<string, unknown>> {
  const value = await req.json();
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error("json_object_required");
  return value as Record<string, unknown>;
}

async function googleRequest(req: Request): Promise<Response> {
  const input = await readJson(req);
  const url = assertGoogleUrl(String(input.url ?? ""));
  const method = String(input.method ?? "GET").toUpperCase();
  const token = await googleAccessToken();
  const headers = new Headers((input.headers ?? {}) as Record<string, string>);
  headers.set("authorization", `Bearer ${token}`);
  if (input.body !== undefined && !headers.has("content-type")) headers.set("content-type", "application/json");

  const res = await fetch(url, {
    method,
    headers,
    body: input.body === undefined ? undefined : JSON.stringify(input.body),
  });
  const contentType = res.headers.get("content-type") ?? "";
  const payload = contentType.includes("application/json") ? await res.json() : await res.text();
  return reply(res.status, { ok: res.ok, status: res.status, data: payload });
}

async function supabaseRequest(req: Request): Promise<Response> {
  const token = Deno.env.get("SUPABASE_ACCESS_TOKEN");
  if (!token) return reply(503, { ok: false, error: "SUPABASE_ACCESS_TOKEN is not configured" });
  const input = await readJson(req);
  const url = assertSupabaseManagementUrl(String(input.url ?? ""));
  const method = String(input.method ?? "GET").toUpperCase();
  const headers = new Headers((input.headers ?? {}) as Record<string, string>);
  headers.set("authorization", `Bearer ${token}`);
  if (input.body !== undefined && !headers.has("content-type")) headers.set("content-type", "application/json");
  const res = await fetch(url, {
    method,
    headers,
    body: input.body === undefined ? undefined : JSON.stringify(input.body),
  });
  const contentType = res.headers.get("content-type") ?? "";
  const payload = contentType.includes("application/json") ? await res.json() : await res.text();
  return reply(res.status, { ok: res.ok, status: res.status, data: payload });
}

async function secretMetadata(): Promise<Response> {
  const resource = Deno.env.get("GPP_BOOTSTRAP_SECRET_RESOURCE") ??
    "projects/794183325166/secrets/CodexSupabase/versions/latest";
  const token = await googleAccessToken();
  const encoded = resource.split("/").map(encodeURIComponent).join("/");
  const url = `https://secretmanager.googleapis.com/v1/${encoded}:access`;
  const res = await fetch(url, { headers: { authorization: `Bearer ${token}` } });
  if (!res.ok) {
    const text = await res.text();
    return reply(res.status, { ok: false, status: res.status, error: text.slice(0, 500) });
  }
  const data = await res.json();
  // Deliberately do not return data.payload.data.
  return reply(200, {
    ok: true,
    name: data.name ?? resource,
    payload_present: Boolean(data.payload?.data),
    payload_crc32c_present: data.payload?.dataCrc32c !== undefined,
  });
}

Deno.serve(async (req: Request) => {
  try {
    const url = new URL(req.url);
    if (req.method === "GET" && url.pathname.endsWith("/health")) {
      return reply(200, {
        ok: true,
        service: "gpp-automaton",
        google_identity_configured: Boolean(Deno.env.get("GOOGLE_SERVICE_ACCOUNT_JSON")),
        supabase_admin_configured: Boolean(Deno.env.get("SUPABASE_ACCESS_TOKEN")),
        control_auth_configured: Boolean(Deno.env.get("GPP_CONTROL_TOKEN")),
      });
    }

    const authError = requireControlAuth(req);
    if (authError) return authError;

    if (req.method === "POST" && url.pathname.endsWith("/google/request")) return await googleRequest(req);
    if (req.method === "POST" && url.pathname.endsWith("/supabase/request")) return await supabaseRequest(req);
    if (req.method === "POST" && url.pathname.endsWith("/bootstrap/google-token-test")) {
      await googleAccessToken();
      return reply(200, { ok: true, google_oauth: "verified" });
    }
    if (req.method === "POST" && url.pathname.endsWith("/bootstrap/secret-test")) return await secretMetadata();

    return reply(404, { ok: false, error: "not_found" });
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return reply(500, { ok: false, error: message });
  }
});
