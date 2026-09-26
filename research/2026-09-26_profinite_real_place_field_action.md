# Concrete real-place field on the compact profinite vacuum cell

Date: 2026-09-26
Status: mathematically well-defined toy model built from existing finite-place data. The identification with the physical universe is unproved.

## 1. Internal Hilbert space

Use the compact finite-adelic vacuum cell

\[
\widehat{\mathbf Z}=\prod_p\mathbf Z_p
\]

with normalized additive Haar measure \(\mu_f\), and define

\[
\mathcal H_f=L^2(\widehat{\mathbf Z},d\mu_f).
\]

For \(X\in\widehat{\mathbf Z}\), let

\[
N_p(X)=v_p(X).
\]

Each \(N_p\) is a nonnegative multiplication operator.  Under Haar measure,

\[
\Pr(N_p=a)=(1-p^{-1})p^{-a},
\qquad
\mathbb E N_p=\frac1{p-1}.
\]

The \(N_p\) are independent.

## 2. Additive internal mass-square operator

The finite-place Casimir mass is

\[
\mu_p^2=\frac4{p-1}.
\]

For independent local internal channels, the natural quadratic-field quantity to add is
mass squared rather than mass.  Define

\[
\boxed{
\mathsf M_f^2(X)
=
4M_*^2
\sum_p\frac{N_p(X)}{p-1}.
}
\]

Its Haar expectation is

\[
\int_{\widehat{\mathbf Z}}
\frac{\mathsf M_f^2(X)}{M_*^2}\,d\mu_f(X)
=
4\sum_p\frac1{(p-1)^2}
=
C_2
\approx5.500260.
\]

Since the expectation is finite and the integrand is nonnegative,

\[
\boxed{
\mathsf M_f^2(X)<\infty
\quad\text{for Haar-almost every }X.
}
\]

Therefore \(\mathsf M_f^2\) is a well-defined positive self-adjoint multiplication
operator on its natural dense domain in \(\mathcal H_f\).

This gives a concrete operator-theoretic meaning to the second arithmetic moment
\(C_2\): it is the Haar expectation of the additive finite-place mass-square operator.

## 3. A 4D generally covariant field

Let \(\Psi(x,X)\) be a real scalar on ordinary spacetime \(M_4\) with internal coordinate
\(X\in\widehat{\mathbf Z}\).  Consider

\[
\boxed{
S[\Psi,g]
=
-\frac12
\int_{M_4}d^4x\sqrt{-g}
\int_{\widehat{\mathbf Z}}d\mu_f(X)
\left[
g^{\mu\nu}\partial_\mu\Psi\,\partial_\nu\Psi
+
\mathsf M_f^2(X)\Psi^2
\right].
}
\]

This action is local in ordinary spacetime and nontrivial only in the compact profinite
internal coordinate through the mass operator.

Variation with respect to \(g_{\mu\nu}\) gives an ordinary 4D stress tensor

\[
T_{\mu\nu}^{(f)}
=
\int_{\widehat{\mathbf Z}}d\mu_f(X)
\left[
\partial_\mu\Psi\partial_\nu\Psi
-\frac12g_{\mu\nu}
\bigl((\partial\Psi)^2+\mathsf M_f^2\Psi^2\bigr)
\right].
\]

Hence this finite-place sector gravitates automatically once the real-place action is
accepted.

No Standard Model gauge coupling has been inserted.  Gauge neutrality is therefore a
property of this toy action by construction, not yet a derived theorem.

## 4. Constant internal profile and the arithmetic coefficient

For an internal profile independent of \(X\),

\[
\Psi(x,X)=\psi(x),
\]

the mass term reduces exactly to

\[
\frac12
C_2M_*^2\psi(x)^2.
\]

Thus

\[
\boxed{
m_{\rm eff}^2
=
C_2M_*^2
}
\]

for the constant profinite profile in the quadratic form sense.

This is the cleanest current route by which the arithmetic constant
\(C_2\approx5.500260\) can enter a physical stress tensor without arbitrarily declaring
energy to be proportional to a mass-square moment.

Caution: the constant internal vector is not an eigenvector of the multiplication
operator \(\mathsf M_f^2\).  The equality above is an expectation/quadratic-form identity,
not a one-particle mass eigenvalue.

## 5. Pushforward mass spectrum

The map

\[
X\mapsto\mathsf M_f^2(X)
\]

pushes Haar measure forward to a positive probability measure on \([0,\infty)\).
Its Laplace transform is the exact Euler product

\[
\boxed{
\int e^{-t\mathsf M_f^2/M_*^2}\,d\mu_f
=
\prod_p
\frac{1-p^{-1}}
{1-p^{-1}e^{-4t/(p-1)}}.
}
\]

Thus the 4D field can equivalently be viewed as a generalized free field with an
arithmetic positive mass spectral measure.

This is a much cleaner statement than assigning one ordinary particle to every prime.

## 6. Cosmological dust limit

Decompose the pushforward spectral measure into ordinary 4D massive modes.  Every
component whose physical frequency satisfies \(m\gg H\) has the standard coherently
oscillating scalar limit

\[
\langle P\rangle\simeq0,
\qquad
\langle\rho\rangle\propto a^{-3}.
\]

Therefore this explicit profinite field has a mathematically available CDM regime.

What is not fixed by the action alone is the cosmological state: the spectral amplitudes
of the modes must be derived from initial conditions or from an adelic vacuum/production
mechanism.  Without that state, the model does not predict the dark-matter abundance.

## 7. Why this model is useful even if it fails

It turns the phrase "the finite places gravitate" into a precise testable mathematical
object:

\[
\boxed{
L^2(\widehat{\mathbf Z})
\quad+\quad
\mathsf M_f^2
=
4M_*^2\sum_p\frac{v_p}{p-1}.
}
\]

The remaining questions are no longer semantic:

1. Does the global adelic/celestial theory actually induce this quadratic operator?
2. What is the preferred internal state/profile?
3. Is the induced 4D spectral state cold by matter-radiation equality?
4. Does its perturbation transfer function satisfy CMB and structure constraints?
5. Does nonlinear gravitational clustering produce realistic halos?
6. Does the finite-place sector couple only through the metric after the full gauge theory
   is included?

If the answer to (1) is no, this dark-sector route dies cleanly.  If yes, the rest is
ordinary cosmological field theory with a highly nonordinary number-theoretic spectral
measure.
