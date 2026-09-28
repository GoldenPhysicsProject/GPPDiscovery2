# Zeta coherent-state geometry: an emergent asymptotically AdS2 arithmetic bulk

Date: 2026-09-27
Status: exact RKHS / quantum-geometric identities and pole asymptotics. No RH assumption and no zero data.

This note turns the arithmetic-holography picture into a canonical metric construction rather than imposing the Poincare metric by hand.

## 1. The Dirichlet Hardy space is the canonical arithmetic bulk Hilbert space

Let

H_D^2
=
{ f(s)=sum_{n>=1} a_n n^{-s} : sum_n |a_n|^2 < infinity }.

Equivalently, via the Bohr transform, this is H2_+(K_ar) on the compact prime torus.

For w with Re(w)>1/2, point evaluation is bounded by Cauchy-Schwarz:

|f(w)|
<=
||a||_2 [sum_n n^{-2 Re(w)}]^(1/2)
=
||f|| [zeta(2 Re(w))]^(1/2).

The reproducing kernel is therefore

boxed:
K(s,w)=zeta(s+conj(w)).

Indeed

K_w = sum_n n^{-conj(w)} e_n,

and <f,K_w>=f(w).

Thus zeta itself is the canonical reproducing kernel of the arithmetic Hardy bulk.

## 2. Normalized arithmetic coherent states

For s=sigma+i t, sigma>1/2, define

|Omega_s>
=
1/sqrt(zeta(2 sigma))
sum_{n>=1} n^{-s}|n>.

Then

boxed:
<Omega_w|Omega_s>
=
zeta(s+conj(w))
/
sqrt[zeta(2 Re(s)) zeta(2 Re(w))].

At equal radial coordinate sigma,

boxed:
<Omega_{sigma+i u}|Omega_{sigma+i t}>
=
zeta(2 sigma+i(t-u))/zeta(2 sigma).

This is exactly the coherent kernel already encountered in the critical KMS construction.

As sigma decreases to 1/2, the diagonal remains one while every fixed off-diagonal overlap tends to zero because zeta(2 sigma) diverges whereas zeta(1+i(t-u)) is finite for t!=u. The principal-series boundary therefore appears as an orthogonalized continuum limit of normalizable bulk coherent states.

## 3. Exact quantum information metric

Let

beta=2 sigma,

and let P_beta be the zeta Gibbs law

P_beta(n)=n^(-beta)/zeta(beta).

The logarithmic arithmetic Hamiltonian is E_n=log n.

The coherent-state Fubini-Study / quantum metric coefficient is

boxed:
g(s)
=
partial_s partial_conj(s) log K(s,s)
=
(d^2/d beta^2) log zeta(beta).

Equivalently,

boxed:
g(s)=Var_beta(log N)>0.

A direct state calculation gives the same result:

|| (1-|Omega><Omega|) partial_sigma Omega ||^2
=
|| (1-|Omega><Omega|) partial_t Omega ||^2
=
Var_beta(log N),

and the real cross term vanishes.

Using the standard quantum-information line-element convention,

boxed:
ds_Q^2
=
4 g(sigma)
[d sigma^2+d t^2].

So the arithmetic bulk metric is the Fisher information metric of the zeta Gibbs state.

## 4. The zeta pole generates an AdS2 conformal boundary

Write

sigma=1/2+r,
beta=1+2r,
r>0.

From the Laurent expansion

zeta(1+delta)=1/delta+gamma+O(delta),

we have

log zeta(1+delta)
=
-log delta + O(delta),

and hence

(d^2/d delta^2)log zeta(1+delta)
=
1/delta^2+O(1).

With delta=2r,

boxed:
g(r)
=
1/(4r^2)+O(1).

Therefore

boxed:
ds_Q^2
=
[d r^2+d t^2]/r^2
+
O(1)[d r^2+d t^2].

The critical half-density line r=0 is thus an asymptotically hyperbolic / Euclidean-AdS2 conformal boundary generated solely by the zeta pole and Hilbert-space normalization.

The AdS2 geometry was not imposed.

## 5. Curvature tends exactly to the Poincare value

Put

lambda(r)=4 g(r),

so the metric is

ds_Q^2=lambda(r)(dr^2+dt^2).

Its Gaussian curvature is

K_G(r)
=
-[1/(2 lambda(r))] d^2/dr^2 log lambda(r).

Since lambda(r)=r^(-2)+O(1),

boxed:
K_G(r) -> -1
as r down to 0.

Thus the critical arithmetic boundary has unit-radius hyperbolic asymptotics in this convention.

Numerical controls using only zeta on the absolutely convergent real axis give:

r=1.00: K_G=-1.2780177466
r=0.50: K_G=-1.0667114278
r=0.20: K_G=-1.0076850404
r=0.10: K_G=-1.0012352455
r=0.05: K_G=-1.0001776469
r=0.02: K_G=-1.0000124345
r=0.01: K_G=-1.0000016030.

No zero ordinates enter this test.

## 6. Exact Berry connection and uniform magnetic field in the information metric

For the normalized coherent state,

A_t
=
i<Omega_s,partial_t Omega_s>
=
E_beta[log N]
=
-zeta'(beta)/zeta(beta),

while A_sigma=0 in the natural real gauge.

Differentiate with respect to sigma:

partial_sigma A_t
=
-2 (log zeta)''(beta)
=
-2 g.

Hence the Berry curvature is

boxed:
F
=
-2 g d sigma wedge d t.

The metric area form is

dA_Q
=
4 g d sigma wedge d t.

Therefore

boxed:
F = -(1/2) dA_Q.

So the arithmetic coherent-state bulk carries an EXACT constant Berry magnetic field relative to its own quantum-information area form, not merely an asymptotic one.

This is a strong SU(1,1)/Landau-level style signal and may be relevant to the repeatedly observed k=1/2 module.

## 7. The radial coordinate is an information/RG coordinate

As sigma increases, higher integer energies are exponentially suppressed and

|Omega_s> -> |1>.

Thus:
- r=0 is the critical infinite-distance conformal boundary;
- increasing r is radial coarse-graining by exp[-r log N];
- the deep bulk approaches the trivial arithmetic vacuum n=1.

The proper radial distance to r=0 diverges logarithmically because sqrt(lambda)~1/r.

So the principal-series boundary is genuinely at infinite information distance, just like an AdS conformal boundary.

## 8. Relation to the two-sheet picture

The normalizable coherent-state construction produces one sheet Re(s)>1/2.

The functional equation of the completed theory supplies the reflected sheet Re(s)<1/2.

After conformal compactification of the asymptotically hyperbolic metric, the common boundary is the critical line plus its projective point at infinity, RP1~=S1. A reflected copy may then be Schottky-doubled across that boundary.

Important distinction:
the second sheet is NOT obtained by analytically continuing the positive Hilbert norm zeta(2 sigma) through its pole. It is a reflected/completed copy supplied by the xi functional equation.

This avoids a naive positivity-continuation error.

## 9. What this contributes to RH

The coherent-state geometry proves unconditionally that:
- the critical line is the natural conformal boundary of the arithmetic H2 bulk;
- the boundary dimension is one;
- the half-density 1/2 is the normalizability threshold;
- the bulk is asymptotically AdS2;
- the prime Gibbs state carries an exact quantum metric and Berry curvature.

It still does not place the nontrivial xi zeros.

The RH-bearing theorem remains the completed prime-Archimedean reconstruction: show that the collective fluctuation/Weyl/Fredholm response of the doubled physical bulk is positive/self-adjoint and equals the exact completed xi response.

The gain is that the previously heuristic "arithmetic AdS2" now has a canonical Hilbert space, reproducing kernel, metric, radial semigroup, and conformal boundary before RH is assumed.
