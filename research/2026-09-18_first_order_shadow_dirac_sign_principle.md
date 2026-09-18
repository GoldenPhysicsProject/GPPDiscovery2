# First-order shadow Dirac and the sign that must not be squared away

Date: 2026-09-18

The recurring project pattern is now exact:

- first-order orientation data are sign-sensitive;
- the positive square is even and loses that sign;
- RH lives in the first-order identification shadow = adjoint, not in positivity of the square alone.

## 1. Local Euler holonomy

For p>1 define

z_p(s)=1-p^{-s}
      =1-exp(-s log p).

The existing Lean file PrimeFermionDirac uses the Hilbert-adjoint Dirac

D_p^Hilb(s)
=
[[0, conj(z_p(s))],
 [z_p(s), 0]],

which is self-adjoint for every s by construction and satisfies

(D_p^Hilb)^2=|z_p(s)|^2 I >=0.

This is the correct local Hodge square, but it cannot distinguish the critical line because conjugation has already been inserted by hand.

## 2. Shadow Dirac

Define instead the functional-equation/shadow Dirac

D_p^sh(s)
=
[[0, z_p(1-s)],
 [z_p(s), 0]].

Then

(D_p^sh(s))^2
=
z_p(s) z_p(1-s) I.

Its adjoint is

(D_p^sh(s))^*
=
[[0, conj(z_p(s))],
 [conj(z_p(1-s)),0]].

For s=sigma+it,

z_p(1-s)
=
1-p^{sigma-1} e^{it log p},

while

conj(z_p(s))
=
1-p^{-sigma} e^{it log p}.

Therefore

z_p(1-s)=conj(z_p(s))
iff
p^{sigma-1}=p^{-sigma}
iff
sigma=1/2.

Hence, for every p>1,

D_p^sh(s) is self-adjoint
iff Re(s)=1/2.

On that locus,

D_p^sh(s)=D_p^Hilb(s)

and

(D_p^sh(s))^2
=
|z_p(s)|^2 I >=0.

This is the local Euler-factor form of the theorem "shadow = adjoint iff critical line."

## 3. Explicit shadow-adjoint defect

The upper-right mismatch is

delta_p(s)
=
z_p(1-s)-conj(z_p(s))
=
e^{it log p}(p^{-sigma}-p^{sigma-1}).

Write x=sigma-1/2. Then

delta_p(s)
=
-2 e^{it log p} p^{-1/2} sinh(x log p),

so

|delta_p(s)|^2
=
4 p^{-1} sinh^2(x log p).

It vanishes for every p iff x=0.

For any fixed x!=0 in the critical strip, the unweighted global defect energy

sum_p |delta_p(s)|^2

diverges. Thus off-critical shadow and Hilbert-adjoint structures are not merely unequal; in the natural all-prime unweighted square metric they are infinitely separated. At x=0 the defect is identically zero prime by prime.

This does not by itself prove RH because a zeta zero is not yet proved to be a normal vector in this prime Hilbert metric. It identifies exactly what a successful global first-order construction must establish.

## 4. Modular and Clifford sign principle

The same loss of sign occurs in the already formalized modular sector:

M=[[1,1],[1,0]], det M=-1,

A=M^2=[[2,1],[1,1]], det A=+1.

The eigenvalues of M are

phi, -phi^{-1},

with product -1. Squaring gives

phi^2, phi^{-2},

with product +1.

Likewise

1-phi=-phi^{-1},
phi(1-phi)=-1,
-phi(1-phi)=1.

Thus the golden unit Casimir is the even square of an orientation-reversing first-order pair.

In the Hardy sector, Gamma^2=K^2=I and RH is the one-sided Clifford relation

{Gamma,K}=0

on H2_+. Then J=Gamma K obeys J^2=-I and J^4=I.

In the half-density scalar sector, X^*=-X gives

-X^2=X^*X>=0.

All four are the same sign architecture.

## 5. Strategic consequence

Do not attempt to prove RH from an object in which shadow and adjoint have already been multiplied together or replaced by one another.

Examples of even data that can become blind to the required orientation information:
- |Z|^2;
- Hodge Laplacians D^*D;
- shadow-paired scalar products after phase is discarded;
- ordinary Gram positivity;
- completed boundary self-adjointness without Hardy causality.

The proof-bearing object must retain the two first-order maps separately and prove their identification:

functional shadow = Hilbert adjoint

on the actual completed arithmetic state space.

Only after that identity is established should one square. The square is then positive automatically.

This gives a sharper target for the global prime-Archimedean construction: build a completed shadow Dirac/resolvent whose first-order off-diagonal entries are related by functional shadow, and prove from the positive polarization that they are Hilbert adjoints.