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

The latest CI discrimination now shows every scalar-box gate through `ScalarBoxLogScaleBounds` green; the first scalar failure is solely `ScalarBoxPoleLogScaleBounds`. The archived Actions job-log blob was transiently unavailable during the latest repair run, so no exact compiler line is being claimed from that run. Source inspection identifies the final `η=m/S` whole-goal normalization as unnecessarily brittle, but no scalar theorem statement has been altered and no speculative scalar patch has been promoted without a compiler signal.

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

Fresh CI for head `5616a30f4873e698cd9dc32dde3234fee6344b80` has started. Until it finishes, these identities remain mathematically derived but are not promoted to compiler-certified.

## Boundaries retained

- The scalar core must use the mixed-log structured majorant; the former independent-square majorant is retracted.
- The thermodynamic interpretation is asserted only on the honest Gibbs half-line `β > 1`, not by analytic continuation.
- No half-density or critical-line unitarity theorem is being promoted to an RH zero-location theorem.
- Scalar-box analytic closure is not being promoted to a Yang–Mills or gravity amplitude; honest gauge/gravity cut numerators remain a later layer.