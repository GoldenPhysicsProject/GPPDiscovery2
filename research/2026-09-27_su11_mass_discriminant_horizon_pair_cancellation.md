# SU(1,1) transfer discriminant as the finite-place mass coordinate, and two-sheet cancellation

Date: 2026-09-27
Status: exact local/group identities plus an explicitly conditional horizon interpretation. No RH claim and no claim that observed particle masses are given by this arithmetic invariant.

## 1. The prime Blaschke channel has a canonical SU(1,1) transfer matrix

For a prime p define

a_p = p^(-1/2),
kappa_p = artanh(a_p).

The real SU(1,1)/SO(1,1) transfer representative of the Blaschke automorphism is

G_p
=
1/sqrt(1-a_p^2)
[[1,-a_p],[-a_p,1]].

Equivalently,

G_p
=
[[cosh kappa_p,-sinh kappa_p],
 [-sinh kappa_p,cosh kappa_p]],

so

det G_p = 1

and its eigenvalues are

e^(+kappa_p), e^(-kappa_p).

## 2. Exact mass-discriminant identity

The trace is

Tr G_p = 2 cosh kappa_p.

Therefore its hyperbolic conjugacy discriminant is

(Tr G_p)^2 - 4
=
4 sinh^2 kappa_p.

But the finite-place mass/Casimir coordinate is

mu_p = 2 sinh kappa_p
     = 2/sqrt(p-1).

Hence

boxed:
mu_p^2 = (Tr G_p)^2 - 4 = 4/(p-1).

So the finite-place mass-square coordinate is exactly the conjugacy-class discriminant of the local SU(1,1) Euler/Blaschke transfer matrix.

This is stronger than treating mu_p as an independently assigned mass coordinate: it is already encoded in the local scattering holonomy.

## 3. The positive TFD covariance is one half the squared inverse transfer

Let

C_p = sinh^2 kappa_p,
A_p = sinh kappa_p cosh kappa_p.

The completed two-mode covariance is

Gamma_p
=
[[C_p+1/2,A_p],
 [A_p,C_p+1/2]]
=
1/2
[[cosh(2 kappa_p),sinh(2 kappa_p)],
 [sinh(2 kappa_p),cosh(2 kappa_p)]].

With the sign convention above,

G_p^(-2)
=
[[cosh(2 kappa_p),sinh(2 kappa_p)],
 [sinh(2 kappa_p),cosh(2 kappa_p)]].

Therefore

boxed:
Gamma_p = (1/2) G_p^(-2).

Thus the same local object appears in three exactly equivalent forms:

- Blaschke/Euler transfer G_p;
- TFD covariance Gamma_p;
- mass discriminant mu_p^2=(Tr G_p)^2-4.

The determinant identity det Gamma_p=1/4 follows immediately from det G_p=1.

## 4. The Cayley coordinate is the squeezed eigenvalue ratio

The covariance eigenvalues are

lambda_- = (1/2)e^(-2 kappa_p),
lambda_+ = (1/2)e^(+2 kappa_p).

Therefore

lambda_-/lambda_+
=
e^(-4 kappa_p),

while the square-root ratio is

sqrt(lambda_-/lambda_+)
=
e^(-2 kappa_p)
=
(1-a_p)/(1+a_p)
=
(sqrt(p)-1)/(sqrt(p)+1).

This is exactly the finite-place Cayley coordinate already present in the arithmetic conformal construction.

## 5. Orientation reversal is group inversion and preserves one-sheet mass

Let J be the orientation involution satisfying

J G(kappa) J = G(-kappa)=G(kappa)^(-1).

Because trace is invariant under inversion in SL(2),

Tr G^(-1)=Tr G,

and therefore

mu^2(G^(-1))=mu^2(G).

So a t-orientation reversal does not make an individual massive sheet massless. It reverses the orientation holonomy while preserving its conjugacy-class mass invariant.

This agrees with the earlier covariance result: normal occupation C=sinh^2 kappa is even in kappa, while anomalous pairing A=sinh kappa cosh kappa is odd.

## 6. But the sewn two-sheet holonomy has exactly zero discriminant

For opposite sheets carrying inverse holonomies,

G_+ = G(kappa),
G_- = G(-kappa)=G_+^(-1),

their composed holonomy is

boxed:
G_pair = G_+ G_- = I.

Its discriminant is

boxed:
(Tr G_pair)^2 - 4
=
(Tr I)^2 - 4
=
4-4
=
0.

This gives an exact algebraic distinction:

- each sheet separately carries the same nonzero mass discriminant;
- the orientation-paired composite has zero net SU(1,1) discriminant.

Therefore a horizon fixed point that geometrically sews inverse orientation holonomies can annihilate the **relative mass holonomy** without requiring either constituent to become individually massless before sewing.

This is the cleanest algebraic version found so far of the earlier intuition that opposite time-orientation components can close on themselves at a null boundary.

## 7. Conditional horizon interpretation

The following step is a hypothesis, not yet a theorem of the spacetime model:

If the physical mass of the doubled boundary pair is controlled by the conjugacy discriminant of the composed orientation holonomy, then the branch-point sewing

G(kappa)G(-kappa)=I

forces the paired boundary channel onto the null/massless conjugacy class.

Energy conservation would then require the incoming massive pair energy to leave through another channel, naturally a null radiation channel.

This would realize

massive oriented pair
 -> inverse-holonomy sewing
 -> zero composite mass discriminant
 -> null outgoing channel,

without asserting that one charged fermion by itself disappears or crosses the horizon.

## 8. Prime p=5

For p=5,

a_5=1/sqrt(5),
kappa_5=log(phi),
mu_5=1.

Hence

(Tr G_5)^2-4=1.

The two eigenvalues of G_5 are

phi, phi^(-1),

and the completed covariance eigenvalues are

phi^2/2, phi^(-2)/2.

Thus the previously separate golden identities are all the same conjugacy class:

p=5
<-> kappa=log phi
<-> spec(G)={phi,phi^(-1)}
<-> discriminant(G)=1
<-> mu=1
<-> covariance eigenvalues={phi^2/2,phi^(-2)/2}.

## 9. Global renormalized boost

The raw total prime rapidity

sum_p kappa_p

diverges because

kappa_p = a_p + a_p^3/3 + a_p^5/5 + ...

and sum_p a_p=sum_p p^(-1/2) diverges.

But after subtracting the primitive tangent,

boxed:
K_ren
=
sum_p [atanh(p^(-1/2))-p^(-1/2)]

converges absolutely, since the summand is O(p^(-3/2)).

Hence the renormalized product of the local boost matrices,

prod_p exp(+a_p sigma_x) G_p,

converges to the finite group element

boxed:
G_ren = exp(-K_ren sigma_x).

This is the group-valued counterpart of the det3 subtraction.

Importantly, only the first (odd/tangent) jet appears in the rapidity. The second divergent channel enters through the scalar TFD vacuum normalization rather than through the SU(1,1) boost itself.

That explains why the two critical channels have different operator meanings:

m=1 = divergent total orientation rapidity / tangent;
m=2 = divergent scalar vacuum-normalization / covariance determinant;
m>=3 = convergent nonlinear dressing.

## 10. Exact endpoint relation to det3

At s=1/2 the normalized TFD dressing multiplier is

f_p(1/2)
=
sqrt(1-p^(-1))/(1-p^(-1/2))
=
exp(kappa_p).

After primitive renormalization,

prod_p exp(kappa_p-a_p)
=
exp(K_ren).

The det3 factorization found previously gives

boxed:
exp(K_ren)
=
C_vac det_3(I-D(1/2))^(-1),

where

C_vac
=
prod_p sqrt(1-p^(-1)) exp(1/(2p))

is finite and positive.

Thus the critical det3 endpoint decomposes exactly into

- a renormalized SU(1,1) orientation boost;
- a finite scalar vacuum normalization.

This is a concrete group/scalar factorization of the two-channel renormalization.
