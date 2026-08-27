# Codex formalization update — Fisher, von Mangoldt positive type, sech endpoints

Date: 2026-08-27
Track: Codex/GPT only

## Verify2 advances

Three sequential changes were pushed to `codex/lean-workbench`.

1. `75ae28a504ef222db00c60efab652a597ace272b` repairs the remaining `t=0` complex-power normalization in `ZetaFisherStrictMonotonicity.lean`. The intended theorem is strict decrease of the arithmetic Fisher response for `1 < beta < gamma`, with strictness witnessed by the `n=2` mode.

2. `cd0dea4f55b20416e88e32821eb6945417c91ef1` adds the finite positive-type layer for the global von-Mangoldt cosine response. For every real frequency `omega`, `t -> cos(omega t)` is positive type by an exact cosine/sine Gram-square decomposition. Since `Lambda(n) exp(-a log n) >= 0`, every individual arithmetic mode

   `Lambda(n) exp(-a log n) cos(log(n) t)`

   is positive type, and every finite truncation is positive type. This does **not** yet assert the infinite `tsum` response is positive type; the honest next step is preservation under the pointwise absolutely-convergent limit, followed by identification with

   `Re(-zeta'/zeta(a+i t))`, `a>1`.

3. `2be40b9dc1718d08fb0282d4138326ea34e10509` promotes the quantitative shifted-sech endpoint audit into Lean algebra. Define

   `R(y) = log(1 + exp(-2|y|))`.

   The file proves the exact stable decomposition

   `log(cosh y) = |y| - log 2 + R(y)`

   together with `0 <= R(y) <= exp(-2|y|)`. Hence for

   `D_lam(x) = log(cosh(pi x)) - log(cosh(pi(lam-x)))`,

   on `x >= max(0,lam)`:

   `|D_lam(x)-pi lam| <= exp(-2|pi x|) + exp(-2|pi(lam-x)|)`,

   and on `x <= min(0,lam)`:

   `|D_lam(x)+pi lam| <= exp(-2|pi x|) + exp(-2|pi(lam-x)|)`.

These bounds are designed to give the two endpoint limits directly and then close

`integral_R dx/[cosh(pi x) cosh(pi(lam-x))] = 2 lam/sinh(pi lam)`

from the already-formalized primitive derivative. The `lam=0` value is the removable limit `2/pi`.

## RH boundary

The new finite positive-type result is part of the same connected RH proof program, but it is not substituted for the existing RH-equivalent finite zero-pairing criterion. The missing global bridge remains the explicit-formula/compressed-operator passage from arithmetic plus archimedean structure to that exact zero-pairing PSD form. No analytic-continuation preservation of positivity is assumed.

## YM/gravity boundary

`MassiveVectorWardReconstruction.lean` already proves that the full massive projector reconstructs the fifth-current contribution and that replacing two massive projectors by bare 4D metrics omits three terms: the two single-longitudinal cross terms and the double-longitudinal term. `MassiveVectorStateSumReconstruction.lean` is only state-count algebra. The next honest amplitude theorem must therefore insert actual sewn currents/numerators into the full Ward-correct projector, not rename the existing scalar projector identity.

## CI status at record time

The previous full Build #881 was green. Fresh Build #887 and Gibbs differential #64 are running against Verify2 head `2be40b9dc1718d08fb0282d4138326ea34e10509`; none of the new theorems is promoted to kernel-green status until those workflows finish.

No Claude material was inspected or used.
