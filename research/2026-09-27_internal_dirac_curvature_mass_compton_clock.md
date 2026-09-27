# Exact curvature-to-mass-to-Compton-clock bridge from an internal Dirac operator

Date: 2026-09-27
Status: exact spectral-geometric mechanism inside a compact/internal Dirac model. It is not yet identified with the Standard Model or QCD mass operator.

## 1. Massless parent Dirac operator

Take a product geometry
\[
M_4\times X
\]
with compact Riemannian spin manifold \(X\).

Write the higher-dimensional Dirac operator schematically as
\[
\mathcal D
=
\slashed D_4\otimes I
+
\gamma_5\otimes D_X,
\]
where \(D_X\) is the self-adjoint internal Dirac operator.

Let
\[
D_X\eta_n=\kappa_n\eta_n.
\]

For a separated mode
\[
\Psi(x,y)=\psi_n(x)\eta_n(y),
\]
the massless parent equation
\[
\mathcal D\Psi=0
\]
reduces to
\[
\left(
\slashed D_4+\kappa_n\gamma_5
\right)\psi_n=0.
\]

After the usual chiral rotation/convention adjustment, the four-dimensional mass magnitude is
\[
\boxed{
\frac{m_nc}{\hbar}=|\kappa_n|.
}
\]

Equivalently,
\[
\boxed{
m_n=\frac{\hbar}{c}|\kappa_n|.
}
\]

Thus a 4D mass is literally an internal Dirac spectral gap in this model.

## 2. Exact Compton relation

The reduced Compton wavelength is
\[
\bar\lambda_{C,n}
=
\frac{\hbar}{m_nc}.
\]

Using the spectral mass relation,
\[
\boxed{
\bar\lambda_{C,n}
=
\frac1{|\kappa_n|}.
}
\]

So the inverse internal Dirac eigenvalue is exactly the 4D Compton length.

Likewise
\[
\omega_{C,n}
=
\frac{m_nc^2}{\hbar}
=
c|\kappa_n|,
\]
hence
\[
\boxed{
\omega_{Z,n}
=
2c|\kappa_n|.
}
\]

This gives the exact chain
\[
\boxed{
\text{internal spectral inverse length}
\leftrightarrow
m
\leftrightarrow
\bar\lambda_C^{-1}
\leftrightarrow
\omega_C
\leftrightarrow
\omega_Z.
}
\]

## 3. Lichnerowicz curvature bound

For the untwisted internal Dirac operator,
\[
\boxed{
D_X^2
=
\nabla^*\nabla
+
\frac14\,\mathrm{Scal}_X.
}
\]

If
\[
\mathrm{Scal}_X(y)\ge R_{\min}>0
\]
everywhere, then for every eigenspinor
\[
D_X\eta=\kappa\eta,
\]
\[
\kappa^2\|\eta\|^2
=
\|\nabla\eta\|^2
+
\frac14
\int_X
\mathrm{Scal}_X|\eta|^2
\ge
\frac{R_{\min}}4\|\eta\|^2.
\]

Therefore
\[
\boxed{
|\kappa|
\ge
\frac12\sqrt{R_{\min}}.
}
\]

The four-dimensional mass consequently satisfies
\[
\boxed{
m
\ge
\frac{\hbar}{2c}\sqrt{R_{\min}}.
}
\]

And
\[
\boxed{
\bar\lambda_C
\le
\frac{2}{\sqrt{R_{\min}}},
}
\]
while
\[
\boxed{
\omega_C
\ge
\frac c2\sqrt{R_{\min}},
\qquad
\omega_Z
\ge
c\sqrt{R_{\min}}.
}
\]

This is an exact curvature-to-gap-to-clock inequality.

## 4. Why this is stronger than the old heat-kernel mass ansatz

The earlier flavour work used heat suppression of the form
\[
e^{-t\Delta_X}.
\]

The present mechanism says the primitive object should instead be the positive spectral operator
\[
\boxed{
K^\dagger K
=
D_X^2.
}
\]

Its eigenvalues are the mass squares:
\[
\boxed{
\frac{m_n^2c^2}{\hbar^2}
=
\kappa_n^2.
}
\]

The heat operator
\[
e^{-tD_X^2}
\]
then describes propagation/overlap/Yukawa suppression built from those primitive mass eigenvalues.

So:
\[
\boxed{
\text{Dirac spectrum gives mass;}
\qquad
\text{heat kernel gives hierarchy/overlap}.
}
\]

This resolves the earlier ambiguity between a linear Casimir mass law and an exponential Gaussian mass fit.

## 5. Compactness/confinement and discreteness

If \(X\) is compact and \(D_X\) is elliptic with a self-adjoint domain, its spectrum is discrete.

Hence the mechanism naturally produces
\[
\boxed{
\text{compact/constrained internal geometry}
\to
\text{discrete }\kappa_n
\to
\text{discrete 4D masses}.
}
\]

Positive scalar curvature is sufficient to exclude a zero mode by the elementary Lichnerowicz estimate above.

Compactness alone gives discreteness but not necessarily a positive gap; topology can allow harmonic spinors.

Thus:
\[
\boxed{
\text{compactness gives discreteness;}
\quad
\text{coercivity/curvature/boundary conditions give the gap}.
}
\]

## 6. Gauge curvature enters the same squared operator

For a gauge-coupled Dirac operator \(D_A\), the Weitzenbock/Lichnerowicz form is schematically
\[
\boxed{
D_A^2
=
\nabla_A^*\nabla_A
+
\frac14\mathrm{Scal}
+
\frac12 c(F_A),
}
\]
up to sign and normalization conventions for Clifford contraction.

Thus both geometric scalar curvature and gauge curvature enter the same mass-square operator.

Important:
\[
c(F_A)
\]
is not generally positive, so gauge curvature by itself does **not** imply a positive mass gap.

The correct target is a lower bound on the full operator
\[
D_A^2.
\]

## 7. Connection to confinement intuition

A mode confined to a characteristic internal radius \(R\) has
\[
|\kappa_n|\sim\frac{\alpha_n}{R}
\]
for dimensionless spectral number \(\alpha_n\).

Therefore
\[
m_n c^2
\sim
\alpha_n\frac{\hbar c}{R},
\]
and
\[
\bar\lambda_{C,n}
\sim
\frac{R}{\alpha_n}.
\]

So the earlier box intuition
\[
E\sim\frac{\hbar c}{R}
\]
is precisely the dimensional shadow of an internal Dirac eigenvalue.

The coefficient is not universally one; it is the boundary/geometry-dependent eigenvalue \(\alpha_n\).

## 8. Relation to the doubled-null orientation model

The existing doubled-null model gives
\[
m^2c^2=k^2
\]
for a conserved relative momentum.

The internal Dirac mechanism gives
\[
m^2c^2
=
\hbar^2\kappa^2.
\]

This suggests the precise operator identification
\[
\boxed{
k
\longleftrightarrow
\hbar D_X
}
\]
on a physical transverse/orientation sector.

If this identification can be derived from the actual doubled geometry, then the previously abstract relative momentum becomes an internal Dirac momentum and the mass spectrum becomes geometric rather than inserted.

That intertwiner remains to be constructed.

## 9. Research target

The strongest next question is now concrete:

Can the orientation/transverse operator already present in the GPP doubled geometry be identified with a self-adjoint internal Dirac operator \(D_X\) such that:
1. \(D_X^2\) contains the relevant curvature/gauge terms;
2. its positive discrete spectrum matches the physical mass operator;
3. the same geometry fixes the radius/scale rather than inserting it;
4. its heat kernel yields the observed hierarchy and mixing textures?

If yes, the chain
\[
\boxed{
\text{curvature + confinement}
\to
D_X^2
\to
m^2
\to
\bar\lambda_C
\to
\omega_Z
}
\]
would be exact within the completed particle model.
