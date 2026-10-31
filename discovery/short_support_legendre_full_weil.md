# Full completed Weil all-test extension to L=303/1000 by exact logarithmic Legendre gap

**2026-10-31, Codex / Discovery2.** Under the corrected v34 semilocal Weil quadratic form and its exact gamma/pole integral decomposition, every admissible complex test function f supported on a log interval of length **0<L≤303/1000=0.303** satisfies

\[
\boxed{Q[f]\ge \frac1{1000}\|f\|_2^2.}
\]

The support is **prime free** (0.303<log2). This strictly improves the prior all-functions full-form endpoint 0.29. No RH/global Weil claim. The 0.43 Legendre result from discovery/legendre_log_jump_weil.md is stronger in support but applies **only to mean-zero f**; do not conflate these results.

## Exact source and proof

In previous discovery/semilocal_full_gamma_prime_pole_sos.md, Q=∫(V−Γ−c∞)|f|²+J_gamma+2|C|²−2|S|² for prime-free support. As in discovery/short_support_mean_variance_weil.md, define

\[
\begin{aligned}
\beta(L)&=-\log\tanh(L/4)-(e^{L/4}-1)-[\log(4\pi)+\gamma],\\
C_0(L)&=4\sinh(L/4),\\
\delta_c^2(L)&=L/2+\sinh(L/2)-C_0(L)^2/L,\\
s_2(L)&=\sinh(L/2)-L/2.
\end{aligned}
\]

The exact local potential obeys V−Γ−c∞≥β(L). Decompose f=a+g on [0,L], a=L⁻¹∫f and ∫g=0; then ||f||²=L|a|²+||g||². The pole bound from complex Young (0<η<1) is

\[
2|C|^2-2|S|^2\ge2(1-\eta) C_0^2|a|^2
-[2(\eta^{-1}-1)\delta_c^2+2s_2]\|g\|^2.
\]

**New improvement:** the exact shifted Legendre logarithmic kernel eigenvalue theorem in discovery/legendre_log_jump_weil.md establishes

\[
\int_0^L\frac{e^{y/2}}{2\sinh y}\int_0^{L-y}|f(x+y)-f(x)|^2\,dx\,dy
\ge \|g\|_2^2
\]
for every L≤1. The previous 0.29 result used only J≥Lw(L)||g||²≈0.57||g||², losing almost half the available low-mode logarithmic energy. This logarithmic Legendre bound is sharp for its 1/(2y) comparison kernel.

Therefore, for all L<log2,

\[
Q[f]\ge B_{\rm mean}(L,\eta)L|a|^2+B_{\rm fluct}(L,\eta)\|g\|^2,
\]
where

\[
B_{\rm mean}=\beta+2(1-\eta)C_0^2/L,\quad
B_{\rm fluct}=\beta+1-2(\eta^{-1}-1)\delta_c^2-2s_2.
\]

At rational endpoint L₀=303/1000, η=1/1000, 256-bit FLINT Arb outward arithmetic rigorously proves

\[
B_{\rm mean}=0.0018470020588768320\ldots>1/1000,
\quad B_{\rm fluct}=0.3936904520130685\ldots>1/1000.
\]

Thus Q[f]≥1/1000||f||² at L₀, and for all shorter support via zero-extension to [0,L₀] (translation invariance; no unsupported monotonicity of B constants).

## Reproduction and boundaries

- Arb certificate: discovery/short_support_legendre_full_weil_arb.py on codex/discovery-workbench.
- **CI SUCCESS:** https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41219128071 , verified head 0091ae6094607e073dfe88c44f58d178126654c1. All named check steps passed.
- General Legendre diagonalization and codim-one obstruction: discovery/legendre_log_jump_weil.md, its own independent Arb CI https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41218903018 .

These are analytic derivations + Arb scalar certifications, not a completed Lean formalization of integral forms. The spectral theorem has an elementary proof: A(x^n)=2H_n x^n−Σ_(k<n)x^(n−1−k)/(k+1), A symmetric and degree-filtered; shifted Legendre polynomials diagonalize A; all meanzero modes have H_n≥1. The jump comparison uses sinh y/y≤cosh y≤exp(y²/2)≤exp(y/2) for 0<y≤1.

**Still open:** prime-inclusive full completed positivity through log2 and beyond; mean/constant Schur coupling at L=0.43; global Weil and RH. Do not interpret the mean-zero sector positivity to 0.43 as full unrestricted positivity.
