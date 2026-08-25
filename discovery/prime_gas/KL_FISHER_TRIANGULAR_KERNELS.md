# Directed KL divergences as triangular Fisher-metric integrals

Codex/GPT discovery track, 2026-08-25.

For the zeta Gibbs family on beta>1, let

A(beta)=log zeta(beta),
U(beta)=-A'(beta),
g(beta)=A''(beta)=Var_beta(log n)>0.

The exact directed relative entropy is

D(beta||gamma)
 = A(gamma)-A(beta)+(gamma-beta)U(beta)
 = A(gamma)-A(beta)-(gamma-beta)A'(beta).

For beta<gamma, Taylor's theorem with integral remainder gives

boxed:

D(beta||gamma)
 = int_beta^gamma (gamma-x) g(x) dx.

Reversing the arguments gives the complementary triangular kernel

boxed:

D(gamma||beta)
 = int_beta^gamma (x-beta) g(x) dx.

Both are manifestly nonnegative because g>=0.

Adding them gives

D(beta||gamma)+D(gamma||beta)
 = int_beta^gamma [(gamma-x)+(x-beta)] g(x) dx
 = (gamma-beta) int_beta^gamma g(x) dx,

recovering the exact Jeffreys formula.

Subtracting them gives the orientation-sensitive asymmetry

D(beta||gamma)-D(gamma||beta)
 = int_beta^gamma (beta+gamma-2x) g(x) dx.

Thus the skewness of the information distance is controlled by where the Fisher weight g(x) is concentrated relative to the midpoint.

Local expansion follows immediately. With gamma=beta+delta,

g(beta+u)=g(beta)+g'(beta)u+...,

D(beta||beta+delta)
 = (1/2)g(beta)delta^2+(1/6)g'(beta)delta^3+...
 = (1/2)g beta delta^2-(1/6)kappa_3 beta delta^3+...,

because g'=-kappa_3.

Similarly

D(beta+delta||beta)
 = (1/2)g(beta)delta^2+(1/3)g'(beta)delta^3+...

when expanded with the metric evaluated about beta; their sum reproduces the Jeffreys expansion.

No analytic continuation is used; all statements are restricted to beta,gamma>1.
