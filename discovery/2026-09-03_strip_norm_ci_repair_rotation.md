# Codex rotation: strip norm CI repair and active-front audit

Date: 2026-09-03

Scope: Codex/GPT track only. No Claude research inspected.

## Scalar raised-box

The previous norm-integral theorem head `26c7d61645749c8c801aac50af2bb77a7b71a7b0` produced a split certification result: full Build #1974 passed, while direct changed-Lean smoke #829 failed. The direct smoke result is authoritative for the touched module.

The defect is proof-engineering rather than mathematics. In the on-strip branch of `strip_section_norm_integral_eq_intervalIntegral`, the proof attempted to close

`‖integrand ...‖ = integrand ...`

using a transitivity term built from `Real.norm_eq_abs`; that expression is fragile under the pinned elaborator. The proof has been rewritten to normalize the real norm to absolute value and then use nonnegativity explicitly:

`simpa [Real.norm_eq_abs, abs_of_nonneg hnonneg]`.

The repair is pushed to Verify2 as `59e80343487018df9d085c81de345483f73c12de`. Changed-Lean smoke #830 and full Build #1975 are running on that exact SHA. No certification is claimed until both are terminal green.

If the norm-integral identity certifies, the remaining fixed-`x1` product-integrability target is exact: prove integrability in `x2` of

\[
x_2\mapsto \int_{\mathbb R}\|1_{\mathrm{strip}}(x_2,x_3)Q^{-\epsilon}\|\,dx_3.
\]

The new identity turns this into the ordinary physical inner interval integral. The already-certified one-channel slice majorant has exact integral

\[
\int_0^L (Sx_1x_3)^{-\delta}\,dx_3
=(Sx_1)^{-\delta}\frac{L^{1-\delta}}{1-\delta},
\qquad \delta<1,
\]

so the remaining `x2` domination is the explicit middle majorant already used in the middle DCT. This is the final product-integrability input before Fubini, the nested-simplex representation, the outer DCT, and

\[
J_\epsilon(S,T)\to\frac16.
\]

## Prime-gas thermodynamics

The current quadratic-confinement module already proves a uniform common zeta-weight tail on parameter regions `beta >= -B`, `eta >= eta0 > 0`, and transfers arbitrary fixed logarithmic moments once the corresponding exponent-2 zeta moment is summable. In particular the moments through order four needed by the two-parameter Hessian are already covered. No new tail theorem is required.

The remaining analytic promotion is specifically countable differentiation/interchange for the quadratically confined partition sum. The one-parameter zeta-Gibbs code already demonstrates the desired thermodynamic calculus on `beta > 1` by complex analyticity, including `A'=-U` and `U'=-g`. For the two-parameter quadratically confined family the missing step is to build the real parameterized-series analogue from the uniform moment envelope. Once this lands, the certified Fisher algebra yields the covariance Hessian and strict local thermodynamic response.

## Principal-series / Weil

The finite-interpolation reduction was re-audited. Verify2 formally proves that global transform surjectivity is unnecessary: for a finite zero set `S`, only interpolation on `S union zetaInvolution(S)` is required. The RH reduction still has two genuinely analytic hypotheses: positivity of the actual zeta paired form on the chosen test-transform class and arbitrary finite pair-support interpolation. Neither is supplied by local Gamma/Wiener-Hopf/chamber positivity. No RH claim is promoted.

## Spectral / Mehler-Fock / Wiener-Hopf

No new theorem was promoted this rotation. The strongest current discovery remains the continuous Gamma chamber flow

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2,
\qquad
\widehat{\rho_c}(t)=\operatorname{sech}^{2c}(t/2),
\]

conditional on the Barnes transform identity, with convolution law `rho_c * rho_d = rho_{c+d}` and the previously recorded all-order cumulant/Gaussianization law. The formal blocker remains arbitrary-positive-`c` Fourier-Gamma/Barnes transform plus Fourier uniqueness.

## YM / gravity

No dynamical numerator was promoted. The next honest amplitude calculation remains the complete nonzero-`mu` two-massive-vector color-ordered tree tensor, both physical projectors, and derivation of the FDH cut coefficients including color/coupling/cut normalization. Generalized cuts, higher loops, and gravity double copy remain downstream.
