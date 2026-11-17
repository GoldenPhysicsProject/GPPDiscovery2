# A genuine bulk-edge sewing mechanism without the smallest eigenvalue: nonlocal IMS for the exact Weil kernel

**2026-11-16; exact analytic identity / source-sensitive estimate.** IMS localization is standard analysis, not a new invention. The combination with the arithmetic prime shifts, the explicit gamma error constant, and the certified central surplus provides a concrete route avoiding the badly collapsing rung eigenvalue. **This does NOT prove the all-width Weil form positive; its price can still be exponential in L.**

## 1. The zero-free source form and its nonlocal positive kinetic channel

For real compactly supported f, the actual prime+gamma+constant part of the source Weil form is
\[
 W_0(f)=E_\infty(f)+C_\infty\|f\|^2-2\sum_{\ell_n<L}v_n \int f(x)f(x-\ell_n)dx,
\]
where \(w(t)=e^{-t/2}/(1-e^{-2t})\),
\(E_\infty(f)=\int_0^\infty w(t)\|f-T_t f\|^2dt\),
\(\ell_n=\log n,\ v_n=\Lambda(n)/\sqrt n\).
The rank-two signed pole remains separate:
\[
 W(f)=W_0(f)+2|\langle f,\cosh(x/2)\rangle|^2-2|\langle f,\sinh(x/2)\rangle|^2.
\]

## 2. EXACT nonlocal IMS identity for prime and archimedean channels

Choose real bounded measurable multipliers \(\chi_1,\chi_2\) with
\(\chi_1(x)^2+\chi_2(x)^2=1\) pointwise, and assume sufficient Lipschitz regularity. Put
\(D_\chi(x,y)^2=\sum_{j=1}^2(\chi_j(x)-\chi_j(y))^2\).
For the gamma translation energy, simple expansion gives
\[
 \sum_{j=1}^2\|\chi_j f-T_t(\chi_j f)\|^2-\|f-T_tf\|^2
 =\int_{\mathbb R} f(x)f(x-t)D_\chi(x,x-t)^2 dx.
\]
For each actual prime-power shift,
\[
 \sum_j [-2v_n A_{\chi_jf}(\ell_n)] - [-2v_n A_f(\ell_n)]
 =v_n\int f(x)f(x-\ell_n)D_\chi(x,x-\ell_n)^2dx.
\]
The constant C_infty term localizes EXACTLY because sum chi_j²=1. Combining:
\[
 \boxed{
 \sum_j W_0(\chi_jf)-W_0(f)=\mathcal R_\chi(f),
 }\tag{1}
\]
\[
 \boxed{
 \mathcal R_\chi(f)=\int_0^\infty w(t)\int f(x)f(x-t)D_\chi(x,x-t)^2dx\,dt
 +\sum_{\ell_n<L}v_n\int f(x)f(x-\ell_n)D_\chi(x,x-\ell_n)^2dx.
 }\tag{2}
\]
Every term uses the ACTUAL positive gamma kernel or positive von Mangoldt coefficient. Since f can change sign, R_chi is NOT automatically positive; its absolute value can be bounded. The total completed W identity is (1) with the pole contribution held GLOBAL:
\[
 W(f)=\sum_j W_0(\chi_j f)+\mathrm{Pole}(f)-\mathcal R_\chi(f).
\]
This explicitly avoids accidentally localizing the indefinite rank-one pole as a positive contribution.

## 3. A concrete error budget, independent of the smallest eigenvalue

Let \(\chi_1=\cos\vartheta,\chi_2=\sin\vartheta\) with |\vartheta(x)-\vartheta(y)|<=A|x-y|. Then
\[
 D_\chi(x,y)^2=4\sin^2((\vartheta(x)-\vartheta(y))/2)
 \le\min(4,A^2|x-y|^2).
\]
Cauchy-Schwarz for translations gives
\[
 \boxed{|\mathcal R_\chi(f)|
 \le \|f\|^2\left[
 A^2 C_\gamma+\sum_{\ell_n<L}v_n\min(4,A^2\ell_n^2)
 \right].}\tag{3}
\]
The gamma error constant is EXACT:
\[
 C_\gamma=\int_0^\infty t^2w(t)dt
 =2\sum_{k\ge0}(2k+\tfrac12)^{-3}
 =\tfrac14\zeta(3,\tfrac14)
 =\boxed{7\zeta(3)+\frac{\pi^3}{4}}.
\]
The final equality follows from separating odd integers by residue mod 4 and the standard Dirichlet beta value beta(3)=pi³/32. This is a finite absolute error with NO inverse smallest eigenvalue and NO Schur division by lambda_min. It is thus an **alternative carrying mechanism** for positivity across spatial pieces.

But the prime price in (3) can be O(V_L(L)) for partition transitions on a macroscopic fraction of the width, and V_L(L)~2e^{L/2}. **Therefore this method alone is NOT a uniform certificate or RH proof.** One must exploit the actual localization of the error integral or choose adaptive partitions to absorb it against a genuine spatial reserve.

## 4. Exact positive central mass reserve can be paired against this localization price

The separately proved GLOBAL weighted-Chebyshev theorem gives
\[
 m_L(x)=V(e^{L/2+x})+V(e^{L/2-x})\le V(e^{L^-})
\quad\text{for a.e. }x\in I_L.
\]
Set q_L(x)=V(e^{L^-})-m_L(x)>=0. The stronger theorem in
research/monotone_reweighting_f_theta_falsifier_central_deficit_2026_11_16.md proves
\[
 \boxed{q_L(x)\ge(7/10)e^{L/2}\qquad
      L\ge8\log4,\quad |x|\le L/4\quad\text{a.e.}.}\tag{4}
\]
The actual Weil form is thus
\[
 W_L(f)=E_\infty(f)+E_{\rm prime}(f)+\int q_L|f|^2
 +2|\langle f,c\rangle|^2
 -(|C_\infty|+V(e^{L^-}))\|f\|^2
 -2|\langle f,s\rangle|^2.
\]
This identifies the right quantity to pay a localization/sewing price WITHOUT invoking a tiny previous-rung eigenvalue: the bulk surplus q_L. A viable induction would need the *localized* R_chi absorption inequality, plus control of the remaining boundary/odd-pole block. No such global inequality is claimed here.

## 5. Reproducibility and formalization

Exact rational finite-graph IMS check:
experiments/abel_prime_common_map/verify_graph_ims_sewing.py, with rational two-component unit partitions at four vertices. It tests (1)-(2) on a finite toy graph, NOT on the zeta Weil operator.

Lean/Mathlib-friendly lemma: for any finite weighted graph with nonnegative edges and real partition of unity Σχ_j²=1, the difference of summed edge Dirichlet forms equals Σ_edges w_ij f_i f_j Σ_j(χ_j(i)-χ_j(j))². Apply to the translation integral and finite prime-power sum. Next: prove C_gamma as a special zeta/beta evaluation; avoid unproved Dirichlet beta value if not already in Mathlib and retain the convergent series as the certified constant. Preserve the pole as rank two (one negative odd mode).

**Conclusion:** a mathematically valid localization-carrying mechanism exists that does not divide by lambda_min. Its error is explicit and finite, but not yet small enough to establish the missing source Weil positivity at arbitrary width. This is the precise remaining challenge.
