# Riemann-kernel radical calibrates the split pole channels exactly

Date: 2026-09-29
Status: exact abstract linear algebra plus an exact Weil-spectral radical observation, subject to the standard test-space extension of the Weil sesquilinear formula to the Riemann kernel. No RH claim.

This note was triggered by Daniel's Meta-AI synthesis, which reported finite pole-resolvent
numbers approaching -2 and +2. Those thresholds are not empirical accidents.

## 1. The Riemann kernel gives exact radical vectors

Let Phi be the standard even Riemann kernel with centered Fourier transform

  Phihat(z)=Xi(z)=xi(1/2+i z).

In the standard Weil/Bombieri sesquilinear zero-side realization, a test function f
enters through its Mellin/Fourier values at the centered zeros. Schematically,

  W(f,g)
   = sum_rho F(rho) overline(G(1-conj rho))

with the usual regularization/test-space conventions.

Since Xi vanishes at every nontrivial zero,

  Xi(z_rho)=0,

Phi annihilates every zero channel. Therefore, whenever Phi belongs to the admitted
test-space completion,

  boxed:
  W(Phi,g)=0 for every admissible g.

Thus Phi is an exact radical vector of the GLOBAL Weil form, independently of RH.

Likewise every polynomial differential descendant P(d/du)Phi has transform
P(-iz)Xi(z), hence also vanishes at every zero. In particular

  boxed:
  Phi' is an exact odd radical vector.

This explains why finite-window/prolate approximants to Phi can become spectacularly
near-null without assuming RH: they are approximating an exact global radical.

IMPORTANT: this does NOT imply positivity. An indefinite Hermitian form can have a
large radical.

## 2. Pole split

Write the completed Weil operator/form in the parity decomposition as

  Q = A + (1/2)|c><c| - (1/2)|s><s|,

where
- A is the pole-removed prime--Archimedean part and commutes with parity;
- c is even;
- s is odd.

In the semilocal multiplicative realization,

  c(u)=u^(1/2)+u^(-1/2),
  s(u)=u^(1/2)-u^(-1/2).

Write A_+ and A_- for the even and odd restrictions.

Because Phi is even, <s,Phi>=0. Because Phi' is odd, <c,Phi'>=0.

## 3. Exact even threshold from the vacuum radical

Assume A_+ is invertible on the ambient sector and

  Q Phi = 0.

Then

  A_+ Phi + (1/2)c<c,Phi>=0.

If <c,Phi> != 0,

  A_+^{-1}c
    = -2 Phi/<c,Phi>.

Taking the c-pairing gives

  boxed:
  <c,A_+^{-1}c> = -2.

For the standard Riemann kernel this overlap is nonzero. Indeed c probes the two
elementary Mellin points s=0 and s=1, and xi(0)=xi(1)=1/2, so the even sum is nonzero
(up to the fixed Fourier/Mellin normalization).

Therefore the even pole channel is calibrated exactly at the rank-one positivity
threshold.

## 4. Exact odd threshold from the derivative radical

Similarly, from

  Q Phi'=0

and odd parity,

  A_- Phi' - (1/2)s<s,Phi'>=0.

If <s,Phi'> !=0, then

  A_-^{-1}s
    = 2 Phi'/<s,Phi'>,

hence

  boxed:
  <s,A_-^{-1}s> = 2.

The overlap is nonzero. Integration by parts gives, modulo the fixed normalization,

  <s,Phi'>
    = -(1/2)<c,Phi>,

because s'=(1/2)c and Phi decays rapidly at both ends.

Thus the odd pole channel is also exactly calibrated at threshold.

This is the rigorous structural explanation for the finite calculations that approach
the pair (-2,+2).

## 5. Rank-one inertia theorem

The preceding equalities become decisive once the inertia of A is known.

Finite-dimensional abstract form:

Let A_+ be real symmetric and invertible with inertia

  n_-(A_+)=1,
  n_0(A_+)=0.

Then

  Q_+ = A_+ + (1/2) c c^T

is positive semidefinite with a one-dimensional new kernel exactly when

  c^T A_+^{-1}c = -2.

Proof by the Haynsworth/Schur-complement inertia formula. Consider

  B_+ =
    [ A_+   c ]
    [ c^T  -2 ].

The Schur complement of -2 is Q_+. The Schur complement of A_+ is

  -2 - c^T A_+^{-1}c.

At the radical-calibrated value -2 this scalar complement is zero. Since A_+ has
exactly one negative direction and the -2 pivot supplies exactly that one negative
direction, Q_+ has no negative eigenvalue and acquires one zero.

Similarly, if A_->0 then

  Q_- = A_- - (1/2) s s^T

is positive semidefinite exactly when

  s^T A_-^{-1}s <= 2,

and the radical-calibrated value 2 gives a zero mode.

Therefore:

  boxed:
  if n_-(A_+)=1 and A_->0,
  the exact Phi/Phi' radical calibration forces Q>=0.

By the Weil criterion this would prove RH.

## 6. What has and has not been solved

Solved exactly:
- why the Riemann kernel Phi is the correct vacuum candidate;
- why its finite approximants are near-null;
- why the pole-channel resolvent numbers target -2 and +2;
- why both thresholds are fixed by xi(0)=xi(1) and the exact zero vanishing of Xi;
- why the completed positivity problem can be reduced to the inertia of the pole-removed
  operator A.

Not solved:
- an unconditional proof that the critical-boundary pole-removed operator satisfies
    n_-(A_+)=1 and A_->0
  (or the corresponding infinite-dimensional Morse-index statement).

The existing Perron--Frobenius/Beurling--Deny structure proves simplicity and positivity
of the LOWEST state for the finite pole-removed matrices, but does not by itself exclude
additional negative eigenvalues.

The existing Gamma--Plancherel/Hodge Gram identities prove positive transverse pieces in
safe/shifted regimes, but the project already recorded that extending those positive
identities to the completed critical boundary is the missing no-ghost theorem.

So this is a genuine compression, not a hidden proof.

## 7. New smallest rank-two target

Instead of proving full Weil positivity directly, it is enough to prove the pole-removed
Morse-index statement

  boxed:
  n_-(A_+)=1,
  n_-(A_-)=0

in the completed critical-boundary realization.

The exact Riemann-kernel radical then supplies the Schur thresholds automatically and
forces the full form to be positive semidefinite.

Equivalently, prove positivity of A on the codimension-two neutral space

  <c,f>=<s,f>=0

plus the existence of only the one even Perron--Frobenius negative direction.

This is the sharp no-ghost formulation suggested by the numerical split-signature work.

## 8. Relation to the Hardy/E-map route

This rank-two formulation and the Hardy-E-map quotient formulation locate the same
difficulty differently:

- Hardy/E-map: every zero survives in an explicit fixed strip Hilbert quotient; prove
  the induced quotient dynamics has zero exponential type.
- Weil/no-ghost: Phi and Phi' calibrate the two boundary channels exactly; prove the
  pole-removed transverse operator has no hidden negative modes.

An off-line zero would simultaneously:
- create exponential quotient growth / Hardy anticausal leakage;
- create a hidden negative transverse/no-ghost mode.

A successful proof can therefore target whichever of those two manifestations is more
tractable.
