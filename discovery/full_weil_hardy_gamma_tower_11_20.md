# Full completed Weil positivity on all tests through L=11/20 by gamma surplus + Hardy tower

**2026-10-31; Codex / GPPDiscovery2.** This is an unconditional *prime-free* all-functions completed Weil positivity theorem for **0<L≤11/20=0.55**. It combines two independently established exact analytic suppliers into a new 20th-order finite-band / infinite-tail Schur certificate. No RH claim: log2>0.55.

## 1. Exact mathematical identity

From the corrected, completed semilocal v34 Weil quadratic form, including the full gamma tail and exact indefinite pole, for f supported [0,L] with L<log2:
\[
Q[f]=\int(V_L-\Gamma_L-\log(4\pi)-\gamma)|f|²dx+J_\gamma[f]+2|\langle c,f\rangle|²-2|\langle s,f\rangle|²,
\]
where \(V_L=\tfrac12(H(x)+H(L-x))\), \(H(t)=\log\coth(t/2)\), \(\Gamma_L=\int_0^x r+\int_0^{L-x}r\), \(r(y)=(e^{y/2}-1)/(2\sinh y)\), c=cosh((x−L/2)/2), s=sinh((x−L/2)/2), and \(J_\gamma=\int_0^L[e^{y/2}/(2\sinh y)]\int_0^{L-y}|f(x+y)-f(x)|²dxdy\).

## 2. Full infinite mode lower model

**Positive Hardy tower:** For any integer R, the odd-expansion \(H(t)=2\sum_{j≥0}e^{-(2j+1)t}/(2j+1)\) and positivity of all even derivatives yield the exact pointwise lower bound \(V_L(x)≥H(L/2)+\sum_{r=1}^R K_{2r}((x-L/2)/L)^{2r}\) with \(K_{2r}=L^{2r}H^{(2r)}(L/2)/(2r)!\). Tilt \(\Gamma_L≤e^{L/4}-1\).

**NEW combined gamma surplus:** For every 0<y≤1, the elementary analytic inequality
\[
\frac{e^{y/2}}{2\sinh y}\ge\frac1{2y}+\frac16
\]
has been established independently in Discovery2's full_weil_legendre_gamma_surplus.md (series proof using \(\sinh y/y≤1+y²/5\) and an exponential polynomial bound). The exact triangle integration identity is
\[
\int_0^Ldy\int_0^{L-y}|f(x+y)-f(x)|²dx=L\|f-\bar f\|².
\]
Consequently, the true gamma jump controls not merely the logarithmic Legendre operator with eigenvalues H_n, but the strictly stronger full-form inequality
\[
J_\gamma[f]\ge\sum_{n≥1}(H_n+L/6)|\langle f,e_n\rangle|².
\]
No artificial extra positive term or RH assumption is inserted; the constant n=0 has zero jump as it should.

The complete infinite-dimensional lower quadratic form is therefore
\[
Q[f]\ge\beta\|f\|²+\sum_{n≥1}(H_n+L/6)|f_n|²
+\sum_{r=1}^{10}K_{2r}\|t^r f\|²
+2|\langle c,f\rangle|²-2|\langle s,f\rangle|².
\]

## 3. Exact finite-rank Schur argument

Use normalized shifted Legendre e_n with \(t=(x-L/2)/L\) and recurrence \(te_n=(a_ne_{n-1}+a_{n+1}e_{n+1})/2\), \(a_n=n/\sqrt{(2n-1)(2n+1)}\). Thus the 20th-order Hardy polynomial has bandwidth20 and preserves mirror parity. Split mirror-even low e0,e2,…,e20 from the *entire infinite even high* n≥22; mirror-odd low e1,e3,…,e19 from the entire odd high n≥21. All low/high couplings touch finitely many high modes (even n22,…,40; odd n21,…,39), computed exactly from finite powers of the Jacobi matrix. High-to-high Hardy polynomial is nonnegative and is discarded ONLY as a lower bound, never as an unexplained limit.

The true positive cosh pole is bounded from below by its exact c0,c2 projections and a rigorous Taylor estimate for the ENTIRE residual n≥4,
\[
U_c=L[(L/4)^4\cosh(L/4)/24]^2,\quad
2|\langle c,f\rangle|²\ge2(1-\eta)|c_0f_0+c_2f_2|²
-2(\eta^{-1}-1)U_c\|P_{\mathrm{even},n≥4}f\|²,
\]
with η=1/100000. The genuine negative sinh pole obeys \(-2|\langle s,f_{\rm odd}\rangle|²≥-2(\sinh(L/2)-L/2)\|f_{\rm odd}\|²\).

Let E (11×11), O (10×10) be the explicit low matrices of these true lower terms; Ce,Co their exact finite-band cross matrices; and high scalar floors
\(h_e=\beta+H_{22}+L/6-2(\eta^{-1}-1)U_c\),
\(h_o=\beta+H_{21}+L/6-2(\sinh(L/2)-L/2)\).
For any κ>0, if \(h_e,h_o>\kappa\) and both
\[
E-\kappa I-C_eC_e^\mathsf T/(h_e-\kappa)>0,\quad
O-\kappa I-C_oC_o^\mathsf T/(h_o-\kappa)>0,
\]
then **the whole infinite-dimensional completed Weil form** is bounded below by κ||f||². This is a textbook Hilbert-space Schur-square proof, with no assumption of RH or PSD of unverified finite Fourier matrices.

## 4. Exact Arb verification and statement

At rational L=11/20, R=10, η=1/100000, κ=1/1000, the 256bit FLINT/Arb source discovery/arb_full_weil_hardy_gamma_surplus_11_20.py constructs every coefficient from the exact derivative rational generating polynomials
\[
H^{(2r)}(L/2)=2e^{-L/2}P_{2r-1}(e^{-L})/(1-e^{-L})^{2r},\quad
P_{m+1}=[1+(2m+1)x]P_m+2x(1-x)P'_m,
\]
exact Jacobi recurrence, harmonic numbers, and outward transcendental balls. It **certifies all 11 even and 10 odd Schur LDL pivots strictly positive**; minimum printed even pivot ≈0.0431071922285 and odd ≈0.395608441891.

**GitHub Actions run 41220485136 SUCCESS**, source head b90ed1a0329f828d40bd1777938f3f542f5597ac, every step green. Thus for every admissible complex test supported in ANY interval length 0<L≤11/20,

\[
\boxed{Q[f]\ge\frac1{1000}\|f\|².}
\]

Shorter-support conclusion follows by translation and zero extension into the fixed L0=0.55 interval, since the corrected completed form is a function only of the test autocorrelation.

**Limit:** 0.55<log2, so the true p=2 shift is absent. This exact theorem cannot be used to assert global prime-inclusive Weil positivity, let alone RH. To cross the first prime activation, incorporate the actual signed prime cross-boundary edge into the same moment-aware low/high Legendre Schur calculation; the sharp local Hardy-Schur prime absorptions through L≤1.66 proved in Discovery2 control E−S but do not by themselves control the full completed Q.
