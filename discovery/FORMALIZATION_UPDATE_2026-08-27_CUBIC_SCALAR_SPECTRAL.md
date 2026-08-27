# Codex formalization update — 2026-08-27

Codex/GPT track only. No Claude material inspected.

## Kernel/CI baseline

- `GPPVerify2` `codex/lean-workbench` full Build #853 is green at `ec8e3f722b384d22be234a43da4aa1fd6317a72e`.
- This certifies the current scalar-box physical convergence layer, completed-zeta principal-series response layer, and the repaired von-Mangoldt cosine bridge in the aggregate build.
- The dedicated Gibbs differential gate #30 failed before the entropy theorem because `VonMangoldtCubicPositivity.lean` was still an intentionally non-aggregate candidate module.

## Cubic von-Mangoldt response

The target arithmetic density is

\[
 c_3(\beta,n)=\Lambda(n)(\log n)^2 e^{-\beta\log n},\qquad \beta>1.
\]

The candidate module proves termwise nonnegativity, the strict `n=2` witness, summability from the twice-`logMul` von-Mangoldt L-series, and hence

\[
\sum_n c_3(\beta,n)>0.
\]

CI #30 exposed two Lean-only defects: unresolved `Complex.log` real/imaginary projections in the twice-logarithm term and a syntactic mismatch in `Complex.reCLM.map_tsum`. Both were repaired without changing any theorem statement at Verify2 commit

`10fa6b6060a15cd420b74ff031a4052e507ff595`.

Dedicated Gibbs #32 and full Build #855 are running on that head. Do not promote strict cubic positivity until the dedicated module passes.

## Scalar box and amplitude boundary

The full-build-green scalar layer now includes the moving physical regulator composition into the one-sided `m -> 0+` convergence machinery. The valid domination remains the structured mixed-log majorant; the earlier independent-square surrogate remains retracted.

The next amplitude theorem is not another scalar estimate. The existing `MassiveVectorWardReconstruction` shows that replacing the massive-vector projector by a bare four-dimensional metric contraction drops the fifth-current term, and at rank two drops two single-longitudinal cross terms plus the double-longitudinal term. Therefore the next honest Yang–Mills/gravity step must insert explicit sewn tree currents/numerators with the full Ward reconstruction before dimension-shift/rational extraction.

## Principal-series/completed-zeta response

On the celestial principal line `Re Delta = 1`, the completed-zeta response

\[
\mathcal R(\Delta)=\frac{\Lambda'(\Delta/2)}{\Lambda(\Delta/2)}
\]

is already formalized with

\[
\operatorname{Re}\mathcal R(\Delta)=0
\]

where the logarithmic derivative is defined, and globally with the shadow-odd relation

\[
\mathcal R(\Delta)=-\mathcal R(2-\Delta).
\]

This is a representation/functional-equation statement only, not a zero-location theorem.

## Spectral/chamber convolution

`SechConvolutionKernel.lean` already proves for `lambda != 0`

\[
\frac1{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=
\frac{\tanh(\pi x)+\tanh(\pi(\lambda-x))}{\sinh(\pi\lambda)}.
\]

The remaining theorem is the whole-line improper integral

\[
\int_{\mathbb R}\frac{dx}{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=
\frac{2\lambda}{\sinh(\pi\lambda)},
\]

with the removable `lambda=0` limit treated separately. The proven `SechSquaredIntegral` module gives the preferred Mathlib pattern: explicit antiderivative plus endpoint limits, avoiding series interchange.

## Next frontier

1. Read CI #32/#855; repair the first exact cubic/entropy compiler signal.
2. Once cubic positivity clears, drive the genuine entropy derivative and Legendre differential modules through the dedicated gate.
3. Promote the sech-convolution primitive/endpoints to a whole-line theorem.
4. Begin the explicit YM cut numerator layer using full massive Ward projectors, not scalar/state-count surrogates.
5. Keep the completed-zeta/shadow/Weil route separate from any RH zero-location claim until a genuine global positivity-equivalence theorem is established.
