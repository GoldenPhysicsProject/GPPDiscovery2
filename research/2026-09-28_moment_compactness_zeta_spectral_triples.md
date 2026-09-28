# Moment-compactness closure: finite self-adjoint zeta triples need only local BPY trace-moment convergence

Date: 2026-09-28
Status: exact analytic reduction / new synthesis with the 2025-26 Connes--Consani--Moscovici zeta spectral triples. No RH proof. The purpose is to replace difficult zero-by-zero spectral convergence by convergence of positive inverse-Casimir moments near the origin.

## 1. Finite self-adjoint triples already give finite principal-series Casimirs

The recent zeta-spectral-triple construction starts, for each cutoff pair \(j=(\lambda,N)\), from a self-adjoint first-order operator
\[
D_j=D_{\log}^{(\lambda,N)}
\]
built zero-independently from the finite Weil form / finite Euler data. Its regularized determinant is proportional to the Fourier transform of the lowest Weil-form eigenvector, and that entire function has only real zeros.

Pass to the positive spectral subspace of \(D_j\) and define
\[
\boxed{
C_j=\frac14+D_{j,+}^{\,2},
\qquad
A_j=(C_j-\tfrac14)^{-1}=D_{j,+}^{-2}.
}
\]

Then automatically
\[
C_j\ge\frac14,
\qquad
A_j\ge0.
\]

Thus every finite zeta spectral triple already supplies a bona fide finite/cutoff principal-series Casimir.

Because the spectrum of a first-order operator on a compact interval has linear growth, \(D_{j,+}^{-2}\) is trace class.

## 2. The normalized finite determinant is a positive Fredholm determinant

Let the positive eigenvalues of \(D_j\) be \(\lambda_{j,k}>0\), repeated with multiplicity. The even entire function obtained by Wick-rotating the real-zero determinant has the canonical product
\[
F_j(z)
=
\prod_k\left(1+\frac{z^2}{\lambda_{j,k}^2}\right).
\]

Equivalently,
\[
\boxed{
F_j(z)=\det(I+z^2A_j).
}
\]

There is no nonconstant exponential factor: the Fourier transform is an even entire function of order one, so its Hadamard exponential factor has degree at most one, while evenness removes the linear term; normalization \(F_j(0)=1\) removes the constant.

Every zero of every \(F_j\) lies on the imaginary \(z\)-axis because \(A_j\ge0\).

## 3. The target moments are known locally from xi, without zero input

Let
\[
F(z)
=
\frac{\xi(\frac12+z)}{\xi(\frac12)},
\qquad
\log F(z)
=
\sum_{m\ge1}
\frac{\kappa_{2m}}{(2m)!}z^{2m}.
\]

If \(F=\det(I+z^2A)\), then comparison of the logarithmic Fredholm expansion gives the required trace powers
\[
\boxed{
t_m
:=
\operatorname{Tr}A^m
=
\frac{(-1)^{m+1}\kappa_{2m}}
{2(2m-1)!}.
}
\]

In particular
\[
R=t_1=\frac{\kappa_2}{2}>0.
\]

These numbers are computable directly from derivatives of \(\xi\) at the center. No zeta zeros are used.

After normalization
\[
\rho=A/R,
\]
the desired Renyi trace powers are
\[
\boxed{
\operatorname{Tr}\rho^m=t_m/R^m.
}
\]

These are exactly the BPY density-matrix targets previously derived in the project.

## 4. Moment-to-entire convergence theorem

Let \(A_j\ge0\) be trace-class operators and put
\[
F_j(z)=\det(I+z^2A_j).
\]

Assume

\[
\boxed{
\operatorname{Tr}A_j^m\longrightarrow t_m
\quad\text{for every }m\ge1,
}
\]
where \(t_m\) are the centered-xi values above.

The \(m=1\) convergence implies
\[
\sup_j\operatorname{Tr}A_j<\infty.
\]

Hence, for every \(z\in\mathbb C\),
\[
|F_j(z)|
\le
\exp\!\left(|z|^2\operatorname{Tr}A_j\right),
\]
so \((F_j)\) is a locally bounded normal family of entire functions.

Moreover, on a fixed sufficiently small disk,
\[
\log F_j(z)
=
\sum_{m\ge1}
\frac{(-1)^{m+1}}m
z^{2m}\operatorname{Tr}A_j^m,
\]
and the uniform trace bound dominates this series geometrically. Therefore
\[
\log F_j(z)\to
\sum_{m\ge1}
\frac{(-1)^{m+1}}m t_m z^{2m}
=
\log F(z)
\]
locally uniformly near \(z=0\).

Every subsequential entire limit of \(F_j\) therefore agrees with \(F\) on a neighborhood of the origin, hence everywhere by the identity theorem. Consequently the full sequence satisfies

\[
\boxed{
F_j\longrightarrow
\frac{\xi(\frac12+z)}{\xi(\frac12)}
\quad\text{locally uniformly on }\mathbb C.
}
\]

Since every \(F_j\) has all zeros on the imaginary axis, Hurwitz then forces every zero of \(F\) onto the imaginary axis.

Therefore:

\[
\boxed{
\text{BPY trace-moment convergence of the finite positive inverse Casimirs implies RH.}
}
\]

## 5. This is strictly weaker-looking than zero-by-zero spectral convergence

The usual finite-spectral-triple programme asks to prove convergence of individual eigenvalues of \(D_j\) to all Riemann ordinates.

The theorem above says that this is unnecessary.

It is enough to prove the local origin data
\[
\operatorname{Tr}D_{j,+}^{-2m}
\to
\frac{(-1)^{m+1}\kappa_{2m}}
{2(2m-1)!}
\]
for every fixed \(m\).

That is an inverse-spectrum / low-energy moment problem, precisely the regime in which:
- BPY gives exact cumulants;
- the prime/KMS system gives positive finite approximants;
- Green-operator / Schur-complement estimates are natural;
- Hodge bulk gaps control inverse powers.

This replaces a global zero-tracking problem by a hierarchy of positive Green-trace limits.

## 6. Size-biased Hausdorff reformulation

If \(a_{j,k}\) are the eigenvalues of \(A_j\), define the finite positive measure
\[
\sigma_j
=
\sum_k a_{j,k}\,\delta_{a_{j,k}}.
\]

Then
\[
\int x^n\,d\sigma_j(x)
=
\operatorname{Tr}A_j^{n+1}.
\]

Because
\[
0\le a_{j,k}\le \operatorname{Tr}A_j,
\]
a uniform trace bound places all \(\sigma_j\) in one compact interval.

Thus the entire convergence problem becomes convergence of ONE family of positive Hausdorff measures whose moments are the BPY cumulants.

The determinant is recovered from this size-biased measure by
\[
\log F_j(z)
=
\int
\frac{\log(1+z^2x)}{x}
\,d\sigma_j(x),
\]
with the integrand continuously filled at \(x=0\) by \(z^2\).

This is exactly the size-biased spectral law already discovered in the BPY density-matrix formulation.

## 7. Practical consequence for the current GPP operator construction

For any proposed positive finite-cutoff Casimir
\[
C_X=\frac14+A_X^{-1},
\qquad
A_X=B_XL_X^{-1}B_X^*\ge0,
\]
do NOT first compare its eigenvalues to Riemann zeros.

Compute instead
\[
\operatorname{Tr}A_X,\quad
\operatorname{Tr}A_X^2,\quad
\operatorname{Tr}A_X^3,\ldots
\]
and compare them with the exact BPY targets \(t_m\).

This is cheaper, zero-independent, and directly tied to the determinant convergence theorem above.

It also gives a brutal falsifier: a candidate can reproduce several apparent zeros while having the wrong inverse-spectrum moments, in which case it cannot converge to the xi Casimir.

## 8. New convergence target for the CCM finite spectral triples

Applied to the Connes--Consani--Moscovici finite self-adjoint triples, the open convergence problem can be sharpened to:

\[
\boxed{
\forall m\ge1,\qquad
\operatorname{Tr}
\left(D_{\log,+}^{(\lambda,N)}\right)^{-2m}
\longrightarrow
\frac{(-1)^{m+1}\kappa_{2m}}
{2(2m-1)!}.
}
\]

If this is established along one cofinal cutoff regime with the first traces uniformly bounded, compact-uniform determinant convergence and RH follow automatically.

This is a concrete interface between their finite self-adjoint approximation and the GPP BPY/Green-operator programme.

## 9. Caution about free-spectrum normalization

The finite scaling triple carries a background lattice spectrum. Depending on the precise regularized determinant convention, one may need the RELATIVE inverse-Casimir measure obtained after cancelling the free scaling determinant.

In that case the same theorem applies to the positive physical factor only if the relative determinant can be written as \(\det(I+z^2A_j)\) with \(A_j\ge0\). This positivity must be checked rather than assumed.

The GPP Casimir construction is designed precisely to produce the already-quotiented positive \(A_X=B_XL_X^{-1}B_X^*\), avoiding an uncontrolled difference of two positive spectral measures.
