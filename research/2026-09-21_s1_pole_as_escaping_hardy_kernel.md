# The surviving s=1 pole is an escaping Hardy reproducing kernel

Date: 2026-09-21

This follows the one-ghost reduction

Delta_q B
=
positive Gamma tail
+
positive prime-power channel
-
G_{q-1},

where for r>0

G_r(a,b)
=
int_0^infinity e^{-r x}(1-e^{-a x})(1-e^{-b x}) dx.

Put r=q-1.

## 1. Exact normalized pole state

Define

v_r(x)=sqrt(r) exp(-r x/2),   x>=0.

Then

||v_r||_2^2
=
r int_0^infinity e^{-r x} dx
=
1.

If X is multiplication by x, then

boxed(
r G_r(a,b)
=
<(I-e^{-aX})v_r,(I-e^{-bX})v_r>.
)

Thus the single remaining negative Krein channel is the orbit of one normalized state
under the causal semigroup differences I-e^{-aX}.

## 2. It is exactly a normalized Hardy/Laplace reproducing kernel

On L2(R_+) use the Laplace transform

(Lf)(z)=int_0^infinity f(x)e^{-zx} dx,  Re z>0.

Evaluation at alpha>0 is represented by e^{-alpha x}, whose norm is (2alpha)^(-1/2).
The normalized evaluation vector is therefore

k_alpha(x)=sqrt(2alpha)e^{-alpha x}.

Taking alpha=r/2 gives

boxed(v_r=k_{r/2}).

So the surviving s=1 pole channel is literally a normalized Hardy reproducing kernel
whose evaluation point approaches the Hardy boundary as q downarrow 1.

## 3. Exact boundary escape

For every fixed f in L2(R_+),

<v_r,f> -> 0

as r downarrow 0.

Proof:
first check compactly supported f by Cauchy-Schwarz,

|<v_r,f>| <= sqrt(r) sqrt(R) ||f||_2

on support [0,R], then use density and ||v_r||=1.

Hence

boxed(v_r weakly -> 0,  ||v_r||=1).

The state disappears under weak tests while retaining all of its norm.

Its probability density is

|v_r(x)|^2=r e^{-rx},

an exponential law of mean 1/r. Thus the norm escapes to x~1/r -> infinity.

This is an exact model of the no-escaped-trace / boundary-ghost problem.

## 4. The whole pole feature family collapses onto one escaping ray

For every fixed a>0,

||(I-e^{-aX})v_r-v_r||^2
=
||e^{-aX}v_r||^2
=
r/(r+2a)
->0.

Therefore each nontrivial boundary feature becomes asymptotically the SAME escaped state.

Equivalently,

r G_r(a,b)
=
1
-r/(r+a)
-r/(r+b)
+r/(r+a+b)

and hence

boxed(lim_{r downarrow0} r G_r(a,b)=1)

for all fixed a,b>0.

So the normalized s=1 ghost is asymptotically rank one.

## 5. Co-Poisson pole cancellation versus Hilbert no-escape

The unnormalized pole vector is

u_r(x)=e^{-r x/2}=v_r/sqrt(r).

For integrable f,

<u_r,f>
=
int e^{-r x/2} f(x) dx
->
int f(x) dx.

Thus the co-Poisson constraint

int_0^infinity f(x) dx=0

kills exactly the DISTRIBUTIONAL boundary value of the s=1 pole vector.

But

||u_r||_2=r^(-1/2) -> infinity,

while the normalized v_r keeps norm 1 and escapes weakly.

Therefore:

- co-Poisson removes the trivial pole algebraically on its test space;
- ordinary Hilbert convergence can still lose a unit-norm normalized pole state at infinity;
- these are not contradictory statements.

The missing RH no-escape theorem is precisely a topology statement strong enough to retain
this boundary norm while preserving causal/Hardy structure.

## 6. Ordinary L2 forgets the zero-integral boundary condition

The subspace

{f in C_c^infinity(R_+): int f=0}

is dense in L2(R_+).

Indeed choose phi in C_c^infinity(R_+) with int phi=1 and set

phi_R(x)=R^(-1) phi(x/R).

Then

int phi_R=1,
||phi_R||_2=R^(-1/2)||phi||_2.

For compactly supported f,

f_R=f-(int f)phi_R

has zero integral and ||f_R-f||_2->0.

Hence the co-Poisson s=1 condition is NOT a closed Hilbert condition in ordinary L2.

This rigorously explains why a self-adjoint L2 boundary formulation can be blind to the
pole constraint / Hardy inner defect.

## 7. Causal Hardy space makes interior evaluation continuous

On the causal half-line, for alpha>0,

|Lf(alpha)|
<=
||f||_2 ||e^{-alpha x}||_2
=
||f||_2/sqrt(2alpha).

Thus for every interior alpha the evaluation kernel is a genuine Hilbert vector.
The norm diverges only as alpha downarrow0.

This is exactly the correct geometry:
safe-line pole evaluation is controlled inside the causal Hardy half-plane, and failure at
the critical boundary occurs through normalized reproducing-kernel escape.

## 8. Relation to off-critical Hardy defects

The previously identified bad-zero/model-space defect also appears through Hardy
reproducing kernels at poles of the shifted quotient. As a zero crosses toward the boundary,
its normalized kernel can concentrate while converging weakly to zero.

The trivial s=1 pole therefore supplies an explicit solvable prototype of the same boundary
escape mechanism that an off-critical zero would create.

The one-ghost Gamma reduction plus co-Poisson cancellation should be used as the model case
for the required no-escape topology theorem.

Immediate target:
construct the completed prime-Archimedean graph norm in which the family v_r does NOT lose
its boundary norm, and test whether the full Fourier/order-four co-Poisson lift is isometric
for that graph norm before Hardy compression.