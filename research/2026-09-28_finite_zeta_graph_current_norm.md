# Finite zeta-graph metric: exact GCD taper and logarithmic norm of the von Mangoldt current

Date: 2026-09-28 America/Toronto / 2026-09-29 UTC
Status: exact finite zero-independent theorem and RH-boundary reduction. No RH claim.

This note was derived after the connected logarithmic Euler-current Hilbertization and after
the independent frontier audit corrected the provisional boundary-functional criterion.
The point is to obtain an explicit cutoff-dependent norm in the actual finite zeta gauge,
rather than another abstract carrier.

## 0. Analyticity correction carried forward

The earlier provisional slit-plane criterion was too weak as stated: local boundedness of a
parameter-dependent family of bounded functionals B_u does not imply that
u -> B_u[J(sqrt u)] is holomorphic. One must additionally prove analytic dependence of
u -> B_u (for example norm-holomorphy in a fixed dual space), or, preferably for finite
cutoffs, construct scalar functions m_N(u) that are themselves holomorphic on the slit
plane and prove local uniform boundedness plus Euler-region convergence.

The finite theorem below does NOT claim that this missing analyticity/reconstruction step
has been solved.

## 1. Finite half-density zeta graph

Fix N >= 1 and the divisor-closed set

  S_N = {1,2,...,N}.

On real coefficient vectors indexed by S_N define the half-density zeta synthesis matrix

  Z_N(n,d) = sqrt(d/n) 1_{d|n}.

Its inverse on S_N is the half-density Mobius matrix

  M_N(n,d) = mu(n/d) sqrt(d/n) 1_{d|n}.

This is exactly the finite matrix version of the already-formalized identities

  M_N Z_N = Z_N M_N = I.

Let

  D_N = diag(log n)

and let e_1 be the arithmetic vacuum delta_1.

The half-density von Mangoldt connection current from the vacuum is

  j_N := L_Lambda e_1,

so coordinatewise

  j_N(n) = Lambda(n)/sqrt(n).

Because logMul(e_1)=0, the exact gauge identity

  M D Z - D = L_Lambda

gives

  j_N = M_N D_N Z_N e_1.

Multiplying by Z_N and using Z_N M_N=I,

  boxed:
  Z_N j_N = D_N Z_N e_1.

Since

  (Z_N e_1)(n)=1/sqrt(n),

we get the completely explicit synthesized current

  boxed:
  (Z_N j_N)(n)=log(n)/sqrt(n).

This is already a useful cancellation statement: the irregular prime-supported von
Mangoldt vector becomes the smooth logarithmic number mode after zeta synthesis.

## 2. Exact zeta-graph Gram kernel

Define the positive finite Gram metric

  G_N := Z_N^T Z_N.

For d,e <= N,

  G_N(d,e)
   = sum_{n<=N: d|n, e|n} sqrt(d/n) sqrt(e/n).

Put l=lcm(d,e). The common multiples are n=l q with 1<=q<=floor(N/l), so

  G_N(d,e)
   = sqrt(de)/l * H_floor(N/l).

Using lcm(d,e) gcd(d,e)=de,

  boxed:
  G_N(d,e)
   = [gcd(d,e)/sqrt(de)] H_floor(N/lcm(d,e)),

where H_m=sum_{q<=m}1/q.

Thus the finite zeta-gauge metric is not merely the critical GCD/KMS kernel. It is the
critical kernel multiplied by an exact harmonic boundary taper:

  critical KMS/GCD factor = gcd(d,e)/sqrt(de),
  cutoff/Archimedean taper = H_floor(N/lcm(d,e)).

Normalize by H_N:

  Gtilde_N := G_N/H_N.

Then

  boxed:
  Gtilde_N(d,e)
   = gcd(d,e)/sqrt(de)
     * H_floor(N/lcm(d,e))/H_N.

For every FIXED d,e,

  Gtilde_N(d,e) -> gcd(d,e)/sqrt(de)

as N -> infinity.

But for indices growing with N, the harmonic taper is nontrivial and can be very small.
Therefore replacing the finite metric too early by the limiting pure GCD kernel discards
precisely a boundary effect that may matter for the RH reconstruction.

## 3. Exact norm of the full von Mangoldt current

By definition of the Gram metric and the synthesized-current identity,

  ||j_N||^2_{G_N}
   = j_N^T Z_N^T Z_N j_N
   = ||Z_N j_N||_2^2
   = sum_{n<=N} (log n)^2/n.

Therefore in the normalized graph metric,

  boxed:
  ||j_N||^2_{Gtilde_N}
   = [sum_{n<=N}(log n)^2/n]/H_N.

Since log n <= log N for n<=N,

  sum_{n<=N}(log n)^2/n
  <= (log N)^2 sum_{n<=N}1/n
  = (log N)^2 H_N.

Hence the exact zero-independent cutoff bound

  boxed:
  ||j_N||_{Gtilde_N} <= log N.

No prime number theorem, zero-free region, Mertens estimate, or RH input is used.

The current is therefore polynomial -- indeed linear -- in the logarithmic cutoff in the
canonical normalized finite zeta-graph/KMS metric.

## 4. Why this is stronger than the orthogonal prime-power L2 theorem

The orthogonal prime-power theorem showed that the internal current is Hilbert-valued on
the full open critical half-plane. That was a domain statement in a deliberately
orthogonalized carrier.

The present theorem uses the arithmetic zeta synthesis itself. Its Gram metric tends on
fixed coordinates to the critical TFD/KMS GCD metric already derived independently from
finite self-dual subgroup states. So the same logarithmic current is tame not only in an
auxiliary orthogonal carrier, but in the finite arithmetic graph geometry naturally tied
to Mobius inversion and KMS half-density.

Moreover, the exact harmonic taper keeps the finite boundary data that the pure limiting
GCD kernel forgets.

## 5. Dual formulation: the hard theorem is now a boundary-functional estimate

For any finite linear functional ell_N on the coefficient space,

  |ell_N(j_N)|
  <= ||ell_N||_{Gtilde_N^{-1}} ||j_N||_{Gtilde_N}
  <= (log N) ||ell_N||_{Gtilde_N^{-1}}.

Thus any COMPLETED prime-Archimedean boundary functional whose dual norm grows only
subexponentially in L=log N gives a subexponential scalar response. Polynomial growth in
L is more than enough.

Combined with the previously proved fixed-window vacuum-instability theorem, this suggests
the following precise load-bearing target:

  construct the zero-independent completed scalar reconstruction at cutoff N so that

  (a) the scalar response m_N(u) is holomorphic on the required slit domain after the pole
      and Archimedean cancellations are included at finite N;
  (b) on every compact slit-domain set its appropriate completed dual norm is
      exp(o(log N)) (a polynomial in log N would suffice);
  (c) in the Euler region m_N converges to the exact completed xi response.

Then the connected current contributes at most an extra log N factor, still exp(o(log N)),
and the prior normal-family / vacuum-instability argument can be applied.

This is a quantitatively sharper target than "prove a bounded all-ones functional."

## 6. Raw all-ones scalarization still fails -- this theorem does not hide it

Let 1 denote the raw coefficient-summing functional. In the G_N metric its dual vector is

  Z_N^{-T} 1 = M_N^T 1.

Its d-th coordinate is

  (M_N^T 1)(d)
   = sum_{m<=N/d} mu(m)/sqrt(m)

(up to the exact finite indexing convention).

For every d>N/2 only m=1 occurs, so this coordinate equals 1. Hence there are order-N
uncancelled boundary coordinates already before any delicate arithmetic estimate.

So the raw all-ones functional is NOT the desired completed dual state. The new norm bound
does not repair it. It proves instead that the prime current is tame and forces the
remaining construction to create genuine prime-Archimedean / Poisson cancellation before
scalar evaluation.

This agrees with the independent no-go: a quotient with the inherited Hilbert norm cannot
turn raw summation on all finite-support vectors into a bounded functional.

## 7. Geometric reading of the harmonic taper

The factor

  H_floor(N/lcm(d,e))/H_N

measures how many common-multiple layers of d and e remain before the ultraviolet cutoff N,
with harmonic weighting.

Interior arithmetic modes (fixed d,e while N grows) see the critical KMS/GCD metric.
Modes near the cutoff see a suppressed overlap.

This looks like the finite-volume/Archimedean boundary geometry of the divisor graph. It
should be retained when constructing the finite completed Schur/Poisson response. Taking
the infinite pure GCD kernel first may erase the very taper that regularizes the boundary
dual norm.

This is a new concrete reason to formulate the RH sewing theorem at finite N and only then
take the limit.

## 8. Formalization targets

Existing GPPVerify theorem:
- HalfDensityZetaGauge.lean already certifies MZ=ZM=I and MDZ-D=L_Lambda on finite
  divisor-closed sets.

Immediate finite core suitable for Lean:
1. specialize to S_N and e_1;
2. prove Z_N j_N = D_N Z_N e_1;
3. prove the norm identity
     ||Z_N j_N||^2 = sum_{n<=N}(log n)^2/n;
4. prove
     sum_{n<=N}(log n)^2/n <= (log N)^2 H_N
   for N>=1.

Second layer:
5. prove the Gram-entry formula with gcd/lcm and harmonic numbers;
6. package Gtilde_N positivity and the dual Cauchy-Schwarz estimate.

The finite norm theorem is exact and independent of the still-open scalar reconstruction.
