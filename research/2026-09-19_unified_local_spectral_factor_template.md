# Unified local spectral-factor template at every place

Date: 2026-09-19

The finite-place Poisson kernel and the real-place Gamma shadow kernel have the same exact
first-order architecture.

## 1. Finite prime

Let

a_p=p^(-1/2),

and define the one-sided geometric amplitude on n>=0 by

g_p(n)=sqrt(1-a_p^2) a_p^n.

Then

sum_{n>=0}|g_p(n)|^2=1.

Its Hardy/Fourier transform is

G_p(z)
=
sqrt(1-a_p^2)/(1-a_p z),

|z|=1.

Therefore

boxed(
|G_p(e^(i theta))|^2
=
(1-a_p^2)/|1-a_p e^(i theta)|^2
=
K_{p,1}(theta)
).

Equivalently,

K_{p,1}(theta)
=
sum_{k in Z} a_p^|k| e^(ik theta).

Thus the finite-place shadow/Poisson kernel is the power spectrum of a primitive causal
half-density.

In local zeta notation, for theta=-t log p,

G_p
=
sqrt(1-p^-1) zeta_p(1/2+it),

up to the harmless Fourier-sign convention.

This is exactly the transfer of the one-state stable system / scalar Julia colligation.

## 2. Real place

The Tate primitive half-density on the log-Haar line is

g_infty(u)=e^(u/2)e^(-pi e^(2u)).

Its Fourier transform is

G_infty(t)
=
Z_infty(1/2+it)
=
(1/2)pi^(-1/4-it/2)Gamma(1/4+it/2).

The positive shadow-paired spectrum is

boxed(
K_infty(t)
=
4|G_infty(t)|^2
=
pi^(-1/2)|Gamma(1/4+it/2)|^2
).

Its autocorrelation kernel is

psi_infty(a)
=
sqrt(2) sech(a)^(1/2).

Thus the real place is the continuous log-Haar analogue of the finite geometric filter.

## 3. Uniform local template

At every place v there is now a primitive oriented amplitude g_v and a local spectral
factor G_v such that

boxed(
K_v=|G_v|^2
).

Finite p:
- primitive carrier: valuation semigroup n>=0;
- amplitude: geometric p^-n/2;
- transfer: local Euler resolvent;
- positive square: local Poisson/shadow kernel.

Real infinity:
- primitive carrier: logarithmic scale u in R with the Tate Gaussian half-density;
- transfer: Archimedean local zeta integral;
- positive square: Gamma/shadow autocorrelation kernel.

The fixed local metrics are supplied by Haar measure before any zero set is considered.

## 4. First-order lesson

The local positive kernel should never be regarded as the fundamental datum.  The proof-
bearing object is its spectral factor / oriented amplitude.

At a finite prime the distinction is visible as

1-a_p S

versus

(1-a_p S^*)(1-a_p S).

At infinity it is visible as

g_infty

versus the autocorrelation g_infty * g_infty^shadow.

Squaring first discards orientation/phase.

## 5. Global obstruction

A naive product of local positive spectra on the critical line is not the answer.  The
finite-prime product requires renormalization and, more importantly, boundary modulus is
blind to a global Hardy inner factor.

Therefore the remaining arithmetic theorem is not local positivity.  Local positivity is
now explicit at every place.

The remaining theorem is GLOBAL CAUSAL SEWING:

assemble the primitive local spectral factors, together with the exact Mobius/divisibility
inverse and the Archimedean factor, into a causal global transfer without generating an
incoming defect space.

In Hardy language the desired global transfer is the completed Theta_omega and the
statement is H_omega=0.

This reduces the local-to-global architecture to one question:
why does adelic/Tate-Poisson sewing preserve the incoming orientation of the primitive
local amplitudes?
