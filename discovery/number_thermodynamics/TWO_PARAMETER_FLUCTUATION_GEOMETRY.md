# Two-parameter prime-gas fluctuation geometry

## Purpose

The one-parameter Gibbs family `p_beta(n) ∝ n^{-beta}` has a one-dimensional Fisher metric, so its intrinsic scalar curvature is identically zero. A genuine fluctuation geometry requires at least two independent sufficient statistics.

Use

\[
Z(\beta,\eta)=\sum_{n\ge 2}\exp[-\beta\log n-\eta(\log n)^2]
=\sum_{n\ge2} n^{-\beta}e^{-\eta(\log n)^2},
\]

with normalized weights

\[
p_n=Z^{-1}n^{-\beta}e^{-\eta(\log n)^2}.
\]

For `eta > 0`, the partition sum converges for every real `beta`; on the boundary `eta=0` it converges for `beta>1`. The natural sufficient statistics are

\[
T_1(n)=x_n=\log n,\qquad T_2(n)=x_n^2.
\]

The log-partition Hessian is the Fisher/covariance metric

\[
g=\nabla^2\log Z
=\begin{pmatrix}
\operatorname{Var}(X) & \operatorname{Cov}(X,X^2)\\
\operatorname{Cov}(X,X^2) & \operatorname{Var}(X^2)
\end{pmatrix}.
\]

(Signs from the natural parameters `(-beta,-eta)` cancel in the Hessian.)

## Exact determinant identity

Let `mu_k = E[X^k]`. Then

\[
\det g=(\mu_2-\mu_1^2)(\mu_4-\mu_2^2)-(\mu_3-\mu_1\mu_2)^2.
\]

Introduce the 3x3 moment Gram matrix

\[
M=E\!\left[(1,X,X^2)^T(1,X,X^2)\right]
=\begin{pmatrix}
1&\mu_1&\mu_2\\
\mu_1&\mu_2&\mu_3\\
\mu_2&\mu_3&\mu_4
\end{pmatrix}.
\]

Taking the Schur complement of the upper-left `1` gives exactly `g`, hence

\[
\det g=\det M.
\]

For a discrete probability measure, Cauchy-Binet applied to the weighted Vandermonde matrix gives the exact nonnegative expansion

\[
\boxed{
\det g
=\sum_{i<j<k}p_i p_j p_k
\big[(x_i-x_j)(x_i-x_k)(x_j-x_k)\big]^2.}
\]

Therefore `det g > 0` whenever at least three distinct support points have positive probability. The prime-gas support contains every integer `n>=2`, so throughout the convergence domain the two-parameter Fisher metric is strictly positive definite.

This is stronger than a bare Cauchy-Schwarz argument: it identifies the determinant as a positive weighted sum of squared Vandermonde volumes. It also gives a natural exact target for Lean, first for a finite Gibbs truncation and then for the convergent countable limit.

## Relation to the one-parameter zeta gas

At `eta=0`, `Z(beta,0)=zeta(beta)-1` for the support `n>=2` used here. If the vacuum state `n=1` is included, `Z(beta,0)=zeta(beta)` exactly and `x_1=0`; the same covariance and Vandermonde formulas hold. Thus the existing zeta Gibbs variance/heat-capacity theorem is the `(beta,beta)` component of this two-dimensional metric, while the determinant supplies the first genuinely nontrivial fluctuation-geometric invariant.

No RH implication is asserted. The positivity is ordinary exponential-family/Fisher positivity on the real convergence domain.

## Formalization target

1. Finite support: prove the 3x3 moment determinant equals the 2x2 covariance determinant.
2. Prove the finite Cauchy-Binet/Vandermonde expansion and strict positivity from three explicit states, e.g. `n=1,2,3` (or `2,3,4` if excluding the vacuum).
3. Define the two-parameter truncated Gibbs weights and package `g` as a positive-definite matrix.
4. Only after summability infrastructure is ready, pass to the countable prime-gas limit.
