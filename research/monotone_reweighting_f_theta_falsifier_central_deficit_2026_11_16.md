# The sharp prime-mass theorem is closed under monotone reweighting: exact F_theta falsifier, plus a quantitative central deficit

**2026-11-16; independent follow-up to the global weighted Chebyshev proof.** This is an unconditional elementary theorem that sharply limits how far our superadditivity result can be pushed toward RH. No new zero-location result. Input: the verified unconditional base inequality V(xy)>=V(x)+V(y) for V(x)=sum_{n<=x}Lambda(n)/sqrt(n), established in research/weighted_chebyshev_global_superadditivity_sharp_prime_mass_2026_11_16.md using published psi estimates and an exact finite certificate.

## 1. Generic monotone-reweighting closure theorem (no number theory beyond the base inequality)

Let a_n>=0 (n>=2), A(x)=sum_{2<=n<=x} a_n, and assume
\[
 A(xy)\ge A(x)+A(y)\quad\text{for all real }x,y\ge1.
\]
For ANY nonnegative nondecreasing weight g:[1,infty)->[0,infty), define
\(A_g(x)=\sum_{2<=n<=x}a_n g(n)\). Then

\[
\boxed{A_g(xy)\ge A_g(x)+A_g(y)\quad\text{for ALL }x,y\ge1.}\tag{1}
\]

**Proof, exact and short.** Assume 2<=x<=y; if min{x,y}<2, the claim is immediate by monotonicity. The difference is
\[
 A_g(xy)-A_g(x)-A_g(y)
 =\sum_{y<n\le xy}a_ng(n)-\sum_{n\le x}a_ng(n).
\]
Every n in the first sum is greater than y>=x, so g(n)>=g(x). Every n in the second sum is <=x, so g(n)<=g(x). Consequently
\[
\boxed{A_g(xy)-A_g(x)-A_g(y)
 \ge g(x)\big[A(xy)-A(x)-A(y)\big]\ge0.}\tag{2}
\]
The same works with x,y interchanged. This is not merely finite-range numerics, but a GLOBAL preservation theorem for the full cone of nondecreasing weights. If g(x)>0 and the base surplus is strictly positive, then so is the reweighted surplus.

## 2. Exact off-critical shifted-weight negative control, ALL theta>=0

For theta>=0, take \(g_\theta(n)=\cosh(\theta\log n)\). This function is positive and nondecreasing on n>=1, with g_theta(1)=1. Define
\[
 V_\theta(x)=\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}\cosh(\theta\log n).
\]
By (1),
\[
 \boxed{V_\theta(xy)\ge V_\theta(x)+V_\theta(y)\quad
 \forall x,y\ge1,\ \forall\theta\ge0.}\tag{3}
\]
This is the *same* normalized off-line \(F_\theta\)-style weight deformation used in Discovery2. Its completed shifted-zeta model has zeros displaced from the critical line, subject to the model's separate gamma/pole conventions. Hence **even the exact ALL-WIDTH sharp prime graph mass and multiplicative superadditivity survive the shifted off-line falsifier**. There is no way to infer RH merely from these inequalities.

In fact any power weight g(n)=n^b, b>=0, gives
\[
 \boxed{V_\alpha(xy)\ge V_\alpha(x)+V_\alpha(y)
 \quad\text{for every }\alpha\le1/2,}\tag{4}
\]
where \(V_\alpha(x)=\sum_{n\le x}\Lambda(n)n^{-\alpha}\). For alpha>1, the inequality must fail for sufficiently large x,y because V_alpha(x) tends to the strictly positive finite number h(alpha)=-zeta'(alpha)/zeta(alpha). The range 1/2<alpha<=1 is not resolved by THIS monotone-reweighting argument; finite scans are not a proof.

For any nonnegative nondecreasing g, the same graph mass argument applies to \(v_n^{(g)}=a_n g(n)\) and gives
\[
 \mathrm{ess\,sup}_{x\in I_L}
 \left[A_g(e^{x+L/2})+A_g(e^{L/2-x})\right]
 =\sum_{\log n<L}a_n g(n),
\]
with the strict-cutoff convention at L=log n. Thus the sharp mass result is **structurally stable under off-line deformations**, a clean and necessary no-go.

## 3. A NEW stronger fact for the ACTUAL weight: exponential central depletion

Although the global scalar mass bound is the same across shifted models, the actual unconditional Chebyshev inputs yield a quantitative, spatially localized improvement.

Write \(v(t)=\sum_{\log n\le t}\Lambda(n)/\sqrt n\), and \(v(L^-)=\sum_{\log n<L}\Lambda(n)/\sqrt n\). For a support width L>0 let
\[
 m_L(x)=v(L/2+x)+v(L/2-x)
\]
for interior x outside finitely many jumps, and define the *positive surplus potential*
\[
 q_L(x)=v(L^-)-m_L(x)\ge0\qquad\text{almost everywhere on }I_L.
\]
The inequality q>=0 is exactly the proven superadditivity and strict-cutoff limit.

From the unconditional Chebyshev bounds and partial summation (source note):
\[
 v(t)\le\tfrac{52}{25}e^{t/2}-\tfrac{26}{25}\quad(t\ge0),\qquad
 v(L^-)\ge\tfrac95e^{L/2}-\tfrac9{10}\sqrt{41}\quad(L\ge\log41).
\]
Therefore for the whole interval,
\[
\boxed{
q_L(x)\ge\tfrac95 e^{L/2}
-\tfrac{104}{25}e^{L/4}\cosh(x/2)
+\tfrac{52}{25}-\tfrac9{10}\sqrt{41}
}\tag{5}
\]
at every non-jump interior point (a.e.). This bound is quantitatively useful in the center even though it can be negative near the endpoints.

**Theorem (explicit bulk depletion).** For every \(L\ge8\log4\) and \(|x|\le L/4\), a.e.,
\[
 \boxed{v(L^-)-m_L(x)\ge\tfrac7{10}e^{L/2}.}\tag{6}
\]
**Proof.** Set z=e^{L/8}>=4. On |x|<=L/4,
\(e^{L/4}\cosh(x/2)\le e^{3L/8}=z^3\).
Also sqrt41<13/2, so \(52/25-(9/10)\sqrt{41}>-4\). Thus (5) is at least
\[
 (9/5)z^4-(104/25)z^3-4
 \ge [\,9/5-104/(25\cdot4)-4/4^4\,]z^4
 = (1191/1600)z^4>(7/10)z^4.
\]
All constants are rational apart from the threshold L>=8log4, and all comparisons are elementary. NO RH, zero computations or finite scans.

This yields a useful exact positive-minus-negative *potential* decomposition for the genuine Weil form:
\[
 W_L(f)=
 E_\infty(f)+E_{\mathrm{prime}}(f)
 +2|\langle f,\cosh(x/2)\rangle|^2
 +\int_I q_L(x)|f(x)|^2dx
 -[|C_\infty|+v(L^-)]\|f\|^2
 -2|\langle f,\sinh(x/2)\rangle|^2 .
\]
The positive q_L barrier has order \(e^{L/2}\) throughout the middle half of the spatial interval for L>=8log4. It does not by itself outweigh the constant negative budget or prove full Weil positivity. It suggests a precise BULK/EDGE localization route with IMS/Schur error estimates, avoiding blanket payment of a smallest eigenvalue.

## 4. Honest consequence for the RH programme

- The sharp all-width mass bound is unconditional, but (3) proves that it survives **all** positive shifted F_theta weights and thus has no direct RH discrimination.
- The improved central potential (6) is genuine new source-specific information, but analogous estimates may exist for shifted weights and its sign does not settle the full quadratic form.
- The remaining desired invariant must involve at least one of: the distribution of prime phases with the gamma-energy frequency window, the completed pole interactions, or a completed arithmetic operator structure that the shift control fails.
- Formalization: pure order-theoretic lemma (1)-(2) is straightforward Mathlib material; then specialize to vonMangoldt and log. Center bound (6) is a simple rational-exponential proof once published psi inputs and partial summation are available. Do not claim Lean compilation.
