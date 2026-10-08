# Genuine prime-side Hilbert bound and the point-evaluation obstruction (2026-10-08)

Status: PROVED elementary/standard analytic identities; NO RH proof. Purpose: respond to Muse's valid objection that the Jacobi leakage and fixed-window equivalences supply no new arithmetic estimate.

## 1. A genuinely unconditional inequality from the *actual* one-channel coefficients

For sigma>1/2, define the finite von Mangoldt Dirichlet polynomial

  J_(sigma,N)(t) = sum_{2<=n<=N} Lambda(n) n^(-sigma) exp(-it log n).

Use the Besicovitch/Bohr mean-square norm, the completion of trigonometric polynomials under

  ||J||_B2^2 = lim_(T->infty) 1/(2T) int_(-T)^T |J(t)|^2 dt.

Orthogonality of distinct log n yields, for finite N, the exact Parseval formula

  ||J_(sigma,N)||_B2^2 = sum_(n<=N) Lambda(n)^2 n^(-2sigma).

Let B(sigma) be the N->infty limit. For sigma>1/2, the prime-power expansion proves

  B(sigma) = sum_p (log p)^2 p^(-2sigma)/(1-p^(-2sigma)) < infinity.

This is a genuine *bound* from the Euler prime coefficients, without invoking zeros or assuming RH. More sharply, since log zeta(s)=sum_(p,k>=1) p^(-ks)/k for real s>1,

  B(sigma) = (d^2/ds^2 log zeta(s))_(s=2sigma)
    - sum_p (log p)^2 p^(-4sigma)/(1-p^(-2sigma))^2,

so **0<B(sigma)<(log zeta)''(2sigma)**. The second term is positive and uniformly bounded as sigma approaches 1/2 from the right. Using the Laurent expansion of zeta at 1 gives

  B(1/2+eps) = 1/(4eps^2) + O(1)       (eps->0+).

Indeed the constant term equals (-2 gamma_1 - gamma_E^2) minus sum_p (log p)^2/(p-1)^2, with gamma_1 the first Stieltjes constant in the conventional alternating-sign expansion.

## 2. Adversarial F_theta control fails the same bound at the shifted midpoint

The zeta(s-theta) zeta(s+theta) logarithmic prime coefficients are
  Lambda_theta(n) = Lambda(n)(n^theta + n^(-theta)).
Consequently the very same Hilbert-energy functional equals

  B_theta(sigma) = B(sigma-theta) + 2B(sigma) + B(sigma+theta),

where B(u)=+infinity if u<=1/2. For theta>0 the necessary-and-sufficient finite-energy condition is

  B_theta(sigma)<infinity  iff  sigma>1/2+theta.

In particular for any eps>0 the one-channel current J_(1/2+eps) has finite energy,
but the F_theta current has **infinite** energy for every theta>=eps. When
0<theta<eps, B_theta(1/2+eps) grows as 1/[4(eps-theta)^2] as theta approaches eps from below. At theta=0 it is 4B(sigma), exactly the duplicated one-channel norm.

This is a quantitative prime-side separation that really *fails the shifted Euler control* and does not presuppose a zero. But it still does not impose RH.

## 3. Exact Poisson-semigroup compensation and its no-go

On the Bohr frequency basis exp(-it log n), the positive Poisson semigroup
  P_delta = exp(-delta |D_t|)
acts by P_delta exp(-it log n)=n^(-delta) exp(-it log n), i.e.
  P_delta J_sigma = J_(sigma+delta)
in B2 for sigma>1/2. Thus compensation is a positive-semigroup difference with

  ||(I-P_delta)J_sigma||_B2^2
     = B(sigma)-2B(sigma+delta)+B(sigma+2delta)
     >=0.

For every FIXED delta>0,
  ||(I-P_delta)J_(1/2+eps)||_B2^2 = 1/(4eps^2)+O(1).

Therefore **no fixed positive radial compensation (including delta=1/2 or 1) removes the critical B2 divergence**. Its favorable finite dyadic correction does not translate into a finite global critical-current norm.

## 4. Why the bound cannot be substituted for completed zero survival

B2 mean-square does not control evaluation at ANY fixed t: for distinct primes p_j,
  u_N(t)=N^(-1/2) sum_(j=1)^N exp[-i(t-t0)log p_j]
has ||u_N||_B2=1 but |u_N(t0)|=sqrt N ->infinity. This holds *on prime frequencies alone*.

Even for the exact one-channel J, PNT implies for every FIXED 1/2<sigma<1 and fixed real t,
  sum_(n<=N) Lambda(n)n^(-sigma-it)
      = N^(1-sigma-it)/(1-sigma-it) + o(N^(1-sigma))
as N->infinity: these pointwise partial sums diverge while their Bohr B2 energies stay bounded. The positive mean-square completion and the meromorphic analytic continuation of -zeta'/zeta are **different topological completions**.

The real missing theorem is an arithmetic, pole-subtracted *local* bound
on sums of Lambda(n)n^(-s) that is strong enough to pass across Re(s)=1
into Re(s)>1/2 and glue to the completed logarithmic derivative.
Classical PNT supplies o(N^(1-sigma)), not the necessary cancellation.
No implication from the proven B2 inequality to RH is asserted.

## 5. Actions and test
Propose Claude formalize finite Parseval and B_theta decomposition; don't label
them RH. Test a candidate "local evaluation bridge" against F_theta:
it must fail to continue its current at sigma<=1/2+theta.
This memo also answers Muse's challenge with an actual unconditional
X<=Y inequality and isolates exactly why that inequality falls short.


## 6. A stronger true inequality: sub-Gaussian prime-current concentration

This goes beyond norm equivalences to a probability upper bound directly from prime independence.
On the Haar prime torus, let Z_p be independent uniform unit complex numbers and

  X_p = (log p) p^(-sigma) Z_p / (1 - p^(-sigma) Z_p),  sigma>1/2.

This is the p-th Euler-local logarithmic prime current. Its Fourier series has no constant term, so E[X_p]=0, and by orthogonality

  E|X_p|^2 = (log p)^2 p^(-2sigma)/(1-p^(-2sigma)).

Consequently J_sigma := sum_p X_p converges in L2, and E|J_sigma|²=B(sigma) from §1. Set

  K(sigma) = sum_p (log p)^2 /(p^sigma-1)^2.

It is finite and satisfies K(sigma) ≤ R(sigma) B(sigma) with
  R(sigma) = (1+2^(-sigma))/(1-2^(-sigma)),
because |X_p|≤log(p)/(p^sigma−1) and for q=p^-sigma,
  [q²/(1−q)²] / [q²/(1−q²)] = (1+q)/(1−q) ≤ R(sigma).

Apply Hoeffding's lemma to the independent, centered and bounded real variables
Re X_p and Im X_p, separately, then pass to the L2 limit. If |J|>=u,
at least one of |Re J|, |Im J| is >=u/sqrt(2). The union bound yields

  **P_Haar(|J_sigma| >= u) ≤ 4 exp[-u²/(4 K(sigma))]
      ≤ 4 exp[-u²/(4 R(sigma) B(sigma))]**,  u>0.

This is an UNCONDITIONAL exponential-tail inequality based on the real Euler product, valid for every fixed sigma>1/2; with sigma=1/2+eps it has characteristic scale O(1/eps). It makes no statement about the actual zeta logarithmic derivative at a specified height t.

For a fixed finite set of primes, rational independence of their logarithms
(unique prime factorization) plus Kronecker-Weyl transfers the same
probability bound to the upper asymptotic density of real t along
the genuine arithmetic flow Z_p=p^(-it). No uniform in cutoff
equidistribution rate or localization at a prescribed zero ordinate follows.

For shifted F_theta, the prime variable becomes the sum of geometric
currents of radii p^(-(sigma-theta)) and p^(-(sigma+theta));
the L2 variance diverges when sigma<=1/2+theta. Hence the full
infinite-prime concentration theorem does not apply to the
two-channel control at the same sigma.

**Key boundary:** an exceptional set of Haar density zero can
still contain every individual ordinate of hypothetical off-line zeros.
The prime-current concentration inequality is a genuine bound,
but transferring it to deterministic point evaluations or the fully
completed Weil correlation is the new, necessary estimate. No RH claim.
