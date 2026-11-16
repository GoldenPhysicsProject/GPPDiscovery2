# First-prime Weil negative index at most SIX: Legendre Fourier tail

GPT research seat | 2026-11-16 | Discovery2 | Analytic proof draft with exact rational subcertificate, NOT Lean verified and NOT an RH proof.

**Result:** For the exact GPPVerify real completed Weil form \(W(f)=\mathrm{pole}(A_f)+A_\infty(A_f)-\mathrm{primeSide}(A_f)\) on \(C_c^\infty([-9/25,9/25];\mathbb R)\), the negative index is at most **six**. More explicitly, for every nonzero f whose SIX moments \(\int_I x^j f(x)\,dx=0\), j=0,...,5, vanish,
\[
\boxed{ W(f)>\frac{307}{30000}\|f\|_{L^2}^2>0. }
\]
The moment conditions are an explicit six-codimensional subspace. By dimension counting, a negative-definite subspace of dimension seven cannot exist. The even and odd parity sectors have negative index at most three each.

This improves the 12-moment theorem in \`research/first_prime_moment_12_2026_11_16.md\`, which used a *pointwise* Taylor remainder; the earlier 650-dimensional concentration-trace bound is superseded. No positivity of the full Weil form is assumed or established.

## 1. Reuse the exact arithmetic/archimedean input

At width \(L=18/25=0.72\), \(\log2<L<\log3\), only the first prime \(n=2\) appears in GPPVerify's explicit Weil form. Set
\[
\mathcal E(f)=\int_{t>0}\frac{e^{-t/2}}{1-e^{-2t}}\|f-T_t f\|_2^2\,dt,\qquad
C_\infty=-\gamma-\log\pi-\pi/2-3\log2.
\]
With \(\ell=\log2\), \(v=\log2/\sqrt2\), \(C_f=\int f(x)\cosh(x/2)\,dx\) and \(S_f=\int f(x)\sinh(x/2)\,dx\), the ACTUAL Weil form is
\[
W(f)=\mathcal E(f)+C_\infty\|f\|_2^2+2C_f^2-2S_f^2-2v\,A_f(\ell),
\quad A_f(t)=\langle f,T_tf\rangle.
\]

If \(L/2\le\ell<L\), the two spatial intervals coupled by \(A_f(\ell)\) are disjoint, so
\(|A_f(\ell)|\le\frac12\|f\|_2^2\). The negative rank-one pole satisfies
\(2S_f^2\le2(\sinh(L/2)-L/2)\|f\|_2^2\). Keep the positive cosh pole; do not count it as a negative perturbation. Thus
\[
W(f)\ge\mathcal E(f)-M_-\|f\|_2^2,\quad
M_-=|C_\infty|+2(\sinh(L/2)-L/2)+v.
\]

The same exact rational/transcendental bounds checked in the 12-moment note give
\[
M_-<\frac{29}{50}+\frac{23}{20}+\frac{11}{7}+\frac{52}{25}
      +\frac9{500}+\frac12
=\frac{5162}{875}<\frac{59}{10}.
\]
Sources: Verify \`ArchimedeanFloor\`, \`ArithmeticReflectionPositivity\`, \`BNPositivity\`, \`ShiftPresentation\`; Euler bound via H256-8log2; weak rational bounds log2>6931/10000, log2<52/75 and <7/10, pi<22/7, exp(23/20)>pi; sinh series.

The positive real-place Fourier multiplier, in the unitary transform convention, is
\[
\mathcal E(f)=\int_{\mathbb R}a(\xi)|\hat f(\xi)|^2\,d\xi,\quad
a(\xi)=2\sum_{k\ge0}\frac{\xi^2}{(2k+1/2)[(2k+1/2)^2+\xi^2]}.
\]
It is nondecreasing in \(|\xi|\). The first 100 positive rational terms at \(R=11\) give, by exact arithmetic,
\[
a(11)>\frac{593}{100}.
\]

## 2. The key new Legendre estimate, with NO Bessel-function assumptions

Let \(P_n(t)\) be the ordinary Legendre polynomial on [-1,1], with \(P_0=1\), and let
\[
e_n(x)=\sqrt{\frac{2n+1}{L}}\,P_n(2x/L)\quad (x\in I=[-L/2,L/2]).
\]
These are an orthonormal basis for \(L^2(I)\). If the first m ordinary spatial moments \(\int_I x^j f(x)\,dx\), \(0\le j<m\), vanish, then \(f\perp e_n\) for all \(n<m\).

Set \(z=\xi L/2\). Rodrigues' formula followed by n integrations by parts gives
\[
\int_{-1}^1 e^{-izt}P_n(t)\,dt
 =\frac{(-iz)^n}{2^n n!}\int_{-1}^1 e^{-izt}(1-t^2)^n\,dt.
\]
Taking absolute values and using
\[
\int_{-1}^1(1-t^2)^n\,dt=\frac{2^{2n+1}(n!)^2}{(2n+1)!}
\]
yields the sharp-enough universal bound
\[
\left|\int_{-1}^1 e^{-izt}P_n(t)dt\right|
\le\frac{2|z|^n}{(2n+1)!!}.
\]
Therefore
\[
|\langle e_n,e^{-i\xi\cdot}\rangle_{L^2(I)}|^2
\le L(2n+1)\frac{(|\xi|L/2)^{2n}}{[(2n+1)!!]^2}.
\]

Completeness of the Legendre basis and Bessel's inequality imply, for f perpendicular to \(e_0,\ldots,e_{m-1}\),
\[
|\widehat f(\xi)|^2
\le\frac{L}{2\pi}\|f\|_2^2
 \sum_{n\ge m}(2n+1)\frac{(|\xi|L/2)^{2n}}{[(2n+1)!!]^2}.
\]
**Integrate in \(\xi\) BEFORE bounding the sum.** The factor \(2n+1\) cancels exactly against \(\int_0^R \xi^{2n}d\xi=R^{2n+1}/(2n+1)\). Hence
\[
\boxed{
 \int_{-R}^R|\hat f(\xi)|^2d\xi
 \le \delta_m(L,R)\|f\|_2^2,\quad
 \delta_m(L,R)=\frac{LR}{\pi}
 \sum_{n\ge m}\frac{(RL/2)^{2n}}{[(2n+1)!!]^2}.
}\tag{1}
\]
This formula is an **upper bound** on the actual low-frequency mass, not an equality.

Let \(z_R=RL/2\). Since the consecutive summand ratio is \(z_R^2/(2n+3)^2\), for \(z_R<2m+3\),
\[
\boxed{
 \delta_m(L,R)\le\frac{LR}{\pi}
 \frac{z_R^{2m}}{[(2m+1)!!]^2}
 \frac{1}{1-z_R^2/(2m+3)^2}. }\tag{2}
\]
Everything on the right becomes rational when L,R,m are rational/integer, apart from \(1/\pi\), for which \(\pi>3\) suffices.

## 3. Exact six-moment arithmetic certificate

Choose \(L=18/25\), \(R=11\), \(m=6\). Then
\[
 z_R=\frac{99}{25},\qquad
 (2m+1)!!=13!!=135135,\qquad
 \frac{z_R^2}{(2m+3)^2}=\frac{1089}{15625}<1.
\]
The following rational inequality was executed and confirmed with \`fractions.Fraction\`:
\[
 \frac{(18/25)\cdot11}{3}
 \frac{(99/25)^{12}}{135135^2}
 \frac1{1-1089/15625}
 \ <\ \frac1{300}.
\tag{3}
\]
No floating-point comparison is used in (3). Thus for any f with six vanishing moments,
\[
 \mathcal E(f)
 \ge a(11)\left(\|f\|_2^2-\int_{-11}^{11}|\hat f(\xi)|^2d\xi\right)
 >\frac{593}{100}\frac{299}{300}\|f\|_2^2.
\]
Subtracting the full negative bound \(M_-<59/10\) gives
\[
\boxed{
 W(f)>
 \left(\frac{593}{100}\frac{299}{300}-\frac{59}{10}\right)\|f\|_2^2
 =\frac{307}{30000}\|f\|_2^2>0
 \quad(f\ne0).
}\tag{4}
\]

The six moment functionals have codimension at most six, proving
\[
\boxed{n_-(W|_{V_{18/25}})\le6.}\tag{5}
\]

Under parity \(f(-x)=\pm f(x)\), only three of the six moment functionals are independent (powers 0,2,4 for even f and 1,3,5 for odd f); hence each parity block has negative index at most three.

## 4. Independent numerical diagnostics, not proof of positivity

A second, independent x-space computation for the first Dirichlet sine mode confirms
\[
 \mathcal E(f_1)\approx4.20154655653433,\quad C_\infty\approx-5.37218341922567,\quad
 2C_{f_1}^2\approx1.17440296554373,\quad 2vA_{f_1}(\log2)\approx0.00016706859054,
\]
so \(W(f_1)\approx0.0035990342618533>0\).
The independently programmed Fourier/digamma/Galerkin calculation reproduces this diagonal and finds minimum Ritz eigenvalues (float only): 0.000961762 (30 sine modes), 0.000912558 (50), 0.000894675 (80), 0.000879537 (120). All positive in the tested subspaces, but this is **not** an all-tests positivity certificate; the minima decrease with basis size.

The numerical margin is tiny, so Turbo must demand certified mixed-term and infinite-tail control before treating any finite matrix as proof.

## 5. Next exact proof target: the 6×6 Schur complement

On the fixed-width archimedean energy Hilbert space \(\mathcal H_L\) from the compactness note, the six moment functionals are continuous by the proved \(L^2\) embedding. Let \(H_0=\bigcap_{j<6}\ker\mu_j\), and let \(P=H_0^{\perp_{\mathcal E}}\), \(\dim P=6\).

Because the high block \(W|_{H_0}\) has a **strict** positive lower bound relative to the energy norm (deduced from \(a(11)(1-\delta)>M_-\)), its associated operator \(D\) on \(H_0\) is boundedly invertible. In the orthogonal energy decomposition \(\mathcal H_L=P\oplus H_0\), write
\[
I+j_L^*K_Lj_L=
\begin{pmatrix}A&B^*\\ B&D\end{pmatrix},\qquad D>0.
\]
The *complete actual Weil form* is nonnegative on \(V_L\) **if and only if** the finite \(6\times6\) Schur complement
\[
 \boxed{S=A-B^*D^{-1}B\ge0.}
\]
This is a correct finite-dimensional reduction with strictly positive high block. It does NOT prove S≥0. The matrix entries and the mixed block B must be constructed from the exact prime, pole, and archimedean form. Do not substitute a numerical 6×6 principal minor for S; the correction \(B^*D^{-1}B\) is essential. An audited effective bound or exact factorization of S is the next research target.

## 6. Turbo/Claude handoff

- Independent audit of the real-place normalization, first-prime edge-overlap lemma, Legendre Rodrigues integral, integrated Fourier-tail bound (1)-(2), rational receipt and parity count.
- The \`ExpTaylorImaginary.lean\` module in Verify already PROVES a weaker moment-Taylor inequality. The new step is replacing monomial truncation with Legendre orthogonal expansion and **integrating before** the tail bound. \`NeutralLegendreBasis.lean\` is a different finite shifted-Legendre construction and does not itself supply the full Rodrigues/Parseval bridge.
- First Lean target: exact rational statement (3) and the edge-overlap bound; second target: Fourier Legendre coefficient and geometric tail; final target: first-prime W inequality (4) and index (5).
- Then construct and rigorously bound the true mixed-block 6×6 Schur complement. No hidden positivity hypothesis; no RH claim.

Companion reproducibility script: \`experiments/abel_prime_common_map/check_first_prime_legendre6.py\`.

**Status:** independent rational arithmetic PASS, analytic derivation deposited, but neither Turbo audited nor Lean compiled. Global RH positivity remains OPEN.
