# Exact M2 chamber-normalization closure

Codex/GPT discovery track, 2026-08-25.

For the two-variable Wiener-Hopf convolution built from

P(lambda)=pi lambda/sinh(pi lambda),

the independently audited harmonic-analysis calculation gives the full-plane integral

I_R2 = 2 pi^2 / 15.

The A2 chamber symmetry relevant to the positive-domain integral makes that domain one third of the full plane:

I_Q = I_R2 / 3 = 2 pi^2 / 45.

The loop-convolution normalization is (2pi)^(-2), so

M2 = I_Q/(2pi)^2
   = [2 pi^2/45]/[4 pi^2]
   = 1/90.

Thus the final normalization is pure algebra once two analytic inputs are established:

1. the full-plane convolution integral I_R2=2pi^2/15;
2. the A2 chamber reduction I_Q=I_R2/3.

This note deliberately separates those analytic statements from the trivial final cancellation. A Lean theorem can close the normalization algebra immediately; a complete formal proof of M2=1/90 still requires formalizing the full-plane integral and chamber symmetry rather than treating either as an axiom.

No amplitude interpretation is asserted: this is the exact chamber-convolution harmonic-analysis quantity only.
