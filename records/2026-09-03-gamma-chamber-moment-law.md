# Gamma chamber probability moment law

Starting from the audited Fourier identity

\[
\widehat{\rho_k}(t)=\operatorname{sech}^{2k+2}(t/2),
\qquad
\rho_k(x)=\frac{2^{2k+1}}{\pi\Gamma(2k+2)}|\Gamma(k+1+ix)|^2,
\]

with Fourier convention \(\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx\), the chamber densities have the following immediate consequences.

1. Normalization: \(\widehat{\rho_k}(0)=1\), hence \(\int_{\mathbb R}\rho_k(x)\,dx=1\).
2. Evenness gives mean zero.
3. Since
   \[
   \log \widehat{\rho_k}(t)=(2k+2)\log\operatorname{sech}(t/2)
   =-\frac{k+1}{4}t^2+O(t^4),
   \]
   the second moment/variance is
   \[
   \operatorname{Var}_{\rho_k}(X)=-\widehat{\rho_k}''(0)=\frac{k+1}{2}.
   \]
4. This is compatible with the exact convolution law \(\rho_k=\rho_0^{*(k+1)}\): \(\operatorname{Var}(\rho_0)=1/2\), and variances add under convolution.

Independent high-precision quadrature check in this research run gave, for k=0,1,2,3 respectively, masses exactly 1 to working precision and second moments 0.5, 1.0, 1.5, 2.0.

Status: exact analytic consequence of the discovery-level Barnes/Fourier transform identity; not yet Lean-certified because the transform identity and Fourier differentiation/uniqueness layer have not yet been promoted.

This strengthens the interpretation of the Gamma chamber hierarchy: it is not only a convolution semigroup but a normalized probability family with linearly growing fluctuation scale, \(\sigma_k^2=(k+1)/2\).
