# BPY endpoint and shifted-scattering stress tests
Date: 2026-09-25
Status: diagnostic experiment. No RH claim.

I tested two tempting ways of proving the BPY odd-channel contraction.

## 1. Generic shape conditions do not explain the odd endpoint positivity

The exact odd endpoint kernel is

\[
K_0^-(a,b)=K_0(a,b)-K_0(a,-b),\qquad a,b>0,
\]

with

\[
K_0(a,b)=\frac14\int_0^\infty
(a+b+2t)\Phi(a+t)\Phi(b+t)\,dt.
\]

On sampled half-line grids the Riemann kernel gives a positive matrix down to numerical precision, as expected from the observed critical-line zeros.

I then replaced \(\Phi\) by generic positive rapidly decreasing controls in the *same formula*.

Results:
- Gaussian: essentially degenerate/near-zero spectrum on the tested grid.
- quartic \(e^{-x^4}\): positive in the tested grid.
- pure exponential \(e^{-x}\): negative direction.
- superexponential \(e^{-e^{2x}}\): negative directions.

Therefore positivity is not a generic consequence of positivity, rapid decay, superexponential decay, or log-concavity. Any proof for the Riemann kernel must use its modular/arithmetic structure, not only its shape.

This also explains why trying to prove the endpoint kernel by a generic convexity theorem is unlikely to close.

## 2. Shifted scattering cocycle: direct contractivity survives, naive Loewner evolution does not

For the centered BPY entire function

\[
F(z)=\xi(1/2+z)/\xi(1/2)
\]

define

\[
S_a(z)=\frac{F(z-a)}{F(z+a)}.
\]

On the boundary \(z=it\), evenness/reality gives \(|S_a(it)|=1\). The family also obeys the exact cocycle

\[
\boxed{S_{a+b}(z)=S_a(z-b)S_b(z+a).}
\]

Numerically, on broad samples of the right half-plane and \(0<a<1/2\), \(|S_a(z)|\le1\) to numerical precision. This is the expected de Branges/inner behavior for the actual xi function.

The tempting proof would evolve in \(a\). If \(K=\log F\), then

\[
-\partial_a\log S_a(z)
=
K'(z-a)+K'(z+a).
\]

A Herglotz/Loewner evolution would need the real part of this generator to have one sign in the right half-plane. It does not. The sampled generator becomes strongly negative near high-frequency resonance regions (for example around t roughly 25 in the tested box), despite the sampled transfer itself remaining contractive.

So the simple monotone-inner-flow proof is dead: contractivity cannot be propagated from large a to small a by a pointwise positive infinitesimal generator.

## Consequence

The useful survivor is the cocycle identity, not the naive generator sign. A future proof would have to use a global factorization/energy estimate for the cocycle, not local monotonicity in the displacement parameter.

Reproduction: `experiments/bpy_endpoint_scattering_stress.py`.
