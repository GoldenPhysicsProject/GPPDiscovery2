# Continuous sech Lévy measure: explicit weighted-integrability bound

Codex/GPT research note, 2026-09-07.

## Object

For `c >= 0`, define on `x != 0`

\[
\nu_c(x)=\frac{c}{|x|\sinh(\pi |x|)}.
\]

The raw density is not locally integrable at the origin: `nu_c(x) ~ c/(pi x^2)`.  The Lévy condition is instead

\[
I_c:=\int_{\mathbb R}(1\wedge x^2)\nu_c(x)\,dx<\infty.
\]

This note closes that condition analytically with an explicit bound, independently of the numerical quadrature audits.

## Near-zero region

For `y >= 0`, `sinh y >= y`.  Hence, for `0 < |x| <= 1`,

\[
\sinh(\pi |x|)\ge \pi |x|,
\]

and therefore

\[
x^2\nu_c(x)
=\frac{c|x|}{\sinh(\pi|x|)}
\le \frac{c}{\pi}.
\]

Thus

\[
\int_{|x|\le1}(1\wedge x^2)\nu_c(x)\,dx
=\int_{|x|\le1}x^2\nu_c(x)\,dx
\le \frac{2c}{\pi}.
\]

(The value assigned at the single point `x=0` is immaterial.)

## Exponential tail

For `x >= 1`,

\[
\sinh(\pi x)
=\frac{e^{\pi x}-e^{-\pi x}}2
=\frac{e^{\pi x}}2\bigl(1-e^{-2\pi x}\bigr)
\ge \frac{1-e^{-2\pi}}2 e^{\pi x}.
\]

Consequently

\[
\nu_c(x)
\le \frac{2c}{1-e^{-2\pi}}\frac{e^{-\pi x}}x
\le \frac{2c}{1-e^{-2\pi}}e^{-\pi x}.
\]

By evenness,

\[
\int_{|x|\ge1}(1\wedge x^2)\nu_c(x)\,dx
=2\int_1^\infty\nu_c(x)\,dx
\le
\frac{4c e^{-\pi}}{\pi(1-e^{-2\pi})}.
\]

## Closed Lévy bound

Combining the two regions gives the explicit finite estimate

\[
\boxed{
I_c\le
\frac{2c}{\pi}
+\frac{4c e^{-\pi}}{\pi(1-e^{-2\pi})}
<\infty
}
\qquad(c\ge0).
\]

Therefore `nu_c(x) dx` satisfies the one-dimensional Lévy-measure weighted-integrability condition.  This closes the analytic *integrability* obstruction for the candidate measure.  It does not by itself establish the characteristic exponent identity

\[
\log \Phi_c(t)
=\int_{\mathbb R}(\cos(tx)-1)\nu_c(x)\,dx,
\qquad
\Phi_c(t)=\operatorname{sech}^{2c}(t/2).
\]

That identity remains the next analytic theorem.  Once it is proved, Lévy–Khintchine gives genuine infinite divisibility; Fourier/Barnes identification with

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2
\]

remains a logically separate identification step.

## Formalization split

The most economical Lean decomposition is:

1. prove the local pointwise bound `x^2 * levyDensity c x <= c / pi` for `0 < |x| <= 1` from `sinh y >= y`;
2. prove a tail majorant by the exponential formula for `sinh`;
3. integrate the constant local majorant and exponential tail majorant;
4. combine by evenness and interval decomposition.

No RH, Yang–Mills, Plancherel, or probability-density claim is imported into this result.
