# Scalar horizontal flux criterion extracted from BPY reflection

Date: 2026-09-20

The full two-copy BPY positivity criterion can be reduced to a strictly smaller scalar target.

Let

F(z)=xi(1/2+z)/xi(1/2).

The centered BPY density q is even and satisfies

F(z)=int_R e^{z x} q(x) dx.

## 1. Diagonal BPY kernel is the horizontal modulus derivative

The two-copy BPY reflection kernel is

L_omega(z,w)
=
[E_omega(z) conjugate(E_omega(w))
 -E_omega#(z) conjugate(E_omega#(w))]
/[-i(z-conjugate(w))].

On the real diagonal z=w=t, take the continuous diagonal limit. Equivalently use the
BPY integral directly. Since A-B=-(x-y), the interpolation variable t_BPY disappears and

L_omega(t,t)
=
iint (x+y)sinh(omega(x+y))
 e^{-it(x-y)} q(x)q(y) dx dy.

On the other hand

|F(omega+it)|^2
=
iint e^{omega(x+y)} e^{it(x-y)} q(x)q(y) dxdy.

Using the symmetry (x,y)->(-x,-y), the derivative can be symmetrized:

d/domega |F(omega+it)|^2
=
iint (x+y)sinh(omega(x+y))
 e^{it(x-y)} q(x)q(y) dxdy.

Changing t->-t if necessary gives the same real quantity, hence

boxed(
L_omega(t,t)
=
d/domega |F(omega+it)|^2
).

Thus the diagonal of the de Branges/BPY kernel is the horizontal probability/energy flux.

## 2. Scalar criterion already implies RH

Claim:

boxed(
RH
iff
d/domega |xi(1/2+omega+it)|^2 >=0
for all omega>0 and t in R.
)

Proof of reverse direction:
Assume horizontal monotonicity and suppose rho=1/2+delta+i gamma is a zero with delta>0.
Put

g(omega)=|xi(1/2+omega+i gamma)|^2.

Then g>=0, g is nondecreasing on (0,infinity), and g(delta)=0. Therefore
g(omega)=0 for every 0<omega<=delta. Hence the entire function
s -> xi(s+i gamma) vanishes on a real interval, so xi is identically zero, contradiction.
Functional reflection then excludes zeros with Re<1/2.

Under RH, the standard Hadamard/de Branges factorization gives the same monotonicity.

Therefore one does NOT need to prove the full matrix inequality L_omega(z,w)>=0 directly;
its real diagonal already suffices because of the special analytic divisor structure of xi.

## 3. Logarithmic derivative form

Away from zeros,

d/domega log |F(omega+it)|^2
=
2 Re [xi'/xi(1/2+omega+it)].

Hence another equivalent target is

boxed(
Re xi'/xi(s) >=0
for Re(s)>1/2.
)

This inequality itself excludes zeros in the open half-plane.

## 4. Autocorrelation Loewner form

Define the tilted autocorrelation

R_omega(v)
=
int_R e^{omega(2x-v)}
q(x)q(x-v) dx.

Then

|F(omega+it)|^2
=
int_R e^{itv} R_omega(v) dv.

For every omega, R_omega is positive definite because it is the autocorrelation of
x -> e^{omega x}q(x).

The RH condition is that its omega derivative also be positive definite:

boxed(
partial_omega R_omega is positive definite for every omega>0.
)

Equivalently, the positive-definite autocorrelation family is monotone in the Bochner cone.

This is a useful sharpening: positivity of R_omega itself is automatic; the unresolved
content is positivity of its first horizontal derivative.

## 5. Relation to the reversible Markov operator

For the BPY reversible Markov operator K_omega, full reflection positivity is K_omega>=0.
The scalar criterion tests that reflection form only on Fourier characters f(a)=e^{ita}.

For a generic self-adjoint operator, positivity on this restricted nonlinear family would
not imply positivity. Here it nevertheless implies RH because any off-line zero forces a
failure on one character at the corresponding ordinate.

So the scalar flux route is a genuinely smaller proof target than constructing the full
square root K_omega=L^*L.

## 6. Eisenstein factorization and exact obstruction

v34 gives

W_Xi(a,x)=1/4 P_x E*(i e^{2a},1/2+ix),

P_x=B_x^*B_x>=0.

The horizontal Born identity becomes

|Xi(x+iy)|^2-|Xi(x)|^2
=
1/4 int (cosh(yr)-1) P_x E*(i e^r,1/2+ix) dr,

and Jensen's criterion is

1/4 int y r sinh(yr) P_x E*(i e^r,1/2+ix) dr >=0.

Naively moving P_x onto the weight fails: the formal-adjoint coefficient is

C_{x,y}(a)
=
(x^2+y^2+1/4) cosh(2ya)
-y sinh(2ya)
-(x^2+1/4),

which changes sign; e.g.

C_{0,1/2}(a)=1/2 e^{-a}-1/4<0 for a>log 2.

Thus the positive differential factorization cannot close the scalar flux in the geodesic
variable alone.

The missing square must use the automorphic quotient, the BPY orientation channel, or an
equivalent nonlocal polarization.

## 7. Current proof target

The shortest remaining constructive target is now:

prove
partial_omega R_omega is positive definite

directly from the four-Gaussian/BPY representation or from the completed automorphic
quotient, without using the zeros of xi.

This is weaker than constructing the full BPY Markov square root, but still sufficient for RH.