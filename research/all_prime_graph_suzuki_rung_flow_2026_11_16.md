# All-prime graph Dirichlet form and a discrete arithmetic running flow

**Date:** November 16, 2026. **Research status:** exact source-derived identities plus independently executed real-space diagnostics. These identities do NOT prove RH. The scalar non-archimedean sign criterion is **prior published work** (Masatoshi Suzuki, 2025); the new work here is a unified operator/width presentation and its application to our GPPVerify arithmetic flow. All Lean transfer remains pending.

### Sources and exact provenance

- GPPVerify \`ArithmeticReflectionPositivity.lean\`, \`ArchimedeanFloor.lean\`, and \`ShiftPresentation.lean\` supply the Weil prime/pole/real-place coefficients. Their \`ARP\` and \`OB6\` remain OPEN.
- Masatoshi Suzuki, **"On variants of Chebyshev's conjecture,"** *Ramanujan Journal* **68**, article **95** (published November 10, 2025), DOI **10.1007/s11139-025-01238-9**, https://link.springer.com/article/10.1007/s11139-025-01238-9 . The paper was corrected December 19, 2025. **Suzuki's Theorem 1 and Corollary 1 already prove the equivalence of eventual nonpositivity of the relevant smoothed prime discrepancy with RH.** Suzuki's \(g_0\), \(g_\infty\), and screw function are used explicitly below. We do NOT claim the scalar criterion, the smoothed weighted prime sum, or its RH equivalence as new discoveries.
- GPP prior Haar/Weil/Schur/Abel notes and our \`prime_threshold_running_coupling_2026_11_16.md\`. The latter gives the local prime-entry beta law but does NOT provide an all-prime positive allocation.

## 1. A single exact sum-of-differences for ALL primes, with no repeated gamma energy

Let \(L>0\), \(I_L=[-L/2,L/2]\), and \(f\in C_c^\infty(I_L;\mathbb R)\). Extend f by zero. Define
\[
A_f(t)=\int_{\mathbb R} f(x)f(x-t)\,dx,\quad
w(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
K(u)=2\int_u^\infty w(t)dt,\quad
v_n=\frac{\Lambda(n)}{\sqrt n},\quad\ell_n=\log n.
\]
Only finitely many n satisfy \(\ell_n<L\). The actual Weil form is
\[
W(f)=E(f)+C_\infty\|f\|_2^2+
2\left(\int_I f(x)e^{x/2}dx\right)
 \left(\int_I f(x)e^{-x/2}dx\right)
-2\sum_{\ell_n<L}v_n A_f(\ell_n),\tag{1}
\]
where \(E(f)=\int_0^\infty w(t)\|f-T_tf\|_{L^2(\mathbb R)}^2dt\) and \(C_\infty=-\gamma-\log\pi-\pi/2-3\log2\).

There is an **exact source-kinetic split**:
\[
\boxed{
\begin{aligned}
E(f)
={}&\underbrace{\int_{I}\int_{\substack{y\in I\\y<x}}
w(x-y)|f(x)-f(y)|^2\,dy\,dx}_{E_{\rm int}(f)\ge0}\\
&+\underbrace{\frac12\int_{I}
\big[K(x+L/2)+K(L/2-x)\big]|f(x)|^2 dx}_{E_{\rm edge}(f)\ge0}.
\end{aligned}}\tag{2}
\]
Each PRIME translation admits an exact completion of squares on its **actual** overlap:
\[
-2v_n A_f(\ell_n)
= v_n\int_{\ell_n-L/2}^{L/2}
 |f(x)-f(x-\ell_n)|^2 dx
-v_n\int_I
 \big[\mathbf 1_{\{x+L/2\ge\ell_n\}}
      +\mathbf 1_{\{L/2-x\ge\ell_n\}}\big]|f(x)|^2dx.\tag{3}
\]
Define the universal weighted Chebyshev staircase
\[
\boxed{\quad V(u)=\sum_{\ell_n\le u}v_n
=\sum_{n\le e^u}\frac{\Lambda(n)}{\sqrt n},\quad u\ge0,\qquad V(u)=0 \ (u<0).\quad}\tag{4}
\]
Let \(d_-(x)=x+L/2\), \(d_+(x)=L/2-x\), and
\[
U_L(x)=C_\infty+\frac12[K(d_-(x))+K(d_+(x))]-V(d_-(x))-V(d_+(x)).\tag{5}
\]
Substituting (2)–(4) into (1) gives the **exact all-prime Haar/graph representation**
\[
\boxed{
\begin{aligned}
W(f)={}&E_{\rm int}(f)
+\sum_{\ell_n<L}v_n\int_{\ell_n-L/2}^{L/2}
      |f(x)-f(x-\ell_n)|^2dx\\
&+\int_I U_L(x)|f(x)|^2 dx
+2\left(\int_I f e^{x/2}\right)\left(\int_I f e^{-x/2}\right).
\end{aligned}}\tag{6}
\]
This is not a formal "Haar square" for the full Weil distribution. It is an exact representation of the actual source form. The first two components are NONNEGATIVE but the potential \(U_L\) is signed and the rank-two pole is indefinite on sign-changing tests. In particular, **there is no automatic global SOS theorem here**. Equation (6) is nevertheless valuable: the positive gamma kinetic energy is allocated ONCE, the complete prime graph is retained, and all signed diagonal mass defects collapse to the single explicit arithmetic potential \(U_L\).

### The potential is one universal running function evaluated at BOTH boundaries

Set
\[
q(u)=\frac12K(u)-V(u),\quad u>0.
\]
Then
\[
\boxed{U_L(x)=C_\infty+q(d_-(x))+q(d_+(x)).}\tag{7}
\]
There is NO separate new arbitrary \(q_n\) at each rung; all widths sample the same single q. Its distributional derivative is exact:
\[
\boxed{\quad dq(u)=-w(u)\,du-\sum_{n\ge2}v_n\,\delta_{\ell_n}(du).\quad}\tag{8}
\]
Consequently q is strictly decreasing and all new prime-power events appear as negative downward jumps. This is an exact unified arithmetic running potential, not a monotone positive energy. Its large negative behavior has to be compensated by the **full prime and gamma Dirichlet forms together with the pole term**; dropping any of those invalidates a global positivity argument.

The exterior gamma potential alone CANNOT pointwise dominate all prime degree terms: \(U_L\) is already negative at some interior points even before primes enter. Thus no induction based solely on \(U_L(x)\ge0\) can work. Functional/spectral compensation is essential.

## 2. Exact renormalization against the pole: a single signed prime discrepancy

The pole term in (1) has the **exact autocorrelation form**
\[
\boxed{
2\left(\int f e^{x/2}\right)\left(\int f e^{-x/2}\right)
=4\int_0^L\cosh(t/2) A_f(t)\,dt.
}\tag{9}
\]
Define the **cumulative centered arithmetic driver**
\[
\boxed{
 D(t)=4\sinh(t/2)-V(t),\qquad
 dD(t)=2\cosh(t/2)\,dt-\sum_{n\ge2}v_n\delta_{\ell_n}(dt).
}\tag{10}
\]
Then **for every smooth supported f**, all prime and pole contributions combine into one Riemann–Stieltjes pairing:
\[
\boxed{
 W(f)=E(f)+C_\infty\|f\|_2^2+
 2\int_{[0,L]}A_f(t)\,dD(t)
 =E(f)+C_\infty\|f\|_2^2
 -2\int_0^L D(t)\,A_f'(t)dt .
}\tag{11}
\]
The final equality uses \(D(0)=0\), \(A_f(L)=0\) and Stieltjes integration by parts. This is the **global prime/pole cancellation performed before taking any absolute value**. It is a different exact presentation from the positive-graph/signed-potential representation (6). Both equations hold simultaneously.

The centered driver obeys a universal **smooth drift + arithmetic jump flow**:
\[
\boxed{
D'(t)=2\cosh(t/2)\quad \text{between prime-power thresholds},\qquad
D(\ell_n^+)-D(\ell_n^-)=-v_n .
}\tag{12}
\]
Unlike the individual-prime relative coupling, D is already the FULL accumulated arithmetic flow. It avoids multiple spending of the gamma energy.

**WARNING:** D is not globally nonnegative. Suzuki (2025) explains, using Littlewood-type oscillations, that the weighted prime discrepancy relative to \(2\sqrt x\) changes sign infinitely often. A monotonicity argument premised on \(D\ge0\) indefinitely is therefore invalid. We have to control its PRIMITIVE rather than its instantaneous sign.

## 3. The flat interval channel: exact all-width scalar RG and Suzuki's published criterion

Take the normalized interval indicator
\[
 f_L(x)=L^{-1/2}\,\mathbf 1_{[-L/2,L/2]}(x).
\]
It is in the real-place **form domain** (although not C_c∞ and not the operator domain), because \(E(f_L)<\infty\) for each L. Smooth approximations in energy norm justify inserting it into W. Its autocorrelation is triangular,
\[
A_{f_L}(t)=(1-t/L)_+,\qquad t\ge0.
\]
Set
\[
 F(L):=L W(f_L),\quad
 H(L):=4(e^{L/2}+e^{-L/2}-2)
 -\sum_{\ell_n<L}v_n(L-\ell_n).
\tag{13}
\]
Then source calculations give
\[
\boxed{
\begin{aligned}
 E(f_L)&=\frac2L\int_0^L t\,w(t)dt + K(L),\\
 \mathrm{Pole}(f_L)&=\frac8L(e^{L/2}+e^{-L/2}-2),\\
 -\mathrm{Prime}(f_L)&=-\frac2L\sum_{\ell_n<L}v_n(L-\ell_n),\\
 F(L)&=LE(f_L)+C_\infty L+2H(L),\\
 H(L)&=\int_0^L D(t)dt .
\end{aligned}}\tag{14}
\]
Differentiate between prime thresholds and extend distributionally:
\[
\boxed{
F'(L)=K(L)+C_\infty+2D(L),\qquad
F''(L)=4\cosh(L/2)-2w(L)
-2\sum_{n\ge2}v_n\delta_{\ell_n}.
}\tag{15}
\]
This is an exact global **sawtooth RG law**: smooth gamma + pole drift and discrete prime-power impulses. F is continuous; F' is piecewise smooth with downward jumps \(-2v_n\). Numerically F' is sometimes NEGATIVE, while the integrated F stayed positive in tested windows. Neither F nor H can be proved nonnegative by monotonicity of its derivative.

### PRIOR LITERATURE: This is precisely Suzuki's screw-function channel

Suzuki (2025), equations (7)–(9), defines
\[
g_0(L)=\sum_{\ell_n<L}v_n(L-\ell_n)
-4(e^{L/2}+e^{-L/2}-2),
\]
and a specific archimedean \(g_\infty(L)\) in terms of \(\Gamma'/\Gamma\) and a Hurwitz–Lerch function. Therefore
\[
\boxed{\quad H(L)=-g_0(L)\quad\text{EXACTLY}.\quad}\tag{16}
\]
More strongly, Suzuki's archimedean term matches
\[
\boxed{\quad LE(f_L)+C_\infty L=-2g_\infty(L).\quad}\tag{17}
\]
One direct proof of (17): differentiate both sides. By Fubini, \(\frac d{dL}[LE(f_L)]=K(L)\); the digamma identity \(\psi(1/4)=-\gamma-\pi/2-3\log2\) gives \(C_\infty=\psi(1/4)-\log\pi\); expanding \(\Phi(e^{-2L},2,1/4)\) as a positive convergent series gives \(-2g_\infty'(L)=C_\infty+e^{-L/2}\Phi(e^{-2L},1,1/4)=C_\infty+K(L)\). Both sides vanish at L=0. Thus (17) is exact, not merely numerical.
Consequently
\[
\boxed{
F(L)=-2[g_0(L)+g_\infty(L)]=-2g_\zeta(L),\qquad
W(f_L)=-2g_\zeta(L)/L .
}\tag{18}
\]

**External mathematical theorem, NOT newly proved:** Suzuki's paper states that \(-g_\zeta(L)\ge0\) for every L is equivalent to RH, and Corollary 1 states that **eventual** \(-g_0(L)\ge0\) is equivalent to RH. Therefore the following striking 1-parameter global criteria are available **conditional on accepting Suzuki's published proofs**:
- Full Weil quadratic nonnegativity only on the continuum of normalized interval indicators f_L, for ALL L>0, is RH-equivalent (by screw-function theorem).
- Even the non-archimedean primitive positivity \(H(L)\ge0\) for ALL SUFFICIENTLY LARGE L is RH-equivalent (Suzuki, Corollary 1).

This is NOT a new proof. It tells our induction program that a much simpler scalar **all-prime potential** can suffice: we need not construct a general positive Schur matrix at each width if we can prove the eventual sign of H. The scalar RH equivalence and H sign are already literature-established targets.

## 4. An exact discrete induction rule for every integer threshold, no zeros

Define for integer n≥1,
\[
\begin{aligned}
v_n&=\Lambda(n)/\sqrt n,\qquad V_n=\sum_{k\le n}v_k,\qquad
J_n=\sum_{k\le n}v_k\log k,\\
H_n&=H(\log n)=4(\sqrt n+n^{-1/2}-2)-V_n\log n+J_n,\\
D_n&=H'(\log n^+)=2(\sqrt n-n^{-1/2})-V_n .
\end{aligned}\tag{19}
\]
All quantities are explicit finite arithmetic sums. Starting from \(V_1=J_1=H_1=D_1=0\), the complete transition \(n\to n+1\) is
\[
\boxed{
\begin{aligned}
V_{n+1}&=V_n+v_{n+1},\\
J_{n+1}&=J_n+v_{n+1}\log(n+1),\\
H_{n+1}&=H_n+
4[\sqrt{n+1}+(n+1)^{-1/2}-\sqrt n-n^{-1/2}]\\
&\qquad\qquad -V_n\log(1+1/n),\\
D_{n+1}&=D_n+
2[\sqrt{n+1}-(n+1)^{-1/2}-\sqrt n+n^{-1/2}]
-v_{n+1}.
\end{aligned}}\tag{20}
\]
The new prime power contributes \(-v_{n+1}\) to the **slope**, but its direct contribution to \(H\) is ZERO at birth. This is the exact all-rung running coupling as a two-state **discrete dynamical system**, with no estimated future terms and no RH premise.

Between thresholds \(\log n\le L\le\log(n+1)\), V is constant, and
\[
H_n(L)=8(\cosh(L/2)-1)-L V_n+J_n,\quad
H_n''(L)=2\cosh(L/2)>0.\tag{21}
\]
The minimum on this rung is at the CLAMPED unique stationary point
\[
\boxed{
L_n^*=\min\!\Big(\log(n+1),\max\big(\log n,2\operatorname{arsinh}(V_n/4)\big)\Big).
}\tag{22}
\]
Therefore
\[
\boxed{\quad
H(L)\ge0\ \forall L\ge\log N
\iff H_n(L_n^*)\ge0\ \forall n\ge N.
\quad}\tag{23}
\]
Combining (23) with Suzuki Corollary 1 gives a **countable necessary-and-sufficient RH criterion** purely in terms of the finite arithmetic recurrence (20) and an explicit one-dimensional convex minimization (22). This is a derived recasting of an EXISTING RH-equivalent sign criterion; it is not an RH proof.

A simpler sufficient per-rung test is obtained from the strong-convexity lower bound \(H_n''\ge m_n:=\sqrt n+n^{-1/2}\):
\[
H(L)\ge H_n-\frac{(\min(D_n,0))^2}{2m_n}
\qquad(\log n\le L\le\log(n+1)).\tag{24}
\]
Thus \(H_n\ge(\min(D_n,0))^2/(2m_n)\) for all n≥N guarantees eventual H positivity and hence RH. This is strictly a **sufficient** stronger invariant and is not proved for all integers.

### A mathematically important NO-GO

As cited above, D changes sign infinitely often in the long run (the weighted prime discrepancy oscillates), even though numerical sampling below x=10 million showed D>0. Hence the tempting global induction hypothesis \(D_n\ge0\) is FALSE: the system must track the *reserve* H_n that can absorb temporary negative slope. A sign-preserving **two-dimensional** Lyapunov invariant for (H_n,D_n), rather than monotonicity of H, is the right remaining problem.

## 5. Independent numerical checks and audit status

I implemented and ran:
- \`experiments/abel_prime_common_map/verify_allprime_graph_dirichlet.py\`: for real sine test functions, widths L=.72,1.2,2.0,3.5, independently calculate full original W, interior gamma pair energy, exterior gamma boundary energy, prime jump-square sum, and prime degree potential. Differences were <1e−12 in tested double precision quadrature, with all signs preserved.
- \`experiments/abel_prime_common_map/verify_suzuki_screw_bridge.py\`: compare the exact GPP Weil box expression to \(-2[g_0(L)+g_\infty(L)]/L\) with mpmath Hurwitz–Lerch and digamma factors; PASS at L=.72,1,2,3.5,6,10,12 (difference <1e−9).
- \`experiments/abel_prime_common_map/check_suzuki_discrete_rungs.py\`: sieve first N=10^7 integers, check V_n, H_n, D_n and minima in finite intervals; numerical only, no general sign conclusion.

**What is proved on paper:** exact algebra (2)–(24) from source coefficients, standard Stieltjes integration by parts and the elementary piecewise-convex minimizer, assuming correct published Suzuki definitions. **Pending:** independent Turbo audit, any Lean formalization or directed-interval certification.

**Not proved:** eventual H positivity, all-width scalar Weil positivity, general Weil positivity/OB6/ARP, nor RH. **Do not mistake Suzuki's already-established *equivalence* for an independent proof of either side.**

## 6. Next real attempt

The most promising search is no longer assigning each local prime a separate slice of gamma energy (which double-spends the same resource). Instead work with the exact 2-state recurrence (20) and seek an inequality coupling \((H_n,D_n)\) that propagates through every negative slope jump. Any candidate must (i) be verified for arbitrarily large n by a symbolic argument, not finite sieve; (ii) exploit the actual von Mangoldt/Euler-product structure; (iii) fail for the shifted \(F_\theta\) control with off-line zeros; and (iv) not assume a zero-distribution estimate equivalent to RH.

The operator identity (6) is a separate complementary route for non-flat test functions and may support a genuinely different constructive positive-energy proof if the scalar recurrence cannot be closed.


## 7. Rigorous counterexample: local prime-entry asymptotic freedom does NOT imply global reserve positivity

This counterexample directly tests the hypothesis that every newly entering arithmetic term having relative coupling \(g_n<1\) suffices to preserve global positivity.

Replace the actual sparse von Mangoldt weights by the artificial sequence
\[
\widetilde v_n=\frac{\log n}{\sqrt n}\qquad\text{for EVERY integer }n\ge2.
\]
For each n entering its first support rung, the exact same gamma exterior-energy estimate gives
\[
\widetilde g_n(d)=\frac{2\log n}{\sqrt n K(d)}
<\frac{2}{\sqrt n};
\]
it is \(<1\) for n≥4 and also for n=2,3 by the explicit first-rung estimates in \`prime_threshold_running_coupling_2026_11_16.md\`. At each threshold, \(\widetilde g_n(d)\to0\). The local beta function is again negative quadratic.

Nevertheless its global smoothed reserve
\[
\widetilde H(L)
=4(e^{L/2}+e^{-L/2}-2)
-\sum_{2\le n\le e^L}\frac{\log n}{\sqrt n}(L-\log n)
\]
is **strictly negative at \(L=\log200\)**. Here is an elementary rational certificate that avoids numerical transcendental evaluation.

Use \(\log2>69/100\). For integers \(2\le k\le50\), define
\(j_k=\lfloor\log_2k\rfloor\),
\(h_k=\lfloor\log_2\lfloor200/k\rfloor\rfloor\),
and \(m_k=\lceil\sqrt k\rceil\). Then
\[
\frac{\log k}{\sqrt k}\log\frac{200}{k}
\ge\left(\frac{69}{100}\right)^2
\frac{j_kh_k}{m_k}.
\]
The EXACT rational sum satisfies
\[
\boxed{
\sum_{k=2}^{50}\left(\frac{69}{100}\right)^2
 \frac{j_kh_k}{m_k}
>4\left(\frac{283}{20}+\frac1{14}-2\right).
}\tag{25}
\]
Since \(14<\sqrt{200}<283/20\), we have
\[
4(\sqrt{200}+200^{-1/2}-2)
<4(283/20+1/14-2).
\]
All remaining k>50 contribute NONNEGATIVELY to the sum. Hence
\[
\boxed{\qquad\widetilde H(\log200)<0,\qquad
\text{although every first-rung coupling }\widetilde g_n<1.\qquad}\tag{26}
\]
The exact \`fractions.Fraction\` receipt is
\`experiments/abel_prime_common_map/verify_weak_coupling_no_go.py\`, and was independently EXECUTED; the rational margin is approximately 1.0277. The elementary input \(\log2>69/100\) is a standard strict log inequality and should be provided as a separate Lean lemma; no zeta or zero assumptions enter.

**Consequence:** any purported infinite-rung proof based ONLY on individual \(g_n<1\), negative local beta functions, or the Dirichlet/SOS channel estimate of each entrant is mathematically invalid. The missing ingredient has to use a true feature of the actual \(\Lambda(n)\), e.g. Euler-product multiplicativity, genuine prime-power sparsity with a sufficiently sharp correlated counting estimate, or a number-theoretic reflection mechanism. The finite arithmetic \((H_n,D_n)\) recurrence is an exact proof TARGET, not a closed induction.

This falsifier is not the shifted \(F_\theta\) control; it isolates and rejects the *Euler-product-blind local coupling mechanism*. The genuine \(F_\theta\) control from Suzuki's generalized screw-function theorem remains a separate essential check for any claimed RH-strength global invariant.
