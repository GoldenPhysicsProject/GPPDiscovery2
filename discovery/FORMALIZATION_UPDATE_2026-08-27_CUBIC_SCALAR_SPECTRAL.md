# Codex formalization update — 2026-08-27

Codex/GPT track only. No separate Claude work is used in this update.

## Kernel/CI baseline

- `GPPVerify2` `codex/lean-workbench` full Build #857 is green at `f7ef8dbb7e450dae1cb4da8be80dfc33b1526c57`.
- Dedicated Gibbs differential #34 failed on one Lean-only no-op simplification in `VonMangoldtCubicPositivity.lean`; the arithmetic, summability, cosine bridge, Fisher, and strict-thermodynamic dependencies had already built.
- That exact no-op `simp` was removed at Verify2 commit `c853079cdd5e09e83fc69c3f4e0ef5611404bb0b` with no theorem statement or hypothesis change.
- Build #859 and dedicated Gibbs #36 are running on the repaired cubic head.
- A separate spectral advance was then pushed at Verify2 commit `86402cbb5cd9aec86fca0a0234288da6e6d54671`, and the build workflow now gates that module explicitly at `c75c0a5800b2dad2f65363e95abd3a3efe1072d9`.

## Cubic von-Mangoldt response

The target arithmetic density is

\[
 c_3(\beta,n)=\Lambda(n)(\log n)^2 e^{-\beta\log n},\qquad \beta>1.
\]

The candidate module proves termwise nonnegativity, the strict `n=2` witness, summability from the twice-`logMul` von-Mangoldt L-series, and hence

\[
\sum_n c_3(\beta,n)>0.
\]

CI #30 exposed unresolved complex-log projections and a `map_tsum` shape mismatch. CI #32 then exposed rewrite ordering around nested `logMul`. CI #34 narrowed the remaining reported defect to a redundant simplifier after the natural-cast logarithm had already been rewritten. All three were Lean proof-engineering defects; no mathematical statement was weakened. Strict cubic positivity is still not promoted until the current dedicated gate passes.

## Scalar box and amplitude boundary

The full-build-green scalar layer includes the moving physical regulator composition into the one-sided `m -> 0+` convergence machinery. The valid domination remains the structured mixed-log majorant; the earlier independent-square surrogate remains retracted.

The next amplitude theorem is not another scalar estimate. The existing `MassiveVectorWardReconstruction` shows that replacing the massive-vector projector by a bare four-dimensional metric contraction loses longitudinal/fifth-current contributions. Therefore the next honest Yang–Mills/gravity step must insert explicit sewn tree currents/numerators with the full Ward reconstruction before dimension-shift/rational extraction.

## Principal-series/completed-zeta response

On the celestial principal line `Re Delta = 1`, the completed-zeta response

\[
\mathcal R(\Delta)=\frac{\Lambda'(\Delta/2)}{\Lambda(\Delta/2)}
\]

is formalized with

\[
\operatorname{Re}\mathcal R(\Delta)=0
\]

where defined, and globally with

\[
\mathcal R(\Delta)=-\mathcal R(2-\Delta).
\]

This remains a representation/functional-equation statement only, not a zero-location theorem.

## Spectral/chamber convolution

`SechConvolutionKernel.lean` already proves for `lambda != 0`

\[
\frac1{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=
\frac{\tanh(\pi x)+\tanh(\pi(\lambda-x))}{\sinh(\pi\lambda)}.
\]

The new `SechConvolutionPrimitive.lean` candidate proves the exact differential interface

\[
\frac{d}{dx}\left[\log\cosh(\pi x)-\log\cosh(\pi(\lambda-x))\right]
=
\frac{\pi\sinh(\pi\lambda)}{\cosh(\pi x)\cosh(\pi(\lambda-x))}.
\]

No improper-integral or endpoint theorem is claimed in that module. It is now explicitly gated in the main build workflow. Once kernel-green, the remaining endpoint jump gives the intended whole-line identity

\[
\int_{\mathbb R}\frac{dx}{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=
\frac{2\lambda}{\sinh(\pi\lambda)},
\]

with `lambda=0` handled separately by removable limit/direct sech-squared evaluation.

## Next frontier

1. Read Build #859 / Gibbs #36 and the fresh workflow run triggered by `c75c0a58`; repair the first exact cubic, entropy, or primitive compiler signal.
2. Once cubic positivity clears, drive the genuine entropy derivative and Legendre differential modules through the dedicated gate.
3. Once the primitive clears, formalize its two endpoint limits and the whole-line sech convolution.
4. Begin the explicit YM cut numerator layer using full massive Ward projectors, not scalar/state-count surrogates.
5. Keep the completed-zeta/shadow/Weil route separate from any RH zero-location claim until a genuine global explicit-formula positivity bridge is kernel-checked.
