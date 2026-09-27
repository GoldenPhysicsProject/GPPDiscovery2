# Regularized prime scattering products and the Schatten strip hierarchy

Date: 2026-09-27
Status: exact convergence estimates for the prime Blaschke phase after removing low repetition harmonics. No RH proof.

## 1. Local free-delay-subtracted prime phase

For a prime p put
\[
a_p=p^{-1/2},
\qquad
L_p=\log p.
\]

Use the contractive-orientation local phase
\[
\widetilde B_p(T)
=
\frac{1-a_pe^{-iTL_p}}
{1-a_pe^{iTL_p}}.
\]

For real T this has unit modulus. Its logarithm is
\[
\log\widetilde B_p(T)
=
2i
\sum_{m\ge1}
\frac{a_p^m}{m}
\sin(mTL_p),
\]
with the branch fixed near a_p=0.

The inverse orientation gives the sign used directly in the oscillatory explicit formula.

## 2. Remove the first k-1 repetition harmonics

For integer k>=2 define the regularized local factor by
\[
\boxed{
\log\widetilde B_{p,\ge k}(T)
=
2i
\sum_{m\ge k}
\frac{a_p^m}{m}
\sin(mTL_p).
}
\]

Equivalently, it is the original local phase multiplied by an exponential counterterm cancelling m=1,...,k-1.

For real T the counterterm is pure phase, so
\[
|\widetilde B_{p,\ge k}(T)|=1.
\]

## 3. Exact normal-convergence strip

Let
\[
T=x+iy.
\]

Since
\[
|\sin(mTL_p)|
\le
e^{m|y|L_p},
\]
the m-th term is bounded by a constant times
\[
p^{-m(1/2-|y|)}.
\]

The worst repetition is m=k. Therefore the prime sum converges absolutely and locally uniformly whenever
\[
k\left(\frac12-|y|\right)>1.
\]

Thus
\[
\boxed{
\prod_p\widetilde B_{p,\ge k}(T)
}
\]
has a normally convergent logarithm in the strip
\[
\boxed{
|\operatorname{Im}T|
<
\frac12-\frac1k.
}
\]

This is exactly the centered-variable version of the Schatten condition
\[
D(s)\in\mathfrak S_k
\iff
k\Re s>1,
\]
because
\[
s=\frac12+iT
\quad\Rightarrow\quad
\Re s=\frac12-\Im T.
\]

## 4. Critical det3 case

For k=3,
\[
\boxed{
|\Im T|<\frac16.
}
\]

Thus the m>=3 prime scattering tail defines a genuine analytic zero-free phase factor in a nontrivial strip around the critical axis.

On the real axis its phase derivative is exactly the m>=3 part of the half-density von-Mangoldt current.

The excluded m=1,2 terms are precisely the two channels already isolated by the det3 identity and by the SU(1,1) coherent-tail theorem.

## 5. Coherent-mode interpretation

The universal SU(1,1) coherent state has compact expansion
\[
\Omega_{a_p}
=
\sqrt{1-a_p^2}
\sum_{m\ge0}a_p^m e_m.
\]

Removing the first k compact modes leaves a local tail of norm
\[
a_p^k.
\]

Hence the same inequality
\[
\sum_p a_p^k<\infty
\]
controls:
- Schatten-k membership of the Euler operator;
- absolute summability of the coherent-state tail;
- normal convergence of the k-regularized prime scattering product on the critical axis.

Off the axis, the factor p^{m|\Im T|} produces exactly the shrunken strip above.

## 6. Important obstruction

A fixed regularization order k does **not** give analytic control all the way to
\[
|\Im T|<\frac12.
\]

As the desired strip approaches the edge, k must increase:
\[
k>\frac1{1/2-|\Im T|}.
\]

Therefore the det3 construction is sufficient for the critical-boundary trace-class problem, but not by itself for a proof that the entire de Branges transfer is inner throughout a half-plane/half-strip.

This explains why the boundary Stieltjes criterion can reduce to two channels while the full analytic-continuation/inner-function problem remains genuinely global.

## 7. Nested completion strategy

The SU(1,1) compact basis provides all repetition modes canonically.

For each k one may split
\[
\mathcal K
=
\operatorname{span}\{e_0,\ldots,e_{k-1}\}
\oplus
\mathcal K_{\ge k}.
\]

The tail is analytically controlled in the strip
\[
|\Im T|<1/2-1/k.
\]

This suggests a nested completion program:
1. use the Archimedean K0 module to renormalize the finite low-mode block;
2. keep the high-mode tail as an ordinary convergent analytic product;
3. increase k to enlarge the controlled strip;
4. prove compatibility of the finite-mode completions under k->k+1.

A projective/inductive limit of these compatible completions would be a route to the full global transfer system.

This is stronger than trying to make det3 alone do the entire analytic-continuation job.

## 8. Caution about scalar regularization

Multiplying each local inner factor by scalar exponential counterterms preserves unit modulus on the real axis, but it need not preserve contractivity off the axis.

Therefore the low-mode subtraction should ultimately be implemented as a conservative matrix/system dilation, not merely as a scalar canonical-product renormalization.

The universal SU(1,1) K0/K1 module supplies a natural finite-dimensional low-mode dilation for each k.
