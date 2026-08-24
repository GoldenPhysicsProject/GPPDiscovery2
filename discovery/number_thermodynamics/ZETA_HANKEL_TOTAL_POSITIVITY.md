# Zeta prime-response Hankel positivity

Status: analytic discovery theorem on the absolutely convergent axis only.

Let \(\sigma>0\) and put
\[
F(\sigma):=-\frac{\zeta'}{\zeta}(1+\sigma).
\]
By the absolutely convergent von Mangoldt Dirichlet series,
\[
F(\sigma)=\sum_{n\ge2}\Lambda(n)n^{-(1+\sigma)}
=\int_{(0,\infty)}e^{-\sigma x}\,d\nu(x),
\]
where
\[
\nu:=\sum_{n\ge2}\frac{\Lambda(n)}{n}\,\delta_{\log n}
\]
is a positive discrete measure.

For every integer \(r\ge0\), termwise differentiation is valid on \(\sigma>0\) and gives
\[
(-1)^rF^{(r)}(\sigma)
=\sum_{n\ge2}\Lambda(n)(\log n)^r n^{-(1+\sigma)}
=\int x^r e^{-\sigma x}\,d\nu(x)>0.
\]
Thus \(F\) is strictly completely monotone on \((0,\infty)\).

Define moments
\[
m_r(\sigma):=(-1)^rF^{(r)}(\sigma)
\]
and for \(N\ge0\) the Hankel matrix
\[
H_N(\sigma):=(m_{i+j}(\sigma))_{0\le i,j\le N}.
\]
For any real vector \(c=(c_0,\ldots,c_N)\),
\[
c^TH_N(\sigma)c
=\int\left(\sum_{j=0}^Nc_jx^j\right)^2e^{-\sigma x}\,d\nu(x)\ge0.
\]
Hence \(H_N(\sigma)\) is positive semidefinite.

In fact it is positive definite. If \(c\ne0\), then the polynomial
\[
P_c(x)=\sum_{j=0}^Nc_jx^j
\]
is nonzero and therefore has only finitely many real roots, whereas the support of \(\nu\) contains the infinite set \(\{\log p:p\text{ prime}\}\). At least one support point has \(P_c(x)\ne0\), and its weight is positive. Therefore
\[
c^TH_N(\sigma)c>0.
\]
Consequently
\[
\boxed{\det H_N(\sigma)>0\qquad(\sigma>0,\ N\ge0).}
\]

The first nontrivial determinant is
\[
F(\sigma)F''(\sigma)-F'(\sigma)^2>0,
\]
a strict log-convexity statement for \(-\zeta'/\zeta(1+\sigma)\). Higher determinants give an infinite hierarchy of inequalities among von-Mangoldt logarithmic moments.

Equivalent prime-power form:
\[
m_r(\sigma)=\sum_p\sum_{k\ge1}k^r(\log p)^{r+1}p^{-k(1+\sigma)}.
\]

This result is independent of the principal-series/Weil route. It supplies a canonical positive Hilbert-space Gram structure on the prime side before any reference to zeros. It does **not** by itself imply Weil positivity or RH; the unresolved global step is still to identify an appropriate completed explicit-formula quadratic form with a positive object on an adequate test class.

Formalization target: first kernel-prove finite Hankel PSD/PD from a positive finite weighted sum, then pass to the absolutely convergent von-Mangoldt series. The existing weighted-variance theorem is exactly the \(2\times2\) shadow of this hierarchy.
