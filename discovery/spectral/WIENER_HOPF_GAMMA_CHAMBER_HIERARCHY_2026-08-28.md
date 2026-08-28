# Wiener–Hopf / Gamma full chamber hierarchy

Codex/GPT continuation, 2026-08-28. No Claude material consulted.

The Verify2 base bridge already proves, for every real x including the removable origin,

\[
W_{\mathrm{ext}}(x)=\frac{\pi}{2}\,\Re\rho_\Gamma(0,x),
\qquad
\Re\rho_\Gamma(0,x)=\frac{2}{\pi}W_{\mathrm{ext}}(x).
\]

The normalized Gamma/Mehler–Fock chamber recurrence is

\[
\rho_\Gamma(k+1,x)=R_k(x)\rho_\Gamma(k,x),
\]

with

\[
R_k(x)=\frac{2((k+1)^2+x^2)}{(k+1)(2k+3)}>0.
\]

Induction therefore gives the exact finite-product closure

\[
\rho_\Gamma(k,x)
=
\left(\prod_{j=0}^{k-1}R_j(x)\right)\rho_\Gamma(0,x).
\]

Taking real parts and inserting the base Wiener–Hopf bridge yields

\[
\boxed{
\Re\rho_\Gamma(k,x)
=
\left(\prod_{j=0}^{k-1}R_j(x)\right)
\frac{2}{\pi}W_{\mathrm{ext}}(x)
}.
\]

The full multiplier is strictly positive because every recurrence factor is strictly positive. Hence all chamber spectral densities inherit the sign of the base Wiener–Hopf weight.

This does not yet identify the higher chambers with iterated physical convolutions; it is the exact algebraic bridge obtained from the certified base normalization and certified Gamma recurrence. The next spectral target is to compare this finite product with the existing chamber-convolution formulas and determine whether the convolution normalization generates the same product recursively.
