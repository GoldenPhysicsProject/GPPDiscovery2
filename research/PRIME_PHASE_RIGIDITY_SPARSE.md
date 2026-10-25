# Prime-clock rigidity, sparse-infinite zero invariance, and reflection completion

Golden Physics Project — Codex mathematical discovery lane, 2026-10-25.

**Scope.** Exact classical analysis of Daniel's prime-circle slowdown thought
experiment. Complements the October 15 Hurwitz zero-free Euler-limit obstruction,
the October 25 finite-local slowdown calculation, and the existing principal-series
half-density representation. Neither this note nor its reproducibility script proves RH.

## Theorem 1 — real-dilation clock rigidity

Write the positive rational group as a free multiplicative abelian group on the
primes. For arbitrary real rates `alpha_p`, define the completely additive
frequency on positive rationals

`lambda(prod_p p^v_p) = sum_p v_p alpha_p log(p)`.

Then `lambda` extends to a **continuous additive character into R** of
`(R_{>0}, multiplication)` in its usual real topology if and only if all
`alpha_p` are one common constant `c`. The only extension is `c log(x)`.

**Proof.** Under `x=exp(u)`, a continuous homomorphism from `(R,+)` to
`(R,+)` is `u -> c u`. Evaluating at each prime gives `alpha_p log(p)
= c log(p)`, hence `alpha_p=c` for all p. Conversely `c log(x)` is a
continuous extension. QED.

**Explicit discontinuity certificate.** If `alpha_p != alpha_q`, then
`log(p)/log(q)` is irrational (otherwise distinct prime powers would be
equal). Its rational convergents `b_k/a_k` yield positive integers
`a_k,b_k -> infinity` with

`a_k log(p) - b_k log(q) -> 0`.

Thus `r_k=p^a_k/q^b_k -> 1` in the ordinary real topology, whereas

`lambda(r_k) = (alpha_p-alpha_q) a_k log(p)
                 + alpha_q [a_k log(p)-b_k log(q)]`

diverges in magnitude. This gives a direct, quantitative obstruction to
identifying independently slowed prime clocks with one continuous real Haar
dilation time. For p=2, q=3, `alpha_2=0, alpha_3=1`, the rational
`2^1054/3^665` has `log(r) = -4.36541e-5` while its altered frequency is
`-730.577...`. The attached stdlib code also generates later convergents.

**Topology caveat.** Independent rates are perfectly valid as an abstract
one-parameter flow in the product prime torus, with its product topology,
or as a homomorphism of the discrete rational group. This theorem concerns
the *usual real topology* inherited by `Q_{>0}` from `R_{>0}`. It does not
preclude a nontrivial Hilbert-space coupling using the compact idelic
character sectors; it prevents equating such a flow, without extra
machinery, to one real principal-series dilation character.

## Theorem 2 — freezing infinitely many sparse primes preserves zeros

Let `P` be an (even infinite) set of primes satisfying

`sum_{p in P} p^(-epsilon) < infinity` **for every** `epsilon>0`.

Fix `sigma_0=1/2` and any arbitrary sequence `alpha_p in [0,1]` for
`p in P`; one may set **all** `alpha_p=0`. In `Re(s)>0` put

`s_p' = sigma_0 + alpha_p (s-sigma_0)`,

`M(s) = product_{p in P} (1-p^(-s))/(1-p^(-s_p'))`.

Then `M` is holomorphic and nowhere zero throughout `Re(s)>0`.
Consequently `zeta_P(s)=zeta(s) M(s)` is meromorphic there and has
**exactly the same zeros with the same multiplicities in the critical
strip** as `zeta(s)`. Its pole at `s=1` is not canceled.

**Proof.** On each compact K in the right half-plane let
`delta=min_{s in K} Re(s)>0` and `d=min(delta,1/2)>0`. For every
`alpha_p in [0,1]`,

`Re(s_p')=(1-alpha_p)/2+alpha_p Re(s) >= d`.

Both `p^(-s)` and `p^(-s_p')` have modulus at most `p^(-d)`.
For sufficiently large p, the analytic logarithm defined by the power
series `log(1-z)=-sum_{k>=1}z^k/k` obeys

`|log(1-p^(-s))-log(1-p^(-s_p'))| <= 4 p^(-d)`.

The right side is summable over P by hypothesis, uniformly on K.
Therefore the log-correction converges locally uniformly to a holomorphic
function L(s) and `M(s)=exp(L(s))` is everywhere nonzero. Each omitted
finite prime factor is also nonzero because `Re(s),Re(s_p')>0`.
Multiplication by a nonvanishing holomorphic function preserves zero
orders. QED.

**Fully explicit infinite P.** By Bertrand's postulate choose a prime
`p_n` with `2^(n^2)<p_n<2^(n^2+1)` for each integer `n>=1`.
These primes are distinct. For every epsilon>0,

`sum_n p_n^(-epsilon) <= sum_n 2^(-epsilon*n^2) < infinity`.

This gives an actual infinite set of frozen prime circles with *all*
nontrivial zeta zeros fixed. It is a sparse-set construction, not a
positive-density or all-prime freezing theorem. For Re(s)>1 the modified
function also has the corresponding absolutely convergent, locally changed
Euler product. It need not be a standard Dirichlet L-function.

## Theorem 3 — exact reflection completion does not rescue phase localization

On the full open critical strip `0<Re(s)<1`, define

`H(s) = M(s) M(1-s)`,  `Xi_P(s)=xi(s) H(s)`.

Theorem 2 ensures H is holomorphic and nowhere zero in the strip. Since
the speeds are real, `M(conj(s))=conj(M(s))`. Therefore

- `H(1-s)=H(s)` (the exact completed reflection symmetry);
- `H(conj(s))=conj(H(s))` (real type);
- `H(1/2+it)=|M(1/2+it)|^2>0` for every real t;
- `Xi_P(1-s)=Xi_P(s)`, and **every strip zero of Xi_P is a zero of xi,
  with the same multiplicity**, and conversely.

Let `r_p=p^(-1/2)`. On the line, for any rates `alpha_p in [0,1]`,

`prod_{p in P} ((1-r_p)/(1+r_p))^2
   <= H(1/2+it) <=
 prod_{p in P} ((1+r_p)/(1-r_p))^2`.

Both bounding products are finite, strictly positive, and independent
of t, because `sum_{p in P} r_p<infinity`.

In the completely frozen case `alpha_p=0`, each symmetrized factor on
the line is exactly

`|1-p^(-1/2)*exp(-it log p)|^2 / (1-p^(-1/2))^2`.

Hence even a **functional-equation-respecting, positive, globally bounded
critical-line reweighting of infinitely many prime-circle amplitudes**
does not locate or dislodge any zero. No claim is made that Xi_P remains
entire outside the strip, that its Fourier theta density is positive, or
that its Euler coefficients satisfy genuine arithmetic purity axioms.

## Research interpretation and proof boundary

1. Independent prime speeds are mathematically legitimate on the abstract
   prime torus, but cannot be a single continuous real principal-series
   dilation clock unless they are all equal. This distinguishes compact
   character-sector dynamics from the real Mellin/Haar half-density axis.
2. Even an infinite sparse set of frozen primes can change local Euler
   amplitudes without changing ANY critical-strip zeros. Merely naming an
   infinity of circles, plus reflection symmetry and line positivity of a
   scalar multiplier, is insufficient to derive RH.
3. Theorem 2 is a constructive special case of the pre-existing October 15
   Hurwitz observation: a locally uniform nowhere-zero holomorphic Euler
   counterterm cannot create zeros. These results do **not** say that an
   arbitrary all-prime deformation preserves zeros. Non-summable deformations
   may fail to converge, develop singular factors, alter arithmetic data,
   or produce genuinely different completed L-functions.
4. The outstanding proof obligation is a source-built **zero-independent**
   prime–Archimedean operator or cohomology with a coercive/global Hilbert
   constraint that discriminates genuine zeta from positive-theta shifted
   `F_theta`, Davenport–Heilbronn and Epstein controls. Character-sector
   purity and the correct boundary/Archimedean completion remain necessary
   checks, not established sufficient conditions.

## Reproduction

`python research/prime_phase_rigidity_sparse.py`

`python -m unittest discover -s tests -p 'test_prime_phase_rigidity_sparse.py' -v`

The code tests finite identities and generates Diophantine witnesses. Infinite
normal convergence and the reflection identities are established by the
proofs above, not extrapolated from finitely many numerical samples.
