# The Riemann E-map is the critical KMS zeta transfer: exact prime–Archimedean sewing operator

Date: 2026-09-28
Status: exact zero-independent operator identity / synthesis. No RH proof. This identifies the classical Riemann--Connes map \(\mathcal E\) with the same critical half-density semigroup transfer that emerged independently from the Bost--Connes KMS and BPY programmes.

## 1. Classical arithmetic map

For a suitable even Schwartz function \(f\), define
\[
\mathcal E(f)(u)
=
u^{1/2}\sum_{n\ge1}f(nu),
\qquad u>0.
\]

On the codimension-two Poisson domain
\[
f(0)=0,
\qquad
\widehat f(0)=0,
\]
Poisson summation gives the exact reflection identity
\[
\boxed{
\mathcal E(\widehat f)(u)
=
\mathcal E(f)(u^{-1}).
}
\]

Thus additive Fourier duality in the seed space becomes multiplicative inversion in the arithmetic boundary variable.

## 2. Conjugate by the half-density

Set
\[
g(u)=u^{1/2}f(u).
\]

Let
\[
(U_n g)(u)=g(nu)
\]
be multiplicative dilation on \(L^2(\mathbb R_+^*,d^*u)\). Since \(d^*u=du/u\), every \(U_n\) is unitary.

Now
\[
u^{1/2}f(nu)
=
n^{-1/2}(nu)^{1/2}f(nu)
=
n^{-1/2}(U_ng)(u).
\]

Therefore
\[
\boxed{
\mathcal E(f)
=
\sum_{n\ge1}n^{-1/2}U_n g.
}
\]

This is exactly the critical half-density zeta transfer
\[
\boxed{
Z_{\rm crit}
=
\sum_{n\ge1}n^{-1/2}U_n.
}
\]

The series is not an ordinary bounded-operator sum on all of \(L^2\); its rigorous meaning is on the Poisson/codimension-two test domain or through the connected/rigged completions already developed in the project.

## 3. Mellin diagonalization

For the Mellin/Fourier transform
\[
(\mathcal Mg)(t)
=
\int_0^\infty g(u)u^{-it}\,d^*u,
\]
one has
\[
\mathcal M(U_ng)(t)
=
n^{it}\mathcal Mg(t).
\]

Hence formally, and rigorously first in the safe half-plane before boundary continuation,
\[
\boxed{
\mathcal M(Z_{\rm crit}g)(t)
=
\zeta\!\left(\frac12-it\right)\mathcal Mg(t).
}
\]

So the classical arithmetic map that generates Riemann's \(\Xi\) kernel is literally a critical zeta transfer operator in the scaling representation.

This is the same \(n^{-1/2}\) that arose independently from:
- Bost--Connes KMS midpoint matrix coefficients;
- BPY quarter-density decimation;
- Weil's explicit-formula half-density.

## 4. Poisson summation is the global sewing identity

Let \(\mathcal F\) be the additive Fourier transform on the seed \(f\)-space and let
\[
(J\psi)(u)=\psi(u^{-1})
\]
be multiplicative inversion.

Then the Poisson identity is precisely the intertwining relation
\[
\boxed{
Z_{\rm crit}\,\mathcal F
=
J\,Z_{\rm crit}
}
\]
after the half-density conjugation and on the codimension-two physical domain.

This is the exact global relation that local-prime constructions lacked.

It couples in ONE operator:
- additive lattice self-duality;
- Euler multiplicative semigroup;
- the critical KMS half-density;
- the two-sheet reflection \(u\leftrightarrow u^{-1}\).

Thus the "Euler product + lattice self-duality must occur in the same operator" filter is satisfied by \(\mathcal E\) itself.

## 5. The Archimedean seed that produces completed xi

The recent zeta-spectral-triple analysis recalls Riemann's exact choice
\[
h(u)
=
\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2},
\]
equivalently a specific linear combination of the Fourier-invariant Hermite modes \(h_0,h_4\) with vanishing integral.

Riemann's completed kernel is
\[
\boxed{
k=\mathcal E(h),
}
\]
and its Mellin/Fourier transform is the completed \(\Xi\)-function.

Therefore the completed arithmetic vacuum has the exact zero-independent construction

\[
\boxed{
\text{self-dual Archimedean Hermite seed}
\xrightarrow{\,Z_{\rm crit}\,}
\text{Riemann arithmetic boundary vacuum}
\xrightarrow{\mathcal M}
\Xi.
}
\]

The primes are not sewn onto an unrelated gamma factor afterward. The integer semigroup transfer acts directly on an Archimedean Fourier-self-dual seed.

## 6. Relation to the Bost--Connes finite projector system

The project recently proved that the critical Bost--Connes \(ax+b\) midpoint Gram at finite additive level produces the divisibility projectors
\[
K_{n,N}\chi_k=1_{n\mid k}\chi_k,
\]
and
\[
\sum_n\Lambda(n)K_{n,N}
\to
\log|D|.
\]

The new identity shows that the classical \(\mathcal E\)-map is the corresponding infinite geometric transfer before taking the logarithmic derivative:
\[
Z_{\rm crit}
=
\sum_n n^{-1/2}U_n.
\]

Differentiating its multiplicative/Möbius inverse produces the von-Mangoldt connection already obtained in the critical TFD system.

Thus the finite Bost--Connes projector construction and the Riemann \(\mathcal E\)-map are two realizations of the SAME critical semigroup representation:
- finite additive/Pontryagin picture;
- continuous multiplicative/Poisson picture.

## 7. Why the range is the natural vacuum/cohomology sector

In Mellin space, \(Z_{\rm crit}\) inserts the zeta factor. Therefore every vector in the appropriate \(\mathcal E\)-range carries the zeta divisor.

This is the operator reason the range of \(\mathcal E\) lies in the global Weil radical/cohomological sector used by Connes' spectral approach.

The radical is not an accidental collection of test functions: it is the image of the critical KMS zeta transfer acting on the additive self-dual seed space.

## 8. Möbius gauge is the inverse critical transfer

Formally define
\[
M_{\rm crit}
=
\sum_{n\ge1}\mu(n)n^{-1/2}U_n.
\]

In the safe domain,
\[
M_{\rm crit}Z_{\rm crit}=I.
\]

At the critical boundary neither raw scalar series is a bounded operator on the naive Hilbert space. But this is exactly the singular coherent channel already isolated by the Bohr-Hardy/BPY construction:
- the connected Möbius state survives to the half-density boundary;
- only the all-ones/coherent scalar evaluation requires completion.

So the classical Poisson map, the modern KMS transfer, and the project's connected Möbius renormalization fit one operator equation.

## 9. Consequence for constructing the physical Casimir

The candidate arithmetic Casimir should be built from the scaling generator
\[
A=-i\left(u\frac d{du}+\frac12\right)
\]
(or its logarithmic-coordinate conjugate) AFTER imposing the cohomological/OS quotient generated by \(Z_{\rm crit}\).

The finite zeta spectral triples do exactly this in cutoff form: condition a self-adjoint scaling operator by a near-radical vector produced from the \(\mathcal E\)/prolate construction.

The infinite problem is therefore not to invent the sewing map. It is:

\[
\boxed{
\text{construct the Hilbert/OS completion of }
\operatorname{coker/range}(Z_{\rm crit})
\text{ so that the induced scaling Casimir is self-adjoint.}
}
\]

Equivalently, prove that the critical transfer/restriction map has the reflection-positive closed-range/quotient structure required for OS reconstruction.

## 10. Direct new target

Use the Bost--Connes KMS standard form to HILBERTIZE the classical \(\mathcal E\)-map.

Specifically:
1. approximate \(Z_{\rm crit}\) by the finite self-dual \(ax+b\) systems where the KMS midpoint Gram is positive;
2. use Poisson self-duality to identify the reflected adjoint channel exactly;
3. quotient the coherent divergence by the connected Möbius completion;
4. prove the resulting critical transfer is a partial isometry/contraction between the two reflected sheets;
5. take the induced self-adjoint scaling generator on the physical quotient;
6. square and add \(1/4\) to obtain \(C_{\rm phys}\).

This is now a single coherent construction joining Riemann's 1859 kernel, Poisson summation, Bost--Connes KMS, BPY half-density, Weil reflection positivity, and the modern finite zeta spectral triples.
