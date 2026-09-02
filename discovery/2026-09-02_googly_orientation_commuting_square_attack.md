# Googly attack: orientation-Hodge exchange and the exact remaining twistor theorem

## Status

The old slogan `googly = shadow = T` is not a proof. The current canonical `TwistorGoogly.lean` still contains open stubs for the actual Penrose/cohomology/googly statements.

A cleaner route is now isolated.

## 1. Exact bulk theorem

On complexified Lorentzian two-forms, the Hodge operator has eigenspaces

- SD: `*F = +i F`
- ASD: `*F = -i F`.

Orientation reversal changes the Hodge operator by

`*_{-o} = -*_o`.

Therefore the same field satisfies

`*_{-o} F = -i F`

whenever

`*_o F = +i F`,

and conversely. Thus spacetime orientation reversal exchanges SD and ASD exactly. This is the mathematically secure bulk operation sought by the googly problem.

This algebra is formalized in `GPPVerify/GppVerify/CelestialHolography/OrientationGooglyCore.lean` on branch `codex/orientation-mass-time-formalization`.

## 2. Exact reduction of the linearized googly problem

Let

- `Tw` = twistor data space,
- `Bulk` = complexified curvature space,
- `P_- : Tw -> Bulk` = Penrose transform into one helicity sector,
- `P_+ : Tw -> Bulk` = transform into the opposite helicity sector,
- `R : Bulk -> Bulk` = orientation reversal,
- `G : Tw -> Tw` = candidate googly map.

The decisive square is

```
Tw  --G-->  Tw
 |           |
P_-         P_+
 |           |
 v           v
Bulk --R--> Bulk
```

with theorem target

`P_+(G z) = R(P_-(z))`.

Once this commutation is proved, SD/ASD exchange follows automatically from the bulk orientation theorem. It is no longer an independent googly assumption.

If in addition

`R^2 = id`

and a common Penrose transform is injective on the relevant quotient/cohomology class, then

`G^2 = id`

follows. This gives a precise closure criterion.

## 3. Celestial boundary check

Ordinary celestial shadow acts on labels by

`(Delta,J) -> (2-Delta,-J)`.

This is an exact involution and flips the helicity/spin label. It does not by itself act on internal charge.

Thus the boundary data demanded by the bulk orientation exchange are at least label-compatible:

orientation reversal: SD <-> ASD
celestial shadow: J <-> -J.

Compatibility is necessary, not sufficient. The missing theorem is the actual Penrose/shadow intertwiner with normalization and real-structure control.

## 4. What would count as a genuine linearized solution

Need construct `G` on the correct twistor cohomology/deformation space and prove all of:

1. `G` is well-defined modulo twistor gauge/cohomology equivalence.
2. `P_+ o G = R o P_-` with exact normalizations.
3. `G^2 = id` modulo the same equivalence/reality structure.
4. On momentum/celestial representatives, `G` sends helicity `h` to `-h` and matches `(Delta,J)->(2-Delta,-J)` after the correct Mellin/shadow normalization.
5. MHV and anti-MHV representatives are exchanged with correct little-group weights and phases.

This would solve the linearized googly exchange problem.

## 5. What is still needed for the nonlinear googly problem

The nonlinear problem requires more. The candidate `G` must extend from linear cohomology/classes to nonlinear twistor deformations / Ward data and preserve the integrability equations corresponding to the full field equations. For gravity this means compatibility with the nonlinear graviton construction; for Yang-Mills, with the nonlinear Ward bundle data.

A merely linear SD/ASD map is not a full nonlinear googly solution.

## 6. Main research direction

The strongest candidate is to derive `G` from the same complementary-plane / orientation geometry already appearing on `Gr(2,4)`, rather than introduce an unrelated dual twistor space by hand.

Concrete target:

- represent a spacetime point/alpha-plane incidence as a 2-plane in `C^4`;
- apply the canonical complementary-plane/orientation map;
- compute the induced incidence relation on the dual twistor variables;
- compare it with the standard beta-plane / dual-twistor incidence relation;
- prove the Penrose transform of the induced class is exactly the orientation-reversed curvature.

If this succeeds, the googly map is induced by one geometry rather than postulated as a second copy.

## 7. Connection to the flagship orientation program

This route is structurally compatible with the mass/time work but does not assume identity with it. Both problems are asking whether apparently doubled physical sectors are two oriented lifts of one underlying geometric object.

For googly, that statement is now testable by the commuting square above.
