# Zeta-pole blow-up information geometry

Codex/GPT discovery track, 2026-08-25.

Let

beta_e = 1+e,
gamma_e = 1+c e,

with fixed c>1 and e->0+.

For the zeta Gibbs family,

g(beta) = 1/(beta-1)^2 + O(1),
U(beta) = 1/(beta-1) + O(1).

(The O(1) term in U is immaterial in the difference below.)

## Fisher-distance scaling limit

The Fisher distance is

d_F(beta_e,gamma_e)=int_{beta_e}^{gamma_e} sqrt(g(x)) dx.

Since sqrt(g(1+u))=1/u+O(u),

boxed:

lim_{e->0+} d_F(1+e,1+c e) = log c.

Thus the logarithmic coordinate log(beta-1) is the exact tangent blow-up coordinate at the pole.

## Jeffreys scaling limit

The exact symmetrized relative entropy is

J(beta,gamma)=(gamma-beta)[U(beta)-U(gamma)].

Therefore

J(1+e,1+c e)
 = (c-1)e [1/e - 1/(c e) + O(e)]

and hence

boxed:

lim_{e->0+} J(1+e,1+c e) = (c-1)^2/c.

Combining with the global bound d_F^2 <= J gives the universal pole-tangent inequality

boxed:

(log c)^2 <= (c-1)^2/c,  c>0.

Equivalently, writing c=e^(2x), this is

2|x| <= 2 sinh |x|,

so the boundary inequality is exactly the elementary hyperbolic inequality |x|<=sinh|x|.

The result shows that the Fisher metric has a scale-invariant logarithmic tangent geometry at beta=1+, while the symmetrized relative entropy retains the nonlinear multiplicative separation (c-1)^2/c. No statement about zeta zeros or analytic continuation is involved.
