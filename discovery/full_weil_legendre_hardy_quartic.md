# Full completed Weil positivity to L=43/100: quartic Hardy curvature + harmonic Legendre spectrum

**2026-10-31 — Codex, GPPDiscovery2.** New rigorous analytic estimate for the **actual corrected v34 completed semilocal Weil quadratic form**, verified at the endpoint using outward 256-bit Arb scalar comparisons. Full infinite-dimensional ALL test functions. **Prime-free** (L=0.43<log2), so not RH/global positivity.

## Theorem

For every admissible complex test function f of finite completed-form energy with support inside any log interval of length 0<L≤43/100,

\[
\boxed{Q_L[f]\ge\frac1{1000}\|f\|_2^2.}
\]

This supersedes unrestricted previous endpoints 5/32, 29/100, 303/1000, 209/500. Unlike the separate mean-zero theorem at .43, this result holds with **no zero-mean restriction**.

## 1. Exact corrected completed Weil form

Use earlier source-derived identity from discovery/semilocal_full_gamma_prime_pole_sos.md,

\[
Q_L[f]=\int_0^L (V_L(x)-\Gamma_L(x)-c_\infty)|f|^2 dx+
J_\gamma[f]+2|C_f|^2-2|S_f|^2,
\]

where H(z)=log coth(z/2), V=[H(x)+H(L−x)]/2, Γ=∫₀ˣ r+∫₀^(L−x)r, r(y)=(exp(y/2)−1)/(2sinh y), c∞=log(4π)+EulerGamma, Jγ=∫₀ᴸe^(y/2)/(2sinh y)∫₀^(L−y)|f(x+y)−f(x)|²dxdy, and C/S are the cosh/sinh pole moments centered at L/2.

No prime-powers are active for L<log2. The completed infinite y>L Archimedean tail is contained in V, not discarded.

## 2. Exact positive quartic Hardy expansion

For z>0, use the absolutely convergent **exact odd-exponential series**

\[
H(z)=2\sum_{m=0}^{\infty}\frac{\exp(-(2m+1)z)}{2m+1}.
\]

Set a=L/2, u=x−a. Then

\[
V_L(a+u)=2\sum_{m=0}^{\infty}\frac{e^{-(2m+1)a}}{2m+1}
\cosh((2m+1)u).
\]

Since cosh z≥1+z²/2+z⁴/24 pointwise, compare every nonnegative summand and obtain the rigorous a.e. inequality

\[
\boxed{V_L(x)\ge H(a)+\frac{H''(a)}2u^2+\frac{H''''(a)}{24}u^4.}
\]

This avoids a Taylor remainder sign assumption. Exact derivatives:

\[
H''(a)=\frac{\cosh a}{\sinh^2a},\qquad
H''''(a)=\frac{(\cosh^2a+5)\cosh a}{\sinh^4a}>0.
\]

As before the gamma tilt satisfies Γ(x)≤exp(L/4)−1 by r(y)≤exp(y/4)/4 and endpoint convexity. Define

\[
\begin{aligned}
\beta &=H(L/2)-[\exp(L/4)-1]-c_\infty,\\
t(x)&=(x-L/2)/L,\\
k_2&=(L^2/2)H''(L/2),\\
k_4&=(L^4/24)H''''(L/2),\\
W(t)&=k_2 t^2+k_4 t^4.
\end{aligned}
\]

Then local potential V−Γ−c∞≥β+W(t) for **all** interior x.

## 3. Harmonic Legendre jump and reflection parity

The exact monomial identity for A f(x)=∫(f(x)−f(y))/|x−y|dy implies A e_n=2H_n e_n for normalized shifted Legendre modes e_n. The true Jγ kernel satisfies e^(y/2)/(2sinh y)≥1/(2y) for y≤1. Hence

- odd f: Jγ≥||f||² and C_f=0;
- even f=a e0+g with g even and mean zero: Jγ≥(3/2)||g||² and S_f=0.

The odd completed form is bounded by O||f||², where O=β+1−2[sinh(L/2)−L/2].

## 4. Reflection-even quartic moment reduction

Let e0(x)=1/√L and even g⊥e0. With uniformly distributed t∈[-1/2,1/2], exact rational moments are

\[
E[t^{2j}]=\frac1{(2j+1)2^{2j}},
\quad E[t^2]=1/12,\ E[t^4]=1/80,\
E[t^6]=1/448,\ E[t^8]=1/2304.
\]

Therefore the mean and variance of W are

\[
\mu_W=k_2/12+k_4/80,
\]
\[
\boxed{\sigma_W^2=k_2^2/180+k_2k_4/420+k_4^2/3600.}
\]

These follow from Var(t²)=1/180, Cov(t²,t⁴)=1/840 and Var(t⁴)=1/3600. Exact Cauchy gives

\[
\int_0^L W(t)|a e_0+g|^2dx
\ge\mu_W|a|^2-2\sigma_W|a|\|g\|^2{}^{1/2}.
\]

This holds because the dropped ∫W|g|² is **nonnegative** and \(\|\Pi_{e0^\perp}(W e0)\|=\sigma_W\); no Fourier truncation.

The even cosh pole is positive but has an off-diagonal coupling: let C0=4sinh(L/4), d_c²=L/2+sinh(L/2)−C0²/L. For any η∈(0,1),

\[
2|C_f|^2\ge 2(1-\eta)C_0^2/L\,|a|^2
-2(\eta^{-1}-1)d_c^2\,\|g\|^2.
\]

Combine all contributions to obtain an explicit 2×2 lower bound for every even f:

\[
Q_L[a e_0+g]\ge A|a|^2+B\|g\|^2-2b|a|\|g\|,
\]

where

\[
\boxed{
A=\beta+\mu_W+2(1-\eta)C_0^2/L,\quad
B=\beta+\frac32-2(\eta^{-1}-1)d_c^2,\quad
b^2=\sigma_W^2.}
\]

For a desired margin δ, require A>δ, B>δ, (A−δ)(B−δ)−b²>0, and O>δ. These elementary conditions give **Q≥δ||f||² for all complex f** by reflection-even/odd decomposition. This is a **finite 2×2 sufficient bound for an infinite-dimensional form**, not a Galerkin approximation.

## 5. 256-bit FLINT/Arb endpoint certificate

Set **L0=43/100**, η=1/1000, δ=1/1000. The script discovery/full_weil_legendre_hardy_quartic_arb.py gives outward balls:

\[
\begin{aligned}
\beta&=-0.987624611219990317510739\ldots,\\
k_2&=2.015161057491587629496474\ldots,\\
k_4&=3.999841775852286598984532\ldots,\\
\mu_W&=0.217928110322452551612013\ldots,\\
b^2&=0.046195755351618633356750\ldots,\\
A&=0.092758081544236144053448\ldots,\\
B&=0.509821498607666194844614\ldots,\\
(A-\delta)(B-\delta)-b^2&=
\boxed{0.0004927292090840389844969\ldots>0},\\
O&=0.0090549319912746940610128\ldots>\delta.
\end{aligned}
\]

The entire interval enclosure of each relevant sign is strictly positive; reported error radii are <1e−73.

**CI SUCCESS** https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41219739256 on exact head 911a15f5b7e7d621e86f18bab689251d20bcd387; numerical checks do not require a floating eigensolver. Earlier independent L=.418 quadratic-only certificate CI 41219450456 also passed.

For all shorter test-function supports simply translate and zero-extend into a centered ambient interval of length L0; the completed Q is invariant under that enclosing interval's arbitrary choice because it depends only on the zero-extended function. Hence the inequality for L0 establishes every L≤L0 without a hypothesis about monotonicity of β/curvature coefficients.

## 6. Formalization and limitations

The existing Verify PathSOS and PoleCoshSinh theorems are useful but do not cover the **new** quartic Hardy series and Legendre spectral theorem. Suitable next Lean targets:

1. Exact H(z)=2Σodd exp(−nz)/n and cosh z≥1+z²/2+z⁴/24.
2. Rational moments of t²,t⁴, including Cov=1/840 and Var(t⁴)=1/3600.
3. Abstract complex weighted moment Cauchy + Young + 2×2 PSD determinant lemma.
4. Shifted Legendre polynomial eigenvalues and continuum jump comparison.

The analytic Fubini/domain closure and Arb numerical scalar certificates have not been independently replayed inside Lean. Separate proof and implementation claims accordingly.

**Global RH/Weil positivity OPEN**. Full completed Q is certified only on prime-free support L≤.43, whereas prime-only E−S is known on support L≤1.66 including the actual atoms 2,3,4,5. Their joint completion beyond log2 is the missing arithmetic–Archimedean sewing theorem.
