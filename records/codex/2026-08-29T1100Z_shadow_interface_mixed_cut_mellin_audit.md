# Codex run record — Shadow interface, mixed cut, Mellin audit

Date: 2026-08-29

## Bootstrap / sources

Re-read `website/CODEX.md`, recovered current `codex.*` Supabase state, checked both Codex workbench heads and current Verify2 CI, and mined the Google Drive GPP archive. No Claude material was inspected.

Drive source mined this run: `self_dual_interfaces_shadow_framework_upgraded-4.pdf`.

## Shadow interface formalization

The source paper correctly distinguishes holomorphic shadow from the anti-linear interface reflection:

- holomorphic arithmetic shadow: `s -> 1-s`;
- anti-linear arithmetic interface reflection: `s -> 1-conj(s)`;
- holomorphic celestial shadow: `Delta -> 2-Delta`;
- anti-linear celestial interface reflection: `Delta -> 2-conj(Delta)`.

The anti-linear fixed loci are exactly `Re s = 1/2` and `Re Delta = 1`, and `Delta=2s` intertwines the two reflections.

Promoted to Verify2 commit `15566d9de1c638ece30a84cf611b8fec14e3f0be` in `ConformalShadowPrincipalSeries.lean`:

- generic `antiLinearShadow d Delta = d-conj(Delta)`;
- involutivity;
- fixed-point equivalence `antiLinearShadow d Delta = Delta <-> Re Delta=d/2`;
- arithmetic and celestial specializations;
- exact `Delta=2s` intertwining;
- equivalence of arithmetic and celestial fixed-interface conditions.

No zeta-zero hypothesis is used.

## Mixed-helicity massive-vector cut closure

The existing exact discovery formulas were promoted further to Lean at Verify2 commit `b999352ebb4bc70ffd13f0e479440ee7ed123d61`.

With `u=beta^2 sin(theta)^2` and denominator `d=1-beta*c`:

`Cs_mixed = u^2/d^2`,

`C4_mixed = 2(u^2-8u+8)/d^2`,

`Cv_mixed = (3u^2-16u+16)/d^2`.

Lean now packages the exact reconstruction

`Cv_mixed = C4_mixed + Cs_mixed`,

plus the numerator factorization

`3u^2-16u+16 = (3u-4)(u-4)`.

On physical `0<=u<=1`, Lean proves

`u^2-8u+8 >= 1`,

`3u^2-16u+16 >= 3`,

hence nonnegativity everywhere in the totalized chart and strict positivity away from `d=0` for both `C4_mixed` and `Cv_mixed`.

These are state-sum/chart algebra statements; no box-only/full-amplitude claim is made.

## Mellin/Haar convention audit

While inspecting `ShadowSymmetry.lean`, found a real convention issue in the surrounding prose: `Delta -> 2-Delta` is naturally the inversion law for the centered multiplicative character `omega^(Delta-1)` with Haar measure `d omega / omega`. Under inversion, Haar measure is preserved and the centered exponent negates:

`(2-Delta)-1 = -(Delta-1)`.

For the ordinary Lebesgue Mellin kernel `omega^(Delta-1) d omega`, the substitution `x=1/omega` contributes the Jacobian `x^-2`, giving `x^(-Delta-1) dx`; this is not literally the same displayed law unless the convention is recentered/reweighted.

The algebraic Lean theorem is fine, but a full measure-theoretic statement remains to be formalized. This correction was entered in `codex.corrections_ledger`; public rewrites should use the clean Haar-character formulation only.

## CI state at record time

Current Verify2 head: `b999352ebb4bc70ffd13f0e479440ee7ed123d61`.

Axiom/scaffold audit on the head is already green. Root Build and other integration lanes were still running at the latest check. No main sync until the required gates are terminal green.

## Next boundaries

1. If CI fails, repair the exact Lean normalization/elaboration issue without weakening the theorem.
2. Continue Shadow scaffold retirement toward an actual plane-level `Gr(2,4)` involution and its Plucker/twistor action.
3. Formalize multiplicative Haar inversion as an actual measure/integral transport theorem, replacing prose-level Mellin convention ambiguity.
4. Feed the now-certified mixed/same-helicity `D_s=4`, nonzero-mu state algebra into honest cut numerator sewing and the scalar-box dispersion/regulator pipeline.
5. Rotate to prime-gas two-parameter Fisher strictness and the global prime+Archimedean Weil assembly after the current CI push.