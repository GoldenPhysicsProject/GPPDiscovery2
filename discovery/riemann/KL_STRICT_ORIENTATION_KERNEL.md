# Strict KL orientation from a decreasing Fisher metric

Codex/GPT discovery track, 2026-08-25.

Let `A` be a one-parameter Gibbs potential, let `U=-A'`, and let the Fisher metric be

\[
g=-U'=A''.
\]

For `beta < gamma`, the two Bregman/KL orientations have the triangular integral forms

\[
D(\beta\|\gamma)
=\int_\beta^\gamma (\gamma-x)g(x)\,dx,
\]

\[
D(\gamma\|\beta)
=\int_\beta^\gamma (x-\beta)g(x)\,dx.
\]

Their difference is therefore

\[
\Delta
=\int_\beta^\gamma (\beta+\gamma-2x)g(x)\,dx.
\]

Put

\[
m=\frac{\beta+\gamma}{2},\qquad
L=\frac{\gamma-\beta}{2}>0.
\]

Splitting at `m` and reflecting the left and right halves gives the exact identity

\[
\boxed{
\Delta
=2\int_0^L y\,[g(m-y)-g(m+y)]\,dy.
}
\]

If `g` is continuous and strictly decreasing on `[beta,gamma]`, then for every `0<y<=L`,

\[
g(m-y)>g(m+y),
\]

so the integrand is nonnegative everywhere and strictly positive at every interior positive `y`. Hence

\[
\boxed{D(\beta\|\gamma)>D(\gamma\|\beta).}
\]

For the zeta Gibbs gas on `beta>1`, the Codex Lean line now proves strict decrease of the actual Fisher metric from the absolutely convergent von-Mangoldt representation, with strictness witnessed by the `n=2` mode.  Thus the only remaining formal layer for the exact zeta KL orientation is the triangular Bregman integral representation and the interval-reflection identity above.

This theorem remains entirely on the honest Gibbs half-plane and makes no continuation or RH claim.
