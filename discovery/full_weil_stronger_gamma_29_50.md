# Sharper gamma-jump supplier and full completed Weil positivity to L=29/50

**2026-10-31, Codex / Discovery2.** Extends the *full completed* corrected v34 prime-free Weil positivity theorem from L≤11/20=.55 to **L≤29/50=.58**, for every admissible complex test function and every mode. It uses a new purely elementary gamma surplus inequality and the full finite-band twentieth-order Hardy/Legendre Schur of discovery/full_weil_hardy_tower_53_100.md. RH remains unproved and no prime powers activate before L=log2.

## A new strict gamma inequality on an exact support range

For **every real \(0<y\le7/10\)**,
\[
\boxed{\frac{e^{y/2}}{2\sinh y}\ge\frac1{2y}+\frac{11}{50}.}
\]

**Algebraic proof without interval sampling or numerical differentiation.**

First for \(0<y≤1\), the Taylor series \(\sinh y/y=1+y²/3!+\sum_{n≥2}y^{2n}/(2n+1)!\) has positive tail whose successive coefficient ratio is ≤1/42. Therefore
\[
\frac{\sinh y}y\le1+\frac{y²}6+\frac{y⁴}{120}\sum_{k≥0}\frac1{42^k}
=1+\frac{y²}6+\frac{7y⁴}{820}
\le1+\frac{y²}6+\frac{y⁴}{105}.
\]

Second, \(e^{y/2}\ge1+y/2+y²/8+y³/48\). Expand the desired comparison against this *upper* sinh bound:
\[
\begin{aligned}
&e^{y/2}-(1+\tfrac{11}{25}y)\frac{\sinh y}{y}\\
&\quad\ge y\Bigl[\tfrac3{50}-\tfrac{y}{24}-\tfrac{21y²}{400}
-\tfrac{y³}{105}-\tfrac{11y⁴}{2625}\Bigr]\\
&\quad\ge y\Bigl[\tfrac3{50}-\tfrac{7/10}{24}
-\tfrac{21(7/10)²}{400}-\tfrac{(7/10)³}{105}
-\tfrac{11(7/10)^4}{2625}\Bigr]
=\frac{12533}{15000000}y>0.
\end{aligned}
\]
All steps are exact rational inequalities; the bracket decreases on y≥0. Dividing the strict comparison by \(2\sinh y\) proves the boxed gamma surplus bound.

The exact identity
\[
\int_0^Ldy\int_0^{L-y}|f(x+y)-f(x)|²\,dx
=L\|f-\bar f\|²
\]
now gives, for every \(0<L≤7/10\),
\[
\boxed{J_\gamma[f]\ge J_0[f]+\frac{11L}{50}\|f-\bar f\|²
=\sum_{n≥1}(H_n+\tfrac{11L}{50})|f_n|²,}
\]
where \(J_0\) is the 1/|x−y| log-Legendre form and \(H_n\) are harmonic numbers. This strictly improves the earlier established \(+L/6\) meanzero stiffness.

## Application to the ACTUAL completed Weil form

For no-prime L<log2, the exact full gamma/pole/Hardy decomposition reads
\[
Q_L[f]=\int(V_L-\Gamma_L-c_\infty)|f|²dx+J_\gamma[f]
+2|\langle c,f\rangle|²-2|\langle s,f\rangle|².
\]
The infinite positive Hardy tower \(V_L≥H(L/2)+\sum_{r=1}^{10}K_{2r}t^{2r}\) holds by positivity of all even H derivatives. Tilt is bounded above by \(e^{L/4}-1\). In the normalized Legendre basis, multiply by t^{2r} using an exact Jacobi tridiagonal recurrence. Split the even sector into low n=0,2,…,20 and **all infinite even n≥22**; odd sector low n=1,3,…,19 and **all infinite odd n≥21**. The polynomial Hardy tower couples low to only the first ten high positions, and its infinite high-high contribution is nonnegative. The actual positive cosh pole is retained with exact c0,c2 plus a uniform bound on its residual projection n≥4; the actual negative odd sinh pole is bounded by the exact \(\sinh(L/2)-L/2\) moment norm. No fake contact or zero assumption enters.

With the stronger gamma supplier, add \(11L/50\) to every nonconstant Legendre diagonal. The resulting full Hilbert-space Schur sufficient condition remains:
\[
h_e,h_o>\kappa,\quad
E-\kappa I-C_eC_e^\mathsf T/(h_e-\kappa)>0,\quad
O-\kappa I-C_oC_o^\mathsf T/(h_o-\kappa)>0,
\]
where E is 11×11, O is 10×10, both EXACT rational/Arb functions of L and the Hardy polynomial, and Ce,Co include every genuine low/high coupling. The high scalar floors include the extra gamma surplus and the true signed pole penalties. The complete construction is given and proved for the weaker gamma surplus in discovery/full_weil_hardy_gamma_tower_11_20.md; the only modified analytic term is its now stronger coefficient \(11L/50\).

At **L=29/50=0.58**, choose η=1/100000 and target \(\kappa=1/10000\). The executable source discovery/arb_full_weil_hardy_gamma_29_50.py uses 256-bit outward FLINT Arb on exact integer generating-polynomial derivative coefficients, Jacobi recurrence, rational harmonic numbers and exact transcendental balls. Its CI workflow confirms every LDL pivot strictly positive on BOTH finite Schur operators, their analytically bounded infinite tails, and all positive Hardy coefficients. Therefore for every complex test in the completed log-kinetic form domain and every log support interval of length \(0<L≤29/50\),
\[
\boxed{Q_L[f]\ge\frac1{10000}\|f\|².}
\]
For shorter supports, use translation and zero extension into the fixed ambient .58 window, preserving autocorrelation and the exact completed quadratic form.

**Scope warning:** This remains strictly **prime-free**, since 29/50<log2. The existing source-level all-prime Hardy–Schur theorem E−S≥positive up to 1.66 is NOT a proof of completed Q≥0 beyond log2 because the pole/contact/moment sewing is still missing. The correct next objective is an all-function completed Schur bound at and immediately beyond the genuine p=2 activation using this stronger gamma supplier, retaining the fake shifted-zeta adversarial control.
