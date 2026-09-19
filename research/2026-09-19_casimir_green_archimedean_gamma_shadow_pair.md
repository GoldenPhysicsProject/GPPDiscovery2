# Casimir harmonic square root gives the exact Riemann Archimedean shadow pair

Date: 2026-09-19

This continues the exact Casimir-capacity calculation.

## 1. From the discrete harmonic tail to a quadratic radial Green kernel

The unique discrete Casimir-harmonic extension has profile

1/(n+1).

Pass to a continuous quadratic radial coordinate

n=r^2.

The corresponding Green profile is

G_C(r)=1/(1+r^2).

The first-order amplitude associated with this positive square is

a_infty(r)=G_C(r)^(1/2)=1/sqrt(1+r^2).

## 2. Exact Mellin identity

For 0<Re(s)<1,

2 int_0^infinity r^(s-1)/sqrt(1+r^2) dr

is evaluated by t=r^2:

int_0^infinity t^(s/2-1)(1+t)^(-1/2) dt.

This is

B(s/2,(1-s)/2)
=
Gamma(s/2)Gamma((1-s)/2)/Gamma(1/2).

Therefore

boxed(
2 int_0^infinity
r^(s-1)/sqrt(1+r^2) dr
=
pi^(-1/2)
Gamma(s/2)Gamma((1-s)/2)
).

But

pi^(-1/2)
Gamma(s/2)Gamma((1-s)/2)

=
[pi^(-s/2)Gamma(s/2)]
[pi^(-(1-s)/2)Gamma((1-s)/2)].

Thus the Mellin transform of the square root of the quadratic Casimir Green kernel is
EXACTLY the Riemann Archimedean local factor multiplied by its functional shadow.

No zeta zeros and no RH hypothesis enter.

## 3. Critical-line Haar form

Set

s=1/2+it,
r=e^u,
dr=e^u du.

Then

2 r^(s-1) dr/sqrt(1+r^2)
=
2 e^(s u)/sqrt(1+e^(2u)) du

=
sqrt(2) e^(itu) [cosh u]^(-1/2) du.

Hence

boxed(
pi^(-1/2)
|Gamma(1/4+it/2)|^2
=
sqrt(2)
int_R
e^(itu)/sqrt(cosh u) du
).

The real-place shadow-paired Gamma factor is therefore the Fourier transform, on the
multiplicative Haar coordinate u=log r, of the positive even kernel

boxed(
psi_infty(u)=sqrt(2) sech(u)^(1/2)
).

This is an explicit inversion-symmetric Haar half-density:

psi_infty(-u)=psi_infty(u).

Thus the fixed positive polarization at the real place is not abstract.  It has a closed
form.

## 4. Structural chain

The result gives an exact chain:

discrete Casimir conductance d(d+1)
    ->
harmonic Green tail 1/(n+1)
    ->
quadratic radial fold n=r^2
    ->
positive Green square 1/(1+r^2)
    ->
first-order amplitude 1/sqrt(1+r^2)
    ->
Mellin transform
    ->
Archimedean Gamma(s/2) times shadow Gamma((1-s)/2).

This is the cleanest current realization of the project's first-order sign principle at
the real place: the Gamma shadow product appears only after the positive Green object is
resolved into its amplitude and Mellin dual.

## 5. Relation to the endpoint pole pair

The same discrete harmonic tail, when zoomed at a far endpoint N, has scaled Mellin
resolvent 1/s.  Its oriented shadow contributes -1/(1-s)=1/(s-1).  Thus the two elementary
completion poles and the shadow-paired Gamma amplitude emerge from two limits of the same
Casimir Green geometry:

- local endpoint scaling -> 1/s and 1/(s-1);
- global quadratic radial Mellin transform -> Gamma(s/2)Gamma((1-s)/2).

The full Riemann real place consists of both the pole bookkeeping and the Gaussian/theta
normalization.  This note does not yet derive the entire completed xi factor from the
discrete cell model, but it identifies a single Green kernel underlying both structures.

## 6. Immediate arithmetic target

At each finite prime p the project already has a positive shadow/Cayley kernel and a local
Julia colligation.

At the real place we now have the explicit inversion-even Haar amplitude psi_infty above.

The next constructive question is whether the prime local colligations and this real-place
half-density can be assembled through the exact Möbius/divisibility boundary differential
so that the GLOBAL incoming defect cancels before the positive square is taken.

That would give a zero-independent prime-Archimedean first-order network whose local
metrics are all fixed by Haar/shadow geometry.


## 7. Exact Tate convolution identity

The older Shadow Euler manuscript contains the standard Tate real-place local zeta integral

Z_infty(s)
=
int_0^infinity exp(-pi r^2) r^s dr/r
=
(1/2) pi^(-s/2) Gamma(s/2).

The zero-product claims elsewhere in that manuscript must be handled with care because some
displayed gamma-only forms are RH-conditional.  The Tate integral itself is unconditional.

Define the multiplicative shadow of a function by

(S f)(r)=r^(-1) f(r^(-1)).

Then, for the Mellin convention

M[f](s)=int_0^infinity f(r) r^s dr/r,

one has exactly

M[Sf](s)=M[f](1-s).

Let

f_infty(r)=exp(-pi r^2).

Its multiplicative Haar convolution with its shadow is

(f_infty *_x S f_infty)(r)
=
int_0^infinity
f_infty(x)
S f_infty(r/x)
dx/x.

Directly,

S f_infty(r/x)
=
(x/r) exp(-pi x^2/r^2),

hence

(f_infty *_x S f_infty)(r)
=
(1/r)
int_0^infinity
exp[-pi x^2(1+r^-2)] dx
=
1/[2 sqrt(1+r^2)].

Therefore

boxed(
2/sqrt(1+r^2)
=
4 (f_infty *_x S f_infty)(r)
).

Taking Mellin transforms gives

M[2/sqrt(1+r^2)](s)
=
4 Z_infty(s) Z_infty(1-s)

=
pi^(-1/2) Gamma(s/2)Gamma((1-s)/2),

exactly the shadow-paired Riemann Archimedean factor derived above.

Thus the Casimir amplitude is not merely analogous to the Tate local factor.  It is the
multiplicative Haar convolution of the self-dual Tate Gaussian with its functional shadow.

## 8. Log-Haar autocorrelation form

Set

g_infty(u)
=
e^(u/2) exp(-pi e^(2u)),
qquad r=e^u.

Then

Z_infty(1/2+it)
=
int_R g_infty(u)e^(itu) du.

Its ordinary autocorrelation is explicitly

C_infty(a)
=
int_R g_infty(v)g_infty(v+a) dv

=
1/[2 sqrt(2 cosh a)].

Therefore

boxed(
4 C_infty(a)
=
sqrt(2) sech(a)^(1/2)
=
psi_infty(a)
).

So the positive inversion-even Haar kernel discovered from Casimir capacity is exactly four
times the autocorrelation of the Tate Gaussian half-density.

By Wiener--Khinchin,

Fourier[psi_infty](t)
=
4 |Z_infty(1/2+it)|^2
=
pi^(-1/2)|Gamma(1/4+it/2)|^2.

This identifies three previously separate real-place constructions:

1. Tate's self-dual Gaussian;
2. the Casimir harmonic Green amplitude;
3. the positive shadow-paired Gamma spectral weight.

They are one convolution/autocorrelation structure.

## 9. Significance for the global program

At the real place the required fixed positive polarization is now generated from an
explicit primitive amplitude rather than postulated:

primitive half-density:
  g_infty(u)=e^(u/2)e^(-pi e^(2u));

shadow pairing:
  g_infty with its reflected/orientation-dual copy;

positive boundary kernel:
  psi_infty(u)=sqrt(2)sech(u)^(1/2);

spectral multiplier:
  pi^(-1/2)|Gamma(1/4+it/2)|^2.

This is exactly the architecture sought in the first-order sign program:
retain the two oriented amplitudes separately, pair them by shadow, and only then obtain
the positive square.

The next finite-place comparison should ask whether each local prime Poisson kernel is
likewise the autocorrelation / Julia defect of a primitive one-sided Haar amplitude.
If yes, all places will share one local template and the remaining RH content will be
only the global causal sewing.
