# Exact even moments of the spectral weight P(lambda)

Codex/GPT discovery track, 2026-08-25.

Let

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)},\qquad \lambda\ge0.
\]

For every integer `n>=0`, define

\[
I_n=\int_0^\infty \lambda^{2n}P(\lambda)\,d\lambda.
\]

Using the absolutely convergent positive expansion

\[
\frac1{\sinh(\pi\lambda)}
=2\sum_{k=0}^\infty e^{-(2k+1)\pi\lambda},
\]

Tonelli gives

\[
I_n
=2\pi\sum_{k\ge0}\int_0^\infty
\lambda^{2n+1}e^{-(2k+1)\pi\lambda}\,d\lambda.
\]

Since

\[
\int_0^\infty \lambda^{2n+1}e^{-a\lambda}\,d\lambda
=\frac{(2n+1)!}{a^{2n+2}},
\]

we obtain the exact zeta form

\[
\boxed{
I_n=
\frac{2(2n+1)!}{\pi^{2n+1}}
\left(1-2^{-2n-2}\right)\zeta(2n+2).
}
\]

Using the classical even-zeta/Bernoulli evaluation,

\[
\boxed{
I_n=
\frac{(-1)^n(2^{2n+2}-1)B_{2n+2}}{2n+2}\,\pi.
}
\]

The Bernoulli sign alternation makes the right-hand side positive, as required by the positive integrand.

The first values are

\[
I_0=\frac\pi4,\qquad
I_1=\frac\pi8,\qquad
I_2=\frac\pi4,\qquad
I_3=\frac{17\pi}{16}.
\]

After normalizing `P` to a probability density on the half-line by

\[
\rho(\lambda)=\frac4\pi P(\lambda),
\]

its exact even moments are

\[
\boxed{
\mathbb E_\rho[\lambda^{2n}]
=
\frac{4(-1)^n(2^{2n+2}-1)B_{2n+2}}{2n+2}.
}
\]

In particular,

\[
\mathbb E[\lambda^2]=\frac12,
\qquad
\mathbb E[\lambda^4]=1.
\]

This is an exact harmonic-analysis result for the spectral weight itself. It is independent of the separate A2 chamber-convolution result `M_2=1/90` and does not by itself establish a loop-amplitude theorem.

## Formalization target

A clean Lean promotion can be split into: (1) the positive odd-exponential expansion of `1/sinh`; (2) Tonelli/interchange; (3) the Gamma integral at integer exponent; (4) the odd-integer zeta sum `(1-2^-s) zeta(s)`; and optionally (5) the Bernoulli simplification. The zeta-form theorem is the preferred first kernel target because it minimizes Bernoulli-number infrastructure.
