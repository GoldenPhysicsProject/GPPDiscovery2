# Unconditional full completed Weil positivity through L = 69/200 by a mean/Legendre Schur bound

**2026-10-31 — Codex / Discovery2 — exact analytic theorem with outward Arb endpoint verification.**

This improves the all-function complete (prime-free) Weil positivity window L≤303/1000 to **L≤69/200=0.345**, and addresses the missing constant-to-even-fluctuation coupling as an actual one-sided Schur inequality. No RH claim: 0.345<log2, hence no prime atom has entered. The statement uses the *corrected*, tail-complete v34 semilocal Weil quadratic form.

## Theorem

For any complex test f supported on any interval of logarithmic length at most 69/200 and lying in the completed logarithmic form domain,

\[
\boxed{Q[f] \ge \frac1{1000}\|f\|_{L^2}^2.}
\]

The inequality applies to *all* Fourier modes, including the constant and both reflection parities, not to a finite Galerkin truncation.

## 1. Exact completed form and logarithmic Legendre supplier

On [0,L] with L=69/200, write
\[
Q_L[f]=\int_0^L F_{\rm loc}(x)|f(x)|^2dx+J_\gamma[f]+2|C_f|^2-2|S_f|^2,
\]
where \(c_\infty=\log(4\pi)+\gamma_E\),
\[
F_{\rm loc}(x)=V_L(x)-\Gamma_L(x)-c_\infty,\quad
V_L(x)=\tfrac12[H(x)+H(L-x)],\quad H(z)=\log\coth(z/2),
\]
\[
\Gamma_L(x)=R(x)+R(L-x),\quad R(z)=\int_0^z\frac{e^{y/2}-1}{2\sinh y}\,dy,
\]
\[
J_\gamma[f]=\int_0^L\frac{e^{y/2}}{2\sinh y}\int_0^{L-y}|f(x+y)-f(x)|^2\,dx\,dy,
\]
\[
C_f=\int_0^L f(x)\cosh((x-L/2)/2)\,dx,\qquad S_f=\int_0^L f(x)\sinh((x-L/2)/2)\,dx.
\]
All terms arise from the exact completed Weil form and its Archimedean tail. No prime terms because e^L<2.

The logarithmic Legendre theorem already proved algebraically in discovery/legendre_log_jump_weil.md gives \(J_\gamma[g]\ge \tfrac32\|g\|^2\) for reflection-even mean-zero g, and \(J_\gamma[o]\ge\|o\|^2\) for reflection-odd o. The kernel \(e^{y/2}/(2\sinh y)\ge1/(2y)\) when y≤L≤1. The exact form commutes with reflection about L/2, so the constant couples *only* to even mean-zero g, not to odd o.

Set \(\beta(L)=H(L/2)-(e^{L/4}-1)-c_\infty\), \(C_0=4\sinh(L/4)\), and \(s_2=\sinh(L/2)-L/2\). Then
\[
Q[o]\ge [\beta(L)+1-2s_2]\|o\|^2=:\gamma_o\|o\|^2,\qquad
Q[g]\ge [\beta(L)+3/2]\|g\|^2=:\gamma_e\|g\|^2.
\]

## 2. Exact constant-to-even coupling

Let \(e_0(x)=L^{-1/2}\) and \(f=z e_0+g+o\), \(\int g=0\) even, o odd. The physical completed operator applied to e0 is
\[
(Qe_0)(x)=L^{-1/2}F(x),\qquad
F(x)=V_L(x)-\Gamma_L(x)-c_\infty+2C_0\cosh((x-L/2)/2).
\]
The gamma interior jump annihilates constants, and the sine pole vanishes on e0. Let
\[
m=L^{-1}\int_0^L F(x)\,dx,\quad
b=L^{-1/2}(F-m)\in e_0^\perp,
\qquad \|b\|^2=\operatorname{Var}_{t\in[0,1]}F(Lt).
\]
Then the even block, including the exact off-diagonal constant coupling, obeys
\[
Q[z e_0+g]\ge m|z|^2-2|z|\|b\|\|g\|+\gamma_e\|g\|^2.
\]
No cross terms with o exist.

## 3. Elementary analytic bounds on m and the **variance** of b

Write t=x/L. For all z>0,
\[
H(z)=\log(2/z)+\rho(z),\quad
0\le\rho(z)=\log[(z/2)\coth(z/2)]\le z^2/12.
\]
The upper bound follows from the classical partial fractions \(u\coth u=1+2u^2\sum_{n\ge1}(u^2+\pi^2n^2)^{-1}\le1+u^2/3\) and \(\log(1+w)\le w\); the lower bound follows from \(\tanh u\le u\).

For 0≤y≤L=69/200, the gamma tilt satisfies
\[
\frac14\le r(y)=\frac{e^{y/2}-1}{2\sinh y}
=\frac{e^{y/4}}{4\cosh(y/4)\cosh(y/2)}
\le\frac{e^{y/4}}4.
\]
For the lower bound put u=e^{y/2}∈[1,2]. Then \(4r(y)\ge1\) is equivalent to \(4u^2-(u+1)(u^2+1)=-(u-1)(u^2-2u-1)\ge0\) for 1≤u≤2. The endpoint u<2 is immediate from L≤69/200.

Consequently \(L/4\le\Gamma_L(x)\le L e^{L/4}/4\). Define
\[
A=\frac L4(e^{L/4}-1),\quad
B=\frac{L^2}{24}+2C_0(\cosh(L/4)-1),
\quad
C_{\rm base}=\log(2/L)-c_\infty+2C_0-L/4.
\]
The exact source function decomposes as
\[
F(Lt)=C_{\rm base}+\underbrace{-\tfrac12\log[t(1-t)]}_{v_0(t)}+\delta(t)
\]
where \(-A\le\delta(t)\le B\) on 0<t<1.

Now the *exact* beta-function identities give
\[
\int_0^1v_0(t)\,dt=1,\quad
\operatorname{Var}_{[0,1]}v_0=1-\frac{\pi^2}{12}.
\]
Indeed, the standard Euler integrals are \(\int_0^1\log^2t\,dt=2\) and \(\int_0^1\log t\log(1-t)dt=2-\pi^2/6\).
By Popoviciu's inequality (or elementary interval centering), \(\sqrt{\operatorname{Var}\delta}\le(A+B)/2\). The \(L^2\) triangle inequality applied to centered v0 and delta then yields
\[
\boxed{m\ge m_*:=\log(2/L)-c_\infty+2C_0-L/4+1-A,}
\]
\[
\boxed{\|b\|^2\le D_*:=\left(\sqrt{1-\pi^2/12}+\frac{A+B}{2}\right)^2.}
\]

## 4. A **genuine strict one-sided Schur certificate**, not a numerical Gram extrapolation

Let κ=1/1000. A sufficient exact condition for all-function completed Weil positivity with this margin is

\[
\gamma_o>\kappa,\qquad
\gamma_e>\kappa,\qquad
m_*-\kappa-\frac{D_*}{\gamma_e-\kappa}>0.
\]

This follows by completing the square in the EVEN constant-to-fluctuation block and adding the completely decoupled ODD block:
\[
Q[f]-\kappa\|f\|^2\ge
\left(m_*-\kappa-\frac{D_*}{\gamma_e-\kappa}\right)|z|^2+
(\gamma_e-\kappa)\left(\|g\|-\frac{\sqrt{D_*}}{\gamma_e-\kappa}|z|\right)^2
+(\gamma_o-\kappa)\|o\|^2.
\]
The exact scalar quantities at L=69/200 are all explicit combinations of rationals, π, Euler's γ, log, exp, sinh/cosh and tanh. They are checked with outward FLINT/Arb balls at **256-bit** precision in discovery/arb_full_weil_mean_schur_69_200.py. The Schur residual is about **0.00076283406857**, strictly positive. Unlike previous mean/variance Young bounds, this square completion uses the *actual small variance* of the center-to-boundary potential and the stronger parity-even Legendre spectral gap 3/2. The result improves the previous unrestricted endpoint 303/1000 by approximately 13.86%.

For every shorter support L'<L, zero extend and translate f into the fixed ambient interval [0,L]. The completed Weil distribution depends only on autocorrelations \(q_f\), and hence Q and \(\|f\|_2\) do not change on zero extension. No unsupported monotonicity extrapolation of individual coefficients is needed.

## 5. Scope and immediate next mathematical work

This theorem **does not cross log 2**; primes are absent. The available CI-certified prime-Archimedean kinetic absorption through L≤83/50=1.66 is separate and does not imply full completed Weil positivity because of the signed pole+contact. The present theorem gives a **genuine constant-mode Schur completion** that the previous 0.43 mean-zero result lacked. Extending it to the first prime threshold requires an estimate on the constant-to-even source and on the even mean-zero spectral gap under the weighted prime edges, and retaining the odd-pole negative square. The shifted \(F_\theta\) fake remains an adversarial check on any global attempt.

The exact 41-mode corrected near-null mode at λ=5/2 remains mirror even, and this scalar Schur mechanism is structurally aimed at its low-frequency sector; the present proof is limited to tiny prime-free intervals and does not control the near-null at L=2log(5/2).
