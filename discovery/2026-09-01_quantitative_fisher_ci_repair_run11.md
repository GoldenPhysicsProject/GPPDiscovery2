# Quantitative Fisher witness and CI dependency repair — 2026-09-01

Codex/GPT track only. No Claude material inspected.

## Exact finite Fisher lower witness

On `GPPVerify2/codex/lean-workbench`, the finite ordered Vandermonde energy

`E = sum_{i,j,k} p_i p_j p_k V(i,j,k)^2`

already admits the selected-term lower bound `W_ijk <= E` for pointwise nonnegative weights. Combining this with the exact mass-aware identity

`6 N_F = m0 E`,  where `m0 = sum_i p_i`,

and the elementary bound `p_i <= m0` gives the quantitative Fisher witness

`p_i^2 p_j p_k V(i,j,k)^2 / 6 <= N_F`.

This has been pushed as `FiniteFisherQuantitativeWitness.lean`. For an unnormalized countable weight sequence and a fixed triple whose weights/support values do not depend on the truncation, the left-hand side is prefix-independent once the prefix contains the triple. That is the form consumed by the existing `CountableFisherStrictWitness` limit theorem.

For the two-parameter number-Gibbs weights

`w_n(beta,eta) = n^{-beta} exp(-eta (log n)^2)`

with `eta > 0`, the intended arithmetic witness is the fixed three-state set corresponding to `n = 1,2,3` (subject to the repository's exact indexing convention when the specialization theorem is written). Its weights are strictly positive and the support values `log 1`, `log 2`, `log 3` are distinct. The remaining analytic input is summability of the raw moments through order four and, for a normalized Fisher determinant theorem, normalization of the infinite zeroth moment.

## CI failure and repair

The first smoke run for `FiniteFisherQuantitativeWitness.lean` failed before elaborating the new theorem. The actual failure was a stale dependency rebuild in `FiniteMomentFactorization.lean`: the proof of `triple_monomial_factorization` used commutative simp lemmas, and pinned Lean 4.19 canonicalized the two outer finite-sum binders differently, leaving an exponent-swapped triple-sum goal and introducing `sorryAx` downstream.

The factorization statement is mathematically unchanged. The proof was repaired by expanding finite products of sums with `Finset.sum_mul`, `Finset.mul_sum`, and associativity only, deliberately avoiding `mul_comm`/`mul_left_comm` in the simp set. CI must certify this repair before the quantitative Fisher theorem is treated as branch-certified.

## Scalar-box audit

The concrete raised-box module still contains the exact physical nested simplex moment, interior positivity of the Symanzik polynomial, pointwise regulator removal, and the one-channel majorant

`Q^{-epsilon} <= 1 + (S x1 x3)^{-delta}`

under the established positivity/simplex hypotheses. The live formal obstruction remains the almost-everywhere boundary-face bookkeeping plus nested interval dominated convergence. No new endpoint or Beta/Gamma estimate is required before `J_epsilon(S,T) -> 1/6`.

## Other active-front boundaries

The Gamma/Mehler-Fock/Wiener-Hopf chamber results remain valid Archimedean structure. No global prime-plus-Archimedean Weil quadratic-form identification or unconditional Weil positivity was obtained in this run.

Yang-Mills/gravity remains downstream of scalar regulator closure: the next honest amplitude object is the fixed-loop `D_s = 4`, nonzero-`mu` Yang-Mills tree-sewing numerator/state sum before higher generalized cuts or double-copy gravity are promoted.
