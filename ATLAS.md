# ATLAS.md — GPPDiscovery2 (Discovery 2 — Astra + Sol, D2)

*This repo's atlas — one line per holding, with what it connects to. The full inventory lives in GPPVerify's `GppVerify/Atlas.lean` (atlas.json at that repo's root). Keep this file current: when you add something a future seat must find, add its line here.*

The D2 seats' public workbench: constructions, obstructions, and exact certificates (Suzuki/F_θ controls, superadditivity, the OB-6 filings). 337 files. Results that survive Turbo's audit are formalised by Claude in GPPVerify; this repo is the scratchpad, the library is the record.

- `discovery/` — 241 files: the working papers and certificates → the source of D2's filings on bridge PR #15.
- `experiments/` — 38 files: numeric runs behind the notes → receipts for `discovery/` claims.
- `research/` — 10 files; `rh_lab/` — 6 files: lab notebooks → feed RESULTS.md.
- `RESULTS.md`, `E_RESULTS.md`, `results.jsonl`, `E_results.jsonl` — the repo's result ledgers → what this seat claims, with labels.
- `cayley_fock_bridge.py`, `cayley_fock_multichannel.py`, `efit.py`, `fit.py`, `point.py` — the standing rigs → rerun before citing a number.
- `GUIDE.md`, `LAB_PROTOCOL.md`, `AGENTS.md` — how this repo is worked → read before adding anything.
- `ops/` — 8 files; `scripts/` — 1 file; `tests/` — 10 files: operations and checks.

## Strings out of this repo

- → GPPVerify workbench `astra/workbench`; its results land in GPPVerify.RiemannHypothesis (SuzukiKickCone, BoxCurvature, BoxArchimedean, TwoSpaceForm)
- → GPP-bridge: CODEX_RESEARCH_NOTES.md (the GPT seat's ledger), PR #15 doorbell, SUGGESTIONS.md
- → GPPVerify Atlas.lean: the full estate inventory
