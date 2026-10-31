# A curvature–Legendre–pole completion of the FULL semilocal Weil form through L = 209/500

**Codex, GPPDiscovery2, 2026-10-31.** New analytic all-function theorem with rigorous FLINT Arb scalar sign checks. Applies to the **corrected actual v34 completed semilocal Weil quadratic form** on smooth complex test functions supported on a logarithmic interval of length 0<L≤209/500=0.418 (or finite-energy form-domain closure). **Prime-free**: 0.418<log 2. Not RH or all-support Weil positivity.

## Theorem

\[
\boxed{Q_L[f]\ge \frac{1}{2000}\|f\|_2^2,\qquad 0<L\le\frac{209}{500}.}
\]

This improves the all-test completed-Q interval from 5/32 to 29/100, then 303/1000, now 209/500. The separate mean-zero full-Q theorem reaches 43/100, but only on that codimension-one subspace. The E−S prime-only supersolution reaches 83/50 with atoms 2,3,4,5, but is not full Q.

## 1. Exact completed form and Hardy potential curvature

For f supported in [0,L] and zero-extended, the **exact** v34 corrected prime-free decomposition already recorded in discovery/semilocal_full_gamma_prime_pole_sos.md is

\[
Q_L[f]=\int_0^L (V_L(x)-\Gamma_L(x)-c_\infty)|f(x)|^2 dx
+J_\gamma[f]+2|C_f|^2-2|S_f|^2.
\]

Here
- H(z)=log coth(z/2), V_L(x)=[H(x)+H(L−x)]/2;
- r(y)=(exp(y/2)−1)/(2sinh y), Γ_L(x)=∫₀ˣr+∫₀^(L−x)r;
- c∞=log(4π)+EulerGamma;
- Jγ=∫₀ᴸ [exp(y/2)/(2sinh y)]∫₀^(L−y)|f(x+y)−f(x)|² dxdy;
- C_f=∫₀ᴸ f(x)cosh((x−L/2)/2)dx; S_f=∫₀ᴸ f(x)sinh((x−L/2)/2)dx.

The earlier crude bound V_L≥H(L/2) lost significant positive energy. We now retain exact convex curvature. Direct differentiation gives

\[
H''(z)=\frac{\cosh z}{\sinh^2 z},\qquad
H''''(z)=\frac{(\cosh^2z+5)\cosh z}{\sinh^4 z}>0.
\]

Thus H'' is strictly convex, so V_L''(x)=½[H''(x)+H''(L−x)]≥H''(L/2) by Jensen. Also V_L'(L/2)=0. Integrate twice to get the **pointwise exact lower bound**

\[
\boxed{
V_L(x)\ge H(L/2)+\frac{H''(L/2)}2(x-L/2)^2.}
\]

As in prior full-Q proofs, r(y)≤exp(y/4)/4 (AM–GM), and Γ_L(x)≤exp(L/4)−1 (convex endpoint maximum). Define β(L)=H(L/2)−[exp(L/4)−1]−c∞ and normalized coordinate t(x)=(x−L/2)/L. Then

\[
V_L(x)-\Gamma_L(x)-c_\infty\ge\beta(L)+K(L)t(x)^2,\quad K(L)=\frac{L^2}2H''(L/2)>0.
\]

## 2. Exact logarithmic-Legendre jump supplier

Previous discovery/legendre_log_jump_weil.md derived the exact eigenvalue theorem A P_n=2H_n P_n for A f(x)=∫[f(x)−f(y)]/|x−y|dy, with H_n=harmonic(n). Since true gamma jump weight exp(y/2)/(2sinh y)≥1/(2y) for 0<y≤1, one obtains

- for any reflection-odd f: Jγ[f]≥||f||², and its cosh pole moment C_f=0;
- for any reflection-even f=a e0+g with e0=1/√L, ∫g=0: Jγ[f]≥(3/2)||g||², and sinh pole moment S_f=0.

These are not Galerkin approximations.

## 3. Reflection-odd sector

The negative odd pole moment is bounded by Cauchy:

\[
2|S_f|^2\le2s_2(L)\|f\|^2,\quad s_2(L)=\sinh(L/2)-L/2.
\]

Drop the positive curvature and combine local lower bound + jump to obtain

\[
Q_L[f_{\rm odd}]\ge O(L)\|f_{\rm odd}\|^2,\quad
O(L)=\beta(L)+1-2s_2(L).
\]

## 4. Reflection-even sector: EXACT 2×2 reduction

Write f=a e0+g with g even under midpoint reflection and ∫g=0. Let e2=√(5/L)P2(2x/L−1). The **exact elementary Legendre identity**

\[
t(x)^2e_0(x)=\frac1{12}e_0(x)+\frac1{6\sqrt5}e_2(x)
\]

implies, on dropping only the nonnegative K||tg||²,

\[
K\int t^2|f|^2\ge \frac K{12}|a|^2
-\frac{2K}{6\sqrt5}|a|\|g\|_2.
\]

The even pole is positive but must account for cross-coupling. Put C0(L)=4sinh(L/4), and

\[
d_c^2(L)=\frac L2+\sinh(L/2)-\frac{C_0^2}{L}
=\big\|\cosh((x-L/2)/2)-C_0/L\big\|_2^2.
\]

For any η∈(0,1), complex Young and Cauchy give

\[
2|C_f|^2\ge2(1-\eta)\frac{C_0^2}{L}|a|^2
-2(\eta^{-1}-1)d_c^2\|g\|^2.
\]

Consequently the *actual* reflection-even completed form obeys

\[
\boxed{
Q_L[f_{\rm even}]\ge A|a|^2+B\|g\|^2-2b|a|\|g\|,
}
\]

where

\[
A=\beta+\frac K{12}+2(1-\eta)C_0^2/L,\quad
B=\beta+\frac32-2(\eta^{-1}-1)d_c^2,\quad
b=K/(6\sqrt5).
\]

This uses only one 2×2 Schur matrix: M=[[A,-b],[-b,B]]. It is a **sufficient** positivity condition on the true full infinite-dimensional form; we have not substituted a finite Galerkin truncation for f.

For any desired margin δ>0, if O>δ, A>δ, B>δ, and

\[
\boxed{(A-\delta)(B-\delta)-b^2>0,}
\]

then both parity sectors satisfy Q≥δ||f||², hence all functions satisfy it.

## 5. Endpoint certificate: FLINT/Arb (256 bits)

Set L0=209/500=.418, η=1/100, δ=1/2000. The reproducible outward Arb script is discovery/full_weil_legendre_hardy_curvature_arb.py. At this exact rational endpoint it certifies:

\[
\begin{aligned}
\beta(L_0)&=-0.95619626158656547586\ldots,\\
K(L_0)&=2.01433942800510920771\ldots,\\
A(L_0)&=0.04232242596753749191\ldots,\\
B(L_0)&=0.54358406798365383588\ldots,\\
b(L_0)&=0.15013999635924892609\ldots,\\
(A-\delta)(B-\delta)-b^2
&=0.00017107472064018002934\ldots>0,\\
O(L_0)&=0.04075397552659108235\ldots>0.
\end{aligned}
\]

All printed balls have outward radii below 10^(-73). These sign comparisons are rigorous and do **not** depend on a guessed floating eigenvalue.

**CI SUCCESS**: https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41219450456 on exact commit 2f3cfd33d7ea1788b11ec454f249c21218ffe9f3.

The proof establishes the bound at L=L0; arbitrary smaller supports follow by translation and zero extension of f to an interval of length L0. Both the original entire completed form and its prime-free decomposition depend only on the zero-extended function, not on the enclosing interval's arbitrary endpoint. All f with smaller supports are therefore included.

## 6. Independent assumptions, limits, and Lean formalization

The analytic Legendre completeness and the continuum Fubini/domain closures have **not yet been checked in Lean**. Arb only certifies the explicit rational-endpoint scalar inequalities; the source mathematical proof is the chain of exact inequalities above. The previous Verify PR #474 already formalized the finite cosh/sinh pole identity and PathSOS formalized weighted edge squares.

New formal Lean targets:
1. H'''' positive and integrated midpoint quadratic curvature lower bound for V_L.
2. The elementary t² e0 decomposition into e0/e2 (orthonormal shifted Legendre).
3. Complex Young inequality for cosh pole and abstract 2×2 Schur determinant positivity.
4. Assemble analytic continuum form using the log-Legendre spectrum and proper domain hypotheses.
5. Keep the Arb endpoint as an external checked-numeric dependency until a formal rational interval bridge is available.

**RH/global Weil positivity remain OPEN.** The next physical-arithmetic obstruction is passing the first prime activation L=log2 without losing this new quadratic Hardy curvature, harmonic spectral supplier, and rank-two pole structure. Do not mix this full-Q theorem with the E−S-only prime absorption through L≤83/50=1.66.
