# Codex/GPT formalization update — 2026-08-26

## Scalar-box pole logarithm

CI discrimination on `GPPVerify2:codex/lean-workbench` established that `ScalarBoxPoleEndpointScale` now passes and that the first scalar failure had moved downstream to `ScalarBoxPoleLogScaleBounds`.

Inspection exposed a proof-construction defect in `one_sub_R_le_delta_half`. The desired statement is

\[
R^2=\frac1{1+\delta},\quad 0\le R\le1,\quad \delta\ge0
\Longrightarrow 1-R\le\frac\delta2.
\]

The exact identity is

\[
(1-R)(1+R)=\delta R^2.
\]

Since

\[
R^2\le\frac{1+R}{2},
\]

multiplication by `δ ≥ 0` followed by division by `1+R > 0` gives the result. The previous Lean proof incorrectly invoked a division lemma with denominator `1+R` directly against a goal whose displayed denominator was `2`. The corrected proof was pushed to GPPVerify2 as commit `38d430ec1b8de0e3d3c06d6e4604796ab97c6234`.

Later CI on head `d3abdbf5b23cd523164c8a14ed698bce97029c1a` confirms that the entire pole-log module is now green, including `one_sub_R_le_delta_half`, `one_sub_product_le`, `abs_log_B_le`, and the physical scale theorem `abs_log_t_sub_log_m_div_S_le`. Their printed axiom sets contain no `sorryAx`.

The structured scalar gate then exposed exactly two upstream compiler defects:

1. `ScalarBoxLogSquareRemainder.lowerLogError` and `poleLogError` were executable `def`s over real division. Lean correctly rejected code generation through `Real.instDivInvMonoid`. They have been changed to `noncomputable def` with no mathematical statement change, commit `399464a2f1827cead000f83da22d9de7e233c1c8`.
2. `ScalarBoxSpecialFunctionRemainder.abs_li2Series_neg_a_div_one_sub_a_le_rho` left an inverse-normalization residue in the identity
   \[
   \frac{a/(1-a)}{1-a/(1-a)}=\frac{a}{1-2a}.
   \]
   The proof now factors this through the explicit denominator identity
   \[
   (1-a)\left(1-\frac{a}{1-a}\right)=1-2a,
   \]
   then applies `div_div`. This was pushed as `2f34103c8e6a5edb4ffdfd91670018ededfa3418`.

The structured majorant/core/convergence runs for the new head are pending; no downstream theorem is promoted until those jobs complete.

## Zeta Gibbs differential thermodynamics

The intended real-axis identities remain

\[
S(\beta)=A(\beta)+\beta U(\beta),\qquad
S'(\beta)=-\beta\,\operatorname{Var}_\beta(\log(n+1)),
\]

and

\[
F(\beta)=-\frac{A(\beta)}{\beta},\qquad
F'(\beta)=\frac{S(\beta)}{\beta^2},
\]

for `β > 1` only. The underlying already-certified derivative inputs are `A'=-U` and `U'=-Var`.

The latest proof repair removes fragile coefficient simplification from both derivative theorems. In each case the coefficient identity is first proved explicitly, then rewritten into the `HasDerivAt` goal, leaving Lean only the definitional function equality to check. No theorem statement or domain assumption changed.

- Entropy stabilization: GPPVerify2 commit `ee235a780185749105f6a1b571541ff0ab2524f4`.
- Legendre stabilization: GPPVerify2 commit `5616a30f4873e698cd9dc32dde3234fee6344b80`.

The dedicated Gibbs gate did not reach the entropy theorem itself. Its dependency graph was poisoned by a newly introduced nonexistent direct import `Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt` in `VonMangoldtCubicPositivity.lean`. The actual von-Mangoldt definitions are already supplied transitively through Mathlib's Dirichlet L-series layer used by `GlobalVonMangoldtBridge`. The redundant bad import was removed at commit `a2ee5f9d63b0be2be39c47c54fc191f221132cf2`.

The same CI run also found an independent normalization failure in `VonMangoldtCosineBridge`: simplification of the real part of
\[
n^{-(a+it)}
\]
was not rewriting the complex logarithm and real-part factors robustly. The proof has been rewritten to normalize `Complex.exp_re` with the explicit natural-cast logarithm identity and to eliminate the zero imaginary coefficient before invoking the certified `natCast_neg_cpow_re` theorem. Commit `bb6cbab6822deecb36dee8a5a8b44d2d0ecdb55f`.

These fixes also reopen the strict third-cumulant chain already present in the workbench: positivity of
\[
\sum_{n\ge1}\Lambda(n)(\log n)^2e^{-\beta\log n}
\]
for `β>1`, and its intended bridge to strict decrease of the Gibbs/Fisher variance. Those results are not promoted until current-head CI compiles the chain.

## Boundaries retained

- The scalar core must use the mixed-log structured majorant; the former independent-square majorant is retracted.
- The thermodynamic interpretation is asserted only on the honest Gibbs half-line `β > 1`, not by analytic continuation.
- No half-density or critical-line unitarity theorem is being promoted to an RH zero-location theorem.
- Scalar-box analytic closure is not being promoted to a Yang–Mills or gravity amplitude; honest gauge/gravity cut numerators remain a later layer.
- The global von-Mangoldt/cosine and third-cumulant chain is arithmetic response theory on `Re s > 1`; it is not a zero-location argument.
