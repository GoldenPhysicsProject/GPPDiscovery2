# Codex/GPT research run — scalar inner DCT right-filter assembly

Date: 2026-09-02
Track: Codex/GPT only. No Claude research inspected or used.

## Verified CI state

GPPVerify2 `codex/lean-workbench` commit `fe8c43f52ab3a0bf1268b2b543d56a236733b6e8` passed changed-Lean run `33582986546`. Therefore `GppRaisedBoxInnerAE.integrand_tendsto_one_ae_inner` is changed-module green under the pinned Lean/Mathlib toolchain.

The theorem gives, for `S,T>0` and strict base coordinates `x1,x2>0`, `x1+x2<1`, almost-everywhere convergence of the concrete raised-box integrand to one on the inner interval. The sole exceptional boundary point is the upper endpoint, removed using the pinned Mathlib `NoAtoms` API.

## New formalization

Pushed GPPVerify2 commit `4f1f866aa2a6a70d097091110fe3802a716b5c8e`, adding `GppVerify/CelestialHolography/RaisedBoxInnerDCT.lean`.

The key correction is to formulate regulator removal along the physical right-hand filter

`nhdsWithin 0 (Set.Icc 0 δ)`

rather than the unrestricted neighborhood of zero. The one-channel majorant requires `0 ≤ ε ≤ δ`, and this filter supplies exactly that eventual condition. The existing pointwise convergence theorem is stronger (`nhds 0`) and therefore restricts to the right-hand filter without loss.

The new theorem assembles the actual innermost interval dominated-convergence step:

`∫_0^(1-x1-x2) integrand ε S T x1 x2 x3 dx3  ->  ∫_0^(1-x1-x2) 1 dx3`

using:
- the green AE inner convergence theorem;
- the certified one-channel estimate `integrand ≤ 1 + (S*x1*x3)^(-δ)`;
- interval integrability of the singular channel for `δ<1`;
- nonnegativity of the concrete real-rpow integrand.

The theorem deliberately leaves only AE strong measurability of the concrete `Real.rpow` integrand as an explicit hypothesis. No axiom or surrogate lemma is introduced for this obligation.

Fresh changed-Lean run `33587060991` was queued for `4f1f866...` at the time of this record; do not call the new theorem certified until that run completes.

## Other active fronts

Number thermodynamics remains at the certified normalized strict Fisher/covariance determinant for arbitrary real `β` with `η>0`. The next honest step is differentiation under the quadratically confined tsum, then `∂β log Z = -<L>`, `∂η log Z = -<L²>`, and Hessian = covariance.

Principal-series/completed-zeta and exact Gamma/Mehler-Fock/Wiener-Hopf/chamber results remain valid local/Archimedean structure. No global Weil/RH positivity theorem is claimed. The missing global bridge remains the independent prime-plus-Archimedean quadratic form, exact explicit-formula identification on an adequate test class, and positivity.

Honest fixed-loop `Ds=4, μ≠0` Yang-Mills state sewing remains immediately downstream of scalar regulator closure; no triangle/bubble/rational sector is to be excluded by assumption. Gravity and generalized/higher-loop cuts remain downstream of the honest YM layer.

## Next frontier

1. Read changed-Lean run `33587060991` and repair any elaboration/interface errors.
2. Discharge AE strong measurability of the concrete inner `Real.rpow` integrand on the restricted interval.
3. Remove that hypothesis from `inner_interval_tendsto_one`.
4. Propagate DCT through the middle and outer interval layers and conclude `J_ε(S,T) -> 1/6` for the nonnegative regulator limit.
5. In parallel, begin the rigorous quadratically confined partition-sum differentiation bridge.
