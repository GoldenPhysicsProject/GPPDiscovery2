# Zeta-Gibbs fluctuation geometry: exact differential identities

Codex/GPT discovery track, 2026-08-24.

For the canonical number ensemble on `beta>1`,

\[
P_\beta(n)=\frac{n^{-\beta}}{\zeta(\beta)},\qquad E_n=\log n,
\]

write

\[
K(\beta)=\log\zeta(\beta),\qquad
U(\beta)=-K'(\beta),\qquad
g(\beta)=K''(\beta)=\operatorname{Var}_\beta(\log n).
\]

The existing thermodynamics note identifies `g` as the Fisher information metric. The following differential structure is immediate but useful because it fixes all signs and gives the one-dimensional fluctuation geometry in closed form.

## Exact first-law identities

The Helmholtz free energy and Gibbs/Shannon entropy are

\[
F(\beta)=-\frac{K(\beta)}{\beta},\qquad
S(\beta)=K(\beta)+\beta U(\beta).
\]

Differentiating and using `U=-K'` gives

\[
\boxed{F'(\beta)=\frac{S(\beta)}{\beta^2}},
\]

and

\[
\boxed{S'(\beta)=-\beta g(\beta)}.
\]

Since `g(\beta)>0` for every finite `beta>1`, entropy decreases strictly with inverse temperature. Equivalently, with physical temperature `T=1/\beta`,

\[
\frac{dS}{dT}=\frac{C}{T}>0.
\]

The mean logarithmic energy satisfies

\[
\boxed{U'(\beta)=-g(\beta)<0},
\]

and the heat capacity is

\[
\boxed{C(\beta)=\beta^2 g(\beta)>0}.
\]

Thus

\[
g(\beta)=\frac{C(\beta)}{\beta^2}=-U'(\beta)=-\frac{S'(\beta)}{\beta}.
\]

These are identities, not inequalities inferred numerically.

## Cubic fluctuation tensor

The third energy cumulant is

\[
\kappa_3(\beta)=-K'''(\beta)>0.
\]

Therefore

\[
\boxed{g'(\beta)=-\kappa_3(\beta)<0}.
\]

For the one-dimensional Fisher metric

\[
ds^2=g(\beta)\,d\beta^2,
\]

the Levi-Civita connection in the coordinate `beta` is

\[
\boxed{\Gamma^{\beta}_{\beta\beta}=\frac{g'}{2g}
=-\frac{\kappa_3}{2\kappa_2}},
\]

where `kappa_2=g`. Hence the skewness/cubic fluctuation controls the affine bending of the thermodynamic coordinate.

The intrinsic Riemann curvature of any one-dimensional metric is identically zero. The nontrivial information-geometric content is therefore not scalar curvature but the metric profile `g`, its cumulant hierarchy, and the affine/cubic tensor.

## Flat thermodynamic-length coordinate

Define locally

\[
\tau(\beta)=\int_{\beta_0}^{\beta}\sqrt{g(b)}\,db.
\]

Then

\[
\frac{d\tau}{d\beta}=\sqrt{g(\beta)},
\]

so the Fisher line element becomes exactly

\[
\boxed{ds^2=d\tau^2}.
\]

Thus `tau` is the canonical fluctuation-distance coordinate of the prime gas. All nontrivial arithmetic information is compressed into the nonlinear map `beta -> tau(beta)`.

## Prime decomposition

Using independent geometric prime occupations,

\[
g(\beta)=\sum_p (\log p)^2\frac{p^\beta}{(p^\beta-1)^2},
\]

and

\[
\kappa_3(\beta)
=\sum_p (\log p)^3\sum_{k\ge1}k^2p^{-k\beta}>0.
\]

Therefore both the metric and its derivative decompose exactly prime by prime.

## Boundary

Everything above holds only on the convergent Gibbs domain `beta>1`. No Fisher positivity, monotonicity, or thermodynamic interpretation is analytically continued through the zeta pole or into the critical strip by these identities alone.
