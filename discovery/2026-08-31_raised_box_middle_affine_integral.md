# Codex/GPT research run: raised-box middle affine integral

Date: 2026-08-31

## Scalar-box advance

`GPPVerify2/codex/lean-workbench` advanced through two new commits after the previously recorded inner singular-slice closure.

Commit `9f9d835ba0cd80f22c42035bd2cd3a8c5d13fc5f` adds `RaisedBoxRealMajorantMiddleIntegral.lean`.  It formalizes the second exact real nested integral:

`∫_0^L (L-x)^(1-δ) dx = L^(2-δ)/(2-δ)`

for `δ<2`, with a physical specialization under the stronger raised-box hypothesis `δ<1`.

The proof uses Mathlib's affine reversal identity `intervalIntegral.integral_comp_sub_right` followed by the exact real-power integral theorem.  This is the post-`x3` middle-slice factor needed for the real majorant.  No Fubini/DCT conclusion is claimed yet.

Commit `c76324d6cf95338d19096fde06d5936ea6114426` promotes the new real-majorant chain into `GppVerify/FullConstruction.lean`: endpoint integrability, channel factorization, exact `x3` singular integral, and exact middle affine integral are now all in the common construction graph.

## CI state

The preceding head `0dba1bd6503d9ccc7d854762c6c2488f68af6c7b` had ordinary Build, axiom/scaffold audit, arithmetic CFT, arithmetic OS, sech endpoints, Gibbs thermodynamics, and Fisher cancellation green when checked; finite-core and full-construction lanes were still running.

Fresh CI for `c76324d6cf95338d19096fde06d5936ea6114426` has launched.  At the time of this record, finite-core is running and the principal build/audit/full-construction lanes are queued.  Therefore the new middle theorem is a pushed candidate, not yet called CI-certified.

## Exact next scalar theorem

After integrating `x3`, the singular-channel majorant has the form

`(S*x1)^(-δ) * (1-x1-x2)^(1-δ)/(1-δ)`.

The new middle theorem reduces the `x2` integral to an outer kernel proportional to

`(S*x1)^(-δ) * (1-x1)^(2-δ) / ((1-δ)(2-δ))`.

The next useful Lean closure is therefore the real outer Beta integral (equivalently the simplex singular-majorant integral), followed by the actual nested dominated-convergence theorem for `simplexMoment ε S T -> 1/6` as `ε -> 0+`.

Only after that DCT theorem is proved should the conditional residue assembly be promoted to the unconditional limits `ε I_8(ε) -> 1/6` and the shifted `μ^4` contribution `-> -1/6`.

## Other active fronts

No new RH/Weil claim: the principal-series/completed-zeta structural bridge is exact, but the missing theorem remains identification of the genuine prime-plus-Archimedean relative trace/Gram form with the Weil quadratic form and proof of its positivity.

No new chamber-convolution claim: higher Gamma chambers remain an algebraic positive recurrence hierarchy; repeated sech convolution has not been identified with those higher chambers.

Prime-gas strict one-parameter thermodynamics and the centered two-observable fluctuation determinant remain formal.  Genuine curved thermodynamic geometry still requires construction of a true second coupling, not reuse of the existing one-parameter family.

YM/gravity remains blocked at the honest physics frontier: explicit nonzero-μ fixed-loop-momentum Yang-Mills tree currents/numerators sewn over physical massive-vector polarizations.  Existing projector/state-count algebra is not substituted for this missing amplitude input.
