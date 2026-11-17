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

## 3. Correct finite-section residual certificate (two-stage coupling must NOT be discarded)

**Important algebraic correction to the earlier handoff.** A lower bound on the *raw high Legendre tail* \(W|_{\Pi_{\ge N}}\ge\gamma_N I\) does **not** imply that the tail remains above \(\gamma_N\) *after eliminating the intermediate modes* \(e_5,\dots,e_{N-1}\). The latter operation produces a negative correction \(G D^{-1}G^*\). It would be WRONG to insert \(\gamma_N^{-1}\) in the earlier low-dimensional Schur residual estimate without also controlling this correction. The m=3 negative-index proof and all high-tail coercivity statements (sections 1–2) are unaffected.

There is a **simpler correct alternative**: form the FULL \(N\times N\) low-frequency Galerkin matrix *first* and subtract a certified all-mode residual.

Let \(P_N\) project in \(L^2(I)\) onto \(e_0,\ldots,e_{N-1}\), and \(Q_N=I-P_N\). Write \(\mathscr A\) for the positive selfadjoint operator associated with the real-place form \(E\); on full-log-line Fourier transforms \((\mathscr A f)^\wedge(\xi)=a(\xi)\widehat f(\xi)\), compressed to \(I\). Let \(T=\mathscr A+K_L\) be the selfadjoint operator associated with the ACTUAL Weil form. The finite Legendre functions are in \(\mathrm{Dom}(T)\): their zero-extensions have \(|\widehat e_n(\xi)|=O(1/|\xi|)\) and \(a(\xi)=O(\log(2+|\xi|))\), so \(\mathscr A e_n\in L^2\).

Set
\[
 M_N=(W(e_i,e_j))_{0\le i,j<N},\quad
 \mathcal R_N=Q_N T P_N:\mathbb R^N\to Q_N L^2(I),\quad
 \Gamma_N=\mathcal R_N^*\mathcal R_N.
\]
For every \(f=p+h\) with \(p=P_N f\) and \(h=Q_N f\) in the form domain, and \(W(h)\ge\gamma_N\|h\|_2^2\),
\[
\begin{aligned}
W(f)&=\langle p,M_Np\rangle
       +2\operatorname{Re}\langle\mathcal R_Np,h\rangle+W(h)\\
&\ge \langle p,(M_N-\gamma_N^{-1}\Gamma_N)p\rangle .
\end{aligned}
\]
Thus the genuine sufficient condition is
\[
\boxed{\quad M_N-\gamma_N^{-1}\Gamma_N\succeq0
\quad\Longrightarrow\quad W(f)\ge0\ \text{for EVERY f supported in I}.\quad}\tag{4}
\]

**Exactly how to evaluate the complete, infinite residual:** Because the e_n are in the operator domain and \(\{e_n\}\) is an orthonormal basis,
\[
\boxed{\quad
(\Gamma_N)_{ij}
=\langle T e_i,T e_j\rangle_{L^2(I)}
 -\sum_{k=0}^{N-1}W(e_k,e_i)W(e_k,e_j).
\quad}\tag{5}
\]
This is an exact finite-matrix identity, NOT a residual defined as "whatever is left." The only infinite-dimensional ingredient is a finite number of ordinary \(L^2\) **source-operator norm integrals** \(\langle T e_i,T e_j\rangle\), which can be estimated with validated quadrature, closed kernel estimates, or verified interval arithmetic. It is crucial to obtain an **upper matrix enclosure** for Γ_N from these integrals. A finite sum over tested tail Legendre modes provides a **lower** matrix enclosure and cannot certify positivity.

The real-space action to integrate is explicitly
\[
\begin{aligned}
(Tf)(x)=
&\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
 (2f(x)-f(x-t)-f(x+t))\,dt\\
&+C_\infty f(x)
+2C_f\cosh(x/2)-2S_f\sinh(x/2)\\
&-\frac{\log2}{\sqrt2}[f(x-\log2)+f(x+\log2)],
\qquad x\in I, \tag{6}
\end{aligned}
\]
with f extended by zero outside I. The apparent endpoint divergences are only logarithmic for piecewise-polynomial e_n and hence their squares are integrable. The same source-form normalization as in GPPVerify is used.

Once the corrected \(N\times N\) matrix in (4) is certified, its *finite* Schur complement into the first 3 or first 5 Haar/Legendre modes is legitimate. This order of operations preserves the intermediate-to-tail coupling. It avoids the false shortcut of using γ_N for an already Schur-compressed tail.

### Equivalent two-stage formulation and its needed extra estimate

Write the full operator in low P, intermediate F and tail H blocks:
\[
\mathcal T=
\begin{pmatrix}
A&B^*&C^*\\B&D&G^*\\C&G&H
\end{pmatrix}.
\]
If D is positive, eliminating F produces
\[
S=A-B^*D^{-1}B,\qquad
R=C-GD^{-1}B,\qquad
H_{\rm eff}=H-GD^{-1}G^*.
\]
Even if \(H\ge\gamma_N I\), it only follows that
\[
H_{\rm eff}\ge
\Big(\gamma_N-\|G D^{-1}G^*\|\Big)I.
\]
Therefore the desired small Schur test is
\[
\boxed{\quad
S-\gamma_{\rm eff}^{-1}R^*R\succeq0,\qquad
\gamma_{\rm eff}:=\gamma_N-\|G D^{-1}G^*\|>0.
\quad}\tag{7}
\]
Both \(R^*R\) and \(G^*G\) are complete tail Gram matrices, expressible by (5) with the appropriate finite linear combinations. An independent operator norm bound for \(G D^{-1}G^*\) is mandatory.

### Numerical feasibility, NOT a certificate

Independent real-space quadrature to 160 Legendre modes suggests:
- at N=100, the finite high-tail Ritz lower bound is ~3.86 and its intermediate-mode Schur correction \(G D^{-1}G^*\) has finite-rank operator norm ~0.17, so the tested effective tail remains strongly positive;
- the finite residual from test modes n=100,...,159 is small compared with the ~0.00085 first Ritz margin.

However these are **finite-window-to-finite-window numerical checks**. Neither the *complete* \(\Gamma_N\) nor the *complete* \(G D^{-1}G^*\) has been upper-bounded. I also tried directly integrating \(\|Tg\|^2\) for Galerkin trial vectors, but straightforward Gauss–Legendre quadrature proved unstable because of endpoint logarithms; at present its computed Gram even developed spurious negative eigenvalues. That method cannot be promoted without endpoint-adapted quadrature and rigorous error bounds. No certificate of first-prime positivity has been obtained.

## 4. Lean and Turbo audit targets

1. Formalize the generic Legendre orthogonality and bound (1), independent of Weil.
2. Kernel-check the exact rational 1000-term a_K comparisons and δ_m bounds at m=50,70,100.
3. Transfer (3) into Verify's exact Weil form at support width 18/25.
4. Construct actual low/intermediate/high Schur blocks from the real-space operator, retaining the **entire** dual residual beyond each finite cutoff.
5. Certify the full residual analytically/with directed intervals, including all prime, archimedean and pole mixed contributions. Only then test positivity on the remaining low block.
6. Test the identical construction against the F_theta deformation. Plain Haar or high-frequency positivity is not a ζ-specific discriminator.

**Status:** analytic proof candidate + exact rational calculation; formal CI and full first-prime positivity NOT completed. No RH claim.
