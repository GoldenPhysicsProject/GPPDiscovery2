# Modular-surface arithmetic AdS2 scattering: exact zeta reconstruction and a principal-series correction

Date: 2026-09-27
Status: standard exact hyperbolic-scattering identities, independently re-derived for the current holographic programme. No RH claim. No zero-location input is used in the derivation.

This note cross-checks the "arithmetic AdS2" intuition against the literal hyperbolic surface PSL(2,Z)\H.

## 1. The modular surface gives a genuine arithmetic hyperbolic bulk

Let Gamma=PSL(2,Z) act on the upper half-plane H with the Poincare metric

ds^2=(dx^2+dy^2)/y^2.

The nonholomorphic Eisenstein series E(z,w) at the cusp has constant term

E(z,w)
=
y^w + phi(w)y^(1-w) + nonzero Fourier modes,

with scattering coefficient

boxed:
phi(w)
=
sqrt(pi) Gamma(w-1/2)/Gamma(w)
*
zeta(2w-1)/zeta(2w).

Define the completed but meromorphic zeta factor

Lambda(s)=pi^(-s/2)Gamma(s/2)zeta(s).

Then exactly

boxed:
phi(w)=Lambda(2w-1)/Lambda(2w).

This is the standard one-cusp scattering matrix of the modular surface.

Thus the completed Riemann zeta is literally part of a self-adjoint hyperbolic scattering problem. The "arithmetic bulk" is not only an analogy at this level.

## 2. Unitary principal-series boundary scattering is unconditional

The Eisenstein Laplacian eigenvalue is

lambda(w)=w(1-w).

The continuous/unitary line is

w=1/2+i t,

for which

lambda=1/4+t^2.

The functional equation Lambda(s)=Lambda(1-s) gives

Lambda(2it)=Lambda(1-2it)=conj(Lambda(1+2it)).

Hence

boxed:
phi(1/2+it)
=
conj(Lambda(1+2it))/Lambda(1+2it),

so

boxed:
|phi(1/2+it)|=1

for real t wherever the expression is finite.

Also

boxed:
phi(w)phi(1-w)=1.

This is genuine unitary scattering of a self-adjoint bulk Laplacian, independent of RH.

## 3. The nontrivial zeta zeros are literal scattering resonances

Let rho be a nontrivial zero of zeta, with no accidental numerator cancellation at the corresponding point.

A denominator zero Lambda(2w)=0 gives a pole of phi at

boxed:
w_pole = rho/2.

The same rho gives a numerator zero at

boxed:
w_zero = (rho+1)/2.

These are exchanged by the scattering reflection w -> 1-w after pairing rho with 1-rho.

Thus nontrivial Riemann zeros are actual resonance data of this arithmetic hyperbolic scattering system.

## 4. Important correction: the modular-surface resonance parameter is NOT the zeta principal-series parameter

If RH holds,

rho=1/2+i gamma.

Then the modular-surface resonance pole is

boxed:
w_pole=1/4+i gamma/2,

while its scattering zero is

boxed:
w_zero=3/4+i gamma/2.

They lie symmetrically about the physical scattering line Re(w)=1/2.

Therefore RH does NOT say that these standard modular-surface resonances lie on the modular Laplacian's principal-series line. Instead it says:

boxed:
all nontrivial modular-surface zeta resonances have the same horizontal depth 1/4 from the unitary scattering line.

Equivalently, if rho=beta+i gamma, the pole depth is

1/2-Re(w_pole)
=
(1-beta)/2.

RH makes this universally 1/4.

This corrects an easy but important overstatement in the project heuristic "zeta zeros = principal-series spectrum" when that phrase is interpreted using the standard modular Eisenstein parameter w.

The zeta variable s itself can still carry a separate PSL(2,R)/CFT1 principal-series interpretation with Re(s)=1/2. One must not silently identify that s with the modular-surface Eisenstein parameter w.

## 5. Physical interpretation: RH as universal resonance lifetime, not mere bulk self-adjointness

Because the modular Laplacian is already self-adjoint and its boundary S-matrix is already unitary, neither fact can prove RH.

Self-adjoint scattering systems can have resonances away from their unitary axis.

For the modular surface the exact RH statement becomes a resonance-width rigidity condition:

boxed:
every nontrivial arithmetic resonance has exactly the same decay depth 1/4.

The functional equation supplies pole/zero reflection about the unitary line, but does not by itself force that common depth.

This is the hyperbolic-scattering analogue of the independently found Fisher-zero no-go: unitary real-time dynamics is weaker than the location of its complex resonances.

## 6. Wigner delay on the unitary line

Write

A(t)=Lambda(1+2it).

Then

phi(1/2+it)=conj(A(t))/A(t).

Up to the sign convention used for outgoing versus incoming scattering phase,

d/dt arg phi(1/2+it)
=
-4 Re[Lambda'(1+2it)/Lambda(1+2it)].

Thus the completed logarithmic derivative already used throughout the RH programme is literally the Wigner-Smith time-delay density of the modular-surface cusp S-matrix, after the argument-doubling 1+2it.

This gives a direct physical home for the completed current.

## 7. Relation to the number-circle / prime-Fock picture

The current programme now has two exact geometric realizations of zeta:

A. Number circle:
zeta(s)=(1/2)Tr' Delta_S1^(-s/2),
with unique factorization unitarily rewriting log|D| as the free prime-Fock Hamiltonian.

B. Modular hyperbolic bulk:
phi(w)=Lambda(2w-1)/Lambda(2w),
where completed zeta is the cusp scattering coefficient.

The factor 2 is structural in both:
- the circle Laplacian has eigenvalues n^2, so zeta(s) is its spectral zeta at exponent s/2;
- the modular Eisenstein S-matrix samples Lambda at 2w and 2w-1.

This makes the recurring doubling in the project a concrete geometric feature, but the representation parameters must be kept distinct.

## 8. Consequence for the active proof search

The modular surface supplies a literal self-adjoint holographic parent, but it also proves a no-go against the naive strategy "find any self-adjoint arithmetic bulk and RH follows."

The load-bearing missing theorem must be stronger. Candidate formulations now become:

1. a resonance-width rigidity theorem forcing all poles of the completed arithmetic response to depth 1/4;
2. a positive Fredholm fluctuation determinant in the centered zeta variable;
3. a de Branges/canonical-system structure whose complex resonances are constrained more strongly than generic hyperbolic scattering;
4. a prime-Archimedean quotient whose physical resonance operator is different from the already-self-adjoint free modular Laplacian.

This is a refinement, not a rejection, of arithmetic holography: the literal AdS2-like arithmetic bulk exists, but RH is a special rigidity property of its resonance divisor.
