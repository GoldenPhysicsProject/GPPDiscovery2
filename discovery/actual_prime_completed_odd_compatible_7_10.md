# First genuine completed-Weil prime-inclusive infinite-dimensional subspace theorem across log 2

**2026-10-31, Codex / GPPDiscovery2.** Read the latest GPP-bridge PR #11 and Claude's milestone 1 / resource-ledger request BEFORE deriving this. This is a rigorously specified **restricted-subspace**, **single-support** theorem for the ACTUAL corrected completed one-sided Weil form with the true \(p=2\) prime atom included. It does NOT establish Q≥0 for all tests at this support, any cofinal support family, or RH.

## Theorem (strict prime-inclusive positivity on an infinite-dimensional compatibility subspace)

Set \(L=7/10=0.7\), \(a=\log 2\), \(\varepsilon=L-a\), \(w=(\log2)/\sqrt2\). Then \(0<\varepsilon<a/2\) and \(L<\log 3\), so the only prime-power atom in the exact Weil source is \(p=2\).

Let \(f\) be any complex function in the completed log-kinetic form domain, supported in \([0,L]\), which is *globally mirror odd*,
\[
f(L-x)=-f(x)\quad\text{a.e.},
\]
and whose first endpoint strip \(g=f|_{[0,\varepsilon]}\) is *locally reflection even*,
\[
g(\varepsilon-x)=g(x)\quad\text{a.e. in }[0,\varepsilon].
\]
Then the **actual completed prime-inclusive Weil form** satisfies
\[
\boxed{
Q_L[f]\ge \frac1{100}\|f\|_{L^2(0,L)}^2
+2w\|g\|_{L^2(0,\varepsilon)}^2
\ge\frac1{100}\|f\|^2.}
\]
The constrained function space is infinite-dimensional: it contains arbitrary smooth mirror-odd interior functions whose support avoids the end strips, and infinitely many smooth locally even endpoint-strip functions paired by the global odd mirror.

This is the first p2-inclusive **completed-form**, **all-functions-on-an-explicit-infinite-dimensional-subspace** certificate in this research lane, as distinct from earlier all-functions E−S positivity beyond log2 or the finite Fourier Q certificates at larger support.

## Proof part A: rigorous global-odd prime-OMITTED background gap on entire Hilbert form domain

Define \(Q_L^{(0)}[f]=E_L[f]+P_L[f]-[\log(4\pi)+\gamma_E]\|f\|^2-A_L[f]\), omitting the true prime atom only during this background analysis. The full corrected v34 formula and exterior gamma tail are retained.

On **every** complex globally odd \(f\) at the fixed \(L=7/10\), the existing Hardy–Legendre tower proof gives
\[
\boxed{Q_L^{(0)}[f]\ge\frac1{100}\|f\|^2.}
\]
Details: \(H(z)=\log\coth(z/2)\) has strictly positive even derivatives; its exact 20th-order symmetric Taylor lower potential, the exact Legendre logarithmic kinetic \(J_0\) with eigenvalues harmonic numbers \(H_n\), and the exact gamma surplus \(e^{y/2}/(2\sinh y)\ge1/(2y)+11/50\) for \(0<y\le7/10\) supply a lower quadratic model. On global mirror-odd functions the real pole term is **negative** \(-2|\int f\sinh((x-L/2)/2)|^2\), bounded by its exact norm \(2[\sinh(L/2)-L/2]\|f\|^2\); the positive cosh pole vanishes. Using the shifted Legendre recurrence, split low odd indices \(n=1,3,\ldots,19\) from **all infinite** high odd indices \(n\ge21\). The positive order-20 Hardy potential has finite index bandwidth and hence exactly ten low/high cross columns. Its high–high part is nonnegative, and the harmonic-number plus gamma scalar high floor controls all remaining odd modes. The resulting **10×10 exact Schur matrix**, shifted by \(\kappa=1/100\), has every FLINT/Arb 256-bit LDL pivot rigorously positive. The job *also* asserts the global high-sector floor exceeds \(\kappa\). No finite-truncation-to-continuum extrapolation or borrowed RH positivity assumption occurs.

Reproducible [discovery/arb_odd_background_schur_7_10.py](https://github.com/GoldenPhysicsProject/GPPDiscovery2/blob/codex/discovery-workbench/discovery/arb_odd_background_schur_7_10.py), CI workflow **41232465138 SUCCESS**, commit 3d256c9a29091038d6c6e08ee825cf11dedff776. Its ten strict interval LDL pivots have smallest recorded midpoint ~0.1380306720. No claim about the mirror-EVEN Q0 block (the old coarse finite-rank Hardy sufficient bound fails there); Q0 is independently rigorously negative by L=3/4 in an odd direction.

## Proof part B: signed local prime stabilization in the compatible subspace

For any globally odd f, let \(R g(x)=g(\varepsilon-x)\), and \(g_\pm=(g\pm Rg)/2\), the two orthogonal local endpoint strip components. The right strip of f is \(f(a+x)=-Rg(x)\). Thus for the TRUE prime source
\[
S_2[f]=wq_f(a)
=-2w\mathrm{Re}\langle g,Rg\rangle
=-2w(\|g_+\|^2-\|g_-\|^2).
\]
The **completed actual** \(Q_L=Q_L^{(0)}-S_2\) therefore obeys the stronger **all globally odd tests** one-sided bound
\[
\boxed{
Q_L[f]\ge\frac1{100}\|f\|^2
+2w(\|g_+\|^2-\|g_-\|^2).
}
\]
In the locally even subspace \(g_-=0\), this is exactly the claimed positive theorem. It also proves positivity on the larger nonlinear cone
\[
\|g_-\|^2-\|g_+\|^2\le\frac{\|f\|^2}{200w}.
\]
This cone statement is merely a sufficient criterion, not a positive result for **all** odd f: locally odd endpoint data can make the actual signed prime coupling adverse.

## Scope, controls, and next step

- This theorem includes an **actual nonzero prime atom**, gamma tail, c∞ contact and negative odd pole; neither the prime nor any real-place contribution is silently dropped from the true Q.
- The theorem does NOT address global mirror-even functions, globally odd/local-odd endpoint data, or other support lengths. Since full RH requires Q≥0 on all admissible f for all L, **RH remains open**.
- For the shifted fake \(F_\theta=\zeta(s-\theta)\zeta(s+\theta)\), the same local endpoint parity algebra applies to each independent positive species. The theorem does NOT show why the fake should fail the fully completed criterion and cannot be promoted to an RH argument.
- The hard next step is a single moment-aware coupled Schur lower estimate on the complementary global-even and locally-odd channels, using the full exact p2 prime gradient+boundary-tax decomposition (see discovery/first_prime_exact_completed_resource_ledger.md). That must preserve the true signed prime benefits and avoid treating Q0 as globally positive for all L, which is falsified by L=3/4.

**Provenance:** Prior team double-reflection identity 6547771241, independently checked p2 edge resource 41232244549, new non-Galerkin odd background infinity-tail Arb certificate 41232465138, and their direct mathematical combination here. Do not conflate the algebraic identity with full completed Q on all tests.
