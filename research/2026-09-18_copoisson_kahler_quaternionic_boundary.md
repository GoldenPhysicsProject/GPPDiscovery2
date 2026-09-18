# Co-Poisson charged-Kahler and quaternionic boundary structure

Date: 2026-09-18

The upgraded Which Way Is Forward? v14 emphasizes the standard charged-Kahler polar form

L=Q h,  Q=L/|L|,  h=|L|>=0,

and the distinction between an order-two label action and an order-four Hilbert lift.

The completed co-Poisson RH boundary already carries both structures exactly.

## 1. Completed self-adjoint boundary operator

Under the unitary Mellin transform, v34 constructs

A_xi = M_{Xi(t)} R,

where

(RF)(t)=F(-t),

and Xi(t)=xi(1/2+it) is real and even for real t.

Therefore

A_xi^*=A_xi,

A_xi^2=M_{Xi(t)^2}>=0.

Let

h_xi=|A_xi|=M_{|Xi(t)|}.

Since the real zero set is discrete and therefore null for Lebesgue measure, define a.e.

Q_xi=M_{sgn Xi(t)} R.

Because sgn Xi is real and even,

Q_xi^*=Q_xi,
Q_xi^2=I,
[Q_xi,h_xi]=0,

and

boxed(A_xi=Q_xi h_xi).

This is exactly the standard charged-Kahler signed-generator/positive-magnitude pattern,
now on the completed arithmetic Mellin boundary.

One can package it in the same two-complex-structure form by taking

J_0=i I,
I_xi=i Q_xi.

Then

J_0^2=I_xi^2=-I,
[I_xi,J_0]=0,

and

-I_xi J_0=Q_xi.

No RH assumption is used.

## 2. Canonical quaternionic quarter-turn on the +/-t pair

Let

Sigma=sgn(T),

where T=M_t is the self-adjoint dilation generator.

Reflection reverses frequency:

R Sigma = - Sigma R.

Since sgn Xi(t) is even,

Q_xi Sigma = - Sigma Q_xi.

Therefore

K_xi := Q_xi Sigma

obeys

K_xi^*=-K_xi,
K_xi^2=-I,
K_xi^4=I.

On the two-dimensional fiber associated with t>0 and -t, K_xi is, up to the sign of Xi(t),

[[0,-1],
 [1, 0]].

Thus the completed arithmetic boundary carries an exact order-four quarter-turn on each
principal-series frequency pair.  This is the infinite-dimensional analogue of the
canonical doubled quarter-turn J(x1,x2)=(x2,-x1) in Which Way Is Forward? v14.

Equivalently, the two involutions Q_xi and Sigma anticommute and generate a Cl_2 /
quaternionic two-state algebra.

Again, this uses no zero-location assumption.

## 3. Exact no-go: charged-Kahler polar form exists on every vertical line

For any real a define

A_a=M_{xi(a+it)} R.

Reality of xi gives

xi(a-it)=conj(xi(a+it)).

For a multiplication-reflection operator,

(M_f R)^*=M_{conj(f(-t))}R.

Hence

A_a^*=A_a

for EVERY real a, not only a=1/2, and

A_a^2=M_{|xi(a+it)|^2}>=0.

Therefore every vertical line carries the formal polar decomposition

A_a=Q_a |A_a|.

This proves a useful no-go:

The existence of a self-adjoint reflected generator, a positive magnitude, or a charged-
Kahler L=Qh decomposition does NOT select the critical line.

What is special at a=1/2 is not boundary self-adjointness. It is compatibility of
functional shadow a -> 1-a, complex conjugation, the fixed Haar principal-series metric,
and CAUSAL analytic realization.

## 4. Relation to the upgraded celestial section

Which Way v14 correctly distinguishes:
- bare shadow: Delta -> 2-Delta,
- coefficient conjugation: Delta -> bar Delta,
- anti-linear composition: Delta -> 2-bar Delta,
whose fixed locus is Re Delta=1.

Under Delta=2s the fixed locus is Re s=1/2.

The arithmetic statement is identical in form:
boundary reflection and self-adjointness exist much more generally, while the unitary
principal-series fixed locus occurs only when functional shadow and Hilbert conjugation
land in the same representation.

## 5. Consequence for the RH program

The new paper strengthens the geometry but does not remove the analytic wall.

The remaining theorem is NOT:
"construct a positive h and sign Q."

That is already done.

It is:
"show that the zero/resonance contribution belongs to the fixed causal principal-series
Hilbert/rigged-Hilbert realization in which functional shadow equals Hilbert adjoint."

Equivalently in Hardy language:
prove the shifted completed transfer Theta_omega is inner, i.e. its anticausal Hankel
leakage vanishes.

The first-order structures now make the target canonical and prevent metric fitting, but
arithmetic Haar admissibility / global causality remains the non-circular missing theorem.
