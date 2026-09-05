# Codex/GPT run 11 — cold Gibbs repair and principal-series smoothing frontier

## Scope
Codex/GPT track only. No Claude-owned branches, notes, records, or artifacts were inspected.

## Prime-gas curvature: cold-CI correction

The normalized quadratic Gibbs moment layer at Verify2 commit `5b3ec20ef4f019208f0418715a3bced890b1a8f4` had a split certification state: full Build #2053 passed, but cold changed-Lean #907 failed deterministically in `NumberGibbsQuadraticNormalizedMoments.lean` at the private first raw-moment summability helper with the default 200000-heartbeat limit. The downstream unknown-private-constant error was secondary to that timeout.

The repair at Verify2 `073c3660aa1f965e47393cbf1b0dce2609e53e01` removes the expensive private helper layer and mirrors the already-cold-proven construction in `NumberGibbsQuadraticConfinement`: first build the exponent-2 zeta moment with an explicit type, then invoke `summable_numberGibbs_moment_of_quadratic`, then divide by `Z`. No heartbeat ceiling was raised. Cold #908 and full Build #2054 were started on the repaired head.

The mathematical endpoint remains unchanged: after normalized moments through order six are cold-certified, the remaining curvature bridge is the centered `tsum` identity equating the actual normalized cubic-residual square expectation with `residualSqMoment`; positivity and the algebraic identity `residualSqMoment = D * det H` then imply `R <= 1/2` because `D > 0`.

## Arithmetic/principal-series source cross-link

The focused arithmetic principal-series paper gives the exact trace-class regularizer

`P(x) = pi*x/sinh(pi*x)`

with normalized Fourier multiplier

`P_hat(xi)/P_hat(0) = sech(xi/2)^2`.

It defines the smoothed zero-independent arithmetic heat response

`K_P(t) = (2/pi) <W, P * g_t>`

and states the exact equivalence `RH iff K_P is completely monotone`; under RH the endpoint trace is

`K_P(t) = sum_{gamma>0} m_gamma sech(gamma/2)^2 exp(-gamma^2 t)`.

This connects directly to the already-formalized base Gamma/Wiener-Hopf chamber, since Verify2 has the real-axis identity `P = (pi/2) rho_1` and the multiplier `sech^2`. This is a useful formalization target because it supplies a trace-class/arithmetic smoothing interface without changing the global logical boundary: complete monotonicity of the explicit prime-plus-Archimedean response remains the missing theorem. Local chamber positivity does not imply RH.

## Spectral/chamber frontier

The integer/base chamber layer remains formally stronger than the arbitrary-real-parameter layer. The honest next analytic closure is still the real-line logistic/logit change of variables proving the arbitrary `c > 0` Fourier-Gamma identity, followed by Fourier uniqueness to obtain `rho_c * rho_d = rho_{c+d}`. No Barnes/Plancherel shortcut is promoted.

## YM/generalized-cut frontier

Discovery2 CI #27 is already green for full-conic massive-vector covariance. The next amplitude object is the opposite-tree contraction/full `D_s=4` vector-minus-extra-scalar state sum on the genuine one-complex-dimensional triple cut, followed by the surviving-coordinate large-parameter Badger projection. No master coefficient is inferred from the pre-sewing residue spectrum alone.
