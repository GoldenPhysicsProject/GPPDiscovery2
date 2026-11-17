# Optimal uniform Chebyshev superadditivity gap at weight 1/sqrt(n): exact all-real theorem

**2026-11-16, Discovery2.** Builds on the unconditional published psi estimates and on our independently re-executed global Chebyshev superadditivity certificate. The finite work here is a reproducible **64,516-case exact integer certificate**; the infinite region is handled by a rational analytic inequality. No RH assumption and no claim of worldwide priority. Not yet Lean checked.

## 1. Sharp theorem and the exact best constant

For real x>=1 set \(V(x)=\sum_{2\le n\le x}\Lambda(n)/\sqrt n\). Then

\[
 \boxed{
 \forall x,y\ge2,\qquad
 V(xy)-V(x)-V(y)\ge c_*,
 }\tag{1}
\]
where
\[
 \boxed{c_*=V(4)-2V(2)
  =\frac{\log3}{\sqrt3}+\frac{\log2}{2}-\frac{\log2}{\sqrt2}
  =0.490728619\ldots.}\tag{2}
\]
**Optimality:** equality occurs at x=y=2 (and on portions of the adjacent step-function plateau), so no larger constant holds universally.

The weaker global theorem for x,y>=1 is V(xy)>=V(x)+V(y). The sharp positive gap (1) requires BOTH x,y>=2; the gap must tend to zero when a factor tends to 1.

## 2. Analytic proof for ALL pairs with max{x,y}>=256

Use the two established UNCONDITIONAL inputs:
- Manuel Eberl's Isabelle AFP Chebyshev bound psi(z)>=(9/10)z, all real z>=41 (2024/2025), https://isa-afp.org/entries/Chebyshev_Prime_Bounds.html
- Rosser–Schoenfeld / Johnston–Ramaré–Trudgian (2023), psi(z)<=(26/25)z, all real z>=0, Lemma 5 https://link.springer.com/article/10.1007/s40993-023-00476-4

Partial summation gives
\[
 V(z)\le\tfrac{52}{25}\sqrt z-\tfrac{26}{25}\;(z\ge1),\quad
 V(z)\ge\tfrac95\sqrt z-\tfrac9{10}\sqrt{41}\;(z\ge41).
\]
For x>=2,y>=256 (exchange x,y if needed), the surplus is bounded below by
\[
 F(\sqrt x,\sqrt y)
 =\tfrac95\sqrt{xy}-\tfrac9{10}\sqrt{41}
  -\tfrac{52}{25}(\sqrt x+\sqrt y)+\tfrac{52}{25}.
\]
Both partial derivatives in X=sqrt x,Y=sqrt y are positive on X>=sqrt2,Y>=16. Therefore F is minimized at (x,y)=(2,256). Exact rational root enclosures
\(\sqrt{512}>22627/1000,\sqrt{41}<6404/1000,\sqrt2<1415/1000\),
all checked by squaring integers, give
\[
 \boxed{F(\sqrt2,16)>\frac{4109}{5000}=0.8218>\frac12>c_*.}\tag{3}
\]
Thus the infinite half-plane is settled.

## 3. Exact finite minimization, 64,516 pairs, no floating acceptance tests

If 2<=x,y<256, let n=floor x,m=floor y. Then 2<=n,m<=255; monotonicity gives V(xy)>=V(nm), while V(x)=V(n) and V(y)=V(m). Hence it suffices to prove the 254²=64,516 integer inequalities.

The script experiments/abel_prime_common_map/certify_sharp_weighted_chebyshev_gap.py reuses the **exact outward dyadic 16-term atanh log enclosures** and integer-square-root enclosures of our prior checker at scale B=10^12. It sieves every prime power through 255²=65,025, accumulates rational lower/upper estimates V_lo and V_hi and proves for every (n,m) except (2,2) that
\[
 V_\mathrm{lo}(nm)-V_\mathrm{hi}(n)-V_\mathrm{hi}(m)
 > V_\mathrm{hi}(4)-2V_\mathrm{lo}(2)
 \ge V(4)-2V(2).
\]
At (2,2), identity gives equality. The exact program output:

    ANALYTIC region max{x,y}>=256: gap > 4109/5000
    CERTIFIED 64516 pairs 2<=n,m<=255; all except (2,2) strictly above c_*
    490728619104/10^12 < c_* < 490728619190/10^12
    Next-smallest outward gap 576207034035/10^12 at (2,3)
    6587 prime-power events through 65025
    ALL real x,y>=2: gap >= c_* optimal

Every decision uses integer arithmetic; NO zeta zeros or numerical RH assumption. The external psi bounds and the enclosure lemmas are analytic inputs; the checker is not a Lean proof.

## 4. Exact off-line falsifier preservation and new spatial gap

By the monotone-reweighting theorem in research/monotone_reweighting_f_theta_falsifier_central_deficit_2026_11_16.md, for any nonnegative nondecreasing g,
\[
 V_g(xy)-V_g(x)-V_g(y)
 \ge g(\min\{x,y\})[V(xy)-V(x)-V(y)]
 \ge g(2)c_*\qquad (x,y\ge2).
\]
In particular g(n)=cosh(theta log n) (ALL theta>=0), so the **sharp positive reserve gap also persists in every shifted off-critical F_theta-style prime-weight control**. This further demonstrates that prime mass superadditivity, even with an optimal strict gap, does not imply RH.

For the true Weil graph on I_L=[-L/2,L/2], define visible mass m_L(x)=Σ_{log n<L}v_n(1_{log n≤L/2+x}+1_{log n≤L/2-x}) and q_L=V(e^{L^-})-m_L>=0 a.e. At positions with BOTH distances d_-=L/2+x and d_+=L/2-x strictly greater than log 2, apply (1) after perturbing both downward to avoid jump boundaries:
\[
 \boxed{
 q_L(x)\ge c_*
 \quad\text{for a.e. }x\text{ satisfying }d_->\log2,\ d_+>\log2.
 }\tag{4}
\]
For L>=8log4, the stronger separately established bulk estimate q_L(x)>=.7e^{L/2} applies to |x|<=L/4.

This supplies an unconditional *positive spatial surplus potential* but does not close the odd pole or low-frequency arithmetic Schur block. No full Weil positivity is asserted.

## 5. Next mathematical work

The new gap and the source-corrected Legendre Schur identity \(S_{\rm safe}=F-\delta^{-1}(H-F^2)\) are natural candidates for Lean/Mathlib formalization. Yet an RH-valid proof still needs a global estimate not shared by the shifted control, likely in the completed gamma/pole versus prime-frequency correlation or the exact high-sector Schur inverse.

**Credit:** Eberl / Rosser–Schoenfeld unconditional psi bounds; elementary exact rational interval arithmetic. No claim of novelty over unseen literature or an RH proof.
