# Codex/GPT active-front rotation — 2026-09-03

Research separation preserved: this run used only Codex/GPT repositories and records. No Claude research, branches, notes, or workspace were inspected.

## Scalar box regulator

The previous outer nested norm bound is now certified on Verify2 head `e7bdce51ec90d60ecfba8dccc45e387ec65d5c00`: changed-Lean smoke #851 and full Build #1997 both passed.

A new formal module, `RaisedBoxOuterNestedMeasurability.lean`, was pushed as `6d27869239b3a1df53d72c8aa20a32801b271c0d`. It transfers the already-certified strong measurability of the full-simplex product fiber through the physical nested-coordinate bridge and proves a.e. strong measurability of

`x1 ↦ ∫ x2 in 0..(1-x1), ∫ x3 in 0..(1-x1-x2), Q^(-ε)`

on the strict outer interval `Ioo 0 1`. This is the missing measurability input for the final outer dominated-convergence assembly; the endpoints are null and require only endpoint bookkeeping.

## Prime-gas thermodynamics

The first actual countable differentiation theorem was pushed as `608d6e8e1b5e2d325203d99361d7b701a07abfcf` in `NumberGibbsQuadraticPartitionDerivatives.lean`.

At fixed `η > 0`, it applies Mathlib's `hasDerivAt_tsum_of_isPreconnected` on an open neighborhood of arbitrary `β`, using:

1. the exact pointwise summand derivative `∂β w = -L w`;
2. the all-index completing-the-square envelope by the exponent-2 zeta moment;
3. summability of the exponent-2 first log moment;
4. summability of the partition series at a base point.

Candidate conclusion:

`d/dβ Z(β,η) = Σ_n w_{β,η}(n)(-L_n)`.

This is the first promotion from local term derivatives to the actual infinite partition function. CI certification is pending at the time of this record.

## Principal series / Weil

No RH promotion. `WeilPolynomialInterpolation.lean` remains the correct reduction: finite pair-support interpolation follows algebraically from one nonvanishing seed transform plus closure of the admissible transform class under polynomial spectral multipliers. The unsolved analytic obligations remain positivity of the genuine completed prime-plus-Archimedean Weil form for one concrete admissible class, plus verification that the same class satisfies the seed/polynomial-closure requirements.

## Spectral / Mehler-Fock / Wiener-Hopf / chambers

No status inflation. The exact elementary kinematic weight-shift ODE and integer Gamma/Wiener-Hopf hierarchy are Lean-certified. The continuous Gamma chamber convolution semigroup remains conditional on the arbitrary-positive-parameter Barnes/Fourier-Gamma transform and Fourier uniqueness.

## Yang-Mills / gravity

No numerator was reverse-engineered. The next honest gate remains the full `Ds = 4`, nonzero-μ color-ordered two-massive-vector tree current, both physical projectors, and derivation of FDH sewing coefficients with coupling/color/orientation/normalization retained. Generalized cuts, higher loops, and gravity double copy remain downstream.

## Next

1. certify or repair the strict outer nested measurability module;
2. certify or repair the first `β` derivative of the quadratically confined partition sum;
3. assemble the outer DCT to `simplexMoment ε S T → 1/6`;
4. promote the `η` derivative and Hessian entries after the first countable-interchange pattern is green.
