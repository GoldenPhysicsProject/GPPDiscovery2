# RH discovery: exact Weyl moment budget and ultraviolet decoupling
## 2026-09-23

Status: Sections 1--4 are exact finite consequences of the two-channel Weyl system. Section 5 is a numerical audit against the supplied zero tables. Sections 6--8 give the revised closure strategy. This is discovery-layer work, not an RH proof.

## 1. Finite symmetric Weyl representation

Work in the open eta channel. Normalize the radical vector by
\[
\eta^T\xi=1,\qquad \beta^T\xi=0,
\]
with
\[
T=Q-\varepsilon I\ge0,\qquad T\xi=0.
\]

Let the diagonal nodes be symmetric,
\[
d_{-j}=-d_j,
\]
with eta even, beta odd, and xi even. Define
\[
A(z)=\eta^T(D-zI)^{-1}\xi,
\qquad
B(z)=\beta^T(D-zI)^{-1}\xi,
\qquad
m(z)=\frac{B(z)}{A(z)}.
\]

Then
\[
A(-z)=-A(z),\qquad B(-z)=B(z),
\]
so
\[
\boxed{m(-z)=-m(z).}
\]

The corrected finite operator is self-adjoint, hence m is a rational Herglotz function. Its nonzero poles occur in pairs
\[
\pm\tau_k
\]
with positive Herglotz masses
\[
\rho_k=-\operatorname{Res}_{z=\tau_k}m(z)>0.
\]

Because
\[
A(z)=-\frac1z+O(z^{-2}),
\qquad
B(z)=O(z^{-2}),
\]
we have
\[
m(z)=O(z^{-1})
\]
at infinity, so there is no affine Herglotz term at finite N.

Therefore the exact partial-fraction representation is
\[
\boxed{
m(z)
=
\sum_{\tau_k>0}
\rho_k
\left(
\frac1{\tau_k-z}
+
\frac1{-\tau_k-z}
\right)
=
2z\sum_{\tau_k>0}
\frac{\rho_k}{\tau_k^2-z^2}.
}
\]

## 2. Exact inverse-square Weyl mass sum rule

Differentiate at the origin:
\[
m'(0)
=
2\sum_{\tau_k>0}
\frac{\rho_k}{\tau_k^2}.
\]

But zero is an interpolation node, and the finite Pick/Hermite identity gives
\[
m'(0)=T_{00}=Q_{00}-\varepsilon_N.
\]

Hence
\[
\boxed{
Q_{00}-\varepsilon_N
=
2\sum_{\tau_k>0}
\frac{\rho_k}{\tau_k^2}.
}
\tag{1}
\]

This is an exact finite sum rule.

It is the correct spectral-mass budget for compact Weyl-function convergence. Raw mass
\[
\sum\rho_k
\]
is not the relevant quantity.

## 3. Exact ultraviolet tail bound

Fix a compact disk
\[
|z|\le r
\]
and a spectral cutoff
\[
R>r.
\]

Define the positive UV inverse-square mass
\[
M_N(R)
=
2\sum_{\tau_k>R}
\frac{\rho_k}{\tau_k^2}.
\]

The contribution of poles above R is
\[
m_N^{>R}(z)
=
2z\sum_{\tau_k>R}
\frac{\rho_k}{\tau_k^2-z^2}.
\]

Therefore
\[
\boxed{
|m_N^{>R}(z)|
\le
\frac{|z|}{1-r^2/R^2}\,
M_N(R),
\qquad |z|\le r.
}
\tag{2}
\]

Thus enormous raw Weyl mass at high energy is harmless if its inverse-square weighted mass escapes.

This directly addresses the numerical observation that approximately 99 percent of the raw finite Weyl mass may lie beyond the resolved zeta window.

## 4. Stronger EFT/renormalization statement

The high-energy tail has a universal local linear part. Subtract it:
\[
m_N^{>R}(z)-zM_N(R)
=
2z^3\sum_{\tau_k>R}
\frac{\rho_k}{\tau_k^2(\tau_k^2-z^2)}.
\]

Hence
\[
\boxed{
\left|
m_N^{>R}(z)-zM_N(R)
\right|
\le
\frac{|z|^3}{R^2-r^2}\,
M_N(R),
\qquad |z|\le r.
}
\tag{3}
\]

So even if the inverse-square UV mass does not vanish, its only surviving low-energy effect is a linear contact term.

This is precisely the spectral analogue of integrating out UV states in a Kallen--Lehmann / effective-field-theory propagator: high-energy regulator states can carry huge total spectral weight while affecting low-energy observables only through local counterterms.

The finite Hermite construction already singles out exactly such a local derivative counterterm through the Nyquist mode
\[
h(s)=\frac{\sin(2\pi s)}{2\pi},
\qquad h(n)=0,\quad h'(n)=1.
\]

This gives a physical interpretation of the finite shift and of the failure of the old global compensated remainder: the wrong target tried to cancel the full UV spectrum rather than quotienting out its local contact contribution.

## 5. Connection with the observed residue law

In the dimensionless CCM spectral coordinate
\[
t=\frac{\gamma L}{2\pi},
\]
the observed resolved-zero residue law is
\[
\boxed{
\rho(t)
=
\frac{L}{\pi^2}\sin^2(\pi t).
}
\tag{4}
\]

A true zeta ordinate gamma would therefore contribute to the exact moment budget (1)
\[
2\frac{\rho(t)}{t^2}
=
\boxed{
\frac8L
\frac{\sin^2(\gamma L/2)}{\gamma^2}.
}
\tag{5}
\]

Hence define the real-zero partial moment
\[
S_L(T)
=
\frac8L
\sum_{0<\gamma\le T}
\frac{\sin^2(\gamma L/2)}{\gamma^2}.
\tag{6}
\]

Using the supplied high-precision first-100001 table and the supplied approximately two-million-zero table, the following values were obtained:

### lambda = 3
\[
L=2\log3,
\qquad
Q_{00}=0.04085519868271666.
\]

First 100001 zeros:
\[
S_L=0.04081361585116510,
\]
which is about 99.8982 percent of \(Q_{00}\).

Approximately two million zeros:
\[
S_L=0.04085175294642236,
\]
which is about 99.991566 percent of \(Q_{00}\).

Remaining budget:
\[
3.4457362943\times10^{-6}.
\]

### lambda = 3.6
\[
Q_{00}=0.04476277275923194.
\]

First 100001 zeros:
\[
S_L=0.04472831352542504
\]
(about 99.9230 percent).

Approximately two million zeros:
\[
S_L=0.04475989783302972
\]
(about 99.993577 percent).

Remaining budget:
\[
2.8749262022\times10^{-6}.
\]

### lambda = 4.2
\[
Q_{00}=0.03930418776873591.
\]

First 100001 zeros:
\[
S_L=0.03927343823817888
\]
(about 99.9218 percent).

Approximately two million zeros:
\[
S_L=0.03930162164727548
\]
(about 99.993471 percent).

Remaining budget:
\[
2.5661214604\times10^{-6}.
\]

The expected high-zero tail from the Riemann--von Mangoldt density and the average
\[
\sin^2\sim\frac12
\]
is
\[
\boxed{
S_L(\infty)-S_L(T)
\sim
\frac{2}{\pi L}
\frac{\log(T/2\pi)+1}{T}.
}
\tag{7}
\]

At the top of the large zero table,
\[
T\approx1.13249\times10^6,
\]
this estimate reproduces the observed remaining budget at the few-percent level for lambda=3 and essentially to the displayed digits for lambda=3.6 and 4.2.

This is strong numerical evidence that the relevant Nevanlinna mass is already being saturated by the resolved real zeta spectrum, even though the raw finite Weyl mass is dominated by high-energy spurious poles.

It is evidence, not a proof of RH.

## 6. Revised interpretation of the spurious finite poles

The finite poles beyond the resolution window should be treated as UV regulator states.

Their raw mass can grow without obstructing local convergence.

The correct quantity is
\[
2\sum\frac{\rho_k}{\tau_k^2},
\]
and the exact sum rule says that this quantity is bounded by a single arithmetic diagonal entry:
\[
Q_{00}-\varepsilon_N.
\]

Equation (3) shows more: after matching the local slope, the nonlocal effect of all poles above R is suppressed by
\[
O(R^{-2})
\]
times the bounded inverse-square mass.

Thus the old proposed global convergence
\[
C_N-G_N\to0
\]
was too strong.

The corrected target is a **windowed, renormalized** statement.

## 7. Revised closure target

For every fixed physical/spectral window \(|z|\le r\):

1. Separate the finite Weyl measure into resolved IR poles and an unresolved UV tail.
2. Prove that the resolved poles converge to the arithmetic/zeta poles in the window and that their residues obey the quantized law.
3. Replace the UV tail by its exact linear contact coefficient
   \[
   zM_N(R).
   \]
4. Use (3) to send \(R\to\infty\) after the finite-model limit.

The target is therefore
\[
\boxed{
m_N(z)
=
m_N^{\mathrm{resolved}}(z)
+
b_N z
+
o_K(1)
}
\]
on every compact K in the upper half-plane, where \(b_N\) is the escaped inverse-square UV mass/contact term.

This is a standard spectral-renormalization pattern and is much more compatible with the numerical data than global pole cancellation.

## 8. What remains load-bearing

The exact UV theorem removes the raw-spurious-mass objection, but RH still requires an arithmetic identification step.

One needs a zero-independent proof that, in every fixed window, the resolved part of the finite Weyl measure converges to the completed-zeta boundary data.

Equivalently, one needs a local spectral-measure convergence theorem, not a global remainder theorem.

A promising route is to combine:

- the exact finite Pick interpolation;
- the explicit entire arithmetic Hermite source;
- the Poisson--prolate near-radical;
- the fixed-window explicit formula;
- the transfer-disk inequality;
- and the UV decoupling estimate above.

The physics heuristic is now sharp:

> the CCM finite model behaves like a regulated quantum propagator.  
> Real zeta zeros are the stable infrared spectral states; unresolved finite poles are ultraviolet regulator states; the Nyquist derivative channel is the local counterterm.  
> RH closure should be formulated as convergence of the renormalized IR spectral measure, not convergence of total raw spectral mass.

