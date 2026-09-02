# Raised-box AE import repair — Codex run

Codex/GPT track only. No Claude material inspected.

## Verify2 CI diagnosis

`GPPVerify2:codex/lean-workbench` commit `5a9280fa6e09414e9e3c7806838ee1f82e3376d1` failed changed-Lean run `33575088529` only because the import

`Mathlib.MeasureTheory.Measure.Typeclasses.NullSingletonClass`

does not exist in the pinned Mathlib tree. The source-`sorry` gate passed, and the existing raised-box majorant, pointwise-limit, and concrete-moment dependencies rebuilt successfully.

The mathematics of `RaisedBoxInnerAE.lean` was not implicated. The theorem removes the single upper endpoint of `Ioc 0 (1-x1-x2)` using Lebesgue nonatomicity and applies the already-proved strict-simplex pointwise regulator limit.

## Repair

Replaced the invalid import by the already-valid project module

`Mathlib.MeasureTheory.Measure.Lebesgue.Basic`

while retaining `Measure.ae_ne volume (1 - x1 - x2)`.

New Verify2 head: `ed36c072afed564ef6b547a974dfe65ef7bee579`.
Fresh changed-Lean run: `33579108873`.
At record time the source-`sorry` gate was green and cache/build setup was still running.

## Exact theorem boundary

For fixed `S,T>0`, `x1>0`, `x2>0`, and `x1+x2<1`,

`integrand ε S T x1 x2 x3 -> 1`

as `ε -> 0` for Lebesgue-a.e. `x3` in `Ioc 0 (1-x1-x2)`. The sole possible strict-simplex failure in that half-open interval is the upper endpoint, a null singleton.

If the repaired module is green, the next scalar theorem should be the actual inner interval dominated-convergence limit, using the existing one-channel majorant and inner-slice integrability certificate. No further Beta/Gamma surrogate is justified.

## Other active fronts

Number thermodynamics remains at the certified normalized two-parameter covariance/Fisher determinant stage. The next genuine step is termwise differentiation of `Z(β,η)` and `log Z` on `η>0`, not more algebraic Legendre rewriting.

The Gamma/Mehler-Fock/Wiener-Hopf chamber hierarchy remains exactly formalized through finite positive recurrence factors and strict real-part positivity. The proposed chamber characteristic-function/convolution law still depends on a Barnes/Fourier Gamma integral and must not be axiomatized.

The global Weil/RH boundary is unchanged: no local Archimedean positivity substitutes for identification and unconditional positivity of the genuine prime-plus-Archimedean Weil quadratic form.

Honest `D_s=4, μ≠0` Yang-Mills sewing remains immediately downstream of scalar regulator closure.
