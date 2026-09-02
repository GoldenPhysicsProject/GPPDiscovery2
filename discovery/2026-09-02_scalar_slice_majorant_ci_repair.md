# 2026-09-02 scalar slice-majorant CI repair

## Verify2 state entering the run

`GPPVerify2:codex/lean-workbench` head was `4f1f866aa2a6a70d097091110fe3802a716b5c8e`, containing the first assembled inner interval dominated-convergence theorem for the raised scalar box.

Changed-Lean run `33587060991` failed before compiling that theorem itself. The failure was isolated to its newly exposed dependency `RaisedBoxRealMajorantSlice.lean`; source-sorry gating and all prior scalar dependencies passed.

## Exact failure

Two interface defects were present in `RaisedBoxRealMajorantSlice.lean`:

1. `channel_neg_rpow_factor` rewrote associativity in the wrong direction before applying `Real.mul_rpow`, leaving a target already in the exact form expected by `Real.mul_rpow` but no matching `a * (b * c)` subterm.
2. `channel_inner_intervalIntegrable` attempted to use `IntervalIntegrable.congr` as if it took pointwise binders. In this Mathlib version the resulting goal is an AE equality on `volume.restrict (uIcc 0 L)`.

The audit also exposed a genuine mathematical omission: the theorem claimed the factorization-based interval result for arbitrary real `L`, but the proof requires `x3 >= 0` throughout the integration interval. Therefore the correct theorem needs `0 <= L`. This is satisfied on the physical simplex slice because `L = 1 - x1 - x2 > 0`.

## Repair pushed

Verify2 commits:

- `9eef95d295f3b3544438e1ec4c53cab2fca5800b`: remove the spurious associativity rewrite, add the essential hypothesis `0 <= L`, and construct the AE congruence with `filter_upwards` over `uIcc 0 L`.
- `aa276b9ae4b20e665f46abaebe240e1fcd2c833b`: propagate `hL.le` from the strict simplex-base condition into `RaisedBoxInnerDCT.inner_interval_tendsto_one`.

The repaired slice theorem is now mathematically honest:

`delta < 1`, `S >= 0`, `x1 >= 0`, `L >= 0` imply interval integrability of

`x3 |-> (S * x1 * x3)^(-delta)` on `[0,L]`.

## Active scalar frontier

If changed-Lean passes `aa276b9...`, the next local obligation remains AE strong measurability of the concrete `Real.rpow` integrand on the restricted inner interval. Once that is discharged, the first inner DCT theorem becomes unconditional and can be propagated through the middle and outer simplex integrals toward

`J_epsilon(S,T) -> 1/6` as `epsilon -> 0+`.

## Other fronts retained

- Number thermodynamics: strict normalized Fisher/covariance determinant is already established for arbitrary real beta with eta > 0. Next non-algebraic step is termwise differentiation of the quadratically confined partition sum and Hessian = covariance.
- Principal series / zeta: Delta = 2s, critical-line principal-series structure, and completed-zeta response remain local/Archimedean facts. No global Weil positivity promotion.
- Spectral salvage: exact Gamma/Mehler-Fock/Wiener-Hopf/chamber recurrence and positivity remain salvageable mathematics; no new chamber-convolution theorem was claimed this run.
- Yang-Mills/gravity: honest Ds=4, mu != 0 state sewing remains downstream of scalar regulator closure; no numerator sectors were assumed away.

No Claude material was inspected or used.
