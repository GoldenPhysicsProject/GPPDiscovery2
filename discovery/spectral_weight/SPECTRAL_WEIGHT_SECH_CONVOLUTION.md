# Spectral weight as an exact self-convolution

Let

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)},\qquad
\rho(\lambda)=\frac{2}{\pi}P(\lambda)=\frac{2\lambda}{\sinh(\pi\lambda)}.
\]

With Fourier convention

\[
\widehat f(k)=\int_{\mathbb R}e^{ikx}f(x)\,dx,
\]

the normalized spectral law has

\[
\widehat\rho(k)=\operatorname{sech}^2(k/2).
\]

Now define the normalized hyperbolic-secant density

\[
h(x)=\operatorname{sech}(\pi x).
\]

Its total mass is one and its Fourier transform is the standard self-dual identity

\[
\widehat h(k)=\operatorname{sech}(k/2).
\]

Therefore

\[
\widehat{h*h}(k)=\widehat h(k)^2
=\operatorname{sech}^2(k/2)
=\widehat\rho(k).
\]

By Fourier uniqueness,

\[
\boxed{
\rho=h*h,
\qquad
\frac{2\lambda}{\sinh(\pi\lambda)}
=\int_{\mathbb R}
\operatorname{sech}(\pi x)
\operatorname{sech}(\pi(\lambda-x))\,dx.
}
\]

Equivalently, if \(X,Y\) are independent with density \(h\), then

\[
\boxed{X+Y\sim \rho.}
\]

This gives the spectral weight a literal two-channel convolution factorization. It is stronger than merely knowing positivity of \(P\): the normalized law is an exact convolution square, so its characteristic function is a pointwise square and its positive-definiteness follows immediately from Bochner theory.

The cumulants add under convolution. Since \(\rho=h*h\), every cumulant of \(\rho\) is twice the corresponding cumulant of the single hyperbolic-secant channel. In particular the previously derived

\[
\kappa_2(\rho)=\frac12,
\quad
\kappa_4(\rho)=\frac14,
\quad
\kappa_6(\rho)=\frac12,
\quad
\kappa_8(\rho)=\frac{17}{8}
\]

imply

\[
\kappa_{2m}(h)=\frac12\kappa_{2m}(\rho).
\]

This is an exact harmonic-analysis/Wiener-Hopf factorization statement. It does not by itself identify an amplitude or prove Weil positivity for the completed zeta explicit formula.
