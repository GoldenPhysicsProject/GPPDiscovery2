# Codex/GPT continuation — deterministic Mehler repair and real scalar endpoint certificate

## CI diagnosis

Verify2 head `9eb15fe03c50e5b7086e655d8b23e78832cb1dda` showed two apparent failures with different causes.

The structured-majorant job did not reach Lean: it failed during `Install elan`, so all later scalar steps were skipped/marked failed by the workflow. This is runner/bootstrap noise, not evidence against the scalar theorems.

The `codex-fast` lane had one genuine isolated Lean failure: `GppVerify.CelestialHolography.MehlerFockGammaCollapsedWeight`. Every surrounding scalar-box, dilogarithm, thermodynamic, helicity and Grassmannian step in that job passed. A rerun reproduced the same Mehler-Fock failure, proving it deterministic.

The earlier whole-expression coercion repair (`norm_cast` after rewriting the half-shifted Gamma identity) was therefore insufficient. The theorem was rewritten so that the real identity

`lam^2 * (pi / cosh(pi*lam)) = collapsedWeight lam`

is proved first by ring normalization, then lifted explicitly through `Complex.ofReal`. This removes tactic-sensitive normalization of the opaque real `collapsedWeight` cast.

Verify2 repair commit: `ad04910b2e366c41f6ce0620b024dcbc900a6f51`.

## Scalar-box DCT advance

The concrete raised-box DCT majorant is

`1 + (S*x1*x3)^(-delta)`, with `0 < delta < 1`.

Mathlib's theorem `intervalIntegral.intervalIntegrable_rpow'` gives the exact endpoint criterion `-1 < r` for `x^r`. Setting `r=-delta` proves the singular endpoint kernel `x^(-delta)` is Lebesgue interval-integrable whenever `delta<1`, on arbitrary real interval endpoints and hence on every affine simplex slice `[0,L]`.

This was formalized in

`GppVerify/CelestialHolography/RaisedBoxRealMajorantIntegrability.lean`

with theorems:

- `neg_rpow_intervalIntegrable`
- `neg_rpow_unit_intervalIntegrable`
- `neg_rpow_affine_slice_intervalIntegrable`.

The new file was imported into `FullConstruction` at Verify2 head

`9b92520a892e427208e6b96b8643e53501853a7d`.

CI for this head is newly launched/queued; do not call the endpoint certificate certified until its build lanes complete.

The remaining scalar analytic gap is now narrower: factor/lift the two endpoint kernels through the positive constant `S` and the nested affine simplex, establish a real integrable dominating function (or equivalent Tonelli certificate), exclude boundary faces AE, and invoke dominated convergence for the actual `simplexMoment` to obtain the right-regulator limit `1/6`.

## Other active fronts

### Principal series / completed zeta / Weil

No global RH claim was promoted. The exact `Delta=2s` dictionary, critical-line unitary/anti-Hermitian local response structure, and real-axis Gamma/Wiener-Hopf identities remain valid formal components. The global missing theorem remains an explicit prime-plus-Archimedean trace/Gram identification with the Weil quadratic form on the necessary test-function class, followed by unconditional positivity.

### Prime-gas thermodynamics

No redundant one-parameter rearrangement was added. The existing strict Gibbs variance, heat-capacity, entropy derivative, centered two-observable determinant and cumulant bridge remain the certified frontier. The next worthwhile theorem is genuinely multiparameter fluctuation geometry/curvature.

### YM/gravity cuts

No numerator claim was promoted. The honest blocker remains the absence of fixed-loop-momentum, nonzero-mu Yang-Mills tree currents suitable for sewing into the massive-vector cut. Higher-loop/generalized cuts and gravity numerators remain downstream.

### Spectral/chamber

The exact all-real target remains

`W_WH(lam) W_MF(lam) = lam^2 Gamma(1/2+i lam) Gamma(1/2-i lam) = pi lam^2/cosh(pi lam)`.

The current work is a Lean coercion repair only; no new analyticity or repeated-convolution claim is asserted.

Claude research was not inspected or used.
