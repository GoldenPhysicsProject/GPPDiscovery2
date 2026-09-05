# Codex/GPT run: third-moment cold-CI repair and YM sewing boundary

Date: 2026-09-05

## Verify2 centered third moment

Verify2 head `10477d6f9c6c61d4db788ff6b28cc8f47e8de86b` had a split CI result: full Build #2058 passed, while cold changed-Lean #912 failed in `NumberGibbsQuadraticCenteredThirdMoment.lean`.

The failure was source-level name resolution, not a failed moment identity. The theorem used `centeredLogEnergy` unqualified, but the definition lives in namespace `GppNumberGibbsQuadraticCurvatureSquareBridge`. The preceding centered-moment module already opens that namespace, which is why the first and second centered expectation theorems compiled.

Repair commit in GPPVerify2: `34f3403d5b54e1a45146f15f6af746fd143b6ac9`. The only mathematical-source change is opening `GppNumberGibbsQuadraticCurvatureSquareBridge` in the third-moment module. No theorem statement, Gibbs moment formula, summability hypothesis, or curvature algebra was changed. Cold changed-Lean #913 is the certification gate for this repair.

The target remains

\[
\sum_n p_{\beta,\eta}(n)\bigl(L_n-\mu\bigr)^3
=
\frac{M_3}{Z}-3\mu\frac{M_2}{Z}+2\mu^3
=m_3,
\qquad \mu=\frac{M_1}{Z}.
\]

Once this layer is cold-green, repeat the same normalized `tsum` expansion through orders 4, 5, and 6, then identify the actual cubic-residual square expectation with the already-certified `residualSqMoment` polynomial. That closes the remaining semantic route to the quadratic-number-gas curvature bound `R <= 1/2`.

## YM full-conic sewing boundary

The nonzero-`mu` dimensional-reconstruction baseline remains exactly

\[
C^{(D_s)}(\mu)=C^{(V_m)}(\mu)+(D_s-5)C^{(S)}(\mu),
\]

hence

\[
C^{(4)}(\mu)=C^{(V_m)}(\mu)-C^{(S)}(\mu).
\]

The previously certified full-conic residue covariance and normalized spectra are pre-sewing information only. They do not replace the opposite-side tree contraction. The next honest object is therefore the complete massive-vector sewing with all three physical polarizations, minus the actual scalar sewing, evaluated on the full one-complex-dimensional triple-cut conic. Only after that sewn rational function is available should the surviving-coordinate Badger `T1/T2/T3` subtraction/moment projection be applied.

In particular, no generic `3 x scalar` shortcut is admissible away from the threshold slice, and no box/triangle/bubble master coefficient is promoted from residue covariance alone.

## Other active boundaries

- Scalar cut -> dispersion -> raised-box regulator closure remains certified with the regulator moment tending to `1/6`.
- Principal-series/completed-zeta work remains structural only: no unconditional global prime-plus-Archimedean Weil positivity or complete monotonicity theorem was obtained in this run.
- Integer/base Gamma-Wiener-Hopf chamber structure remains intact. Arbitrary real `c > 0` still requires rigorous logistic/logit change-of-variables plus Fourier uniqueness before the continuous convolution semigroup can be promoted to Lean.

No Claude-owned work was inspected.
