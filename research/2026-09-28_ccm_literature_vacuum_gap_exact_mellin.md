# Literature-assisted direct closure: CCM missing step equals the GPP vacuum-gap criterion

Date: 2026-09-28
Status: literature audit plus new exact finite formula and zero-free numerical evidence. No RH claim.

## 1. What the current public literature actually leaves open

Connes--Consani--Moscovici, *Zeta Spectral Triples* (arXiv:2511.22755), gives:

- a finite self-adjoint operator \(D_{\log}^{(\lambda,N)}\) whenever the smallest finite Weil eigenvalue is simple and its eigenvector is even;
- a regularized determinant whose entire factor is the Fourier transform of that finite ground eigenvector;
- all zeros of each finite determinant on the real spectral axis;
- a prolate trial state
  \[
  k_\lambda=\mathcal E(h_\lambda),
  \]
  with \(h_\lambda\) the unique \(h_{0,\lambda}\)-\(h_{4,\lambda}\) linear combination of zero integral;
- and, crucially, Lemma 7.3: the Fourier transform of \(k_\lambda\) already converges to Riemann's \(\Xi\) uniformly on closed substrips of \(|\Im z|<1/2\).

Their Section 8 states two missing steps:
1. prove the finite Weil ground is simple and even;
2. prove \(k_\lambda\) approximates that ground strongly enough.

Thus GPP's independently derived vacuum-gap inequality attacks EXACTLY their second missing theorem, not a neighboring surrogate.

## 2. Quantitative closure theorem

Let \(Q_\lambda\) be a finite even Weil block, \(u_\lambda\) its normalized ground state, \(v_\lambda\) the normalized projection of \(k_\lambda\), and
\[
\epsilon_\lambda
=
\langle v_\lambda,Q_\lambda v_\lambda\rangle-\lambda_{1,\lambda},
\qquad
\Delta_\lambda
=
\lambda_{2,\lambda}-\lambda_{1,\lambda}.
\]

The elementary spectral theorem gives
\[
\boxed{
1-|\langle u_\lambda,v_\lambda\rangle|^2
\le
\frac{\epsilon_\lambda}{\Delta_\lambda}
}
\]
and after phase alignment
\[
\boxed{
\|u_\lambda-v_\lambda\|_2^2
\le
2\,\frac{\epsilon_\lambda}{\Delta_\lambda}.
}
\]

If \(u_\lambda,v_\lambda\) are supported on a logarithmic interval of half-width \(A=\log\lambda\), then for \(z=t+i\eta\)
\[
|\widehat u_\lambda(z)-\widehat v_\lambda(z)|
\le
\|u_\lambda-v_\lambda\|_2
\left(
\int_{-A}^{A}e^{2\eta x}\,dx
\right)^{1/2}.
\]

For every fixed \(0<a<1/2\),
\[
\sup_{|\eta|\le a}
|\widehat u_\lambda-\widehat v_\lambda|
\lesssim_a
\lambda^a
\sqrt{\epsilon_\lambda/\Delta_\lambda}.
\]

Therefore the sufficient rate
\[
\boxed{
\frac{\epsilon_\lambda}{\Delta_\lambda}
=
o(\lambda^{-1})
}
\]
already implies convergence on every closed substrip \(|\Im z|\le a<1/2\), because
\[
\lambda^a\sqrt{o(\lambda^{-1})}
=
o(\lambda^{a-1/2})
\to0.
\]

Combined with CCM Lemma 7.3 and Hurwitz, this yields RH once the finite determinants have the required self-adjoint/simple-even construction.

So the required relative vacuum rigidity is MUCH weaker than the earlier heuristic \(O(\lambda^{-4})\) rate. Any \(o(\lambda^{-1})\) Rayleigh-excess/gap ratio suffices.

## 3. Exact finite Mellin formula for the prolate trial vector

Let the time-limited prolate combination be represented on \([-\lambda,\lambda]\) by
\[
h_\lambda(x)=\sum_{q=0}^{M} d_q x^q,
\]
and set
\[
k_\lambda(u)=u^{1/2}\sum_{n\ge1}h_\lambda(nu).
\]

On
\[
u=e^y,\qquad -A\le y\le A,\qquad A=\log\lambda,
\]
only \(n\le c=\lambda^2\) occur.

For a Fourier frequency \(\omega\), define
\[
I_\lambda(\omega)
=
\int_{-A}^{A}
k_\lambda(e^y)e^{-i\omega y}\,dy.
\]

Swap the finite \(n\)-sum with the integral. For
\[
a_q=q+\frac12-i\omega,
\]
one obtains EXACTLY
\[
\boxed{
I_\lambda(\omega)
=
\sum_q\frac{d_q}{a_q}
\left[
\lambda^{a_q}
\sum_{n\le c}n^{-1/2+i\omega}
-
\lambda^{-a_q}
\sum_{n\le c}n^q
\right].
}
\]

Thus the finite prolate trial vector has a completely explicit arithmetic Fourier representation involving only:

- a critical-line Dirichlet polynomial
  \[
  \sum_{n\le c}n^{-1/2+i\omega};
  \]
- ordinary power sums \(\sum_{n\le c}n^q\);
- and the prolate polynomial coefficients \(d_q\).

No quadrature is required.

This is conceptually important: the same \(1/2\) half-density selected by the KMS/principal-series construction appears directly in the literal CCM prolate trial vector.

## 4. Why the exact formula may be more than a numerical convenience

The first term contains the truncated critical Dirichlet series. The second term is a finite Euler--Maclaurin/Faulhaber subtraction determined by the prolate source.

So the map
\[
h_\lambda\mapsto k_\lambda
\]
is an explicit finite renormalization of the critical Dirichlet polynomial.

This gives a new possible analytic attack on the residual:
instead of estimating \(Q_\lambda k_\lambda\) entrywise, rewrite the finite Fourier coefficients via the boxed formula and use the defining prolate differential equation to control the subtraction algebraically.

The hope is that the prolate equation turns the large Dirichlet/Faulhaber pieces into boundary terms proportional to the time--frequency leakage \(1-\chi_\lambda\).

That would give the exact bridge
\[
\boxed{
\epsilon_\lambda
\lesssim
(1-\chi_\lambda)\times(\text{explicit polynomial factor}),
}
\]
which is precisely the kind of estimate needed for \(\epsilon_\lambda/\Delta_\lambda=o(\lambda^{-1})\).

## 5. Zero-free scan: first decisive evidence

A literal Legendre--Galerkin implementation of the CCM \(h_{0,\lambda}\)-\(h_{4,\lambda}\) trial state was projected into the actual finite Weil matrix, using no Riemann-zero ordinates.

At \(N=28,T=300\):

### \(c=3\)
\[
|\langle u,v\rangle|
=
0.999999840274066\ldots
\]
and
\[
\boxed{\epsilon/\Delta
=
1.856851359\times10^{-6}}.
\]

### \(c=5\)
\[
|\langle u,v\rangle|
=
0.999999957435492\ldots,
\]
\[
\boxed{\epsilon/\Delta
=
2.755997178\times10^{-7}}.
\]

### \(c=7\)
\[
|\langle u,v\rangle|
=
0.999999991040211\ldots,
\]
\[
\boxed{\epsilon/\Delta
=
1.416362459\times10^{-7}}.
\]

These are dramatically better than the naive truncated-Riemann-\(\Phi\) control.

For \(c\ge11\), the first prototype hit a double-precision floor in the prolate construction: the residual stalled near \(10^{-15}\), hence the Rayleigh defect near \(10^{-30}\), while the true Weil gaps are already \(10^{-36}\) to \(10^{-46}\). The subsequent large \(\epsilon/\Delta\) values are therefore NOT interpretable as a mathematical failure of the prolate trial state.

A high-precision Legendre + exact-Mellin scan has been launched to resolve this.

## 6. Public-literature no-go that the synthesis respects

Makraini's 2026 truncated-Weil analysis reports that norm convergence of the truncated Weil operator to the prolate projection is impossible. That does not obstruct the present route.

The GPP/CCM target is only one distinguished low-energy vector/projector:
\[
u_\lambda\approx k_\lambda,
\]
not norm convergence of the whole operator.

This is exactly the kind of situation where the vacuum-gap ratio is stronger conceptually and weaker analytically than operator-norm convergence.

## 7. Direct next theorem

The most valuable analytic target is now:

> Prove a zero-independent bound of the form
> \[
> \epsilon_\lambda
> \le
> C\,\lambda^B(1-\chi_4(\lambda))
> \]
> for the literal CCM prolate trial state, while proving a lower bound on the first physical even gap
> \[
> \Delta_\lambda
> \ge
> \lambda^{-C'}e^{-o(\lambda^2)}
> \]
> strong enough that
> \[
> \epsilon_\lambda/\Delta_\lambda=o(\lambda^{-1}).
> \]

The known prolate concentration asymptotic has
\[
1-\chi_4(\lambda)
\sim
\text{poly}(\lambda)e^{-4\pi\lambda^2},
\]
so even a substantially weaker exponential gap lower bound could close the convergence theorem.

The public literature therefore does not replace the GPP mechanism. It identifies that our independently found vacuum-gap estimate is pointed exactly at the published missing theorem.
