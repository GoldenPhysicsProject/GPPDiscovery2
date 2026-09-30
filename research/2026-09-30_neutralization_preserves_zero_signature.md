# Neutralization preserves every nontrivial zero channel

Date: 2026-09-30
Status: exact Fourier/Mellin algebra plus Weil-signature reduction. No RH claim.

This note closes an important logical loophole in the pole-neutral route. The operator
L0 = d^2/du^2 - 1/4 annihilates the two elementary pole modes, but it does NOT suppress
any nontrivial zeta zero. Consequently positivity after neutralization is itself RH-strength.

## 1. Mellin multiplier of the pole-killing operator

Use the centered Fourier/Mellin coordinate
  s = 1/2 + i z
and Fourier convention
  ghat(z)=integral_R g(u)e^{-izu}du.

For
  L0 = d^2/du^2 - 1/4,
integration by parts gives
  (L0 g)^hat(z)=-(z^2+1/4) ghat(z).

Since
  s(1-s)=1/4+z^2,
we have the exact identity

  boxed:
  (L0 g)^hat(z) = -s(1-s) ghat(z).

Thus L0 kills precisely the elementary completed pole points s=0 and s=1.

At every nontrivial zero rho,
  rho(1-rho) != 0,
so L0 acts by a NONZERO scalar on that zero-evaluation channel.

## 2. Off-line mirror signature survives neutralization

The finite reflection-positivity core already proves that an off-line mirror pair
rho, tau rho=1-conj rho spans a hyperbolic plane in the Weil form.

On the zero side, replacing f by L0 g multiplies the rho coordinate by
  -rho(1-rho)
and the tau-rho coordinate by
  -(tau rho)(1-tau rho).

These are nonzero and are conjugate under the mirror symmetry. Therefore the
two-dimensional mirror-pair Hermitian form is changed only by an invertible diagonal
congruence.

Sylvester inertia is invariant under invertible congruence.

Hence:

  boxed:
  an off-line mirror pair remains indefinite after L0 neutralization.

The pole-killing differential cannot turn a ghost pair positive.

## 3. Interpolation survives because the multiplier is nonzero

Let rho_1,...,rho_m be any finite set of nontrivial zeros and prescribe target values
a_j.

Standard Paley-Wiener/Weil test-function interpolation allows a compactly supported
smooth f whose Mellin transform assumes prescribed values at the rho_j.

For neutral functions f=L0 g the values satisfy
  F(rho_j)=-rho_j(1-rho_j)G(rho_j).

Since every rho_j(1-rho_j) is nonzero, prescribing F(rho_j)=a_j is equivalent to
prescribing
  G(rho_j)=-a_j/[rho_j(1-rho_j)].

Thus the neutral range retains the same finite zero-coordinate freedom as the original
Weil test class.

In particular, if an off-line mirror pair exists, one can realize its negative
hyperbolic direction using a neutral test function.

## 4. Exact equivalence of neutral positivity and RH

On the neutral subspace the rank-two pole form vanishes:
  <c,f>=<s,f>=0
implies
  Q(f,f)=A(f,f).

Therefore:

RH
=> Weil Q >=0
=> A >=0 on the neutral subspace.

Conversely, suppose
  A(f,f)>=0
for every neutral admissible f.

If an off-line zero existed, Section 2 plus Section 3 would produce a neutral f whose
Weil form is negative. But on that f, Q=A, contradiction.

Hence

  boxed:
  RH
  iff
  A|_N >=0
  iff
  <L0 g, A L0 g> >=0 for every admissible compactly supported smooth g.

This equivalence is subject only to the usual Weil test-space interpolation/density
hypotheses; no zero location is assumed in deriving the L0 multiplier.

## 5. Consequence for proof search

The proposed search for a positive factorization
  L0^* A L0 = B^* B
is legitimate, but it would BE an RH proof. It cannot follow merely from local Gamma
positivity, prime positivity, or a generic functional-analytic identity, because known
off-line mirror configurations would make the left side indefinite.

This explains why the earlier fixed-q Gamma-prime-pole Krein square remains indefinite:
local positive pieces cannot repair the global mirror-pair sign.

The only viable factorization must use genuinely GLOBAL arithmetic sewing:
Poisson self-duality plus Euler data in the same operator.

## 6. Better exact target

Instead of asking vaguely for positivity of A after pole healing, seek an explicit
zero-independent operator B built from the global Poisson/Euler sewing such that

  <L0 g, A L0 g> = ||B g||^2

for all g in the Weil test domain.

If such an identity is derived from the primes and Poisson summation without zero data,
RH follows immediately.

The factorization must fail for Beurling-prime analogues or functional-equation-only
analogues with off-line zeros; this is a mandatory falsifier against accidentally proving
a generic false statement.
