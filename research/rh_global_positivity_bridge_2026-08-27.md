# RH global positivity bridge — 2026-08-27

Codex/GPT track only. No Claude material inspected.

## Exact formal target already in GPPVerify2

`GppWeilCriterion.rh_iff_weil_pairedForm_nonneg` proves

\[
\mathrm{RH}\;\Longleftrightarrow\;
\forall S\subset Z_{\mathrm{nt}}\text{ finite},\;\forall c,
\operatorname{Re}\sum_{\rho\in S}\overline{c(1-\bar\rho)}c(\rho)\ge0.
\]

Thus the remaining RH problem in this track is not the algebraic involution/fixed-locus step. It is the analytic theorem that produces this finite zero-pairing positivity from the explicit formula / operator realization.

## What the newer prime-Poisson line actually proves

For every `p>1`, `a>0`, the local response

\[
W_{p,a}(t)=\log p\,[K_{p^{-a}}(t\log p)-1]
\]

is positive type, and equals

\[
2\,\Re\bigl(-\partial_s\log\zeta_p(a+it)\bigr).
\]

Finite sums over primes preserve positive type. On the honest Dirichlet half-plane `a>1`, the global von-Mangoldt identity already formalized gives

\[
\Re\left(-\frac{\zeta'}{\zeta}(a+it)\right)
=
\sum_{n\ge1}\Lambda(n)e^{-a\log n}\cos(t\log n).
\]

This strongly suggests the next kernel theorem: the global real logarithmic-derivative response is positive type for `a>1`.

## Critical correction: why finite-prime PSD does not by itself prove Weil PSD

The classical Weil explicit-formula quadratic form is not the same object as the translation-invariant local prime kernel. The prime contribution enters as a perturbation against the archimedean term. Therefore the inference

`each prime kernel PSD => Weil form PSD`

is invalid. In the usual explicit-formula sign convention the prime piece is subtracted from the archimedean piece, so positive type of the prime response alone gives no Loewner domination.

A second warning is spectral: the prime kernels have discrete Fourier support at frequencies `k log p`, whereas a purely archimedean Wiener-Hopf square carries a continuous spectral density. A naive claim that `archimedean kernel - prime kernel` is positive type as a translation-invariant kernel would require domination of those discrete atoms by the archimedean spectral measure and is therefore not the right formulation. The correct positivity must live in the explicit-formula test-function/operator space, not in a pointwise subtraction of two stationary kernels.

## The sharpened bridge

The useful chain is now:

1. Prove global prime-response positive type on `a>1`.
2. Formalize the exact classical Weil explicit-formula quadratic form on convolution-square test functions, including archimedean and prime pieces with the correct sign.
3. Formalize finite interpolation: arbitrary coefficients on a finite zero set can be realized by an admissible transform. This is the missing passage from classical Weil positivity to the already-proved `pairedForm` criterion.
4. Investigate the only genuinely RH-level step: a positivity-preserving renormalized continuation/compression from the convergent prime response to the critical-line explicit-formula form. If this is proved unconditionally, `rh_iff_weil_pairedForm_nonneg` closes RH immediately.

## Wiener-Hopf/celestial role

The focused kinematic-block paper identifies the archimedean explicit-formula density `Re psi(s)`, the positive weight `|Gamma(2s)|^2`, and the Wiener-Hopf factorization of the Plancherel weight. The correct objective is therefore to factor the archimedean operator as a manifest square and then compare the arithmetic perturbation in that Hilbert/test-function space. This is materially stronger and more precise than merely showing pointwise positivity of either side.

## Immediate executable targets

- `GlobalVonMangoldtPositiveType.lean`: prove `t -> Re(-zeta'/zeta(a+it))` is positive type for `a>1`, using the existing von-Mangoldt cosine series and Gram-square machinery.
- `WeilFiniteInterpolation.lean`: isolate a finite transform-interpolation theorem sufficient to convert classical explicit-formula positivity into `GppWeilCriterion.pairedForm` positivity.
- Keep the critical renormalization/compression theorem named explicitly; do not smuggle it in as analytic continuation, since ordinary analytic continuation does not preserve positive type.

If the compression/explicit-formula theorem is closed with all hypotheses discharged, the existing criterion yields the Riemann Hypothesis and it should be claimed as such.