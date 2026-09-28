# Principal-series closure without positivity: real-rooted Casimir limits

Date: 2026-09-28
Status: exact equivalence and a strictly weaker closure target than global positivity. No RH proof.

Daniel emphasized that the closure theorem need not be a positivity criterion; any zero-independent mechanism forcing every zero into the unitary principal series is acceptable. This yields a simpler target.

## 1. Minimal algebraic criterion: REALITY of the centered square

Define
\[
X(z)=\frac{\xi(\frac12+z)}{\xi(\frac12)}=F(z^2).
\]

For a nontrivial zero
\[
\rho=\beta+i\gamma,\qquad \gamma\neq0,
\]
the corresponding zero of \(F\) is
\[
u_\rho=(\rho-\tfrac12)^2
=(\beta-\tfrac12)^2-\gamma^2
+2i\gamma(\beta-\tfrac12).
\]

Therefore
\[
\boxed{
u_\rho\in\mathbb R
\iff
\beta=\frac12
}
\]
for every nontrivial zero.

Since \(F(u)>0\) for real \(u\ge0\), any real zero of \(F\) is automatically negative.

Hence
\[
\boxed{
\mathrm{RH}
\iff
F(u)\text{ has only real zeros}
\iff
F(u)\text{ has only negative real zeros}.
}
\]

This is strictly conceptually weaker than constructing a positive Fredholm operator. Positivity is one sufficient mechanism for real-rootedness, but it is not required.

## 2. Laguerre--Pólya formulation

The entire function \(F\) has order \(1/2\).

For a real entire function of this order,
\[
\boxed{
\mathrm{RH}
\iff
F\in\mathcal{LP},
}
\]
the Laguerre--Pólya class.

Equivalently, there exists a sequence of real polynomials \(P_j\), each with only real zeros, such that
\[
\boxed{
P_j\to F
}
\]
locally uniformly on \(\mathbb C\).

Thus the physical construction need only produce a REAL-ROOTED FINITE APPROXIMATION SCHEME.

It need not first prove:
- Weil positivity;
- Stieltjes positivity;
- Pick positivity;
- complete monotonicity;
- positive Fredholm factorization.

All of those remain useful sufficient structures, but they are stronger than the minimum required.

## 3. Self-adjoint finite matrices are enough

If
\[
P_j(u)=\det(M_j-uI)
\]
for a finite real symmetric/self-adjoint matrix \(M_j\), then every zero of \(P_j\) is real automatically.

Therefore a direct principal-series proof can be organized as:

1. construct finite zero-independent self-adjoint arithmetic matrices \(M_j\);
2. normalize their characteristic determinants \(P_j\);
3. prove \(P_j\to F\) locally uniformly.

Then any nonreal zero of \(F\) would, by Hurwitz, force nearby nonreal zeros of \(P_j\) for large \(j\), impossible.

This is enough for RH.

No positivity of \(M_j\) is needed.

## 4. Vitali + Shadow-Euler uniqueness makes the convergence burden smaller

Full local-uniform convergence need not be proved directly.

Let
\[
u_{k,N}
=
\left(\frac{kN}{k+N}-\frac12\right)^2
\]
for one fixed \(k\ge2\). The points \(u_{k,N}\) have an interior accumulation point
\[
(k-\tfrac12)^2.
\]

Suppose:

1. the family \(\{P_j\}\) is locally bounded on \(\mathbb C\);
2. for every fixed \(N\),
   \[
   P_j(u_{k,N})\to F(u_{k,N}).
   \]

Then Vitali's theorem gives local-uniform convergence
\[
P_j\to F
\]
on the connected domain.

Since every \(P_j\) is real-rooted, Hurwitz gives real-rootedness of \(F\), hence RH.

Therefore the load-bearing theorem can be weakened to:

\[
\boxed{
\text{self-adjoint finite arithmetic approximants}
+
\text{local boundedness}
+
\text{scalar convergence on ONE Shadow-Euler sequence}.
}
\]

This is weaker than the earlier positive-resolvent/Pick criterion.

## 5. Jensen-polynomial formulation

Because \(F\) is real entire,
\[
F(u)=\sum_{n\ge0}a_nu^n,
\]
membership in the Laguerre--Pólya class is equivalently encoded by hyperbolicity of all Jensen polynomials
\[
\boxed{
J_{d,n}(X)
=
\sum_{j=0}^d
\binom dj a_{n+j}X^j.
}
\]

Thus another zero-independent RH target is:

\[
\boxed{
\text{prove every Jensen polynomial of the centered Casimir function }F
\text{ is hyperbolic}.
}
\]

This is a PURE REAL-ROOTEDNESS criterion with no Hilbert-space positivity hypothesis.

It may be approachable if the self-dual divisor/Hodge construction supplies an interlacing recurrence or a finite Jacobi matrix whose characteristic polynomials are precisely the relevant Jensen/Padé approximants.

## 6. Orthogonal-polynomial / Jacobi route

A real symmetric tridiagonal (Jacobi) matrix automatically has:
- real spectrum;
- interlacing spectra of principal minors;
- real-rooted characteristic polynomials.

The local prime valuation chains already have tridiagonal precision matrices
\[
K_p^{-1}
\sim
(I-p^{-1/2}S)(I-p^{-1/2}S^*).
\]

So the global question can be reframed:

> Does the product-formula + Fourier/Hodge quotient turn the tensor product of local valuation-chain Jacobi systems into a one-dimensional effective Jacobi/canonical system whose finite characteristic polynomials converge to \(F\)?

If yes, RH follows from real-rootedness and convergence alone.

This may be the simplest representation-theoretic realization of "the zeros are in the principal series."

## 7. Equivalent principal-series criteria zoo

Any ONE of the following would suffice:

1. **Real Casimir:** every zero has \(\rho(1-\rho)\in\mathbb R\).
2. **Real centered square:** every zero of \(F(u)\) is real.
3. **Laguerre--Pólya:** \(F\in\mathcal{LP}\).
4. **Real-rooted approximants:** \(F\) is a local-uniform limit of real-rooted finite arithmetic polynomials.
5. **Self-adjoint Casimir:** \(F\) is a characteristic/relative determinant of a self-adjoint operator.
6. **Jacobi/canonical system:** \(F\) is the spectral determinant of a real Sturm--Liouville/Jacobi system.
7. **de Branges/Hermite--Biehler:** construct an HB function whose real part/companion is \(X\).
8. **Inner scattering:** a shifted xi ratio is inner for a sequence of shifts tending to zero.
9. **Pick/Herglotz:** the logarithmic resolvent response is a Pick function.
10. **Stieltjes/Fredholm positivity:** stronger sufficient realizations already derived.
11. **Jensen hyperbolicity:** all Jensen polynomials of \(F\) are real-rooted.

The programme should not privilege positivity. The minimal invariant is real-rootedness of the CASIMIR function.

## 8. Immediate front

The most economical current target is now:

\[
\boxed{
P_j(u)=\det(M_j-uI),
\quad M_j=M_j^*,
}
\]
with \(M_j\) built from the finite self-dual divisor/prime-Hodge system, and prove:

\[
\boxed{
P_j(u_{k,N})\to
\frac{\xi(\frac12+\sqrt{u_{k,N}})}{\xi(\frac12)}
}
\]
for one fixed \(k\ge2\), plus a local determinant bound.

This avoids proving an infinite positive form entirely.

If this succeeds, Vitali + Hurwitz place every zero of \(F\) on the real axis, which is exactly every nontrivial zeta zero on
\[
\Re s=\frac12.
\]
