# Codex formalization update — 2026-08-27

Codex/GPT track only. No separate Claude work is used in this update.

## Live branch and CI correction

The authoritative live `GPPVerify2` `codex/lean-workbench` head at the start of this continuation was `c75c0a5800b2dad2f65363e95abd3a3efe1072d9`. Later hashes quoted in a split-thread summary were not on the live branch and are not treated as certified history.

Build #863 at `c75c0a58` failed at the explicitly gated sech-convolution module. Every scalar-box checkpoint before that gate passed, including regulator bounds, log-series kernel, Spence constant/continuity/derivative/constancy/identity, and the real inversion kernel. Dedicated Gibbs #40 failed later in `VonMangoldtCubicPositivity.lean`; the von-Mangoldt cosine bridge itself compiled green.

## Cubic von-Mangoldt response

The arithmetic density remains

\[
c_3(\beta,n)=\Lambda(n)(\log n)^2e^{-\beta\log n},\qquad \beta>1.
\]

Gibbs #40 showed that after expanding the twice-`logMul` coefficient the cpow exponent had already normalized to `-β`, so the generic `t=0` cosine rewrite no longer matched syntactically. The proof now simplifies the coefficient real/imaginary parts explicitly, specializes `natCast_neg_cpow_re` at `t=0`, normalizes that lemma, and rewrites the resulting `n^{-β}` real part. This repair is Verify2 commit `c8def559979bf125123b62722ee952b9f7a903cd`. The theorem statement, half-plane hypothesis, and strict `n=2` witness are unchanged.

## Spectral/chamber convolution

Build #863 exposed a parser defect rather than a mathematical one: Unicode `λ` was used as a binder in `SechConvolutionKernel.lean`, but Lean treats `λ` as reserved lambda syntax. The kernel binders were renamed to `lam` at Verify2 commit `99afd4bdb9810dc06c4c961b7a5f96d57c936537`, and the dependent primitive binders were repaired at `567026a7292ab7bb9dead5ec93cfc50e82251f28`.

The intended exact differential interface remains

\[
\frac{d}{dx}\left[\log\cosh(\pi x)-\log\cosh(\pi(\lambda-x))\right]
=
\frac{\pi\sinh(\pi\lambda)}{\cosh(\pi x)\cosh(\pi(\lambda-x))}.
\]

No whole-line integral is promoted until this module is kernel-green. Once green, the next target is the endpoint jump and

\[
\int_{\mathbb R}\frac{dx}{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=
\frac{2\lambda}{\sinh(\pi\lambda)},
\]

with `lambda=0` handled separately.

## Scalar box and amplitude boundary

Build #863 independently confirms the scalar-box analytic checkpoint chain through the real inversion kernel. The valid domination remains the structured mixed-log majorant; the independent-square surrogate remains retracted. The next amplitude layer remains explicit Yang-Mills/gravity sewn tree currents and numerators with the full massive Ward projector, not a scalar/state-count surrogate.

## Principal-series/completed-zeta response

The formalized structural statements remain

\[
\operatorname{Re}\mathcal R(\Delta)=0\quad (\operatorname{Re}\Delta=1),
\qquad
\mathcal R(\Delta)=-\mathcal R(2-\Delta),
\]

where the completed-zeta logarithmic response is defined. These are representation/functional-equation statements only, not zero-location results.

## Current CI and next frontier

Verify2 head is now `c8def559979bf125123b62722ee952b9f7a903cd`. Build #869 is in progress and dedicated Gibbs #46 is pending on that head.

1. Read #869/#46 and repair the first exact remaining compiler signal.
2. If the spectral primitive clears, formalize its endpoint limits and whole-line convolution.
3. If cubic positivity clears, drive the genuine entropy/free-energy differential theorem gate.
4. Preserve the scalar-box closure while beginning explicit YM/gravity sewn numerators with full Ward reconstruction.
5. Keep the completed-zeta/Weil route separated from any RH claim until a genuine explicit-formula positivity equivalence is kernel-checked.
