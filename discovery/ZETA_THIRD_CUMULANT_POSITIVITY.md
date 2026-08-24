# Zeta Gibbs third cumulant: analytic positivity

For real beta > 1, let

Z(beta) = zeta(beta),  p_beta(n) = n^{-beta}/Z(beta),  E_n = log n.

The Gibbs cumulants satisfy

kappa_r(beta) = (-1)^r d^r/d beta^r log Z(beta).

In particular,

kappa_3(beta) = - d^3/d beta^3 log zeta(beta).

On beta > 1, Euler's product is absolutely convergent and

log zeta(beta) = sum_p sum_{k>=1} p^{-k beta}/k.

Termwise differentiation is justified on every closed half-line beta >= 1+epsilon, giving

d^3/d beta^3 log zeta(beta)
  = - sum_p sum_{k>=1} k^2 (log p)^3 p^{-k beta}.

Therefore

kappa_3(beta)
  = sum_p sum_{k>=1} k^2 (log p)^3 p^{-k beta} > 0

for every beta > 1. Strictness is immediate because every summand is nonnegative and, for example, the p=2, k=1 term is strictly positive.

Equivalent von Mangoldt form:

kappa_3(beta)
  = sum_{n>=2} Lambda(n) (log n)^2 n^{-beta} > 0,

since for n=p^k, Lambda(n)(log n)^2 = (log p)(k log p)^2 = k^2 (log p)^3.

Consequently the Gibbs variance is strictly decreasing:

d/d beta Var_beta(log n) = -kappa_3(beta) < 0.

More generally, the same Euler-product argument gives the full strict sign hierarchy

(-1)^r d^r/d beta^r log zeta(beta)
  = sum_p sum_{k>=1} k^{r-1}(log p)^r p^{-k beta} > 0

for every integer r >= 1 and beta > 1.

Status: analytic discovery theorem on the honest Euler-product half-line only. No continuation of positivity into the critical strip is claimed. The next formal target is to derive the r=3 von-Mangoldt Dirichlet-series identity from the already formalized global von Mangoldt/log-derivative bridge and the all-orders zeta logarithmic-moment machinery.
