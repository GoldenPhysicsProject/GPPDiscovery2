# Googly antiunitary orientation exchange — 2026-08-27

## Sources audited

- GPP Drive `twistor-googly-essay.txt` and the archived googly manuscript lineage.
- `GppVerify/CelestialHolography/HolographicChain.lean`.
- `GppVerify/CelestialHolography/GrassmannianGr24.lean`.
- `GppVerify/CelestialHolography/CelestialShadowHelicity.lean`.
- `GppVerify/CelestialHolography/DiscreteSymmetryHelicity.lean`.
- `GppVerify/CelestialHolography/TwistorGoogly.lean`.

## Correction to the old manuscript wording

For a massless particle, ordinary time reversal reverses both momentum and angular
momentum and therefore preserves helicity.  Parity reverses momentum while preserving
axial angular momentum, hence reverses helicity.  PT also reverses helicity.  Therefore
the celestial shadow law `J -> -J` cannot be identified with bare T on a nonzero-helicity
massless state.

The correct candidate is an antiunitary orientation-reversing exchange: antiunitarity
supplies complex conjugation, while orientation reversal exchanges the self-dual and
anti-self-dual Hodge sectors.

## New formal target promoted to Verify2

`GooglyAntiunitaryExchange.lean` defines an explicit anti-linear involution on the ordered
basis `(e12,e13,e14,e23,e24,e34)` of `wedge^2 C^4`:

- conjugate the first three components;
- conjugate and negate the last three components.

The file targets/proves:

1. involutivity;
2. coordinatewise Hermitian norm-square preservation;
3. anti-commutation with the explicit Hodge star,
   `star (Theta v) = - Theta (star v)`;
4. self-dual modes map to anti-self-dual modes;
5. anti-self-dual modes map back to self-dual modes.

Verify2 commits:

- theorem file: `6d4631a83d9a98811e77c3259e0637d79805a5c0`;
- explicit fast CI gate: `6b1b02402693aeab0ead0c5eb491588a00a62475`.

## Existing exact celestial side

`CelestialShadowHelicity.lean` already proves

`(Delta,J) -> (2-Delta,-J)`

under shadow, including `+2 <-> -2` for gravitons and `+1 -> -1` for gauge bosons.
On the principal series `Delta = 1 + i nu`, the dimension part becomes complex
conjugation.

This is now structurally aligned with the new anti-linear orientation-reversing Hodge
exchange, but the equality of the two operations has NOT yet been proved.

## Existing genuine Gr(2,4) content

`GrassmannianGr24.lean` models `Gr(2,4)` as actual two-dimensional complex subspaces of
`C^4`, with orthogonal complement a genuine involutive self-map.  `HolographicChain.lean`
proves the explicit Plucker relation and derives the SD/ASD quadratic balance from it.

## Honest remaining googly gap

`TwistorGoogly.lean` still marks these as genuine infrastructure gaps:

- Penrose correspondence;
- Penrose-Ward transform;
- SD and ASD sheaf/cohomology identifications;
- the induced cohomological googly map;
- identification of that geometric map with the antiunitary orientation/shadow exchange.

Thus the next rigorous bridge is not another helicity-label theorem.  It is to construct a
geometric map from the Gr(2,4)/twistor orientation involution to the SD/ASD cohomological
sectors and prove that its celestial boundary action is the already-formalized shadow
transformation.

## Broader implication under investigation

The same pattern is being compared with the RH fixed-point mechanism:
positive structure + involutive/antiunitary exchange + positivity of the paired form forces
spectral support onto the fixed locus.  This remains a connected research program, not yet a
proof of the missing Weil/explicit-formula positivity theorem.
