# First-prime Weil form: five-moment strict positivity and negative index at most five

GPT Discovery2 | 2026-11-16 | Analytic proof candidate + independent exact rational checks | **NOT** Lean compiled; **NOT** RH proof.

This improves \`research/first_prime_legendre_6_2026_11_16.md\`, which itself superseded earlier bounds 650 and 12. It uses the actual completed Weil quadratic form from GPPVerify, with pole, archimedean and von Mangoldt prime contributions and their signs intact. The only new ingredient is a sharpened Legendre Fourier leakage bound using two nontrivial cosine Taylor terms. The estimated five-dimensional obstruction is genuine, not a statement that it contains negative directions.

## Statement

Let \(I=[-9/25,9/25]\), width \(L=18/25=0.72\), and let \(V_L\) be the real \(C^\infty\) compactly supported functions on \(I\). Set
\[
\mu_j(f)=\int_I x^j f(x)\,dx,\qquad 0\le j<5.
\]
Let \(W(f)=\mathrm{weilForm}(\mathrm{autocorr}(f))\) exactly as defined in
\`GppVerify/RiemannHypothesis/ArithmeticReflectionPositivity.lean\`.

**Main theorem candidate (all analytic steps supplied below):**
\[
\boxed{\quad \forall f\in V_L\setminus\{0\},\
[\mu_0(f)=\cdots=\mu_4(f)=0]\Longrightarrow
 W(f)>\frac{709}{100000}\|f\|_2^2>0.\quad}\tag{1}
\]
Consequently the negative index of \(W\) on this width is at most FIVE. Even and odd parity have at most 3 and 2 negative directions, respectively. The finite arithmetic core has been executed using exact Python \`fractions.Fraction\`; remaining analytic formalization and independent Turbo audit are **not** complete.

## 1. Exact source Weil form, with no sign changes

For real f supported on \(I\), set \(A_f(t)=\langle f,T_t f\rangle\), \(\ell=\log2\),
\(v=\log2/\sqrt2\), and \(w(t)=e^{-t/2}/(1-e^{-2t})\).
At this width \(\log2<L<\log3\), so the only visible prime power is \(n=2\). The exact original GPPVerify Weil quadratic is
\[
W(f)=E(f)+C_\infty\|f\|_2^2+2C_f^2-2S_f^2-2vA_f(\ell), \tag{2}
\]
\[
E(f)=\int_{t>0}w(t)\|f-T_t f\|_2^2dt,\quad
C_\infty=-\gamma-\log\pi-\pi/2-3\log2,\quad
C_f=\int f\cosh(x/2),\quad S_f=\int f\sinh(x/2).
\]
This is the exact archimedean decomposition proved algebraically in earlier Discovery2 notes, and anchored in Verify \`ArchimedeanFloor.lean\`, \`BNPositivity.lean\` and \`ArithmeticReflectionPositivity.lean\`.

Since \(\ell>L/2\), the source and target edge pieces in \(A_f(\ell)\) are disjoint. Cauchy–Schwarz plus \(2ab\le a^2+b^2\) gives
\[
 |A_f(\ell)|\le \tfrac12\|f\|_2^2. \tag{3}
\]
By exact Cauchy–Schwarz on the sinh pole,
\[
2 S_f^2\le 2(\sinh(L/2)-L/2)\|f\|_2^2.
\]
Drop ONLY the positive term \(2C_f^2\). Thus
\[
W(f)\ge E(f)-M_-\|f\|_2^2,\qquad
M_-:=|C_\infty|+2(\sinh(L/2)-L/2)+\frac{\log2}{\sqrt2}.\tag{4}
\]
The prime has not been discarded: its most negative possible contribution is bounded by the exact disjoint-edge correlation.

## 2. Tight elementary bound on the actual negative perturbation

For \(L=18/25\), the following **strict** rational bounds suffice:
\[
\begin{array}{lll}
\gamma<578/1000,&\log\pi<11448/10000,&\pi/2<15708/10000,\\
3\log2<207945/100000,&
2[\sinh(9/25)-9/25]<158/10000,&
\log2/\sqrt2<4902/10000 .
\end{array}
\]
Their sum is exactly
\[
\boxed{\quad M_-<\frac{117581}{20000}=5.87905<\frac{147}{25}=5.88.\quad}\tag{5}
\]
Here is an independently auditable rational/analytic route:

- \(\gamma<H_{1024}-\log1024=H_{1024}-10\log2\); since \(\log2>693147/10^6\), exact rational evaluation of the 1024-term harmonic sum gives \(H_{1024}-10(693147/10^6)<578/1000\).
- **Use the existing Mathlib \`Real.pi_lt_d6\` bound**, or another direct \(\pi<31416/10000\). The weaker \(\pi<22/7\) is NOT adequate here. By the positive exponential Taylor series, the rational partial sum \(\sum_{k=0}^7(11448/10000)^k/k!\) exceeds \(31416/10000\), whence \(\log\pi<11448/10000\). Also \(\pi/2<15708/10000\).
- Since \(\log2<69315/10^5\), \(3\log2<207945/10^5\).
- For \(0\le x<1\), \(2(\sinh x-x)\le x^3/3+x^5/[60(1-x^2)]\). This follows by bounding the tail of the power series from \(x^5/5!\) by a geometric series. At \(x=9/25\), this rational majorant is \(<158/10^4\).
- From \(\log2<693148/10^6\) and \(\sqrt2>14142/10^4\), one obtains \(\log2/\sqrt2<4902/10^4\), verified by exact rational cross multiplication. The sqrt inequality reduces to a rational square.

**Scope:** Only rational comparisons were executed as checks, not the corresponding transcendental lemmas in Lean. Verify contains the relevant Euler harmonic, log2 and \(\pi\) bounds.

## 3. The exact positive Fourier multiplier

With unitary Fourier transform \(\hat f(\xi)=(2\pi)^{-1/2}\int f(x)e^{-i\xi x}dx\),
\[
E(f)=\int_{\mathbb R}a(\xi)|\hat f(\xi)|^2d\xi,\quad
a(\xi)=2\sum_{k\ge0}
 \frac{\xi^2}{(2k+\tfrac12)[(2k+\tfrac12)^2+\xi^2]}. \tag{6}
\]
Every term is nonnegative and increases in \(|\xi|\), so
\[
E(f)\ge a(R)\left(\|f\|_2^2-\int_{-R}^R|\hat f(\xi)|^2d\xi\right).
\]
At \(R=47/4=11.75\), the exact **100-term positive rational partial sum** of (6) satisfies
\[
\boxed{\quad
a(47/4)>
 \sum_{k=0}^{99}
 \frac{16(47/4)^2}{(4k+1)[(4k+1)^2+4(47/4)^2]}
 >\frac{1199}{200}=5.995.\quad}\tag{7}
\]

## 4. Sharpened Legendre band bound using the weighted cosine moment

Let \(P_n\) be the standard Legendre polynomial and
\(e_n(x)=\sqrt{(2n+1)/L}\,P_n(2x/L)\) on I. The \(e_n\) are an orthonormal basis of \(L^2(I)\). Vanishing spatial moments \(\mu_0,\ldots,\mu_4\) imply \(f\perp e_0,\ldots,e_4\).

Rodrigues plus integration by parts gives, for \(z=\xi L/2\),
\[
\int_{-1}^1e^{-izt}P_n(t)dt=
\frac{(-iz)^n}{2^n n!}\int_{-1}^1e^{-izt}(1-t^2)^n dt
=\frac{2(-iz)^n}{(2n+1)!!}\,h_n(z),\tag{8}
\]
where the *real even weighted cosine average*
\[
h_n(z)=\frac{\int_{-1}^1\cos(zt)(1-t^2)^n dt}{\int_{-1}^1(1-t^2)^n dt}
\]
is normalized so that \(h_n(0)=1\).

For every real \(y\),
\(1-y^2/2\le\cos y\le1-y^2/2+y^4/24\). The beta integrals give
\[
\mathbb E_n[t^2]=\frac1{2n+3},\qquad
\mathbb E_n[t^4]=\frac3{(2n+3)(2n+5)}.
\]
Consequently, with
\[
A_n(z)=\frac{z^2}{2(2n+3)},\qquad
B_n(z)=\frac{z^4}{8(2n+3)(2n+5)},
\]
one has
\[
1-A_n(z)\le h_n(z)\le1-A_n(z)+B_n(z).\tag{9}
\]
If \(A_n(z)\le1\), then \(h_n(z)\ge0\), so
\(|h_n(z)|^2\le[1-A_n(z)+B_n(z)]^2\).
For n≥5 and |ξ|≤R=47/4, \(|z|\le z_*=RL/2=423/100\) and \(A_n(z_*)<1\).
No Bessel-function assumption or questionable alternating-series continuation is used.

By Parseval in the Legendre basis and Cauchy–Schwarz, for f orthogonal to e_0,...,e_4,
\[
|\hat f(\xi)|^2\le\frac{L}{2\pi}\|f\|_2^2
 \sum_{n\ge5}\frac{(2n+1)(|\xi|L/2)^{2n}}{[(2n+1)!!]^2}|h_n(\xi L/2)|^2. \tag{10}
\]

Now INTEGRATE in ξ before bounding the frequency tail. For each n=5,...,11 define rational
\[
\begin{split}
 A_n&=\frac{z_*^2}{2(2n+3)},\qquad
 B_n=\frac{z_*^4}{8(2n+3)(2n+5)},\\
 F_n&=1-\frac{2n+1}{2n+3}2A_n+
          \frac{2n+1}{2n+5}(A_n^2+2B_n)\\
   &\qquad-\frac{2n+1}{2n+7}2A_nB_n+
           \frac{2n+1}{2n+9}B_n^2.
\end{split}\tag{11}
\]
This is exactly \((2n+1)\int_0^1u^{2n}(1-A_nu^2+B_nu^4)^2du\).

For n≥12 use the safe bound \(|h_n(z)|\le1\) (average of cosines), plus the geometric bound on the remaining positive summands. Therefore
\[
\boxed{
\int_{-R}^R|\hat f(\xi)|^2d\xi\le\delta_5\|f\|_2^2,\qquad
\delta_5\le
\frac{LR}{\pi}\left[
 \sum_{n=5}^{11}\frac{z_*^{2n}F_n}{[(2n+1)!!]^2}
 +\frac{z_*^{24}}{25!!^2[1-z_*^2/27^2]}
 \right]. }\tag{12}
\]
This is a *pointwise bound for the entire infinite Legendre tail*, NOT a truncation of the Weil quadratic form. It controls all off-basis and mixed pairings through an operator-norm estimate.

Every ingredient on the right is rational except \(\pi^{-1}\), conservatively bounded by \(1/3\).
Exact \`fractions.Fraction\` evaluation verifies
\[
\boxed{\quad\delta_5<\frac9{500}=0.018.\quad}\tag{13}
\]

## 5. Strict positivity on five moment constraints

Combining (4), (5), (7) and (13), for any nonzero real \(f\in V_L\) with moments 0,...,4 zero,
\[
\begin{split}
 W(f)&\ge E(f)-M_-\|f\|_2^2\\
 &>\left[\frac{1199}{200}\left(1-\frac9{500}\right)-\frac{147}{25}\right]\|f\|_2^2\\
 &=\boxed{\frac{709}{100000}\|f\|_2^2>0.}
\end{split}\tag{14}
\]
The common kernel of five independent linear moments has codimension five, so any negative-definite subspace has dimension at most five:
\[
\boxed{\qquad n_-(W|_{V_{18/25}})\le5.\qquad}\tag{15}
\]
Reflection parity splits the moment conditions into 3 even and 2 odd constraints, giving upper bounds n_-^{even}≤3, n_-^{odd}≤2.

## 6. Exact high-block coercivity and the real five-by-five obstruction

Let \(H_L\) be the completion of \(V_L\) in the **positive** archimedean norm \(\|f\|_{\mathcal E}=\sqrt{E(f)}\) from \`fixed_window_weil_compact_2026_11_16.md\`. The inclusion \(H_L\hookrightarrow L^2(I)\) is continuous (positive tail bound) and compact (Fourier high-frequency coercivity). The five moments extend continuously; let
\(H_0=\bigcap_{j=0}^4\ker\mu_j\), \(P=H_0^{\perp_{\mathcal E}}\) (dimension 5).

Our rational bound gives \(\mathcal E(f)>(588709/100000)\|f\|_2^2\) on the moment-nullspace, so, since \(W(f)\ge E(f)-(147/25)\|f\|_2^2\),
\[
 \boxed{
 W(f)\ge\frac{709}{588709}E(f)
 \quad\forall f\in H_0.}\tag{16}
\]
The strict positivity extends to the completion by continuity; weak ≥ is sufficient for bounded invertibility. This produces a **quantitative inverse-norm** estimate for the high block:
\[
 \|D^{-1}\|_{\mathcal E}\le\frac{588709}{709}\approx830.34.
\]
In the energy-orthogonal decomposition \(H_L=P\oplus H_0\), represent the actual completed Weil form by
\[
 \begin{pmatrix}A&B^*\\B&D\end{pmatrix}.
\]
Because D is strictly positive and invertible, the WHOLE infinite-dimensional Weil form is nonnegative at this width if and only if the **exact** finite Schur complement
\[
 \boxed{\quad S_5=A-B^*D^{-1}B\ \succeq 0,\quad S_5\text{ is }5\times5.\quad}\tag{17}
\]
No claim that \(S_5\) is positive is made. In particular, checking a numerical five-by-five principal minor without the exact cross-block correction \(B^*D^{-1}B\) would be logically invalid.

## 7. Verification status and immediate handoff

* **Executed and checked:** exact rational sum for the 100-term archimedean lower bound, each F_n, finite sum + geometric tail at n=12, harmonic H1024 bound, exp Taylor degree 7, sinh series comparison, sqrt2 rational comparison, total M_- and positive 709/100000 margin. See \`experiments/abel_prime_common_map/check_first_prime_legendre5.py\`.
* **Analytic proof candidate, not Lean checked:** Fourier-Plancherel and real-place normalization, Legendre Parseval/Rodrigues identity, beta-weight cosine moments, complete tail estimate (10)–(12), support-overlap lemma, gamma/pi/log transcendental comparisons, high-block completion and Schur complement.
* **Not proved:** \(S_5\succeq0\), the zero-index claim on this width, all-width arithmetic reflection positivity, RH.

**Turbo:** audit the five-moment proof firsthand, especially (10)–(12), then give Claude these concrete formalization units: edge-overlap; cosine quadratic/quartic inequalities; Legendre Rodrigues and beta moments; spectral/Parseval identity with frequency integration; finite rational certificate; strict five-moment W positivity; index ≤5; optional high-block coercivity and five-dimensional Schur equivalence. Existing Verify \`Upstream/ExpTaylorImaginary.lean\` supplies a weaker moment method but is not enough for the Legendre improvement.

This result supersedes the six-, twelve- and 650-direction handoffs ONLY in the upper-bound sense; keep previous files for method provenance. There is still no RH proof and no claim of global positivity.
