# Minimal principal-series criterion: slit-plane analyticity and a self-adjoint off-diagonal resolvent

Date: 2026-09-28
Status: exact RH equivalence plus an exact free-resolvent representation of the prime term in the Euler domain. This deliberately removes all positivity assumptions. No RH proof is claimed.

## 1. The genuinely minimal analytic target

Define the unconditional centered Casimir entire function
\[
F(u)=\frac{\xi(\frac12+\sqrt u)}{\xi(\frac12)},
\]
understood branch-independently through the even factorization
\[
\xi(\tfrac12+z)/\xi(\tfrac12)=F(z^2).
\]

Every nontrivial zero \(\rho\) gives
\[
u_\rho=(\rho-\tfrac12)^2.
\]

Because \(\xi(\tfrac12+\sqrt u)>0\) for real \(u\ge0\), \(F\) has no zero on \([0,\infty)\).

Hence
\[
\boxed{
\mathrm{RH}
\iff
F\text{ is zero-free on }\mathbb C\setminus(-\infty,0]
}
\]
and equivalently
\[
\boxed{
\mathrm{RH}
\iff
m(u):=\frac{F'(u)}{F(u)}
\text{ is holomorphic on }\mathbb C\setminus(-\infty,0].
}
\]

This criterion asks for neither positivity nor a determinant. It asks only that the logarithmic Casimir response have no physical-sheet singularity away from the negative real axis.

An off-line zero \(\rho=\frac12+\delta+i\gamma\) with \(\delta\gamma\ne0\) produces
\[
u_\rho=\delta^2-\gamma^2+2i\delta\gamma,
\]
a non-real pole of \(m\).

## 2. Any self-adjoint resolvent realization is sufficient

Let \(L=L^*\) be any self-adjoint operator with spectrum contained in \([0,\infty)\), and let \(\Phi,\Psi\) be vectors or admissible rigged boundary vectors for which
\[
R_{\Phi,\Psi}(u)
=
\langle \Phi,(L+u)^{-1}\Psi\rangle
\]
is defined.

Then \(R_{\Phi,\Psi}\) is holomorphic on
\[
\mathbb C\setminus(-\infty,0].
\]

No diagonal condition \(\Phi=\Psi\) is required.
No positivity of the scalar function is required.
The matrix element may change sign and need not be Herglotz or Stieltjes.

Therefore it is enough to construct
\[
\boxed{
m(u)
=
\langle \Phi,(L+u)^{-1}\Psi\rangle
+
h(u)
}
\]
where \(L=L^*\ge0\) and \(h\) is holomorphic on the slit plane.

This alone proves RH.

This is strictly weaker than every previous positive-Fredholm, Stieltjes, Pick, or Weil-positivity target.

## 3. The prime logarithmic derivative is already an off-diagonal FREE resolvent

Let
\[
L_0=-\frac{d^2}{dx^2}
\]
on \(L^2(\mathbb R)\).

For the principal branch \(\Re\sqrt u>0\),
\[
\boxed{
(L_0+u)^{-1}(x,y)
=
\frac{e^{-\sqrt u|x-y|}}{2\sqrt u}.
}
\]

Put
\[
s=\frac12+\sqrt u.
\]

In the absolute Euler domain \(\Re s>1\),
\[
\frac{\zeta'}{\zeta}(s)
=
-\sum_{n\ge2}\Lambda(n)n^{-s}.
\]

Hence the prime part of the centered Casimir response is EXACTLY
\[
\boxed{
m_{\rm prime}(u)
=
-\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(L_0+u)^{-1}(0,\log n).
}
\]

Equivalently, with the formal half-density von Mangoldt current
\[
J_\Lambda
=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n},
\]
\[
\boxed{
m_{\rm prime}(u)
=
-\langle \delta_0,(L_0+u)^{-1}J_\Lambda\rangle.
}
\]

This is not an analogy. The square-root subordination kernel found in the previous heat note is exactly the standard free one-dimensional resolvent kernel.

Thus the primes are already coupled to the correct second-order Casimir propagator.

## 4. Why positivity kept looking unnatural

The source and sink in the prime response are DIFFERENT:
\[
\delta_0
\quad\text{and}\quad
J_\Lambda.
\]

So the natural scalar object is an off-diagonal resolvent matrix element, not a norm square.

Trying to force
\[
m(u)=\langle v,(L+u)^{-1}v\rangle
\]
was stronger than the explicit formula naturally supplies.

The negative sign of the prime contribution is also no obstruction to self-adjointness. Off-diagonal resolvent matrix elements have no fixed sign.

This explains why local prime positivity repeatedly failed to assemble into a global positive heat trace while the representation-theoretic picture continued to look self-adjoint.

## 5. The exact remaining domain obstruction

The formal scalar current
\[
J_\Lambda
=
\sum_n\Lambda(n)n^{-1/2}\delta_{\log n}
\]
is too large to be an ordinary Hilbert vector. In fact the Euler-domain convergence threshold of the matrix element is precisely
\[
\Re\sqrt u>\frac12.
\]

Therefore the remaining theorem is NOT positivity. It is a boundary-domain/renormalization theorem:

> After the Archimedean and pole/vacuum completion dictated by Poisson self-duality and the product formula, the completed source must define an admissible rigged vector (or relative resolvent functional) for a self-adjoint logarithmic Casimir on the whole slit plane.

If this is proved, RH follows immediately from resolvent analyticity.

This recovers the earlier "primitive temperateness" criterion in a sharper operator form: temperateness is one sufficient domain condition, but any rigged-resolvent admissibility that gives slit-plane holomorphy is enough.

## 6. Finite version and the simplest possible limit theorem

At finite arithmetic cutoff \(P\), the source is finite:
\[
J_{\Lambda,P}
=
\sum_{n\in\mathcal N_P}
\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
\]

Thus
\[
m_P(u)
=
-\langle\delta_0,(L_0+u)^{-1}J_{\Lambda,P}\rangle
+
m_{\infty,P}(u)
+
m_{{\rm vac},P}(u)
\]
is a scalar matrix element of a finite/direct-sum self-adjoint system and is holomorphic on the slit plane.

If one can prove:

1. \(m_P(u)\to m(u)\) on any set with an interior accumulation point in the Euler domain;
2. the family \(\{m_P\}\) is locally bounded on the slit plane after the exact Archimedean/vacuum completion;

then Vitali gives local-uniform convergence on the slit plane, so \(m\) is holomorphic there and RH follows.

This is potentially much easier than proving positivity or determinant convergence.

The absolute Euler expansion already gives pointwise convergence in the first region. The whole problem has collapsed to a cutoff-uniform NORMAL-FAMILY BOUND.

## 7. Physical interpretation

The centered variable \(u=(s-\frac12)^2\) is the conformal-Casimir defect.

The kernel
\[
e^{-\sqrt u|x-y|}/(2\sqrt u)
\]
is the Euclidean Green function of the one-dimensional massive free field.

The primes sit at logarithmic positions
\[
x_n=\log n
\]
with charges
\[
\Lambda(n)/\sqrt n.
\]

So the explicit formula literally couples the self-dual logarithmic number line to a point-source arithmetic current through the free Casimir propagator.

RH says that after the global Poisson/product-formula boundary completion, this source-response system is a genuine physical-sheet self-adjoint resolvent: all singularities lie on the self-adjoint spectral cut, hence every zeta zero is principal-series.

This is currently the simplest operator statement in the programme.
