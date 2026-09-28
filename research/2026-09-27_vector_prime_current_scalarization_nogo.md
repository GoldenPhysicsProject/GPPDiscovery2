# Primitive prime current is already tempered before scalarization; diagonal Hilbert reconstruction is impossible

Date: 2026-09-27
Status: exact zero-independent functional-analytic reduction. No RH claim.

This note sharpens the current primitive-temperateness frontier by keeping the prime labels instead of collapsing them immediately to one scalar channel.

## 1. Vector-valued primitive current

Let H_p=ell2(P) with orthonormal basis e_p indexed by primes. Define the H_p-valued distribution on the logarithmic line

J_vec
=
sum_p (log p)/sqrt(p) e_p delta_{log p}.

For phi in S(R),

<J_vec,phi>
=
sum_p (log p)/sqrt(p) phi(log p)e_p,

and therefore exactly

||<J_vec,phi>||^2
=
sum_p (log p)^2/p |phi(log p)|^2.

Bound the prime sum by all integers and group e^k<=n<e^(k+1):

sum_{e^k<=n<e^(k+1)}
(log n)^2/n |phi(log n)|^2

<=
e (k+1)^2 sup_{x in [k,k+1]} |phi(x)|^2.

Hence for any Schwartz seminorm with N>3/2,

||<J_vec,phi>||^2
<=
C_N sup_x[(1+|x|)^N|phi(x)|]^2
sum_{k>=0}(k+1)^(2-2N).

Thus

boxed:
J_vec belongs to S'(R;ell2(P))

unconditionally, with no prime number theorem and no prime/continuum cancellation.

The primitive arithmetic channel is therefore perfectly tempered as a vector-valued boundary field.

## 2. The scalar obstruction is exactly the all-ones collapse

The scalar primitive comb is obtained formally by applying

ell_infty(e_p)=1

to every prime direction:

ell_infty J_vec
=
sum_p (log p)/sqrt(p) delta_{log p}.

But ell_infty is not a bounded functional on ell2(P).

So the exponential/temperedness difficulty is not present in the labeled prime field itself. It is created by collapsing infinitely many orthogonal prime channels into the same scalar observable.

This is the same structural obstruction already seen in the Bohr-Hardy Euler evaluation E_0.

## 3. No diagonal weighted Hilbert norm can fix both sides

One might try to repair the problem by changing only the Hilbert weights on prime labels.

Let w_p>0 and define the diagonal Hilbert norm

||c||_w^2=sum_p w_p |c_p|^2.

For the primitive coefficient vector a_p=(log p)/sqrt p to belong to H_w one needs

(A) sum_p w_p (log p)^2/p < infinity.

For the all-ones scalarization ell_infty(c)=sum_p c_p to be bounded on H_w one needs

(B) sum_p 1/w_p < infinity.

If both held, Cauchy-Schwarz would give

sum_p (log p)/sqrt p
<=
[
sum_p w_p(log p)^2/p
]^(1/2)
[
sum_p 1/w_p
]^(1/2)
<infinity.

But for all sufficiently large p,

(log p)/sqrt p > 1/p,

and Euler's prime harmonic series sum_p 1/p diverges. Contradiction.

Therefore

boxed:
there is NO positive diagonal reweighting of the prime Hilbert space
that simultaneously
(1) contains the critical primitive current as a vector and
(2) makes all-ones scalar evaluation bounded.

This kills a large class of naive graph-norm fixes.

## 4. Consequence: the missing completion must be genuinely non-diagonal

Any successful completed reconstruction must use at least one of:

- prime/Archimedean cancellation before taking the scalar observable;
- a non-diagonal graph norm coupling distinct prime directions;
- a quotient/Schur complement removing the escaping coherent mode;
- a rigged distributional boundary map rather than an ordinary bounded Hilbert functional.

Simply strengthening or weakening each prime independently cannot work.

This is important because it prevents us from wasting effort searching for a magical diagonal Sobolev weight.

## 5. Abel-regulated scalarization shows the same half-density wall

For epsilon>0 consider

ell_epsilon(e_p)=p^(-epsilon).

Its ell2 dual norm is

||ell_epsilon||^2=sum_p p^(-2epsilon).

This is finite only for epsilon>1/2.

Thus a bounded diagonal scalarization already costs a further half-density beyond the critical prime current. This is the prime-first-chaos version of the previously derived "half plus half = Euler domain" obstruction.

## 6. Relation to the primitive-temperateness RH criterion

The existing scalar criterion is that

e^(x/2) dx
-
sum_p (log p)/sqrt p delta_{log p}

extend temperedly after the exact renormalization.

The present result says:

- the labeled prime half of this expression is already tempered in a natural Hilbert-valued sense;
- the real difficulty is constructing a completed scalar reconstruction that combines the singular all-ones prime collapse with the Archimedean continuum before either is interpreted separately.

So the target can be restated more precisely:

boxed:
construct a continuous prime-Archimedean quotient map
from the vector-valued tempered boundary field
to one scalar tempered distribution,
without factoring through ell_infty.

If such a map reproduces the exact completed current, the existing Gaussian-resolvent theorem forces RH.

## 7. Heuristic warning

A no-go saying "the critical prime current is not a Hilbert vector" is representation-dependent and too crude. With prime labels retained it is an honest tempered vector distribution. The real no-go is narrower and stronger: a purely diagonal Hilbert topology cannot also support the scalar all-ones reconstruction.

That distinction should be used in future searches.
