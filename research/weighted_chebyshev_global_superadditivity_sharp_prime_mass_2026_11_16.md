# Weighted Chebyshev multiplicative superadditivity: a GLOBAL unconditional arithmetic theorem and a sharp Weil-graph bound

**Date:** 2026-11-16. **Status:** rigorous analytic reduction to unconditional published psi bounds, plus **40,401 exact-integer finite inequalities**, independently re-executable in under one second. No RH/ARP/OB-6 assumption. This exact weighted inequality was not located in our targeted literature search; no claim of worldwide novelty or priority is made without a comprehensive literature review.

## 1. The theorem

For every real x>=1 define
\[
 V(x):=\sum_{2\le n\le x}\frac{\Lambda(n)}{\sqrt n},\qquad
 \psi(x):=\sum_{n\le x}\Lambda(n).
\]
Then
\[
 \boxed{V(xy)\ge V(x)+V(y)\quad\forall x,y\ge1.}\tag{A}
\]
The inequality is strict if x,y>=2. Equivalently, with the log-width staircase
\[
 v(t):=\sum_{\log n\le t}\frac{\Lambda(n)}{\sqrt n},
\]
we have
\[
 \boxed{v(a+b)\ge v(a)+v(b)\quad\forall a,b\ge0.}\tag{B}
\]

Crucially, (A) uses actual von Mangoldt coefficients. It fails for the toy nonnegative weight supported only at n=2. However a finite small-range search indicates that the shifted model Lambda(n)cosh(theta log n) ALSO obeys analogous superadditivity for theta=.05 through 5, so (A) is NOT presently an RH discriminator.

## 2. Only two externally established unconditional inputs

The proof uses these already-established non-RH Chebyshev facts:

1. Eberl, *Concrete bounds for Chebyshev's prime counting functions*, Archive of Formal Proofs (2024), https://isa-afp.org/entries/Chebyshev_Prime_Bounds.html : \(\psi(z)\ge(9/10)z\) for every real z>=41. The source provides machine-checked Isabelle proofs.
2. Rosser–Schoenfeld's upper bound \(\psi(z)\le(26/25)z\) for all z>=0, recorded explicitly as Lemma 5 by Johnston, Ramaré and Trudgian, *An explicit upper bound for L(1,chi) when chi is quadratic*, *Research in Number Theory* 9:72 (2023), https://link.springer.com/article/10.1007/s40993-023-00476-4 .

Neither estimate assumes RH.

## 3. Proof on the infinite region, reduced to ONE rational inequality

Partial summation gives, for z>=1,
\[
 V(z)=\frac{\psi(z)}{\sqrt z}
      +\frac12\int_1^z\frac{\psi(t)}{t^{3/2}}\,dt .
\]
The two cited Chebyshev bounds yield
\[
 \boxed{V(z)\le\frac{52}{25}\sqrt z-\frac{26}{25}\quad(z\ge1)}\tag{C}
\]
and
\[
 \boxed{V(z)\ge\frac95\sqrt z-\frac9{10}\sqrt{41}
            \quad(z\ge41).}\tag{D}
\]

If x,y>=2 and xy>=41, subtracting the two upper estimates from the lower gives
\[
 V(xy)-V(x)-V(y)\ge
 F(\sqrt x,\sqrt y)
 :=\frac95\sqrt{xy}-\frac9{10}\sqrt{41}
   -\frac{52}{25}(\sqrt x+\sqrt y)+\frac{52}{25}.
\]

Assume without loss of generality that y>=203 and x>=2. The partial derivatives of F with respect to the independent root variables \(X=\sqrt x\), \(Y=\sqrt y\) are
\[
\partial_XF=\tfrac95Y-\tfrac{52}{25}>0,\qquad
\partial_YF=\tfrac95X-\tfrac{52}{25}>0,
\]
because X>=sqrt2>7/5 and Y>=sqrt203>2. Thus F is minimized at x=2, y=203.

The following one-sided rational root bounds are proved merely by squaring integers:
\[
 \sqrt{406}>\tfrac{20149}{1000},\quad
 \sqrt{41}<\tfrac{6404}{1000},\quad
 \sqrt2<\tfrac{1415}{1000},\quad
 \sqrt{203}<\tfrac{14248}{1000}.
\]
Therefore
\[
 \begin{split}
 F(\sqrt2,\sqrt{203})
 &>\tfrac95\cdot\tfrac{20149}{1000}
 -\tfrac9{10}\cdot\tfrac{6404}{1000}\\
 &\quad-\tfrac{52}{25}
       \left(\tfrac{1415}{1000}+\tfrac{14248}{1000}\right)
 +\tfrac{52}{25}\\
 &=\boxed{\tfrac{139}{25000}>0}.
 \end{split}
\]
Hence (A) is proved for every pair x,y>=2 with max{x,y}>=203, a fully INFINITE region, with no numerical sampling of large x.

## 4. The finite remainder, certified by INTEGER arithmetic only

For 2<=x,y<203, let n=floor(x), m=floor(y). Then 2<=n,m<=202 and the right-continuous staircase obeys V(x)=V(n), V(y)=V(m), while xy>=nm gives V(xy)>=V(nm). Therefore it suffices to prove
\[
 \boxed{V(nm)>V(n)+V(m)\quad(2\le n,m\le202),}\tag{E}
\]
exactly 201²=40,401 finite integer cases, with nm<=40804.

The companion checker
experiments/abel_prime_common_map/certify_global_weighted_chebyshev_superadditivity.py
does NOT call floating-point arithmetic, prime tables or unverified epsilon assumptions. It sieves primes through 40804, generates every prime power p^k there, and encloses each transcendental term log(p)/sqrt(p^k) by exact scaled integer lower/upper bounds at scale B=10^12:

- For each p, dyadically reduce p/2^j∈[1,2]; use log z=2 sum_{k=0}^{15} w^{2k+1}/(2k+1)+R with w=(z-1)/(z+1)≤1/3. The positive remainder is strictly less than 1/B, verified by the integer inequality 9B<4(33)3^33. Every operation rounds down for lower and up for upper.
- Enclose sqrt(q) via root_lo=isqrt(q B²); set root_hi=root_lo+1. Then exact term bounds are v_lo=floor(B logp_lo/root_hi) and v_hi=ceil(B logp_hi/root_lo). No approximate real is compared in the acceptance conditions.
- Accumulate V_lo and V_hi for every n≤40804 and certify the exact rational inequality V_lo[nm]-V_hi[n]-V_hi[m] > 0 for every pair.

The recorded output is:

    Large-domain analytic rational gap >= 139/25000
    ALL 40,401 integer pairs 2<=n,m<=202 certified strictly positive
    Minimum outward rational gap: 490728619104 / 1000000000000 at (2, 2)
    Events: 4353 prime powers through 40804
    Finite certificate uses exact integer math only
    GLOBAL THEOREM: V(x*y)>=V(x)+V(y) for all real x,y>=1
    Theorem relies on published UNCONDITIONAL psi bounds, NOT RH

For x<2 or y<2, one summand V(x) or V(y) vanishes and V is nondecreasing, so (A) holds trivially. Thus the proof covers every real x,y>=1.

Caveat: the checker is a reproducible arithmetic certificate with an analytic proof of its enclosures, NOT itself a kernel-checked Lean file. The cited infinite-region psi inputs are established theorems; the finite proof has not yet been ported to Lean.

## 5. APPLICATION: sharp exact all-prime graph mass potential for every Weil width

Return to the actual Weil source graph, with L>0, v_n=Lambda(n)/sqrt(n), and **strict support cutoff** ell_n=log n<L (ell_n=L has zero shift overlap). Put
\[
 V_L(u)=\sum_{\ell_n<L,\ \ell_n\le u}v_n,\qquad
 m_L(x)=V_L(x+L/2)+V_L(L/2-x).
\]

For x in the INTERIOR of I_L away from the finite set of potential jumps, choose a small δ>0 such that both staircases are unchanged on reducing their arguments by δ. By (B),
\[
 m_L(x)=v(d_--\delta)+v(d_+-\delta)
 \le v(L-2\delta)\le \sum_{\ell_n<L}v_n=:V_L(L).
\]
This is an a.e. assertion, which is exactly what the quadratic-form multiplication potential needs. Conversely, in a small positive-measure neighborhood of either boundary of I_L, one distance is <log2 and the other is sufficiently close to L to include ALL finite visible shifts ell_n<L, giving m_L(x)=V_L(L).

Therefore the essential supremum is **EXACTLY**
\[
 \boxed{
 \|m_L\|_{L^\infty(I_L)}
 =\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
 =V_L(L)\quad\forall L>0.
 }\tag{F}
\]

This replaces the previous factor-two prime bound 2V_L(L) **unconditionally at every width**, and proves the stronger candidate formerly only seen in numerical probes. The first-prime Lean exact normalization remains a corollary.

With c=cosh(x/2), s=sinh(x/2), the exact source identity from the companion prime_graph_parity_smooth_moment_schur note is
\[
 W_L(f)=
 E_\infty(f)+\sum_{\ell_n<L}v_n\int_{J_{\ell_n}}|f(x)-f(x-\ell_n)|²dx
 +2|\langle f,c\rangle|²
 -|C_\infty|\|f\|²-\int_I m_L(x)|f(x)|²dx-2|\langle f,s\rangle|² .
\]
The negative pole rank-one has norm 2||s||²=2sinh(L/2)-L. Hence, for EVERY finite L,

\[
 \boxed{
 W_L(f)\ge E_\infty(f)-
 \underbrace{[\,|C_\infty|+V_L(L)+2\sinh(L/2)-L\,]}_{B_{\rm sharp}(L)}
 \|f\|².
 }\tag{G}
\]

No RH or zeros are used to establish this improved all-width coercivity budget. At L=18/25 it recovers the EXACT in-tree M_minus = 5.877965579449... certified <147/25. Thus GPPVerify's first-prime result is the special case of a **global exact arithmetic mass theorem**.

The high-moment theorem and finite Schur matrix in the earlier note now use B_sharp(L) with NO optimization, numerical M_L estimate or unproved superadditivity step. This is an arithmetic-specific reduction, but its positivity at all widths, the low-block Schur inequality, and RH remain OPEN.

## 6. Scope, falsifiers and formalization

This is NOT RH and not equivalent to RH. The geometric bound is a statement about the total negative PRIME MASS, not the completed positive Weil pairing. Example: a nonnegative fake weight supported only at n=2 violates (A) for x=y=2, showing some arithmetic specificity; however the known off-line F_theta control may retain superadditivity and must continue to be tested. The source comparison's gamma/pole and all-width low-frequency Schur positivity remain essential.

Lean upstream targets: (i) generic partial-summation estimates for weighted Chebyshev; (ii) the psi bounds, one of which is already fully Isabelle-formalized; (iii) the 40,401 event-based finite certificate, which can be compressed to a min-gap theorem; (iv) multiplicative superadditivity and conversion to additive log scale; (v) universal exact all-prime graph mass operator bound with boundary cutoff handled a.e.; (vi) rerun first-prime M_minus regression. No unverified physical principle is imported.

Sources: AFP Eberl (2024) and Johnston–Ramaré–Trudgian (2023) as URLs above. The numeric and infinite proof was audited separately against source GPPVerify FirstPrimeNegativeBound.lean and ArchimedeanFloor.lean. **No Lean build has been attempted.**
