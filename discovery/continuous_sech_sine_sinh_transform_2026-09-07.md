# Continuous sech Lévy exponent: sine-over-sinh transform

Codex/GPT research note, 2026-09-07.

For the compensated exponent kernel

\[
K_c(t,x)=\frac{c(1-\cos tx)}{|x|\sinh(\pi |x|)},
\]

the remaining analytic identity can be reduced to the classical sine transform

\[
S(t)=\int_0^\infty \frac{\sin(tx)}{\sinh(\pi x)}\,dx.
\]

For \(x>0\),

\[
\frac1{\sinh(\pi x)}
=2\sum_{n=0}^\infty e^{-(2n+1)\pi x}.
\]

Termwise integration is justified once domination is supplied, and

\[
\int_0^\infty e^{-ax}\sin(tx)\,dx=\frac{t}{a^2+t^2}\qquad(a>0).
\]

Hence

\[
S(t)=2t\sum_{n=0}^\infty
\frac1{(2n+1)^2\pi^2+t^2}.
\]

Using the half-integer Mittag-Leffler identity

\[
\sum_{n=0}^\infty\frac1{(n+\tfrac12)^2+a^2}
=\frac{\pi}{2a}\tanh(\pi a),
\]

with \(a=|t|/(2\pi)\), one obtains for \(t\ne0\)

\[
\sum_{n=0}^\infty
\frac1{(2n+1)^2\pi^2+t^2}
=\frac1{4|t|}\tanh\frac{|t|}{2}.
\]

Oddness then gives the exact transform

\[
\boxed{S(t)=\frac12\tanh\frac t2}.
\]

At \(t=0\) both sides vanish.

Therefore, for

\[
I_c(t)=2c\int_0^\infty
\frac{1-\cos(tx)}{x\sinh(\pi x)}\,dx,
\]

once differentiation under the integral is formalized,

\[
I_c'(t)=2cS(t)=c\tanh\frac t2.
\]

Since \(I_c(0)=0\),

\[
\boxed{I_c(t)=2c\log\cosh\frac t2}.
\]

Equivalently on the full line,

\[
\boxed{
\int_{\mathbb R}K_c(t,x)\,dx
=2c\log\cosh\frac t2}.
\]

This is the exact Lévy-Khintchine exponent required for
\(\Phi_c(t)=\operatorname{sech}^{2c}(t/2)\). The remaining formal obligations are: compensated-kernel integrability, differentiation under the integral sign, and the half-integer Mittag-Leffler/tanh summation (or an equivalent contour proof). No RH, Plancherel, or loop-measure claim is implied by this identity.
