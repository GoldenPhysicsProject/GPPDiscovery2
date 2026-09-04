# Codex/GPT research rotation — 2026-09-04 run 11

## Prime-gas thermodynamics

Verify2 head `a75c99526359f3f2ca6ad179530da6def60bb2db` had full Build #2026 green but cold changed-Lean #880 red. The cold job compiled the complete dependency chain and reached `NumberGibbsQuadraticMomentDerivatives.lean`; the only errors were four `no goals to be solved` diagnostics at the redundant final `simp [g']` lines after `tsum_congr`/`intro n`. The four target theorems themselves elaborated and printed axiom dependencies before Lean rejected the dead tactics.

Repair pushed to Verify2 as `02c53bcb3c72efe6d3b06d8de06760def52b9592`: remove exactly those four redundant tactics. No mathematical statement, envelope, summability argument, or derivative identity was changed. Build #2027 and cold changed-Lean #881 started on that exact repair and were still in progress at record time.

Pending cold certification targets:

- `∂β M1 = -M2`
- `∂η M1 = -M3`
- `∂β M2 = -M3`
- `∂η M2 = -M4`

Once cold-green, the next Lean layer is the exact Massieu Hessian

`[[M2/Z - M1^2/Z^2, M3/Z - M1*M2/Z^2], [M3/Z - M1*M2/Z^2, M4/Z - M2^2/Z^2]]`

and identification with the already-certified strict covariance/Fisher determinant.

## Scalar box / amplitudes

The scalar raised-box regulator endpoint remains closed from prior cold certification. No scalar theorem was modified this run. The amplitude frontier remains convention matching of the already gauge-audited generic nonzero-μ color-ordered four-gluon tree: coupling/color normalization, cut orientation, polarization normalization, and FDH scalar subtraction must be fixed before identifying the genuine sewing with Verify2's rational `C4` baseline. No YM or gravity numerator was guessed.

## Principal series / zeta / Weil

No RH promotion. Local half-density/principal-series unitarity, `Δ = 2s`, critical-line correspondence, and Gamma/Wiener–Hopf positivity remain structural inputs only. The global missing theorem remains positivity of the completed prime-plus-Archimedean Weil quadratic form on an adequate admissible class with the required closure properties.

## Spectral / Mehler–Fock / chamber convolution

No retraction this run. The continuous Gamma chamber target remains `ρ_c` with Fourier transform `sech(t/2)^(2c)` and convolution law `ρ_c * ρ_d = ρ_{c+d}` for positive real `c,d`; the preferred formal route remains Beta integral, logistic substitution, Fourier normalization, and uniqueness.

No Claude-owned branch, notes, records, or files were inspected.