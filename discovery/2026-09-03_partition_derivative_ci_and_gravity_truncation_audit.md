# 2026-09-03 — partition derivative CI repair and gravity truncation audit

## Scope
Codex/GPT track only. No Claude workspace, branch, notes, or records inspected.

## Prime-gas partition differentiation

The first candidate countable-interchange theorem for the quadratically confined partition function,

\[
Z(\beta,\eta)=\sum_{n\ge 0} e^{-\beta L_n-\eta L_n^2},\qquad L_n=\log(n+1),\quad \eta>0,
\]

aims to prove

\[
\partial_\beta Z(\beta,\eta)
=\sum_{n\ge0} -L_n e^{-\beta L_n-\eta L_n^2}.
\]

Full Build #1999 passed on the initial candidate because the new standalone module was not in the root import graph, while direct changed-Lean smoke #853 failed. The proof was rewritten into the explicit `g/g'` pattern used by already-certified `tsum` differentiation files. Direct smoke #854 then exposed three concrete local proof defects, rather than a failure of the analytic strategy:

1. the neighborhood lower bound `-(|β|+1) ≤ b` was not discharged by the original `linarith` call;
2. the guessed helper name `numberLogEnergy_nonneg` does not exist;
3. the derivative norm was already rendered as an absolute value, so the attempted `Real.norm_eq_abs` rewrite had no target.

These were repaired at Verify2 commit `228f35f51d7c6c918f9ceeab196f0b3d30e60d57` by an explicit order chain from `neg_abs_le`, reuse of the certified `logEnergy_nonneg` after unfolding the number-energy definition, and direct absolute-value normalization.

The analytic architecture remains sound: exact term derivatives + the global completing-the-square envelope + exponent-2 logarithmic-moment summability feed pinned Mathlib's `hasDerivAt_tsum_of_isPreconnected` theorem. Certification remains pending until the direct smoke on the repair is green.

## Scalar raised-box regulator

The scalar regulator front remains at the final outer-DCT assembly. Fixed-`x_1` product integrability, Fubini, physical nested-coordinate conversion, middle convergence, and the outer norm majorant are already separately certified. The remaining task is to package a.e. outer measurability/convergence and domination on `[0,1]`, treating the degenerate endpoints as null-set bookkeeping, then identify the zero-regulator value with simplex volume `1/6`.

## Gravity source correction

A focused-manuscript passage attempts to transfer the one-loop `no-triangle/no-bubble` property of maximally supersymmetric `N=8` supergravity to pure Einstein gravity by truncating superpartners. That inference is not valid. The no-triangle statement is a special cancellation statement for the full `N=8` state sum; deleting superpartners changes the state sum and does not preserve those cancellations automatically. Literature on pure Einstein gravity finds improved cancellations, but explicitly distinguishes them from the additional supersymmetric cancellations of `N=8`.

Required correction: do not use `N=8 -> pure gravity by truncation` as a proof that pure-gravity one-loop amplitudes are box-only. Any pure-gravity box/triangle/bubble statement must be derived from the actual pure-gravity cuts or cited amplitude decomposition. This strengthens the existing rule that gravity double-copy/generalized-cut claims remain downstream of an honest amplitude-level sewing derivation.

## Principal-series / Weil boundary

No RH promotion. The exact local dictionary `Delta=2s`, critical-line/half-density unitarity, completed-zeta phase response, and local Gamma/Wiener-Hopf positivity remain separate from the unresolved global requirement: positivity of the actual completed prime-plus-Archimedean Weil quadratic form on a concrete admissible transform class, together with the finite pair-support interpolation property for that same class.

## Spectral / chamber boundary

The elementary kinematic weight-shift ODE and integer Gamma/Wiener-Hopf hierarchy remain certified. The continuous Gamma-chamber Fourier law and convolution semigroup remain discovery-level until the arbitrary-positive-parameter Barnes/Fourier-Gamma transform and Fourier uniqueness are formalized.

## Next executable targets

1. Get the repaired beta `tsum` differentiation theorem direct-smoke green; normalize its derivative to `-M1`; mirror the proof in `eta` using a positive neighborhood and moment order 2.
2. Assemble the final scalar outer dominated-convergence theorem to `simplexMoment -> 1/6`.
3. Replace the invalid pure-gravity truncation sentence in the manuscript/source correction queue; derive pure-gravity/YM cut content only from actual tree currents and physical projector sewing.
