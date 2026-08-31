# Two-parameter zeta-Gibbs domain and Fisher geometry — 2026-08-31

Consider the genuine two-parameter deformation

\[
Z(\beta,\eta)=\sum_{n\ge 1}\exp\{-\beta\log n-\eta(\log n)^2\}.
\]

This supplies the missing open two-dimensional thermodynamic parameter domain; it is not an attempt to manufacture curvature from the one-dimensional beta family.

## Exact convergence domain

Write the nth summand as

\[
a_n=n^{-\beta}\exp[-\eta(\log n)^2].
\]

1. If \(\eta>0\), then for every real \(\beta\) and every \(p>1\), eventually
\(\eta\log n+\beta\ge p\), hence
\(a_n=n^{-(\eta\log n+\beta)}\le n^{-p}\). Therefore the series converges absolutely for every \(\beta\in\mathbb R\).

2. If \(\eta=0\), this is the ordinary Dirichlet series \(\sum n^{-\beta}\), so convergence is exactly \(\beta>1\).

3. If \(\eta<0\), then
\[
\log a_n=|\eta|(\log n)^2-\beta\log n\to+\infty,
\]
so the summand does not even tend to zero. The series diverges.

Thus the open thermodynamic domain is the half-plane \(\eta>0\), with the ordinary zeta Gibbs ray \(\eta=0,\beta>1\) as a convergent boundary component.

## Exact differential geometry

On \(\eta>0\), super-polynomial decay permits termwise differentiation to every finite order on compact parameter subsets. With \(X_n=\log n\) and Gibbs weights

\[
p_n=Z^{-1}e^{-\beta X_n-\eta X_n^2},
\]

we obtain

\[
\partial_\beta\log Z=-\mathbb E[X],\qquad
\partial_\eta\log Z=-\mathbb E[X^2],
\]

and

\[
\nabla^2\log Z=
\begin{pmatrix}
\operatorname{Var}(X) & \operatorname{Cov}(X,X^2)\\
\operatorname{Cov}(X,X^2) & \operatorname{Var}(X^2)
\end{pmatrix}.
\]

For any real \((a,b)\ne(0,0)\), its quadratic form is

\[
\operatorname{Var}(aX+bX^2).
\]

Every integer \(n\ge1\) has strictly positive Gibbs weight. If this variance vanished, the polynomial \(a x+b x^2\) would be constant on the infinite set \(\{\log n:n\ge1\}\), hence would be a constant polynomial. Since its constant coefficient is zero, this forces \(a=b=0\), contradiction. Therefore the Hessian/Fisher metric is strictly positive definite throughout \(\eta>0\).

This dovetails with the already-formalized `PrimeFisherTwoParameterStrict` polynomial-positivity mechanism and the finite covariance/Vandermonde determinant identities. It gives a concrete next formalization target for actual two-parameter zeta-Gibbs information geometry.

## Reproducibility

`experiments/zeta_two_parameter_geometry.py` evaluates truncated moments and the 2x2 Fisher determinant at representative parameter points. Numerical positivity is only a sanity check; the proof above is structural.

## Next formal steps

Formalize the convergence half-plane \(\eta>0\), compact-uniform moment summability, the first/second derivative identities for `log Z`, and strict positive definiteness via the polynomial-score argument. Only after the 2D metric itself is certified should scalar curvature be computed.
