# Codex/GPT continuation — CI failure correction and strict-Fisher endpoint audit

Date: 2026-08-30
Track: Codex/GPT only

## CI correction

Verify2 branch `codex/lean-workbench` remains at `43fe174d534050dfce0b56e1437394dcc7f422fe`.

The previous status note said the finite-core workflow was still running. That is now obsolete: GitHub Actions run `22381109187` terminated red, with failed job `build (4)` / job id `99272683428`.

The available GitHub connector has exposed the failed run/job state but has not yielded the underlying Lean compiler diagnostic or annotation body in usable form. Therefore no speculative Verify2 repair has been made and `main` has not been advanced. The failed job has been re-run unchanged to distinguish a deterministic Lean failure from a transient runner/cache failure while preserving the exact head.

This is the precise current blocker: terminal red certification exists, but the theorem/module-level compiler diagnostic is not yet available through the connector. Do not infer or weaken any theorem until the diagnostic is recovered.

## Prime-gas Fisher endpoint

Source audit confirms that `PrimeFisherCenteredGeometry.normalized_centered_quadratic_pos` already proves, for beta>1 and every nonzero pair (a,b),

  sum_n p_beta(n) [a(log n-mu1)+b((log n)^2-mu2)]^2 > 0.

`PrimeFisherCountableGeometry.prime_fisher_normalized_det_nonneg` currently packages only nonnegativity of the normalized covariance determinant. `PrimeFisherHankelSchurBridge` proves the exact identity

  det H3 = m0^3 det Cov(X,X^2),

and `PrimeHankelAllOrderStrict` gives strict weighted square positivity for every nonzero polynomial on the full infinite prime-power support.

Thus the most economical strict covariance endpoint remains the centered coefficient identity

  E[(a X_c + b Y_c)^2] = A a^2 + 2 B a b + C b^2,

with A=Var(X), B=Cov(X,X^2), C=Var(X^2), followed by the existing abstract strict-quadratic determinant lemma. The only substantive Lean work in that route is justified `tsum` linearity/distribution; moment summability through degree four is already present.

## Raised scalar-box endpoint

The mathematical regulator limit remains closed:

  J_eps(S,T) = int_{Delta_3} [S x1 x3 + T x2 x4]^(-eps) dx -> 1/6

for S,T>0 and eps->0+.

The certified ingredients already include interior pointwise convergence, a fixed-delta majorant, and the exact singular-simplex integral

  int_{Delta_3} (x1 x3)^(-delta) dx
   = B(1-delta,3-delta) B(1-delta,2)
   = Gamma(1-delta)^2/Gamma(4-2delta),

for 0<delta<1. The remaining work is Lean packaging of the null boundary, AE convergence, and nested/filter dominated convergence for the concrete `simplexMoment`. This is a formalization gap, not a remaining analytic gap.

## Other frontiers retained without inflation

- Spectral/Mehler-Fock/Wiener-Hopf: all-real extended Gamma weight and strict chamber positivity remain exact; exact Mehler-Fock/Macdonald resummation to the scalar-box dilogarithms remains open.
- Principal-series/Weil: positive-real half-density, Delta=2s and local completed-zeta/explicit-formula machinery remain distinct from the unresolved global relative prime-plus-Archimedean trace/Gram positivity theorem. No RH claim.
- YM/gravity: state-sum, Ward, mu^4 dimension-shift and mu^8 radial algebra remain infrastructure. The next honest cut theorem is the explicit fixed-loop-momentum mu!=0 Yang-Mills tree numerator sewn over the three physical massive-vector polarizations, before generalized/higher-loop cuts.
