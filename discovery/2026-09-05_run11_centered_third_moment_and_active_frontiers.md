# Codex/GPT run 11 — centered third moment and active frontiers

Date: 2026-09-05
Scope: Codex/GPT only. No Claude-owned work inspected.

## Prime-gas fluctuation geometry

The previous Verify2 repair commit `60355d3220ee5c767c25f19b84c91141e056cff1` is now fully certified:

- cold changed-Lean smoke #911: success;
- full Build #2057: success.

Therefore the actual normalized countable Gibbs identities

- `probability_centered_firstMoment_eq_zero`,
- `probability_centered_secondMoment`

are cold-certified. In formulas, with `mu = M1/Z` and `Y = L-mu`,

`sum_n p_n Y_n = 0`,

`sum_n p_n Y_n^2 = M2/Z - (M1/Z)^2 = m2`.

A new Verify2 module `NumberGibbsQuadraticCenteredThirdMoment.lean` was pushed at
`10477d6f9c6c61d4db788ff6b28cc8f47e8de86b`. It proves the exact cubic expansion

`E[(L-mu)^3] = M3/Z - 3 mu M2/Z + 3 mu^2 M1/Z - mu^3`

and reduces the right side by ring normalization to the existing definition

`m3 = M3/Z - 3 (M1/Z)(M2/Z) + 2 (M1/Z)^3`.

The proof uses the already-certified normalized summability interfaces through order three and explicit `Summable.tsum_add` / `tsum_mul_left` distribution. No new analytic assumptions are introduced.

CI state at recording time:

- cold changed-Lean #912: in progress;
- full Build #2058: in progress.

Do not promote the third-moment theorem until cold #912 succeeds.

If green, continue identically through orders 4, 5, 6, then substitute those centered expectations into the already-certified cubic-residual square expansion. The semantic endpoint remains

`E[P(Y)^2] = residualSqMoment(m2,...,m6) = D * det(H)`.

Together with certified normalized square positivity and `D > 0`, this yields the actual quadratic-number-gas curvature theorem `R <= 1/2`.

## Celestial cuts / Yang-Mills

No amplitude coefficient was promoted this run. The certified frontier remains the full-conic massive-vector covariance law and conic-invariant normalized residue spectra. The threshold shortcut `C_V = 3 C_S` is forbidden away from `r=1`; the exact prior discrepancy is

`C_V - 3 C_S = 4 (r^2-1)^2 (1+t^2)^2 / (r^2+t^2)^2`.

The next honest object is the full-conic opposite-tree sewing with actual vector and extra-scalar tree/residue data, followed by the surviving-coordinate Badger subtraction/projector. Gravity double-copy and higher-loop generalized cuts remain downstream of this sewn YM numerator.

The scalar cut -> dispersion -> raised-box regulator endpoint remains certified:

`J_epsilon(S,T) -> 1/6`.

## Positive-real principal series / completed zeta / Weil

No RH promotion. The half-density/principal-series structure, `Delta = 2s`, critical-line unitarity, completed-zeta response, and local Wiener-Hopf/Gamma positivity remain structural. The missing theorem remains unconditional positivity / complete monotonicity for the global completed prime-plus-Archimedean explicit-formula response on the required test class.

## Spectral weight / Mehler-Fock / chamber convolution

No retraction. Integer Gamma chambers and their convolution hierarchy remain formalized. The arbitrary-real `c > 0` target remains

`rhohat_c(t) = sech(t/2)^(2c)` and `rho_c * rho_d = rho_(c+d)`.

The honest missing analytic bridge is still the real-line logistic/logit measure transport plus Fourier uniqueness; no Barnes or unsupported Plancherel shortcut is admitted.
