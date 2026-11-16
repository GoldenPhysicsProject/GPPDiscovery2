# A quantitative Weil scale-transport theorem and a rigorous first propagation step

**GPPDiscovery2, 2026-11-16.** New mathematical derivation, formalization/audit still required. Relies on the named, unconditional GPPVerify theorem \`GppRungZeroWide.weilForm_autocorr_ge_wide\` at width L₀=1/8. This is a **general finite-step induction rule**, not an all-width RH proof.

## 1. Put every width on one fixed Hilbert space

Use the reference interval \(J=[-1/2,1/2]\), \(g\in C_c^\infty(J;\mathbb R)\), and unitary width dilation
\[
 f_L(x)=L^{-1/2}g(x/L),\qquad \operatorname{supp}(f_L)\subset I_L=[-L/2,L/2].
\]
Write \(\mathcal E_L(g)=\mathcal E(f_L)\) for the positive real-place energy, and \(\mathcal W_L(g)=W(f_L)\) for the ACTUAL completed Weil quadratic, prime/pole/gamma included. The source normalization is fixed in GPPVerify \`ArchimedeanFloor.lean\`, \`BNPositivity.lean\` and \`ArithmeticReflectionPositivity.lean\`.

Let \(a(r)=2\sum_{k\ge0}r^2/[(2k+\frac12)((2k+\frac12)^2+r^2)]\) for \(r\ge0\), and \(K(L)=2\int_L^\infty w(t)dt\), \(w(t)=e^{-t/2}/(1-e^{-2t})\). Fourier/Plancherel and zero extension imply
\[
 \mathcal E_L(g)=\int_{\mathbb R}a(|\xi|/L)|\hat g(\xi)|^2d\xi,\qquad
 \mathcal E_L(g)\ge K(L)\|g\|_2^2.
 \tag{1}
\]

The pole is
\[
 \mathcal P_L(g)=2L\,A_+(L)A_-(L),\qquad
 A_\pm(L)=\int_Jg(t)e^{\pm Lt/2}dt,
 \tag{2}
\]
and the real prime side is
\[
 \mathcal S_L(g)=2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
    A_g(\log n/L),\qquad A_g(h)=\langle g,T_hg\rangle_{L^2(\mathbb R)}.
 \tag{3}
\]
Only finitely many n with \(\log n<L\) contribute at each L. The completed Weil form is
\[
 \boxed{\quad\mathcal W_L(g)=\mathcal E_L(g)+C_\infty\|g\|_2^2
     +\mathcal P_L(g)-\mathcal S_L(g).\quad}\tag{4}
\]

## 2. Uniform in-frequency bound for the kinetic dilation

The positive Fourier symbol has derivative
\[
 r a'(r)=4\sum_{k\ge0}
\frac{r^2(2k+\frac12)}{[(2k+\frac12)^2+r^2]^2},\qquad r>0.
\]
The elementary split below proves \(\boxed{0\le r a'(r)<12}\) for all r>0:

- If \(r\le1\): the k=0 summand is \(\le2\), and the k≥1 tail is
\(\le4\sum_{k\ge1}(2k)^{-3}
 =\tfrac12\sum_{k\ge1}k^{-3}<3/4\).
- If \(r\ge1\): on \(\lambda_k=2k+1/2\le r\), sum terms \(\le4\lambda_k/r^2\). There are at most \(r/2+1\) such indices, so the subtotal is \(\le2+4/r\).
On \(\lambda_k>r\), sum terms \(\le4r^2/\lambda_k^3\).
With the first such \(\lambda>r\) and step 2, \(\sum_{\lambda_k>r}\lambda_k^{-3}
\le r^{-3}+(4r^2)^{-1}\); the subtotal is \(\le1+4/r\).
The total is \(\le3+8/r\le11\).

By the fundamental theorem of calculus in \(\log r\),
\[
 |a(r)-a(r')|\le12|\log(r/r')|.
\]
Applying this under Fourier/Plancherel gives the **unconditional kinetic transport bound**
\[
\boxed{
 |\mathcal E_L(g)-\mathcal E_{L_0}(g)|
 \le12\left|\log\frac L{L_0}\right|\|g\|_2^2.
}\tag{5}
\]

## 3. Explicit uniform continuity modulus for *all* old/new prime channels

Fix L,L₀>0, \(L_*=\max(L,L_0)\) and
\[
 V_*:=\sum_{\substack{n\ge2\\\log n\le L_*}}\frac{\Lambda(n)}{\sqrt n}
 \quad(<\infty).
\]
The Fourier representation of A_g gives, for every frequency R>0 and h,h' real,
\[
\begin{aligned}
 |A_g(h)-A_g(h')|
 &\le R|h-h'|\|g\|_2^2
       +2\int_{|\xi|>R}|\hat g(\xi)|^2d\xi\\
 &\le\left[
   \frac{R|h-h'|}{K(L_0)}
     +\frac2{a(R/L_0)}
   \right]\mathcal E_{L_0}(g).
\end{aligned}\tag{6}
\]
The second inequality uses (1) and monotonicity of a. This is a **complete infinite-frequency tail bound**. It holds even if one shift is \(\ge1\) (where the overlap vanishes) and the other is <1 (where the compressed operator suddenly has L² norm one).

Because \(\log n\le L_*\) for every term in V_*,
\[
|\log n/L-\log n/L_0|
 \le L_* |L^{-1}-L_0^{-1}|.
\]
Thus the entire prime sum obeys
\[
 |\mathcal S_L(g)-\mathcal S_{L_0}(g)|
 \le 2V_*\left[
 \frac{R L_* |L^{-1}-L_0^{-1}|}{K(L_0)}
 +\frac2{a(R/L_0)}
 \right]\mathcal E_{L_0}(g). \tag{7}
\]
This is valid for EVERY finite support width, including crossings of many prime thresholds. It is not an RH equivalent restatement: its right side is explicit in the gamma kernel and von Mangoldt weights only, and proves a quantitative norm-continuity result.

For the pole, since \(|t|\le1/2\) on J,
\(|A_\pm(L)|\le e^{L/4}\|g\|_2\) and
\(|A_\pm'(L)|\le\tfrac14e^{L/4}\|g\|_2\).
Hence
\[
 |\mathcal P_L(g)-\mathcal P_{L_0}(g)|
 \le(2+L_*)e^{L_*/2}|L-L_0|\|g\|_2^2.\tag{8}
\]

Combine (5), (7), and (8); the \(C_\infty\) scalar is width-independent. Define the EXPLICIT modulus
\[
\boxed{
\begin{aligned}
\Omega(L,L_0;R)
={}&\frac{12|\log(L/L_0)|
 +(2+L_*)e^{L_*/2}|L-L_0|}{K(L_0)}
\\
&+2V_*\left[
\frac{R L_*|L^{-1}-L_0^{-1}|}{K(L_0)}
+\frac2{a(R/L_0)}\right].
\end{aligned}}\tag{9}
\]
Then
\[
\boxed{
 |\mathcal W_L(g)-\mathcal W_{L_0}(g)|
 \le\Omega(L,L_0;R)\,\mathcal E_{L_0}(g)
\quad\text{for every smooth supported }g.
}\tag{10}
\]
Taking \(R=|L-L_0|^{-1/2}\) as L→L₀ gives \(\Omega\to0\), because \(a(R/L₀)\to\infty\). There is no norm discontinuity at prime onset in the energy metric, even though the prime shift has an L² operator-norm jump.

## 4. A genuine CONDITIONAL one-step induction algorithm

Suppose at width L₀ we have an independently proved positive coercive margin
\[
 \mathcal W_{L_0}(g)\ge\varepsilon_0\,\mathcal E_{L_0}(g)
 \quad\forall g\text{ supported in J},\quad\varepsilon_0>0.
\tag{11}
\]
For any new width L and frequency R with \(\Omega(L,L_0;R)<\varepsilon_0\), (10) yields
\[
\mathcal W_L(g)\ge
[\varepsilon_0-\Omega(L,L_0;R)]\mathcal E_{L_0}(g).
\]
The kinetic bound (5) and lower coercivity (1) imply
\[
\mathcal E_L(g)\le[1+\rho(L,L_0)]\mathcal E_{L_0}(g),\quad
\rho(L,L_0)=\frac{12|\log(L/L_0)|}{K(L_0)}.
\]
Therefore the exact **propagation recurrence** is
\[
\boxed{
 \varepsilon_{\rm next}
 =\frac{\varepsilon_0-\Omega(L,L_0;R)}
        {1+\rho(L,L_0)}>0,
\qquad
 \mathcal W_L(g)\ge\varepsilon_{\rm next}\mathcal E_L(g).
}\tag{12}
\]
This is a mathematically noncircular step from positivity at one support width to positivity at a strictly larger width, based on source coefficients and explicit error bounds. It can be iterated for as long as its test passes, without pre-assuming positivity of an entire later rung.

**Critically:** it is NOT guaranteed to iterate forever. Margins may shrink toward zero, the prime weight V_* grows, and the step sizes may become summable. All-width positivity requires an additional theorem preventing accumulation of zero crossings or providing an arithmetic lower barrier on the renormalized margin. The recurrence isolates precisely where that RH-strength input is needed.

## 5. One explicit unconditional positive-width extension from the Lean-verified base

GPPVerify \`RungZeroWide.lean\` proves for width \(L_0=1/8=0.125\)
\[
\boxed{
 \mathcal W_{L_0}(g)\ge \frac1{20}\|g\|_2^2
}\tag{13}
\]
for smooth compact-supported real tests, with standard axioms and no \`sorry\`. There are no prime terms at this width. The exact source form is
\(\mathcal W_{L_0}=\mathcal E_{L_0}+K_{\rm bounded,L_0}\), with
\(\|K_{\rm bounded,L_0}\|\le|C_\infty|+4\sinh(1/16)<6\), by the same source estimates in \`BNPositivity.lean\`.
Therefore
\[
 \mathcal E_{L_0}\le\mathcal W_{L_0}+6\|g\|_2^2
 \le121\mathcal W_{L_0},
\]
giving the unconditional **energy-norm** base margin
\[
\boxed{
 \mathcal W_{L_0}\ge\frac1{121}\mathcal E_{L_0}.
}\tag{14}
\]

Let \(L_1=1251/10000=0.1251\), a STRICTLY larger width. Both \(L_0,L_1<\log2\), so \(V_*=0\) in (9). The exact positive tail satisfies \(K(1/8)>4\): letting \(z=e^{-1/16}>15/16\), its logarithmic ratio exceeds 31; \(\log31>16/5\) follows e.g. from
\(e^{16/5}\le(10/9)^{32}<31\);
and \(2\arctan z\ge z>15/16\), hence \(K(1/8)>16/5+15/16>4\).

Moreover
\[
 \log(L_1/L_0)=\log(1251/1250)<1/1250,
\quad L_*<1/4,\quad
(2+L_*)e^{L_*/2}< (9/4)(8/7)=18/7,
\]
using \(e^{1/8}<8/7\).
Consequently, with \(|L_1-L_0|=1/10000\), the exact rational estimates yield
\[
\boxed{
 \Omega(L_1,L_0;R)<\frac{69}{28000},\qquad
 \rho(L_1,L_0)<\frac3{1250}.
}\tag{15}
\]
The arbitrary R is irrelevant because \(V_*=0\).

Substitute (14)–(15) into the recurrence (12):
\[
\frac{1/121-69/28000}{1+3/1250}
 =\frac{98255}{16980656}>\frac1{175}.
\]
Therefore the strengthened concrete theorem is
\[
\boxed{
\forall f\in C_c^\infty([-1251/20000,1251/20000];\mathbb R),\quad
W(f)\ge\frac1{175}\,\mathcal E(f)\ge0.
}\tag{16}
\]

This extends the existing Lean-certified support width \(1/8\) by \(1/10000\) through a **general width-transport theorem**, without assuming arithmetic reflection positivity or RH. It is an analytic theorem candidate with exact rational comparisons, and has NOT been Lean compiled yet. Its significance is the general, reusable recurrence, not the tiny numerical gain.

All rational inequalities in the right-hand side and the n=0-prime propagation were executed exactly using \`fractions.Fraction\` (see the companion script), and the analytic bounds derive from elementary gamma-kernel/Fourier statements. Turbo should independently audit each analytic step before Claude promotes (16) to Verify.

## 6. What is genuinely needed for infinity

This recurrence creates a precise mathematical meaning for “go from one rung to the next indefinitely.” Start with a proven \((L_0,\varepsilon_0)\), compute \(\Omega\), choose L₁ so \(\Omega<\varepsilon_0\), update \(\varepsilon_1\) by (12), and repeat.

To reach \(L\to\infty\), we need to prove **a priori** that some admissible sequence has
\(\sum_k(L_{k+1}-L_k)=\infty\), or construct an invariant lower bound
\(\varepsilon(L)\) that never vanishes. Because the independent prime corrections are not summable, this probably requires a correlated cancellation identity linking the exact resolvent mass defect, pole, gamma and prime terms.

An explicit F_θ deformation with off-line zeros must FAIL any proposed global invariant; merely reproducing the local beta functions or the continuity recurrence is not sufficient.

### Turbo/Claude tasks

1. Formalize generic multiplier derivative bound \(\sup_{r>0}r a'(r)\le12\) and kinetic width transport (5).
2. Formalize generic Fourier autocorrelation translation modulus (6); upstreamable as a Hilbert-space lemma.
3. Formalize actual Weil width modulus (9)–(12) with no ARP/RH premise.
4. Verify the rational single-step extension from \(1/8\) to \(1251/10000\) and the exact \(\varepsilon>1/175\) bound. It is a compact first Lean target.
5. Investigate a **correlated** arithmetic spectral-flow invariant preventing the recurrence's step sizes from collapsing; test an \(F_\theta\) negative control in the same rescaled test family.

**Status:** new analytic rule with a fully explicit nontrivial example; **not yet Lean/CI checked, not an RH proof**.
