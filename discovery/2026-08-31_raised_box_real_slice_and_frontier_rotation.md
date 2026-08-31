# Codex/GPT research run: raised-box real slice and frontier rotation

Date: 2026-08-31

## Verify2 scalar-box advance

On `codex/lean-workbench`, two concrete real-majorant modules were added after auditing the existing raised-box stack.

First, `RaisedBoxRealMajorantSlice.lean` proves the nonnegative factorization

`(S*x1*x3)^(-δ) = (S*x1)^(-δ) * x3^(-δ)`

and uses the already-certified endpoint theorem to obtain interval integrability of the singular channel on every affine inner simplex slice. Commit: `6710083dc0e74eca24bfea13080b2492601194cb`.

Second, `RaisedBoxRealMajorantSliceIntegral.lean` uses Mathlib's exact `intervalIntegral.integral_rpow` theorem to target the explicit real slice identities

`∫_0^L x^(-δ) dx = L^(1-δ)/(1-δ)`

and

`∫_0^L (S*x1*x3)^(-δ) dx3 = (S*x1)^(-δ) * L^(1-δ)/(1-δ)`

for `δ<1` and nonnegative physical slice data. Commit: `0dba1bd6503d9ccc7d854762c6c2488f68af6c7b`.

These two new files are pending terminal CI certification as of this note. No scalar regulator closure is claimed yet.

## Exact scalar frontier

The existing concrete raised-box layer already proves interior positivity, pointwise regulator removal, and the one-channel bound

`Q^(-ε) ≤ 1 + (S*x1*x3)^(-δ)`.

The complex Beta reduction and Gamma closure are already formal, including

`B(1-δ,3-δ) B(1-δ,2) = Γ(1-δ)^2 / Γ(4-2δ)`.

`RaisedBoxResidueAssembly.lean` still takes as hypothesis the actual one-sided convergence

`simplexMoment ε S T → 1/6` as `ε→0+`.

Therefore the remaining Lean task is the real nested Fubini/DCT assembly: use the new explicit inner-slice evaluation to produce an integrable middle/outer majorant, discharge AE pointwise convergence on the simplex interior, and apply nested interval-integral dominated convergence. Only after this theorem lands may the raised-box residue `1/6` and the μ^4 shifted contribution `-1/6` be promoted from conditional assembly to unconditional closure.

## Spectral / Wiener–Hopf audit

No new theorem was added because the all-real result already exists in `SechConvolutionZeroShift.lean`:

`∫_R dx / (cosh(πx) cosh(π(λ-x))) = (2/π) extendedWienerHopfWeight λ`

for every real `λ`, including the removable origin. The chamber hierarchy file explicitly states that no convolution theorem is assumed: higher Gamma chambers are propagated algebraically by positive recurrence factors. Hence repeated-sech-convolution identification of higher chambers remains open and must not be inferred from positivity alone.

## Prime-gas audit

The strict zeta-Gibbs cumulant determinant and strict thermodynamic consequences are already formal on the current branch. `ZetaGibbsInformationGeometry.lean` is still a one-parameter Bregman/Jeffreys geometry in β. A genuinely curved multi-parameter thermodynamic manifold requires introducing and controlling a second coupling (naturally the already-observed `X^2` statistic); no curvature claim is made before that two-parameter partition function is constructed.

## Weil bridge audit

`PrimeResponseTransferOperator.lean` proves strict contraction and positive completed defect only for a scalar normalized response model. The file itself explicitly separates this from the true Archimedean/prime amplitude spaces and genuine Weil quadratic form. The RH-critical missing theorem therefore remains the actual arithmetic relative-trace/Gram identification plus positivity. No RH claim.

## YM/gravity boundary

No change in the honest boundary: graph/topology and Ward/projector infrastructure do not replace explicit fixed-loop-momentum nonzero-μ Yang–Mills tree currents/numerators sewn over physical massive-vector polarizations. Higher-loop/generalized cuts and gravity remain downstream.
