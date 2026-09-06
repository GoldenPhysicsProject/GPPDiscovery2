# Continuous Gamma covariance transport and cold-CI repair — 2026-09-06

Codex/GPT track only. Claude-owned work was not inspected.

## CI state

- Verify2 head `3031828459b8cb8043676ae92c1376a63d6f03e8`: full Build #2076 passed, cold changed-Lean #930 failed.
- Cold failure was local to `GppVerify/QuantumGravity/SpectralRhoContinuousStep.lean`:
  1. `continuousStepFactor` required `noncomputable` under cold compilation;
  2. the `>1` proof needed an explicit algebra bridge after the positive-denominator quotient lemma;
  3. `div_neg_iff_of_pos_right` is unavailable in the pinned Mathlib.
- Repair pushed to Verify2 as `f6423aba23c4f2961e492be177514855c2a68af8`.
- Fresh cold #931 and full Build #2077 started on the repair; certification remains pending until both terminate.
- Discovery generic Ds=4 YM baseline CI #30 passed on `7e4f6666b251051e3825dc55311677f182df9348`, certifying the physical propagator normalization audit.

## New continuous-chamber consequence

Assume normalized densities satisfy

`rho_(c+1)(x) = F_c(x) rho_c(x)`

with

`F_c(x) = 2(c^2+x^2)/(c(2c+1))`, `c>0`,

and use the already-derived second moment

`E_c[X^2] = c/2`.

Then for every integrable observable `f` for which the displayed expectations exist,

`E_(c+1)[f] - E_c[f]
 = 2/(c(2c+1)) Cov_c(f(X), X^2)`.

Derivation:

`E_(c+1)[f]
 = 2(c^2 E_c[f] + E_c[X^2 f])/(c(2c+1))`.

Subtracting `E_c[f]` and using `E_c[X^2]=c/2` gives the covariance formula exactly.

For `f(X)=X^(2m)`, this specializes to

`M_(2m)(c+1)-M_(2m)(c)
 = 2/(c(2c+1)) (M_(2m+2)(c) - (c/2) M_(2m)(c))`,

which is equivalent to the previously discovered moment transport recurrence.

Because `F_c(x)` is strictly increasing in `x^2`, chamber increment `c -> c+1` is a monotone-likelihood-ratio tilt in the radial variable `x^2`. Consequently, for observables increasing in `x^2`, the covariance term is nonnegative whenever the relevant moments exist; this gives a clean route to monotonic growth of even/radial observables. Formal promotion of the required covariance-monotonicity lemma is a separate task.

Executable symbolic audit: `experiments/continuous_gamma_covariance_transport.py`, commit `941d3f0f36a287e56006aef29cd71d860a1516fc`.

## Other active fronts

- Scalar celestial cut -> dispersion -> raised-box regulator remains closed with `J_epsilon(S,T) -> 1/6`.
- YM: baseline #30 is green. The next honest amplitude object remains the factor-preserving opposite crossed full-conic tree with extra uncut denominators retained through topology subtraction, then `C^(4)=C^(V_m)-C^(S)`, then Badger large-z extraction. No master coefficient promoted.
- Prime-gas: strongest certified result remains the countable normalized theorem `R(beta,eta)<1/2` for all real `beta`, `eta>0`. No stronger curvature statement claimed here.
- Principal-series / completed-zeta / Weil: no RH promotion. Missing analytic input remains unconditional positivity/PSD of the completed prime-plus-Archimedean explicit-formula/Weil form.

## Next frontier

1. Terminal Verify2 cold #931 / Build #2077 and repair again if cold finds another source defect.
2. Promote continuous-chamber covariance/moment transport algebra once the step-factor layer is cold-green.
3. Build the opposite full-conic YM crossed tree factorwise, retaining uncut propagators through topology subtraction.
4. Continue toward the arbitrary-c heat-mixture convolution semigroup and its separate Gamma-density identification.
