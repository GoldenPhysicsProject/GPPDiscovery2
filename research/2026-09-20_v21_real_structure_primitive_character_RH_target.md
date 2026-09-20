# v21 real-structure correction and the primitive-character RH target

Date: 2026-09-20

This note replaces the overly literal finite-Haar-quotient reading used in some 2026-09-18
scratch notes with the corrected structure in Which Way Is Forward? v21.

## 1. v21 correction

In v21 the simultaneous reversal D on the four-lift carrier is not interpreted as a finite
gauge average on the Hilbert carrier. Relative to the microscopic complex structure I_q it is
an anti-linear involution, hence a real structure. Its fixed carrier H_D is a real form.

The numerical projector (1+D)/2 remains the real-part projector. Haar averaging survives as
a representation-theoretic statement on the finite LABEL group and as a statement about
D-invariant measures, but it is not the fundamental Hilbert-space quotient mechanism.

This distinction must be kept in the RH bridge.

## 2. Exact Haar-line real structure

Take the multiplicative Haar coordinate

u=log r

and

H=L^2(R,du).

Define

(Rf)(u)=f(-u),
(Cf)(u)=conj(f(u)),
D_H=R C.

Then R is unitary, C is antiunitary, they commute, and

D_H^2=I.

With the ordinary complex structure I=i,

D_H I = - I D_H.

Thus D_H is a real structure on H in exactly the sense used by v21.

Its fixed real form is

H_R={f : f(u)=conj(f(-u)) a.e.}.

For f in H_R,

R f = C f.

So on the real form the two half operations, reflection and conjugation, coincide. This is the
infinite-dimensional Haar analogue of the v21 finite half-flip identity.

## 3. Action on Mellin character lines

For the formal Mellin character

phi_nu(u)=exp(nu u),

one has

R phi_nu = phi_{-nu},
C phi_nu = phi_{conj(nu)},
D_H phi_nu = phi_{-conj(nu)}.

With

nu=s-1/2,

these are exactly

shadow:       nu -> -nu,
conjugation:  nu -> conj(nu),
real structure: nu -> -conj(nu).

The individual complex character line L_nu=C phi_nu is D_H-stable iff

L_nu=L_{-conj(nu)}.

Because two exponentials exp(nu u) and exp(mu u) are proportional for all u only when nu=mu,
this is equivalent to

nu=-conj(nu),

hence

Re(nu)=0,
Re(s)=1/2.

Therefore:

PRIMITIVE CHARACTER REALITY THEOREM.
An individual Mellin character line is invariant under the canonical Haar real structure D_H
iff its exponent lies on the unitary principal-series axis.

This is a direct operator realization of the centered fixed-locus architecture formalized in
OrientationCriticalRealStructureBridge.lean.

## 4. Exact loophole: a real total resonance space does not imply RH

If Re(nu) != 0, the two-dimensional complex space

E_nu = span_C{phi_nu, phi_{-conj(nu)}}

is nevertheless D_H-stable: D_H exchanges its two generators.

A D_H-fixed real vector is for example

phi_nu + phi_{-conj(nu)}

up to the appropriate coefficient conjugation.

Hence a global arithmetic resonance space may possess a perfectly good real structure while
containing off-critical conjugate-shadow pairs.

This is not a pathology. It is precisely how real structures normally package conjugate
complex representations.

The v21 Spin(10,2) Majorana-Weyl theorem gives an instructive finite-dimensional analogue:
one real chiral module complexifies into a complex representation plus its conjugate partner.
Therefore "one real object" does not imply "each complex label is fixed by conjugation."

This kills the naive inference

global real structure => every zero fixed by s -> 1-conj(s).

## 5. Sharpened non-circular RH target

What would be sufficient is stronger:

PRIMITIVE ARITHMETIC REAL-LINE ADMISSIBILITY.
For every primitive nontrivial zero contribution, the associated arithmetic resonance is
realized on a single one-dimensional Mellin character line which is invariant under D_H.

Then the primitive-character reality theorem gives Re(rho)=1/2 immediately.

Equivalent operator formulation:

construct the zero-independent arithmetic resonance representation so that every primitive
resonance block is a one-dimensional irreducible character of the unitary multiplicative
Haar representation, rather than a two-line nonunitary conjugate-shadow pair.

This is stronger than merely constructing a D_H-real total space.

## 6. Relation to the existing temperedness target

The unitary representation of R_+^x on L^2(dr/r) has generalized characters r^{i gamma}.
For

rho=1/2+delta+i gamma,

the half-density character is

r^{rho-1/2}=exp(delta u) exp(i gamma u).

When delta != 0 it is not tempered on R. Therefore primitive arithmetic real-line
admissibility can also be phrased as:

each zero contribution is a tempered generalized character of the fixed self-adjoint Haar
dilation generator.

That is the same hard bridge already isolated in ExpNotTempered.lean and the Meyer/Weil
admissibility program, now with the v21 real-structure interpretation made exact.

## 7. Consequence for current strategy

Do not attempt to prove RH from:
- existence of a global anti-linear real structure;
- equal weighting of paired lifts;
- a real Majorana-type packaging;
- self-adjointness of a reflected boundary operator.

All of those allow paired off-axis sectors.

The next useful theorem must prevent PAIR PACKAGING at the primitive arithmetic resonance
level. Possible routes remain:
1. a true unitary/tempered spectral realization of each zero atom;
2. a one-dimensional multiplicity theorem for primitive arithmetic character lines together
   with D_H invariance of each line;
3. a passive/minimum-phase boundary theorem eliminating the off-axis Blaschke pair;
4. a global no-ghost coercive estimate whose kernel cannot contain a paired nonunitary block.

This is the corrected v21-informed RH target.
