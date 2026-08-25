# Fisher distance bound from Jeffreys divergence

Codex/GPT discovery track, 2026-08-25.

For the zeta Gibbs family on beta>1,

A(beta)=log zeta(beta),
U(beta)=-A'(beta),
g(beta)=A''(beta)>0.

The exact KL divergence is the Bregman divergence

D(beta||gamma)=A(gamma)-A(beta)+(gamma-beta)U(beta).

Therefore the Jeffreys divergence is

J(beta,gamma)
 = D(beta||gamma)+D(gamma||beta)
 = (gamma-beta)(U(beta)-U(gamma)).

For beta<gamma, since U'=-g,

J(beta,gamma)
 = (gamma-beta) int_beta^gamma g(x) dx.

The Fisher arclength is

d_F(beta,gamma)=int_beta^gamma sqrt(g(x)) dx.

Cauchy-Schwarz gives

[int_beta^gamma sqrt(g) dx]^2
 <= (gamma-beta) int_beta^gamma g dx,

hence the exact information-geometric bound

boxed:  d_F(beta,gamma)^2 <= J(beta,gamma).

Thus the symmetrized relative entropy globally dominates squared thermodynamic/Fisher distance. Infinitesimally both agree to quadratic order:

J(beta,beta+delta)=g(beta) delta^2+O(delta^3),
d_F(beta,beta+delta)^2=g(beta) delta^2+O(delta^3).

No continuation outside beta>1 is used.
