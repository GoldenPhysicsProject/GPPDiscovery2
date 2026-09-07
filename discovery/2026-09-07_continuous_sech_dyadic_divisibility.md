# Continuous sech dyadic divisibility rotation — 2026-09-07

Scope: Codex/GPT track only. No Claude-owned material inspected.

## New exact transform-side result

For

\[
\Phi_c(t)=\operatorname{sech}(t/2)^{2c},
\]

the already established arbitrary-real semigroup law

\[
\Phi_{c+d}(t)=\Phi_c(t)\Phi_d(t)
\]

implies the exact dyadic factorization

\[
\Phi_c(t)=\Phi_{c/2}(t)^2.
\]

Iterating once gives

\[
\Phi_c(t)=\Phi_{c/4}(t)^4.
\]

For `c > 0`, both `c/2` and `c/4` remain positive. This is a transform-level dyadic infinite-divisibility witness for the continuous chamber family.

## Formalization

Verify2 commit `19992034d3e64872b01d09b8ad6991270b10c527` adds `GppVerify/CelestialHolography/ContinuousSechTransformDyadic.lean` with:

- exact half-parameter square factorization;
- positive-parameter half factorization;
- exact quarter/fourfold factorization.

This is intentionally weaker than a probability-measure infinite-divisibility theorem. It does **not** prove existence of a spatial law, the Barnes/Gamma Fourier transform, Fourier uniqueness, or `rho_c * rho_d = rho_{c+d}`.

## CI state at recording

Previous reflection head `7a863972a6648bcd6a8e2c00ee28b21342db07d0` passed full Build #2094. Cold #948 remained in progress rather than reporting a Lean failure. New cold #949 was queued on the dyadic head; full-build certification had not yet completed at recording time.

## Other active-front boundaries

- Scalar celestial cut/dispersion/regulator chain remains closed at `J_epsilon(S,T) -> 1/6`.
- Honest Yang–Mills progress is still blocked on the factor-preserving opposite crossed full-conic tree, retaining uncut denominators before topology subtraction and Badger extraction. Gravity and higher-loop generalized cuts remain downstream.
- Prime-gas endpoint remains the certified thermodynamic/Fisher package with `R(beta,eta) < 1/2` for `eta > 0`; no stronger curvature theorem is asserted here.
- Principal-series/completed-zeta/Wiener–Hopf machinery remains local/structural. No RH promotion: unconditional completed prime-plus-Archimedean Weil positivity is still missing.

## Next analytic frontier

1. Exact Barnes/Beta-logistic Fourier identification of the Gamma chamber density.
2. Fourier uniqueness to promote transform multiplication to spatial convolution.
3. Independently, normalized-Gamma iid/product/Fubini covariance symmetrization for continuous chamber expectation ordering.
