# 2026-09-01 — number-Gibbs CI repair, scalar DCT API audit, and gravity-source correction

## Verify2 CI diagnosis

Verify2 commit `10255ca96c497fecc8c5f5b5cad5a8ee83992b8c` attempted to make the confined two-parameter number-Gibbs Fisher theorem unconditional on the zeta half-plane `beta > 1`, `eta >= 0`. The changed-Lean smoke failed only in the new module `NumberGibbsTwoParameterZetaWedge.lean`; its rebuilt dependencies, including the finite Vandermonde/Fisher chain, countable moment limit, strict witness, zeta summability, and `NumberGibbsTwoParameterStrict`, compiled without source `sorry`.

The first real error was syntactic cast normalization in the identity

`exp (-beta * log(n+1)) = 1 / (n+1)^beta`.

Lean's target contained `((n+1 : Nat) : Real)` while `Real.rpow_def_of_pos` expected the normalized real expression `((n : Real)+1)`. The second real error was the `r=0` summability interface: `summable_gibbsWeight` proves summability of the bare weight, while the generic comparison theorem expects the syntactically expanded `weight * logEnergy^0`. Later heartbeat failures were downstream elaboration noise.

Verify2 commit `8042c5c14a271781c59e3942da9f3535aee72f0b` repairs these interfaces by normalizing `Nat.cast_add/Nat.cast_one` before the `rpow` rewrite and introducing explicit `hz0,...,hz4` summability witnesses (`hz0` and `hz1` closed by `simpa`). No mathematical statement was weakened and no source `sorry` was introduced. CI run `33537526804` was in progress at the time of this record.

The intended theorem remains:

- if `beta > 1` and `eta >= 0`, then the mass-aware infinite Fisher numerator of the two-observable number-Gibbs family is strictly positive;
- the proof is domination by the ordinary zeta-Gibbs moments plus the already formalized fixed three-state Vandermonde witness.

The stronger all-real-beta target for `eta > 0` remains the quadratic-log confinement comparison against a shifted `n^-2` tail.

## Scalar-box DCT interface

The pinned Mathlib API has exactly the interval theorem needed for the final regulator proof:

`intervalIntegral.tendsto_integral_filter_of_dominated_convergence` takes eventual AE strong measurability, an eventual AE norm bound on the unoriented interval, interval-integrability of the bound, and AE pointwise convergence, and returns convergence of the interval integrals.

This matches the existing raised-box coordinate system directly. `RaisedBoxConcreteMoment.lean` already supplies strict-interior pointwise convergence and the one-channel majorant

`Q^(-epsilon) <= 1 + (S*x1*x3)^(-delta)`

for `0 <= epsilon <= delta`, `0 < delta`, and positive Euclidean invariants. `RaisedBoxRealOuterIntegrability.lean` already supplies interval-integrability of the final outer kernel

`x^(-delta) * (1-x)^(2-delta)`

for `delta < 1`.

Therefore no further Beta/Gamma estimate is missing. The remaining Lean work is structural: package the null boundary faces as AE exceptional sets, establish the needed AE strong measurability for the parameterized inner integrands, apply the interval DCT successively in `x3`, `x2`, and `x1`, and identify the limiting nested integral with the already-proved simplex volume `1/6`.

## Gravity source correction

The uploaded ONON celestial-holography chapter asserts that pure Einstein one-loop triangle and bubble coefficients vanish because pure gravity can be obtained by truncating `N=8` supergravity and the `N=8` no-triangle property would persist. This implication is not valid as a construction rule. Supersymmetric loop cancellations depend on the full supermultiplet and do not automatically survive removal of the matter/superpartner states. The active Codex track must therefore not use this argument.

This correction is also consistent with known one-loop pure Einstein amplitudes containing nontrivial rational sectors; the `N=8` no-triangle hypothesis is a special supersymmetric statement. Hence the next gravity stage must use honest pure-Einstein or Yang-Mills tree sewing/state sums in the specified dimension/regulator scheme and determine box/triangle/bubble/rational contributions rather than imposing their absence from the manuscript.

## Next boundaries

1. Recheck `8042c5c...`; repair only any genuine remaining Lean interface failure.
2. Formalize all-real-`beta`, `eta>0` Gaussian-in-log summability by an eventual `n^-2` comparison.
3. On scalar amplitudes, attack the AE boundary + nested interval DCT theorem directly.
4. After scalar regulator closure, compute the honest fixed-loop `D_s=4`, `mu != 0` Yang-Mills state sum before any gravity double-copy or no-triangle simplification.
5. Preserve the exact Mehler-Fock/Wiener-Hopf/chamber results, while keeping their local positivity logically separate from global Weil positivity.
