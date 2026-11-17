# Spectral layer-cake: the first-prime Weil form has at most THREE negative directions

GPT Discovery2 | 2026-11-16 | Exact rational subcertificate EXECUTED; analytic theorem candidate, awaiting independent Turbo audit/Lean | No RH claim

This supersedes the five-moment **negative-index count** from \`first_prime_legendre_5_2026_11_16.md\`, while strengthening its high-block coercivity. It supplies 3-, 4-, and 5-moment alternatives with different Schur conditioning. The first-prime cap/Pauli description in \`haar_peter_weyl_prime_caps_2026_11_16.md\` remains exact and compatible.

## 1. Exact real-place/prime/pole setup

Let \(L=18/25=0.72\), \(I=[-L/2,L/2]\), and \(f\in C_c^\infty(I;\mathbb R)\). The actual GPPVerify Weil form on autocorrelations is
\[
W(f)=E(f)+C_\infty\|f\|_2^2+2 C_f^2-2 S_f^2-2v A_f(\log2),\tag{1}
\]
with
\[
E(f)=\int_{t>0}\frac{e^{-t/2}}{1-e^{-2t}}\|f-T_tf\|_2^2dt,\quad
C_\infty=-\gamma-\log\pi-\pi/2-3\log2,\quad
v=(\log2)/\sqrt2.
\]
For \(\log2>L/2\), the left/right edge supports are disjoint, giving \(|A_f(\log2)|\le\|f\|_2^2/2\). The negative pole has exact norm
\(2S_f^2\le2(\sinh(L/2)-L/2)\|f\|_2^2\).
The positive cosh pole may be dropped for a conservative lower bound, so
\[
 W(f)\ge E(f)-M_-\|f\|_2^2,\quad
 M_-=|C_\infty|+2(\sinh(L/2)-L/2)+v<147/25=5.88.\tag{2}
\]
The last strict transcendental estimate and rational subchecks are in \`check_first_prime_legendre5.py\`. No arithmetic sign is lost. The source identities are GPPVerify \`ArithmeticReflectionPositivity.lean\`, \`ArchimedeanFloor.lean\`, \`BNPositivity.lean\`.

## 2. Positive spectral layer cake: the new step

The unitary log-Fourier transform yields
\[
 E(f)=\int_{\mathbb R}a(\xi)|\widehat f(\xi)|^2d\xi,\qquad
 a(r)=2\sum_{k\ge0}\frac{r^2}{(2k+\tfrac12)((2k+\tfrac12)^2+r^2)},\quad r\ge0.\tag{3}
\]
Define the finite, **exact rational** positive sum
\[
 a_{100}(r)=\sum_{k=0}^{99}
 \frac{16r^2}{(4k+1)((4k+1)^2+4r^2)}.\tag{4}
\]
For rational \(r\), \(a_{100}(r)\in\mathbb Q\), and \(a(r)\ge a_{100}(r)\). Every summand of \(a_{100}\) increases in \(r\).

For increasing rational thresholds \(0=r_0<r_1<\cdots<r_J\), define \(\Delta_j=a_{100}(r_j)-a_{100}(r_{j-1})>0\). Pointwise in frequency,
\[
 a(|\xi|)\ge\sum_{j=1}^J\Delta_j\,\mathbf 1_{\{|\xi|\ge r_j\}}.\tag{5}
\]
Indeed, the right-hand side telescopes to \(a_{100}(r_i)\) in the shell \(r_i\le|\xi|<r_{i+1}\), while \(a(|\xi|)\ge a_{100}(r_i)\). By Tonelli/Plancherel,
\[
\boxed{
 E(f)\ge\sum_{j=1}^J\Delta_j
 \left(\|f\|_2^2-\int_{-r_j}^{r_j}|\widehat f(\xi)|^2d\xi\right).
}\tag{6}
\]
This is a fully source-independent elementary inequality for any nonnegative increasing multiplier. It avoids throwing away most of the energy by selecting only one cutoff.

## 3. Legendre/Haar control on the small frequency bands

Let \(\mu_k(f)=\int_I x^kf(x)dx\) and impose \(\mu_k(f)=0\) for \(0\le k<m\). This is orthogonality to the first m zonal \(SO(3)\) Peter–Weyl/Legendre modes. For \(e_n(x)=\sqrt{(2n+1)/L}P_n(2x/L)\), Rodrigues gives
\[
\int_{-1}^1e^{-izt}P_n(t)dt=
\frac{2(-iz)^n}{(2n+1)!!}\,h_n(z),\qquad
h_n(z)=\frac{\int_{-1}^1(1-t^2)^n\cos(zt)dt}
           {\int_{-1}^1(1-t^2)^ndt}.
\]
Using globally valid \(1-y^2/2\le\cos y\le1-y^2/2+y^4/24\) and exact beta moments, if
\(z^2<2(2m+3)\), then all \(n\ge m\) obey
\[
0\le h_n(z)\le1-\frac{z^2}{2(2n+3)}
+\frac{z^4}{8(2n+3)(2n+5)}.
\]
Integrate the squared right side in the **frequency variable BEFORE bounding the sum**, use \(|h_n|\le1\) for n≥12, and dominate the remaining Legendre tail geometrically. Define \(z_r=Lr/2\) and, for m≤n≤11,
\[
A_n(r)=\frac{z_r^2}{2(2n+3)},\quad
B_n(r)=\frac{z_r^4}{8(2n+3)(2n+5)},\tag{7}
\]
\[
F_n(r)=1-\frac{2(2n+1)A_n}{2n+3}
+\frac{(2n+1)(A_n^2+2B_n)}{2n+5}
-\frac{2(2n+1)A_nB_n}{2n+7}
+\frac{(2n+1)B_n^2}{2n+9}.
\]
The exact **rational** upper bound (using \(1/\pi<1/3\)) is
\[
\boxed{
\begin{aligned}
\int_{-r}^{r}|\widehat f(\xi)|^2d\xi
 &\le\delta_m^{\rm rat}(r)\|f\|_2^2,\\
\delta_m^{\rm rat}(r)
 &=\frac{Lr}{3}\left[
   \sum_{n=m}^{11}\frac{z_r^{2n}F_n(r)}{((2n+1)!!)^2}
  +\frac{z_r^{24}}{(25!!)^2(1-z_r^2/27^2)}
 \right].
\end{aligned}}\tag{8}
\]
The hypotheses include \(z_r^2<2(2m+3)\) and \(z_r<27\), both checked for each finite radius below. The estimate is not a truncated matrix approximation: it bounds the COMPLETE infinite Legendre tail, uniformly for every smooth test satisfying the moments.

Combine (6) and (8):
\[
\boxed{
 E(f)\ge A_m^{\rm rat}\|f\|_2^2,\qquad
 A_m^{\rm rat}=\sum_{j=1}^J
 (a_{100}(r_j)-a_{100}(r_{j-1}))
 (1-\delta_m^{\rm rat}(r_j)).
}\tag{9}
\]
Every term is a computable element of \(\mathbb Q\). The threshold sequences are chosen with \(0\le\delta_m^{\rm rat}(r_j)<1\).

## 4. Three independently executed exact rational certificates

The script \`experiments/abel_prime_common_map/check_first_prime_layercake_3_4_5.py\` has been **actually executed** with arbitrary-precision \`fractions.Fraction\`. Every comparison below is exact rational, not float.

| Vanishing moments | Thresholds \(r_j\) | Rational spectral certificate | Derived full Weil lower bound | High-block energy bound |
|---|---|---|---|---|
| \(m=3\) | \(r=1/2,1,\ldots,23/2,47/4\) (24 thresholds) | \(A_3^{\rm rat}>59/10=5.9\) | \(W(f)>(1/50)\|f\|^2\) | \(W(f)\ge(1/295)E(f)\) |
| \(m=4\) | \(r=1,2,\ldots,13\) | \(A_4^{\rm rat}>121/20=6.05\) | \(W(f)>(17/100)\|f\|^2\) | \(W(f)\ge(17/605)E(f)\) |
| \(m=5\) | \(r=2,4,6,8,10,12,13,14\) | \(A_5^{\rm rat}>123/20=6.15\) | \(W(f)>(27/100)\|f\|^2\) | \(W(f)\ge(9/205)E(f)\) |

The rational quantities are approximately \(A_3^{\rm rat}=5.901146893482\), \(A_4^{\rm rat}=6.054627789167\), \(A_5^{\rm rat}=6.155580955888\), but those decimals are **diagnostics only**. The strict comparisons are \(\mathbb Q\)-certified.

For the **three-moment** certificate, at the largest \(r=47/4\), \(z_r=423/100\), and \(z_r^2=(423/100)^2<2(2\cdot3+3)=18\). This close but strict inequality validates the weighted-cosine sign required in the proof; do not discard it.

The energy-coercivity constants follow algebraically from
\(W\ge E-(147/25)\|f\|^2\) and \(E\ge A\|f\|^2\), e.g.
\[
 1-\frac{(147/25)}{59/10}=\frac{1}{295}.
\]
All three source estimates preserve the pole and n=2 signed contributions.

## 5. Finite-index theorems and true Schur complement

The m moment functionals have codimension m in \(V_L\), so any negative-definite subspace of W has dimension at most m. **Strongest bound:**
\[
\boxed{n_-(W|_{V_{18/25}})\le3.}\tag{10}
\]
Even functions automatically have odd moments zero, so the three constraints are \(\mu_0=\mu_2=0\) in the even sector; odd functions have only \(\mu_1=0\). Accordingly:
\[
\boxed{n_-^{\rm even}\le2,\qquad n_-^{\rm odd}\le1.}\tag{11}
\]

At each m, the positive archimedean energy norm completes \(V_L\) to \(H_L\), and \(H_m\) is the kernel of its first m continuous moment functionals. The full actual Weil operator on
\(H_L=P_m\oplus H_m\) has block
\(Q=\begin{psmallmatrix}A&B^*\\B&D\end{psmallmatrix}\), \(D\ge\eta_m I\),
so \(W\ge0\) iff the **actual**, mixed-coupling-preserving Schur complement
\(S_m=A-B^*D^{-1}B\ge0\).

Do not confuse the dimension of a Schur obstruction with a positive Schur certificate: **no \(S_m\) has been shown positive yet.**

**Strategy trade-off:** m=3 proves the strongest finite negative-index bound, but \(\eta_3^{-1}\le295\) for its residual-certified Schur. The m=5 method has \(\eta_5^{-1}\le205/9\approx22.78\), thirteen-fold better conditioning, at the cost of a 5×5 low block. For proving true window positivity, **try the 5×5 residual certificate first**, as specified in \`first_prime_schur_residual_certificate_2026_11_16.md\`. For the strongest abstract theorem, state m=3.

## 6. Proof and review status

- **Executed:** exact \`Fraction\` code; all 24+13+8 frequency thresholds; exact finite symbol sums, beta-weight cosine coefficients and tail geometric denominators, lower energy and coercivity comparisons.
- **Analytic, still to audit/formalize:** exact normalization of GPPVerify Weil form, Fourier-Plancherel, positive spectral multiplier, Rodrigues/Legendre completeness, integration and upper bounds in (8), completion and dimension count.
- **Not established:** full positivity even at \(L=18/25\), all-width ARP/OB6, RH, the noncompact spectral placement of zeros, or a \(\zeta\)-specific positive square.

Immediate Lean targets: (i) generic monotone-multiplier finite layer-cake inequality (5)–(6) (upstreamable); (ii) polynomial Legendre beta-moment band bound (8); (iii) exact rational certificates (9); (iv) Weil 3-moment strict positivity and index count (10)–(11); (v) stronger m5 high-block inverse bound \(205/9\) and residual Schur work. No \`sorry\`, no assumption of the desired positivity theorem, and no ad hoc spectral-zero axioms.
