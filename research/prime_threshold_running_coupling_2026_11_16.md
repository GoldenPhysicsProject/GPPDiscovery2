# A running coupling for every prime-power support threshold

**Date:** 2026-11-16. **Authoring seat:** GPT / GPPDiscovery2. **Status:** direct functional-analytic derivation for audit; not yet Lean formalized. **No RH claim.**

## Result at a glance

There is an exact renormalization-type law for the effect of a **newly entering** prime-power translation on the *actual* completed Weil form. It uses **the positive archimedean Dirichlet form** as the measuring metric, not the standard \(L^2\) norm. If \(n=p^k\) is a prime power, \(\ell_n=\log n\), and \(L=\ell_n+d\) lies in the first exposure rung \(\log n<L\le\log(n+1)\), then
\[
\boxed{
\bigg|2\frac{\Lambda(n)}{\sqrt n}\operatorname{Re} A_f(\ell_n)\bigg|
\le g_n(d)\,\mathcal E(f),\qquad
g_n(d)=\frac{2\Lambda(n)}{\sqrt n\,K(d)},
}
\]
where \(A_f(t)=\langle f,T_tf\rangle_{L^2(\mathbb R)}\) and
\[
K(d)=2\int_d^\infty\frac{e^{-t/2}}{1-e^{-2t}}\,dt
=\log\frac{1+e^{-d/2}}{1-e^{-d/2}}
+2\arctan(e^{-d/2}).
\]
The coupling \(g_n(d)\) is dimensionless, positive, strictly increasing in \(d>0\), and tends to 0 at the threshold \(d\downarrow0\).

This produces an **exact local differential beta function** with ultraviolet variable \(\mu=1/d\),
\[
\boxed{
\frac{d g_n}{d\log\mu}
=-\frac{d\,w(d)}{v_n}\,g_n^2,\qquad
w(d)=\frac{e^{-d/2}}{1-e^{-2d}},\quad
v_n=\frac{\Lambda(n)}{\sqrt n}>0.
}
\]
Since \(d\,w(d)\to\frac12\),
\[
\boxed{
\frac{d g_n}{d\log\mu}\sim-\frac{g_n^2}{2v_n}
\quad (\mu\to\infty).
}
\]
This is a mathematically exact analogue of a negative one-loop beta function for a **relative form bound**. It is not the beta function of a quantum field theory, and it is not a proof of positivity at all widths.

## 1. The entire argument is an exact real-place boundary decomposition

Fix any \(L>0\) and set \(I_L=[-L/2,L/2]\). Extend \(f\in L^2(I_L)\) by zero. For the positive archimedean energy (possibly \(+\infty\) for rough f)
\[
\mathcal E(f)=\int_0^\infty w(t)\,\|f-T_tf\|_2^2\,dt,
\qquad w(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\]
write the energy as the exact nonnegative double integral
\[
\mathcal E(f)=\int_{x>y}w(x-y)|f(x)-f(y)|^2\,dx\,dy.
\]
Retain only pairs with exactly one point outside the interval, where f is zero. There are two disjoint exterior contributions, yielding
\[
\boxed{
\mathcal E(f)\ge
\frac12\int_{I_L}
\left[K(x+L/2)+K(L/2-x)\right]|f(x)|^2\,dx.
}\tag{1}
\]
This **boundary barrier** is a pointwise positive multiplication form in the actual real-place energy, not an invented counterterm. It applies to arbitrary complex f in the energy domain and contains NO prime or zeta input.

The barrier grows logarithmically at the two endpoints. It is consistent with the exact endpoint subtraction formula for the archimedean operator in
\`first_prime_operator_endpoint_residual_2026_11_16.md\`.

## 2. The new prime term lives on two disjoint tiny caps

Let \(\ell>0\), \(\ell<L\le2\ell\), and \(d=L-\ell\in(0,\ell]\). Define
\[
I_-=[-L/2,L/2-\ell],\qquad
I_+=[\ell-L/2,L/2].
\]
The two intervals have equal length d and are disjoint up to endpoints. The shift \(T_\ell f(x)=f(x-\ell)\) maps \(L^2(I_-)\) unitarily to \(L^2(I_+)\) and vanishes on the complement under compression. Thus
\[
|A_f(\ell)|=
\left|\int_{I_+}\overline{f(x)}f(x-\ell)\,dx\right|
\le\frac12\left(\|f\|_{L^2(I_-)}^2+\|f\|_{L^2(I_+)}^2\right).
\tag{2}
\]
But \(x+L/2\le d\) on \(I_-\), and \(L/2-x\le d\) on \(I_+\). Since K is decreasing, the **full** positive energy (1) satisfies
\[
\boxed{
\mathcal E(f)\ge
\frac{K(d)}2
\left(\|f\|_{L^2(I_-)}^2+\|f\|_{L^2(I_+)}^2\right).
}\tag{3}
\]
Combining (2) and (3) gives the central inequality:
\[
\boxed{|A_f(\ell)|\le\mathcal E(f)/K(d).}\tag{4}
\]
Notice the subtle distinction: the compressed shift has operator norm **one** on ordinary L² as soon as d>0 (and the selfadjoint Pauli prime exchange has norm \(v_n\)). Nevertheless its QUADRATIC FORM has vanishing relative bound \(g_n(d)\to0\) in the positive archimedean metric. This is the exact mechanism behind “threshold asymptotic freedom”.

For the actual Weil form, the prime-power \(n\) contribution is
\(-2v_n\operatorname{Re}A_f(\ell_n)\) with \(v_n=\Lambda(n)n^{-1/2}\). Inequality (4) gives
\[
-2v_n\operatorname{Re}A_f(\ell_n)\ge-g_n(d)\mathcal E(f),\qquad
g_n(d)=2v_n/K(d).
\tag{5}
\]

**No repeated energy budget is permitted.** Estimate (5) works for EACH new prime contribution independently. If several prime terms are simultaneously present, simply adding their separate bounds may spend the same exterior energy many times and produces a weak or divergent estimate. This is exactly why the result does not prove RH.

## 3. Running-coupling law and asymptotic freedom

Differentiate the **closed form** of K, or differentiate under the defining integral:
\[
K'(d)=-2w(d)<0.
\]
Therefore, with \(g_n(d)=2v_n/K(d)\),
\[
\boxed{\quad
g_n'(d)=\frac{4v_n\,w(d)}{K(d)^2}
       =\frac{w(d)}{v_n}g_n(d)^2>0.
\quad}\tag{6}
\]
For the ultraviolet scale \(\mu=1/d\),
\[
\boxed{
\beta_n(g_n,d)
=\frac{d g_n}{d\log\mu}
=-\frac{d\,w(d)}{v_n}\,g_n^2.
}\tag{7}
\]
As \(d\downarrow0\),
\[
w(d)=\frac1{2d}+O(1),\qquad
K(d)=\log(4/d)+\pi/2+O(d),
\]
so \(g_n(d)\sim 2v_n/\log(1/d)\) and
\[
\boxed{
\beta_n\sim-\frac{g_n^2}{2v_n}.
}\tag{8}
\]
This negative quadratic beta function is not postulated; it follows directly from Weil's **real-place gamma kernel** and the prime-translation support geometry. It is one legitimate rigorous realization of Daniel's intuition about Haar measure, running coupling, and arithmetic “asymptotic freedom.”

No identification with \(\Lambda_{\rm QCD}\), a quantum gauge coupling, the physical renormalization group, or a Yang–Mills gap is asserted.

## 4. A single rule for every \(n\), extending to infinity

For \(n\ge2\) and **only** if \(n\) is a prime power (\(\Lambda(n)>0\)), its initial support rung is
\[
 \log n<L\le\log(n+1),\qquad
 d=L-\log n\le\log(1+1/n)\le 1/n.
\]
Since \(d\le1/n\), we automatically have \(L\le2\log n\) for n≥2, so the two-cap condition of §2 applies at **every** new integer threshold (including prime powers).

Let \(z=e^{-d/2}\). Using \(1-z\le d/2\) and \(1+z\ge1\), we obtain \(K(d)\ge\log(2/d)\ge\log(2n)\). Therefore
\[
\boxed{
0<g_n(d)
\le\frac{2\Lambda(n)}{\sqrt n\,\log(2n)}
\le\frac{2\log n}{\sqrt n\,\log(2n)}
<\frac2{\sqrt n}
}\tag{9}
\]
for every prime power entering its first rung. No prime number theorem, zeta zeros, or zero-density estimate is needed.

**For all n≥4**, the right side is at most one, with strict inequality in (9). For n=2 it improves directly to \(g_2\le1/\sqrt2\), since \(\log(4)=2\log2\); for n=3,
\(\log6>\tfrac32\log3\) (because \(6>3^{3/2}\)), implying \(g_3<4/(3\sqrt3)<1\).
Thus the new term on EVERY rung satisfies the uniform conservative condition
\[
\boxed{\quad g_n(d)<1\quad\text{for all prime powers }n\ge2
\text{ in their first exposure rung.}\quad}\tag{10}
\]
More importantly, the new-term relative bound tends to zero as n grows:
\(g_n=O(n^{-1/2})\) at rung endpoints, without PNT. For a prime n=p,
\(g_p(d_{\max})\sim2/\sqrt p\) since \(K(\log(1+1/p))\sim\log(4p)+\pi/2\).
Consequently the individual entrant terms are asymptotically weak across **infinitely many** prime thresholds.

**Essential non-conclusion:** the **sum of all** these absolute couplings does not provide a finite all-prime energy budget. In fact \(\sum_{p}p^{-1/2}\) diverges (it dominates the divergent \(\sum_p 1/p\)). Any all-rung argument must exploit signed correlations, the exact local prime mass defect, or an arithmetic conserved flow. Independent termwise perturbative summation is insufficient.

## 5. A conditional, noncircular one-step propagation lemma

For the SAME support width L, define \(W_{\rm before,L}\) by removing just the newly entering n-th prime-power term from the actual finite-support Weil form, and \(W_{\rm after,L}\) by restoring it. The difference is exactly \(-2v_n\operatorname{Re}A_f(\ell_n)\).

If one has independently established a true coercive margin
\[
W_{\rm before,L}(f)\ge\varepsilon_L\,\mathcal E(f)
\quad\text{for ALL admissible f of support width L},
\]
then (5) gives
\[
\boxed{
W_{\rm after,L}(f)
\ge(\varepsilon_L-g_n(d))\mathcal E(f).
}\tag{11}
\]
Hence positivity survives the insertion if \(g_n(d)\le\varepsilon_L\). As \(d\downarrow0\), \(g_n(d)\to0\), so ANY fixed positive pre-entry margin admits some interval of post-entry stability.

**The missing bridge:** knowing positivity at a *smaller width* L₀ does NOT give the premise for \(W_{\rm before,L}\) at a larger width L by restriction alone: new functions live on a strictly larger support interval, even when they do not couple to the new prime. We need a **width-transport theorem** and ultimately a **uniform no-zero-crossing / Lyapunov inequality** for the renormalized family. The prime beta function alone is not sufficient for RH.

## 6. A separate width-transport mechanism for the positive kinetic channel

There is an additional exact and useful observation. Identify all spatial intervals with the fixed reference \(I_1=[-1/2,1/2]\) by the unitary scaling
\(f_L(x)=L^{-1/2}g(x/L)\). Write the archimedean energy in the reference Fourier coordinate \(\eta\):
\[
\boxed{
 E_L(g)=\int_\mathbb R a(\eta/L)|\widehat g(\eta)|^2\,d\eta.
}\tag{12}
\]
The positive multiplier obeys the derivative formula
\[
r a'(r)=4\sum_{k\ge0}
\frac{r^2(2k+1/2)}
{[(2k+1/2)^2+r^2]^2}>0.
\tag{13}
\]
An elementary split at \(2k+1/2=r\), separating \(0<r\le1\) and \(r\ge1\), establishes the deliberately loose universal bound
\[
\boxed{\quad 0\le r a'(r)\le12\qquad(r>0).\quad}\tag{14}
\]
For \(r\le1\), the k=0 summand is ≤2 and the remaining k≥1 tail is ≤4∑_{k≥1}(2k)^{-3}<3/4. For \(r\ge1\), group λ_k≤r and λ_k>r: the first part is ≤2+4/r, the tail ≤1+4/r, totaling ≤3+8/r≤11. Hence 12 is valid for both cases.

By the ordinary fundamental theorem of calculus in log r, (12)–(14) give a **uniform** kinetic width-transport estimate:
\[
\boxed{
|E_L(g)-E_{L'}(g)|
\le12\,|\log(L/L')|\,\|g\|_2^2
\qquad(L,L'>0),
}\tag{15}
\]
on their common smooth/form domain. Unlike a naive norm estimate, the bound is independent of g's oscillation frequency: the leading logarithmic kinetic divergence cancels.

All the other finite-width Weil terms are bounded L² operators. Their translated representations under unitary scaling are strongly continuous in L, but NOT norm-continuous on L² at prime thresholds: the cap-shift operator norm jumps from 0 to 1. However, the embedding of the **archimedean energy completion into L²(I₁) is compact** (proved by Fourier high-frequency tail in the companion compactness note); composing a strongly continuous, uniformly bounded family of operators with this compact embedding makes the induced perturbation **norm-continuous in the stronger energy metric**, even across a prime threshold.

As a consequence (subject to the standard compact-embedding and common-domain functional-analytic lemmas), the **renormalized Weil form family** can be represented by a norm-continuous family of bounded selfadjoint operators \(Q_L\) on a single reference energy Hilbert space, of the form
\[
Q_L=I+\text{compact selfadjoint perturbation}+\text{bounded small kinetic variation}.
\tag{16}
\]
Thus a **strict** positive coercivity margin at L₀ persists over some open interval of widths around L₀, even if a new prime power enters. This is a principled width-transport statement. It is not a uniform all-width gap.

The only way to change the **negative index** as width L increases is for the renormalized operator to acquire a genuine zero eigenvalue. That turns the all-width RH-strength problem into an explicitly localized **no-zero-crossing problem for the arithmetic operator flow**. The negative index is nondecreasing under the original nested support embeddings, so any lost positivity cannot later be restored merely by enlarging the support domain.

## 7. What must be proved next to get an all-the-way-to-infinity theorem

The correct induction must simultaneously control **three** pieces:

1. **Width transport:** quantify how the strictly positive base spectral gap changes under L→L+δ, using (15) and norm continuity of the actual compressed old-prime shifts in the energy metric. Need an explicit modulus, not just continuity.
2. **New prime:** use the exact local coupling \(g_n(d)\) and its negative beta function (7). It is tiny at birth and O(n^{-1/2}) by the end of its first rung.
3. **Accumulated arithmetic flow:** prove a cancellation or conservation identity preventing the smallest eigenvalue from crossing zero over infinitely many rungs. This is the **genuine RH-level missing piece**. Source candidates: the exact shift-resolvent mass defect (GPPVerify \`ShiftPresentation\`), a certified coupled Schur invariant, or a positivity-preserving arithmetic transfer operator. Do NOT replace this with \(\sum g_n\), which gives no closure.

The attractive hypothesis is that the pole, gamma, and prime channels define a **correlated transport invariant** with a nonnegative beta function for a renormalized Schur margin; this is a research conjecture, NOT established by the present result. A valid proof must demonstrate the invariant algebraically and pass an \(F_\theta\) negative control.

### Audit / formalization requests

- **Lean unit 1:** exact exterior boundary barrier inequality (1), valid for all finite-energy compactly supported functions. It is generic for positive decreasing translation kernels, not zeta-specific and may be upstreamable to mathlib.
- **Lean unit 2:** disjoint-cap correlation (2), local relative bound (4) and (5), and derivative \(\beta_n\) (6)–(8).
- **Lean unit 3:** universal threshold estimate (9), \(g_n<1\), and asymptotic decay without PNT.
- **Lean unit 4:** common-domain kinetic dilation (12), multiplier derivative estimate (13)–(15), width-family norm continuity in energy metric, and local persistence of strict positivity (conditional on a proved base gap).
- **Research continuation:** find and test a noncircular *arithmetic* no-crossing invariant, not merely a new RH-equivalent criterion.

\`experiments/abel_prime_common_map/check_prime_threshold_running_coupling.py\` records independent floating-point checks of K, its derivative, beta function and the universal rung upper bounds. Floats do not certify the analytic inequalities.

**Bottom line:** we have one exact general rule for *every* new prime-power threshold, with a negative quadratic running beta function and asymptotic weakness. The required all-width accumulation/cancellation remains unproved. 


## 8. Essential negative control: the same local beta law survives Fθ

The running coupling is a *local support/geometric bound*, not yet a \(\zeta\)-specific property. Test the off-line-zero deformation
\[
F_\theta(s)=\xi(s-\theta)\xi(s+\theta),\quad0<\theta<1/2,
\]
from the GPP/Turbo comparison experiments. Its prime-power weights are multiplied relative to the single-\(\zeta\) weights by \(2\cosh(\theta\log n)\) in the product's explicit formula (carefully account for doubled archimedean and pole channels when building the full deformed form). Accordingly the **same** boundary method yields, for the isolated deformed prime-side term,
\[
 g_{n,\theta}(d)
 =2\cosh(\theta\log n)\,g_n(d).
\]
At the end of a prime rung and with n=p prime,
\[
g_{p,\theta}\asymp p^{\theta-1/2}
\quad(p\to\infty)
\]
(up to the fixed scalar and log ratio). This also tends to ZERO when \(\theta<1/2\), even though \(F_\theta\) has shifted/off-critical zeros. **Thus local threshold asymptotic freedom cannot, by itself, prove RH.** The missing global invariant must use the precise one-channel Euler product, signed prime/gamma/pole interference or a spectral trace identity that rejects \(F_\theta\). This is an explicit falsification criterion for any claimed induction proof.

## 9. Separate Abel–Cesàro convergence-strip guardrail from the GPP source

I additionally reopened Daniel Toupin's original \`rh_cesaro_v2.tex\` and GPPVerify's live \`flint/workbench\` files \`CesaroAbelState.lean\` and \`CesaroWeilGram.lean\`. The Lean branch already explicitly identifies the relevant domain boundary: the positive Abel integral for a character exponent \(\alpha\) requires \(|\Re\alpha|<\varepsilon\), and a positive Gram of character exponents requires \(|\Re\alpha_i|<\varepsilon/2\). Outside that strip the rational expression is MEROMORPHIC CONTINUATION, not a positive integral; \`WeilIsGram\` and \`HPsi\` are correctly marked OPEN.

An important source-level issue in \`rh_cesaro_v2.tex\`, proof of Theorem \`W-pos-cesaro\`: it sets \(\varepsilon_0>2\max|\Re\rho-\tfrac12|\) and then incorrectly asserts integrability for **all** \(0<\varepsilon<\varepsilon_0\). The inequality is backwards. For a noncritical \(\rho\), \(\chi_\rho(t)=t^{\rho-1/2}\), and
\[
\frac{\varepsilon}{2}\int_{\mathbb R}e^{-\varepsilon|u|}
|\chi_\rho(e^u)|^2du
=\frac{\varepsilon^2}{\varepsilon^2-(2\Re\rho-1)^2}
\]
holds as a convergent positive integral **only** for
\(\varepsilon>|2\Re\rho-1|\). Thus one cannot take \(\varepsilon\downarrow0\) through positive integrals if \(\Re\rho\neq1/2\). The rational meromorphic formula at smaller epsilon cannot be used to infer positivity; indeed for real nonzero \(\delta=2\Re\rho-1\) and \(0<\varepsilon<|\delta|\), it gives a **negative** value although the actual integral diverges. The Lean \`CesaroAbelState\` guardrail is CORRECT. The formal \`WeilIsGram\` challenge remains precisely the need to construct a common ε-dependent admissible family realizing the true arithmetic form without presupposing criticality.

This is why the new **positive boundary-energy beta function** must not be conflated with a positive Abel limit of arbitrary off-line zeta characters. They are different regularization parameters, and neither bypasses the global Weil/trace identification gap.


## 10. Exact local sum-of-squares sewing at each prime entry

There is a stronger operator interpretation of the inequality \(g_n<1\). On the two caps of width \(d=L-\ell_n\), identify their wavefunctions \(a,b\in L^2([0,d])\) via the common translation coordinate. The actual prime contribution is \(-2v_n\operatorname{Re}\langle a,b\rangle\). The positive **exterior** real-place energy already contains at least
\[
\frac{K(d)}2(\|a\|^2+\|b\|^2).
\]
These two pieces obey the EXACT completed-square identity
\[
\boxed{
\begin{aligned}
\frac{K(d)}2(\|a\|^2+\|b\|^2)
 -2v_n\operatorname{Re}\langle a,b\rangle
={}&\left(\frac{K(d)}2-v_n\right)
       (\|a\|^2+\|b\|^2)\\
&+v_n\|a-b\|^2.
\end{aligned}}\tag{17}
\]
Because \(g_n=2v_n/K(d)<1\) on the new prime's first rung, the right-hand side is **strictly positive** for any nonzero cap wavefunction. This is a genuine explicit two-channel (Pauli/Haar) positive-square sewing of a new prime jump with its gamma boundary barrier, with no RH premise.

For the first prime n=2 and throughout \(\log2<L\le\log3\), the worst-case (latest) cap margin has
\[
\frac{K(\log(3/2))}2-\frac{\log2}{\sqrt2}
  \approx1.3408>0,
\]
and becomes even larger as L↓log2. Similarly each prime-power entry has a positive margin at the end of its initial rung.

**Crucial accounting rule:** the same positive archimedean boundary energy is present only ONCE in the full Weil quadratic. Formula (17) may be applied to ONE prime channel, or to multiple channels only with a proved disjoint/weighted allocation of that energy. Summing independent instances of (17) without such an allocation would count one positive resource repeatedly and is invalid. This highlights a concrete global research target: construct a positive partition or a correlated *operator-valued* allocation of gamma/Haar energy across all concurrently visible prime modes, respecting the exact shifted-resolvent mass defect. The all-prime allocation is unproved and must reject Fθ.
