# Fisher–Vandermonde CI repair — 2026-09-01

Codex/GPT track only. No Claude material inspected.

## Verify2 state

`GPPVerify2/codex/lean-workbench` at the start of this run was `c49615e2cd1302e34079cb95b3cda976d4db7115` (`Repair Fisher Vandermonde sum normalization`). Its `Codex changed Lean smoke` run `33486867708` completed with failure in the changed-Lean compilation step. Source-sorry gate, checkout, elan, caches, and mathlib cache all passed.

The failing module remains `GppVerify/RiemannHypothesis/FiniteFisherVandermondeIdentity.lean`; the mathematical theorem statement is unchanged:

`orderedVandermondeEnergy p x = momentDiscriminant (rawMoment p x 0) ... (rawMoment p x 4)`.

The previous attempted proof introduced five explicit triple-moment factorization channels and then used `simp_rw` over `Finset.sum_add_distrib` / `Finset.sum_sub_distrib`; that normalization remained brittle under pinned Lean 4.19.

## Repair pushed

Restored the direct algebraic proof pattern that was present on `main`:

1. unfold `orderedVandermondeEnergy`, `momentDiscriminant`, and `rawMoment`;
2. rewrite the pointwise squared Vandermonde by `vandermonde_sq_expansion`;
3. normalize finite sums using `Finset.sum_add_distrib`, `Finset.sum_sub_distrib`, `Finset.sum_mul`, and `Finset.mul_sum`;
4. close the resulting polynomial identity with `ring`.

This avoids `simp_rw`'s no-progress failure and does not alter the mathematics.

New Verify2 commit: `955eed046bab573c6e7d1e1b568f42835bc83ed7` (`Restore robust direct Vandermonde sum factorization`). CI status immediately after push is pending; no certification claim yet.

## Active frontier

Once this identity is green, force-rebuild `FiniteFisherQuantitativeWitness.lean`, whose target lower bound is

`(p i)^2 * p j * p k / 6 * ((x i - x j)*(x i - x k)*(x j - x k))^2 ≤ fisherNumerator(...)`.

That gives a prefix-independent positive lower bound from the fixed `(1,2,3)` number-Gibbs witness and can be passed through the already-existing countable strict-witness bridge.

Scalar-box status is unchanged: the remaining gap is the almost-everywhere boundary-face bookkeeping plus nested interval dominated-convergence composition proving `J_ε(S,T) → 1/6`. YM/gravity remains downstream at honest fixed-loop `D_s=4, μ≠0` tree sewing. Archimedean principal-series / Gamma / Mehler–Fock / Wiener–Hopf results remain intact; no global Weil-positivity or RH claim is promoted.
