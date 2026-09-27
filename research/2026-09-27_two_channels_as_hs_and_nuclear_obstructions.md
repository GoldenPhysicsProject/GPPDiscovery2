# Historical two-channel estimate, corrected operator interpretation

**Correction, 2026-09-27:** the column norm estimates below are correct,
but the common-module synthesis operator \(V_2:\ell^2(\mathcal P)\to\mathcal K\)
is already trace class. A summable row expansion proves this. \(V_1\) is
not even bounded on \(\ell^2\), and the remaining \(k=2\) failure is bounded
extension to the all-ones/\(\ell^\infty\) boundary coefficients, not nuclearity
on Hilbert space. The original low-mode completion interpretation in sections
5–8 is superseded by
[the exact domain correction](2026-09-27_coherent_synthesis_domain_correction.md).
The diagonal Euler operator's Schatten/det3 threshold is unchanged.

Date: 2026-09-27
Status: exact norm/ideal estimates for the universal SU(1,1) prime coherent family. No RH proof.

## 1. Prime coherent tails

At the critical Haar boundary let
\[
r_p=p^{-1/2}
\]
and
\[
\Omega_p
=
\sqrt{1-r_p^2}
\sum_{n\ge0}r_p^n e_n.
\]

Let
\[
R_p^{(k)}
=
(I-\Pi_{<k})\Omega_p.
\]

The exact tail theorem gives
\[
\boxed{
\|R_p^{(k)}\|=r_p^k=p^{-k/2}.
}
\]

Consider the synthesis map whose columns are these tail vectors:
\[
V_k:\ell^2(\mathcal P)\to\mathcal K,
\qquad
V_k c=\sum_p c_pR_p^{(k)}.
\]

Whenever the column square norms are summable, V_k is Hilbert--Schmidt.

## 2. Vacuum-only subtraction is not Hilbert--Schmidt

For k=1,
\[
\|R_p^{(1)}\|^2=p^{-1}.
\]

Hence
\[
\sum_p\|R_p^{(1)}\|^2
=
\sum_p\frac1p
=
\infty.
\]

So after removing only the vacuum,
\[
\boxed{
V_1\notin\mathfrak S_2.
}
\]

The primitive m=1 direction is therefore the obstruction to ordinary Hilbert--Schmidt implementability of the critical coherent deformation.

## 3. Removing the primitive mode makes the family Hilbert--Schmidt

For k=2,
\[
\|R_p^{(2)}\|=p^{-1},
\]
so
\[
\sum_p\|R_p^{(2)}\|^2
=
\sum_p p^{-2}
<\infty.
\]

Therefore
\[
\boxed{
V_2\in\mathfrak S_2.
}
\]

But
\[
\sum_p\|R_p^{(2)}\|
=
\sum_p\frac1p
=
\infty.
\]

Thus this particular column expansion is not absolutely summable. Nevertheless
the operator is nuclear by a different, row-wise expansion; column divergence
alone cannot establish failure of nuclearity.

This is the distinct m=2 obstruction.

## 4. Removing the first two excitations makes the tail nuclear by columns

For k=3,
\[
\|R_p^{(3)}\|
=
p^{-3/2},
\]
and
\[
\sum_p\|R_p^{(3)}\|
=
\sum_p p^{-3/2}
<\infty.
\]

Hence the tail admits an absolutely summable rank-one expansion:
\[
\boxed{
V_3
\text{ is nuclear in the column decomposition.}
}
\]

This is the coherent-family counterpart of the critical det3/Fredholm threshold.

## 5. The two channels have different operator meanings

The critical hierarchy is therefore

\[
\boxed{
\begin{array}{ccl}
m=1
&:&
\text{failure of Hilbert--Schmidt implementability},
\\[3pt]
m=2
&:&
\text{trace class on }\ell^2\text{, but divergent all-ones boundary synthesis},
\\[3pt]
m\ge3
&:&
\text{nuclear tail}.
\end{array}
}
\]

This is stronger than saying merely that the first two prime-zeta terms diverge.

They are two different ideal-theoretic defects.

## 6. QFT/TFD interpretation

The same distinction appears in the Gaussian/TFD language.

The first coherent jet changes the one-point/displacement sector.

The second jet changes the covariance/normal-ordering sector.

After both are renormalized, the remaining nonlinear tail is trace controlled.

So the two Archimedean counterterms should be expected to perform two separate jobs:

1. **mean/tangent completion** restoring Hilbert--Schmidt implementability;
2. **covariance/curvature completion** restoring nuclear Fredholm control.

This matches the earlier identification of m=1 and m=2 as the first two cumulants.

## 7. Exact low-mode Gram decomposition

For two coherent parameters r,s,
\[
\langle\Omega_r,\Omega_s\rangle
=
\frac{\sqrt{(1-r^2)(1-s^2)}}{1-rs}.
\]

The compact low-mode part is
\[
\boxed{
K_{<k}(r,s)
=
\sqrt{(1-r^2)(1-s^2)}
\frac{1-(rs)^k}{1-rs},
}
\]
and the tail is
\[
\boxed{
K_{\ge k}(r,s)
=
\sqrt{(1-r^2)(1-s^2)}
\frac{(rs)^k}{1-rs}.
}
\]

Both are positive Gram kernels because they are orthogonal projections of the same coherent-state kernel.

For k=3 the global prime tail is therefore a manifestly positive nuclear Gram object; all nontrivial renormalization is confined to the finite compact block
\[
\operatorname{span}\{e_0,e_1,e_2\}.
\]

After fixing the vacuum normalization, the unresolved physical block is precisely
\[
\operatorname{span}\{e_1,e_2\}.
\]

## 8. Sharpened completion target

The two-channel Archimedean sewing should preserve this ideal ladder.

A successful global construction should:
- cancel/renormalize the e1 tangent defect so the relative Bogoliubov/coherent deformation becomes Hilbert--Schmidt;
- cancel/renormalize the e2 covariance defect so the remaining perturbation becomes nuclear;
- leave the e_{n>=3} tail untouched except for ordinary trace-class propagation.

This supplies a concrete operator-theoretic criterion for judging candidate completions before attempting the full RH positivity theorem.
