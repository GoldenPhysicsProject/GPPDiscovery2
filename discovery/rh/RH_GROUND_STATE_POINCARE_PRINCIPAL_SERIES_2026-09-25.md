# RH ground-state transform: principal-series Poincare gap
## Date: 2026-09-25
## Status: exact finite algebra; continuum identification is the RH-equivalent endpoint problem

Let Q=A+(1/2)cc^T on an even finite CCM sector, with A real symmetric and A_ij<=0 for i!=j.
Assume phi_i>0 and Q phi=0. Put C=c^T phi and assume c_i phi_i>=0, C>0.
For x_i=phi_i h_i define nu_i=c_i phi_i/C.

Then the exact ground-state transform is

x^T Q x
=
(1/2) sum_{i,j} (-A_ij) phi_i phi_j (h_i-h_j)^2
-
(C^2/2) Var_nu(h).

Proof:
For E=(1/2)sum(-A_ij)phi_i phi_j(hi-hj)^2,
E = x^T A x - sum_i hi^2 phi_i (A phi)_i.
Since A phi=-(C/2)c,
x^T A x = E -(C/2)sum_i c_i phi_i hi^2.
Adding (1/2)(c^T x)^2 gives
E -(C^2/2)[sum nu_i hi^2-(sum nu_i hi)^2].

Thus Q>=0 is equivalent on this positive ground-state gauge to the sharp Poincare inequality

(2/C^2) E(h) >= Var_nu(h).

The threshold is exactly 1.

For the shifted finite operator T=Q-eps I with positive ground vector phi and Q phi=eps phi, the same calculation gives the exact identity

x^T T x = E(h) - (C^2/2) Var_nu(h).

Hence the normalized jump gap 1 is automatic once the finite ground vector is known positive; conversely the Poincare inequality proves T>=0 in this gauge.

Continuum interpretation:
Riemann's positive Fourier density Phi is the BPY tilted log-radius density up to normalization. The pole weight c(x)=2 cosh(x/2) makes
nu_*(dx) proportional to c(x)Phi(x)dx, i.e. the equal mixture of the BPY endpoint tilts s=0 and s=1.

The non-pole A=-W_R-W_P has nonpositive off-diagonal kernel: an Archimedean continuous jump kernel plus arithmetic jumps at +/- log n weighted by Lambda(n)/sqrt(n). Therefore its Phi-transform is a reversible nonlocal Dirichlet form.

The exact endpoint problem is:
normalized arithmetic jump Dirichlet form >= Var_{nu_*}.
This is a sharp Poincare spectral-gap statement. In representation language:
- eigenvalue 1 = tempered/principal-series threshold;
- spectrum below 1 = complementary-series/bad-zero sector;
- RH = no spectrum below 1.

Radical family:
Any translate Phi(.-a) has Fourier transform exp(-iat)Xi(t), hence still vanishes on every zeta zero. Where it belongs to the form domain, its ground-state quotient h_a=Phi(.-a)/Phi lies at the unit threshold. This explains numerically observed generalized eigenvalues piling up at 1 and shows that the gap is sharp, not strictly greater than 1.

This identity is the ground-state-coordinate version of the existing BPY endpoint Laguerre-Nevanlinna kernel criterion, not a separate assumption.

Open load-bearing theorem:
prove the sharp Poincare inequality noncircularly, or equivalently rule out a complementary-series bound state below 1. The finite secular pole reduction and the cross-resolvent/cumulative-mass machinery are concrete finite approximants to this statement.

No RH proof is claimed.
