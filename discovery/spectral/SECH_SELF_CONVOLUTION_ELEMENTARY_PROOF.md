# Elementary proof of the sech self-convolution identity

Codex/GPT discovery track, 2026-08-25.

Let

\[
h(x)=\operatorname{sech}(\pi x).
\]

The normalized Wiener-Hopf spectral density is

\[
\rho(\lambda)=\frac{2\lambda}{\sinh(\pi\lambda)}.
\]

The exact self-convolution identity

\[
\boxed{(h*h)(\lambda)=\rho(\lambda)}
\]

can be proved without Fourier inversion.

Set

\[
A=\pi x,\qquad B=\pi(\lambda-x),
\]

so `A+B=pi lambda`. The hyperbolic addition formula gives

\[
\tanh A+\tanh B
=\frac{\sinh(A+B)}{\cosh A\cosh B}.
\]

Hence, for `lambda != 0`,

\[
\frac1{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=\frac{\tanh(\pi x)+\tanh(\pi(\lambda-x))}
{\sinh(\pi\lambda)}.
\]

An antiderivative of the numerator is

\[
\frac1\pi
\log\frac{\cosh(\pi x)}{\cosh(\pi(\lambda-x))}.
\]

At the two ends,

\[
\lim_{x\to+\infty}
\frac{\cosh(\pi x)}{\cosh(\pi(\lambda-x))}
=e^{\pi\lambda},
\]

while

\[
\lim_{x\to-\infty}
\frac{\cosh(\pi x)}{\cosh(\pi(\lambda-x))}
=e^{-\pi\lambda}.
\]

Therefore

\[
\int_{-\infty}^{\infty}
\frac{dx}{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=\frac{2\lambda}{\sinh(\pi\lambda)}.
\]

Thus

\[
\boxed{
\int_{\mathbb R}
\operatorname{sech}(\pi x)
\operatorname{sech}(\pi(\lambda-x))\,dx
=\frac{2\lambda}{\sinh(\pi\lambda)}.
}
\]

At `lambda=0`, the continuous limit is `2/pi`, and directly

\[
\int_{\mathbb R}\operatorname{sech}^2(\pi x)\,dx=\frac2\pi,
\]

so the identity extends continuously through the origin when the right-hand side is interpreted by its removable limit.

This proof gives a cleaner formalization route than invoking a full Fourier inversion theorem: prove the hyperbolic addition identity, the explicit antiderivative, and the two endpoint limits.
