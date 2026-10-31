# Higher Hardy-curvature tower: infinite-dimensional Weil Schur certificate up to L=53/100

**2026-10-31. Codex/Discovery2. No RH claim.**

This generalizes the strict all-function completed Weil interval from **L≤49/100** (fourth derivative) to **L≤53/100** (twentieth derivative). The full corrected real-place Gamma tail and indefinite pole are retained, and the exact arithmetic prime comb is empty for L≤0.53<log2. It is an unconditional all-infinite-modes theorem on this specific range, not finite Fourier Galerkin inference.

## 1. An arbitrary-order exact nonnegative Hardy tower

Set \(H(z)=\log\coth(z/2)=2\sum_{j≥0}e^{-(2j+1)z}/(2j+1)\). For every integer r≥1,
\[
H^{(2r)}(z)=2\sum_{j≥0}(2j+1)^{2r-1}e^{-(2j+1)z}>0.
\]
In particular all even derivatives, including the (2R+2)-th Taylor remainder, are positive. Write \(x=L(1/2+t)\), |t|≤1/2. The symmetric Hardy potential \(V_L(x)=[H(x)+H(L-x)]/2\) therefore obeys, for **every** finite R,
\[
\boxed{V_L(x)\ge H(L/2)+\sum_{r=1}^R K_{2r}(L)t^{2r},\quad
K_{2r}(L)=\frac{L^{2r} H^{(2r)}(L/2)}{(2r)!}>0.}
\]
This inequality is valid everywhere in the open interval and requires no assumptions on zeta zeros or numerical matrix entries. The completed gamma tilt satisfies Γ_L(x)≤e^{L/4}−1. Hence for prime-free L≤1, the EXACT completed Weil form has the operator lower bound
\[
\boxed{Q_L[f]\ge
\beta(L)\|f\|²+\sum_{n≥0}H_n|\langle f,e_n\rangle|²
+\sum_{r=1}^R K_{2r}(L)\|t^r f\|²
+2|\langle c,f\rangle|²-2|\langle s,f\rangle|²,}
\]
where β=−log tanh(L/4)−(e^{L/4}−1)−log4π−EulerGamma, c=cosh((x−L/2)/2), s=sinh((x−L/2)/2), and e_n=√((2n+1)/L)P_n(2x/L−1). The exact logarithmic Legendre eigenvalues H_n were independently established in discovery/legendre_log_jump_weil.md, with J_gamma≥J0 since e^{y/2}/(2sinh y)≥1/(2y) for y≤1.

## 2. Exact recurrence: finite low modes + entire infinite high tail

Multiplication by t in normalized Legendre coordinates is the symmetric Jacobi operator
\[
t e_n=\tfrac12(a_{n+1}e_{n+1}+a_ne_{n-1}),\quad
a_n=\frac{n}{\sqrt{(2n-1)(2n+1)}}.
\]
Thus multiplication by t^{2r} has matrix \(M^{2r}\) and bandwidth 2r, with no hidden high-mode edges beyond that range.

For R=10, define the even low subspace E_lo=span{e_0,e_2,...,e_20}, entire even tail E_hi=span{e_22,e_24,...}; and the odd low O_lo=span{e_1,e_3,...,e_19}, entire odd tail O_hi=span{e_21,e_23,...}. EXACT low/high coupling from the polynomial tower reaches only even high indices 22,24,...,40 and odd high 21,23,...,39. The whole residual high-to-high polynomial contribution is nonnegative and can be **dropped for a lower bound**; the logarithmic Legendre stiffness there is ≥H_22 (even) or H_21 (odd).

The positive cosh pole is retained through its exact projections c0,c2:
\[
c_0=\frac{4\sinh(L/4)}{\sqrt L},
\quad c_2=\sqrt{5L}\left[\frac{4\sinh(L/4)}L-\frac{48\cosh(L/4)}{L²}+\frac{192\sinh(L/4)}{L³}\right].
\]
All components n≥4 have squared norm ≤U_c=L[((L/4)^4 cosh(L/4)/24)]², by subtracting the degree-two cosh Taylor polynomial, which lies in span{e0,e2}. For η=10^-5, a Young square yields an exact positive pole low block \(2(1−η)(c0,c2,0,\dots)^*(c0,c2,0,\dots)\) and a rigorously negative *tail* contact \(-2(η^{-1}−1)U_c\) on every even n≥4. This is an analytic inequality on the full infinite tail, not a finite projection assumption.

The odd sinh pole is genuinely negative; retain its correct sign by \(-2|\langle s,f_{\rm odd}\rangle|²≥-2S_2\|f_{\rm odd}\|²\), \(S_2=\sinh(L/2)-L/2\). Even/odd sectors are exactly uncoupled by reflection symmetry.

Construct real symmetric low matrices
\[
E_{ij}=(\beta+H_i-p_i)\delta_{ij}+\sum_{r=1}^{10}K_{2r}(M^{2r})_{ij}
+2(1-\eta)c_ic_j,\qquad i,j\in\{0,2,\ldots,20\}
\]
with p0=p2=0, p_i=2(η^-1−1)U_c for i≥4, c_i=0 for i≥4; and
\[
O_{ij}=(\beta+H_i-2S_2)\delta_{ij}+\sum_{r=1}^{10}K_{2r}(M^{2r})_{ij},
\qquad i,j\in\{1,3,\ldots,19\}.
\]
Let Ce,Co be the exact 11×10 and 10×10 low/high coupling matrices from the same finite-band polynomial tower. Let
\[
h_e=\beta+H_{22}-2(\eta^{-1}-1)U_c,\qquad
h_o=\beta+H_{21}-2S_2.
\]
For any κ>0, the EXACT all-function sufficient conditions are
\[
h_e,h_o>\kappa,\qquad
\boxed{E-\kappa I-\frac{C_eC_e^T}{h_e-\kappa}>0,\quad
O-\kappa I-\frac{C_oC_o^T}{h_o-\kappa}>0.}
\]
These are only 11×11 and 10×10 **interval-certifiable** matrices, yet by completing the square against the full infinite high-mode Hilbert spaces, their positivity proves Q_L≥κ||f||² on the full form domain, not just those 21 low modes.

## 3. All derivative coefficients evaluated without numerical differentiation

For x=e^{-L}, and m≥0,
\[
\sum_{j\ge0}(2j+1)^m x^j=\frac{P_m(x)}{(1-x)^{m+1}},
\]
where P0=1 and the EXACT integer-polynomial recurrence is
\[
P_{m+1}(x)=[1+(2m+1)x]P_m(x)+2x(1-x)P_m'(x).
\]
Consequently for r≥1,
\[
\boxed{H^{(2r)}(L/2)
= \frac{2e^{-L/2}P_{2r-1}(e^{-L})}{(1-e^{-L})^{2r}}.}
\]
Every coefficient in the automated certificate is therefore built from EXACT integer polynomial arithmetic, exact rational L, Arb exp/log/sinh/cosh and Arb square roots. No finite-difference derivative approximation, sampled high mode or manufactured contact appears.

## 4. Strict endpoint certificate

At L=53/100, R=10, η=1/100000, κ=1/10000, the script discovery/arb_full_weil_hardy_tower_53_100.py constructs the actual 256-bit outward FLINT/Arb low Schur matrices, applies the exact finite-band high coupling and certifies every real symmetric LDL pivot strictly >0. All \(K_{2r}>0\), \(h_e>\kappa\), \(h_o>\kappa\) are asserted. The resulting theorem is

\[
\boxed{\text{For all admissible complex } f \text{ supported in any interval length }\le 53/100,\quad
Q[f]\ge10^{-4}\|f\|².}
\]

Extension to every shorter L uses translation and zero extension into the FIXED ambient 0.53 interval; the completed distribution depends only on autocorrelation. No unproved monotonicity in L or unjustified finite Galerkin limit enters.

The certificate is strongest here because it retains ten positive Hardy curvature orders, including strong endpoint contributions that lower-order methods discard. It still does not cross log2. The next objective is the genuine p=2 activation and a noncircular completed prime/gamma/pole one-sided Schur estimate across its threshold, then the global Weil form and RH. The shifted-zeta Fθ control remains a mandatory falsifier.
