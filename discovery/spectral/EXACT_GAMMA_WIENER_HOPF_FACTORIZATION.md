# Exact Gamma half-plane factorization of the Mehler--Fock convolution family

The normalized spectral family has Fourier transform

\[
\widehat\rho_m(k)=\operatorname{sech}^{2m}(k/2),\qquad m\in\mathbb Z_{>0}.
\]

Use the classical Gamma modulus identity

\[
\Gamma\!\left(\frac12+iy\right)
\Gamma\!\left(\frac12-iy\right)
=\frac{\pi}{\cosh(\pi y)}.
\]

With \(y=k/(2\pi)\), define

\[
H_+(z):=\frac1\pi
\Gamma\!\left(\frac12-\frac{i z}{2\pi}\right)^2,
\qquad
H_-(z):=\frac1\pi
\Gamma\!\left(\frac12+\frac{i z}{2\pi}\right)^2.
\]

Then for every real \(k\),

\[
\boxed{
H_+(k)H_-(k)=\operatorname{sech}^2(k/2).
}
\]

Moreover

\[
H_-(k)=\overline{H_+(k)},
\qquad H_+(0)=H_-(0)=1.
\]

The pole sets are explicit:

\[
\operatorname{poles}(H_+)=\{-i\pi(2n+1):n\ge0\},
\]

\[
\operatorname{poles}(H_-)=\{+i\pi(2n+1):n\ge0\}.
\]

Because the Gamma function has no zeros, \(H_+\) is holomorphic and zero-free on the open upper half-plane, while \(H_-\) is holomorphic and zero-free on the open lower half-plane. Thus this is an exact normalized scalar half-plane factorization of the spectral Fourier kernel. No Cauchy-integral reconstruction is required.

For the full convolution family,

\[
\boxed{
\widehat\rho_m(k)=H_+(k)^mH_-(k)^m.
}
\]

So every integer convolution chamber inherits the same half-plane factors by simple powers.

A further exact unitary boundary factor is

\[
\boxed{
S(k):=\frac{H_-(k)}{H_+(k)}
=\left[
\frac{\Gamma(\frac12+\frac{i k}{2\pi})}
{\Gamma(\frac12-\frac{i k}{2\pi})}
\right]^2,
\qquad |S(k)|=1
}
\]

for real \(k\). Hence the positive spectral modulus and a pure principal-series phase are separated canonically on the real axis.

## Boundary of the claim

This is an exact Gamma half-plane factorization of the already established \(\operatorname{sech}^{2m}\) Fourier family. Calling it a *canonical outer Wiener--Hopf factorization* would additionally require checking the precise Hardy/outer normalization and growth hypotheses adopted in the target theorem. Those analytic function-space conditions are not asserted here. The algebraic factorization, zero-free half-plane domains, pole locations, normalization, and unit-modulus boundary ratio are exact.
