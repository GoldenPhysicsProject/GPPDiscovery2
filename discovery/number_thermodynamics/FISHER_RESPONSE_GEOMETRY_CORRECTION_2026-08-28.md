# Zeta Gibbs Fisher response geometry: convexity and the one-dimensional curvature boundary

Codex/GPT continuation, 2026-08-28.

For the one-parameter zeta Gibbs family on `beta > 1`, let

\[
g(\beta)=\kappa_2(\beta)=\operatorname{Var}_\beta(\log n).
\]

Existing exact cumulant differentiation gives

\[
\boxed{g'(\beta)=-\kappa_3(\beta)},
\qquad
\boxed{g''(\beta)=\kappa_4(\beta)}.
\]

The current formalized sign results give `kappa_3 > 0` and `kappa_4 > 0` on `beta>1`, hence

\[
\boxed{g'(\beta)<0},\qquad
\boxed{g''(\beta)>0}.
\]

Thus the Fisher susceptibility/variance is strictly decreasing and strictly convex throughout the convergence chamber. This is a genuine fluctuation-response geometry statement.

## Important geometric correction

A one-dimensional Riemannian metric

\[
ds^2=g(\beta)\,d\beta^2
\]

has identically zero intrinsic Riemann curvature wherever `g>0`: locally one can introduce arc-length coordinate

\[
y(\beta)=\int^\beta \sqrt{g(b)}\,db
\]

and obtain `ds^2=dy^2`.

Therefore `g''=kappa_4>0` must not be described as nonzero intrinsic Fisher/Ruppeiner curvature. It is curvature of the response function as a scalar graph / Hessian response, not intrinsic curvature of the one-dimensional statistical manifold.

This distinction strengthens the program rather than weakening it: a genuinely nontrivial thermodynamic curvature requires at least a two-parameter family. A natural extension is to introduce a fugacity/chemical-potential parameter conjugate to an arithmetic observable (for example prime-factor number `Omega(n)`, `log n`, or a local-prime occupation source) and study the Hessian metric

\[
g_{ij}=\partial_i\partial_j\log Z.
\]

Then mixed third and fourth cumulants become Christoffel/curvature data rather than merely derivatives along a one-dimensional curve.

## Physics -> number theory target

In ordinary thermodynamic information geometry, nonzero scalar curvature diagnoses statistical interactions/correlations. The Euler product is an independent-prime gas in the grand-canonical factorization, so a useful test is whether the two-parameter curvature vanishes in coordinates that fully separate prime occupations and becomes nontrivial only when the arithmetic observable couples primes globally. That can distinguish coordinate artifacts from genuine arithmetic correlation.

## Number theory -> physics target

The exact cumulant hierarchy gives a rare analytically controlled statistical model with all response derivatives encoded by derivatives of `log zeta(beta)`. It can serve as a laboratory for deciding which thermodynamic curvature quantities have invariant physical content, rather than identifying every higher derivative with geometric curvature.

No stronger sign hierarchy is asserted here beyond the signs already proved/formalized.
