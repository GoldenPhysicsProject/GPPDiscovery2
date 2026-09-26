# BPY S^4 harmonic audit: first-mode dominance and the moving-bottleneck no-go
Date: 2026-09-26
Status: exact analytic derivation plus route audit. No RH claim.

## 1. Exact S^4 angular harmonic data

For the universal coordinate Z with density

  w(z)=(3/4)(1-z^2),  -1<z<1,

we already have E[Z^2]=1/5.

For the worst radial rapidity f(z)=artanh(z), direct integration gives

  E[Z artanh Z] = 1/4.

Indeed, on [0,1], choose the antiderivative
  V(z)=-(1-z^2)^2/4
of z(1-z^2); the boundary term V(z)artanh(z) vanishes at both endpoints, and
integration by parts gives

  ∫_0^1 z(1-z^2)artanh(z) dz = (1/4)∫_0^1(1-z^2)dz = 1/6.

Multiplying by the even-density factor 3/2 yields 1/4.

Therefore the orthogonal projection of artanh(Z) onto the first odd spherical harmonic
span{Z} is exactly

  [E(Z artanh Z)/E(Z^2)] Z = (5/4) Z.

Its squared L2 norm is

  (25/16) E[Z^2] = 5/16.

The total rapidity norm is also exact. With z=tanh u,

  E[(artanh Z)^2]
   = (3/4) ∫_R u^2 sech^4(u) du
   = pi^2/12 - 1/2.

(The last identity follows from the standard Fourier transform of sech^4, equivalently
from the trigamma value psi_1(2)=pi^2/6-1.)

Hence the higher odd harmonics have total squared norm

  pi^2/12 - 13/16
  ≈ 0.00996703342411322.

So even at the extreme R=1, the first odd S^4 harmonic carries about 96.91% of the
relative-rapidity L2 energy. Numerically the fraction is even larger for R<1.

This explains why the one-fifth scale is so persistent: the BPY rapidity is overwhelmingly
a first-harmonic deformation of the S^4 coordinate.

## 2. Why this still does not prove transfer contractivity

The actual half-density BPY law is not the raw two-copy Gaussian law.

Writing the two un-tilted radial variables as Q1,Q2 and

  T=Q1+Q2,
  C=(Q1-Q2)/(Q1+Q2)=R Z,

the half-density two-copy tilt contributes

  (Q1 Q2)^(1/4)
  = const * T^(1/2) (1-R^2 Z^2)^(1/4).

Moreover, with x=(1/2)log Q1, y=(1/2)log Q2, the BPY reflection measure contains

  u sinh(omega u),
  u=x+y
   = log(T/2) + (1/2)log(1-R^2 Z^2).

Thus the physical angular weight on a fixed (T,R) slice is the S^4 density multiplied by
an additional even factor involving u sinh(omega u).

## 3. Exact moving-bottleneck obstruction to a slice-wise Poincare proof

For every R>0 there are radial slices satisfying

  2 < T < 2/sqrt(1-R^2).

On such a slice,

  u(0)=log(T/2)>0,

while

  u(1)=log[(T/2)sqrt(1-R^2)]<0.

Hence there is z0 in (0,1) with u(z0)=0. For omega>0,

  u sinh(omega u) = omega u^2 + O(u^4),

and u'(z0) is nonzero. Therefore the physical fixed-slice angular density has a quadratic
zero,

  W(z) ~ const * (z-z0)^2.

The same is true at -z0.

This destroys any uniform slice-wise weighted Poincare gap. An odd test function can be
chosen approximately zero on |z|<z0, approximately sign(z) outside, and smoothed across
width epsilon at ±z0. Its L2 norm stays bounded below while its weighted angular Dirichlet
energy is O(epsilon), because

  ∫_{-epsilon}^{epsilon} x^2*(1/epsilon^2) dx = O(epsilon).

Therefore the beautiful raw S^4 spectral gap cannot, by itself, prove

  ||P_- f|| <= ||P_+ f||

for the completed BPY measure.

This is a useful no-go: the missing estimate cannot be a fixed-(T,R) angular Poincare
inequality.

## 4. What survives: a global hypocoercive target

The bottleneck location z0=z0(T,R) moves with the radial variables. A test function that
hides its angular derivative at the zero of one slice cannot do so coherently across all
radial slices without developing radial/center variation.

That points to a genuinely global estimate of hypocoercive type:

  angular odd energy + center/radial transport energy
    >= c * odd L2 energy,

with the first-order BPY null/Dirac system supplying the coupling between angular and
center derivatives.

This fits the previously derived equations

  partial_c U + partial_d V = 0,
  partial_c V + partial_d U = 0.

The next experiment should therefore stop trying to prove positivity on each fixed center
or fixed radial slice. Instead build a two-variable coercivity estimate in which the moving
quadratic zero is controlled by the transverse transport derivative. This is exactly the
kind of mechanism by which hypocoercivity restores a gap when each fiber separately has
zero gap.

The raw S^4 constants 1/5 and spectral gap 4 remain useful as the angular component of
that estimate; they are not the whole estimate.
