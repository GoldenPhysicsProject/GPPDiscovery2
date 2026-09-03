# Codex/GPT active-front rotation — 2026-09-03

Research separation honored: Codex/GPT state only. No Claude research inspected.

## Scalar box

The spectral ODE repair at Verify2 `e83d1addc636e25bf93f3ad8da2b522a330c8147` is fully green (changed-Lean #850, Build #1996).

New candidate theorem pushed to Verify2 as `e7bdce51ec90d60ecfba8dccc45e387ec65d5c00` in `RaisedBoxOuterNormBound.lean`:

`nestedInnerIntegral_norm_le_outerMajorant`

For `0<delta<1`, `0<=epsilon<=delta`, `S,T>0`, `0<x1<1`,

|| integral_{0}^{1-x1} dx2 integral_{0}^{1-x1-x2} dx3 Q^{-epsilon} ||
<= 1 + (S*x1)^(-delta)/(1-delta).

The proof integrates the already-certified middle constant bound over x2 and uses `1-x1 <= 1`. This is exactly the missing domination inequality for the final outer DCT. CI is currently running on the candidate head; do not call it certified until green.

The remaining scalar assembly is now: outer AEStronglyMeasurable transfer from the full-simplex fiber representation, a.e. pointwise convergence from `middle_interval_tendsto_inner_one` away from the null endpoints, apply interval DCT with `middleConstant_outer_intervalIntegrable`, then rewrite the limiting nested integral to `simplexVolume = 1/6`.

## Prime-gas thermodynamics

The termwise first/second beta/eta derivative identities and the global all-index quadratic-confinement envelope are already green. The unresolved theorem is now purely interchange: differentiate the countable `tsum` under the parameter derivative. No new tail estimate is needed. After interchange, the Hessian of log Z is the covariance matrix of `(L,L^2)` and the already-proved strict Fisher determinant gives strict convexity/local invertibility.

## Principal series / completed zeta / Weil

No RH promotion. The exact local structure remains Delta=2s and principal-line unitarity. The abstract finite-support interpolation reduction remains useful, but the real global obstruction is unchanged: positivity of the actual completed prime-plus-Archimedean Weil quadratic form on one concrete admissible transform class, plus finite interpolation for that same class. Gamma/chamber/Wiener-Hopf positivity does not discharge Weil positivity.

## Spectral / Mehler-Fock / Wiener-Hopf / chambers

The elementary kinematic weight-shift ODE is now green after normalization repair. The continuous Gamma-chamber semigroup, cumulant hierarchy, and Levy density remain discovery-level because arbitrary-c Barnes/Fourier-Gamma transformation and Fourier uniqueness are still not formalized. No status inflation.

## Yang-Mills / gravity

No amplitude numerator promoted. The next honest dynamical gate remains the full Ds=4, mu!=0 color-ordered two-massive-vector tree current, both physical projectors, and derivation of the FDH sewing coefficients with coupling/color/orientation/normalization intact. Generalized cuts, higher loops, and gravity double copy remain downstream.
