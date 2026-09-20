# BPY reflection as a reversible Markov operator: RH is one-step spectral positivity

Date: 2026-09-20

The two-copy BPY colligation admits a sharper probability/operator interpretation.

## 1. Normalize the positive BPY measure

For fixed omega>0 let

d mu_omega(t,x,y)
=
(x+y)sinh(omega(x+y))q(x)q(y) dt dx dy

and divide by its finite total mass to obtain a probability measure P_omega.

Define the two oriented scalar observables

A=(1-t)y-tx,
B=(1-t)x-ty.

The swap J:(t,x,y)->(t,y,x) exchanges A and B and preserves P_omega, so (A,B)
is an exchangeable pair and A,B have the same marginal rho_omega.

## 2. The exponential subspace is the full A-observable sector

Define

U_A:L2(rho_omega)->L2(P_omega),
(U_A f)(t,x,y)=f(A).

U_A is an isometry.

The BPY generators are U_A(e_z), with e_z(a)=exp(i z a).

Because q has super-exponential decay, the A marginal has exponential moments of all
orders. Boundary characters exp(i t a), t real, are L2 limits of e_{t+i epsilon} as
epsilon down to zero. If f is orthogonal to all real Fourier characters, the finite
complex measure f(a) rho_omega(da) has identically zero Fourier transform, hence f=0.

Therefore the closure of the BPY exponential span is exactly

M_omega = U_A L2(rho_omega).

So no hidden restriction to a small analytic test class remains at this stage.

## 3. Canonical Markov operator

Define

K_omega=U_A^* J U_A.

Then

(K_omega f)(a)=E_omega[f(B)|A=a].

Because (A,B) is exchangeable:

K_omega^*=K_omega.

Because conditional expectation is Markov:

K_omega 1=1,
K_omega preserves positivity,
||K_omega||<=1.

Hence

spec(K_omega) subset [-1,1]

unconditionally.

The BPY reflection form becomes

<J U_A f,U_A f>
=
<f,K_omega f>.

Therefore

boxed(RH iff K_omega >=0 for every omega>0).

In words: RH is the assertion that the one-step orientation-exchange Markov operator has
no negative spectrum.

## 4. Relation to the even/odd graph transfer

Let

V_+=P_+U_A,
V_-=P_-U_A.

Then

V_+^*V_+=(I+K_omega)/2,
V_-^*V_-=(I-K_omega)/2.

Whenever I+K_omega is injective on the relevant support, the BPY angular/graph operator
C_omega defined by C_omega V_+=V_- satisfies, after the canonical normalization by
(I+K_omega)^(1/2),

C_omega^*C_omega
~=
(I-K_omega)(I+K_omega)^(-1).

Thus

||C_omega||<=1
iff
K_omega>=0.

This is the exact operator bridge between the v34 graph-contraction criterion and the
new reversible-Markov formulation.

## 5. "Do not square too early" becomes literal

Since K_omega is self-adjoint,

K_omega^2>=0

for every omega, with no RH input.

K_omega^2 is the two-step orientation exchange A->B->A. It has forgotten the sign of every
one-step eigenvalue.

Thus the project's first-order sign principle appears again in an exact probabilistic form:

one-step K may have negative spectrum;
two-step K^2 is automatically positive.

Any argument that only controls the two-step/Gibbs square cannot prove RH.

## 6. Half-step factorization target

A sufficient zero-independent closure would be an explicit factorization

K_omega=L_omega^* L_omega

constructed directly from the BPY/Gaussian/arithmetic data.

An especially strong form would be a latent variable Z for which A and B are conditionally
independent with the same conditional law:

P(A in da,B in db)
=
int P_z(da) P_z(db) d lambda(z).

Then for every f,

E[conj(f(A))f(B)]
=
int |int f(a)P_z(da)|^2 d lambda(z)
>=0,

and RH follows.

This conditional-iid representation is not presently known and may be stronger than
necessary. The obvious midpoint c=(A+B)/2 cannot serve by itself, because conditional on
c the relation A+B=2c leaves A and B perfectly mirror-correlated rather than independent.

The practical target is therefore to find a genuine arithmetic/Gaussian half-step carrier,
not merely a deterministic midpoint.

## 7. Joint-density form

The coordinate pullback kernel H_omega(a,b) from v34 is the unnormalized joint density of
(A,B). The Markov kernel is

K_omega(a,db)
=
H_omega(a,b) db / m_omega(a),

where

m_omega(a)=int H_omega(a,b) db.

The density H_omega(a,b) is pointwise positive, but pointwise positivity is not operator
positivity. RH is exactly positive definiteness of this positive bivariate kernel.

For a+b>=0 there is the exact directional Gram difference

H_omega(a,b)
=
int_0^infinity [
 g_+(a+t)g_+(b+t)
 -
 g_-(a+t)g_-(b+t)
] dt,

where

g_+(x)=e^{omega x}q(x),
g_-(x)=e^{-omega x}q(x)=g_+(-x).

Thus the one-step Markov positivity problem is equivalently a domination problem between
the positive-time tilted Hankel channel and its reflected channel.

This is the current constructive frontier.