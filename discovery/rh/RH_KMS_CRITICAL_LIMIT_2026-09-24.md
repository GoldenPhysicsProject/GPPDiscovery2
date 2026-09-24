# RH discovery: tame critical-temperature limit in the prime KMS geometry
## The finite-place sector is polynomially stable as beta -> 1

**Date:** 2026-09-24  
**Status:** exact finite-place estimate. It does not solve the singular scalar pullback or the real-place gluing problem and therefore is not an RH proof.

## 1. Critical and off-critical midpoint weights

For a prime power \(n=p^k\), the Bost--Connes midpoint normalization at inverse
temperature \(\beta\) gives
\[
c_\beta(n)
=
\Lambda(n)n^{-\beta/2}.
\]

At the critical point,
\[
c_1(n)
=
\Lambda(n)n^{-1/2}.
\]

Write
\[
\delta=\beta-1\ge0.
\]
Then
\[
c_\beta(n)
=
c_1(n)e^{-\delta\log n/2}.
\]

The critical KMS dual metric from the companion discovery note has
\[
d_1(p^k)
=
\frac{1-p^{-k}}{k\log p}.
\]

For a logarithmic cutoff
\[
\log n\le L,
\]
define
\[
\|a\|_{*,L}^2
=
\sum_{p^k\le e^L}
\frac{|a(p^k)|^2}{d_1(p^k)}.
\]

## 2. Exact critical-limit estimate

For \(x\ge0\),
\[
0\le1-e^{-x}\le x.
\]
Hence
\[
|c_1(n)-c_\beta(n)|
\le
\frac{\delta}{2}
(\log n)c_1(n).
\]

Therefore
\[
\|c_1-c_\beta\|_{*,L}^2
\le
\frac{\delta^2}{4}
\sum_{p^k\le e^L}
(\log p^k)^2
\frac{|c_1(p^k)|^2}{d_1(p^k)}.
\]

Using
\[
\frac{|c_1(p^k)|^2}{d_1(p^k)}
=
\frac{k(\log p)^3}{p^k-1},
\]
and the crude estimates
\[
p^k-1\ge\frac12p^k,
\qquad
k\log p=\log(p^k),
\qquad
\log p\le\log(p^k),
\]
gives
\[
(\log p^k)^2
\frac{|c_1(p^k)|^2}{d_1(p^k)}
\le
2\frac{(\log n)^5}{n}.
\]

Discarding the prime-power restriction,
\[
\|c_1-c_\beta\|_{*,L}^2
\le
\frac{\delta^2}{2}
\sum_{2\le n\le e^L}
\frac{(\log n)^5}{n}.
\]

The integral test yields
\[
\sum_{n\le e^L}\frac{(\log n)^5}{n}
\le
C+\frac16L^6.
\]

Thus
\[
\boxed{
\|c_1-c_\beta\|_{*,L}
=
O\!\left(
|\beta-1|\,L^3
\right).
}
\tag{1}
\]

This uses no zero information and no prime number theorem.

## 3. Consequence

The critical-temperature limit of the **finite-place midpoint field** is tame in
its natural KMS geometry.

For any diagonal exhaustion \(\beta_L\downarrow1\) satisfying
\[
(\beta_L-1)L^3\to0,
\]
one has
\[
\boxed{
\|c_{\beta_L}-c_1\|_{*,L}\to0.
}
\tag{2}
\]

For example, every algebraic choice
\[
\beta_L-1=L^{-A},
\qquad A>3,
\]
works.

There is no need for an exponentially fine approach to the critical
temperature in the KMS fluctuation metric.

## 4. Where the genuine singularity remains

This estimate does **not** imply the corresponding scalar Weil prime form
converges with the same rate.

The scalar restriction to the arithmetic Kronecker orbit can align an
exponentially large number of prime-power directions. That pullback is not a
bounded map on the raw KMS Hilbert space.

Therefore the obstruction is not the finite-place thermal limit itself. It is
the **completed trace/pullback to the scalar boundary**, together with the
trivial/pole and Archimedean channels.

This sharpens the earlier thermodynamic statement:

- finite-place KMS ladder: polynomially stable at \(\beta=1\);
- metaplectic real-place ladder: explicit and exponentially decaying in its
  tower index;
- unique growing geometric term: the anti-midpoint trivial/pole direction;
- unresolved operation: completed prime--Archimedean scalarization.

The project should therefore stop treating the entire
\[
\beta\to1^+
\]
limit as uniformly mysterious. In the natural product geometry, the prime
fluctuation vector itself is under quantitative control.

## 5. Sufficient completed-trace criterion

Let
\[
\mathcal T_L
\]
denote the still-to-be-constructed **connected completed trace** from the
prime--Archimedean KMS parent to the localized scalar Weil form.

Because the prime critical-limit error is \(O(\delta L^3)\) in the parent
metric, it is enough for RH if one proves a trace estimate of the form
\[
\boxed{
\|\mathcal T_L\|
\le
e^{o(L)}
}
\tag{3}
\]
on the connected subspace after the trivial coherent channel is removed.

Indeed choose \(\delta_L\) so that
\[
\delta_LL^3\,\|\mathcal T_L\|\to0
\]
while \(\delta_L\downarrow0\).
If the \(\beta>1\) parent is semibounded uniformly modulo a
subexponential boundary term, the critical scalar form inherits a
subexponential lower floor.

By the vacuum-instability theorem already established in the discovery
program, that lower floor implies RH.

Equation (3) is dramatically weaker than the old demand that the trace be
contractive or isometric.

## 6. Physics reading

The finite-place sector behaves as an ordinary thermodynamic fluctuation field:
its susceptibility remains polynomial and its critical-temperature
renormalization is tame.

The violent behavior appears only when all prime channels are forced into one
coherent scalar phase.

That is exactly what one expects from an infrared observable obtained by
restricting a many-channel thermal field to a singular coherent trajectory.

The real-place and pole terms must therefore be understood as the
renormalization of this scalarization, not as unrelated corrections.

The new quantitative target is:
\[
\boxed{
\text{completed connected scalarization has subexponential norm}.
}
\]

If that can be proved, the prime critical limit is already strong enough to
finish the stability argument.
