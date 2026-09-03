# Gamma-chamber convolution flow: explicit Levy generator

Date: 2026-09-03
Status: exact conditional consequence of the Barnes/Fourier transform identity; not yet Lean-certified

## Input already isolated on the Codex/GPT track

For c > 0 define

rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2.

The discovery-level Barnes transform is

  rhohat_c(t) = sech(t/2)^(2c).

At c=1 this is the normalized base chamber

  rho_1(x) = rho_0^chamber(x) = 2 x / sinh(pi x),
  rhohat_1(t) = sech(t/2)^2.

Hence the continuous parameter is additive under convolution:

  rho_c * rho_d = rho_(c+d).

## New exact consequence: Levy-Khintchine exponent

Write

  rhohat_c(t) = exp(-Psi_c(t)),

so

  Psi_c(t) = 2 c log cosh(t/2).

Define the symmetric measure on R\{0}

  nu_c(dx) = c / (|x| sinh(pi |x|)) dx.

Then

  Psi_c(t) = integral_R (1-cos(t x)) nu_c(dx).

Derivation: if

  F_c(t) = integral_R (1-cos(t x)) c/(|x| sinh(pi |x|)) dx,

then F_c(0)=F_c'(0)=0 and

  F_c''(t)
    = c integral_R x/sinh(pi x) cos(t x) dx
    = (c/2) rhohat_1(t)
    = (c/2) sech(t/2)^2.

On the other hand

  d^2/dt^2 [2 c log cosh(t/2)] = (c/2) sech(t/2)^2,

with the same value and first derivative at t=0. Therefore the two functions agree.

The Levy integrability conditions are also compatible with the density: near zero,

  1/(|x| sinh(pi |x|)) ~ 1/(pi x^2),

so (1 wedge x^2) nu_c is locally integrable; at infinity the density decays exponentially.

## Structural bridge

Because rho_1(x)=2x/sinh(pi x), the Levy density can be written

  nu_c(dx) = (c/2) rho_1(x)/x^2 dx

away from x=0.

Thus the same certified base Gamma/Wiener-Hopff weight that generates the discrete chamber hierarchy also controls the infinitesimal Levy generator of the continuous convolution flow. This is stronger than merely saying that chamber index is convolution order: the infinitesimal semigroup structure is explicitly encoded by the base spectral density.

## Formal status / next target

No unconditional theorem is promoted until the arbitrary-c Barnes transform is proved in Lean. Once that transform is formalized, the next exact targets are:

1. prove the integral representation for 2 log cosh(t/2) from the c=1 Fourier transform;
2. package nu_c as a Levy measure;
3. prove rho_(c+d) = rho_c * rho_d by Fourier uniqueness;
4. recover variance and all even cumulants from the Levy measure and compare with the Bernoulli-number cumulant formula already recorded.

This result does not imply Weil positivity or RH. It is a spectral/Wiener-Hopff structural theorem candidate only.
