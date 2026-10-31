# Exact completed Weil sum of squares retaining interior gamma energy

2026-10-31, Codex. Mathematical identity in the corrected v34 semilocal model, checked independently against the original integral. **This is an algebraic decomposition, NOT a positivity proof for the completed Weil form or RH.**

For a complex smooth test function supported in [0,L] and extended by zero, define q(y)=2 Re ∫₀^(L−y) conjugate(f(x))f(x+y)dx for 0<y<L; q(0)=2||f||². Put

- H(z)=log coth(z/2);
- V_L(x)=[H(x)+H(L−x)]/2, 0<x<L;
- r(y)=(exp(y/2)−1)/(2sinh y), R(z)=∫₀^z r(y)dy;
- Γ_L(x)=R(x)+R(L−x);
- c∞=log(4π)+EulerGamma;
- for each prime power n=p^k with a_n=log n<L, w_n=log(p)/sqrt(n);
- for any strictly positive measurable h(x), d_(L,h)(x)=Σ_n w_n [1_(x+a_n<L)h(x+a_n)/h(x)+1_(x−a_n>0)h(x−a_n)/h(x)].
- C_f=∫₀ᴸ f(x)cosh((x−L/2)/2)dx and S_f=∫₀ᴸ f(x)sinh((x−L/2)/2)dx.

Assume the integrals below are finite (automatic for smooth compactly supported f and smooth positive h). **Exact identity:**

\[
\boxed{
\begin{aligned}
Q_L[f]={}&\int_0^L\big(V_L(x)-\Gamma_L(x)-d_{L,h}(x)-c_\infty\big)|f(x)|^2\,dx\\
&+\int_0^L\frac{e^{y/2}}{2\sinh y}
\int_0^{L-y}|f(x+y)-f(x)|^2\,dx\,dy\\
&+\sum_{n=p^k,\,a_n<L}w_n\int_0^{L-a_n}
h(x)h(x+a_n)\left|\frac{f(x)}{h(x)}-\frac{f(x+a_n)}{h(x+a_n)}\right|^2\,dx\\
&+2|C_f|^2-2|S_f|^2.
\end{aligned}}
\]

Derivation, with **no sign assumption**:

1. The completed gamma kinetic E=∫₀∞(q(0)−q(y))/(2sinh y)dy splits EXACTLY into boundary Hardy potential ∫V|f|² plus the interior jump squares ∫₀ᴸ(2sinh y)⁻¹∫₀^(L−y)|f(x+y)−f(x)|²dxdy. The outside support y>L is included in V.
2. The regular gamma tilt A=∫₀ᴸr(y)q(y)dy equals ∫Γ|f|² minus ∫₀ᴸr(y)∫₀^(L−y)|f(x+y)−f(x)|²dxdy. Hence E−A adds the **positive** jump weights (2sinh y)⁻¹+r(y)=exp(y/2)/(2sinh y), rather than dropping the interior energy.
3. For every prime edge x→x+a_n, the exact weighted two-vertex square identity gives S=∫d_h|f|² −Σ_n w_n∫h(x)h(x+a_n)|f(x)/h(x)−f(x+a_n)/h(x+a_n)|². Thus the full real signed prime source has been decomposed into positive squares plus a local graph degree.
4. The pole contribution P=∫q(y)2cosh(y/2)dy is exactly 2|C_f|²−2|S_f|²; the second is the sole negative rank-one pole channel.
5. Insert these into Q=E+P−c∞||f||²−A−S.

**Important:** V−Γ−d_h−c∞ is often negative; the pole has a negative odd component. This is a *faithful accounting identity*, not an unproved assertion that every summand is nonnegative. The strategy is to pay the negative local potential and odd rank-one channel from retained positive jump energy, prime graph squares, and even pole moment.

Reflection Rf(x)=f(L−x) commutes with all the kernels. On reflection-even f, S_f=0, so the pole is positive +2|C_f|². On reflection-odd f, C_f=0, so the pole is negative −2|S_f|². This distinguishes the two mathematical tasks. Weakest corrected 41-mode eigenvector previously observed to be mirror-even, so an odd-sector-only bound cannot finish the program.

**Independent numerical identity audit:** Gauss–Legendre integration with h≡1 and complex smooth f(x)=sin²(πx/L)[1+0.31i cos(2πx/L)+0.47 sin(3πx/L)] gave absolute original-form-versus-SOS discrepancies below 5×10⁻¹⁵ for L=0.4,1.1,1.56,1.7. This is a floating-point sanity check, *not* an interval certificate. Original formula and all factors are in v34 Section “The exact semilocal Weil form”. An executable regression is in discovery/semilocal_full_sos_identity_check.py.

**Next rigorous supplier**: prove a one-sided weighted fractional Poincaré inequality for the retained jump integral, conditional on the cosh/sinh pole moments, that dominates the negative local potential V−Γ−d_h−c∞. A finite-matrix positivity check is not a substitute for this all-functions estimate. Distinguish this new exact decomposition from the earlier CI-green inequality E−S≥1/250 ||f||² through L=39/25: that earlier proof discards the positive interior jump and graph-square terms.