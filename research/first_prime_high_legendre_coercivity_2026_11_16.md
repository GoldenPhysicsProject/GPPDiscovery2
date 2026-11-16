# Explicit rising high-mode coercivity for the actual first-prime Weil form

**Date:** November 16, 2026. **Scope:** Analytic derivation, exact rational test executed locally; pending independent review and Lean compilation. **Not** a proof of full first-prime positivity or RH.

This extends \`research/first_prime_layercake_index3_2026_11_16.md\` and the exact first-prime Haar/Legendre construction. The earlier m=3 result gives the sharpest dimensional negative-index bound. The NEW ingredient here is a much stronger \`W\` lower bound on the far Legendre tail, which significantly reduces the residual penalty needed for a genuine finite-section Schur proof.

Let \(L=18/25\), \(I=[-L/2,L/2]\), \(e_n(x)=\sqrt{(2n+1)/L}P_n(2x/L)\) and \(W=E+\langle \cdot,K_L\cdot\rangle\) be the EXACT Weil form from Verify, with archimedean energy multiplier
\[
a(r)=2\sum_{k\ge0}\frac{r^2}{(2k+1/2)((2k+1/2)^2+r^2)}.
\]
The source-supported prime/pole and real-place constant give \(W(f)\ge E(f)-(147/25)\|f\|_2^2\), independently of any assumed positivity.

## 1. Direct high-Legendre spectral bound

Suppose \(f\) is orthogonal to the first \(m\) Legendre basis functions, i.e. \(\int_Ix^jf(x)\,dx=0\) for \(j=0,\dots,m-1\). Take the rational cutoff \(R_m=m/L\), so \(z_m=R_mL/2=m/2\).

The Rodrigues/Parseval bound from the companion work, using only \(|h_n(z)|\le1\), gives the COMPLETE frequency-tail inequality
\[
\int_{-R_m}^{R_m}|\widehat f(\xi)|^2d\xi\le\delta_m\|f\|_2^2,
\]
\[
\boxed{
 \delta_m\le \frac{m}{3}\frac{(m/2)^{2m}}{[(2m+1)!!]^2}
 \frac1{1-\frac{m^2}{4(2m+3)^2}} .
}\tag{1}
\]
This requires only \(\pi>3\). For large m the explicit bound is exponentially tiny. The elementary inequalities
\((2m+1)!!\ge2^m m!\), \(m!\ge(m/e)^m\), and \(e<3\) give the uniform rational upper estimate
\[
\boxed{
 \delta_m<\frac{16m}{45}\left(\frac9{16}\right)^m.
}\tag{2}
\]
One can also avoid Stirling or exponential comparisons entirely by evaluating (1) as an exact rational number.

Thus, for any \(K\ge1\), with the finite positive rational multiplier
\[
 a_K(R)=\sum_{k=0}^{K-1}\frac{16R^2}{(4k+1)((4k+1)^2+4R^2)},
\]
we have
\[
\boxed{\quad W(f)\ge\left[a_K(R_m)(1-\delta_m)-147/25\right]\|f\|_2^2.\quad}\tag{3}
\]
All quantities are explicit and the estimate covers every smooth compact-support test satisfying the m moments, not a finite Galerkin matrix.

## 2. Three independently executed exact rational receipts

Take \(K=1000\), and evaluate the finite sum and (1) with \`fractions.Fraction\`, retaining the strict comparisons as rational:

| m | R_m | Proven rational comparisons | Concluded analytic high-tail inequality |
|---|---|---|---|
| 50 | \(625/9\) | \(a_{1000}(R_m)>77/10,\ \delta_m<1/1000\) | \(W(f)>(9/5)\|f\|_2^2\) |
| 70 | \(875/9\) | \(a_{1000}(R_m)>81/10,\ \delta_m<1/1000\) | \(W(f)>(11/5)\|f\|_2^2\) |
| 100 | \(1250/9\) | \(a_{1000}(R_m)>42/5,\ \delta_m<1/1000\) | \(W(f)>(5/2)\|f\|_2^2\) |

For example at m=100, the final strict rational margin is
\[
 \frac{42}{5}\left(1-\frac1{1000}\right)
 -\frac{147}{25}-\frac52
 =\frac{29}{2500}>0.
\]
Every finite rational substatement was **independently executed on Nov 16** with the exact Python script
\`experiments/abel_prime_common_map/check_first_prime_high_mode_tail.py\`.
The analytic use of Fourier Plancherel and Legendre completeness remains an audit/formalization obligation.

These are lower bounds for the entire infinite-dimensional space orthogonal to the first m Legendre modes. Increasing m produces increasing possible lower bounds, and the elementary formula a(R) grows logarithmically: indeed, when \(2k+\tfrac12\le R\), the kth summand of a(R) is at least \(1/(2k+\tfrac12)\). Combining with (2) proves \(W|_{\Pi_{\ge m}H}\) has a coercivity floor tending to infinity as \(m\to\infty\). This gives a quantitative compact-resolvent / discrete-spectrum mechanism for the fixed-width selfadjoint form, stronger than merely 'identity plus compact' in the energy norm.

## 3. Concrete full-residual Schur certificate

Let \(H_m\) be the L²-orthogonal complement of e_0,...,e_{m-1}; the true form satisfies \(W(h)\ge\gamma_m\|h\|_2^2\) there, with \(\gamma_{50}=9/5\), \(\gamma_{70}=11/5\), \(\gamma_{100}=5/2\). Let \(g_1,\dots,g_d\) be finite, explicit trial vectors in the operator domain (finite Legendre combinations are acceptable: their zero-extensions have Fourier decay \(O(1/r)\), and \(a(r)=O(\log(2+|r|))\), so \(a(r)\widehat g_i(r)\in L²\)).

If \(g_i\) are approximate solutions eliminating the **intermediate** modes e_d,...,e_{m-1}, write the full residuals against the high tail as
\[
 r_i=\Pi_{\ge m}(Tg_i)\in H_m,\qquad T=A_{\rm arch}+K_L,\quad
 W(g_i,h)=\langle Tg_i,h\rangle_{L²}.
\]
Here T is the unbounded selfadjoint form operator, and for finite Legendre combinations \(g_i\) it has the L² action described by the Fourier multiplier \(a(\xi)\) plus bounded K_L. The **exact** sufficient certificate is
\[
\boxed{
  \lambda_{\min}\left(\big(W(g_i,g_j)\big)_{i,j\le d}\right)
  >\gamma_m^{-1}\,\big\|\big(\langle r_i,r_j\rangle\big)_{i,j\le d}\big\|_{\mathrm{op}}
}\tag{4}
\]
**provided** the g_i also solve the finite Galerkin elimination in the intermediate modes, so that the remaining positive high block and their cross terms are the only uneliminated couplings. More invariantly, the full finite \(d\)-dimensional corrected Schur matrix must dominate \(\gamma_m^{-1}R^*R\). A numerical Ritz principal matrix alone does not prove (4); the residuals must be norm-bounded in the complete \(H_m\).

A more practical decomposition chooses \(d=5\) and solves the positive finite Galerkin block on n=5,...,m-1. The m=5 spectral layer-cake result supplies positive coercivity \(27/100\) to the WHOLE intermediate-plus-tail block; the present m=100 result strengthens the **remaining tail** to \(5/2\). The resulting two-stage Schur decomposition preserves all mixed terms and provides a much smaller error penalty.

### Independent numerical diagnostic, not part of proof

I reconstructed the full real-space Weil matrix using Gauss–Legendre quadrature for the actual translation energy, exact archimedean tail, n=2 compressed prime overlap and exact pole integrals, at 12,20,30,50,70 Legendre modes. At n=70 the first finite Ritz eigenvalue is ~0.0008496503, positive, and the even/odd split is stable. However, the full first-prime positive Schur complement is not yet certified and the minimum is small enough that interval and residual error management are essential.

I also tested the 5-mode Schur correction against a 140-mode numerical Galerkin matrix: after eliminating modes n=5,...,99, the residual from modes n=100,...,139 has norm ~0.02135. This is a **lower bound on the unknown full residual norm**, not an upper bound; it CANNOT be used as a certificate. The sharper high-mode coercivity m=100 improves the approximate penalty to about 0.00018 for this *truncated residual*, versus ~0.00169 under the old 0.27 high-block bound. The finite corrected Schur margin is ~0.00085, so an independently proven complete-tail residual bound may now be viable. Do not claim success until the infinite tail has been rigorously bounded.

## 4. Lean and Turbo audit targets

1. Formalize the generic Legendre orthogonality and bound (1), independent of Weil.
2. Kernel-check the exact rational 1000-term a_K comparisons and δ_m bounds at m=50,70,100.
3. Transfer (3) into Verify's exact Weil form at support width 18/25.
4. Construct actual low/intermediate/high Schur blocks from the real-space operator, retaining the **entire** dual residual beyond each finite cutoff.
5. Certify the full residual analytically/with directed intervals, including all prime, archimedean and pole mixed contributions. Only then test positivity on the remaining low block.
6. Test the identical construction against the F_theta deformation. Plain Haar or high-frequency positivity is not a ζ-specific discriminator.

**Status:** analytic proof candidate + exact rational calculation; formal CI and full first-prime positivity NOT completed. No RH claim.
