# Full completed Weil positivity to L=49/100 via quartic Hardy–Legendre Schur

**2026-10-31, Codex / GPPDiscovery2.** This extends the exact prime-free, all-test-function completed Weil window from 9/20=0.45 to **49/100=0.49**. The true pole, gamma tail and all logarithmic modes are included. Since 0.49<log2 there are no active prime powers, so this is NOT an RH proof.

## A. Universal exact lower supplier

For the actual corrected v34 completed semilocal Weil form, for any complex f supported in [0,L] with 0<L<log2,

\[
Q_L[f]=\int_0^L(V_L-\Gamma_L-c_\infty)|f|^2dx+J_\gamma[f]
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2.
\]

Definitions: \(H(z)=\log\coth(z/2)\), \(V_L(x)=[H(x)+H(L-x)]/2\), \(\Gamma_L(x)=\int_0^x r+\int_0^{L-x}r\), \(r(y)=(e^{y/2}-1)/(2\sinh y)\), \(c_\infty=\log(4\pi)+\gamma_E\), \(c(x)=\cosh((x-L/2)/2)\), \(s(x)=\sinh((x-L/2)/2)\), and \(J_\gamma\) the exact completed positive interior jump with kernel \(e^{y/2}/(2\sinh y)\).

Set \(t=(x-L/2)/L\). For 0<x<L, \(H(z)=2\sum_{j\ge0}e^{-(2j+1)z}/(2j+1)\); all even derivatives are strictly positive. Taylor about z=L/2 and average \(H(z+Lt)+H(z-Lt)\) to fourth order, the sixth-order remainder is nonnegative. Hence

\[
V_L(x)\ge H(L/2)+K_2t^2+K_4t^4,
\quad K_2=\frac{L^2}{2}\frac{\cosh(L/2)}{\sinh^2(L/2)},\quad
K_4=\frac{L^4}{24}\frac{\cosh(L/2)(\cosh^2(L/2)+5)}{\sinh^4(L/2)}.
\]

The exact tilt obeys \(\Gamma_L\le e^{L/4}-1\), and for L≤1 the completed jump dominates the 1/|x-y| logarithmic Legendre form. With \(\beta=H(L/2)-(e^{L/4}-1)-c_\infty\), we therefore get

\[
Q_L[f]\ge\beta\|f\|^2+\sum_{n\ge0}H_n|\langle f,e_n\rangle|^2
+K_2\|tf\|^2+K_4\|t^2f\|^2
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2,
\]

where \(e_n(x)=\sqrt{(2n+1)/L}P_n(2x/L-1)\), \(H_n=\sum_{j=1}^n1/j\) and \(H_0=0\). The logarithmic Legendre eigenvalue theorem is independently derived in discovery/legendre_log_jump_weil.md; no zeta zeros or RH used.

## B. EXACT finite-to-infinite Legendre Schur, not a Galerkin extrapolation

The normalized three-term recurrence gives \(t e_n=(a_{n+1}e_{n+1}+a_n e_{n-1})/2\), with \(a_n=n/\sqrt{(2n-1)(2n+1)}\), a0=0. Thus t² has |m−n|≤2 and t⁴ has |m−n|≤4, and both preserve reflection parity. Every finite low-to-INFINITE-high coupling is therefore EXACTLY finite rank.

### Even sector: three low modes, infinite tail

Let \(f_+=u_0e_0+u_2e_2+u_4e_4+v\), where v contains *every* even n≥6. The log-kinetic high tail is ≥H6||v||², H6=49/20. The only nonzero low/high multipliers for K2t²+K4t⁴ land at high indices 6,8.

Retain the positive pole without pretending it is diagonal. Put \(\eta=1/100000\), \(c_0=\langle c,e_0\rangle=4\sinh(L/4)/\sqrt L\) and

\[
c_2=\sqrt{5L}\left[\frac{4\sinh(L/4)}L-\frac{48\cosh(L/4)}{L^2}+\frac{192\sinh(L/4)}{L^3}\right].
\]

Taylor of cosh to degree two shows that the squared norm of its entire residual Legendre projection n≥4 is at most

\[
U_c=L\left[\frac{(L/4)^4\cosh(L/4)}{24}\right]^2.
\]

The exact positive pole inequality, valid for arbitrary complex f, is

\[
2|\langle c,f\rangle|^2\ge2(1-\eta)|c_0u_0+c_2u_2|^2
-2(\eta^{-1}-1)U_c\bigl(|u_4|^2+\|v\|^2\bigr).
\]

Let \(T^{(2)}_{mn}=\langle e_m,t^2e_n\rangle\), \(T^{(4)}_{mn}=\langle e_m,t^4e_n\rangle\), calculated EXACTLY by squaring the three-term Jacobi recurrence. Define low index set I+={0,2,4}, high coupling indices J+={6,8}. Let

\[
M_+=\mathrm{diag}(\beta+H_n:n\in I_+)
+K_2T^{(2)}_{I_+,I_+}+K_4T^{(4)}_{I_+,I_+}
+2(1-\eta)(c_0,c_2,0)^*(c_0,c_2,0)
-2(\eta^{-1}-1)U_c\,\mathrm{diag}(0,0,1),
\]
\[
C_+=K_2T^{(2)}_{I_+,J_+}+K_4T^{(4)}_{I_+,J_+},\qquad
h_+=\beta+H_6-2(\eta^{-1}-1)U_c.
\]

For any \(\kappa>0\), if \(h_+>\kappa\) and the explicit symmetric **3×3 real** matrix

\[
\boxed{M_+-\kappa I_3-\frac{C_+C_+^\mathsf T}{h_+-\kappa}}
\]

is positive definite, then the ENTIRE INFINITE even quadratic form Q+ is ≥κ||f+||², because the exact mixed term is completed against the norm-bound high block. Nothing is assumed about convergence of positive finite compressions.

### Odd sector: two low modes, infinite tail

Take \(f_-=u_1e_1+u_3e_3+v\), v containing all odd n≥5. The cosh pole vanishes; the true negative sinh pole is retained through its global exact squared-norm \(\|s\|²=\sinh(L/2)-L/2\), so \(-2|\langle s,f_-\rangle|²\ge-2\|s\|²\|f_-\|²\).

Let I−={1,3}, J−={5,7}, and

\[
M_-=\mathrm{diag}(\beta+H_n-2\|s\|²:n\in I_-)
+K_2T^{(2)}_{I_-,I_-}+K_4T^{(4)}_{I_-,I_-},
\]
\[
C_-=K_2T^{(2)}_{I_-,J_-}+K_4T^{(4)}_{I_-,J_-},\quad
h_-=\beta+H_5-2\|s\|²,\quad H_5=137/60.
\]

If \(h_->\kappa\) and \(M_--\kappa I_2-C_-C_-^\mathsf T/(h_--\kappa)\) is positive definite, then Q−≥κ||f−||² on **all infinitely many** odd modes.

This is an exact, complete two-sector Schur sufficient condition. It uses only honest positive and negative terms from the completed Weil form. It will generally FAIL once the prime comb becomes active unless genuine prime contributions are incorporated.

## C. 256-bit Arb endpoint certification

Fix **L=49/100=.49**, \(\eta=1/100000\), \(\kappa=1/1000\). In the accompanying script discovery/arb_full_weil_legendre_schur_49_100.py, all coefficients are built as Arb intervals from exact rational endpoints, π, Euler's constant, log/sinh/cosh and the finite Jacobi recurrence. No numerical eigenvalues are trusted; strict positivity is established by outward-rounded interval LDL pivots of the **Schur matrices**.

Preliminary independent numeric approximation (not the certificate):
- even high \(h_+\approx1.3160611\), odd high \(h_-\approx1.1444864\);
- even effective 3×3 matrix after \(\kappa I\): its smallest ordinary eigenvalue ≈0.00311339, first LDL pivot ≈0.06826795, next ≈0.04916138, last ≈0.91242484;
- odd effective 2×2 after \(\kappa I\): smallest ≈0.218817.

The strict Arb signs establish for **every** complex form-domain test f on length L=49/100:

\[
\boxed{Q_L[f]\ge \frac1{1000}\|f\|_2^2.}
\]

For every shorter interval, translate and zero extend f into the **fixed** L=49/100 ambient support; the completed Weil quadratic form depends only on autocorrelation, so both Q and the L² norm are preserved.

**Boundary:** 49/100<log2, no prime powers. This is stronger prime-free completed positivity than previous L≤9/20, L≤43/100, and no evidence of RH by itself. The first activation of p=2 is at L=log2; crossing it in a completed-form theorem, not merely proving E−S≥0, remains the principal objective. The exact finite-range prime shifts are bounded by weighted Hardy-Schur SOS, but require a moment-aware Schur that protects the even low eigenvalues.
