# GPP Automaton bootstrap and recovery

## Purpose

Bootstrap a persistent administrative control plane capable of operating the authorized GPP development stack without relying on any single ChatGPT connector.

## Root identity

Primary automation principal:

`gpp-automaton@gpp-automaton.iam.gserviceaccount.com`

Google Cloud project ID:

`gpp-automaton`

The control plane is intended to operate with broad project-level administrative authority where explicitly granted by the project owner.

## Root secret store

Google Secret Manager is the intended long-term root secret store.

Known bootstrap secret resource:

`projects/794183325166/secrets/CodexSupabase`

Do not place secret payloads, service-account private keys, personal access tokens or refresh tokens in this repository.

## Bootstrap sequence

1. Obtain a networked runtime with outbound HTTPS.
2. Authenticate as the GPP Automaton service account using workload identity, an attached service-account identity, or the existing bootstrap key only for initial setup.
3. Exchange the service-account JWT at Google OAuth and verify access to Secret Manager.
4. Read only the required secret payloads in memory.
5. Use the Supabase credential to establish the persistent database/Edge Function control path.
6. Deploy the GPP Automaton bridge.
7. Move remaining provider credentials into Secret Manager.
8. Replace static service-account keys with workload identity or attached identity where practical.
9. Rotate any credential that was ever exposed in chat or another transient surface.
10. Verify all provider adapters and record results in `AUDIT.md`.

## First target runtime

Supabase Edge Functions are the preferred bootstrap runtime because they provide outbound HTTPS and can be deployed without maintaining a VM. The ChatGPT Supabase connector exposed `deploy_edge_function` and `execute_sql` during discovery, but the connector became unavailable at invocation time on 2026-08-30. Deployment should resume there when the connector is available again.

Alternative runtimes, in priority order:

- Google Cloud Run with an attached GPP Automaton identity.
- GitHub Actions using workload identity federation into Google Cloud.
- A managed serverless runtime with outbound HTTPS and a secret store.
- A dedicated administrative VM only if the serverless routes are unavailable.

## Required environment/secret names

The bridge should consume configuration by secret/environment reference, never by source literal:

- `GOOGLE_PROJECT_ID`
- `GOOGLE_SERVICE_ACCOUNT_JSON` only during bootstrap if no attached identity is available
- `SUPABASE_PROJECT_REF`
- `SUPABASE_ACCESS_TOKEN`
- `GPP_CONTROL_TOKEN` or equivalent asymmetric caller-authentication configuration
- provider credentials added later

## Google verification test

A successful bootstrap must verify both OAuth token issuance and Secret Manager access. The critical resource check is:

`projects/794183325166/secrets/CodexSupabase/versions/latest`

The bridge must report only success/failure metadata, never the decoded payload.

## Supabase security repair

Once Supabase administrative access is established, repair the known `codex.corrections_ledger` exposure and then run the security advisor again:

```sql
alter table codex.corrections_ledger enable row level security;
revoke all on table codex.corrections_ledger from anon, authenticated;
grant select, insert, update, delete on table codex.corrections_ledger to service_role;
```

Do not mark this remediation complete until the migration succeeds and the advisor is rechecked.

## Recovery principle

The system must be capable of recreating provider adapters from this repository plus the root automation identity and root secret store. Losing a ChatGPT connector must not strand administration again.
