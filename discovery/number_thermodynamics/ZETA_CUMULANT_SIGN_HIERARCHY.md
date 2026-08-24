# Zeta Gibbs cumulant sign hierarchy on the convergent axis

Status: analytic theorem for real beta > 1. This note does not extend any positivity statement by analytic continuation and makes no RH claim.

Let

Z(beta) = zeta(beta) = product_p (1-p^{-beta})^{-1}, beta > 1,

and define the Gibbs cumulants of the arithmetic energy E_n = log n by

kappa_r(beta) = (-1)^r d^r/d beta^r log Z(beta).

Absolute convergence of the Euler product on beta > 1 gives

log zeta(beta) = sum_p sum_{k>=1} p^{-k beta}/k.

Termwise differentiation is justified on every closed half-line beta >= 1+epsilon. For every integer r >= 1,

(-1)^r d^r/d beta^r log zeta(beta)
 = sum_p sum_{k>=1} k^{r-1} (log p)^r p^{-k beta}.

Every summand is nonnegative, and the p=2, k=1 term is strictly positive. Therefore

kappa_r(beta) > 0

for every r >= 1 and every beta > 1.

Using n=p^k and Lambda(p^k)=log p, this is equivalently

kappa_r(beta)
 = sum_{n>=2} Lambda(n) (log n)^{r-1} n^{-beta} > 0.

In particular,

kappa_1 = -zeta'/zeta > 0,

kappa_2 = d^2 log zeta/d beta^2 = Var_beta(log n) > 0,

kappa_3 = -d^3 log zeta/d beta^3
 = -zeta'''/zeta + 3 zeta' zeta''/zeta^2 - 2 (zeta'/zeta)^3 > 0.

Hence the Fisher fluctuation is strictly decreasing:

d/d beta Var_beta(log n) = -kappa_3(beta) < 0.

More generally the derivatives of log zeta are completely alternating on (1,infinity):

(-1)^r (log zeta)^{(r)}(beta) > 0, r>=1.

Equivalently, -d/d beta log zeta(beta) is completely monotone. This is a direct prime-power consequence of the Euler product, stronger than the earlier numerical third-cumulant scan.

Formalization boundary: GPPVerify2 already contains the global von-Mangoldt identity -zeta'/zeta = L(Lambda) on Re(s)>1 and the all-orders raw zeta/log-energy moment identities. The remaining Lean task is to formalize differentiated von-Mangoldt weighted series (or an equivalent prime-power series) and strict positivity for the real beta axis, then identify the r=3 case with the derivative of the already formalized Gibbs variance.
