# Normalized spectral-weight characteristic function and cumulants

For the exact even spectral weight

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)},
\]

the previously established Fourier transform convention is

\[
\widehat P(k)=\int_{-\infty}^{\infty}e^{ik\lambda}P(\lambda)\,d\lambda
=\frac{\pi}{2\cosh^2(k/2)}.
\]

Since \(\widehat P(0)=\pi/2\), the normalized full-line probability density is

\[
\rho(\lambda)=\frac{2}{\pi}P(\lambda)
=\frac{2\lambda}{\sinh(\pi\lambda)}.
\]

Hence its characteristic function is exactly

\[
\boxed{\varphi(k)=\int_{\mathbb R}e^{ik\lambda}\rho(\lambda)\,d\lambda
=\operatorname{sech}^2(k/2).}
\]

This packages the complete even-moment hierarchy into one elementary function.  In particular

\[
\log\varphi(k)=-2\log\cosh(k/2).
\]

Using

\[
\log\cosh x
=\sum_{n\ge1}\frac{2^{2n}(2^{2n}-1)B_{2n}}
{2n(2n)!}x^{2n},
\]

and the characteristic-function cumulant convention

\[
\log\varphi(k)=\sum_{m\ge1}\kappa_m\frac{(ik)^m}{m!},
\]

all odd cumulants vanish and

\[
\boxed{
\kappa_{2n}
=(-1)^{n+1}\frac{2(2^{2n}-1)B_{2n}}{2n}
\qquad(n\ge1).
}
\]

Because \((-1)^{n+1}B_{2n}>0\), every even cumulant is positive.  The first values are

\[
\boxed{
\kappa_2=\frac12,\quad
\kappa_4=\frac14,\quad
\kappa_6=\frac12,\quad
\kappa_8=\frac{17}{8}.
}
\]

The corresponding normalized even moments begin

\[
\boxed{
\mathbb E[\lambda^2]=\frac12,\quad
\mathbb E[\lambda^4]=1,\quad
\mathbb E[\lambda^6]=\frac{17}{4},\quad
\mathbb E[\lambda^8]=31.
}
\]

The direct moment formula follows from the geometric expansion of \(1/\sinh(\pi\lambda)\):

\[
\mathbb E_\rho[\lambda^{2n}]
=\frac{4(2n+1)!}{\pi^{2n+2}}
\left(1-2^{-2n-2}\right)\zeta(2n+2).
\]

This is a harmonic-analysis result about the exact spectral weight.  It is not, by itself, an amplitude theorem or a Weil-positivity theorem.  The separate \(A_2\) chamber-convolution result \(M_2=1/90\) remains logically distinct.
