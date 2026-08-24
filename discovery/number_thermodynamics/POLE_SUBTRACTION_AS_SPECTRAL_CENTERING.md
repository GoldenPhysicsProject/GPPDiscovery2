# Zeta pole subtraction as centering of the arithmetic spectral measure

Codex/GPT discovery track, 2026-08-24.

## Shifted arithmetic measure

Start from the exact von Mangoldt Laplace representation, valid for `Re s>1`,

\[
-\frac{\zeta'}{\zeta}(s)
=\sum_{n\ge2}\Lambda(n)n^{-s}.
\]

Write

\[
s=1+z,\qquad \Re z>0,
\]

and define the positive atomic measure

\[
\boxed{
\rho:=\sum_{n\ge2}\frac{\Lambda(n)}{n}\,\delta_{\log n}.
}
\]

Then

\[
\boxed{
-\frac{\zeta'}{\zeta}(1+z)
=\int_0^\infty e^{-zx}\,d\rho(x).
}
\]

This is just the absolutely convergent Dirichlet series rewritten on logarithmic energy space.

## The pole is Lebesgue measure

For `Re z>0`,

\[
\boxed{
\frac1z=\int_0^\infty e^{-zx}\,dx.
}
\]

Therefore the pole-subtracted logarithmic derivative has the exact representation

\[
\boxed{
-\frac{\zeta'}{\zeta}(1+z)-\frac1z
=
\int_0^\infty e^{-zx}\,[d\rho(x)-dx].
}
\]

Thus removing the simple pole at `s=1` is literally the operation

\[
\text{positive arithmetic measure}\quad d\rho
\quad\longmapsto\quad
\text{signed discrepancy measure}\quad d\rho-dx.
\]

No asymptotic theorem or continuation is needed for this identity: both Laplace transforms converge ordinarily for `Re z>0`.

## Why this matters for positivity

Before pole subtraction, the arithmetic spectral measure is positive and immediately generates:

- complete monotonicity in the radial/Laplace variable;
- positive type in the Fourier variable;
- positive Hankel moment matrices.

After subtracting `dx`, those properties are no longer automatic because the measure is signed. This isolates a precise global source of difficulty:

**the local Euler factors are positive; the global renormalization required to remove the density responsible for the pole is not positivity-preserving term by term.**

This is structurally parallel to the already observed fact that the finite-prime Weil scalar multiplier changes sign even though each local Poisson convolution kernel is positive type.

## Density interpretation

Heuristically, the prime number theorem says

\[
\sum_{n\le X}\Lambda(n)\sim X.
\]

In logarithmic coordinate `x=log n`, the unshifted von Mangoldt measure therefore has exponential mean density, while the `1/n` tilt converts that leading growth into approximately constant density. The Lebesgue subtraction `dx` removes precisely that mean background.

The exact Laplace identity above does not require the PNT; the PNT only explains why `dx` is the natural continuum background.

## Completed object

The completed zeta logarithmic derivative adds the Archimedean Gamma term and elementary factors to the pole-subtracted arithmetic contribution. In the same language, those terms should be sought as explicit continuous/singular measures or kernels on logarithmic energy space.

A genuinely global positivity theorem would then have to show that the **completed** arithmetic-plus-Archimedean discrepancy functional, after all required subtractions, is a positive square on the Weil test class. This is more precise than asking local positive kernels to remain positive under analytic continuation.

## Formalization target

On `Re z>0`, formalize

\[
-\zeta'/\zeta(1+z)-1/z
\]

as the difference of the already formalized von Mangoldt L-series and the elementary Laplace transform of Lebesgue measure. The measure-theoretic packaging can follow after the series/integral identity is kernel-clean.

No RH claim is made.
