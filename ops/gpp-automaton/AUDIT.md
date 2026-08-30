# GPP Automaton bootstrap audit

This file records control-plane bootstrap work. It must never contain secret payloads.

## 2026-08-30

### Objective

Create a persistent high-capability administrative bridge for the authorized GPP development stack.

### Completed

- Confirmed GitHub write/admin access to `GoldenPhysicsProject/GPPDiscovery2` through the connected GitHub app.
- Confirmed Supabase connector discovery exposed Edge Function deployment and SQL execution actions.
- Confirmed the Supabase connector became unavailable when SQL execution was invoked; no SQL change was applied.
- Recorded the control-plane architecture in `README.md`.
- Recorded bootstrap, recovery, IAM/secret-store strategy and the known Supabase RLS repair in `BOOTSTRAP.md`.
- Added the first Supabase Edge Function implementation in `bridge/index.ts`.
- The bridge implements authenticated health, Google OAuth bootstrap verification, Secret Manager presence verification without returning payload data, a general authenticated Google API request adapter restricted to `*.googleapis.com`, and a general Supabase Management API adapter restricted to `api.supabase.com`.
- Added `bridge/deno.json`.

### Existing credential/runtime evidence

A previous local bootstrap test successfully parsed the GPP Automaton service-account JSON and created a signed RS256 Google OAuth JWT without exposing the private key. The subsequent token exchange failed before reaching Google because the local execution container could not resolve `oauth2.googleapis.com`.

### Not yet completed

- The bridge has not yet been deployed to Supabase Edge Functions because the Supabase connector disappeared at invocation time.
- The Google service-account JSON has not been copied into Git or Drive by this bootstrap work.
- The `CodexSupabase` secret payload has not been read or verified by the bridge.
- The known `codex.corrections_ledger` RLS remediation has not yet been applied.
- No credential rotation has been performed.
- No claim of a working production control plane is made until deployment and end-to-end tests succeed.

### Next executable sequence

1. Restore any networked deployment surface, preferably Supabase Edge Functions or Cloud Run.
2. Configure bridge secrets/environment without committing payloads.
3. Deploy `bridge/index.ts`.
4. Call `/health`.
5. Call `/bootstrap/google-token-test`.
6. Call `/bootstrap/secret-test` and verify only secret metadata/presence.
7. Exercise the Supabase Management API adapter.
8. Apply and verify the `codex.corrections_ledger` RLS repair.
9. Add provider adapters and browser-automation execution as required.
10. Move toward attached identity/workload federation and rotate transient bootstrap credentials.
