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

for `β > 1` only. The underlying already-certified derivative inputs are `A'=-U` and `U'=-Var`. The two new files had failed their first CI compilation, so their proofs were simplified to isolate the coefficient algebra explicitly rather than rely on broad `convert/simp/ring` chains. The entropy cleanup is commit `56e80bdd7fe047c4cb717d6cf501a08c7c67f5c4`; the Legendre cleanup is commit `898089dd395ea9a21bb49fc6b04900dac329386c`.

At the time of this note, CI for the cleaned head was pending. Therefore these two new differential identities are mathematically derived but not yet claimed compiler-certified.

## Boundaries retained

- The scalar core must use the mixed-log structured majorant; the former independent-square majorant is retracted.
- The thermodynamic interpretation is asserted only on the honest Gibbs half-line `β > 1`, not by analytic continuation.
- No half-density or critical-line unitarity theorem is being promoted to an RH zero-location theorem.