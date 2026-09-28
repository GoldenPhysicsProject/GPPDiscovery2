# Critical BPY connected intertwiner is bounded below: first-Laguerre-chaos coercivity

Date: 2026-09-28
Status: exact zero-independent coercivity theorem for the critical connected BPY decimation synthesis. No RH claim.

This strengthens the 2026-09-27 bounded Bohr-to-BPY intertwiner. The connected map is not merely bounded: at the critical half-density it has a strictly positive lower frame bound. The proof uses only the first orthogonal Gamma/Laguerre chaos and the BPY Mellin identity at safe real arguments.

## 1. BPY Gamma field at the critical quarter-density

Let
\[
\Gamma_r\sim{\rm Gamma}(2,1),\qquad r\ge1,
\]
be independent and define
\[
Q=\frac1\pi\sum_{r\ge1}\frac{\Gamma_r}{r^2}.
\]

For each integer \(n\ge1\), the decimated copy is
\[
Q_n=\frac1\pi\sum_{r\ge1}\frac{\Gamma_{nr}}{r^2}.
\]

At the arithmetic principal-series midpoint \(s=1/2\), put
\[
a=\frac14,
\qquad
V_n:=Q_n^a-\mathbb E Q^a.
\]

These are exactly the critical centered BPY vectors
\[
V_n=\widetilde\Omega_{n,1/2}.
\]

Let
\[
Y_j=\frac{\Gamma_j-2}{\sqrt2}.
\]
Because a Gamma(2,1) variable has mean \(2\) and variance \(2\), the \(Y_j\) form an orthonormal family in the first Laguerre chaos.

## 2. Exact first-chaos projection

Let \(P_1\) denote orthogonal projection onto
\[
\mathcal H_1=\overline{\operatorname{span}}\{Y_j:j\ge1\}.
\]

By decimation covariance,
\[
\boxed{
P_1V_n=\sum_{r\ge1}b_rY_{nr},
}
\]
where
\[
b_r=\mathbb E[Q^aY_r]
=\frac1{\sqrt2}\operatorname{Cov}(Q^a,\Gamma_r).
\]

All \(b_r\) are strictly positive.

To compute them, write
\[
c_r=\frac1{\pi r^2},
\qquad
L_Q(t)=\mathbb E e^{-tQ}
=
\left(\frac{\sqrt{\pi t}}{\sinh\sqrt{\pi t}}\right)^2.
\]

For \(0<a<1\),
\[
q^a=\frac{a}{\Gamma(1-a)}
\int_0^\infty(1-e^{-tq})t^{-a-1}\,dt.
\]

Using the Gamma(2,1) Laplace identities
\[
\mathbb E e^{-u\Gamma}=(1+u)^{-2},
\qquad
\mathbb E[\Gamma e^{-u\Gamma}]=2(1+u)^{-3},
\]
one obtains
\[
\operatorname{Cov}(e^{-tQ},\Gamma_r)
=
-\frac{2c_rt}{1+c_rt}L_Q(t).
\]

Therefore
\[
\boxed{
b_r
=
\frac{\sqrt2\,a\,c_r}{\Gamma(1-a)}
\int_0^\infty
\frac{L_Q(t)t^{-a}}{1+c_rt}\,dt.
}
\]

In particular \(b_r>0\).

## 3. A rigorous \(\ell^1\) diagonal-dominance estimate

Define
\[
I(c)=
\int_0^\infty
\frac{L_Q(t)t^{-a}}{1+ct}\,dt.
\]

Then
\[
\frac{b_r}{b_1}
=
\frac1{r^2}\frac{I(c_r)}{I(c_1)}
\le
\frac1{r^2}\frac{I(0)}{I(c_1)},
\]
because \(I(c)\le I(0)\).

Normalize
\[
d\nu(t)=\frac{L_Q(t)t^{-a}}{I(0)}\,dt.
\]
Since \(x\mapsto(1+c_1x)^{-1}\) is convex,
\[
\frac{I(c_1)}{I(0)}
=
\mathbb E_\nu\frac1{1+c_1T}
\ge
\frac1{1+c_1\mathbb E_\nu T}.
\]

Now
\[
\mathbb E_\nu T
=
(1-a)\frac{\mathbb E Q^{a-2}}{\mathbb E Q^{a-1}}.
\]

At \(a=1/4\), the BPY identity
\[
\mathbb E Q^{s/2}=2\xi(s)
\]
and the functional equation give
\[
\mathbb E_\nu T
=
\frac34\frac{\xi(9/2)}{\xi(5/2)}.
\]

Using the explicit completed-zeta factors,
\[
\frac{\xi(9/2)}{\xi(5/2)}
=
\frac{21}{4\pi}
\frac{\zeta(9/2)}{\zeta(5/2)}
<
\frac{21}{4\pi}.
\]

Since \(c_1=1/\pi\),
\[
\boxed{
\frac{I(0)}{I(c_1)}
<
1+\frac{63}{16\pi^2}.
}
\]

Consequently
\[
\sum_{r\ge2}\frac{b_r}{b_1}
<
\left(\frac{\pi^2}{6}-1\right)
\left(1+\frac{63}{16\pi^2}\right).
\]

The right side is strictly less than \(1\). Indeed, with \(x=\pi^2\), this is equivalent to
\[
16x^2-129x-378<0,
\]
which follows from the elementary bounds \(9<x<10\): the polynomial is increasing on \([9,10]\) and its value at \(10\) is \(-68\).

Therefore
\[
\boxed{
\sum_{r\ge2}b_r<b_1.
}
\]

This is the key coercive inequality.

## 4. Dirichlet-convolution operator is invertible

Identify the first chaos with \(\ell^2(\mathbb N)\) by \(Y_j\leftrightarrow e_j\).

The first-chaos synthesis operator is
\[
B=\sum_{r\ge1}b_rS_r,
\qquad
S_re_n=e_{rn}.
\]

Equivalently,
\[
(Bc)_j=\sum_{n\mid j}c_n b_{j/n},
\]
so \(B\) is Dirichlet convolution by the positive sequence \(b\).

Since every \(S_r\) is an isometry,
\[
\|B-b_1I\|
\le
\sum_{r\ge2}b_r
<
b_1.
\]

Hence \(B\) is boundedly invertible by a Neumann series and
\[
\boxed{
\|Bc\|_2
\ge
\delta\,\|c\|_2,
\qquad
\delta:=b_1-\sum_{r\ge2}b_r>0.
}
\]

## 5. Coercivity of the FULL connected BPY synthesis

For a finite coefficient vector \(c\),
\[
\sum_n c_nV_n
\]
has first-chaos projection \(Bc\). Orthogonal projection can only decrease norm, so
\[
\left\|\sum_n c_nV_n\right\|_2
\ge
\|Bc\|_2
\ge
\delta\|c\|_2.
\]

Therefore the critical connected synthesis
\[
C_{1/2}:\ell^2(\mathbb N)\simeq H^2(K_{\rm ar})
\longrightarrow
L^2(\text{BPY field}),
\qquad
C_{1/2}e_n=V_n,
\]
satisfies the operator inequality
\[
\boxed{
C_{1/2}^*C_{1/2}\ge\delta^2I.
}
\]

Combined with the previously proved upper Schur bound, \(C_{1/2}\) is a topological embedding with closed range and bounded inverse on its range.

## 6. Meaning for the RH reconstruction problem

This removes a possible hidden failure mode.

The connected prime-torus data are NOT being crushed when mapped into the BPY Gaussian field at the critical half-density. The map is stably injective.

Thus the current architecture is sharper:

- internal zeta/Mobius state: healthy in \(H^2\) for \(\Re s>1/2\);
- full von Mangoldt connection: healthy in \(H^1\) for \(\Re s>1/2\);
- connected prime-to-BPY map: bounded AND bounded below at the critical midpoint;
- remaining singularity: the one coherent/all-ones scalar reconstruction channel.

In particular, an RH closure can no longer fail because the connected BPY representation loses arithmetic information. The only place left for a ghost is the completed scalar/reflection channel.

## 7. What this does NOT prove

A bounded-below connected intertwiner does not make the all-ones evaluation bounded; equivalent Hilbert norms cannot repair that singular functional.

It also does not prove the Weil reflection form is positive.

The next target is therefore genuinely rank-one/non-normal:

construct the completed KMS/TFD/Archimedean scalar channel so that it couples to this coercive connected sector without factoring through the raw evaluation \(E_0\).
