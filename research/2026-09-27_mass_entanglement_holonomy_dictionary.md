# Exact mass--entanglement--holonomy dictionary of the prime modular mode

Date: 2026-09-27
Status: exact identities inside the finite-place TFD/SU(1,1) model. No claim that this alone derives Standard Model masses.

For one prime mode write

a=tanh(kappa)=p^(-1/2),
C=sinh^2(kappa),
mu=2 sinh(kappa),

so

mu^2=4C=4/(p-1).

Let G(kappa) be the real SU(1,1) transfer matrix

G(kappa)
=
[[cosh kappa,-sinh kappa],
 [-sinh kappa,cosh kappa]].

Then

det G=1,
Tr G=2 cosh kappa,

and therefore

boxed:
mu^2=(Tr G)^2-4.

Thus the mass-square coordinate is the hyperbolic conjugacy discriminant of the local Euler/Blaschke scattering holonomy.

## Entanglement negativity

The two-mode TFD state has Schmidt ratio tanh(kappa). Its logarithmic negativity is

E_N=2 kappa.

Therefore

boxed:
E_N
=
2 arcosh(Tr G/2),

and

boxed:
mu
=
2 sinh(E_N/2).

Equivalently,

boxed:
mu^2
=
4 sinh^2(E_N/2).

So mass, entanglement negativity, and the transfer conjugacy class are one-to-one coordinates on the same local SU(1,1) orbit.

## Purity

The reduced state has geometric spectrum

rho=(1-a^2) sum_{n>=0} a^(2n) |n><n|.

Its purity is

P=Tr rho^2
 =(1-a^2)/(1+a^2).

Using a=tanh kappa,

P=sech(2 kappa).

Since E_N=2 kappa,

boxed:
P=sech(E_N).

Using mu^2=4 sinh^2 kappa gives

cosh(2 kappa)=1+2 sinh^2 kappa=1+mu^2/2,

hence

boxed:
P=1/(1+mu^2/2).

Thus the local mass coordinate can also be reconstructed directly from reduced-state purity:

boxed:
mu^2=2(P^(-1)-1).

For the prime mode this becomes

P_p=(p-1)/(p+1),

which is equivalent to mu_p^2=4/(p-1).

## Covariance

The completed covariance is

Gamma
=
[[C+1/2,A],
 [A,C+1/2]],

with

A=sinh kappa cosh kappa.

Its trace is

Tr Gamma
=
cosh(2 kappa)
=
cosh(E_N)
=
1+mu^2/2.

Therefore

boxed:
mu^2=2(Tr Gamma-1).

Since det Gamma=1/4, this is a pure Gaussian covariance. The finite-place mass is exactly its excess trace above the vacuum covariance.

## Cayley coordinate

The finite-place Cayley coordinate is

r_C
=
(sqrt(p)-1)/(sqrt(p)+1)
=
e^(-2 kappa)
=
e^(-E_N).

Therefore

boxed:
E_N=-log r_C.

So the previously separate quantities

- p-adic Cayley contraction,
- TFD logarithmic negativity,
- SU(1,1) boost length,
- finite-place mass coordinate,
- reduced-state purity,

are exact reparameterizations of one local invariant.

A compact exact dictionary is

r_C=e^(-E_N),

P=sech(E_N),

mu=2 sinh(E_N/2),

Tr G=2 cosh(E_N/2),

mu^2=(Tr G)^2-4.

## Two-sheet orientation

Orientation reversal sends

kappa -> -kappa,
G -> G^(-1).

It leaves

mu^2,
P,
|E_N|

unchanged, while reversing the oriented boost parameter and the anomalous covariance.

For an inverse-holonomy pair,

G(kappa)G(-kappa)=I,

so the composite conjugacy discriminant vanishes even though each marginal sheet has the same nonzero mass invariant.

This cleanly separates two statements:

1. time-orientation reversal does not erase local mass or local entanglement;
2. sewing the inverse holonomies can erase the **relative/composite holonomy gap**.

A physical horizon-annihilation model still needs a unitary boundary interaction carrying the conserved energy/charges into outgoing channels, but the group-theoretic cancellation mechanism itself is exact.
