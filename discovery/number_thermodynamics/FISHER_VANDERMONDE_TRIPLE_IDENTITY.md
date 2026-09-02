# Fisher determinant as a Vandermonde triple expectation

For any real random variable `X` with finite fourth moment, let

\[
g=\operatorname{Cov}(X,X^2)
 =\begin{pmatrix}
 \operatorname{Var}(X) & \operatorname{Cov}(X,X^2)\\
 \operatorname{Cov}(X,X^2) & \operatorname{Var}(X^2)
 \end{pmatrix}.
\]

Let `X_1,X_2,X_3` be iid copies of `X`. Then the exact identity is

\[
\boxed{
\det g
=\frac16\,\mathbb E\!\left[
 (X_1-X_2)^2 (X_2-X_3)^2 (X_3-X_1)^2
\right].
}
\]

This is the `d=2` covariance-volume identity.  Write

\[
V(X_1,X_2,X_3)
=\det\begin{pmatrix}
1 & X_1 & X_1^2\\
1 & X_2 & X_2^2\\
1 & X_3 & X_3^2
\end{pmatrix}
=(X_1-X_2)(X_2-X_3)(X_3-X_1).
\]

The general Gram/Cauchy--Binet symmetrization for the centered feature pair
`(X,X^2)` gives

\[
3!\det\operatorname{Cov}(X,X^2)=\mathbb E[V^2],
\]

which is the displayed formula.

## Consequences

1. `det g >= 0` is manifest without invoking an abstract Cauchy--Schwarz step.
2. `det g > 0` iff the law of `X` is not supported on at most two points.  Indeed, the nonnegative integrand is positive exactly when the iid triple contains three distinct values with positive probability.
3. For the quadratically confined number gas

\[
p_n(\beta,\eta)=Z(\beta,\eta)^{-1}
\exp[-\beta\log n-\eta(\log n)^2],\qquad \eta>0,
\]

all `p_n` are strictly positive and `log n` takes infinitely many distinct values. Hence

\[
\boxed{\det\nabla^2\log Z(\beta,\eta)>0}
\]

for every real `beta` and every `eta>0`, once differentiation under the countable sum has been justified.  This gives a direct strict-convexity witness for the full countable model: the three states `n=1,2,3` alone contribute a strictly positive term to the iid triple expectation.

More explicitly, because all terms are nonnegative,

\[
\det g\ge
p_1p_2p_3
\,(\log2)^2(\log3-\log2)^2(\log3)^2,
\]

since the six permutations of `(1,2,3)` cancel the prefactor `1/6`.  Thus strict positivity does not require a limiting argument from finite truncations once the covariance moments exist.

## Formalization target

A robust Lean route is to first prove a finite weighted version:

\[
\det\operatorname{Cov}_p(x,x^2)
=\frac16\sum_{i,j,k}p_ip_jp_k
(x_i-x_j)^2(x_j-x_k)^2(x_k-x_i)^2,
\]

under `p_i >= 0` and `sum p_i = 1`, then derive strict positivity from three positive-weight pairwise-distinct support points.  The countable number-gas theorem can then use Tonelli/nonnegative summation plus the explicit `(1,2,3)` witness.

Status: exact identity independently checked algebraically/numerically; promoted as a discovery/formalization target, not yet a Lean theorem.
