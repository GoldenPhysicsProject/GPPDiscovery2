# All-function completed Weil positivity to L=9/20 via Legendre finite-rank Schur

**2026-10-31, Codex / Discovery2.** This extends the previous unconditional full completed no-prime Weil result L≤209/500=0.418 to **L≤9/20=0.45**, using the exact full-tail-corrected v34 Weil quadratic form. The prime comb is exactly empty because 9/20<log 2. All complex test functions in the logarithmic kinetic form domain are covered; this is **not** finite Fourier Galerkin positivity and **not RH**.

## 1. Exact completed decomposition and curvature supplier

On [0,L], with no prime atoms, the already verified decomposition is

\[
Q[f]=\int_0^L [V_L(x)-\Gamma_L(x)-c_\infty]|f|^2dx+J_\gamma[f]
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2,
\]
where \(c_\infty=\log(4\pi)+\gamma_E\), \(H(z)=\log\coth(z/2)\), \(V_L(x)=[H(x)+H(L-x)]/2\), \(\Gamma_L(x)=R(x)+R(L-x)\), \(R'(y)=(e^{y/2}-1)/(2\sinh y)\), \(c(x)=\cosh((x-L/2)/2)\), \(s(x)=\sinh((x-L/2)/2)\), and \(J_\gamma\) is the true positive interior jump energy with weight \(e^{y/2}/(2\sinh y)\). For L≤1, \(J_\gamma\ge J_0\), whose exact normalized shifted-Legendre eigenvalues are harmonic numbers \(H_n\). This follows from the self-adjoint log-kernel polynomial identity in discovery/legendre_log_jump_weil.md; no RH input.

Write \(t=(x-L/2)/L\in[-1/2,1/2]\). By the positive odd-exponential series for \(H\), \(H''''>0\), so \(H''\) is convex. Consequently \(V_L''(x)\ge H''(L/2)\), and symmetry forces \(V_L'(L/2)=0\). Thus
\[
V_L(x)\ge H(L/2)+K t^2,\quad
K=\tfrac{L^2}{2}H''(L/2)
=\tfrac{L^2}{2}\frac{\cosh(L/2)}{\sinh^2(L/2)}.
\]
The tilt satisfies \(\Gamma_L(x)\le e^{L/4}-1\). Put
\[
\beta=-\log\tanh(L/4)-(e^{L/4}-1)-c_\infty.
\]
Then the full quadratic form is bounded below by
\[
\boxed{Q[f]\ge \beta\|f\|^2+J_0[f]+K\|tf\|^2
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2.}
\]

## 2. Sharp low-mode and tail geometry in the LEGENDRE basis

Use normalized shifted Legendre \(e_n(x)=\sqrt{(2n+1)/L}P_n(2x/L-1)\), so \(J_0[e_n]=H_n\), \(H_0=0\). Reflection about L/2 separates even n and odd n exactly; no even-odd coupling. Define
\[
a_n=\frac{n}{\sqrt{(2n-1)(2n+1)}},\quad a_0=0.
\]
Then multiplication by t² has a TRIDIAGONAL-by-parity matrix:
\[
\langle e_n,t^2e_n\rangle=\tfrac14(a_n^2+a_{n+1}^2),\qquad
\langle e_n,t^2e_{n+2}\rangle=\tfrac14a_{n+1}a_{n+2}.
\]
This is the exact Legendre three-term recurrence applied twice, not a numerical fitting procedure.

### Even sector, all infinitely many modes

Split any even f=u0 e0+u2 e2+v, with \(v\perp e_0,e_2\) and containing all even n≥4. Thus \(J_0[v]\ge H_4\|v\|²=(25/12)\|v\|²\). The ONLY curvature low-to-high cross term is between e2 and e4, of strength \(K T_{24}\), where \(T_{24}=a_3a_4/4\); no other low/high curvature couplings exist.

Let \(c_j=\langle c,e_j\rangle\) for j=0,2 and \(\eta=1/100000\). The exact low projections are
\[
c_0=4\sinh(L/4)/\sqrt L,\qquad
c_2=\sqrt{5L}\left[\frac{4\sinh(L/4)}{L}
-\frac{48\cosh(L/4)}{L^2}
+\frac{192\sinh(L/4)}{L^3}\right].
\]
Taylor's theorem \(\cosh z=1+z²/2+R_4(z)\), \(|R_4(z)|\le |z|^4\cosh(|z|)/24\), and \(\operatorname{span}\{e_0,e_2\}=\operatorname{span}\{1,t^2\}\) give the rigorous all-mode tail estimate
\[
\|P_{\mathrm{even},n\ge4}c\|²\le U_c
=L\left[\frac{(L/4)^4\cosh(L/4)}{24}\right]^2.
\]
Young's inequality applied to the **actual positive cosh pole** (not dropped or assumed diagonal) gives
\[
2|\langle c,f\rangle|²\ge
2(1-\eta)|c_0u_0+c_2u_2|²
-2(\eta^{-1}-1)U_c\|v\|².
\]

Set \(T_{00}=1/12\), \(T_{02}=a_1a_2/4\), \(T_{22}=(a_2²+a_3²)/4\).
The complete even form is bounded from below by a two-dimensional low matrix with
\[
A=\beta+K T_{00}+2(1-\eta)c_0²,\quad
B=\beta+3/2+K T_{22}+2(1-\eta)c_2²,\quad
C=K T_{02}+2(1-\eta)c_0c_2,
\]
and an infinite high block \(h_e I\) where
\[
h_e=\beta+25/12-2(\eta^{-1}-1)U_c.
\]
Only the curvature edge e2↔e4 couples them. For any target \(\kappa>0\), a genuinely INFINITE-dimensional exact Schur sufficient condition is
\[
h_e>\kappa,\quad A>\kappa,\quad
\boxed{(A-\kappa)\left[B-\kappa-\frac{(K T_{24})²}{h_e-\kappa}\right]>C².}
\]
No unsummed tail, cross term, or pole contact is omitted.

### Odd sector, all infinitely many modes

Split o=u1 e1+v_odd with only odd n≥3 in its tail. \(J_0[v_{\rm odd}]\ge H_3\|v_{\rm odd}\|²=11/6\|v_{\rm odd}\|²\). The sine pole is truly NEGATIVE; bound it from below by \(-2\|s\|²\|o\|²\) where the exact \(\|s\|²=\sinh(L/2)-L/2\). The only odd low/high curvature edge is e1↔e3 with coefficient \(KT_{13}=K a_2a_3/4\). Define
\[
A_o=\beta+1+K(a_1²+a_2²)/4-2\|s\|²,\quad
h_o=\beta+11/6-2\|s\|².
\]
A sufficient all-odd-modes condition is
\[
\boxed{h_o>\kappa,\quad A_o-\kappa>\frac{(K T_{13})²}{h_o-\kappa}.}
\]
The positive cosh pole is zero on odd functions. This retains the correct sign of the negative pole sector.

## 3. Concrete OUTWARD interval endpoint

Take **L=9/20=0.45**, \(\eta=1/100000\), \(\kappa=1/2000=0.0005\). The symbolic exact inequalities above are evaluated at 256-bit FLINT/Arb in discovery/arb_full_weil_legendre_schur_9_20.py.

Expected approximate intermediary values, provided only for orientation (CI gives the rigorous intervals):
- \(h_e\approx1.0450254976038\);
- \(A\approx0.0335386939657\), \(B\approx0.7257752075\), \(C\approx0.1520100171\);
- \(B-\kappa-(K T_{24})²/(h_e-\kappa)\approx0.70938442827\);
- **even Schur determinant after \(\kappa I\)** approximately \(0.0003300897406>0\);
- **odd Schur residual after \(\kappa I\)** approximately \(0.237835631975>0\).

Thus both infinite even and odd sector bounds are strictly positive, and
\[
\boxed{Q[f]\ge(1/2000)\|f\|²\quad\text{for all f supported in any interval of length } L\le9/20.}
\]

All shorter supports follow by zero extension into the *fixed ambient* 9/20 window, preserving the corrected completed distribution's dependence on autocorrelation; no questionable monotonicity in L is used.

**Crucial scope:** This is still prime-free since \(9/20<\log2\). In particular it does NOT prove the full completed prime-inclusive Weil positivity through log2, let alone all cofinal windows or RH. The novelty relative to the earlier L≤209/500 result is an exact low-mode/tail Schur completion in Legendre space, including the true even positive pole tail and the true odd negative pole, rather than discarding the positive \(K\|t g\|²\) contribution. The next target is adding the p=2 shift as an explicit finite-range signed perturbation at activation, using the weighted Hardy-Schur and exact prime Fock source already developed.
