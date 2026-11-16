# The first-prime Weil form has negative index at most TWELVE

16 November 2026 | GPT Discovery2 research | proof-quality analytic draft; exact rational arithmetic checked; Lean and Turbo audit pending.

**Main finding:** For the *actual* GPPVerify completed Weil form on smooth real functions supported in
\(I=[-9/25,9/25]\) (width \(L=18/25=0.72\)), the negative index is at most **12**.
This strengthens the preceding 650 bound in
\`research/fixed_window_weil_compact_2026_11_16.md\`.
It does NOT show that any negative direction exists or that the negative index is zero; ARP, OB6 and RH remain open. The key improvement is an explicit, elementary finite-codimension subspace defined by vanishing **spatial moments**, instead of a numerically determined singular-vector subspace.

## 1. Exact form and the one-prime overlap

From GPPVerify's \`ArithmeticReflectionPositivity.lean\`, \`ArchimedeanFloor.lean\`, \`BNPositivity.lean\` and \`ShiftPresentation.lean\` (derived in the companion compactness note), for real \(f\in C_c^\infty(I)\),

\[
 W(f)=\mathcal E(f)+C_\infty\|f\|_2^2
    +2 C_f^2-2 S_f^2
    -2v\,A_f(\ell),
 \quad C_\infty=-\gamma-\log\pi-\pi/2-3\log2,
 \tag{1}
\]
where
\[
 \ell=\log2,\quad v=(\log2)/\sqrt2,\quad
 A_f(\ell)=\int f(x)f(x-\ell)\,dx,
\quad C_f=\int f(x)\cosh(x/2)\,dx,\quad
 S_f=\int f(x)\sinh(x/2)\,dx,
\]
and
\[
 \mathcal E(f)=\int_0^\infty
 \frac{e^{-t/2}}{1-e^{-2t}}\|f-T_t f\|_2^2\,dt.
\]
Since \(\log2<L<\log3\), only \(n=2\) appears in the finite prime sum (not \(n=4\)).

The old estimate used \(|A_f(\ell)|\le\|f\|_2^2\), but the geometry of the first-prime overlap halves that bound:

**Edge-overlap lemma:** if \(\ell\ge L/2\), then
\[
 |A_f(\ell)|\le \tfrac12\|f\|_2^2. \tag{2}
\]
Proof: \(A_f(\ell)\) pairs the left edge \(I\cap(I-\ell)\) with the right edge \(I\cap(I+\ell)\). The two edge intervals are disjoint when \(2\ell\ge L\). Cauchy–Schwarz and \(2ab\le a^2+b^2\) give \(2|A_f(\ell)|\le\|f_{\rm left}\|_2^2+\|f_{\rm right}\|_2^2\le\|f\|_2^2\). The same argument applies to arbitrary real f on I, not only smooth f.

The positive cosh rank-one pole can be retained rather than bounded in absolute value, while the negative sinh pole satisfies
\[
 2S_f^2\le 2\|\sinh(x/2)\|_{L^2(I)}^2\,\|f\|_2^2
 =2[\sinh(L/2)-L/2]\,\|f\|_2^2. \tag{3}
\]

Consequently
\[
\boxed{\quad W(f)\ge \mathcal E(f)-M_-\|f\|_2^2,\quad
 M_-:=|C_\infty|+2[\sinh(L/2)-L/2]+v.\quad} \tag{4}
\]

**Important:** This is a *lower bound on the true signed prime/pole/archimedean form*. We have not thrown away a negative term or silently changed the Weil form. The positive cosh pole was omitted only in a conservative lower bound.

## 2. Positive archimedean symbol

With the unitary Fourier transform,
\[
 \mathcal E(f)=\int_{\mathbb R}a(\xi)|\widehat f(\xi)|^2d\xi,
\quad
 a(\xi)=2\sum_{k\ge0}
 \frac{\xi^2}{(2k+1/2)[(2k+1/2)^2+\xi^2]}.\tag{5}
\]
The series is positive and \(a(\xi)\) is nondecreasing as a function of \(|\xi|\). Therefore
\[
 \mathcal E(f)\ge a(R)\int_{|\xi|>R}|\widehat f(\xi)|^2\,d\xi.\tag{6}
\]
This is the exact Fourier normalization from the earlier fixed-window compactness note. For \(R=11\) its first 100 *positive rational* series terms already yield
\[
\boxed{\quad
 a(11)\ge\sum_{k=0}^{99}
 \frac{16\cdot121}{(4k+1)((4k+1)^2+484)}
 >\frac{593}{100}.\quad}\tag{7}
\]
The strict inequality was executed and passed using Python \`fractions.Fraction\` (not floating point). The source script below retains the exact integer arithmetic.

## 3. A twelve-dimensional low-frequency obstruction, by spatial moments

Define the twelve common linear functionals
\[
 \mu_j(f)=\int_I x^j f(x)\,dx,\qquad j=0,1,\dots,11,
\quad \mathcal V=\bigcap_{j=0}^{11}\ker\mu_j.\tag{8}
\]

For any \(f\in\mathcal V\), Taylor's formula for the complex exponential (in its integral-remainder form, exploiting \(|e^{i\theta}|=1\) for real \(\theta\)) gives, uniformly for \(|\xi|\le R\) and \(x\in I\),
\[
 \left|e^{-i\xi x}-\sum_{j=0}^{11}\frac{(-i\xi x)^j}{j!}\right|
 \le \frac{(R L/2)^{12}}{12!}.\tag{9}
\]
All polynomial terms vanish when integrated against f, so by Cauchy–Schwarz,
\[
 |\widehat f(\xi)|
 \le\sqrt{\frac{L}{2\pi}}\frac{(R L/2)^{12}}{12!}\|f\|_2.
\]
After integration over \([-R,R]\),
\[
 \int_{-R}^R|\widehat f(\xi)|^2d\xi
 \le\delta_{L,R,12}\|f\|_2^2,\qquad
 \delta_{L,R,m}:=\frac{LR}{\pi}\left[\frac{(RL/2)^m}{m!}\right]^2.
 \tag{10}
\]

Set \(L=18/25\), \(R=11\), \(m=12\). Since \(\pi>3\), the following strict **rational** inequality holds (checked by exact \`Fraction\` arithmetic):
\[
\boxed{
 \delta_{18/25,11,12}
 <\frac{(18/25)\,11}{3}
   \left[\frac{((18/25)\,11/2)^{12}}{12!}\right]^2
 <\frac{1}{300}.}\tag{11}
\]

By Plancherel, (6), (7), and (11), every \(f\in\mathcal V\) satisfies
\[
\boxed{
 \mathcal E(f)>
 \frac{593}{100}\frac{299}{300}\|f\|_2^2
 \quad (f\ne0).}\tag{12}
\]

## 4. Rational majorant on the bounded negative term

We only need \(M_-<59/10=5.9\), considerably easier than computing \(M_-\) itself.
The following elementary inequalities suffice:
\[
 \gamma<29/50,\quad \log\pi<23/20,\quad
 \pi/2<11/7,\quad 3\log2<52/25,\\
 2[\sinh(9/25)-9/25]<9/500,\quad (\log2)/\sqrt2<1/2.
 \tag{13}
\]
Their sum is an exact rational
\[
 M_-<\frac{29}{50}+\frac{23}{20}
 +\frac{11}{7}+\frac{52}{25}
 +\frac9{500}+\frac12
 =\frac{5162}{875}
 <\frac{59}{10}.\tag{14}
\]

Elementary ways to audit the transcendental inputs:
- \(\gamma < H_{256}-\log256\), the in-tree Euler–harmonic bound used in \`RungZeroWide.lean\` for smaller n; \(\log2>6931/10000\), so
\(H_{256}-8(6931/10000)<29/50\), checked exactly using \(\sum_{j=1}^{256}1/j\).
- \(\pi<22/7\), and \(\exp(23/20)\ge\sum_{j=0}^5(23/20)^j/j!>22/7\); hence \(\log\pi<23/20\).
- \(\pi<22/7\) gives \(\pi/2<11/7\).
- \(\log2<52/75\) gives \(3\log2<52/25\).
- For \(0<x<1\), \(\sinh x-x\le x^3/[6(1-x^2)]\), so at \(x=9/25\),
\(2(\sinh x-x)\le 243/13600<9/500\).
- \(\log2<7/10\) and \(\sqrt2>7/5\) give \((\log2)/\sqrt2<1/2\).

All purely rational comparisons above were independently executed and pass. The transcendental comparison lemmas, the Fourier transform result and the moment remainder require independent proof/formalization, not a numerical assertion.

## 5. Strict high-frequency positivity and negative index ≤12

Combining (4), (12), and (14) gives, for EVERY nonzero real \(f\in V_L\) satisfying the 12 moments (8),
\[
\begin{aligned}
 W(f)
 &>\left[\frac{593}{100}\frac{299}{300}-\frac{59}{10}\right]\|f\|_2^2\\
 &=\boxed{\frac{307}{30000}\|f\|_2^2>0.}\tag{15}
\end{aligned}
\]

Because \(\mathcal V\) is the intersection of only **12 kernels** of linear functionals, it has codimension at most 12. Any negative-definite subspace of dimension 13 would contain a nonzero vector in \(\mathcal V\), contradicting (15). Therefore the actual fixed-window Weil form has
\[
\boxed{\qquad n_-(W|_{V_{18/25}})\le12.\qquad}\tag{16}
\]

This proof **avoids** the previous compact-operator eigenvalue machinery altogether; the explicit polynomial moment constraints substitute for the abstract low-frequency spectral subspace. The result is valid even without proving the Hilbert completion, since all calculations take place directly on smooth compact-support tests.

Parity refines the statement: the complete form commutes with \(f(x)\mapsto f(-x)\), and the 12 moment constraints split into 6 even moments and 6 odd moments. Thus on the even and odd parity sectors separately, the same argument bounds negative index by at most 6 (the opposite-parity moments vanish automatically).

## 6. Lean formalization and future research

**Priority 1 (smallest independent theorem):** formalize the real Cauchy–Schwarz edge-overlap lemma for translations \(L/2\le t<L\) on support width L, and derive
\(-2v A_f(t)\ge-v\|f\|_2^2\) for \(v\ge0\).
This lemma is reusable for every *first prime entering a rung*.

**Priority 2:** formalize the 12 vanishing-moment Fourier Taylor remainder and the explicit finite rational 100-term series bound. A finite sum normalized as in (7) is compatible with \`norm_num\`/ring tactics but may require a separate arithmetic proof certificate for practical Lean performance.

**Priority 3:** close the real-place Fourier multiplier identity and its high-frequency lower bound for smooth compact-support f. Match \`ArchimedeanFloor.lean\` normalization and the \`zq\` digamma symbol exactly.

**Priority 4:** prove the concrete \(M_-<59/10\) inequalities, avoiding new numerical axioms. \(\gamma<29/50\) follows by the existing harmonic bound at n=256 with a weak \(\log2\) rational bound.

**Priority 5:** assemble (15) and dimension count (16) for the actual Weil form, no circular Gram square root, no RH premise. Then search within the 12-dimensional complement for a *positive* certificate. A 12-dimensional negative-index upper bound does NOT reduce the proof to checking twelve arbitrary f: the complete high/low block and mixed couplings must be controlled, possibly by a Schur complement with certified operator bounds.

**Scope:** This result is an **analytic derivation and exact rational check**, not an audited Lean theorem and not a proof of RH. It improves an upper bound on the negative index in one finite window; it does not show the index is zero, does not give a uniform all-L bound, and does not identify zeros with Hilbert spectral atoms.

Companion exact arithmetic receipt:
\`experiments/abel_prime_common_map/check_first_prime_moment12.py\`.
