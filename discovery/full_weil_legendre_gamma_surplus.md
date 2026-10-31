# Full completed Weil positivity on ALL tests to L=1/2: gamma surplus + banded Legendre infinite-tail Schur

**2026-10-31, Codex / GPPDiscovery2.** New **analytic all-function infinite-dimensional completed semilocal Weil theorem** with 256-bit outward FLINT Arb endpoint certification. No RH/global arbitrary-support positivity claim. This is PRIME-FREE, since 1/2<log2. Previous local all-test completed Q endpoints L≤.43/.49 are superseded, but their proof methods remain useful.

## Theorem

For every admissible complex test function of finite logarithmic kinetic energy supported in an interval of logarithmic length 0<L≤1/2, the **actual corrected v34 completed Weil form** satisfies

\[
\boxed{Q_L[f]\ge 10^{-4}\|f\|_2^2.}
\]

The contact subtraction, regular gamma tilt, infinite gamma tail and indefinite rank-two pole are ALL included. This is not a finite Galerkin extrapolation: all Legendre n≥12 are controlled by a rigorous operator tail bound.

## 1. Genuine corrected completed form and pointwise suppliers

The exact representation from discovery/semilocal_full_gamma_prime_pole_sos.md is

\[
Q=\int(V_L-\Gamma_L-c_\infty)|f|^2dx+J_\gamma[f]
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2
\]

where V=(H(x)+H(L−x))/2, H(z)=log coth(z/2), gamma tilt Γ(x)=∫₀ˣr+∫₀^(L−x)r with r=(e^(y/2)−1)/(2sinh y), c∞=log(4π)+EulerGamma, c(x)=cosh((x−L/2)/2), s(x)=sinh((x−L/2)/2), and Jγ is the positive continuum jump with weight w(y)=e^(y/2)/(2sinh y).

Use exact positive quartic Hardy series from discovery/full_weil_legendre_hardy_quartic.md:

\[
V_L(x)\ge H(L/2)+\frac{H''(L/2)}2(x-L/2)^2
+\frac{H''''(L/2)}{24}(x-L/2)^4
\]

because H(t)=2Σ_(n odd≥1)e^(−nt)/n and cosh z≥1+z²/2+z⁴/24 termwise. Also Γ≤e^(L/4)−1. Let β=H(L/2)−[e^(L/4)−1]−c∞, z=2x/L−1, and

\[
W(z)=k_2(z/2)^2+k_4(z/2)^4,\quad
k_2=\frac{L^2}2H''(L/2),\quad
k_4=\frac{L^4}{24}H''''(L/2).
\]

Then the local potential is ≥β+W(z) and W is nonnegative multiplication.

## 2. NEW extra gamma surplus: exact Jγ ≥ J0+(L/6)Var

For all 0<y≤1, prove the simple universal pointwise inequality

\[
\boxed{\frac{e^{y/2}}{2\sinh y}\ge \frac1{2y}+\frac16.}
\]

Rigorous elementary proof:
- sinh(y)/y=Σ_{n≥0}y^{2n}/(2n+1)! ≤1+(10/57)y² <1+y²/5. The coefficient bound follows from (2n+3)(2n+2)≥20 for n≥1 and geometric majorization starting at 1/3!=1/6; valid y≤1.
- e^(y/2)≥1+y/2+y²/8+y³/48.
- For 0<y≤1,
  \[
  e^{y/2}-(1+y/3)(1+y^2/5)
  \ge y[1/6-3y/40-11y^2/240]\ge 11y/240>0.
  \]
Hence e^(y/2)≥(1+y/3)(sinh y/y), equivalent to the boxed inequality.

The exact variance identity is

\[
\int_0^Ldy\int_0^{L-y}|f(x+y)-f(x)|^2dx
=L\|f-\bar f\|_2^2.
\]

Thus the TRUE completed gamma jump obeys

\[
J_\gamma[f]\ge J_0[f]+\frac L6\|f-\bar f\|^2,\quad
J_0[f]=\frac12\int_{0<x<y<L}\frac{|f(x)-f(y)|^2}{y-x}dxdy.
\]

The exact shifted-Legendre spectral theorem from discovery/legendre_log_jump_weil.md gives J0=Σ_(n≥1)H_n|f_n|², H_n=Σ_{j=1}^n1/j. Therefore Jγ≥Σ_(n≥1)(H_n+L/6)|f_n|². The constant n=0 mode has zero jump, as required.

## 3. Certified finite-rank pole lower model

The even pole c(x)=cosh((x−L/2)/2) has a degree-two polynomial approximation

\[
c_2(x)=1+\frac{(x-L/2)^2}{8}=1+\frac{L^2z^2}{32}.
\]

For |x−L/2|≤L/2, the exact Taylor remainder is bounded by

\[
0\le c(x)-c_2(x)\le \varepsilon_c=
\frac{(L/4)^4\cosh(L/4)}{24}.
\]

Therefore ||c−c2||²≤L ε_c². For 0<η<1, complex Young gives the exact lower bound

\[
2|\langle c,f\rangle|^2
\ge 2(1-\eta)|\langle c_2,f\rangle|^2
-2(\eta^{-1}-1)L\varepsilon_c^2\|f\|^2.
\]

The odd pole is bounded from below by the exact norm

\[
-2|\langle s,f\rangle|^2\ge
-2[\sinh(L/2)-L/2]\|f\|^2.
\]

Define the nonnegative scalar penalty

\[
\alpha=
2[\sinh(L/2)-L/2]
+2(\eta^{-1}-1)L\varepsilon_c^2.
\]

In the normalized shifted Legendre basis e_n(x)=√((2n+1)/L)P_n(z), the polynomial c2 has only modes n=0 and n=2, with EXACT coefficients:

\[
(c_2)_0=\sqrt L(1+L^2/96),\quad
(c_2)_2=\sqrt L\,L^2/(48\sqrt5).
\]

Hence the entire **true completed Q** has the explicit operator lower bound

\[
\boxed{
Q\ \succeq\
\underbrace{\operatorname{diag}(H_n+\tfrac L6\,1_{n\ge1}+\beta-\alpha)}_{D}
+\underbrace{k_2(Z/2)^2+k_4(Z/2)^4}_{W\ge0}
+2(1-\eta)|c_2\rangle\langle c_2|,
}
\]

where Z is multiplication by z. The lower bound requires no assumption that f occupies finitely many Legendre modes.

## 4. EXACT finite-band high-tail Schur argument

The multiplication operator Z has exactly the symmetric Jacobi coefficients

\[
Z_{n,n+1}=Z_{n+1,n}
=\frac{n+1}{\sqrt{(2n+1)(2n+3)}}.
\]

Consequently W contains only |n−m|≤4 (and preserves parity). Take N=12, low span e0,...,e11 and infinite high span e12,e13,... . The positive pole rank-one approximation c2 lies **entirely** in the low sector. Let A be the exact 12×12 low restriction of D+W+rankone. Let B be the exact low-to-high coupling. Because W is quartic, **B has only FOUR nonzero high columns n=12,13,14,15**. In particular, every interaction with all infinitely many n≥16 is identically zero, not numerically neglected.

The high block is

\[
C\ge d I,\quad d=H_{12}+L/6+\beta-\alpha>0,
\]

because W≥0 and H_n increases with n. For any margin δ<d, exact completion of the high-sector square proves

\[
D+W+\mathrm{pole}\ge\delta I
\]

as soon as the finite **12×12 Schur** matrix

\[
\boxed{
A-\delta I-BB^\mathsf{T}/(d-\delta)
}
\]

is strictly positive definite. This proves the sign on the *entire infinite tail* with no operator-norm convergence hypothesis or finite-Galerkin extrapolation.

## 5. Outward Arb endpoint certificate

At exact rational L0=1/2, choose η=1/1000, δ=1/10000. The reproducible script

  discovery/full_weil_legendre_gamma_surplus_arb.py

uses 256-bit FLINT Arb, exact rational harmonic numbers, and exact Jacobi coefficient formulas. All transcendental functions and roots are outward balls. It certifies

\[
\begin{aligned}
\beta&=-1.156757395612774274103\ldots,\\
k_2&=2.020382565200781469322\ldots,\\
k_4&=3.999715760842790348749\ldots,\\
\varepsilon_c&=1.0252102435564278766\times10^{-5}\ \text{(upper ball)},\\
\alpha&=0.005224738616835360781964\ldots,\\
d&=2.024561877314401909126482\ldots>\delta.
\end{aligned}
\]

All 12 interval LDL pivots of \(A-\delta I-BB^T/(d-\delta)\) are strictly positive. The smallest printed pivot is approximately **0.01588677559283148726**. Therefore the analytic infinite-operator comparison yields full \(Q_L[f]\ge10^{-4}\|f\|²\) at L=L0, and smaller supports by zero extension into centered ambient L0.

**GitHub Actions SUCCESS** https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41220298062, exact head fd3684cd6b55170fd368bffda4f2321a7109c63b, all CI steps successful. This is an analytic + interval scalar finite-block Schur certificate. The complete continuum density/Fubini and scalar sign checks are not yet formalized in Lean.

Independent previous banded-tail L=12/25=.48 CI https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41220135877 also passes; other team's existing .49 method independently passes CI 41220010988. This 1/2 result is stronger.

## 6. Scope and formalization

Still **NO PRIME SOURCE** at support 1/2 because 1/2<log2. RH/global Weil positivity remains open. The next major goal is to keep the positive jump surplus, Hardy quartic (or higher) curvature, and finite-rank pole approximation while incorporating the first true prime shift at L=log2 into a genuine operator Schur bound. Prime shifts are not finite-band in Legendre modes, so need an additional infinite-tail estimate or positive graph-square sewing.

For GPPVerify, the new Lean targets not already merged are:
- elementary gamma-jump surplus inequality w(y)≥1/(2y)+1/6 on y≤1;
- exact Legendre harmonic eigenvalues H_n from the monomial action of A;
- true Jacobi three-term recurrence / quartic bandwidth four;
- abstract Hilbert-space Schur tail lemma for bounded finite-rank cross B, high block C≥dI, and strict finite interval Schur PSD;
- pole cosh Taylor remainder and Young bound;
- Hardy odd-exp series positive curvature.
Maintain source/Lean separation: FLINT Arb success is not a Lean formal proof of these analytic steps.
