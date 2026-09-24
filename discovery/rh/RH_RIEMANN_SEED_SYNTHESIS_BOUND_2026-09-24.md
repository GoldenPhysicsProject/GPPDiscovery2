# RH discovery: the Riemann Archimedean synthesis map is uniformly bounded
## A Schur bound for half-density arithmetic translates

**Date:** 2026-09-24  
**Status:** exact Hilbert-space bound for the Archimedean synthesis map already present in the arithmetic principal-series program. Together with the half-density zeta-gauge theorem it gives a subexponential bound for the completed finite synthesis \(CZ\). It does not by itself identify the Weil quadratic form with a positive Schur complement and is not an RH proof.

## 1. The exact Riemann seed

Use the Archimedean seed already derived in the program:
\[
\boxed{
\phi(u)
=
\left(
4\pi^2e^{9u/2}
-
6\pi e^{5u/2}
\right)
e^{-\pi e^{2u}}.
}
\tag{1}
\]

Its arithmetic orbit gives the Riemann kernel:
\[
\Phi(u)
=
\sum_{n\ge1}
n^{-1/2}T_{\log n}\phi(u),
\qquad
(T_af)(u)=f(u+a).
\]

The Fourier transform satisfies
\[
\widehat\phi(z)
=
\pi^{-1/4-iz/2}
\left(iz-\frac12\right)
\Gamma\left(\frac54+\frac{iz}{2}\right),
\]
and
\[
\widehat\phi(z)
\zeta\left(\frac12+iz\right)
=
\Xi(z).
\]

For a finite arithmetic set \(S\subset\mathbb N\), define
\[
\boxed{
Ce_n
=
n^{-1/2}T_{\log n}\phi,
\qquad n\in S.
}
\tag{2}
\]

The goal is to bound \(C:\ell^2(S)\to L^2(\mathbb R)\) independently of the arithmetic cutoff.

## 2. Weighted norms of the seed

For real \(q\), put
\[
N(q)
=
\|e^{qu}\phi(u)\|_{L^2(\mathbb R)}.
\]

With \(x=e^{2u}\), direct integration gives
\[
\begin{aligned}
N(q)^2
={}&
8\pi^4
\frac{\Gamma(q+9/2)}{(2\pi)^{q+9/2}}
\\
&-
24\pi^3
\frac{\Gamma(q+7/2)}{(2\pi)^{q+7/2}}
\\
&+
18\pi^2
\frac{\Gamma(q+5/2)}{(2\pi)^{q+5/2}}.
\end{aligned}
\tag{3}
\]

This is finite exactly when
\[
q>-\frac52.
\]

Therefore both
\[
N(q),\qquad N(-q)
\]
are finite for every
\[
|q|<\frac52.
\]

## 3. Exponential decay of the translation Gram kernel

Define the autocorrelation
\[
K(a)
=
\langle\phi,T_a\phi\rangle.
\]

Fix
\[
0<q<\frac52.
\]

For \(a\ge0\),
\[
\begin{aligned}
K(a)
&=
\int
\phi(u)\phi(u+a)\,du
\\
&=
e^{-qa}
\int
\left[e^{-qu}\phi(u)\right]
\left[e^{q(u+a)}\phi(u+a)\right]du.
\end{aligned}
\]

Cauchy--Schwarz yields
\[
|K(a)|
\le
e^{-qa}N(-q)N(q).
\]

By autocorrelation symmetry the same bound holds for negative \(a\):
\[
\boxed{
|K(a)|
\le
A_qe^{-q|a|},
\qquad
A_q:=N(q)N(-q),
\qquad
0<q<\frac52.
}
\tag{4}
\]

No arithmetic input is used here.

## 4. Uniform Schur bound for the synthesis operator

The Gram matrix of \(C\) is
\[
G_{mn}
=
\langle Ce_m,Ce_n\rangle
=
\frac1{\sqrt{mn}}
K\!\left(\log\frac nm\right).
\]

Using (4),
\[
\boxed{
|G_{mn}|
\le
\frac{A_q}{\sqrt{mn}}
\min\left\{
\left(\frac mn\right)^q,
\left(\frac nm\right)^q
\right\}.
}
\tag{5}
\]

Choose
\[
\boxed{
\frac12<q<\frac52.
}
\]

For \(n\ge m\),
\[
|G_{mn}|
\le
A_qm^{q-1/2}n^{-q-1/2}.
\]

Therefore
\[
\sum_{n\ge m}|G_{mn}|
\le
A_q
\left(
1+\frac1{q-1/2}
\right).
\]

For \(n\le m\),
\[
|G_{mn}|
\le
A_qn^{q-1/2}m^{-q-1/2},
\]
so
\[
\sum_{n\le m}|G_{mn}|
\le
A_q
\left(
1+\frac1{q+1/2}
\right).
\]

Hence every row sum is bounded independently of \(m\) and independently of the finite set \(S\). Since \(G\) is Hermitian, Schur's test gives
\[
\boxed{
\|G\|
\le
A_q
\left[
2+
\frac1{q-1/2}
+
\frac1{q+1/2}
\right].
}
\tag{6}
\]

Because
\[
G=C^*C,
\]
we obtain the cutoff-independent synthesis bound
\[
\boxed{
\|C\|_{\ell^2(S)\to L^2(\mathbb R)}
\le
\left\{
A_q
\left[
2+
\frac1{q-1/2}
+
\frac1{q+1/2}
\right]
\right\}^{1/2}.
}
\tag{7}
\]

This holds for every finite arithmetic set \(S\).

The natural choice \(q=1\) already works.

## 5. Completed finite synthesis is subexponentially bounded

On a divisor-closed set \(S\subset[1,e^L]\), the companion zeta-gauge theorem gives
\[
\|Z\|
\le
\sqrt{
\tau_{\max}(e^L)(1+L)
}
=
e^{o(L)}.
\]

Therefore
\[
\boxed{
\|CZ\|
\le
\|C\|\|Z\|
=
e^{o(L)}.
}
\tag{8}
\]

Likewise, since \(M=Z^{-1}\) obeys the same bound,
\[
\|CM^{-1}\|
=
e^{o(L)}.
\]

This is exactly the finite operator appearing in the previously derived identity
\[
C_{\mathcal P,\mathbf N}
M_{\mathcal P,\mathbf N}(0)^{-1}e_0
=
\sum_{\mathbf m}
n(\mathbf m)^{-1/2}
T_{\log n(\mathbf m)}\phi.
\]

Thus the arithmetic vacuum-to-Archimedean completion map is not exponentially ill-conditioned in its natural finite Hilbert geometry.

## 6. Why this is important

Earlier no-go results showed that raw periodization is not closable in the Gamma Sobolev topology because it samples pointwise Fourier data.

The map \(C\) is qualitatively different.

It includes the fixed Riemann seed \(\phi\), whose translation autocorrelation decays exponentially. This smoothing is strong enough to make the entire half-density arithmetic translation family a Bessel sequence with a cutoff-independent Bessel bound.

So the real-place completion cures precisely the growth mechanism that ruined raw scalar periodization.

The result is:
\[
\boxed{
\text{half-density zeta gauge }Z
\quad+\quad
\text{Riemann seed synthesis }C
\quad\Longrightarrow\quad
\|CZ\|=e^{o(L)}.
}
\]

That is the exact growth scale required by the vacuum-instability criterion for RH.

## 7. What is still missing

This theorem does **not** yet imply a subexponential lower bound for the Weil form.

The old global Schur determinant construction proves that \(C M^{-1}\) generates the correct finite completed Dirichlet response, but that bordered analytic system does not carry the positive metric required to identify its quadratic boundary Schur complement with the localized Weil Hamiltonian.

The remaining bridge is therefore narrower than before:

> construct the completed Hodge--Koszul / zeta-gauge boundary coupling so that the scalar Weil form is its quadratic Schur boundary form.

If that exact quadratic identification is achieved, the norm estimates are now already strong enough:

- positive arithmetic bulk;
- \(\|Z^{\pm1}\|=e^{o(L)}\);
- \(\|L_\Lambda\|=e^{o(L)}\);
- \(\|C\|=O(1)\);
- \(\|CZ\|=e^{o(L)}\);
- Archimedean Weil channel independently bounded below by a constant.

A Schur complement built from these pieces would have a subexponential negative floor, which by the vacuum-instability exponent theorem would imply RH.

## 8. New minimal joint

The hard joint is no longer "control the primes", "control the gamma factor", or "prove convergence of all finite zeros."

It is one algebraic/functional-analytic identity:
\[
\boxed{
Q_W
=
\text{quadratic boundary Schur form of the positive zeta-gauge/Hodge bulk
coupled through }CZ,
}
\]
up to the already-controlled fixed Archimedean renormalization.

If this identity can be established without assuming RH, the current estimates appear sufficient for the stability closure.
