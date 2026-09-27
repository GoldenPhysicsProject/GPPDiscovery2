# After primitive renormalization the global prime scattering phase has finite half-derivative energy

Date: 2026-09-27
Status: exact almost-periodic coefficient estimate. It sharpens the m=1 versus m=2 distinction. No RH proof.

## 1. Local relative phase

For a prime p let

a_p=p^(-1/2),
L_p=log p.

On the real spectral axis the relative Euler scattering factor is

S_p(T)
=
(1-a_p e^(iL_pT))/(1-a_p e^(-iL_pT)),

with |S_p(T)|=1.

Choose the logarithm continuously from a_p=0. Then

log S_p(T)
=
-2i sum_{m>=1} a_p^m sin(mL_pT)/m

(up to the overall orientation sign convention).

The frequencies are

lambda_{p,m}=m log p=log(p^m).

By unique factorization,

m log p = n log q

for primes p,q and positive m,n implies p=q and m=n.

Thus all positive prime-power frequencies are distinct.

## 2. Natural Bohr H^(1/2) energy

For an almost-periodic Fourier series

f(T)=sum_lambda c_lambda e^(i lambda T),

define the formal homogeneous half-derivative energy

E_{1/2}(f)
=
sum_lambda |lambda| |c_lambda|^2.

For one local prime phase, both +/- frequencies occur. Its contribution is

E_{1/2,p}
=
2 sum_{m>=1}
(m L_p)
(a_p^(2m)/m^2)

=
2 L_p
sum_{m>=1} p^(-m)/m.

Therefore

boxed:
E_{1/2,p}
=
-2(log p) log(1-p^(-1)).

## 3. The unrenormalized global phase has infinite half-derivative energy

Summing over primes,

E_{1/2}^{raw}
=
2 sum_p
(log p)
sum_{m>=1} p^(-m)/m.

The m=1 contribution is

2 sum_p (log p)/p,

which diverges.

Hence the raw critical prime scattering phase is not a finite-energy H^(1/2)-type almost-periodic phase.

This is a precise functional-space version of the primitive-channel obstruction.

## 4. Remove only the primitive harmonic

Define the primitive-renormalized local phase

log S_p^{(>=2)}(T)
=
-2i
sum_{m>=2}
a_p^m sin(mL_pT)/m.

Its global half-derivative energy is

E_{1/2}^{(>=2)}
=
2 sum_p
(log p)
sum_{m>=2} p^(-m)/m.

Equivalently,

boxed:
E_{1/2}^{(>=2)}
=
2 sum_p
(log p)
[-log(1-p^(-1))-p^(-1)].

Since

-log(1-p^(-1))-p^(-1)
=
O(p^(-2)),

and

sum_p (log p)/p^2 < infinity,

we obtain

boxed:
E_{1/2}^{(>=2)} < infinity.

So subtracting the primitive m=1 tangent is already enough to place the remaining global phase in the natural half-derivative energy class.

## 5. Why m=2 still matters for determinants

This result does not contradict the det3 threshold.

For the scalar Euler determinant, absolute trace/nuclear summability sees the coefficients linearly. The second channel contains

sum_p p^(-1),

which diverges, so m=2 must also be removed before an ordinary regularized determinant is available at the critical boundary.

For the unitary phase energy, coefficients are squared. The m=2 harmonic contributes at size

sum_p
(log p)
(p^(-1))^2

=
sum_p (log p)/p^2,

which converges.

Therefore:

boxed:
m=1 = obstruction to finite H^(1/2) scattering-phase energy;

boxed:
m=2 = additional obstruction to scalar trace/determinant summability.

This is a sharper functional distinction between the two exceptional channels.

## 6. Group versus determinant renormalization

The SU(1,1) boost rapidity has

kappa_p
=
atanh(a_p)
=
a_p+a_p^3/3+a_p^5/5+...

and requires only subtraction of the primitive a_p term for absolute convergence of the global rapidity.

Likewise the unitary scattering phase requires only primitive subtraction to acquire finite half-derivative energy.

But the normalized TFD scalar dressing contains both a first jet and a second vacuum-normalization jet, and its infinite product is naturally det3-renormalized.

This yields a consistent hierarchy:

1. orientation/group sector:
   remove m=1;

2. unitary phase / restricted-energy sector:
   remove m=1;

3. scalar determinant line:
   remove m=1 and m=2;

4. m>=3:
   ordinary nuclear/Fredholm tail.

This suggests that the two-channel Archimedean completion should not treat m=1 and m=2 symmetrically.

The primitive channel should repair the global scattering/implementability geometry.

The double-prime channel should repair the scalar determinant/vacuum normalization over that already-renormalized unitary geometry.

## 7. Possible global construction target

A promising order of construction is therefore:

first construct a renormalized unitary prime scattering operator from the primitive-subtracted phase in its finite H^(1/2) energy space;

then construct its determinant line by the second m=2 renormalization;

finally sew the Archimedean compact ladder and rational endpoint factors.

If the first step admits an analytic causal extension to the physical half-plane and the determinant line reproduces xi, the remaining positivity problem becomes much more rigid than a generic prime--Archimedean domination inequality.

The analytic/casual extension is still the unresolved theorem.
