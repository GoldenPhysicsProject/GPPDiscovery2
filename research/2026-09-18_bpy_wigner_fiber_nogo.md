# BPY fiberwise positivity is impossible: the local defect is the Wigner function of q

Date: 2026-09-18

This sharpens the exact 1+1 Dirac reformulation of the BPY two-copy colligation.

## 1. One real spectral mode

For fixed u and real z,

f_+(t,u,v)
=
exp[i z(1-2t)u/2] cos(zv/2),

f_-(t,u,v)
=
-i exp[i z(1-2t)u/2] sin(zv/2).

The phase in t has unit modulus, so after integrating t in [0,1] the fixed-u difference is

N_+(u,z)-N_-(u,z)
=
int_R r_u(v)
[cos^2(zv/2)-sin^2(zv/2)] dv

=
int_R
q((u+v)/2) q((u-v)/2)
cos(zv) dv.

## 2. This is exactly a Wigner distribution

Put x=u/2.  Then

q((u+v)/2) q((u-v)/2)
=
q(x+v/2) q(x-v/2).

For real q, the continuous Wigner distribution is, up to Fourier-sign convention,

W_q(x,k)
=
int_R q(x+v/2) q(x-v/2) exp(-ikv) dv.

Because the integrand is even in v after taking the real part,

boxed[
N_+(u,z)-N_-(u,z)=W_q(u/2,z)
]

with the corresponding convention.

Thus the pointwise-in-u BPY even-minus-odd norm is literally the phase-space Wigner
function of the Riemann/BPY wavefunction q.

## 3. Hudson no-go

Hudson's theorem (R. L. Hudson, Reports on Mathematical Physics 6 (1974), 249-252)
states that a pure continuous-variable L2 state has an everywhere nonnegative Wigner
function iff its wavefunction is Gaussian, i.e. an exponential of a quadratic polynomial.

The BPY function

q(x)=Phi(x)/Xi(0)

is not Gaussian: the exact Riemann kernel Phi contains exp(-pi n^2 exp(2|x|))-type
super-exponential structure and is not the exponential of a quadratic polynomial.

Therefore its Wigner function must take negative values.

Consequently there exist real u,z for which

N_+(u,z)-N_-(u,z)<0,

or equivalently

||f_-||_u > ||f_+||_u.

## 4. Consequence for the RH contraction attack

The desired BPY inequality

||P_- f||_{mu_omega}
<=
||P_+ f||_{mu_omega}

cannot be established fiberwise in the center coordinate u.

Any proof based on:
- fixed-u supersymmetric positivity,
- fixed-center log-concavity,
- fixed-center positive definiteness,
- or a pointwise-in-u Dirac flux sign

is impossible.

The global u integration is essential.

The BPY measure weights the fibers by

u sinh(omega u)

times the two-copy q-product.  RH positivity, if proved through this route, must therefore
come from a genuinely nonlocal compensation among centers u, not from positivity of each
relative-coordinate fiber.

This explains why the earlier HCM / fixed-center Kontorovich-Lebedev attempt failed:
fixed-center positivity is too strong and in fact false for any non-Gaussian pure state.

## 5. Refined first-order target

The 1+1 Dirac equations remain useful, but the energy identity must be integrated in the
center variable before a sign is taken.

The next viable object is therefore a TWO-DIMENSIONAL weighted Dirac current on the full
(c,d,u) BPY domain, or after integrating c, a nonlocal u-coupled current.

The sought inequality must exploit the special u-weight

u sinh(omega u)

and the exact relation of q to the Riemann kernel, rather than attempt to dominate sine by
cosine at every fixed center.
