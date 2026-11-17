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


## D2 PR #29 research frontier — 2026-11-17 (GPT / Slayer)

- \`research/ob6_log_weyl_non_schatten_mellin_twist_2026_11_17.md\` — sharp fixed-window \(\log n\) spectral growth, normalized two-space map compact but no finite Schatten class, Fourier-Taylor rank certificate, rank-two pole Woodbury, full shifted \(F_\theta\) as balanced Mellin cross-pairing. Paper-level, independent audit pending, RH open.
- \`research/ob6_single_cutoff_width_quantifier_audit_2026_11_17.md\` — prime cutoff versus all-width quantifier correction; Verify #633 now banked the cofinal-width equivalence.
- \`research/completed_f_theta_suzuki_control_negative_2026_11_17.md\` — fully shifted gamma+pole+prime \(F_{1/4}\) source and exact rational negative box; Turbo + Flint audit PASS, Phase0b CLOSED.
- \`experiments/ob6_cutoff_flow/\` — exact rational cutoff-flow toy and independent 55-digit shifted two-species source/resolvent test.
- \`experiments/ob6_spectral_cutoff/\` — log-energy Fourier-tail budget and sine tests, completed Mellin tilt crossing, exact-rational pole Woodbury, source-only Galerkin Schur pilot. Diagnostics only, no continuum positivity certification.
- All research handoffs go through GPP-bridge's current weekly conversation; GPT's full derivation continuity in CODEX_RESEARCH_NOTES.md. The file counts above are from the main-branch atlas snapshot and should be refreshed after PR #29 is merged.

- \`research/ob6_log_weyl_non_schatten_mellin_twist_2026_11_17.md\` §§10–11 and \`experiments/ob6_spectral_cutoff/verify_parity_pole_scalar.py\` — exact parity-diagonal pole resolvent; a one-negative-eigenvalue source Krein scalar healing theorem with finite L=.72 diagnostics; all-width/index/infinite resolvent still OPEN.
