# RH Higgs Goldstone quotient — exact uniform chiral mass after removing the pole mode
## Date: 2026-09-24
## Status: exact one-dimensional spectral theorem; no RH claim

The co-Poisson/pole completion contains the two elementary modes
\[
e^{x/2},\qquad e^{-x/2},
\]
annihilated by
\[
K_0=-\partial_x^2+\frac14.
\]

The Higgs interpretation suggests treating these as Goldstone/vacuum modes rather than as part of the physical fluctuation spectrum. This note proves that after removing either mode, the corresponding first-order chiral factor has a cutoff-uniform spectral gap.

## 1. Positive chiral factor

Let
\[
D_-=\partial_x-\frac12
\]
on \(L^2(0,L)\) with quadratic form domain \(H^1(0,L)\).

Its kernel is
\[
\ker D_-=\operatorname{span}\{e^{x/2}\}.
\]

The quadratic form is
\[
q_-[f]=\|D_-f\|_2^2.
\]

The associated self-adjoint operator is
\[
D_-^*D_-=-\partial_x^2+\frac14
\]
with the natural Robin boundary conditions
\[
f'(0)-\frac12f(0)=0,
\qquad
f'(L)-\frac12f(L)=0.
\]

The zero eigenfunction is \(e^{x/2}\).

For every nonzero integer mode \(n\ge1\), put
\[
k_n=\frac{n\pi}{L}.
\]
The remaining eigenfunctions have the form
\[
f_n(x)
=
\cos(k_nx)+\frac{1}{2k_n}\sin(k_nx),
\]
and the eigenvalues are
\[
\lambda_n
=
\frac14+k_n^2
=
\frac14+\frac{n^2\pi^2}{L^2}.
\]

Hence the exact first positive eigenvalue is
\[
\boxed{
\lambda_1
=
\frac14+\frac{\pi^2}{L^2}.
}
\]

Consequently, for every \(f\in H^1(0,L)\) satisfying
\[
\langle f,e^{x/2}\rangle=0,
\]
one has the sharp coercivity estimate
\[
\boxed{
\|(\partial_x-\tfrac12)f\|_2^2
\ge
\left(\frac14+\frac{\pi^2}{L^2}\right)\|f\|_2^2.
}
\]

In particular
\[
\boxed{
\|f\|_2
\le
2\|(\partial_x-\tfrac12)f\|_2
}
\]
uniformly in \(L\).

## 2. Negative chiral factor

Likewise
\[
D_+=\partial_x+\frac12
\]
has
\[
\ker D_+=\operatorname{span}\{e^{-x/2}\}.
\]

Its natural self-adjoint square is again
\[
D_+^*D_+=-\partial_x^2+\frac14
\]
with Robin conditions
\[
f'(0)+\frac12f(0)=0,
\qquad
f'(L)+\frac12f(L)=0.
\]

After removing \(e^{-x/2}\), the same positive spectrum remains:
\[
\boxed{
\lambda_n=\frac14+\frac{n^2\pi^2}{L^2},
\qquad n\ge1.
}
\]

Thus
\[
\boxed{
\|f\|_2
\le
2\|(\partial_x+\tfrac12)f\|_2
}
\]
for \(f\perp e^{-x/2}\), uniformly in \(L\).

## 3. Weighted-Poincaré form

For \(D_-\), write
\[
f(x)=e^{x/2}g(x).
\]
Then
\[
D_-f=e^{x/2}g',
\]
and
\[
f\perp e^{x/2}
\iff
\int_0^L e^x g(x)\,dx=0.
\]

The preceding theorem is exactly the weighted Poincaré inequality
\[
\boxed{
\int_0^L e^x|g|^2dx
\le
\frac{1}{1/4+\pi^2/L^2}
\int_0^Le^x|g'|^2dx.
}
\]

The limiting Poincaré constant is \(4\), independent of the interval length.

The \(D_+\) statement is the reflected weighted inequality with weight \(e^{-x}\).

## 4. Higgs interpretation

The apparently exponentially large pole inverse
\[
A=(\partial_x-\tfrac12)^{-1}
\]
is badly conditioned only because it approaches the exact vacuum mode \(e^{x/2}\).

After quotienting that one Goldstone direction, its inverse norm is uniformly bounded:
\[
\boxed{
\|(D_-|_{\ker(D_-)^\perp})^{-1}\|
\le2.
}
\]

The same is true for the shadow mode \(e^{-x/2}\).

Therefore the co-Poisson completion has exactly two elementary massless/vacuum directions, and **all orthogonal fluctuations carry mass at least \(1/2\)**.

This is the literal one-dimensional Higgs mechanism for the pole sector:
\[
\text{vacuum mode removed}
\quad\Longrightarrow\quad
m_{\rm Higgs}^2\ge\frac14.
\]

## 5. Combination with the prime Hodge result

The prime Koszul system already has the much larger many-channel Green suppression
\[
\|D_{\rm prime}^{-1}\|
=
O(\sqrt L\,e^{-L/2}).
\]

Independently, the exact Hodge decomposition of the prime logarithmic current gives
\[
P_L
=
P_L^{\rm coherent}+P_L^{\rm conn},
\qquad
\|P_L^{\rm conn}\|=O(L^2).
\]

The present theorem shows that the elementary pole/co-Poisson sector has no hidden exponential inverse after its two exact vacuum modes are removed.

Thus a completed self-adjoint Feshbach realization would have:
- a massively gapped prime bulk;
- a uniformly gapped pole/shadow bulk after the two Goldstone modes are quotiented;
- an already-polynomial connected prime current;
- a uniformly semibounded Archimedean bath.

The only remaining possible exponential obstruction is the **exact way the coherent prime mode is glued to the two completion/Goldstone boundary modes**.

This is narrower than the previous generic completion problem.

## 6. Exact next theorem

Construct the completed boundary relation so that:
1. the two co-Poisson modes \(e^{\pm x/2}\) are the only null directions of the completion sector;
2. the coherent Hodge-exact prime current is absorbed into those boundary/gauge directions;
3. the resulting physical quotient is self-adjoint;
4. its graded heat trace equals the exact arithmetic completed heat trace.

By the signed self-adjoint heat criterion, positivity of the final graded measure is not required. Self-adjointness and exact spectral identification are sufficient for RH.
