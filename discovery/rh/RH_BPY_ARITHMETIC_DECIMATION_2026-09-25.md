# BPY arithmetic decimation: exact origin of the half-density and prime lengths
## Date: 2026-09-25
## Status: exact zero-independent probability/field identities; new bridge to the causal prime-shift program. No RH claim.

Use the four-field BPY realization
\[
Q=\frac1\pi\sum_{n\ge1}\frac{\Gamma_{2,n}}{n^2},
\]
where the \(\Gamma_{2,n}\) are independent Gamma(shape 2, scale 1) variables. Equivalently
\[
X=\frac12\log Q
\]
is the BPY log-radius before/after the appropriate quarter-density tilt.

## 1. Exact arithmetic decimation

For every integer \(d\ge1\), define the decimated copy
\[
Q^{(d)}:=\frac1\pi\sum_{m\ge1}\frac{\Gamma_{2,dm}}{m^2}.
\]
Since \((\Gamma_{2,dm})_{m\ge1}\) is again an iid Gamma(2,1) sequence,
\[
Q^{(d)}\stackrel d=Q.
\]

The contribution of modes whose index is divisible by \(d\) to the original field is
\[
Q_{\mathrm{div}(d)}
:=\frac1\pi\sum_{d\mid n}\frac{\Gamma_{2,n}}{n^2}
=\frac1{d^2}Q^{(d)}.
\]
Hence
\[
\boxed{Q_{\mathrm{div}(d)}=d^{-2}Q^{(d)}}
\]
as an exact identity on the common product probability space.

For log-radius,
\[
X_{\mathrm{div}(d)}
:=\frac12\log Q_{\mathrm{div}(d)}
=X^{(d)}-\log d.
\]
Thus multiplication by \(d\) in the arithmetic index is exactly translation by \(\log d\) in BPY log-radius.

For \(d=p^k\),
\[
\boxed{\Delta X=-k\log p,}
\]
the same prime-power length appearing in the Weil/von-Mangoldt causal-shift channel.

## 2. Exact half-density from the BPY quarter-density insertion

The centered BPY measure is obtained from the Gaussian field by the quarter-power radial insertion \(Q^{1/4}\). Under arithmetic decimation,
\[
(Q_{\mathrm{div}(d)})^{1/4}
=(d^{-2}Q^{(d)})^{1/4}
=
\boxed{d^{-1/2}(Q^{(d)})^{1/4}.}
\]

Therefore the arithmetic half-density weight \(d^{-1/2}\) is not an externally imposed normalization in this field realization: it is the exact scaling dimension of the BPY quarter-density insertion under mode decimation.

This gives a zero-independent field-theoretic explanation of the ubiquitous Weil factor
\[
\Lambda(d)d^{-1/2}
\]
once the logarithmic generator of prime-power decimation supplies the \(\log p\) factor.

## 3. Prime-power filtration and the von Mangoldt step

Fix a prime \(p\). The sigma-algebras
\[
\mathcal F_{p,k}
=
\sigma(\Gamma_{2,n}:p^k\mid n)
\]
form a decreasing filtration. Their conditional expectations \(E_{p,k}\) are nested orthogonal projections on \(L^2\) of the product Gamma field.

The martingale-difference projections
\[
D_{p,k}=E_{p,k}-E_{p,k+1}
\]
are pairwise orthogonal and positive in quadratic form. The natural logarithmic generator
\[
\mathcal L_p=(\log p)\sum_{k\ge0}D_{p,k}
\]
assigns the same step energy \(\log p=\Lambda(p^k)\) to each successive \(p\)-adic depth.

This is the exact probabilistic counterpart of the prime-power tower
\[
\sum_{k\ge1}(\log p)p^{-k/2}V_{k\log p}.
\]

What remains open is the radial compression theorem: identify the compression of this positive divisibility-filtration generator to the BPY log-radius/two-copy boundary with the prime jump Dirichlet form of the Weil ground-state transform.

## 4. Exact Laplace self-similarity

The BPY radial Laplace transform is
\[
\mathbb E(e^{-tQ})
=
\prod_{n\ge1}\left(1+\frac{t}{\pi n^2}\right)^{-2}
=
\left(\frac{\sqrt{\pi t}}{\sinh\sqrt{\pi t}}\right)^2.
\]

Writing
\[
Q=d^{-2}Q^{(d)}+R_d,
\]
where \(R_d\) contains the modes \(d\nmid n\), the two terms are independent and
\[
\mathbb E(e^{-tR_d})
=
\frac{L_Q(t)}{L_Q(t/d^2)}.
\]

For a prime \(p\), with \(x=\sqrt{\pi t}\),
\[
\boxed{
L_{R_p}(t)
=
p^2\left(\frac{\sinh(x/p)}{\sinh x}\right)^2.
}
\]
This is an exact self-decomposability relation indexed by arithmetic dilation.

## 5. Divisibility field and GCD covariance

The family \(Q^{(d)}\) is an arithmetic random field over the divisibility semigroup. Let
\[
V_Q=\operatorname{Var}(Q)=\frac{2\zeta(4)}{\pi^2}.
\]
For \(d,e\ge1\), writing \(g=(d,e)\),
\[
\operatorname{Cov}(Q^{(d)},Q^{(e)})
=
V_Q\,\frac{g^4}{d^2e^2}.
\]
Therefore
\[
\boxed{
\operatorname{Corr}(Q^{(d)},Q^{(e)})
=
\left(\frac{(d,e)}{\sqrt{de}}\right)^4.
}
\]

Thus the familiar critical GCD kernel
\[
K_{1/2}(d,e)=\frac{(d,e)}{\sqrt{de}}
\]
appears directly: the quadratic BPY radial field carries its fourth power as its normalized covariance.

This links three previously separate objects:
- BPY four-field radial geometry;
- the half-density GCD/Poisson metric;
- the multiplicative prime-decimation semigroup.

## 6. New closure target

Construct the radial/two-copy compression
\[
\mathsf C:
L^2(\text{Gamma product field})
\to
L^2(\nu_*)
\]
so that the positive filtration form
\[
\sum_p(\log p)\sum_k\|D_{p,k}F\|_2^2
\]
compresses to the arithmetic part of the sharp ground-state Poincare form
\[
\sum_{p^k}\frac{\log p}{p^{k/2}}
\int \Phi(x)\Phi(x+k\log p)
\bigl(h(x)-h(x+k\log p)\bigr)^2\,dx.
\]

If this intertwining is exact (or differs by an explicitly positive Archimedean term), the prime contribution has a genuine zero-independent positive parent rather than an assumed scalar positivity.

The nontrivial issue is the scalar compression: \(Q=d^{-2}Q^{(d)}+R_d\) contains the independent complement \(R_d\), so the log-radius is not a pure shift before the connected/two-copy quotient. This is precisely the same boundary scalarization obstruction seen in the causal zeta/Koszul program.

No RH claim is made.
