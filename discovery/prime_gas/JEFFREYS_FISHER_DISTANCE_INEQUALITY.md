# Jeffreys divergence versus Fisher distance in the zeta Gibbs family

Codex/GPT discovery track, 2026-08-25.

For the zeta Gibbs family on beta>1,

p_beta(n) = n^{-beta}/zeta(beta),

g(beta) = d^2/d beta^2 log zeta(beta) = Var_beta(log n) > 0.

The Fisher arclength coordinate is

tau(gamma)-tau(beta) = int_beta^gamma sqrt(g(x)) dx.

The already-derived symmetrized KL / Jeffreys divergence is

J(beta,gamma)
 = D(p_beta||p_gamma)+D(p_gamma||p_beta)
 = (gamma-beta) int_beta^gamma g(x) dx,

for 1<beta<gamma.

## Exact comparison

Cauchy--Schwarz on [beta,gamma] gives

(int_beta^gamma sqrt(g(x)) dx)^2
 <= (int_beta^gamma 1 dx)(int_beta^gamma g(x) dx).

Therefore

boxed:

J(beta,gamma) >= (tau(gamma)-tau(beta))^2.

Thus Jeffreys divergence dominates squared geodesic distance for this one-dimensional Fisher manifold.

Equality in Cauchy--Schwarz would require sqrt(g) to be constant almost everywhere on the interval. But g'(beta)=-kappa_3(beta)<0 for the zeta Gibbs family, so g is strictly decreasing and equality is impossible for beta<gamma. Hence

boxed:

J(beta,gamma) > (tau(gamma)-tau(beta))^2,

for every 1<beta<gamma.

## Universal pole-scaling limit

Let

beta = 1+epsilon,
gamma = 1+c epsilon,

with c>1 fixed and epsilon -> 0+.

Since

g(1+u) = u^{-2}+O(1),

the Fisher distance obeys

tau(gamma)-tau(beta) -> log c.

Meanwhile

J(beta,gamma)
 = (c-1)epsilon int_epsilon^{c epsilon} [u^{-2}+O(1)] du
 -> (c-1)^2/c.

Therefore the geometric inequality has the universal pole limit

boxed:

(log c)^2 < (c-1)^2/c,  c>1.

Equivalently,

sqrt(c) |log c| < c-1.

This is not a zero-location statement. It is a sharp asymptotic relation between information divergence and Fisher distance in the thermodynamic blow-up coordinate near the zeta pole.
