# Two-parameter zeta-Gibbs Fisher determinant: explicit 3-point lower bound

For the genuine two-parameter family

\[
Z(\beta,\eta)=\sum_{n\ge1}e^{-\beta\log n-\eta(\log n)^2},
\qquad \eta>0,
\]

let

\[
p_n=Z^{-1}e^{-\beta x_n-\eta x_n^2},\qquad x_n=\log n.
\]

The Fisher metric in natural coordinates `(beta, eta)` is the covariance matrix
of the sufficient statistics `X` and `X^2`:

\[
g=\begin{pmatrix}
\operatorname{Var}(X)&\operatorname{Cov}(X,X^2)\\
\operatorname{Cov}(X,X^2)&\operatorname{Var}(X^2)
\end{pmatrix}.
\]

The finite-support Gram/Cauchy-Binet identity gives

\[
\det g
=\sum_{i<j<k}p_i p_j p_k
  (x_j-x_i)^2(x_k-x_i)^2(x_k-x_j)^2.
\]

The countable extension is the next formal target; all summands are nonnegative,
so once that passage is justified, the single triple `n=1,2,3` gives the explicit
strict lower bound

\[
\boxed{
\det g\ge
\frac{e^{-\beta\log6-\eta[(\log2)^2+(\log3)^2]}}{Z(\beta,\eta)^3}
\,[\log2\,\log3\,\log(3/2)]^2>0.
}
\]

This is stronger than qualitative positive definiteness: it supplies a concrete
arithmetic witness for nondegeneracy everywhere on the open convergence domain
`eta > 0`. The same witness also applies on the boundary `eta=0, beta>1`, where
`Z=zeta(beta)`, provided the countable determinant identity is established there.

`two_parameter_fisher_vandermonde_lower_bound.py` checks the bound numerically at
representative points, including negative beta with positive eta. The numerical
check is evidence only; the theorem target is the countable nonnegative
Cauchy-Binet/Vandermonde expansion plus the explicit retained triple.

## Formalization target

Reuse the already-formalized finite strict Hankel/Vandermonde algebra and the
all-order strict polynomial Gram infrastructure. Prove a countable determinant
expansion or a monotone finite-truncation lower-bound theorem sufficient to retain
the `(1,2,3)` triple. This should yield strict Fisher determinant positivity with
an explicit lower bound without relying on curvature numerics.
