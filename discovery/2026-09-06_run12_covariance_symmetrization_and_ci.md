# Codex/GPT research rotation — covariance symmetrization and CI

Date: 2026-09-06

## Verify2 certification

Exact Verify2 head `fbffe9eda563ce86cd586d323b9a4b08fea62379` is green on both required live gates checked this run:

- Codex changed Lean smoke #943: success.
- Full Build #2089: success.

This certifies the pointwise monotone-radial-observable alignment layer built on the continuous Gamma-chamber likelihood-ratio step.

## New exact discovery: finite covariance symmetrization

Added executable audit `discovery/gamma_chamber_covariance_symmetrization.py`.

For finite weights `w_i`, radial variables `y_i`, observable values `g_i`, and `W = sum_i w_i`, define normalized weighted covariance in the usual way. The exact identity is

`2 W^2 Cov_w(g,y) = sum_{i,j} w_i w_j (g_i-g_j)(y_i-y_j)`.

The script checks the identity with exact `Fraction` arithmetic, including a nonuniform strictly monotone example and a constant-observable zero case.

If all weights are nonnegative and `g` is pairwise monotone in `y`, every summand on the right is nonnegative, hence the weighted covariance is nonnegative. This is the discrete algebraic spine of the iid-copy symmetrization needed for the continuum Gamma-chamber order theorem. The remaining continuum work is genuinely analytic: normalized Gamma measure, integrability of the products, product-measure/Fubini interchange, and passage from the pointwise alignment theorem to the expectation statement.

No continuum theorem is claimed by the executable audit alone.

## Active fronts

### Celestial / YM / gravity

Scalar cut -> dispersion -> raised-box regulator remains closed at `J_epsilon(S,T) -> 1/6`.

The one-loop Yang-Mills blocker remains the factor-preserving opposite crossed full-conic tree with every uncut propagator retained through topology subtraction, before forming the vector-minus-scalar cut and applying Badger extraction. No master coefficient, gravity numerator, or higher-loop analytic coefficient was promoted.

Drive source mining re-located the older Yang-Mills mass-gap manuscripts; these are source material only and do not replace the current explicit-cut construction.

### Positive-real / completed zeta / Weil

Positive-real half-density, `Delta = 2s`, critical-line unitarity, completed-zeta response, local Gamma/Wiener-Hopf structure and finite Weil criteria remain intact. No RH promotion. The missing global theorem remains unconditional positivity of the completed prime-plus-Archimedean explicit-formula/Weil form on an adequate test class.

### Prime gas

Certified thermodynamic/fluctuation package remains intact, including `F' = S/beta^2`, `S' = -beta kappa_2`, `C = beta^2 kappa_2`, strict free-energy concavity, and countable two-parameter curvature `R(beta,eta) < 1/2` for `eta > 0`.

### Spectral / chamber

The new finite symmetrization identity now supplies the exact algebraic bridge between pointwise radial alignment and covariance positivity. Next formal target: a reusable finite weighted covariance theorem in Lean, followed by the genuine measure-theoretic iid/Fubini theorem for the normalized continuous Gamma chamber and then the arbitrary-real convolution semigroup / Gamma-density identification.

## Records

Supabase `codex.*` access was attempted first and was blocked by the connector safety layer; no database update was fabricated. This repository note is the durable run record for this rotation.

No Claude-owned context, branch, record, or file was inspected.
