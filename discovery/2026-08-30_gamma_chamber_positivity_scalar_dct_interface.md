# Codex continuation: Gamma-chamber positivity and scalar DCT interface

Date: 2026-08-30

## Exact spectral consequence promoted to Verify2

The existing chamber hierarchy already gives

\[
\operatorname{Re}\rho_k(x)
=\left(\prod_{j=0}^{k-1} r_j(x)\right)
\frac{2}{\pi}P_{\rm WH}^{\rm ext}(x),
\]

where every recurrence factor `r_j(x)` is strictly positive and the continuously
extended Wiener--Hopf weight satisfies `P_WH^ext(x)>0` for every real `x`, including
`x=0` where the removable singularity is assigned its analytic value `1`.

Therefore

\[
\boxed{\operatorname{Re}\rho_k(x)>0\quad\text{for every }k\in\mathbb N,
\ x\in\mathbb R.}
\]

This is an exact consequence of the already-formalized Gamma recurrence and the
all-real Wiener--Hopf extension.  It does not assert a Plancherel interpretation,
Mehler--Fock inversion theorem, or a Weil/RH positivity theorem.  The theorem has
been promoted to `WienerHopfGammaChamberHierarchy.lean` as `rhoGamma_re_pos`.

## Raised-box DCT: exact Mathlib interface

The scalar-box blocker is now an interface problem, not a missing majorant.  Mathlib
provides the filter-parametric interval theorem

`intervalIntegral.tendsto_integral_filter_of_dominated_convergence`.

Its hypotheses match the regulator problem directly: eventual AE strong
measurability, an eventual AE bound by an interval-integrable function, and AE
pointwise convergence.  The positive-regulator filter can be taken as

\[
\mathcal N(0)\cap\{0\le\varepsilon\le\delta\}
\]

(or an equivalent `nhdsWithin` formulation) with fixed `0<delta<1`.

For the concrete raised-box integrand,

\[
Q=Sx_1x_3+Tx_2x_4,
\qquad
Q^{-\varepsilon}\le 1+(Sx_1x_3)^{-\delta},
\]

and after the spectator coordinate is integrated out the singular majorant is
exactly the existing nested Beta object

\[
\int_0^1 x^{-\delta}\int_0^{1-x}
 y^{-\delta}(1-x-y)\,dy\,dx
 =B(1-\delta,3-\delta)B(1-\delta,2)
 =\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)}.
\]

Thus the next Lean work should not create another special-function layer.  It should
build the three nested DCT steps (or one simplex-measure DCT), converting the existing
complex Beta integrability certificate to the real nonnegative majorant interface as
needed.  The endpoint faces are null sets and should be handled AE rather than by
forcing strict positivity there.

## Prime-Fisher determinant audit correction

`TwoParameterFisherDeterminant.lean` contains the exact finite three- and four-point
Vandermonde determinant identities, but it explicitly leaves the infinite Gibbs layer
separate.  `PrimeFisherCenteredGeometry.lean` proves strict positivity of every
nonzero centered two-observable score on the full countable probability ensemble.
`StrictQuadraticDeterminant.lean` gives the exact algebraic implication from a strict
binary quadratic form to positive determinant.

The only missing packaging theorem is therefore the analytic expansion identifying
the centered-score `tsum` with

\[
A a^2+2Bab+Cb^2,
\]

where `A,B,C` are the normalized covariance entries.  Once that `tsum` identity is
proved using moment summability through order four, the strict determinant follows
immediately.  No countable Cauchy--Binet theorem is required for this route.

## Honest boundaries preserved

- Scalar box: not closed until the original concrete nested moment satisfies
  `J_epsilon(S,T) -> 1/6` under positive regulator removal.
- Yang--Mills/gravity: state-count and rational defect algebra are not yet an explicit
  nonzero-mu tree-amplitude sewing derivation.
- Weil/RH: chamber positivity is local/spectral Gamma algebra and does not imply the
  global signed explicit-formula positivity criterion.
- Mehler--Fock: positivity of the Gamma chamber hierarchy does not supply the missing
  Mehler--Fock-to-dilog reconstruction.
