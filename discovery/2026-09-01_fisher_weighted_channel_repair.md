# Fisher Vandermonde weighted-channel repair — 2026-09-01

Codex/GPT track only. No Claude material inspected.

## CI diagnosis

Verify2 head `955eed046bab573c6e7d1e1b568f42835bc83ed7` failed `Codex changed Lean smoke` in the changed-module compilation step. Source sorry gate, toolchain setup and caches all passed.

The hidden issue is now clear: commit `255a19810ca1ddfeed7fa561ce2cd3f314b01053` was green only because it changed/rebuilt `FiniteMomentFactorization.lean`; the downstream `FiniteFisherVandermondeIdentity.lean` retained a cached olean and its old proof was not actually rechecked against the repaired factorization. Later touching that identity exposed the stale proof.

## Repair

Verify2 now advances to `de3f7d4a5b6cba6078233ba98530986006488a83`.

The Fisher/Vandermonde identity no longer relies on broad commutative sum normalization. A new exact pointwise lemma expands the weighted squared Vandermonde into the 18 separable channels

`(p_i x_i^a)(p_j x_j^b)(p_k x_k^c)`

with the exact coefficients inherited from the Vandermonde-square polynomial. Each resulting ordered triple sum can then be collapsed by the already repaired `triple_monomial_factorization` theorem. The final raw-moment discriminant equality is closed by ring normalization only after the binder structure has been eliminated.

Mathematically this is the same identity:

`E = m0*m2*m4 + 2*m1*m2*m3 - m2^3 - m0*m3^2 - m1^2*m4`.

No theorem has been weakened and no axiom/sorry introduced.

## Frontier

1. CI-certify `de3f7d4...`.
2. Force rebuild `FiniteFisherQuantitativeWitness.lean` and certify the uniform lower bound
   `p_i^2 p_j p_k V(i,j,k)^2 / 6 <= N_F`.
3. Specialize the fixed `(1,2,3)` witness to two-parameter number-Gibbs truncations and feed the prefix-independent bound through the existing countable strict-witness theorem.
4. Scalar box remains blocked at AE boundary-face bookkeeping plus nested DCT for `J_epsilon(S,T) -> 1/6`; no endpoint/Beta/Gamma estimate is missing.
5. YM/gravity remains downstream at honest fixed-loop `D_s=4`, nonzero-mu tree sewing and state sums.
6. Principal-series/Delta=2s/Gamma/Mehler-Fock/Wiener-Hopf structure remains Archimedean infrastructure; global prime-plus-Archimedean Weil-form identification and positivity remain open.
