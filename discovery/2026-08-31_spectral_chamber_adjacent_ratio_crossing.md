# Exact adjacent spectral-chamber ratio and crossing

For the exact chamber hierarchy

\[
\rho_k(x)=\frac{2^{2k+1}}{(2k+1)!}\frac{x}{\sinh(\pi x)}\prod_{j=1}^{k}(j^2+x^2),\qquad k\ge 0,
\]

the common Archimedean factor cancels between adjacent chambers. Direct algebra gives

\[
\frac{\rho_{k+1}(x)}{\rho_k(x)}
=\frac{2^{2k+3}}{(2k+3)!}\frac{(2k+1)!}{2^{2k+1}}\big((k+1)^2+x^2\big)
=\frac{2\big((k+1)^2+x^2\big)}{(k+1)(2k+3)}.
\]

Hence adjacent chambers have a unique nonnegative crossing determined by

\[
\rho_{k+1}(x)=\rho_k(x)
\iff 2x^2=k+1
\iff |x|=\sqrt{\frac{k+1}{2}}.
\]

Therefore

\[
|x|<\sqrt{\frac{k+1}{2}}\Rightarrow \rho_{k+1}(x)<\rho_k(x),
\]

while

\[
|x|>\sqrt{\frac{k+1}{2}}\Rightarrow \rho_{k+1}(x)>\rho_k(x).
\]

This sharpens the previously recorded universal tail statement. Every fixed chamber has the same exponential decay scale \(e^{-\pi |x|}\), but increasing the chamber index transfers relative spectral weight from the central region into the tails. The transfer threshold grows only as \(\sqrt{k/2}\).

The result is purely within the exact Gamma/Mehler-Fock chamber hierarchy. It does not imply a repeated-sech convolution law and has no direct Weil-positivity consequence.

`discovery/spectral_chamber_adjacent_ratio.py` numerically regression-checks the ratio formula for several chambers and spectral points; the identity itself is algebraic.
