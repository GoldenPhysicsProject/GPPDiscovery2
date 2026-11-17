# Canonical Legendre Schur test and correction of a Weil-form domain error

**2026-11-16; mathematical correction.** An earlier Discovery2 note stated that sharply truncated polynomials are NOT in the logarithmic Weil form domain. THIS IS FALSE. This note corrects it and constructs a simpler finite source matrix. Full Weil positivity, ARP, OB-6 and RH remain open. Nothing here was built in Lean.

## 1. The exact operator domain includes polynomial indicators

Let I=[-L/2,L/2] and extend all I-supported functions by zero. The Archimedean energy has exact Fourier symbol
\[
 a(\lambda)=2\sum_{k\ge0}\frac{\lambda^2}
 {(2k+1/2)((2k+1/2)^2+\lambda^2)}
 =\Re[\psi(1/4+i\lambda/2)-\psi(1/4)]
 =O(\log(2+|\lambda|)).
\]
For any ordinary polynomial p, e=1_I p has Fourier decay
\[
 |\hat e(\lambda)|\le (|p(-L/2)|+|p(L/2)|+\int_I|p'(x)|dx)/|\lambda|
 \quad(|\lambda|\ge1)
\]
by one integration by parts. Therefore
\[
 \int_{\mathbb R}a(\lambda)^2|\hat e(\lambda)|^2 d\lambda<\infty
\]
because log²(lambda)/lambda² is integrable. So **e belongs to the L² operator domain of a(D)**, even though it jumps at both endpoints. The source Weil prime, constant and pole pieces are bounded for every fixed L, so e lies in the completed Weil operator domain too.

For the indicator p=1 the energy is explicitly finite:
\[
 \|1_I-T_t1_I\|^2=2\min(t,L),\qquad
 E_\infty(1_I)=2\int_0^\infty w(t)\min(t,L)dt<\infty,
\]
as w(t)~1/(2t) near zero and w decays exponentially. This directly refutes the earlier assertion. Sharp cutoff functions would be excluded by a stronger fractional derivative, but NOT by the Weil logarithmic symbol.

The original test functions for ARP are smooth compactly supported. The logarithmic operator/form on L²(I) is their closure; approximating polynomial indicators in H^s for any 0<s<1/2 suffices, since a(lambda)² ≤ C_s(1+|lambda|^{2s}). Standard H^s zero-boundary density for s<1/2 (or explicit boundary-layer cutoffs) shows these polynomial indicators belong to that closure.

## 2. Canonical orthonormal Legendre moments

Set
\[
 e_j(x)=1_I(x)\sqrt{(2j+1)/L}\,P_j(2x/L),\qquad j=0,\ldots,N-1,
\]
where P_j are the standard Legendre polynomials. The e_j are L²(I)-orthonormal, and each lies in the completed source Weil operator domain by §1. Let P be their orthogonal projector, Q=I-P. The Q-space consists EXACTLY of the zero-first-N-moment functions; by the previous high-frequency lemma its closed Weil form obeys W(h)≥δ||h||² for some explicitly chosen δ>0, depending on L,N.

Let A_L be the genuine (gamma + signed pole + prime powers) localized source Weil operator. Define two FINITE real symmetric source matrices
\[
 F_{ij}=\langle e_i,A_L e_j\rangle,\qquad
 H_{ij}=\langle A_L e_i,A_L e_j\rangle.
\]
The off-diagonal leakage B=Q A_L P has columns b_j=Q A_L e_j. Orthonormality gives the exact SPECTRAL VARIANCE identity
\[
 \boxed{Z_{ij}=\langle b_i,b_j\rangle,\qquad Z=H-F^2\succeq0.}\tag{1}
\]
No arbitrary smooth bumps, ill-conditioned raw moment Gram inverses or discontinuous-function domain errors.

For f=∑μ_j e_j +h with h∈Q and W(h)≥δ||h||²,
\[
 W(f)\ge \mu^\mathsf{T}[F-\delta^{-1}(H-F^2)]\mu+
 \delta\left\|h+\delta^{-1}\sum_j\mu_jb_j\right\|^2.
\]
Hence
\[
 \boxed{F-\delta^{-1}(H-F^2)\succeq0
        \ \Longrightarrow\ W_L(f)\ge0\quad\forall f\in C_c^\infty(I).}\tag{2}
\]
This is a rigorously derived FINITE SUFFICIENT TEST, not an established positive matrix. The exact necessary-and-sufficient Schur formula uses the positive high-sector inverse D^-1 instead of δ^-1 I. F and H contain the true arithmetic Weil coefficients. The leakage variance H-F² is precisely the measurable obstruction to reducing positivity to the finite low-moment block F alone.

The projected operator on the polynomials is explicit:
\[
 A_L\phi=1_I a(D)\phi+C_\infty\phi
 +e^{x/2}\langle e^{-x/2},\phi\rangle
 +e^{-x/2}\langle e^{x/2},\phi\rangle
 -1_I\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
    [\phi(x-\log n)+\phi(x+\log n)].
\]
Endpoint jumps cause no divergence for its a(D) term.

## 3. Audit / formalization targets

A 5x5 exact rational toy audit is in experiments/abel_prime_common_map/verify_legendre_variance_schur.py. It is NOT an RH certificate. Verify should formalize:
- Fourier decay O(1/|lambda|) of interval polynomial indicators and log-multiplier L²-domain inclusion.
- For finite-rank orthogonal P and selfadjoint A, the identity P A (I-P) A P = P A² P - (P A P)² on P's range (domain assumptions explicit).
- Completing the square with a positive high sector ≥δ.
- The exact source operator and finite matrix in the polynomial basis, preserving the F_theta negative control.

**RETRACTION:** Earlier instructions in prime_graph_parity_smooth_moment_schur_2026_11_16.md and an earlier GPP-bridge comment said that indicator-cutoff polynomials were excluded from the logarithmic form domain. That is mathematically incorrect; use this corrected note and the explicit box-energy integral. No Lean compilation claimed.
