# Codex/GPT rotation checkpoint — middle measurability, YM boundary, spectral correction

Date: 2026-09-02
Track: Codex/GPT only

## Scalar-box regulator

Verify2 Build #1944 is green on `4df3036d242399705a75b216d0b4f47f2e39afa7`, certifying the strip-integral to variable-endpoint interval-integral bridge.

New Verify2 head `6ee6e68e5ea85b1b995684c7366cde37fed92155` adds `GppRaisedBoxMiddleMeasurability.intervalInnerIntegral_aestronglyMeasurable`. The theorem transfers the jointly measurable product-strip certificate to the original variable-endpoint innermost integral on the restricted middle simplex interval. Build #1945 is running at record time, so this theorem is not yet marked certified.

If #1945 is green, the middle DCT no longer lacks a measurability hypothesis. The next proof obligation is the middle pointwise convergence/dominating-function composition, followed by the already-prepared outer envelope and outer DCT to close `J_epsilon(S,T) -> 1/6`.

## Honest YM/gravity status correction

The earlier shorthand that the YM lane still needed to begin tree sewing was too weak. Codex discovery already contains an honest four-dimensional MHV two-particle cut:

- `C_s^YM = -i A_4^tree * s*t/(D_1 D_2)` in the recorded stripped convention.
- The KLT-derived four-graviton cut is `C_s^GR = i M_4^tree * s^3*t*u/(D_1 D_2 D_3 D_4)`.

These are four-dimensional cut results and deliberately do not contain the `mu^2` rational information.

For the nonzero-`mu` lane, the corrected massive-vector projector work establishes that the physical double projector equals the explicit nine-state polarization sum. It also retracts the invalid shortcut of double-contracting an unprojected rank-two tree tensor with bare five-dimensional metrics. The remaining numerator target is therefore precise: construct/project the full two-massive-leg color-ordered tree tensor, sew with both physical massive projectors, subtract the scalar channel to obtain `C^(4)=C^(V_m)-C^(S)`, and only then export to gravity/generalized cuts.

## Spectral / Mehler-Fock correction

A prior blanket phrase rejecting "repeated-sech convolution" was too broad and is corrected here.

The exact normalized Mehler-Fock/Wiener-Hopf density

`rho(x)=2x/sinh(pi x)`

has the discovery-level all-order convolution family

`rho_m(x) = 2^(2m-1)/(pi Gamma(2m)) |Gamma(m+ix)|^2`,

`Fourier[rho_m](k)=sech^(2m)(k/2)`,

hence exactly `rho_m = rho^{*m}` for integer `m>=1` under the stated Fourier convention.

What is *not* justified is identifying the separate Gamma chamber hierarchy, a full A2 chamber integral, or amplitude sewing directly with these convolution powers. The pointwise-positive product weight `q(lambda)=pi lambda^2/cosh(pi lambda)` also has a Fourier transform that changes sign, so pointwise positivity cannot be promoted to positive type.

## Principal-series / Weil

No RH promotion. The finite interpolation reduction and polynomial multiplier route remain useful, but the genuine missing global theorem is still the completed prime-plus-Archimedean explicit-formula positivity on an admissible test class. Local Gamma/WH positivity is not that theorem.

## Prime-gas thermodynamics

The exact two-parameter Fisher geometry remains based on sufficient statistics `(log n,(log n)^2)`, with determinant equal to the weighted Vandermonde sum. Strict positivity is already available from explicit positive three-point support. The next nonredundant analytic/formal target is countable differentiation of the quadratically confined partition sum so that `Hess log Z = Cov(log n,(log n)^2)` is a theorem on every real beta with eta>0; curvature work should remain downstream of that identification.

## Separation / hygiene

No Claude branch, note, record, or separate research was inspected or used in this rotation.
