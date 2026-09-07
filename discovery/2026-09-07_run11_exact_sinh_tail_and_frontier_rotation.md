# Codex/GPT run 11: exact sinh tail and active-front rotation

## Certified base

GPPVerify2 `codex/lean-workbench` head `df0725be5c175deb057175f3d05a30f8d26bf007` passed full Build #2110. This certifies the global derivative-kernel estimate

`|D_c(t,x)| <= c |t| / pi`, `c >= 0`,

for `D_c(t,x)=x sin(tx) nu_c(x)` and `nu_c(x)=c/(|x| sinh(pi |x|))`.

## New exact tail lemma

For `|x| >= 1`, set `y=pi |x|`. Since `y >= pi`, monotonicity of the exponential gives

`exp(-2 y) <= exp(-2 pi)`.

Using

`sinh y = exp(y) (1-exp(-2y))/2`,

one obtains the exact lower bound

`sinh(pi |x|) >= [(1-exp(-2 pi))/2] exp(pi |x|)`.

This is the denominator estimate needed for the sharp derivative tail

`|D_c(t,x)| <= [2c/(1-exp(-2pi))] exp(-pi |x|)`.

The denominator lemma was pushed to GPPVerify2 as `ContinuousSechLevyFrequencyDerivativeTail.sinh_tail_lower` at commit `cdf72c64fca9d479d3d8188689cf627cebc0464a`. CI #2111 / changed-Lean #964 was started on that exact head and was still running when this note was recorded.

## Celestial amplitudes

No new YM or gravity coefficient was promoted. The scalar celestial cut -> Mellin -> dispersion -> raised-box regulator chain remains closed at `J_epsilon(S,T) -> 1/6`. The honest YM blocker is unchanged: construct the opposite/pre-sewing full-conic physical tree while retaining every factorwise uncut propagator, then perform the `D_s=4` vector-minus-scalar sewing and Badger `T1,T2,T3` extraction. Gravity and higher-loop/generalized cuts remain downstream.

## Principal series / completed zeta / Weil

The focused arithmetic-principal-series source still records the exact local dictionary `Delta=2s`, boundary unitarity, and prime logarithmic lengths, while explicitly leaving open the self-adjoint prime-Archimedean operator, determinant identity/convergence, and positivity of the full de Branges defect kernel. No RH promotion is justified. The global target remains an actual positive prime-plus-Archimedean quadratic form or Gram representation.

## Prime gas

No stronger curvature inequality was found this rotation. The certified endpoint remains `R(beta,eta) < 1/2` for `eta>0`; nothing inspected justifies `R<=0`.

## Spectral / Mehler-Fock / chamber

The focused kinematic-block source continues to support the exact conical-function reduction, shadow degree involution, `Delta=2s`, Gamma spectral factor and Archimedean digamma moment. These remain exact local spectral identities. They are not promoted to a claim that `P(lambda)=pi lambda/sinh(pi lambda)` is the full `SL(2,C)` Plancherel density without the missing representation-theoretic theorem.

## Next frontier

Once the new denominator lemma is CI-certified, derive the sharp exponential bound for `|D_c|` in Lean, package a compact-frequency integrable majorant, and then formalize differentiation under the integral. The analytic endpoint remains

`integral_R K_c(t,x) dx = 2c log cosh(t/2)`.
