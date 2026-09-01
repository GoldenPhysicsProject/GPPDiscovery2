# Countable Fisher fixed witness and scalar DCT frontier

Date: 2026-09-01
Track: Codex/GPT only

## Verify2 advance

The finite quantitative Fisher witness at Verify2 commit `29f17d38863b4a672a33800e3edd329f7a25d51b` is changed-Lean smoke green.

A generic countable fixed-witness bridge was then added. For nonnegative weights `w : ℕ → ℝ`, observables `x : ℕ → ℝ`, and fixed indices `i,j,k`, the finite quantitative inequality gives every prefix containing those indices the same lower bound

\[
c_{ijk}=\frac{w_i^2w_jw_k}{6}
\big[(x_i-x_j)(x_i-x_k)(x_j-x_k)\big]^2.
\]

The new intended theorem packages this as an eventual prefix-independent bound and combines it with raw-moment summability through order four to obtain strict positivity of the countable mass-aware Fisher numerator whenever the three selected weights are positive and the three observable values are pairwise distinct.

This is the exact interface needed for the two-parameter number-Gibbs specialization: choose a fixed three-state arithmetic witness and prove the model-specific weight positivity and moment summability separately.

## CI regression surfaced

The first build of the new bridge (`3eeb6f23c01234faa8615187d3f84a29e862f22a`) correctly forced a previously cached dependency, `CountableFisherMomentLimit.lean`, to rebuild. That dependency had two stale Lean-4.19 proofs:

1. the `Fin N` raw-moment / `Finset.range N` bookkeeping bridge no longer closed under its old broad `simp` proof;
2. the passage of a lower bound through a limit used `le_of_tendsto`, which has the wrong inequality orientation for an eventual statement `c ≤ f N`.

The repair replaces the first proof by an explicit rewrite using `← Fin.sum_univ_eq_sum_range` and replaces the lower-bound limit arguments by `ge_of_tendsto`. The same orientation correction was applied to the strict-witness bridge itself. Current Verify2 head after these repairs: `8ef243c8fcb9e8f2a7e831d6763506deabeb8fab`. Its changed-Lean smoke was still running when this note was written, so this head is not yet recorded as certified.

No `sorry` was introduced; the source-sorry gate passed on the failed run.

## Scalar-box audit

The raised-box affine-simplex integration algebra is further closed than the old shorthand frontier suggested. `RaisedBoxSimplexNestedReduction.lean` already proves the exact nested-to-reduced identity and then

\[
I_\delta
=
B(1-\delta,3-\delta)\,B(1-\delta,2),
\qquad \delta<1,
\]

for the two-dimensional singular majorant after the spectator simplex coordinate has been integrated out. The file itself records that the remaining regulator theorem is dominated convergence for the original raised-box integrand, not another Beta/Fubini identity.

`RaisedBoxConcreteMoment.lean` already supplies the physical object

\[
J_\varepsilon(S,T)=\int_{\Delta_3}Q^{-\varepsilon},
\quad Q=Sx_1x_3+Tx_2x_4,
\]

interior pointwise convergence to 1, and the one-channel domination

\[
Q^{-\varepsilon}\le 1+(Sx_1x_3)^{-\delta}
\]

for `0 ≤ ε ≤ δ`, `0 < δ`. `RaisedBoxRealOuterIntegrability.lean` supplies the endpoint integrability certificate for the reduced real outer kernel when `δ<1`.

Therefore the genuine remaining scalar closure is the nested interval dominated-convergence implementation with almost-everywhere treatment of simplex boundary faces, followed by the already formalized zero-regulator volume identity to obtain `J_ε(S,T) → 1/6`.

## Other fronts / boundaries

No new global Weil/RH theorem was obtained. The positive-real half-density, principal-series / `Δ=2s`, completed-zeta response, Gamma/Mehler-Fock/Wiener-Hopf and chamber-convolution results remain Archimedean infrastructure; global prime-plus-Archimedean Weil-form identification and unconditional positivity remain open.

No new Yang-Mills or gravity numerator theorem was promoted. Honest fixed-loop `D_s=4`, nonzero-`μ` tree sewing/state sums remain downstream of scalar regulator closure.

No Claude material was inspected or used.
