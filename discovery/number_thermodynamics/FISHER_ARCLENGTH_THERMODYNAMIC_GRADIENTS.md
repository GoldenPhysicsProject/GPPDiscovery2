# Fisher-arclength thermodynamic gradient identities

Codex/GPT discovery track, 2026-08-25.

For the zeta Gibbs ensemble on `beta>1`, let

\[
K(\beta)=\log\zeta(\beta),\qquad
U=-K',\qquad
g=K''=\operatorname{Var}_\beta(\log n)>0,
\]

and

\[
C=\beta^2g,
\qquad
S=K+\beta U.
\]

The exact response identities are

\[
U'=-g,
\qquad
S'=-\beta g.
\]

Define Fisher arclength by

\[
\frac{d\tau}{d\beta}=\sqrt{g(\beta)}.
\]

Since `g>0` for finite `beta>1`,

\[
\frac{d\beta}{d\tau}=\frac1{\sqrt g}.
\]

Therefore

\[
\boxed{
\frac{dU}{d\tau}=-\sqrt g=-\frac{\sqrt C}{\beta}
}
\]

and

\[
\boxed{
\frac{dS}{d\tau}=-\beta\sqrt g=-\sqrt C.
}
\]

Hence the heat capacity has the coordinate-invariant Fisher-gradient form

\[
\boxed{
C(\beta)=\left(\frac{dS}{d\tau}\right)^2
}
\]

and equivalently

\[
\boxed{
C(\beta)=\beta^2\left(\frac{dU}{d\tau}\right)^2.
}
\]

Thus the thermodynamic stability quantity `C` is exactly the squared speed of entropy along the one-dimensional Fisher manifold; the entropy decreases monotonically in the orientation of increasing `beta` and its Fisher-speed is `sqrt(C)`.

A further exact ratio is

\[
\boxed{
\frac{dS}{dU}=\beta,
}
\]

because `S'/U'=beta` wherever `g>0`. This is the usual thermodynamic conjugacy relation recovered directly from the arithmetic Gibbs geometry.

These identities are restricted to the ordinary Gibbs half-plane `beta>1`. They do not analytically continue positivity into the critical strip and have no zero-location implication by themselves.

## Formalization target

The Lean target is elementary once the existing kernel-checked identities `U'=-g`, `S'=-beta*g`, `C=beta^2*g`, and positivity of `g` are collected under a single real-variable interface. The only additional analytic layer is the derivative of the arclength coordinate `tau`; the squared-gradient identities can alternatively be formalized algebraically using a local symbol `v=sqrt(g)` before constructing the global integral coordinate.
