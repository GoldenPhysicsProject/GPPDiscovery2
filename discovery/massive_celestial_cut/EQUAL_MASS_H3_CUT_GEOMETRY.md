# Equal-mass D-dimensional cut as a fixed-radius H^3 shell

Codex/GPT discovery track, 2026-08-24.

## Setup

Split a D-dimensional massless cut momentum as

\[
L=\ell+L_\perp,\qquad \mu^2=-L_\perp^2\ge0.
\]

Then `L^2=0` implies the four-dimensional momentum is timelike,

\[
\ell^2=\mu^2.
\]

For a two-particle cut with total four-momentum `P=(M,0)` and `M>2\mu`, write

\[
\ell_1=(E,\mathbf p),\qquad \ell_2=(E,-\mathbf p),
\]

with

\[
E=\frac M2,\qquad
|\mathbf p|=\frac12\sqrt{M^2-4\mu^2}.
\]

## Hyperbolic radius

Normalize the massive momentum by its mass:

\[
y:=\frac{\ell}{\mu}\in H^3,\qquad y^2=1,
\]

and parameterize

\[
y=(\cosh r,\sinh r\,\hat n),\qquad \hat n\in S^2.
\]

Comparison with the center-of-mass cut gives the exact identities

\[
\boxed{\cosh r=\frac{M}{2\mu}},
\]

\[
\boxed{\sinh r=\frac{\sqrt{M^2-4\mu^2}}{2\mu}},
\]

and hence

\[
\boxed{\tanh r=\sqrt{1-\frac{4\mu^2}{M^2}}=:\beta}.
\]

Equivalently,

\[
r=\operatorname{arcosh}\frac{M}{2\mu}
 =\operatorname{artanh}\beta
 =\log\frac{M+\sqrt{M^2-4\mu^2}}{2\mu}.
\]

Thus a fixed-`M`, fixed-`\mu` two-particle cut is not the whole massive hyperboloid: it is the angular `S^2` at one fixed hyperbolic radius `r`.

## Phase-space meaning

The standard integrated two-body phase space is

\[
\int d\Pi_2=\frac{1}{8\pi}
\sqrt{1-\frac{4\mu^2}{M^2}}.
\]

Therefore the exact hyperbolic form is

\[
\boxed{\int d\Pi_2=\frac{\tanh r}{8\pi}}.
\]

This identifies the velocity suppression at threshold with the radial coordinate of `H^3`.

At threshold `M\downarrow2\mu`, one has `r\downarrow0` and the phase space vanishes linearly as `tanh r~r`. In the massless limit `\mu\downarrow0` at fixed `M`, `r\to\infty` and `tanh r\to1`, recovering the massless integrated phase-space factor `1/(8\pi)`.

## Spherical transform interface

For radial harmonic analysis on `H^3`, the zonal spherical functions are

\[
\varphi_\lambda(r)=\frac{\sin(\lambda r)}{\lambda\sinh r},
\]

with positive-`\lambda` radial Plancherel density

\[
\frac{\lambda^2}{2\pi^2}\,d\lambda.
\]

The equal-mass cut therefore samples the massive principal-series radial basis at the single radius

\[
r=r(M,\mu)=\operatorname{arcosh}(M/2\mu),
\]

while its remaining cut integration is over the angular `S^2`.

This is the correct geometric starting point for D-dimensional unitarity in celestial variables. The massless limit is singular at the level of the raw `H^3` radial function because `r\to\infty`; obtaining the previously derived massless celestial Gamma/Beta weight requires the appropriate rescaled/Mellin boundary limit, not simply substituting `\mu=0` into `\varphi_\lambda`.

## Boundary

This identifies the geometry and phase-space measure only. It does not yet compute D-dimensional Yang--Mills or gravity state sums, `\mu^2` numerator insertions, or rational terms. Those must be derived from the actual massive four-dimensional cut trees (equivalently the D-dimensional polarization/state sum) before celestial transformation.
