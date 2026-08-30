# GPP Automaton bootstrap audit

This file records control-plane bootstrap work. It must never contain secret payloads.

## 2026-08-30

### Objective

Create a persistent high-capability administrative bridge for the authorized GPP development stack.

### Completed

- Confirmed GitHub write/admin access to `GoldenPhysicsProject/GPPDiscovery2` through the connected GitHub app.
- Confirmed Supabase connector discovery exposed Edge Function deployment and SQL execution actions, but the connector became unavailable when invoked; no direct Supabase SQL change was applied through that connector.
- Recorded the control-plane architecture in `README.md`, bootstrap/recovery strategy in `BOOTSTRAP.md`, and initial Supabase Edge Function implementation in `bridge/index.ts` with `bridge/deno.json`.
- Installed and authenticated the Vercel connector and created the production project `gpp-automaton` (`prj_uHhzmEUPZiEyvWLLvIA9wXDQeSE6`).
- Deployed a working production Vercel serverless runtime and verified HTTP 200 health responses.
- Verified Vercel OIDC claims for the team issuer `https://oidc.vercel.com/daniel-toupins-projects` and production project subject form.
- Used the existing GPP Automaton service-account key locally only to sign a short-lived Google OAuth assertion; the private key was not committed to GitHub or installed as a Vercel runtime secret.
- Used the short-lived assertion from a fixed-purpose bootstrap function to create Google Workload Identity Federation pool `gpp-vercel` and OIDC provider `vercel` in project number `794183325166`.
- Provider conditions restrict accepted Vercel tokens to owner `daniel-toupins-projects`, project `gpp-automaton`, environment `production`.
- Granted the `gpp-vercel` workload principal set `roles/iam.workloadIdentityUser` and `roles/iam.serviceAccountTokenCreator` on `gpp-automaton@gpp-automaton.iam.gserviceaccount.com`.
- Verified permanent keyless authentication end to end: Vercel OIDC -> Google STS/WIF -> service-account impersonation -> Google Resource Manager.
- Verified Secret Manager access through the permanent keyless bridge without exposing payload data.
- Verified `CodexSupabase` exists as version 1 and contains a payload with CRC metadata.
- Diagnosed the stored `CodexSupabase` payload without exposing it: version 1 is a four-character JSON number, not a Supabase PAT.
- Confirmed Secret Manager currently contains only one secret, `CodexSupabase`.
- Attempted Supabase Management API authentication using the stored payload; Supabase returned HTTP 401 `JWT could not be decoded`, consistent with the malformed/wrong secret payload.
- Confirmed the official Supabase Management API SQL endpoint needed for the pending repair is `POST /v1/projects/{ref}/database/query` and requires database write permission.

### Current control-plane state

The production `gpp-automaton` Vercel runtime is live and can authenticate to Google Cloud keylessly through Vercel OIDC and Google Workload Identity Federation. Static Google credentials are no longer required in the permanent runtime path. Secret Manager can be read in-memory by the bridge.

The remaining blocker to Supabase administration is credential content, not network/runtime/IAM. `CodexSupabase` version 1 does not contain a valid Supabase Management API PAT.

### Still pending

- Replace/add a Secret Manager version for `CodexSupabase` containing the intended Supabase Management API PAT.
- Verify Supabase Management API project access for `dunrgpupddbmzffntwph`.
- Apply and verify:
  ```sql
  alter table codex.corrections_ledger enable row level security;
  revoke all on table codex.corrections_ledger from anon, authenticated;
  grant select, insert, update, delete on table codex.corrections_ledger to service_role;
  ```
- Run Supabase security checks after the migration.
- Add broader provider adapters and authenticated administrative operations.
- Retire transient bootstrap deployments after their short-lived assertions expire; never rely on them for ongoing authentication.
- Rotate any credentials that were previously pasted into chat after durable secret storage is confirmed.

### Next executable sequence

1. Correct `CodexSupabase` with a valid PAT in Secret Manager.
2. Verify `GET https://api.supabase.com/v1/projects/dunrgpupddbmzffntwph` through the bridge.
3. Apply the fixed RLS migration through `/v1/projects/dunrgpupddbmzffntwph/database/query`.
4. Verify RLS/grants and run security-advisor checks.
5. Extend the control plane to additional Google Cloud, GitHub, DNS, Play/Search Console, deployment and browser-automation surfaces.
