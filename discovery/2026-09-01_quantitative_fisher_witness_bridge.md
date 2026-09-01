# Quantitative finite Fisher witness bridge — 2026-09-01

Codex/GPT track only. No Claude material inspected or used.

## New formal step

Verify2 `codex/lean-workbench` now contains a quantitative strengthening of the finite Vandermonde witness theorem:

For nonnegative finite weights `p` and any chosen ordered triple `i,j,k`,

`p_i p_j p_k [(x_i-x_j)(x_i-x_k)(x_j-x_k)]^2 <= E(p,x)`,

where `E` is the full ordered finite Vandermonde energy.

This is stronger than the previous theorem `E>0` from one positive distinct triple. The selected witness has a fixed numerical value and remains a lower bound when additional nonnegative support points are appended. This is the exact property needed to prevent strictness from disappearing in a countable limit.

Verify2 commit: `a136ab75d68b45bd3f23a8c6da59dc04ed69bb28`.

## Countable Fisher interface audit

`CountableFisherStrictWitness.lean` already proves the topological half in the needed form: any eventually uniform lower bound `c` on finite-prefix mass-aware Fisher numerators transfers to the infinite numerator, and `c>0` gives strict positivity. Therefore the remaining countable number-Gibbs task is constructive rather than topological.

The ordinary one-parameter zeta-Gibbs model is already stronger still: `ZetaGibbsTwoObservableStrict.lean` proves strict countable covariance determinant positivity directly from the first three states. Do not describe that model as awaiting countable strictness.

The unfinished application is the two-parameter number-Gibbs family

`w_n(beta,eta) = n^(-beta) exp(-eta (log n)^2)`

(or the zero-indexed equivalent convention used by a formal module once installed).

For this family the next Lean bridge should convert the fixed three-state Vandermonde term into an eventual lower bound for the finite `fisherNumerator`, then feed it to `fisherNumerator_infinite_pos_of_eventually_partial_ge` after proving raw-moment summability through order four.

## Exact lower-bound algebra to formalize next

The existing identity is

`6 N_F = m_0 E`,

with `N_F` the division-free Fisher numerator and `E` the ordered Vandermonde energy.

For a chosen witness triple, let

`W_ijk = p_i p_j p_k [(x_i-x_j)(x_i-x_k)(x_j-x_k)]^2`.

The new theorem gives `E >= W_ijk`. If one also uses `m_0 >= p_i > 0`, then

`6 N_F = m_0 E >= p_i W_ijk > 0`,

so

`N_F >= p_i W_ijk / 6`.

For a fixed triple already present in every sufficiently large prefix, the right-hand side is independent of the prefix. This supplies the required uniform `c>0`.

A sharper symmetric mass lower bound is unnecessary; any one positive fixed weight is enough.

## Scalar-box audit

The concrete raised-box module already contains the physical nested simplex moment, interior pointwise regulator convergence, and the one-channel domination by `1 + (S x1 x3)^(-delta)`. The simplex measure bridge already contains the inner affine-slice and reduced outer interval-integrability certificates. The missing scalar theorem remains the nested almost-everywhere boundary handling plus iterated dominated-convergence composition yielding

`J_epsilon(S,T) -> 1/6`.

No endpoint/Beta/Gamma estimate is missing.

## Other fronts

- YM/gravity: still downstream of scalar regulator closure; next honest target remains the fixed-loop `D_s=4`, nonzero-`mu` Yang-Mills tree-sewing numerator/state sum before generalized cuts or double copy.
- Principal-series/Weil: local half-density, `Delta=2s`, critical-line unitary, Gamma/Mehler-Fock/Wiener-Hopf structure remain valid; no global prime-plus-Archimedean Weil quadratic-form identification or positivity was obtained here.
- Spectral chamber results remain on the corrected convolution interpretation: the Mehler-Fock density is the spectral-space generator, while powers of `sech` occur on the Fourier side; no repeated-sech x-space claim is reinstated.

## CI

At the time of this record, GitHub Actions had not yet registered a workflow run for Verify2 commit `a136ab75...`. Treat the new Lean theorem as pushed but not CI-certified until the changed-Lean smoke run appears and passes.
