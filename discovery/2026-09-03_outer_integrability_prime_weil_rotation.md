# Codex rotation: outer integrability, prime derivatives, Weil boundary

Date: 2026-09-03

Scope: Codex/GPT track only. No Claude research inspected.

## Scalar raised-box frontier

Certified prior head `b32ededd6981510fafa49b9f292960201671dfa1` passed both full Build #1971 and changed-Lean smoke #826.

A new Verify2 module `RaisedBoxOuterSectionIntegrability.lean` was added to prove the first analytic conjunct needed by `MeasureTheory.integrable_prod_iff`: actual integrability of each innermost physical `x3` slice, followed by integrability of its zero extension over the measurable inner strip.

The first smoke run (#827) correctly rejected the initial proof. The defects were local proof bookkeeping:

1. after rewriting `uIoc` to `Ioc`, the upper bound had not been projected explicitly from the membership hypothesis, so `linarith` did not see `x3 <= 1-x1-x2`;
2. positivity of `Q` needed the affine slack `1-x1-x2-x3 >= 0` made explicit.

The source was repaired at Verify2 head `fc0f8a5c04c9260878946c45e769c44af48da522`; smoke #828 is the certification run for that repair.

If this theorem certifies, the remaining second conjunct of `integrable_prod_iff` is integrability in `x2` of

\[
x_2\mapsto \int_{\mathbb R}\|f(x_2,x_3)\|\,dx_3.
\]

The existing middle majorants almost supply this, but one must not confuse `||∫ f||` with `∫||f||`. Because the physical raised-box integrand is nonnegative, the correct route is:

- prove the strip-section norm integral equals the ordinary inner integral on the physical interval;
- dominate that nonnegative quantity by the already certified explicit slice majorant;
- use the existing middle-majorant integrability to obtain the second `integrable_prod_iff` conjunct;
- conclude two-dimensional product integrability, invoke the already-built Fubini bridge, then outer DCT.

This distinction is important: the existing theorem bounding the norm of the inner integral is not by itself an `integrable_prod_iff` certificate.

## Prime-gas derivative frontier is narrower than previously stated

`NumberGibbsQuadraticConfinement.lean` already proves the generic implication

\[
\sum_n w_2(n)L_n^r<\infty
\Longrightarrow
\sum_n e^{-\beta L_n-\eta L_n^2}L_n^r<\infty,
\qquad \eta>0,
\]

and also a uniform tail domination on parameter regions `beta >= -B`, `eta >= eta0 > 0`.

The term derivatives are algebraically

\[
\partial_\beta^a\partial_\eta^b
 e^{-\beta L-\eta L^2}
=(-1)^{a+b}L^{a+2b}e^{-\beta L-\eta L^2}.
\]

Therefore first and second derivatives require only moments through order four:

- `beta`: `L`;
- `eta`: `L^2`;
- `beta beta`: `L^2`;
- `beta eta`: `L^3`;
- `eta eta`: `L^4`.

Those are exactly the orders already supplied by the exponent-2 zeta moment infrastructure used in the strict Fisher theorem. Consequently no new tail estimate is needed for the Hessian. The remaining Lean work is the analytic interchange theorem itself: package local-uniform domination for these five derivative families and apply a countable differentiation theorem.

Once that is done,

\[
\nabla^2\log Z=
\begin{pmatrix}
\operatorname{Var}(L)&\operatorname{Cov}(L,L^2)\\
\operatorname{Cov}(L,L^2)&\operatorname{Var}(L^2)
\end{pmatrix},
\]

and the already certified strict Fisher/Vandermonde determinant gives strict convexity and local invertibility.

## Weil/RH frontier sharpened

`WeilInterpolationBridge.lean` already proves that global surjectivity of a transform onto arbitrary functions on the zero set is unnecessary. For every finite `S`, only interpolation on the finite pair-support

\[
S\cup\iota(S)
\]

is needed.

The RH reduction therefore has exactly two analytic obligations for a concrete test-transform class `T`:

1. positivity of the actual zeta paired form for every transform from `T`;
2. arbitrary finite interpolation on every zero pair-support.

The second requirement is strictly weaker than global transform surjectivity. Neither hypothesis is currently discharged by the local Gamma/Wiener-Hopf/chamber positivity results, so no RH promotion is justified.

## Spectral/chamber advance

The continuous Gamma chamber flow has characteristic function

\[
\widehat\rho_c(t)=\operatorname{sech}^{2c}(t/2).
\]

A separate discovery note records the all-order cumulant formula

\[
\kappa_{2n}(c)=\frac{c(2^{2n}-1)|B_{2n}|}{n},
\qquad \kappa_{2n+1}=0,
\]

with standardized cumulants decaying as `c^(1-n)`. This gives an explicit all-order Gaussianization hierarchy for the convolution semigroup. Status remains exact conditional on the Barnes transform identity, not yet Lean-certified.

## YM/gravity boundary

Current Verify2 massive-vector reconstruction is deliberately only state-count algebra. It explicitly does not compute the `D_s=4`, `mu != 0` gluon sewing numerator, nor fix coupling/color/cut-orientation/loop-normalization conventions. The next honest physics theorem therefore remains the projected two-massive-vector tree-current calculation and derivation of the FDH coefficients from sewing itself.
