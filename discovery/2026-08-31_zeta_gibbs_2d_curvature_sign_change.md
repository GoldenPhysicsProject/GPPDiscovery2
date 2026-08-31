# Zeta-Gibbs 2D Fisher curvature: sampled sign change

## Exact setup

Use the genuine two-parameter arithmetic Gibbs family

\[
Z(\beta,\eta)=\sum_{n\ge1}\exp\{-\beta\log n-\eta(\log n)^2\},\qquad \eta>0.
\]

Writing \(X=\log n\) and \(T=(X,X^2)\), the Fisher/Hessian metric of
\(\psi=\log Z\) is

\[
g=\operatorname{Cov}(T)=
\begin{pmatrix}
\operatorname{Var}(X) & \operatorname{Cov}(X,X^2)\\
\operatorname{Cov}(X,X^2) & \operatorname{Var}(X^2)
\end{pmatrix}.
\]

The strict two-score positivity already formalized on the one-parameter zeta
boundary strongly motivates the same nondegeneracy on the open \(\eta>0\)
family; the numerical probe below keeps `det(g)>0` at every tested point.

For a 2D Hessian metric, with the scalar-curvature sign convention used in the
companion executable,

\[
R=-\frac{1}{2(\det g)^2}
\det\begin{pmatrix}
\psi_{11}&\psi_{12}&\psi_{22}\\
\psi_{111}&\psi_{112}&\psi_{122}\\
\psi_{112}&\psi_{122}&\psi_{222}
\end{pmatrix}.
\]

All third derivatives are minus the corresponding third joint cumulants of
\((X,X^2)\), since both natural parameters enter the Gibbs weight with minus
signs.

## Discovery result

High-precision finite-sum evaluation, checked for stability by doubling the
truncation from 10,000 to 20,000 terms in a rapidly convergent region, gives
both curvature signs. Representative values are approximately

- \((\beta,\eta)=(0,1)\): \(R=-0.1857212891\),
- \((0,1.5)\): \(R=-0.0501642533\),
- \((0,2)\): \(R=+0.05550882915\),
- \((0,3)\): \(R=+0.2024087841\),
- \((1,2)\): \(R=-0.03845115184\).

Thus the tempting conjecture that the genuine two-parameter zeta-Gibbs Fisher
surface has globally negative scalar curvature is false, at least under this
standard Hessian-curvature convention. The sign-change locus itself becomes a
new arithmetic/statistical observable worth analyzing.

This is a numerical discovery, not a formal theorem. The exact next steps are:

1. formalize convergence/smooth differentiation of `Z(beta,eta)` on `eta>0`;
2. identify the Hessian entries with covariances and prove positive definiteness;
3. derive the third derivatives as joint cumulants;
4. formalize the Hessian 2D curvature determinant formula;
5. only then attack existence/location/meaning of a zero-curvature locus.

Executable: `experiments/zeta_gibbs_2d_fisher_curvature.py`.
