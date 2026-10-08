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


## 7. A deterministic height-aspect inequality with increasing arithmetic cutoff

The preceding Haar/Besicovitch average takes height T->infinity at fixed
coefficient cutoff N. We can make N grow linearly with T, with
**unconditional deterministic control**, by applying the classical
Montgomery--Vaughan Dirichlet-polynomial mean value theorem:

For arbitrary a_n and any interval I of length T,
  int_I |sum_(n<=N) a_n n^(-it)|² dt
    = T sum_(n<=N)|a_n|² + O(sum_(n<=N) n |a_n|²),
with absolute implied constant. Set N=floor(T), a_n=Lambda(n)n^(-sigma).
For each fixed 1/2<sigma<1, the PNT and partial summation give

  sum_(n<=T) n Lambda(n)² n^(-2sigma)
       = O_sigma(T^(2-2sigma) log T),
  sum_(n>T) Lambda(n)² n^(-2sigma)
       = O_sigma(T^(1-2sigma) log T).

Hence the genuine quantitative prime-to-physical-height inequality is

  **1/T int_T^(2T) |sum_(n<=T) Lambda(n)n^(-sigma-it)|² dt
     = B(sigma) + O_sigma(T^(1-2sigma) log T).**

This is an actual deterministic estimate with a growing arithmetic cutoff,
valid for every sigma>1/2 (formula and stated rate for 1/2<sigma<1).
Because 1-2sigma<0, the error decays. It uses the actual one-channel
von Mangoldt coefficients, not any zero hypothesis.

Compare this height aspect T~N to the fixed-height regime: for each
fixed t and fixed 1/2<sigma<1, PNT gives
  J_(sigma,N)(t) ~ N^(1-sigma-it)/(1-sigma-it),
whose modulus diverges as N^(1-sigma). The limits N->infty and
T->infty thus DO NOT commute. This makes precise why the genuine
height-mean inequality cannot rule out a specific off-line zero.

Ref: classical Montgomery--Vaughan mean-value theorem, e.g. Goldston
and Gonek "Mean value theorems for long Dirichlet polynomials and
tails of Dirichlet series" (1997). Need no new conjectures.


## 8. Exact micro-height prime-pair kernel and suppression of local Hecke returns

For H>0, T real and finite N, exact integration (no averaging theorem) gives

  I(T,H;N,sigma) = 1/H int_T^(T+H)|J_(sigma,N)(t)|² dt
   = sum_(n,m<=N) Lambda(n)Lambda(m)/(nm)^sigma
       * exp[-i(T+H/2)log(n/m)]
       * sinc[(H/2)log(n/m)],

with sinc(y)=sin(y)/y. The **off-diagonal** consists of correlations
between distinct n,m, and H much smaller than N admits many n,m with
|n-m| ≲ N/H. These are genuine cross-prime correlations and are not
controlled by local Hecke recurrences.

Separate only pairs with n=p^k and m=p^l from the SAME prime p, k≠l.
Their average-integral factor is at most
  2/(H |k-l| log p).
For the complete infinite-prime same-p portion (absolutely summable
under this bound for sigma>1/2), the total offdiagonal magnitude obeys

  **|Off_sameprime| ≤ C_sigma/H**, where
  C_sigma =
    4 sum_p (log p) * [p^(-2sigma)/(1-p^(-2sigma))]
      * [-log(1-p^(-sigma))] < infinity.

Proof: write q=p^-sigma, then
  sum_{k,l>=1,k!=l} q^(k+l)/|k-l|
   = (2q²/(1-q²)) sum_{h>=1}q^h/h
   = (2q²/(1-q²))[-log(1-q)].
Multiply by 2 logp/H. Convergence: summand
is O(logp*p^(-3sigma)), summable for sigma>1/2.

This is a quantitative and genuinely unconditional **NO-GO** for
the proposed insertion of local same-prime Hecke return moments
into micro-height Dirichlet-polynomial quadratic forms: all
offdiagonal same-prime Euler-return interactions are O(1/H),
so they vanish as the observation window H increases.
Any nontrivial short-height obstruction must sit in **cross-prime**
pairs n=p^k, m=q^l, p≠q, including very close logarithmic frequencies.
That is arithmetically different from the local rank defect D_p=2/p.

A hypothetical off-axis zero rho=beta+i gamma appearing in the
pole-subtracted explicit formula contributes a model term
  N^(rho-s)/(rho-s),  s=sigma+it, sigma<beta.
Its squared local average over an interval of length H centered
at gamma is EXACTLY
  N^(2(beta-sigma)) * [2/(H(beta-sigma))]
     arctan[H/(2(beta-sigma))]
  ~ [pi/(beta-sigma)] N^(2(beta-sigma))/H
for H->infty. Hence ordinary mean value at H~N is blind to such a
term whenever beta<1 and sigma>1/2, because
2(beta-sigma)<1. To resolve it one needs a height interval
H≲N^(2(beta-sigma)), well below the H~N diagonal regime.

This is a scaling analysis of ONE possible zero term, not a
lower bound for the full completed zero sum (other terms may
interfere). It nevertheless identifies the precise frontier:
short-height, **cross-prime** offdiagonal cancellation after
subtracting the genuine pole term. MV diagonal estimates
cannot see the hypothesized off-axis contributions.


## 9. NEW quantitative cross-prime inequality: Fejer smoothing yields a power-saving in Haar center height

This is an honest X<=Y analytic estimate, not a zero detector/equivalence.
Let w_H(v)=H^-1(1-|v|/H)_+ on [-H,H], normalized to integral one.
Its Fourier transform is Phi_H(omega)=sinc(H omega/2)^2>=0.
Define the triangular-height averaged prime-current energy I_tri(T,H;N)
= int_R w_H(t-T) |J_(sigma,N)(t)|² dt.
The distinct-prime cross term is

  C_tri(T,H;N) =
    sum_{n=p^k,m=q^l<=N;p!=q}
      Lambda(n)Lambda(m)(nm)^(-sigma)
      exp[-iT log(n/m)] Phi_H(log(n/m)).

For distinct prime bases the reduced ratio p^k/q^l uniquely identifies
the ORDERED pair, so all cross-prime frequencies log(n/m) are distinct.
Taking the *long-center-time Bohr mean square* therefore diagonalizes
the cross term exactly:

  **||C_tri(.,H;N)||_B2(T)^2 =
     sum_{n=p^k,m=q^l<=N;p!=q}
       Lambda(n)^2 Lambda(m)^2 (nm)^(-2sigma)
         sinc[(H/2)log(n/m)]^4.**

This extends by B2 convergence uniformly in N because the RHS is
dominated by B(sigma)^2<infinity for sigma>1/2.

For any auxiliary P>=2, split into n,m<=P and max(n,m)>P.
For n!=m<=P, |log(n/m)| >= 1/(P+1). Therefore
sinc[(H/2)log(n/m)]^4 <= 16(P+1)^4/H^4.
For the remaining terms use |sinc|<=1 and B_tail(sigma,P)
=sum_{n>P}Lambda(n)^2 n^(-2sigma). Hence the explicit inequality

  **||C_tri(.,H)||_B2^2
    <= 16(P+1)^4 B(sigma)^2/H^4
       +2 B(sigma) B_tail(sigma,P).**

By standard Chebyshev/PNT summation,
  B_tail(sigma,P) <<_sigma P^(1-2sigma) log P,
for 1/2<sigma<1. Choosing P=floor(H^[4/(3+2sigma)]) gives
the genuine *power-decay bound*

  **||C_tri(.,H)||_B2^2
    <<_sigma H^[-4(2sigma-1)/(3+2sigma)] log H.**

Compare rectangular height window: the parallel rate is only
H^[-2(2sigma-1)/(1+2sigma)] log H; triangular Fejer improves
the exponent because its Fourier kernel is squared.

The same-prime contribution decays FASTER under Fejer averaging:
  **|Off_sameprime,tri| <=
    (8/H²) sum_p
    [p^(-2sigma)/(1-p^(-2sigma))] Li_2(p^(-sigma))
    = O_sigma(H^-2)**,
using sinc²(x)<=1/x² and
sum_{k!=l}q^(k+l)/(k-l)^2 = 2 q² Li_2(q)/(1-q²).
(The p-th geometric log factors cancel against log(p)^2 from
the two amplitudes.)

This is a proven nonlinear prime-pair **averaged** inequality.
It passes F_theta falsification in the *finite-energy sense*:
the two-channel Hilbert norm ceases to exist when
sigma<=1/2+theta. It does NOT control C_tri(T,H) at a fixed
chosen T (e.g. an off-axis zero ordinate). That deterministic
local transference is still the missing RH-strength step.
The arithmetic one-parameter flow can be exceptional to Haar
mean-square even when every finite collection of prime
frequencies is equidistributed over very long t intervals.


## 10. Exact exceptional-point counterexample: the SAME cross-prime term diverges at T=0

The Fejer kernel Phi_H(omega)=sinc(H omega/2)^2 is nonnegative.
At center T=0, EVERY summand in C_tri(0,H;N) is nonnegative.
Fix any H>0 and 1/2<sigma<1. For large X, restrict the cross-prime
sum to distinct ordinary primes p,q within
  [X,(1+c_H)X],   c_H=min(1/2,1/(2H)).
Then |(H/2)log(p/q)|<=1/4 and Phi_H(log(p/q))>=sinc(1/4)^2>0.
PNT for the FIXED relative window c_H gives
  sum_(X<=p<=(1+c_H)X) (log p)p^(-sigma)
    ~ [(1+c_H)^(1-sigma)-1] X^(1-sigma)/(1-sigma).
Its square dominates the diagonal sum
  sum_(p in interval)(log p)^2 p^(-2sigma)
   = O_sigma,H(X^(1-2sigma)log X),
so the restricted offdiagonal block is
  >= c_(sigma,H) X^(2-2sigma)       (large X)
for some positive c_(sigma,H).
Hence

  **lim_(N->infty) C_tri(0,H;N)=+infinity for EVERY FIXED H>0,
     even though ||C_tri(.,H)||_B2(T)^2 ->0 as H->infty.**

This is a rigorous, directly arithmetic counterexample to upgrading
the Fejer-smoothed Haar mean-square power bound to pointwise center
height T=0. It exhibits the severe noncommutativity of prime cutoff,
height averaging, and deterministic center evaluation.
It does NOT mean the properly pole-subtracted/Archimedean-completed
quantity diverges; the pole piece can cancel raw coherent growth.
It demonstrates why the completed matching is indispensable.


## 11. Sharper cross-prime Fejer power-decay: integer spacing improves the exponent

The cutoff split in §9 proves one (weak) rate; it is NOT sharp.
A direct near-diagonal pair count yields a MUCH stronger unconditional bound:

  **||C_tri(.,H)||_B2(T)^2 <<_sigma
      H^(1-4sigma) [log(2+H)]^4,   1/2<sigma<1, H>=2.**

Here is a complete elementary majorant (no conjectural prime pairs).
By unique reduced cross-prime ratios (§9),
  ||C_tri||_B2²
   = sum_{cross n,m} Lambda(n)^2Lambda(m)^2 (nm)^(-2sigma)
       sinc[(H/2)log(n/m)]^4.
Majorize Lambda(n)^2 <= (log n)^2 and enlarge to ALL
distinct integers n,m>=2 with b_n=(log n)^2 n^(-2sigma).

Split pairs into "far" max(n,m)>2 min(n,m) and "near" n/2<=m<=2n.
For far pairs, |log(n/m)|>=log 2, so sinc^4<=const/H^4.
Their entire contribution <= const/H^4*(sum b_n)^2, finite
because sigma>1/2.

For near pairs, d=|m-n|>=1 and |log(n/m)|>=d/(2n).
Moreover b_nb_m <= C_sigma n^(-4sigma)log(2n)^4.
Then
  sinc[(H/2)log(n/m)]^4 <= min[1,(4n/(H d))^4].
The sum over near integers m is
  O((n/H)^4)  if n<=H,
  O(n/H)      if n>H.
Hence the full near contribution is at most
  C_sigma [H^-4 sum_{n<=H}n^(4-4sigma)log(2n)^4
         + H^-1 sum_{n>H}n^(1-4sigma)log(2n)^4]
  <<_sigma H^(1-4sigma)log(2+H)^4
for 1/2<sigma<1 (so 4-4sigma>-1 and 1-4sigma<-1).

This improves §9's decay exponent from
4(2sigma-1)/(3+2sigma) to **4sigma-1**, e.g.
sigma=3/4 now gives mean-square O(H^-2 log^4 H).
All steps are explicit and unconditional. This bound is for
the Bohr mean-square of the cross-prime **center-height function**,
NOT its value at any fixed t and not the completed Weil distribution.
§10 proves the same function may diverge at fixed center T=0 as
N->infty, so the pointwise-upgrade obstruction remains exact.


## 12. A uniform POINTWISE O(1) inequality for the cross-prime quadratic form

This is a different conclusion from §§9-11: it holds at *every*
deterministic center T and cutoff N, not just in Bohr mean.
For Fejer weight w_H, the integral
  I_tri(T,H;N)=int_R w_H(t-T)|J_(sigma,N)(t)|² dt
is NONNEGATIVE for each real T and H>0.

Split exactly into I_tri=B_N(sigma)+S_same(T,H;N)+C_cross(T,H;N).
Here B_N=sum_{n<=N}Lambda(n)^2 n^(-2sigma) <= B(sigma).
By §9 the same-prime offdiagonal satisfies
  |S_same|<=D_sigma/H²,
  D_sigma=8 sum_p [p^(-2sigma)/(1-p^(-2sigma))] Li_2(p^(-sigma))
  <infinity for sigma>1/2.
Therefore the nontrivial signed different-prime correlation has the
explicit, genuinely pointwise one-sided bound

  **C_cross(T,H;N) >= -B(sigma)-D_sigma/H²,
     for all T in R, H>0, N>=2 and fixed sigma>1/2.**

This is a PROVED O(1) prime-side inequality that uses the zeta
one-channel finite B(sigma), and is uniform over the arithmetic
cutoff and deterministic center. For the F_theta shifted control,
the corresponding finite bound is unavailable below
sigma<=1/2+theta because B_theta diverges.

**Fundamental limitation:** C_cross is QUADRATIC in Lambda, whereas
the completed Weil/two-box prime sum is LINEAR in Lambda; their
Archimedean/pole terms are not the same. Therefore one may NOT
substitute this O(1) lower bound for the desired O(1) lower bound
on S_l(x)-A_l sqrt(x). Constructing an exact and sign-compatible
mapping from the completed Weil observable into this quadratic
prime-pair form would be a genuinely new RH-strength theorem.
No such trace/linearization sewing map is proved here. This
distinction must accompany every citation of the inequality.
