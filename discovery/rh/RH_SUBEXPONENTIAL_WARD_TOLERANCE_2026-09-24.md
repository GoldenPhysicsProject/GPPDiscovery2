# RH discovery: subexponential Ward tolerance and the massive co-Poisson identity
## Exact boundary annihilation and a weaker closure theorem

**Date:** 2026-09-24  
**Status:** Sections 1--5 are exact. Section 6 gives a conditional RH closure whose missing input is now only a subexponentially bounded completed Ward/Feshbach defect. This is not an RH proof.

## 1. The RH detector is stable under subexponential perturbations

Fix one triangular window
\[
h_\ell(u)=(1-|u|/\ell)_+,
\qquad
C_\ell(t)=\mathcal W(h_\ell(\,\cdot-t)).
\]

From the fixed-window theorem,
\[
C_\ell(t)=\sum_\rho H_\ell(\lambda_\rho)e^{\lambda_\rho t},
\qquad
\lambda_\rho=\rho-\frac12,
\]
and
\[
\Theta:=\sup_\rho\left|\Re\rho-\frac12\right|
\]
is exactly the least exponential rate of an eventual one-sided upper bound on
\(C_\ell\).

Therefore the following perturbative form is immediate.

### Theorem 1 (subexponential Ward tolerance)
Suppose
\[
C_\ell(t)=M(t)+R(t),
\]
where for every \(\varepsilon>0\)
\[
M(t)\le A_\varepsilon e^{\varepsilon t},
\qquad
|R(t)|\le B_\varepsilon e^{\varepsilon t}
\]
for all sufficiently large \(t\). Then RH holds.

More generally, if the two terms have one-sided growth exponents
\(\alpha_M,\alpha_R\), then
\[
\Theta\le\max\{\alpha_M,\alpha_R\}.
\]

Hence an exact arithmetic Ward identity is stronger than necessary. A positive or
semibounded model may differ from the true completed Weil observable by any
\[
\boxed{e^{o(t)}}
\]
error without changing the RH conclusion.

In particular, **polynomial error is harmless**.

This observation applies equally to the heat-smoothed fixed-window correlation, because
Gaussian convolution multiplies every zero exponent by the nonzero factor
\(e^{\tau\lambda_\rho^2}\) and leaves its real exponential rate unchanged.

## 2. Full co-Poisson identity before imposing the two moment conditions

Let \(f\) be an even Schwartz function on \(\mathbb R\), restricted to
\(\mathbb R_+\). Use the cosine transform
\[
(\mathcal Cf)(y)
=
2\int_0^\infty \cos(2\pi xy)f(x)\,dx
\]
and multiplicative inversion
\[
(\mathcal If)(x)=x^{-1}f(x^{-1}).
\]

Let
\[
(\mathcal Pf)(x)=\sum_{n\ge1}f(nx).
\]

Ordinary Poisson summation gives, without assuming \(f(0)=0\) or
\(\int f=0\),
\[
\boxed{
\mathcal Pf(x)
-
\mathcal I\mathcal P\mathcal C f(x)
=
\frac{\mathcal Cf(0)}{2x}
-
\frac{f(0)}2.
}
\tag{1}
\]

The familiar exact co-Poisson identity on \(\mathscr S_{00}^+\) is simply the
restriction on which the two boundary terms vanish.

Thus the failure of exact shadow intertwining on the full Schwartz space has
**rank two**: it is carried only by the two elementary boundary modes \(1\) and
\(x^{-1}\).

## 3. Half-density logarithmic form

Introduce the unitary half-density logarithmic map
\[
(Uf)(u)=e^{u/2}f(e^u).
\]

Multiplicative inversion becomes reflection:
\[
U\mathcal I U^{-1}=R,
\qquad
(RF)(u)=F(-u).
\]

If
\[
\mathbf P=U\mathcal P U^{-1},
\qquad
\mathbf C=U\mathcal C U^{-1},
\]
then (1) becomes
\[
\boxed{
\mathbf P F
-
R\mathbf P\mathbf C F
=
\frac12\,\mathcal Cf(0)e^{-u/2}
-
\frac12\,f(0)e^{u/2}.
}
\tag{2}
\]

The only obstruction is therefore the two-dimensional span
\[
\operatorname{span}\{e^{-u/2},e^{u/2}\}.
\]

These are exactly the two nonunitary elementary pole channels corresponding to
\(s=0\) and \(s=1\).

## 4. Exact massive co-Poisson Ward identity

Define the positive one-dimensional massive operator
\[
\boxed{
K_0
=
-\frac{d^2}{du^2}+\frac14
=
\left(\frac d{du}+\frac12\right)^*
\left(\frac d{du}+\frac12\right)
\ge\frac14
}
\tag{3}
\]
on \(L^2(\mathbb R,du)\).

Distributionally,
\[
K_0e^{u/2}=0,
\qquad
K_0e^{-u/2}=0.
\]

Applying \(K_0\) to (2) therefore gives the exact identity
\[
\boxed{
K_0\mathbf P
=
K_0R\mathbf P\mathbf C
=
RK_0\mathbf P\mathbf C.
}
\tag{4}
\]

No moment conditions remain.

This is an exact global Ward identity: the positive local Hodge square \(K_0\)
annihilates precisely the two boundary modes which obstruct co-Poisson
intertwining.

Under Fourier/Mellin transform, \(K_0\) has multiplier
\[
t^2+\frac14.
\]

On the principal series \(s=1/2+it\),
\[
s(1-s)=t^2+\frac14.
\]

Thus the same massive Hodge factor is exactly the elementary completion factor
which removes the \(s=0,1\) pole channels of zeta.

This is not a new functional equation; rather, it identifies its elementary
completion as a **positive Hodge/Ward operator**.

## 5. Why this helps but does not by itself prove RH

The operator \(K_0\) is strictly positive on \(L^2(\mathbb R)\), even though its
two formal zero modes \(e^{\pm u/2}\) are non-\(L^2\).

Hence (4) shows that the elementary pole obstruction can be killed without
introducing an indefinite local metric.

However, functional-equation/shadow symmetry alone is known to coexist with
off-critical zeros. The remaining RH content is still the causal/Hardy or
semiboundedness property of the completed prime--Archimedean quotient.

The useful consequence is that a future global Ward/Feshbach construction does
not have to spend analytic effort controlling the two elementary pole channels:
they are annihilated exactly by the positive local operator \(K_0\).

## 6. Approximate completed Ward identity is enough

Let \(Q_L\) denote the exact localized completed Weil quadratic form at support
scale \(L\). Suppose one constructs, from the heat-regularized Hodge--Koszul bulk,
co-Poisson boundary, and Archimedean synthesis, a manifestly semibounded form
\(Q_L^{\rm model}\) satisfying
\[
Q_L^{\rm model}[f]\ge -P(L)\|f\|^2
\]
with \(P(L)=e^{o(L)}\), and suppose the arithmetic identification is only
approximate:
\[
\boxed{
\left|
Q_L[f]-Q_L^{\rm model}[f]
\right|
\le
E(L)\|f\|^2,
\qquad
E(L)=e^{o(L)}.
}
\tag{5}
\]

Then
\[
Q_L[f]\ge-[P(L)+E(L)]\|f\|^2,
\]
so the localized Weil Hamiltonian is subexponentially semibounded.

By the vacuum-instability exponent theorem, this forces
\[
\Theta=0
\]
and hence RH.

### Consequence

The missing nonlocal arithmetic Ward theorem has been weakened from

> exact equality with a positive norm square

to

> equality modulo a subexponentially bounded form error.

A polynomial operator-norm error is sufficient.

This is a materially weaker target and is stable under finite-rank boundary
renormalizations, compact errors, and polynomially growing Feshbach couplings.

## 7. Existing polynomial boundary scale

The exact Archimedean synthesis already obeys
\[
\|\mathcal C_L\|_{\rm HS}^2=O(L),
\]
and after one logarithmic derivative,
\[
\boxed{
\|\mathcal C_L\mathsf L\|_{\rm HS}^2=O(L^3).
}
\tag{6}
\]

Thus any completed Ward/Feshbach defect which factors through a bounded number
of these differentiated boundary channels is automatically polynomial:
\[
\|R_L\|
\le
\operatorname{poly}(L).
\]

The remaining load-bearing problem is now sharply stated:

> **Factor the difference between the true completed Weil form and the
> heat-Hodge/Feshbach model through the explicit co-Poisson boundary channels.**

If the factorization contains only the already-known massive pole modes and
the differentiated Archimedean synthesis channels, equations (3)--(6) give the
required subexponential bound and RH follows.

This is the next target to test algebraically.
