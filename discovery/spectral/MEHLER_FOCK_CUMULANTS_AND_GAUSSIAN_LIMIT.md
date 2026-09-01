# Exact cumulants and Gaussian limit of the Mehler--Fock chamber family

For the exact normalized chamber family

\[
\widehat{\rho_k}(t)=\operatorname{sech}^{2k+2}(t/2),
\qquad k\ge 0,
\]

set \(m=k+1\). The characteristic cumulant generating function is

\[
K_m(t)=\log \widehat{\rho_k}(t)=2m\log\operatorname{sech}(t/2).
\]

Its Taylor expansion at the origin is

\[
K_m(t)=-\frac m4t^2+\frac m{96}t^4-\frac m{1440}t^6+\frac{17m}{322560}t^8+O(t^{10}).
\]

With the characteristic-function convention

\[
K_m(t)=\sum_{r\ge1}\kappa_r\frac{(it)^r}{r!},
\]

all odd cumulants vanish and the first even cumulants are

\[
\boxed{\kappa_2=\frac m2},\qquad
\boxed{\kappa_4=\frac m4},\qquad
\boxed{\kappa_6=\frac m2},\qquad
\boxed{\kappa_8=\frac{17m}{8}}.
\]

Hence

\[
\operatorname{Var}(X_k)=\frac{k+1}{2},
\]

and the exact fourth central moment is

\[
\boxed{\mu_4=\kappa_4+3\kappa_2^2=\frac{m(3m+1)}4}.
\]

Therefore the standardized kurtosis and excess kurtosis are

\[
\boxed{\frac{\mu_4}{\mu_2^2}=3+\frac1m=3+\frac1{k+1}},
\qquad
\boxed{\gamma_2=\frac1{k+1}}.
\]

The sixth central moment is likewise

\[
\boxed{\mu_6=\kappa_6+15\kappa_4\kappa_2+15\kappa_2^3
=\frac{m(15m^2+15m+4)}8}.
\]

## Gaussian chamber limit

Let

\[
Y_k=\frac{X_k}{\sqrt{(k+1)/2}}.
\]

Then

\[
\widehat{Y_k}(t)
=\operatorname{sech}^{2m}\!\left(\frac{t}{\sqrt{2m}}\right).
\]

Since \(\log\operatorname{sech}u=-u^2/2+O(u^4)\),

\[
\log \widehat{Y_k}(t)
=2m\log\operatorname{sech}\!\left(\frac{t}{\sqrt{2m}}\right)
=-\frac{t^2}{2}+O\!\left(\frac{t^4}{m}\right),
\]

for fixed \(t\). Thus

\[
\boxed{\widehat{Y_k}(t)\to e^{-t^2/2}}
\]

and Levy continuity gives

\[
\boxed{Y_k\Rightarrow N(0,1)}.
\]

This is also immediate from the exact convolution law \(\rho_k=\rho_0^{*(k+1)}\): the chamber index is an integer convolution time and the normalized chamber law obeys the classical central limit theorem. The exact excess-kurtosis decay \(1/(k+1)\) quantifies the first non-Gaussian correction.

## Boundary

This is an exact consequence of the already-derived chamber characteristic function. It is a statement about the Archimedean Mehler--Fock/Gamma convolution family. It does not identify the global Weil quadratic form and does not imply RH or an amplitude sewing theorem.
