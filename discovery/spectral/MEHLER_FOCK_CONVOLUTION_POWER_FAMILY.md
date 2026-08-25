# Exact Mehler-Fock convolution-power family

## Scope

This note extends the verified normalized Mehler-Fock / Wiener-Hopf density

\[
\rho(x)=\frac{2x}{\sinh(\pi x)},\qquad \widehat\rho(k)=\operatorname{sech}^2(k/2),
\]

under the Fourier convention

\[
\widehat f(k)=\int_{\mathbb R}e^{ikx}f(x)\,dx,
\qquad
f(x)=\frac1{2\pi}\int_{\mathbb R}e^{-ikx}\widehat f(k)\,dk.
\]

No RH or amplitude claim is made. This is an exact harmonic-analysis identity.

## The all-order family

For every integer \(m\ge 1\), define

\[
\rho_m(x)
=\frac{2^{2m-1}}{\pi\,\Gamma(2m)}\,|\Gamma(m+ix)|^2.
\]

The classical beta/Gamma Fourier integral

\[
\int_{\mathbb R}e^{i\omega u}\operatorname{sech}^{2m}u\,du
=\frac{2^{2m-1}}{\Gamma(2m)}
 \left|\Gamma\!\left(m+\frac{i\omega}{2}\right)\right|^2
\]

gives, after \(k=2u\),

\[
\rho_m(x)
=\frac1{2\pi}\int_{\mathbb R}e^{-ikx}
  \operatorname{sech}^{2m}(k/2)\,dk.
\]

Hence

\[
\boxed{\widehat{\rho_m}(k)=\operatorname{sech}^{2m}(k/2)}.
\]

Because \(\widehat\rho=\operatorname{sech}^2(k/2)\), Fourier multiplication gives the exact convolution law

\[
\boxed{\rho_m=\rho^{*m}}.
\]

Thus every finite convolution power stays in one explicit Gamma-product family.

## Polynomial-times-base-density closure

Using

\[
|\Gamma(m+ix)|^2
=\left(\prod_{j=1}^{m-1}(j^2+x^2)\right)|\Gamma(1+ix)|^2
\]

and

\[
|\Gamma(1+ix)|^2=\frac{\pi x}{\sinh(\pi x)},
\]

we obtain

\[
\boxed{
\rho_m(x)
=\frac{2^{2m-2}}{\Gamma(2m)}
\left(\prod_{j=1}^{m-1}(j^2+x^2)\right)\rho(x).
}
\]

The first cases are

\[
\rho_1=\rho,
\]

\[
\rho_2(x)=\frac{2}{3}(1+x^2)\rho(x),
\]

\[
\rho_3(x)=\frac{2}{15}(1+x^2)(4+x^2)\rho(x).
\]

This is a useful exact chamber/convolution closure: repeated gluing does not generate a new transcendental spectral weight; it only multiplies the base Mehler-Fock density by a positive even polynomial with a known normalization.

## Probability and positivity consequences

Since \(\widehat{\rho_m}(0)=1\),

\[
\int_{\mathbb R}\rho_m(x)\,dx=1.
\]

Also \(\rho_m(x)>0\) for all real \(x\), with the removable \(x=0\) value inherited from the Gamma form. Therefore the entire convolution semigroup at integer time \(m\) is an explicit positive probability density.

The characteristic function is

\[
\varphi_m(k)=\operatorname{sech}^{2m}(k/2),
\]

so cumulants scale linearly:

\[
\kappa_n[\rho_m]=m\,\kappa_n[\rho].
\]

In particular, all odd cumulants vanish and

\[
\operatorname{Var}(\rho_m)=\frac m2.
\]

## Exact boundary

This result strengthens the existing one-step factorization \(\rho=h*h\), \(h(x)=\operatorname{sech}(\pi x)\), to every integer convolution power. It does **not** establish an amplitude sewing theorem, a full \(A_2\) chamber integral, or a Weil/RH positivity theorem. Those require their own measure/intertwining identifications.