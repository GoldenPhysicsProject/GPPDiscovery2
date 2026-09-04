# Codex/GPT rotation — Massieu positive metric and active frontiers

Date: 2026-09-04

Scope: Codex/GPT research track only. No Claude-owned research inspected.

## Prime-gas fluctuation geometry

Verify2 commit `e50faa6de9e981ff18f65f5e8ee0bb37973869fb` is now cold- and full-build-green (#895 / #2041). This certifies the strict covariance nondegeneracy inequality

`fisherBE^2 < fisherBB * fisherEE`

and nonvanishing Massieu/Fisher determinant on the quadratically confined domain `eta > 0`.

New Verify2 commit `13e66832df3c7e33ee610a14c002212aa83fdcad` adds `NumberGibbsQuadraticMassieuPositiveDefinite.lean`. The new source proves:

- `fisherBB > 0` directly from the abstract countable strict weighted-variance theorem, using the positive support points n=0,1 and the already-certified quadratic-confinement summability;
- `fisherEE > 0` from `fisherBB > 0` plus the strict covariance determinant inequality;
- the Sylvester package `fisherBB > 0 ∧ massieuFisherDet > 0 ∧ fisherEE > 0`.

At this record write, Build #2042 is in progress on the new commit. The new module is therefore pending CI rather than certified.

If CI is green, the next exact theorem should package positivity of the full quadratic form. Algebraically, for A=fisherBB, B=fisherBE, C=fisherEE and D=A*C-B^2,

`A * (A*a^2 + 2*B*a*b + C*b^2) = (A*a + B*b)^2 + D*b^2`.

With A>0 and D>0 this yields strict positivity for every nonzero tangent vector `(a,b)`.

## Celestial scalar box / generalized cuts

The raised scalar-box regulator endpoint remains closed and certified: `J_epsilon(S,T) -> 1/6` on the stated physical domain.

For the honest nonzero-mu Yang-Mills continuation, Discovery2 already contains the generic Ds=4 state sum, Ward audit, exact x-pole decomposition, propagator ancestry audit, and the existing Badger s23 triangle/bubble subtraction machinery. The remaining hard interface is not normalization: it is a proved generalized-cut/master-integral projector that transports the raw x-pole sewing into box/triangle/bubble master coefficients. Pole order alone must not be relabeled as topology. No physical FDH numerator, D-dimensional gravity double copy, or higher-loop claim is promoted until this projector is derived.

## Principal series / Weil

The positive-real half-density, Delta=2s, critical-line unitarity, shadow conjugation, completed-zeta response, and local Gamma/Wiener-Hopf results remain structural. No RH promotion. The global blocker remains unconditional positivity of the genuine completed prime-plus-Archimedean Weil quadratic form on an adequate admissible class, with the explicit-formula and closure/interpolation machinery needed to connect it to the finite spectral criteria.

## Spectral / Mehler-Fock / chamber convolution

The exact arbitrary-c target remains

`rho_c(x) = 2^(2c-1)/(pi*Gamma(2c)) * |Gamma(c+i*x)|^2`,

`Fourier(rho_c)(t) = sech(t/2)^(2c)`,

and hence `rho_c * rho_d = rho_(c+d)`.

The Beta/Gamma bridge is already formalized; the remaining formal bottleneck is the real-line logistic change of variables and Fourier uniqueness. No Barnes axiom or unproved SL(2,C) Plancherel identification is justified. The Mehler-Fock Legendre-Q layer remains downstream of missing special-function infrastructure.
