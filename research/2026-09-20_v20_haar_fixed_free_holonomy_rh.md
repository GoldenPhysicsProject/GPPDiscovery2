# Which Way Is Forward v20 -> RH integration audit

Date: 2026-09-20

This note records what v20 materially contributes to the active RH program, what it does not,
and the exact corrections needed when importing the orientation language.

## 1. Finite V4 is a genuine Haar/Peter--Weyl face

The four orientation labels form

V4 = Z2 x Z2,

with characters

1, q, t, chi=q t.

The selected simultaneous reversal D=(-1,-1) generates a subgroup <D> of order two.
The normalized finite Haar projector is

P_D=(I+D)/2.

On the character basis,

P_D 1=1,
P_D q=0,
P_D t=0,
P_D chi=chi.

More strongly, every D-invariant complex function on V4 is uniquely

a*1+b*chi.

This has been formalized in

GppVerify/StandardModel/FourLiftHaarPeterWeyl.lean.

The exact conceptual point is that the four-lift model is not merely an equal-probability
toy. It is the finite compact harmonic-analysis analogue of the other Haar mechanisms in
the project.

This does not by itself prove that D is a physical gauge redundancy.

## 2. Fixed locus and free deck cover are different mechanisms

The celestial/RH anti-linear label map

Delta -> 2-conj(Delta)

has a fixed locus

Re Delta=1,

or Re s=1/2 under Delta=2s.

The four-lift deck involution D acts freely on the four labels.

The determinant square-root deck transformation also acts freely away from the branch
locus and carries nontrivial closed-loop holonomy.

These should not be merged into one generic "orientation Z2" argument.

There are two distinct mechanisms:

A. Fixed-locus selection:
   an anti-linear or adjoint compatibility condition forces a spectral parameter to a
   unitary axis.

B. Free-cover holonomy:
   local sheet labels may be redundant while closed histories carry a nontrivial relative
   sign.

RH is of type A. The determinant square-root cover is of type B.

A free-cover monodromy argument cannot by itself prove the RH fixed-locus theorem.

## 3. Operational theorem: local versus history observables

v20's Operational Alternative is logically correct if the operational algebra is understood
broadly enough to contain history-dependent observables.

If all O in A_op are invariant, the operational state factors through the quotient.
A nontrivial measurable holonomy is simply an O in the larger history algebra which is not
captured by pointwise local sheet labels.

The useful refinement is therefore not a logical trichotomy replacing the theorem. It is a
two-level operational audit:

- local/point observables may all descend to the quotient;
- loop/history observables may still detect nontrivial deck holonomy.

The determinant cover in v20 is the canonical example.

## 4. Z4 versus V4

The cyclic quarter-turn carrier Z4 and the four-lift carrier V4 are not isomorphic.

The correct common quotient statement is

Z4/<tau^2> ~= Z2,

V4/<D> ~= Z2.

Important correction: V4 has three nontrivial elements of order two. D is not abstractly
unique. It is distinguished only after the q/t factorization is specified and simultaneous
reversal is selected.

This finite quotient statement is formalized in

GppVerify/StandardModel/Z4V4CommonQuotient.lean.

## 5. Zitter/deck status

v20 proves an explicit three-way intertwiner between

- determinant square-root cover,
- transverse Spin(2) half-angle cover,
- free Dirac Compton double cover.

With the proper-time phase used as the lift coordinate,

zeta_perp/rho = exp(2 i omega_C tau),

and one transverse-vector circuit lasts

pi/omega_C,

at which the Dirac spinor acquires -1.

Since omega_Z=2 omega_C, this is exactly one zitterbewegung period.

This equality and the determinant/transverse/Dirac cover intertwiner are exact.

However the diagonal four-lift D on (q,t) is not thereby proved to be the same deck
transformation. That identification still needs the spin--gauge/orientation intertwiner.
Therefore write

"same period and explicitly intertwined free Dirac/determinant/transverse cover"

rather than

"D equals zitter"

until the final carrier map is constructed.

## 6. (10,2) uniqueness window

Starting from signature (6,2), adjoining n positive directions gives (6+n,2) and

p-q = 4+n.

Using the standard Majorana--Weyl congruence p-q = 0 mod 8 gives

n = 4 mod 8.

Therefore n=4 is the unique purely positive extension with total dimension below 20.
The next is n=12, giving (18,2).

The arithmetic implication has been formalized in

GppVerify/StandardModel/Spin102SignatureUniqueness.lean.

The Clifford classification itself remains standard prior art rather than something
re-proved by that Lean file.

## 7. Direct relevance to RH

v20 does NOT supply the missing arithmetic no-ghost theorem.

Its contribution is structural discipline:

1. fix the Haar metric before the spectral parameter;
2. distinguish a deck symmetry from a fixed-locus adjoint condition;
3. require an explicit intertwiner rather than an analogy of Z2 labels;
4. allow history/holonomy information without confusing it with pointwise spectral
   fixed-locus information;
5. separate a signed first-order generator Qh from its positive magnitude.

The corresponding RH target is now:

construct a zero-independent arithmetic intertwiner on the completed prime--Archimedean
boundary such that functional shadow is carried to Hilbert adjoint in the fixed Haar metric.

The already-formalized finite theorem

CayleyHaarMetricRigidity.lean

then forces the Cayley scalar to unit modulus and hence Re s=1/2.

The remaining hard theorem is the existence of that arithmetic intertwiner / causal
no-leakage completion, not the critical-line algebra once it exists.

## 8. Next construction

The v34 BPY two-copy colligation should be recast as a graph in a fundamental-symmetry
space. For a graph

G(C)={(x,Cx)},

with fundamental symmetry J=diag(I,-I),

J-positivity is exactly

||Cx|| <= ||x||.

Thus the unresolved BPY estimate is literally a contraction theorem for the graph map.
The next step is to identify the prime--Archimedean Schur transfer C explicitly and seek
a zero-independent factorization/intertwiner which makes contractivity follow from the
fixed Haar parent rather than from RH-equivalent positivity.
