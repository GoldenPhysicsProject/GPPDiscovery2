# The full von Mangoldt current already lives in Bohr H1 on Re(s)>1/2

Date: 2026-09-28
Status: exact zero-independent Banach-space theorem. No RH claim.

This note differentiates the already-proved Bohr-Hardy identity
\(Z_sM_s=1\) before scalarization.

## 1. Hardy objects

On the compact prime torus
\[
K_{\rm ar}=\prod_p S^1
\]
let \(\chi_n\) be the character indexed by the prime-exponent vector of \(n\).

For
\[
s=\sigma+it,\qquad \sigma>\frac12,
\]
define
\[
Z_s=\sum_{n\ge1}n^{-s}\chi_n,
\qquad
M_s=\sum_{n\ge1}\mu(n)n^{-s}\chi_n.
\]

Both belong to \(H^2(K_{\rm ar})\). Moreover their \(s\)-derivatives
\[
Z_s'=-\sum_{n\ge1}(\log n)n^{-s}\chi_n,
\qquad
M_s'=-\sum_{n\ge1}\mu(n)(\log n)n^{-s}\chi_n
\]
also belong to \(H^2\), because
\[
\sum_n(\log n)^2n^{-2\sigma}<\infty
\]
for every \(\sigma>1/2\).

Hence \(s\mapsto Z_s,M_s\) are \(H^2\)-valued holomorphic maps on the open critical half-plane.

The prior theorem gives
\[
Z_sM_s=1
\qquad\text{in }H^1/L^1(K_{\rm ar})
\]
throughout \(\Re s>1/2\).

## 2. Differentiate before scalarizing

The bilinear product
\[
H^2\times H^2\to H^1
\]
is continuous by Hölder. Therefore the product identity can be differentiated as an \(H^1\)-valued identity:

\[
Z_s'M_s+Z_sM_s'=0.
\]

Define
\[
\boxed{
P_s:=-Z_s'M_s=Z_sM_s'\in H^1(K_{\rm ar}).
}
\]

Now compute its Fourier coefficient at \(n\):
\[
\widehat P_s(n)
=
n^{-s}\sum_{ab=n}(\log a)\mu(b).
\]

Using the exact convolution identity
\[
\mu * \log=\Lambda,
\]
we obtain
\[
\boxed{
P_s
=
\sum_{n\ge1}\Lambda(n)n^{-s}\chi_n
\quad\text{as an }H^1\text{ function/distribution for every }\Re s>\frac12.
}
\]

This is the full von Mangoldt current, internally continued to the open critical half-plane without using zeros and without analytic continuation of the scalar Dirichlet series.

## 3. Why there is no contradiction with the scalar pole/zeros

At the identity point \(1_K=(1,1,\ldots)\), formal evaluation gives
\[
P_s(1_K)=\sum_n\Lambda(n)n^{-s}=-\frac{\zeta'}{\zeta}(s),
\]
but point evaluation at \(1_K\) is not a bounded functional on this Hardy space in the critical strip.

Therefore the theorem does NOT analytically continue the scalar logarithmic derivative through its poles. It shows something sharper:

\[
\boxed{
\text{the arithmetic current is regular internally;}
\quad
\text{the singularity is entirely in scalar reconstruction.}
}
\]

This matches the earlier \(Z_sM_s=1\) theorem but now at the logarithmic-connection/current level.

## 4. A canonical bounded coupling to the self-dual integer heat kernel

For \(t>0\), define the absolutely convergent prime-torus function
\[
K_t(z)
=
\sum_{n\ge1}e^{-\pi t n^2}\chi_n(z).
\]

Because
\[
\sum_ne^{-\pi tn^2}<\infty,
\]
we have \(K_t\in C(K_{\rm ar})\subset L^\infty(K_{\rm ar})\).

Define
\[
\mathcal E_t(f)
=
\int_{K_{\rm ar}}f(z)\overline{K_t(z)}\,dm_{\rm Haar}(z).
\]

Then
\[
|\mathcal E_t(f)|
\le
\|K_t\|_\infty\|f\|_1,
\]
so
\[
\boxed{
\mathcal E_t:H^1(K_{\rm ar})\to\mathbb C
}
\]
is bounded.

Applied to the arithmetic current,
\[
\boxed{
\mathcal E_t(P_s)
=
\sum_{n\ge1}\Lambda(n)n^{-s}e^{-\pi tn^2}.
}
\]

For every fixed \(t>0\) this scalar function is entire in \(s\).

Thus we now have one exact zero-independent map that couples:
- the Euler/prime current on the compact prime torus;
- the integer Fourier spectrum \(n\);
- the circle heat kernel \(e^{-\pi tn^2}\);
- and hence the Poisson/theta self-duality used in the Archimedean completion.

This is precisely the kind of "Euler product + lattice self-duality in one step" demanded by the Beurling/Davenport-Heilbronn controls.

## 5. Important limitation

The kernel \(K_t(z)\) is modular under \(t\mapsto1/t\) only at special additive/lattice characters, in particular at the identity where it reduces to the ordinary theta heat trace. A generic prime-torus point is a completely multiplicative phase, not an additive character of \(\mathbb Z\).

So the bounded heat scalarization does not itself prove the completed modular identity for the von Mangoldt current.

The remaining theorem is now very concrete:

construct the completed \(t\downarrow0\) reconstruction of \(\mathcal E_t(P_s)\), with the Archimedean channel included BEFORE the limit, and prove that the resulting reflected two-point functional is positive.

## 6. Why this is stronger than the previous scalar criterion

Previously the primitive current was known to be the load-bearing scalar distribution and its temperateness was RH-strength.

Now the whole prime-power current is an honest \(H^1(K_{\rm ar})\) object through \(\Re s>1/2\). The failure occurs only after applying an unbounded boundary character.

Thus future no-go arguments based on divergence of
\[
\sum_n\Lambda(n)n^{-s}
\]
must distinguish:
- internal Hardy convergence: already solved;
- scalar identity evaluation: singular;
- heat-regularized reconstruction: bounded;
- completed reflection-positive limit: still open/RH-bearing.
