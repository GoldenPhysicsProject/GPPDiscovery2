# Mehler-Fock / Wiener-Hopf product: exact Fourier transform and sign obstruction

Codex/GPT discovery track, 2026-08-25.

From the exact spectral bridge

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)},\qquad
m(\lambda)=\lambda\tanh(\pi\lambda),
\]

we obtained

\[
q(\lambda):=P(\lambda)m(\lambda)
=\frac{\pi\lambda^2}{\cosh(\pi\lambda)}.
\]

Use the Fourier convention

\[
\widehat f(k)=\int_{-\infty}^{\infty}e^{-ik\lambda}f(\lambda)\,d\lambda.
\]

The standard self-reciprocal hyperbolic identity is

\[
\widehat{\operatorname{sech}(\pi\lambda)}(k)
=\operatorname{sech}(k/2).
\]

Since multiplication by \(\lambda^2\) corresponds to \(-\partial_k^2\),

\[
\widehat q(k)
=-\pi\frac{d^2}{dk^2}\operatorname{sech}(k/2).
\]

A direct differentiation gives

\[
\boxed{
\widehat q(k)
=\frac{\pi}{4}\operatorname{sech}(k/2)
\left(2\operatorname{sech}^2(k/2)-1\right).
}
\]

Equivalently,

\[
\widehat q(k)
=-\frac{\pi}{4}\left(2\tanh^2(k/2)-1\right)\operatorname{sech}(k/2).
\]

Therefore \(\widehat q(k)=0\) exactly when

\[
\operatorname{sech}^2(k/2)=\frac12,
\]

that is

\[
\boxed{|k|=2\,\operatorname{arcosh}\sqrt2\approx1.762747174.}
\]

For larger \(|k|\), \(\widehat q(k)<0\). Thus the product weight \(q(\lambda)\) is pointwise nonnegative but is **not** positive definite / positive type under this Fourier convention.

This is an important separation rule. The Gamma/Mehler-Fock product is an exact positive spectral density, but it cannot be inserted as a positive-type translation kernel merely because it is pointwise positive. Any Weil/Wiener-Hopf positivity argument using this product must keep track of which side of the Fourier transform carries the nonnegative measure.
