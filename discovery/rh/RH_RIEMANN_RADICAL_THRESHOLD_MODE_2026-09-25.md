# RH threshold mode from the Riemann radical
## Date: 2026-09-25
## Status: exact formal identity at the quadratic-form level, subject to standard domain justification for differentiating the translation radical. No RH claim.

Let Phi be Riemann's positive even Fourier density, so its Fourier transform is Xi.
For every real a, translation gives
Phi_a(x)=Phi(x-a),
hat{Phi_a}(t)=e^{-iat} Xi(t).

Therefore Phi_a vanishes on the full nontrivial zeta zero set in the explicit-formula pairing, independently of where those zeros lie. Hence every admissible translate lies in the Weil radical:
Q Phi_a = 0
in the form sense.

Differentiating at a=0 gives
Q Phi' = 0.

Use the even-sector positive ground-state gauge from
RH_GROUND_STATE_POINCARE_PRINCIPAL_SERIES_2026-09-25.md.
Let
h_1(x)=-Phi'(x)/Phi(x).

Because Phi is even, h_1 is odd. The ground-state transform of Q has the form
Q[Phi h] = E(h) - (C^2/2) Var_nu(h).
For odd h, the nu-mean is zero, so the radical identity Q Phi'=0 gives

E(h_1) = (C^2/2) ||h_1||_{L^2(nu)}^2.

Thus h_1 sits exactly at the normalized spectral threshold 1.

Interpretation:
- h_0=1 is the zero mode of the reversible Markov/jump generator;
- h_1=-d log Phi/dx is the canonical odd threshold mode;
- if Phi is strictly decreasing on x>0, h_1 has exactly one zero, at x=0;
- an eigenvalue below h_1 is precisely a complementary-series/bad-zero mode.

Therefore a genuine one-dimensional oscillation theorem for the completed arithmetic jump generator would prove RH:
if the one-node odd threshold mode is the first excited state, the spectral gap is exactly the principal-series threshold and no complementary state exists.

This is the nonlocal analogue of the Sturm statement:
ground state has zero nodes; first excited state has one node.

Caution:
for a nonlocal jump generator, ordinary local Sturm-Liouville nodal theory does not apply automatically. Prime jumps crossing x=0 create reflected plus-square terms in the half-line odd restriction, so a proof must establish variation-diminishing/sign-regular structure for the completed semigroup, not merely cite local Sturm theory.

The threshold is sharp because the translated Riemann radical supplies generalized threshold states; no proof should seek a gap strictly larger than 1.
