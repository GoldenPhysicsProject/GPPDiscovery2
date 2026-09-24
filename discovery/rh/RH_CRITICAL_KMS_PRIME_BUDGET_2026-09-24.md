# RH discovery: critical-KMS prime fluctuation budget
## A polynomial dual norm and the remaining connected-completion problem

**Date:** 2026-09-24  
**Status:** Sections 1--4 are exact consequences of the already-verified Bost--Connes/KMS prime ladder plus elementary summation. Sections 5--7 isolate a sufficient completion theorem and the precise obstruction. This is discovery-layer work, not an RH proof.

## 1. Critical KMS metric on one prime-power ladder

In the Bost--Connes arithmetic flow,
\[
[H,\mu_{p^k}]
=
(k\log p)\mu_{p^k}.
\]

For inverse temperature \(\beta\), the verified Duhamel norm of the \(p^k\) ladder direction is
\[
d_{\beta}(p^k)
=
\frac{p^{-k\beta/2}}
{\kappa_\beta(k\log p)},
\qquad
\kappa_\beta(\omega)
=
\frac{\beta\omega/2}
{\sinh(\beta\omega/2)}.
\]

At the critical temperature \(\beta=1\),
\[
d(p^k)
=
p^{-k/2}
\frac{\sinh(k\log p/2)}
{k\log p/2}.
\]

Since
\[
\sinh(k\log p/2)
=
\frac12\left(p^{k/2}-p^{-k/2}\right),
\]
this simplifies exactly to
\[
\boxed{
d(p^k)
=
\frac{1-p^{-k}}
{k\log p}
=
\frac{1-p^{-k}}{\log(p^k)}.
}
\tag{1}
\]

Thus the critical KMS metric assigns a strictly positive norm to each primitive prime-power frequency and makes distinct \((p,k)\) directions orthogonal.

## 2. Weil prime coefficient in the same basis

The completed Weil prime side uses
\[
c(p^k)
=
\Lambda(p^k)p^{-k/2}
=
(\log p)p^{-k/2}.
\]

Regard \(c\) as a linear functional on the orthogonal KMS tangent space whose basis vector \(\mu_{p^k}\) has squared norm \(d(p^k)\).

Its dual squared norm, truncated at logarithmic length \(L\),
\[
k\log p\le L,
\]
is therefore
\[
\|c\|_{*,L}^2
=
\sum_{p^k\le e^L}
\frac{|c(p^k)|^2}{d(p^k)}.
\]

Using (1),
\[
\frac{|c(p^k)|^2}{d(p^k)}
=
\frac{(\log p)^2p^{-k}}
{(1-p^{-k})/(k\log p)}
=
\boxed{
\frac{k(\log p)^3}{p^k-1}.
}
\]

Hence
\[
\boxed{
\|c\|_{*,L}^2
=
\sum_{p^k\le e^L}
\frac{k(\log p)^3}{p^k-1}.
}
\tag{2}
\]

This is exact.

## 3. Elementary polynomial bound

For \(n=p^k\ge2\),
\[
p^k-1\ge \frac12p^k.
\]
Also
\[
k\log p=\log n,
\qquad
\log p\le\log n.
\]
Therefore
\[
\frac{k(\log p)^3}{p^k-1}
\le
2\frac{(\log n)^3}{n}.
\]

Discarding the restriction to prime powers and summing over every integer,
\[
\|c\|_{*,L}^2
\le
2\sum_{2\le n\le e^L}
\frac{(\log n)^3}{n}.
\]

By the integral test,
\[
\sum_{2\le n\le X}\frac{(\log n)^3}{n}
\le
C+\int_1^X\frac{(\log x)^3}{x}\,dx
=
C+\frac14(\log X)^4.
\]

Thus
\[
\boxed{
\|c\|_{*,L}^2
=
O(L^4),
\qquad
\|c\|_{*,L}
=
O(L^2).
}
\tag{3}
\]

No prime number theorem or zero information is needed for this estimate.

A sharper \(O(L^3)\) bound follows from standard Chebyshev control of
\(\sum_{p\le X}\log p\), but the elementary \(O(L^4)\) estimate is already
subexponential and therefore sufficient for the new vacuum-stability strategy
if the scalar completion map can be controlled.

## 4. Why this matters after the vacuum-instability theorem

The previous discovery established that RH follows from any subexponential
lower bound on the localized completed Weil Hamiltonian:
\[
e(R)\ge-\exp(o(R)).
\]

Equivalently, in the CCM support variable \(L\), any polynomial lower bound for
the lowest unshifted finite/localized energy is enough.

Equation (3) therefore says that the **arithmetic prime fluctuation vector itself
has only polynomial size in the natural critical KMS dual metric**.

This is a major weakening compared with the raw scalar prime operator, whose
coefficient sum
\[
\sum_{p^k\le e^L}\Lambda(p^k)p^{-k/2}
\]
is exponentially large in \(L\).

The KMS geometry has converted the dangerous coherent size into a polynomial
fluctuation budget.

## 5. The exact obstruction: raw scalarization destroys the KMS gain

The prime piece of the scalar Weil form is schematically
\[
\mathcal P_L(f)
=
2\Re
\sum_{p^k\le e^L}
c(p^k)
\langle f,T_{k\log p}f\rangle.
\]

If one naïvely applies Cauchy--Schwarz in the KMS tangent metric, one obtains
\[
|\mathcal P_L(f)|
\le
2\|c\|_{*,L}
\left(
\sum_{p^k\le e^L}
d(p^k)
|\langle f,T_{k\log p}f\rangle|^2
\right)^{1/2}.
\]

The first factor is polynomial by (3), but the second need not be.
The scalar correlation samples live on an exponentially dense multiplicative
set. A generic scalar \(L^2\) vector can have many large translation
correlations, and the sum above can grow exponentially.

This is not a technical nuisance. It explains why a generic bounded trace from
the prime-Fock/KMS parent to the one-dimensional scalar orbit cannot exist.

The polynomial KMS budget becomes useful only **after the coherent mean has
been removed or cancelled by the pole--Archimedean channel**.

This is the same topology wall already seen in the critical Bohr/GNS
construction: the arithmetic parent is well behaved in its natural product
Hilbert geometry, while restriction to the one-dimensional Kronecker orbit is
singular unless the real-place completion supplies extra regularity.

## 6. Connected-completion criterion

The new RH criterion suggests the following target, which is strictly weaker
than the earlier contractive Hardy trace or exact positive norm-square
programs.

Let \(\mathcal H_L^{\rm KMS}\) be the truncated critical KMS tangent space with
orthogonal prime-power basis and metric (1). Let
\[
v_L
=
\sum_{p^k\le e^L}
\frac{c(p^k)}{d(p^k)}\,\mu_{p^k},
\]
so that
\[
\|v_L\|_{\rm KMS}^2
=
\|c\|_{*,L}^2
=
O(L^4).
\]

### Sufficient completion theorem

Suppose one can construct, independently of the zeta zeros,

1. a nonnegative bulk form \(\mathcal E_L(f)\ge0\);
2. a **connected** prime--Archimedean fluctuation map
   \[
   J_L:\mathcal D_L\to\mathcal H_L^{\rm KMS};
   \]
3. a real-place/boundary remainder \(\mathcal B_L(f)\);

such that the completed localized Weil form satisfies
\[
\boxed{
\mathcal W_L(f*\widetilde f)
=
\mathcal E_L(f)
-
2\Re\langle J_Lf,v_L\rangle_{\rm KMS}
+
\mathcal B_L(f),
}
\tag{4}
\]
and, for normalized \(f\),
\[
\|J_Lf\|_{\rm KMS}
\le
e^{o(L)},
\qquad
\mathcal B_L(f)\ge-e^{o(L)}.
\]

Then, by Cauchy--Schwarz and (3),
\[
\mathcal W_L(f*\widetilde f)
\ge
-\,O(L^2)e^{o(L)}
-e^{o(L)}
=
-\exp(o(L)).
\]

The vacuum-instability theorem then gives RH.

Thus the missing map need not be isometric, contractive, or positivity
preserving. It only needs **subexponential connected form control**.

## 7. Physics interpretation

This is the natural thermal-field-theory picture.

The raw prime sum is analogous to an unrenormalized coherent field amplitude.
Its norm is exponentially large because it includes the classical mean.

The critical KMS/Duhamel metric instead measures fluctuations. In that metric
the von Mangoldt field has only polynomial susceptibility:
\[
\chi_L^{\rm prime}
=
\|c\|_{*,L}^2
=
O(L^4).
\]

The pole and Archimedean terms should therefore be viewed as the completion
that subtracts the coherent background and supplies the real-place
counterterm.

What RH needs is not zero fluctuation and not positivity of every local
component. It needs thermodynamic stability:
\[
E_{\rm vac}(L)\ge-\exp(o(L)).
\]

A completed connected response representation of the form (4) would provide
exactly that.

## 8. Revised research frontier

The high-value question is now:

\[
\boxed{
\text{Can the completed pole--Archimedean channel be identified as the
coherent subtraction that turns scalar prime response into the KMS
fluctuation field?}
}
\]

Concrete next tests:

1. Compute the one-point/coherent component of the critical BC/KMS prime field
   and compare it with the rank-two pole term.
2. Add the explicit real-place Gamma/Digamma boundary distribution and test
   whether the **connected** response reproduces the full CCM Hermite source.
3. Search for an exact Schur-complement identity in which the positive KMS
   covariance is the bulk block and the pole--Archimedean channel is the
   boundary block.
4. Prove only a polynomial/subexponential norm bound for the resulting Schur
   boundary map. The previous demand for exact positivity is unnecessary.

The critical gain is quantitative:
\[
\boxed{
\text{prime fluctuation budget }=O(L^4),
}
\]
while the new RH closure requires only
\[
\boxed{
\text{completed vacuum floor }=-\exp(o(L)).
}
\]

The remaining problem is therefore a **connected-completion theorem**, not a
raw prime estimate.
