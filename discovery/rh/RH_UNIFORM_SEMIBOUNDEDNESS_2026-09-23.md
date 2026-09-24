# RH discovery: uniform semiboundedness is enough
## A stability-of-the-Weil-Hamiltonian criterion

**Date:** 2026-09-23  
**Status:** exact criterion and exact CCM/fixed-window bridge. This is not an RH proof. The remaining proof target is a uniform lower bound.

## 1. Fixed-window notation

Let
\[
f_\ell(u)=\ell^{-1/2}\mathbf 1_{[0,\ell]}(u),
\qquad
h_\ell=f_\ell*\widetilde f_\ell
=(1-|u|/\ell)_+.
\]

Let \(\mathcal W\) be the completed additive Weil distribution and define
\[
C_\ell(t)
=
\mathcal W\!\left(h_\ell(\,\cdot-t)\right).
\]

The fixed-window theorem already proved in the project says that for any fixed \(\ell>0\),
RH is equivalent to any eventual uniform upper bound
\[
C_\ell(t)\le M
\qquad (t\gg1).
\]

For \(t>\ell\), the two boxes are disjoint. Put
\[
u_{\ell,t}=f_\ell-T_t f_\ell.
\]
Then
\[
\|u_{\ell,t}\|_2^2=2
\]
and
\[
u_{\ell,t}*\widetilde u_{\ell,t}
=
2h_\ell-h_\ell(\,\cdot-t)-h_\ell(\,\cdot+t).
\]
Since \(C_\ell\) is even,
\[
\boxed{
\mathcal W
\left(
u_{\ell,t}*\widetilde u_{\ell,t}
\right)
=
2\{C_\ell(0)-C_\ell(t)\}.
}
\tag{1}
\]

## 2. Exact two-box stability criterion

Define
\[
E_\ell(t)
=
\frac{
\mathcal W(u_{\ell,t}*\widetilde u_{\ell,t})
}{
\|u_{\ell,t}\|_2^2
}
=
C_\ell(0)-C_\ell(t),
\qquad t>\ell.
\]

### Theorem
For every fixed \(\ell>0\),
\[
\boxed{
\mathrm{RH}
\iff
\inf_{t>\ell}E_\ell(t)>-\infty.
}
\tag{2}
\]

Equivalently,
\[
\boxed{
\mathrm{RH}
\iff
\text{the Weil quadratic form is uniformly semibounded on one two-box orbit.}
}
\]

### Proof

If RH holds, the zero-side expression of the Weil form is nonnegative on convolution squares, so
\[
E_\ell(t)\ge0.
\]

Conversely, suppose
\[
E_\ell(t)\ge-K
\]
for all sufficiently large \(t\). Then by definition
\[
C_\ell(t)
\le
C_\ell(0)+K.
\]
The fixed-window boundedness theorem then excludes every off-axis zero. Hence RH.

No positivity is required. A finite lower floor is enough.

## 3. Global stability criterion

For a support radius \(R\), define the localized lower edge
\[
e(R)
=
\inf
\left\{
\mathcal W(f*\widetilde f):
\|f\|_2=1,\ 
\operatorname{supp}f\subset[-R,R]
\right\}
\]
on any standard compactly supported form core on which the Weil form is defined.

### Corollary
\[
\boxed{
\mathrm{RH}
\iff
\inf_{R>0}e(R)>-\infty.
}
\tag{3}
\]

Under RH one has \(e(R)\ge0\).

For the converse, if \(e(R)\ge-K\) uniformly, translate the two-box vector \(u_{\ell,t}\) without changing its autocorrelation so that it lies in a symmetric support interval. Then
\[
\mathcal W(u_{\ell,t}*\widetilde u_{\ell,t})
\ge
-K\|u_{\ell,t}\|_2^2
=
-2K.
\]
Equation (1) gives
\[
C_\ell(t)\le C_\ell(0)+K,
\]
and RH follows from the fixed-window theorem.

Thus an off-axis zero is equivalent to a spectral instability:
\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
e(R_j)\to-\infty
\quad\text{along some }R_j\to\infty.
}
\tag{4}
\]

This is much weaker than Weil positivity. The required statement is only
**stability from below**.

## 4. Physics interpretation

Equation (3) has the form of the stability condition for a Hamiltonian family.

- RH corresponds to a no-ghost phase in which the completed Weil Hamiltonian is actually positive.
- A hypothetical off-axis zero is a nonunitary dilation mode.
- Translating two separated boxes amplifies that mode exponentially while their \(L^2\) norm remains fixed.
- Therefore an off-axis zero drives the localized vacuum energy to \(-\infty\).

So the correct physical heuristic is not “prove every finite Hamiltonian is positive.” It is:

\[
\boxed{
\text{prove the arithmetic Hamiltonian has a support-independent lower floor.}
}
\]

That alone forces RH.

## 5. Exact bridge to the CCM central matrix entry

Now use the CCM support parameter
\[
L=2\log\lambda
\]
and choose the triangle of the same width,
\[
h_L(u)=(1-|u|/L)_+.
\]

The finite CCM central diagonal entry is
\[
Q_{00}
=
(W_{02})_{00}
-
(W_R)_{00}
-
(W_P)_{00}.
\]

The fixed-window correlation at the origin is
\[
C_L(0)=\mathcal W(h_L).
\]

These are exactly the same number:
\[
\boxed{
Q_{00}=C_L(0).
}
\tag{5}
\]

### Direct verification of the three pieces

The elementary/pole term is
\[
\int_{\mathbb R}
2\cosh(u/2)h_L(u)\,du
=
\frac{32}{L}\sinh^2(L/4)
=
(W_{02})_{00}.
\]

The Archimedean contribution is
\[
-(\log4\pi+\gamma)
-
\int_0^L
\frac{
2e^{u/2}(1-u/L)-2
}{
e^u-e^{-u}
}\,du
+
2\int_L^\infty
\frac{du}{e^u-e^{-u}},
\]
and
\[
\int_L^\infty
\frac{du}{e^u-e^{-u}}
=
\frac12
\log\frac{e^L+1}{e^L-1}.
\]
This is exactly \(-(W_R)_{00}\).

Finally,
\[
-\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\{h_L(\log n)+h_L(-\log n)\}
=
-2
\sum_{n\le e^L}
\frac{\Lambda(n)}{\sqrt n}
\left(1-\frac{\log n}{L}\right),
\]
which is exactly \(-(W_P)_{00}\).

Hence (5) is an identity, with no RH input.

## 6. Finite Weyl moment budget

For the shifted finite CCM matrix
\[
T_N=Q_N-\varepsilon_NI\ge0,
\]
let
\[
m_N(z)=\frac{B_N(z)}{A_N(z)}
\]
be the odd finite Herglotz Weyl function.

If its positive poles are \(\tau_{N,k}\) with masses
\[
\rho_{N,k}
=
-\operatorname{Res}_{z=\tau_{N,k}}m_N(z)>0,
\]
then
\[
m_N(z)
=
2z\sum_k
\frac{\rho_{N,k}}{\tau_{N,k}^2-z^2}.
\]

Therefore
\[
m_N'(0)
=
2\sum_k\frac{\rho_{N,k}}{\tau_{N,k}^2}.
\]

But zero is a Pick interpolation node, so
\[
m_N'(0)=T_{00}=Q_{00}-\varepsilon_N.
\]

Using (5),
\[
\boxed{
2\sum_k\frac{\rho_{N,k}}{\tau_{N,k}^2}
=
C_L(0)-\varepsilon_N.
}
\tag{6}
\]

This exactly identifies the finite inverse-square Weyl mass budget with the
fixed-window arithmetic correlation, up to the lowest-energy shift.

## 7. Why the residue law has exactly the fixed-window weight

Write a critical-line ordinate in dimensionless CCM coordinate as
\[
\tau=\frac{\gamma L}{2\pi}.
\]

The fixed-window transform is
\[
H_L(z)
=
L
\left(
\frac{\sinh(Lz/2)}{Lz/2}
\right)^2.
\]

On the unitary axis,
\[
H_L(i\gamma)
=
\frac{4}{L}
\frac{\sin^2(\gamma L/2)}{\gamma^2}.
\]

The observed CCM residue law is
\[
\rho(\tau)
=
\frac{L}{\pi^2}\sin^2(\pi\tau).
\]

Since
\[
\tau^2
=
\frac{\gamma^2L^2}{4\pi^2},
\]
one gets exactly
\[
\boxed{
\frac{\rho(\tau)}{\tau^2}
=
H_L(i\gamma).
}
\tag{7}
\]

Thus the inverse-square Weyl masses are not merely numerically similar to the
fixed-window zero weights. The two weight formulas are algebraically identical
once the residue quantization law is imposed.

This explains the zero-table saturation of the moment budget.

Equation (7) does **not** prove the residue law; it identifies its precise
arithmetic meaning.

## 8. Finite-section stability target

Let \(\varepsilon_{L,N}\) be the lowest eigenvalue of the unshifted finite CCM
matrix at support \(L\).

If the Fourier/Galerkin spaces are a form core at each fixed \(L\), then their
lowest eigenvalues converge to the localized lower edge \(e(L)\).

Consequently a sufficient finite-dimensional RH closure is
\[
\boxed{
\exists K<\infty
\text{ such that }
\varepsilon_{L,N}\ge-K
\quad
\text{uniformly along a form-core exhaustion in }L,N.
}
\tag{8}
\]

No convergence of the finite ground state to \(\Xi\) is required for this
criterion. No global spectral gap is required. No proof that
\(\varepsilon_{L,N}\to0\) is required.

The only required spectral statement is that the vacuum floor does not run to
\(-\infty\) as the support grows.

## 9. Relation to the failed global compensated-remainder target

The earlier target
\[
C_N-G_N\to0
\]
was too strong because high-energy finite poles carry enormous raw Weyl mass.

The UV-decoupling theorem showed that these poles contribute only an
inverse-square moment plus a local contact term at low energy.

The present stability criterion goes one step further: it shows that even the
full identification of the limiting Weyl measure is unnecessary for RH.

It is enough to prevent an unbounded negative-energy runaway.

This matches the physics:

> a unitary theory need not identify every regulator state before one can prove
> vacuum stability.

## 10. New frontier

The current best target is therefore:

\[
\boxed{
\inf_{L,N}\varepsilon_{L,N}>-\infty
}
\]

in a mathematically correct form-core/exhaustion formulation.

Potential mechanisms already present in the project that should now be
revisited specifically for a **lower bound**, not positivity, are:

1. the exact Eisenstein factorization
   \[
   \mathscr P_x=B_x^*B_x\ge0;
   \]
2. the Möbius/zeta gauge Gram square;
3. the finite Hodge--Koszul no-ghost construction;
4. the rank-two boundary channel;
5. the Nyquist/contact interpretation of the shift;
6. a Maass--Selberg or Schur-complement estimate in which the remaining
   boundary ghost is only bounded, rather than forced to vanish.

A bounded boundary ghost would now be enough.

That is a materially weaker analytic objective than the previous positivity
program and is the next route to attack.
