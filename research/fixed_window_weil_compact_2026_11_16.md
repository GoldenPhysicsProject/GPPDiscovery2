# Fixed-window Weil form as positive archimedean energy plus a compact perturbation

**Research note, 2026-11-16.** GPT seat, GPPDiscovery2. Mathematical draft for Turbo audit, then Claude/Verify formalization. No RH claim. This is a continuation of PR #29's common Abel–Cesàro map and bounded \(B_N\)-completion. No changes to submitted manuscripts.

## 0. Objects and source cross-check

Work in the real Hilbert space \(L^2(\mathbb R)\). Let \(L>0\), \(I_L=[-L/2,L/2]\), and \(V_L=C_c^\infty(\mathbb R,\mathbb R)\) with support in \(I_L\). Let \(T_t f(x)=f(x-t)\) and \(A_f(t)=\int_{\mathbb R} f(x)f(x-t)\,dx\).

The exact source definitions and identities are in GPPVerify main:

- \`RiemannHypothesis/ArithmeticReflectionPositivity.lean\`: \(W(f)=\mathrm{pole}(A_f)+A_\infty(A_f)-\mathrm{primeSide}(A_f)\).
- \`ArchimedeanFloor.lean\`, \`RungZeroPositivity.lean\`: \(A_\infty(A_f)=C_\infty \|f\|_2^2+2\int_0^\infty w(t)(\|f\|_2^2-A_f(t))\,dt\), initially normalized and then scaled (normalization and integrability already checked on smooth compact-support functions).
- \`BNPositivity.lean\`: \(\mathrm{pole}(A_f)=2(C_f^2-S_f^2)\).
- \`ShiftPresentation.lean\`: exact finite-prime regrouping and cutoff-independence.

Here
\[
  C_\infty=-\gamma-\log\pi-\frac{\pi}{2}-3\log2,\quad
  w(t)=\frac{e^{-t/2}}{1-e^{-2t}}\quad(t>0),
\]
and
\[
 C_f=\int f(x)\cosh(x/2)\,dx,\qquad
 S_f=\int f(x)\sinh(x/2)\,dx.
\]
For \(n=p^k\), \(\Lambda(n)=\log p\), and otherwise \(\Lambda(n)=0\).

All exact results below refer to this specific completed Weil form, not an analogous positive model.

## 1. Exact positive kinetic decomposition: no hidden arithmetic positivity

Define
\[
 (\mathscr D f)(t,x)=\sqrt{w(t)}[f(x)-f(x-t)]
 \quad\text{in } L^2((0,\infty)\times\mathbb R,dt\,dx)
\]
and \(\mathcal E(f,g)=\langle\mathscr D f,\mathscr D g\rangle\), \(\mathcal E(f)=\mathcal E(f,f)\).

For \(f\in V_L\) the energy is finite: as \(t\downarrow0\), \(w(t)=O(t^{-1})\) and \(\|f-T_tf\|_2=O(t\|f'\|_2)\); as \(t\to\infty\), \(w(t)=O(e^{-t/2})\) and \(\|f-T_tf\|_2\le2\|f\|_2\).

The elementary identity
\[
 \|f-T_tf\|_2^2=2[\|f\|_2^2-A_f(t)]
\]
then turns the *actual* real-place term into
\[
\boxed{\quad
 A_\infty(A_f)=C_\infty\|f\|_2^2+\|\mathscr D f\|_2^2.\quad} \tag{1}
\]

For every integer \(N\) with \(L<\log(N+1)\), the original Weil form is exactly
\[
\boxed{
 W(f)=\mathcal E(f)
   +C_\infty\|f\|_2^2+2 C_f^2-2 S_f^2
   -2\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}A_f(\log n).}\tag{2}
\]
The summand vanishes for \(\log n>L\), so the expression is independent of every admissible \(N\). This is an identity on *one fixed real test domain* including prime, gamma, and pole with their correct signs. Mixed bilinear forms follow by polarization of (1)–(2).

A different exact two-positive-space presentation also follows from GPPVerify's \(\Phi_p\) regrouping, when \(\theta(N)+C_\infty\ge0\):
\[
\begin{aligned}
\mathcal A_N f&=\big(\sqrt{\theta(N)+C_\infty}\,f,\ \mathscr D f,\ \sqrt2\,C_f\big),\\
\mathcal B_N f&=\big((\sqrt{w_p}\Phi_p f)_{p\le N},\ \sqrt2\,S_f\big),\\
W(f)&=\|\mathcal A_N f\|^2-\|\mathcal B_N f\|^2,\quad
w_p=(\log p)(1-p^{-1}). \tag{3}
\end{aligned}
\]
All entries of both maps are independently explicit and linear. Unlike the earlier \(B_N\) construction, the source positive space is manifestly a sum of squares; no positivity of \(B_N\), Weil or RH is needed to define it. Contractivity \(\|\mathcal B_N f\|\le\|\mathcal A_N f\|\) remains exactly the unproved Weil positivity inequality. Neither the negative sinh pole nor the prime mass defect is dropped.

## 2. A fixed, cutoff-INDEPENDENT Hilbert metric

The energy alone controls \(L^2\) on every fixed-width test space. If \(t>L\), then \(f\) and \(T_tf\) have disjoint supports, so
\[
 \|\mathscr D f\|_2^2\ \ge\ 
 k(L)\|f\|_2^2,\qquad k(L):=2\int_L^\infty w(t)\,dt>0. \tag{4}
\]
With \(z=e^{-L/2}\in(0,1)\), direct integration gives the exact, elementary expression
\[
\boxed{\quad k(L)=\log\frac{1+z}{1-z}+2\arctan z.\quad} \tag{5}
\]

Let \(\mathcal H_L\) be the Hilbert completion of \(V_L\) under \(\|\mathscr D f\|_2\). By (4), the inclusion \(j_L:\mathcal H_L\to L^2(I_L)\) extends boundedly, with \(\|j_L\|\le k(L)^{-1/2}\). **This metric depends on L but NOT on prime cutoff N and is constructed from the already proved positive real-place term.** No shift of an N-dependent \(B_N\) norm is being made.

The important additional statement is that this inclusion is COMPACT.

## 3. Fourier symbol of the real-place energy

Use the unitary Fourier transform
\(\widehat f(\xi)=(2\pi)^{-1/2}\int_\mathbb R f(x)e^{-i\xi x}dx\).
Plancherel and Tonelli yield
\[
 \mathcal E(f)=\int_\mathbb R a(\xi)|\widehat f(\xi)|^2d\xi,\qquad
 a(\xi)=2\int_0^\infty w(t)(1-\cos \xi t)\,dt. \tag{6}
\]
Expand the positive geometric series
\[
 w(t)=\sum_{k\ge0}e^{-(2k+1/2)t}.
\]
Since each integrand \(e^{-(2k+1/2)t}(1-\cos\xi t)\) is nonnegative, Tonelli is legitimate; the elementary Laplace transform gives
\[
\boxed{
 a(\xi)=2\sum_{k=0}^\infty
  \frac{\xi^2}{(2k+1/2)[(2k+1/2)^2+\xi^2]}.
}\tag{7}
\]
Equivalently, by the classical series for the digamma function,
\[
 a(\xi)=\operatorname{Re}\psi(1/4+i\xi/2)-\psi(1/4).\tag{8}
\]
Since \(\psi(1/4)=C_\infty+\log\pi\), (1) and (8) reproduce the actual \(\operatorname{Re}\psi(1/4+i\xi/2)-\log\pi\) archimedean symbol in Verify's \`ArchimedeanFrequencySplit.lean\`, independently fixing the normalization.

Every summand in (7) is nondecreasing in \(|\xi|\). Furthermore,
\[
\boxed{\quad a(R)\ \uparrow\ \infty\quad(R\to\infty).\quad}\tag{9}
\]
Indeed, for any fixed integer \(M\), as \(R\to\infty\) the first \(M\) summands tend to \(2/(2k+1/2)\); their sum diverges as \(M\to\infty\). No RH, PNT or zero data enters.

For any \(R>0\), (6)–(9) give the uniform Fourier-tail inequality
\[
 \int_{|\xi|>R}|\widehat f(\xi)|^2\,d\xi
 \ \le\ \frac{\mathcal E(f)}{a(R)}. \tag{10}
\]

### Compactness proof

The low-frequency Fourier restriction
\(S_R:L^2(I_L)\to L^2([-R,R])\),
\[
(S_R f)(\xi)=(2\pi)^{-1/2}\int_{I_L}e^{-i\xi x}f(x)dx
\]
is Hilbert–Schmidt: its squared kernel norm is exactly \(LR/\pi\). Hence it is compact. On an \(\mathcal H_L\) unit ball, (10) makes the high-frequency \(L^2\) tail uniformly small as \(R\to\infty\). For fixed \(R\), the low-frequency part is precompact because \(S_R\) is Hilbert–Schmidt. Therefore its image in \(L^2(\mathbb R)\) is totally bounded. The embedding \(j_L\) is compact. This is a direct Fourier cutoff proof, not an appeal to a positivity assumption.

## 4. Weil form = identity plus a compact selfadjoint perturbation

Because the support of \(f\) is \(I_L\), put
\[
 \mathcal P_L=\{n\ge2:\log n\le L,\ \Lambda(n)>0\},
 \quad v_n=\Lambda(n)n^{-1/2},\quad t_n=\log n.
\]
This is a finite set. Let \(P_I\) denote restriction/compression to \(L^2(I_L)\), and \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\) on \(I_L\). The real-space selfadjoint bounded operator
\[
 K_L=C_\infty I+2|c\rangle\langle c|-2|s\rangle\langle s|
     -\sum_{n\in\mathcal P_L}v_nP_I(T_{t_n}+T_{-t_n})P_I \tag{11}
\]
has
\[
 W(f)=\|\mathscr D f\|_2^2+\langle f,K_Lf\rangle_{L^2(I_L)}. \tag{12}
\]
The pole is EXACTLY rank two with one positive and one negative channel. Every prime kick is the actual compressed translation with the correct von Mangoldt weight.

The explicit operator-norm bound
\[
\begin{aligned}
 \|K_L\|&\le M_L,\\
 M_L&:=|C_\infty|+4\sinh(L/2)+2\sum_{n\in\mathcal P_L}v_n
 \quad(<\infty), \tag{13}
\end{aligned}
\]
uses \(\|c\|_2^2=\sinh(L/2)+L/2\),
\(\|s\|_2^2=\sinh(L/2)-L/2\),
and \(\|T_t\|_{L^2\to L^2}=1\).

The compact embedding \(j_L\) makes
\(B_L=j_L^*K_Lj_L\) a COMPACT selfadjoint operator on \(\mathcal H_L\), and
\[
\boxed{\quad W(f,g)=\langle f,(I+B_L)g\rangle_{\mathcal H_L}\quad}
 \tag{14}
\]
for \(f,g\in V_L\) and by continuity in the energy completion. Therefore the negative index of the fixed-width Weil form is FINITE. The possible eigenvalue \(-1\) of \(B_L\) has finite multiplicity. The result makes no assertion that the negative index is zero.

## 5. Explicit computable upper bound on the negative index

Compactness is not the whole conclusion. The Hilbert–Schmidt trace of \(S_R\) gives a quantitative finite-codimension certificate.

The positive trace-class operator \(S_R^*S_R\) on \(L^2(I_L)\) has
\[
 \operatorname{Tr}(S_R^*S_R)=\|S_R\|_{\rm HS}^2=LR/\pi.
\]
List its eigenvalues in nonincreasing order. Remove the span \(E_m\) of its first \(m\) eigenvectors. For any \(f\perp E_m\),
\[
 \|S_Rf\|_2^2\le\frac{LR}{\pi(m+1)}\|f\|_2^2. \tag{15}
\]
Then by (6)–(10),
\[
 \mathcal E(f)\ge
 a(R)\left(1-\frac{LR}{\pi(m+1)}\right)\|f\|_2^2, \tag{16}
\]
and, using (12)–(13),
\[
 \boxed{\quad W(f)\ge
 \left[
 a(R)\left(1-\frac{LR}{\pi(m+1)}\right)-M_L
 \right]\|f\|_2^2,\quad f\in V_L\cap E_m^\perp.\quad}\tag{17}
\]

Pick ANY \(R>0\) with \(a(R)>2M_L\), which exists by (9), and then take
\[
 m=\left\lceil\frac{2LR}{\pi}\right\rceil.
\]
The right-hand side of (17) is STRICTLY positive for nonzero \(f\in V_L\cap E_m^\perp\). By dimension counting, any negative-definite subspace of the Weil form has dimension at most \(m\).

**Unconditional quantitative theorem:**
\[
\boxed{\quad
  n_-(W|_{V_L})\le
  \left\lceil\frac{2LR}{\pi}\right\rceil
  \quad\text{whenever }a(R)>2M_L.\quad}\tag{18}
\]

The estimate is intentionally coarse. Its role is to replace an open-ended infinite-dimensional search with a finite, precisely specified bandlimiting/Galerkin obstruction at each fixed \(L\). It does NOT certify that the finite obstruction is absent. No uniform bound in \(L\) is claimed, and off-line zeros, if they exist, could force a negative direction at sufficiently large width without contradicting (18).

## 6. Parity and the one negative pole channel

On the centered interval \(I_L\), reflection \(Rf(x)=f(-x)\) commutes with the selfadjoint energy operator, the compression of \(T_t+T_{-t}\), and the real-place scalar term. Since \(c\) is even and \(s\) is odd, writing \(f=f_e+f_o\) gives the exact orthogonal decomposition \(W(f)=W(f_e)+W(f_o)\):
\[
\begin{aligned}
W(f_e)&=\mathcal E(f_e)+C_\infty\|f_e\|_2^2
      +2 C_{f_e}^2-2\sum_n v_n A_{f_e}(t_n),\\
W(f_o)&=\mathcal E(f_o)+C_\infty\|f_o\|_2^2
      -2 S_{f_o}^2-2\sum_n v_n A_{f_o}(t_n).
\end{aligned}\tag{19}
\]
Thus the negative rank-one pole lies entirely in the odd sector. The even sector has a positive rank-one pole, but the scalar \(C_\infty\) and prime correlations remain signed, so this alone does not prove even positivity.

## 7. What this changes in our RH strategy

1. The SOURCE Hilbert metric is the **same for every cutoff N** at fixed width. It is the physical/arithmetical real-place Dirichlet form, not an invented equivalent norm.
2. The prime, mass and pole terms are bounded \(L^2\) perturbations, hence COMPACT in this stronger metric. A high-frequency negative tower at one fixed width is impossible.
3. We have an explicit, although very loose, finite-dimensional upper bound (18). This bypasses the **RungStepCoupling** induction mechanism in a mathematically precise sense: the next proof can attack each width directly without propagating the smallest eigenvalue of a previous rung. The all-width uniform problem remains.
4. A practical strategy is to certify the finite low-band matrix *with a rigorous tail bound* from (17), including all mixed pairings and exact \(\Gamma\)/prime/pole contributions. Floating-point positivity alone is not a proof. The low-band matrix is the prolate-spheroidal concentration operator \(S_R^*S_R\), a canonical frequency-band projector rather than a tailored Gram square root.
5. After auditing the fixed-width theorem, ask whether its low-band negative index can be bounded by **zero uniformly in L** using an arithmetic or reflection-positivity mechanism. That is still the RH-strength missing step.

## 8. Turbo/Claude formalization handoff

Stage A (uses existing Lean objects): exact real-place energy identity (1), pole identity (already proved), finite-prime compressed-shift identity, and two-positive map (3). Keep the real test space as \`ContDiff ℝ ∞\` (not the vacuous analytic \`⊤\` class).

Stage B: energy integrability, exact lower bound (4), tail evaluation (5), polarization, real Hilbert completion \(\mathcal H_L\), cutoff-independent embedding.

Stage C: Fourier-Plancherel identity (6), nonnegative series (7), monotonicity/divergence (9), Fourier-tail estimate (10). Digamma identity (8) is useful for normalization, not needed for compactness.

Stage D: compactness of the finite-interval to finite-band Fourier restriction (Hilbert–Schmidt kernel), compactness of \(j_L\), operator (11) and compact selfadjoint \(B_L\); fixed-width negative index finite.

Stage E: trace-class \(S_R^*S_R\), (15)–(18), and parity (19). Keep the exact width \(L\), actual \(\Lambda(n)\) support and prime powers, and the correct signs throughout. Verify against \`F_theta\` deformation, oblique compression and off-line Abel regulator controls.

This note is an **analytic derivation**, not a Lean-verified theorem or a proof of RH. For the previous Abel carrier map, see \`research/abel_prime_common_map_2026_11_16.md\` in the same PR.


### Sharper, optimized index bound (important for usable certification)

The condition \(a(R)>2M_L\) is merely a convenient sufficient choice. Solving the **actual** positivity condition (17), for any \(R>0\) with \(a(R)>M_L\), gives
\[
 m+1>\frac{LR}{\pi}\frac{a(R)}{a(R)-M_L}. \tag{20}
\]
Consequently the sharper, fully explicit theorem is
\[
\boxed{\quad
 n_-(W|_{V_L})\le
 m_L(R):=\left\lceil\frac{LR\,a(R)}
 {\pi(a(R)-M_L)}\right\rceil
 \quad \text{for every }R>0\text{ with }a(R)>M_L.\quad} \tag{21}
\]
One can minimize this bound over \(R\). Unlike (18), it does not throw away half the available high-frequency energy.

**Uncertified floating-point scale check (mpmath digamma, not interval arithmetic):**

| Width \(L\) | \(M_L\) upper bound | Approximate optimizing \(R\) | Bound \(m_L(R)\) |
|---:|---:|---:|---:|
| 0.125 | 5.6223462 | 19.20 | 6 |
| 0.72 (first prime 2) | 7.8237477 | 178.85 | 399 |
| 1.0 (prime 2 only) | 8.4368228 | 332.22 | 1094 |
| 2.0 | 15.9254566 | 618584 | 7,037,062 |

These integers illustrate the *size* of the bound, not certified negative indices. For \(L=0.72\), the earlier easy bound with \(a(R)>2M_L\) was approximately \(83{,}542\), so the optimization matters. The \(L=0.125\) case is already unconditionally positive in Verify; this new bound is not an improvement to that positivity theorem. For certification one must choose rational/directed-interval enclosures proving both \(a(R)>M_L\) and the strict right-hand inequality in (17), not trust the floated optimum.

**Caution about \(m\):** The trace bound uses the *full* Fourier concentration operator \(S_R^*S_R\) with the real interval \(I_L\); truncating its eigenspace in a finite numerical basis without a certified tail is NOT sufficient. The identities (15)–(21) are analytic, with the numerical table only as a diagnostic.
