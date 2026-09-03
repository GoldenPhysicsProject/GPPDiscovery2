# Continuous Gamma-chamber convolution semigroup

The integer chamber hierarchy admits a natural exact continuous extension. For every real `c > 0`, define

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}\Gamma(c+ix)\Gamma(c-ix)
=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2.
\]

The Barnes Fourier transform gives, with convention
\(\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx\),

\[
\int_{\mathbb R}|\Gamma(c+ix)|^2e^{-itx}\,dx
=\frac{2\pi\Gamma(2c)}{4^c}\operatorname{sech}^{2c}(t/2),
\]

hence

\[
\boxed{\widehat{\rho_c}(t)=\operatorname{sech}^{2c}(t/2)}.
\]

Consequences:

1. `rho_c` is normalized because its transform equals 1 at `t=0`.
2. For `c,d>0`, multiplication of characteristic functions gives
   \[
   \boxed{\rho_c*\rho_d=\rho_{c+d}}.
   \]
3. The previously discovered integer hierarchy is the lattice restriction
   \[
   \rho_k^{\mathrm{chamber}}=\rho_{k+1},\qquad k\in\mathbb N.
   \]
   Therefore `rho_k * rho_l = rho_{k+l+1}` is exactly the restriction of an additive continuous semigroup in the parameter `c`.
4. Expanding the logarithm at the origin,
   \[
   \log\widehat{\rho_c}(t)=2c\log\operatorname{sech}(t/2)
   =-\frac{c}{4}t^2+O(t^4),
   \]
   gives
   \[
   \boxed{\operatorname{Var}_{\rho_c}(X)=\frac c2}.
   \]
5. This continuous family is the symmetric generalized-hyperbolic-secant / Meixner convolution family. The hyperbolic-secant law is known to be infinitely divisible, which explains why noninteger positive powers of the characteristic function remain probability characteristic functions.

This is a stronger structural salvage than the discrete chamber recurrence alone: the Gamma spectral weights sit on an exact continuous probability convolution flow, and the chamber index is a discrete sampling of the flow time.

Formalization status: discovery-level. Lean promotion requires the Barnes Fourier-Gamma transform for arbitrary positive real `c`, normalization/positivity, and Fourier uniqueness/convolution. No identification with cut-loop depth or the separate Mehler-Fock spectral transform is asserted without an additional theorem.
