# Codex / GPT Discovery2 workbench

GPPDiscovery2 is the **GPT/Codex research and experimentation laboratory** for the Golden Physics Project. It is not the canonical Lean verification repository. Other assistants have separate workspaces; do not overwrite their work.

## Current routing (Daniel, 2026-11-17; supersedes old PR #11 instructions)

1. **Bootstrap first:** read private GPP-bridge CODEX.md, CODEX_RESEARCH_NOTES.md, CODEX_HEURISTICS.md and relevant work/codex/*.md, along with recent GPP-bridge PR #15 discussion. Read older no-go audits to avoid repeating failed reductions.
2. **Research in Discovery2:** run mathematics, exact-arithmetic checks, scripts, numerics, falsifiers, and reproducible experiments here. Commit public theorem/proof notes and reusable code to a Discovery2 research branch/PR, currently draft PR #29 for the arithmetic–Cesàro/Suzuki line.
3. **Private full-fidelity continuity:** append detailed derivations, tests, failure analysis, branch/commit receipts and next proof obligations to GPP-bridge/CODEX_RESEARCH_NOTES.md. Periodically mirror material entries to Supabase codex.* where access permits. Do not put private internal strategy or secrets in this public repo.
4. **Audit channel:** send a **single complete result/handoff** in GPP-bridge PR #15 to Turbo, with exact claims, links, reproductions, controls and limitations. Turbo audits independently and relays validated units to Claude via PR #14.
5. **Verify is read-only for GPT in this workflow:** inspect GPPVerify, other Discovery repositories, bridge audits and the GPP Drive folders for source matching, but **do not modify or merge canonical GPPVerify** or bypass Turbo->Claude promotion unless Daniel explicitly changes the routing.
6. **Experiment discipline:** read LAB_PROTOCOL.md, run python -m rh_lab.cli check and python -m unittest discover -s tests before changing the rh_lab framework, preserve catalog metadata for new rh_lab experiments and log precise evidence level. Standalone scripts must state assumptions and falsifiers. If local runner unavailable, do not claim CI or remote execution occurred.
7. **Scientific standards:** test completed shifted F_theta controls, check actual pole+gamma+prime normalization, distinguish exact identities from finite rational checks and conditional inequalities, and never present a finite positive test as RH or a physical unification theorem.

The active arithmetic–Cesàro work is a research program. A global one-sided bound on the **completed** Suzuki potential would imply RH, but no such estimate is established as of this instruction update.
