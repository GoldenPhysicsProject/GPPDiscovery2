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

## CI failures and repairs

The first smoke run for `FiniteFisherQuantitativeWitness.lean` failed before elaborating the new theorem. The actual failure was a stale dependency rebuild in `FiniteMomentFactorization.lean`: the proof of `triple_monomial_factorization` used commutative simp lemmas, and pinned Lean 4.19 canonicalized outer finite-sum binders differently, leaving exponent-permuted triple-sum goals and introducing `sorryAx` downstream.

The factorization statement is mathematically unchanged. It was repaired by collapsing the three finite sums one binder at a time with ordered `Finset.mul_sum` / `Finset.sum_mul` rewrites. The repair commit `255a19810ca1ddfeed7fa561ce2cd3f314b01053` passed the changed-Lean smoke, and `triple_monomial_factorization` rebuilt without `sorryAx`.

Forcing a rebuild of the quantitative theorem then exposed a second stale dependency: `FiniteFisherVandermondeIdentity.lean`. Its old proof of `orderedVandermondeEnergy_eq_momentDiscriminant` relied on global expansion plus broad commutative simplification. With the repaired factorization rebuilt under Lean 4.19, that proof left a large ordered triple-sum identity and therefore reintroduced `sorryAx` into downstream Fisher theorems.

That identity was rewritten around five explicit raw-moment factorization channels `(0,2,4)`, `(1,2,3)`, `(2,2,2)`, `(0,3,3)`, and `(1,1,4)`, matching the exact discriminant

`6 (m0 m2 m4 + 2 m1 m2 m3 - m2^3 - m0 m3^2 - m1^2 m4)`.

The first CI run of that rewrite, commit `33498bface77f6cebb86f75d8c9457ad172803de`, failed at line 50 with `simp made no progress`. Importantly, the prerequisite `FiniteMomentFactorization`, `FiniteVandermondeExpansionKernel`, `FiniteVandermondeEnergy`, and `FiniteFisherMomentBridge` modules all rebuilt successfully without `sorryAx`; the failure occurred only in the sum-distribution normalization inside `orderedVandermondeEnergy_eq_momentDiscriminant`.

That brittle `simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib]` step has now been replaced by recursive `simp_rw` distribution. The repair is commit `c49615e2cd1302e34079cb95b3cda976d4db7115`; its changed-Lean smoke is running. Until it passes, and `FiniteFisherQuantitativeWitness.lean` is force-rebuilt afterward, the quantitative lower witness remains mathematically derived and present on the branch but is not yet called CI-certified.

## Scalar-box audit

The concrete raised-box module still contains the exact physical nested simplex moment, interior positivity of the Symanzik polynomial, pointwise regulator removal, and the one-channel majorant

`Q^{-epsilon} <= 1 + (S x1 x3)^{-delta}`

under the established positivity/simplex hypotheses. The live formal obstruction remains the almost-everywhere boundary-face bookkeeping plus nested interval dominated convergence. No new endpoint or Beta/Gamma estimate is required before `J_epsilon(S,T) -> 1/6`.

## Other active-front boundaries

The positive-real principal-series dictionary still formally separates ordinary inversion `s -> 1-s` / celestial shadow `Delta -> 2-Delta` from the anti-linear Weil reflection `s -> 1-conj(s)`. On the critical axis the Weil reflection fixes `s`, whereas inversion becomes conjugation. This distinction remains essential: no celestial-shadow positivity statement has been identified with the global Weil quadratic form.

The Gamma/Mehler-Fock/Wiener-Hopf chamber results remain valid Archimedean structure. No new spectral theorem was added in this run, and no global prime-plus-Archimedean Weil quadratic-form identification or unconditional Weil positivity was obtained.

Yang-Mills/gravity remains downstream of scalar regulator closure: the next honest amplitude object is the fixed-loop `D_s = 4`, nonzero-`mu` Yang-Mills tree-sewing numerator/state sum before higher generalized cuts or double-copy gravity are promoted.
