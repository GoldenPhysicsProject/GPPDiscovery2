# Codex rotation: strip norm integral and active-front status

Date: 2026-09-03

Scope: Codex/GPT track only. No Claude research inspected.

## Scalar raised-box advance

Verify2 head `fc0f8a5c04c9260878946c45e769c44af48da522` is fully certified: changed-Lean smoke #828 and full Build #1973 both passed.

That certifies:

- interval integrability of the concrete raised-box `x3` slice on every physical affine interval under `0 <= epsilon <= delta < 1`;
- integrability of the zero extension of that slice over the measurable inner simplex strip.

The next theorem has now been pushed to Verify2 as `26c7d61645749c8c801aac50af2bb77a7b71a7b0`:

\[
\int_{\mathbb R}\|1_{\mathrm{strip}}(x_2,x_3)Q^{-\epsilon}\|\,dx_3
=
\int_0^{1-x_1-x_2}Q^{-\epsilon}\,dx_3.
\]

The point is not cosmetic. `MeasureTheory.integrable_prod_iff` requires integrability in `x2` of the integral of the norm, not merely a bound on the norm of the inner integral. Nonnegativity of the physical raised-box integrand supplies the bridge between these quantities.

Current CI for this theorem is smoke #829 / Build #1974; certification is pending.

If it certifies, the second product-integrability conjunct can be obtained by dominating this norm integral with the already-certified explicit slice majorant and integrating that majorant over the physical `x2` interval. Then the chain is:

1. two-dimensional section `Integrable`;
2. Fubini bridge from the grouped full-simplex fiber to the nested interval integral;
3. outer dominated convergence;
4. unconditional regulator limit

\[
J_\epsilon(S,T)\to\frac16.
\]

## Prime-gas frontier

No new tail theorem is required for the Hessian. The quadratic-confinement infrastructure already transfers all moments needed through order four. The remaining issue is countable differentiation/interchange for the parameterized partition sum. The first and second derivatives require only `L`, `L^2`, `L^3`, `L^4` weighted sums, already covered by the existing moment framework.

Target differential identity remains

\[
\nabla^2\log Z=
\begin{pmatrix}
\operatorname{Var}(L)&\operatorname{Cov}(L,L^2)\\
\operatorname{Cov}(L,L^2)&\operatorname{Var}(L^2)
\end{pmatrix}.
\]

Combined with the certified strict Fisher determinant this gives strict convexity and local invertibility of the thermodynamic moment map.

## Principal-series / Weil frontier

The local dictionary remains exact:

\[
\Delta=2s,
\qquad
\Re\Delta=1\Longleftrightarrow\Re s=\frac12,
\qquad
\Delta\mapsto2-\Delta\Longleftrightarrow s\mapsto1-s.
\]

The global RH-critical target remains unchanged: identify the actual completed prime-plus-Archimedean explicit-formula quadratic form with an unconditional positive Gram/Hilbert form on a concrete admissible transform class, while retaining arbitrary finite interpolation on zero pair-supports. Local Gamma/Wiener-Hopf/chamber positivity is not enough.

## Spectral / chamber context

The continuous Gamma chamber family

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2
\]

has discovery-level transform law

\[
\widehat{\rho_c}(t)=\operatorname{sech}^{2c}(t/2),
\]

hence a continuous convolution semigroup `rho_c * rho_d = rho_{c+d}`. The all-order cumulant law recorded earlier is consistent with the known infinitely-divisible generalized hyperbolic-secant/Meixner family. Pitman-Yor's work on infinitely divisible laws associated with hyperbolic functions provides external context for this semigroup structure, but does not replace the Barnes-transform proof required for Lean promotion.

## YM / gravity boundary

No numerator has been promoted without derivation. The missing dynamical theorem remains the complete nonzero-`mu` two-massive-vector color-ordered tree tensor, with both physical projectors and fixed color/coupling/cut normalization, followed by derivation of the FDH cut coefficients. Higher-loop generalized cuts and gravity double copy stay downstream.
