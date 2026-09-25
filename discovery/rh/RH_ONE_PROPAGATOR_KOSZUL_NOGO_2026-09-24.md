# RH correction — naive one-propagator Koszul Green extraction cannot equal the Euler logarithmic derivative
## Date: 2026-09-24
## Status: exact finite-dimensional analytic obstruction

This note tests the immediate Feshbach idea suggested by the corrected causal many-prime gap.

The causal many-prime Hodge--Dirac has a strong inverse bound on the critical line, but the exact zeta prime observable cannot be a plain fixed matrix element of that positive Hodge inverse. The obstruction is already visible in the scalar CAR model.

## 1. Scalar CAR model

Let (t=(t_1,dots,t_n)inmathbb C^n) and let
[
D(t)=sum_{j=1}^n
left(t_jarepsilon_j+overline{t_j},iota_jight)
]
on the finite fermionic Fock space.

The CAR give
[
D(t)^2=E(t)I,
qquad
E(t)=sum_j|t_j|^2.
]

Whenever (E(t)
e0),
[
oxed{
D(t)^{-1}=rac{D(t)}{E(t)}.
}
]

Therefore every fixed matrix element of (D(t)^{-1}) is of the form
[
rac{	ext{linear combination of }t_j,overline{t_j}}
{sum_j|t_j|^2}.
]

A product of a fixed finite number (r) of such Green operators has denominator only a power
[
E(t)^r.
]

## 2. Euler logarithmic derivative has incompatible singularities

For commuting local Euler holonomies (t_j(z)), the logarithmic derivative of the product is
[
rac{d}{dz}logprod_jt_j(z)
=
sum_jrac{t_j'(z)}{t_j(z)}.
]

This has an individual pole on the hypersurface
[
t_j(z)=0
]
even when all other (t_k(z)
e0).

By contrast, the Hodge denominator
[
E(t)=sum_j|t_j|^2
]
does not vanish there if any other channel remains nonzero.

Hence for (nge2) the Euler logarithmic derivative cannot equal a fixed matrix element of (D^{-1}), nor a fixed finite product of (D^{-1})'s with coefficients analytic and nonsingular at the individual local-zero hypersurfaces.

Any attempted equality must put the missing (t_j^{-1}) singularities into the boundary/source vectors themselves. That merely moves the ill-conditioning into the coupling and forfeits the claimed free gain from the collective Hodge gap.

## 3. Holomorphy/positivity tension

There is a second version of the same obstruction.

The positive Hodge square necessarily uses adjoints:
[
D^2=sum|t_j|^2 I.
]
Its inverse is nonholomorphic in the spectral parameter because it depends on (overline{t_j}).

The zeta logarithmic derivative is holomorphic/meromorphic:
[
sum_j t_j'(z)t_j(z)^{-1}.
]

Thus a positive self-adjoint Hodge inverse cannot by itself preserve the analytic phase required by the zeta observable.

This is the finite-CAR analogue of the already-known chiral-Hermitianization warning: modulus-square determinants are positive but lose analytic phase.

## 4. Consequence for the current RH program

The corrected causal many-prime gap remains useful:
[
|D_L^{-1}|=O(sqrt L e^{-L/2}).
]

But the missing completed scalar map cannot simply be
[
langle y_L,D_L^{-1}x_Langle
]
with fixed regular boundary vectors and be exactly the Euler logarithmic derivative.

The viable architectures are narrower:

1. a genuinely chiral Green function whose cross block retains (M_L^{-1}=Z_L);
2. a top-degree/determinant-line insertion carrying the Euler product before Hodge scalarization;
3. a Schur/Feshbach system whose boundary couplings themselves encode the local inverses but whose completed pole/Archimedean sector cancels their coherent exponential norm;
4. or the corrected Nevanlinna/Hermite route, which bypasses this factorization entirely.

The first two preserve analytic phase but do not inherit the many-prime Hodge gap for free. Therefore the next proof attempt must explicitly show how the chiral analytic response is controlled by the massive Hodge parent without hiding an exponential boundary coupling.

This obstruction should be used as a cheap falsifier for future Feshbach proposals.
