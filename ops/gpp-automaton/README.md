# GPP Automaton Control Plane

This directory records the bootstrap and implementation of the GPP Automaton administrative control plane.

## Goal

Provide a persistent, extensible execution layer through which an authorized operator can administer the Golden Physics Project development stack end to end, independent of which native ChatGPT connector happens to be available in a given session.

The intended control path is:

`Operator -> ChatGPT/Codex -> GPP Automaton -> provider APIs / deployment runtimes / authenticated browser automation`

The system is designed for broad administrative capability while keeping credentials out of source control and logs.

## Capability targets

- Google Cloud Resource Manager, IAM, Secret Manager, Cloud Run, Cloud Functions, Cloud Build, Storage, Logging, Monitoring, Search Console, Play Developer APIs, and other enabled Google APIs.
- Supabase Management API, database migrations, Edge Functions, Vault, auth and project administration.
- GitHub repository administration, CI/CD, releases, Actions, issues, pull requests and repository configuration.
- Google Drive/Docs/Sheets and other authorized Workspace APIs.
- DNS/domain providers, deployment services and application backends.
- A general outbound HTTPS provider adapter for services that do not yet have a dedicated module.
- Authenticated browser automation for settings that have no usable API.

## Design rules

1. No secret payload is committed to Git.
2. Secret values are never written to application logs or audit records.
3. Administrative actions are auditable by operation, caller, target, timestamp and outcome.
4. Provider adapters can be added without changing the front-end contract.
5. The control plane may hold broad privileges, but every externally callable operation remains authenticated.
6. Bootstrap and disaster recovery are documented so the system can recreate itself.

## Current bootstrap state

The source-of-truth bootstrap record is `BOOTSTRAP.md`. The first bridge implementation is under `bridge/`.

As of 2026-08-30, the principal runtime blocker is not local credential parsing or JWT signing. A prior local test successfully loaded the GPP Automaton service-account JSON and produced a signed Google OAuth JWT, but the local execution container could not resolve `oauth2.googleapis.com`. Supabase Edge Functions were identified as a suitable networked bootstrap runtime, but the Supabase connector became unavailable at invocation time. This repository therefore records the implementation and recovery path so deployment can resume immediately on the next writable execution surface.
