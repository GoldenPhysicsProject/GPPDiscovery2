# Horizon time-orientation flip as inversion of the SU(1,1) squeeze

Date: 2026-09-27
Status: exact SU(1,1) algebra plus a proposed horizon sewing interpretation. No claim that black-hole annihilation follows from the algebra alone.

## 1. Prime/paired TFD state as a squeeze orbit

Let
\[
S(\kappa)
=
\exp\!\left[\kappa(K_+-K_-)\right]
\]
for real kappa in the paired k=1/2 SU(1,1) module.

Then
\[
|\Omega_\kappa\rangle
=
S(\kappa)|0\rangle
\]
has coherent coordinate
\[
r=\tanh\kappa
\]
and expansion
\[
|\Omega_\kappa\rangle
=
\operatorname{sech}\kappa
\sum_{n\ge0}
(\tanh\kappa)^n|n,n\rangle.
\]

For a critical prime,
\[
\tanh\kappa_p=p^{-1/2}.
\]

## 2. Orientation parity sends the squeeze to its inverse

Let
\[
J|n,n\rangle=(-1)^n|n,n\rangle.
\]

Then
\[
JK_\pm J=-K_\pm,
\qquad
JK_0J=K_0.
\]

Therefore
\[
\boxed{
JS(\kappa)J
=
S(-\kappa)
=
S(\kappa)^{-1}.
}
\]

Consequently
\[
\boxed{
J|\Omega_\kappa\rangle
=
|\Omega_{-\kappa}\rangle.
}
\]

Thus the sheet/orientation involution does not merely attach an abstract minus sign: it reverses the SU(1,1) boost/squeeze rapidity.

## 3. What flips and what does not

The normal covariance
\[
C=\sinh^2\kappa
\]
is even:
\[
C(-\kappa)=C(\kappa).
\]

The anomalous covariance
\[
A=\sinh\kappa\cosh\kappa
\]
is odd:
\[
A(-\kappa)=-A(\kappa).
\]

Therefore the finite mass coordinate
\[
\mu^2=4C
\]
is invariant under the orientation flip.

This is important:
\[
\boxed{
t\text{-orientation reversal by itself does not make the mass gap vanish.}
}
\]

It reverses the pairing/orientation phase, not the occupation/mass magnitude.

Any horizon model in which mass disappears or converts to radiation needs an additional boundary interaction or quotient.

## 4. The two SU(1,1) lightcone directions are exchanged

The coherent hyperboloid coordinates are
\[
X_\pm=e^{\pm2\kappa}.
\]

Under
\[
\kappa\mapsto-\kappa,
\]
we get
\[
\boxed{
X_+\leftrightarrow X_-.
}
\]

So the orientation involution literally exchanges the two null directions of the SU(1,1) adjoint geometry.

This gives a precise algebraic version of the earlier “two time arrows / null boundary” intuition.

## 5. Opposite sheets carry inverse holonomies

Suppose a folded two-sheet geometry assigns
\[
t=\operatorname{sgn}\sigma
\]
and the microscopic orientation acts by J at
\[
\sigma\mapsto-\sigma.
\]

Then the two sheet transports are naturally
\[
S(\kappa)
\qquad\text{and}\qquad
S(-\kappa).
\]

Their composition is exactly
\[
\boxed{
S(\kappa)S(-\kappa)=I.
}
\]

Thus the two conjugate sheets carry inverse SU(1,1) holonomies.

At a branch fixed point, a sewing rule based on composition of the two sheet transports has trivial net internal holonomy.

This is a mathematically clean candidate for what “the two orientations close on one another at the horizon” could mean.

## 6. Relation to annihilation language

The identity
\[
S(\kappa)S(-\kappa)=I
\]
does **not** mean that two physical fermions automatically annihilate.

What it says is:
\[
\boxed{
\text{orientation coupling on one sheet}
+
\text{orientation coupling on the reversed sheet}
=
\text{zero net SU(1,1) holonomy}.
}
\]

If a boundary interaction converts the paired massive sector to a null/radiative sector while preserving charge, fermion parity, stress energy, and unitarity, the inverse-holonomy identity would give a natural internal cancellation mechanism.

The dynamical conversion map is still missing.

## 7. Zitter beat under the same involution

The two proper-time orientations carry phases
\[
e^{\mp i\omega_C\tau},
\qquad
\omega_C=\frac{mc^2}{\hbar}.
\]

Their relative phase rate is
\[
2\omega_C
=
\frac{2mc^2}{\hbar}
=
\omega_Z.
\]

The SU(1,1) orientation involution exchanges the two squeeze/lightcone directions at the same time that the particle orientation model exchanges the two proper-time phases.

This is a structural compatibility, not yet an explicit intertwiner between the Dirac spinor and the arithmetic SU(1,1) module.

## 8. Sharpened horizon target

A viable folded-horizon theory should therefore separate three operations:

1. **orientation reversal**
   \[
   J:\kappa\to-\kappa;
   \]

2. **fixed-point sewing**
   which composes inverse sheet holonomies and can make the net internal transport trivial;

3. **unitary channel conversion**
   which transfers the massive paired energy/charges into allowed null outgoing channels.

Conflating step 1 with annihilation is incorrect.

The exact algebra supports steps 1 and the inverse-holonomy part of step 2. Step 3 remains a physical construction problem.
