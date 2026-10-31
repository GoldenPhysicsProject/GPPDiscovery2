# First-prime completed Weil at L=7/10: all odd functions positive and at most ONE possible negative direction in the entire form

2026-10-31 | Codex/Discovery2. This is an **unconditional infinite-dimensional negative-index reduction** for the ACTUAL prime-inclusive corrected v34 completed Weil form at the single fixed logarithmic support L=7/10>log2. It does NOT show all-test PSD even at this L and does NOT prove RH.

## Theorem

Let Q_L be the corrected completed one-sided Weil Hermitian quadratic form on the logarithmic kinetic form domain of complex L²(0,L), L=7/10. The only prime power is p=2.

1. **Strict full mirror-odd positivity:** for every f with f(L−x)=−f(x),
\[
Q_L[f]\ge \tfrac1{100}\|f\|².
\]
2. **Global negative index at most one:**
\[
\boxed{\operatorname{ind}_-(Q_L)\le1.}
\]
Equivalently, there cannot exist a two-dimensional complex linear subspace on which Q_L is strictly negative definite. Because the odd subspace is positive and the reflection-even/odd subspaces exactly decouple, any negative eigenvector of the completed fixed-support selfadjoint form, **if one exists**, must lie in the global mirror-even sector and have multiplicity one. This is a genuine infinite-dimensional statement, not a finite Fourier matrix extrapolation. It does NOT claim there is a negative eigenvector.

## Proof part A: exactly pay the TRUE first-prime source using Hardy's UNUSED singular endpoint curvature

For L=.7, a=log2, epsilon=L−a, w=a/sqrt2, define strips A=[0,epsilon],B=[a,L], boundary mass M and cross-edge square D:
\[
-S_{p=2}[f]=wD[f]-wM[f]
\]
for ALL complex f. The exact full corrected completed form is
\[
Q_L[f]=\int_0^L(V_L-\Gamma_L-c_\infty-w1_{A\cup B})|f|²
+J_\gamma[f]+wD[f]+2|C_f|²-2|T_f|².
\]
No gamma tail or source contact omitted, no RH assumption. With H(z)=log coth(z/2), V_L=½(H(x)+H(L−x)), write \(t=(x-L/2)/L\) and retain the six positive even Hardy Taylor coefficients through degree 12:
\(P_6(t)=H(L/2)+\sum_{r=1}^6 K_{2r}t^{2r}\).
Since all K_{2r}>0, the entire omitted Hardy remainder R6=V−P6 is pointwise nonnegative and monotone in |t|. The endpoint strips have minimum R6 at x=epsilon and x=a, and **256-bit outward Arb rigorously certifies**
\[
R6_{\mathrm{endpoint,min}}=0.51086057394217007168\ldots
>w=0.49012907173427359585\ldots.
\]
Thus \(V_L-w1_{A\cup B}\ge P_6\) POINTWISE on the whole support. The true negative prime tax is fully paid by unused Hardy curvature, while the positive genuine prime-edge gradient wD remains; dropping only wD gives a valid lower comparison on ALL f.

## Proof part B: positive logarithmic Legendre background and true signed poles

With 0<y≤L=.7, \(e^{y/2}/(2\sinh y)\ge1/(2y)+11/50\), so exact positive completed gamma jump
\(J_\gamma\ge J_0+(11L/50)\mathrm{Var}\) with the exact shifted-Legendre log-jump spectrum H_n (harmonic numbers). Regular gamma tilt has \(\Gamma_L\le e^{L/4}-1\); all positive K_{2r}t^{2r} remain. Pole term is exactly \(+2|C_f|²-2|T_f|²\), with C in reflection-even and T in reflection-odd.

On odd sector: drop positive prime gradient and use \(-2|T_f|²\ge -2(\sinh(L/2)-L/2)\|f\|²\), then exact Legendre Jacobi bandwidth12 and an infinite high tail with scalar floor. The 6×6 odd low/high Schur matrix shifted by κ=1/100 is rigorously interval-positive (smallest midpoint LDL pivot 0.07583694909), and high floor>κ. Hence Q_odd≥κ||f||².

On even sector: the negative sinh pole vanishes; keep the positive cosh pole via exact low projections c0,c2 and a rigorously bounded entire higher-mode residual using a Young square, \(\eta=10^{-5}\). The low even space is e0,e2,...,e12 (7 dimensions), the ENTIRE even high remainder is n≥14. Positive Hardy t^{2r} polynomial has bandwidth12, so low/high coupling has exactly six columns n=14,16,...,24. The high–high curvature is PSD and can be dropped, leaving high floor \(h_e>0\). Let E be the exact 7×7 even low comparison matrix and C_e the 7×6 exact low/high coupling. The infinite-dimensional comparison quadratic form has the Hilbert-space Schur complement
\[
S_e=E-C_e C_e^{\mathsf T}/h_e.
\]
By completing the square, **its negative index equals the negative index of S_e**. FLINT/Arb at 256 bits applies exact unpivoted LDL to the actual interval matrix S_e, asserting every pivot strictly separated from zero. The certified signs are
\[
\boxed{(+,-,+,+,+,+,+).}
\]
The first two pivot enclosures are approximately +0.14106869092968385822 and −0.03660755110423493981; subsequent five pivots are STRICTLY positive (≈1.84446, 1.46662, 1.74995, 1.96617, 2.10137). All positive and negative signs have tiny outward errors (~1e−72). Hence the comparison has exactly ONE negative direction, while the odd comparison is strictly positive. Since the ACTUAL Q≥the comparison as Hermitian quadratic forms on the entire completed form domain, monotonicity of the negative index proves \(\operatorname{ind}_-(Q)\le1\).

This at-most-one conclusion does NOT rely on the actual comparison negative pivot being a genuine negative eigenvalue of Q. Comparison is a LOWER form, so an actual strictly POSITIVE Q is completely consistent with a negative comparison eigenvalue.

## Reproducibility

- Complete strict odd positive form and pointwise prime tax payment: GPPDiscovery2 discovery/actual_p2_complete_mirror_odd_fullspace_7_10.md, script discovery/arb_true_p2_odd_hardy_remainder_7_10.py, **GitHub Actions 41232717596 SUCCESS**.
- New full-space negative-index bound: GPPDiscovery2 discovery/arb_actual_p2_even_comparison_inertia_7_10.py, **GitHub Actions 41232909222 SUCCESS** on exact head 278a4d1eb57f762143ffd0d57ab11a08301bdc54. Prints and certifies the full 7-pivot sign pattern; same script imports the previously checked true p2 source and odd proof. No floating-point eigensolvers determine any sign.
- Independent direct Q0 negative at L=.75/true p2 repair: CI 41232244549 and earlier team CI 41231660694.
- Note is restricted to one support L=.7; mirror-even singleton defect remains unclosed; false-shifted F_theta still has local positive graph squares, so no arithmetic selecting principle or RH.

## Next precise target

Either find a **structurally exact nonlocal rank-one supplier** that makes the one remaining mirror-even defect of the LOWER comparison nonnegative, or replace the coarse gamma/pole/Hardy lower comparison with a sharper one retaining more signed arithmetic and endpoint information. The global RH-strength issue remains a support-uniform completed prime–Archimedean sewing law that rejects F_theta. Never present one fixed support's index bound as all-support positivity.
