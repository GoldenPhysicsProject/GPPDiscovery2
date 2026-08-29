# Codex/GPT all-fronts continuation — 2026-08-29 07:35Z

Track: Codex/GPT only. Branches: GPPVerify2 `codex/lean-workbench`, GPPDiscovery2 `codex/discovery-workbench`.

## CI diagnosis and repairs

The previous verification head `8fe153105cd5386c9d5a60ec30865bdd26b1de6d` had four green specialized gates (axiom/scaffold audit, causal-diamond Fisher, arithmetic OS, Gibbs thermodynamics) and four red gates (finite-core closures, sech convolution endpoints, full construction, global Build).

The failures were localized rather than mathematical regressions across the active fronts:

1. `UniversalNotFidelity.lean`: global Build stopped because simplification left `Matrix.vecMul` expressions unevaluated in the 2x2 Pauli identity. Repair commit `0391d5edae1d651b528e1ef215f2a90f790cc95a` explicitly unfolds `Matrix.vecMul` and `dotProduct` before ring normalization.
2. `WienerHopfGammaChamberPositiveFactor.lean`: the chamber monotonicity proof mixed the named `rhoStepFactor` inequality with the expanded recurrence coefficient, so `nlinarith` could not connect them. Commit `ee2bb5db610dd70cb0552956be24beaea3d303b7` adds the exact named recurrence
   `rhoGamma (k+1) x = (rhoStepFactor k x : C) * rhoGamma k x`,
   and commit `e9ea8726138fcff80505c201ac9311eebb493193` rewrites the strict increase/decrease proofs through that recurrence.
3. `LocalEulerShadowColligation.lean`: the unit-circle Blaschke norm proof failed only because the real-coordinate norm equality appeared in mixed product/power normal forms. Commit `199a05a8cda1e1e7cbdc60524117f930c770cd65` normalizes the coordinate algebra with `ring_nf` before `nlinarith`.

These commits are awaiting CI at the time of this record; they are repairs, not yet certified green.

## Exact mathematics retained

### Gamma / Wiener-Hopff chamber recurrence

With
`rhoStepFactor k lam = 2 (((k+1)^2 + lam^2))/((k+1)(2k+3))`,
we now package the exact complex recurrence as

`rhoGamma (k+1) lam = rhoStepFactor k lam * rhoGamma k lam`.

Combined with strict positivity of `Re rhoGamma k lam`, this gives the intended threshold logic:
- `k+1 < 2 lam^2` implies strict chamber growth;
- `2 lam^2 < k+1` implies strict chamber decay.

No arithmetic Weil identification is asserted by this Archimedean result.

### Local Euler-shadow colligation

The target remains exact: for real `a`, if `|z|^2=1` and `1-a z != 0`, then

`normSq ((z-a)/(1-a z)) = 1`.

The repair changes only normalization of the elementary real-coordinate identity; no new hypothesis or axiom is introduced.

### Prime-gas strict Hankel geometry

Inspection confirms the current branch already contains a stronger result than the older three-point Fisher witness target. `PrimeHankelAllOrderStrict.lean` proves, for every `beta>1` and every nonzero real polynomial `p`,

`0 < sum'_n fisherWeight beta n * (p(log n))^2`,

using the positive support `2,4,8,...`. Thus the actual arithmetic Fisher measure has an all-order strictly positive polynomial Gram form. Future two-parameter Fisher work should specialize this stronger theorem rather than rebuild strictness from a three-point truncation.

## Frontiers

1. Amplitudes: finish the honest double massive-projector MHV sewing, subtract the scalar state, then propagate the D-dimensional numerator to gravity/double copy and generalized cuts.
2. Principal-series/RH: combine finite-prime positive-type / von-Mangoldt cosine identities with the Archimedean Gamma/Wiener-Hopf factor in the correctly signed global Weil quadratic form. This remains the decisive missing global identification; RH is not claimed.
3. Thermodynamics: package the all-order strict Hankel theorem into explicit strict positive-definiteness/determinant statements for the two-parameter `(log n,(log n)^2)` Fisher metric.
4. Spectral: after CI certifies the named recurrence repair, extend the Gamma chamber result toward exact convolution-power/chamber composition rather than only one-step monotonicity.
