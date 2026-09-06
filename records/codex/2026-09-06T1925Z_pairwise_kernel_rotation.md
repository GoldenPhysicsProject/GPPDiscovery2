# Codex/GPT rotation — 2026-09-06 19:25Z

Scope: Codex/GPT work only. No Claude-owned branch, record, file, or context inspected.

## CI / certified state

- Verify2 free-energy head `7e59b4927c5ac1bb62706e91d54aedaa7e2ecd09` is now fully certified: cold changed-Lean #938 and full Build #2084 both passed.
- This certifies `F'(β)=S(β)/β²` and the nonnegative first-derivative consequence already added on the previous rotation.
- Audit of `ZetaGibbsFreeEnergyCurvature.lean` confirmed that the stronger second differential law was already present, so it was not duplicated: `F''(β)=-κ₂(β)/β-2S(β)/β³<0` on `β>1`.

## Spectral / chamber advance

Pushed Verify2 commit `fbe4b57faaaa46ffe1f670db967566514a51f8d3` extending `SpectralRhoContinuousStep.lean` with the exact pairwise alignment kernel

`(F_c(y)-F_c(x))(y²-x²) = 2/[c(2c+1)] (y²-x²)²`, `c>0`,

plus nonnegative and strict-positive consequences (strict when `x² ≠ y²`).

This is the algebraic sign kernel needed by the iid symmetrization formula for covariance. It is the clean bridge from the already-certified likelihood-ratio identity to analytic covariance positivity/radial stochastic ordering once the normalized continuous Gamma measure is instantiated.

Fresh CI for `fbe4b57...` is pending; no certification is claimed for this new theorem layer yet.

## Number thermodynamics

No redundant theorem was added. Existing formal source already proves the exact free-energy curvature law and strict concavity on `β>1`. The strongest countable two-parameter geometric endpoint remains `R(β,η)<1/2` for `η>0`.

## Celestial cut / YM / gravity / higher loops

`TreeLoopSewing.lean` was re-audited. The graph-theoretic all-loop count is genuinely formal: a `(4+2L)`-point cubic tree sewn in `L` disjoint pairs yields four external legs and cycle rank `L`. The analytic shadow-discontinuity-to-momentum-pair-closure identity remains an explicit local hypothesis in `ShadowPairSewing`; it is not proved by the topology theorem.

Scalar cut -> dispersion -> raised-box regulator remains closed at `J_ε(S,T) -> 1/6`.

For honest one-loop YM, the blocker remains the factor-preserving opposite crossed full-conic tree with the extra uncut denominators retained through topology subtraction. No YM master coefficient, gravity numerator, or higher-loop analytic coefficient is promoted.

## Principal series / completed zeta / Weil

`WeilPositivityCriterion.lean` was re-audited. It proves the finite-support equivalence between RH and PSD of the zero-paired Weil/Yakaboylu form, including actual closure of the nontrivial-zero set under `ρ -> 1-conj(ρ)`. It explicitly does not prove the missing analytic input: unconditional completed prime-plus-Archimedean explicit-formula/operator positivity. No RH promotion.

## Promotion state

PR #22 is open and draft, with head `fbe4b57...`; GitHub currently reports it mergeable but `mergeable_state=unstable`. Its own body requires exact-head full gates and reconciliation of branch divergence before merge. No destructive ref update or merge was attempted.

## Next frontier

1. Terminal cold/full CI for `fbe4b57...`; repair immediately if needed.
2. If green, formalize the analytic covariance symmetrization/normalized-Gamma instantiation rather than another algebraic restatement.
3. Spectral: arbitrary-real convolution semigroup and Gamma-density identification.
4. YM: explicit factor-preserving opposite crossed tree; gravity/higher-loop analytic cuts remain downstream.
5. RH: construct the completed prime-plus-Archimedean explicit-formula quadratic form without unknown-zero input and attack its positivity.
