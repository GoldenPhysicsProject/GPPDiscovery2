# Codex run: scalar-aware Fisher/Vandermonde factorization

The Verify2 head `de3f7d4a5b6cba6078233ba98530986006488a83` failed the changed-Lean compilation gate again even though the source-sorry gate and setup stages passed. The recurring instability was isolated to the finite Fisher/Vandermonde identity proof rather than to the underlying mathematical identity.

## Structural repair

The prior proof expanded the weighted Vandermonde square into eighteen separable channels but then relied on finite-sum normalization to move integer coefficients such as 2 and 6 across three nested binders before `triple_monomial_factorization` could match. That is brittle under pinned Lean 4.19.

Verify2 now adds a scalar-aware factorization theorem

`triple_monomial_factorization_smul`

which proves directly that for any real scalar r,

sum_{i,j,k} r ((p_i x_i^a)(p_j x_j^b)(p_k x_k^c))
= r m_a m_b m_c.

The proof moves the same scalar through the three finite sums structurally and then invokes the already-repaired binder-preserving triple factorization theorem.

`FiniteFisherVandermondeIdentity.lean` was rewritten so every term in the weighted Vandermonde-square expansion is syntactically `r * channel`, with r in {1,2,6}. After distributing only addition/subtraction across the finite sums, every channel can be collapsed by the scalar-aware theorem without commutative simp reordering binders.

Current Verify2 head after the two commits: `f2a3e545a4fd5a79de880c82411d059c245aa5a5`.

## Mathematical target unchanged

The exact identity remains

E = m0 m2 m4 + 2 m1 m2 m3 - m2^3 - m0 m3^2 - m1^2 m4,

and therefore, using the existing bridge `6 N_F = m0 E`, the quantitative finite witness target remains

(p_i^2 p_j p_k / 6) [(x_i-x_j)(x_i-x_k)(x_j-x_k)]^2 <= N_F.

No axiom, sorry, or weakened theorem was introduced.

## Other frontiers

Scalar box: still blocked at the AE boundary-face bookkeeping plus nested interval dominated-convergence composition required for J_epsilon(S,T) -> 1/6. Existing pointwise convergence and majorant/integrability ingredients are not the blocker.

Yang-Mills/gravity: remains downstream of scalar regulator closure at the first honest fixed-loop Ds=4, mu != 0 tree-sewing numerator and state sum.

Principal-series / Weil: Archimedean positive-real half-density, Delta=2s, critical-line unitarity, Gamma/Mehler-Fock/Wiener-Hopf structure remain valid. The non-circular global prime-plus-Archimedean Weil-form identification and unconditional positivity remain open.

Prime/number thermodynamics: once the finite Fisher identity and quantitative witness are CI-green, specialize the fixed (1,2,3) witness to w_n(beta,eta)=n^{-beta} exp(-eta (log n)^2), prove the required countable moment summability, and pass the uniform lower bound through the existing countable strict-witness theorem.

No Claude material used.