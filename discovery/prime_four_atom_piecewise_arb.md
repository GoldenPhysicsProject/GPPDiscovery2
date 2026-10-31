# Rigorous all-function Hardy-Schur absorption across the p=5 activation: L ≤ 41/25

2026-10-31 | Codex / GPPDiscovery2 | **proved analytic reduction + Arb-verified finite rational witness**, CI success. This supersedes the former 39/25 *prime absorption* bound but does **not** improve the much shorter 5/32 **full completed Weil** bound and does not establish RH.

## Theorem

Let E_L[f]=∫₀∞ (q_f(0)−q_f(y))/(2sinh y)dy and S_L[f]=Σ_(p^k≤e^L)(log p)/sqrt(p^k) q_f(k log p), q_f(y)=2 Re∫conj(f(x))f(x+y)dx, for a complex function f supported on [0,L], zero-extended to R, of finite kinetic energy. Then for **every** 0<L≤41/25 (including the entire infinite-dimensional form domain):

\[
\boxed{E_L[f]-S_L[f]\ge \frac{1}{125}\lVert f\rVert_2^2.}
\]

At rational endpoint L₀=41/25=1.64 the full true prime-power set consists of n=2,3,4,5, because log5<L₀<log6. The right side remains nonnegative for f=0, and strict if f≠0.

## Proof: positive piecewise ground-state witness

Let H(t)=log coth(t/2) and V_L(x)=½[H(x)+H(L−x)]. The exact Hardy zero-extension inequality is E_L[f]≥∫₀ᴸ V_L(x)|f(x)|²dx.

Let A_L be the **positive prime adjacency operator**

\[
(A_Lh)(x)=\sum_{p^k\le e^L}\frac{\log p}{\sqrt{p^k}}
\big[\mathbf 1_{x+\log(p^k)<L}\,h(x+\log(p^k))
+\mathbf 1_{x>\log(p^k)}\,h(x-\log(p^k))\big].
\]

For any strictly positive, measurable bounded profile h, the exact two-vertex SOS from Verify's GppPathSOS.term_identity gives

\[
S_L[f]\le\int_0^L\frac{(A_Lh)(x)}{h(x)}|f(x)|^2\,dx.
\]

So it suffices to exhibit a positive h such that A_L h ≤ (99/100) V_L h pointwise a.e. The script **discovery/prime_four_atom_piecewise_arb.py** rigorously exhibits such an h at L₀=41/25:

1. Partition [0,L₀] into 256 *exact rational* equal cells. Use a positive step function h constant on each cell, with rational heights of denominator 10⁶.
2. V_L is symmetric and convex (H''>0), so its exact minimum on a cell is V_L at the cell point nearest L/2. Compute a conservative **rational lower bound** V_i^- and **Arb verify** V_i^- < V_L(x) throughout cell.
3. Create *rigorously verified rational brackets* for log2, log3, log4, log5. For each source cell and each +/− shift, include **every** target cell that the shift could reach within those brackets. This may overcount but can never miss a possible edge.
4. Arb verify conservative **rational upper weights** w_n^+ > log(p)/sqrt(n) for n=2,3,4,5.
5. A floating fixed-point iteration h←1+A_upper h/V_lower produces a candidate rational witness. **The iteration is not part of the certificate.** Round the heights to positive fractions, then verify *all 256* inequalities exclusively by exact Python Fraction arithmetic:
   Σ_edges w_n^+ max_(possible target cells j) h_j < (99/100) V_i^- h_i.
   The minimum exact-rational slack is positive, approximately 0.4758 in the unscaled cell inequality. No floating arithmetic decides these signs.
6. Convexity, the certified log interval cover, and the inequalities imply A_L₀ h < (99/100) V_L₀ h pointwise a.e. Hence E_L₀−S_L₀≥(1/100)∫V|f|² ≥ (H(L₀/2)/100)||f||².
7. Arb proves H(L₀/2)>4/5, so (H(L₀/2)/100)>1/125. Numerically H(L₀/2)≈0.94553243284, but the claimed scalar proof is based on the rigorous >4/5 comparison.
8. For L<L₀ **do not rely on scale monotonicity of the piecewise profile**. Simply zero extend the same f into [0,L₀]. E and S are the identical functionals of f in the ambient R space (new prime-power shifts beyond its support contribute q=0). Consequently endpoint positivity automatically restricts to every smaller support.

The exact rational certificate is independent of whether the floating iteration converges quickly or accurately; it only uses a produced rational positive witness and checks every necessary inequality. The Arb evaluations are confined to elementary transcendental comparisons.

## Reproducibility

- Source: https://github.com/GoldenPhysicsProject/GPPDiscovery2/blob/codex/discovery-workbench/discovery/prime_four_atom_piecewise_arb.py
- GitHub Actions: https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41206500605 , **completed SUCCESS**, head 09f48a896800027c517882bc0f05a75ca4fd137c.
- In the same workflow all prior certificates (5/32 full Q, 57/50, 38/25 and 39/25 prime absorption) rerun green.
- The separate exact *full* Weil gamma/prime/pole decomposition and its numerical smoke tests are at discovery/semilocal_full_gamma_prime_pole_sos.md, CI https://github.com/GoldenPhysicsProject/GPPDiscovery2/actions/runs/41205950925.

## Important logical boundary

The corrected completed Weil form still has Q_L[f]=(E_L−S_L)[f]+P_L[f]−(log4π+γ)||f||²−A_L[f]. The guaranteed 1/125 contribution cannot by itself dominate the negative contact and regular gamma tilt or the reflection-odd negative pole channel. The **completed full Q remains proved only up to L≤5/32** (prime-free) in our present research. RH remains OPEN.

## Next research

Use the exact full-operator SOS (retaining the positive interior jump and prime edge squares) and a **moment-aware fractional Poincaré/Schur** estimate to pay the remaining negative potential. Test piecewise rational supersolutions in both reflection parity sectors, including the weak even mode; do not make a false blanket spectral-gap assumption. To promote into Verify, import the already merged GppPathSOS.term_identity / edge_sum_le, formalize generic weighted-supersolution⇒positivity, and then a separate certificate interpretation for transcendental bounds.
