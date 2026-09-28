# Double projection: the arithmetic k=1/2 sheet doubles to the celestial weight-one layer

Date: 2026-09-27
Status: exact geometric and spectral identities plus a representation-theoretic synthesis. This is not a derivation of 4D gravity.

## 1. One arithmetic sheet

The zeta-pole boundary kernel is, after Cayley transformation,

K_{1/2}(u,v)=(1-u conj(v))^(-1),

the holomorphic SU(1,1) kernel with lowest weight k=1/2.

Its noncompact generator K1 has vacuum spectral density

dmu_1(x)=sech(pi x) dx.

The one-dimensional conformal boundary simultaneously carries the principal-series half-density

Re Delta_1=1/2.

## 2. Geometric double

The disk/right-half-plane has conformal boundary RP1~=S1.

Doubling a disk across its boundary gives the Riemann sphere

boxed:
Double(D)=CP1~=S2.

This is the same geometric step already identified in the arithmetic-to-celestial projection picture.

## 3. Spectral double

Take two copies of the universal k=1/2 module and the summed noncompact generator

J=K1 tensor I + I tensor K1.

The product-vacuum characteristic function is

<0,0|exp(-itJ)|0,0>
=
sech^2(t/2).

Fourier inversion gives the exact convolution density

boxed:
dmu_2(x)
=
2x/sinh(pi x) dx.

This is, up to the conventional normalization, the celestial principal-series Plancherel density already used in the project.

Thus the same operation that doubles the arithmetic sheet geometrically has a parallel tensor-square operation on the universal SU(1,1) spectral module.

## 4. Half plus half gives the celestial real weight

At the representation-label level, a scalar celestial primary has

Delta_2=1+i lambda,

with chiral weights

h=bar h=(1+i lambda)/2

for zero spin.

Each chiral real part is therefore 1/2, and

boxed:
Re Delta_2
=
1/2+1/2
=
1.

This is exactly the boundary-dimension rule d/2 under the step d=1 -> d=2.

The statement should be read as a weight-addition/chiral-pairing identity, not as proof that an arbitrary PSL(2,R) representation tensor square is literally a PSL(2,C) celestial representation.

## 5. Matched doubling table

Arithmetic layer:
- geometry: disk / half-plane;
- boundary: RP1;
- group: PSL(2,R);
- Hardy weight: k=1/2;
- principal-series real part: 1/2;
- K1 vacuum spectral density: sech(pi x).

Doubled/celestial layer:
- geometry: CP1 sphere;
- boundary dimension: 2;
- group: PSL(2,C) at the celestial kinematic level;
- scalar principal-series real part: 1;
- spectral density from two arithmetic K1 copies: 2x/sinh(pi x).

This is an unusually coherent match between geometric doubling, conformal weight doubling, and the independently derived tensor-square Plancherel law.

## 6. What remains open

The missing exact arrow is a functor/intertwiner taking the real SU(1,1)/PSL(2,R) arithmetic module and its sheet reflection into the full PSL(2,C) celestial representation, including:
- left/right chirality;
- spin/helicity;
- Lorentz covariance;
- the correct celestial Mellin normalization.

Only after that map is built would it be justified to say that celestial holography is literally the complexified/doubled arithmetic hologram.

The present result is evidence for that construction target, not a proof of 4D Einstein dynamics.
