# Penrose ray quotient: tautological spinor-line twist and sky descent

Date: 2026-09-07
Status: exact finite GPP algebra + literature-backed geometric synthesis; LeBrun identification still open

## Recovery / correction context

The full Penrose/Twistor Newsletter review had already been completed and persisted.  The strongest previous exact result was

`T_gamma^aligned / <Z_gamma>`

with induced two-dimensional transport

`x'=-i p`, `p'=-i P(k,k)x`, hence `x''+P(k,k)x=0`.

That result remains correct.  What required correction was the bundle-level interpretation of the raw coordinate pair `(x,p)`.

## 1. Gauge covariance of the quotient

Under the null-spinor little-group change

`lambda -> a lambda`, `lambdatilde -> a^{-1} lambdatilde`, `a != 0`,

the physical null direction `k=lambda lambdatilde` and therefore `U=P(k,k)` are unchanged.

Since `omega=x lambda` and `p=lambdatilde.pi`, the quotient coordinates transform as

`(x,p) -> a^{-1}(x,p)`.

The induced Einstein-ray generator is linear and commutes with this common rescaling.

Changes of the complementary adapted spinors alter only the discarded coordinates on the ray-aligned subspace, so the quotient projection is unchanged.

Formalized in:

`GppVerify/CelestialHolography/PenroseLocalTwistorRayGaugeCovariance.lean`

commit `7d65b4ffd7fbd2fc9a821b6ae450af464506e58c`.

Thus the raywise projective system is genuinely attached to the ray and not to one chosen adapted spin frame.

## 2. Important correction: raw x is not an ordinary scalar Einstein scale

A genuine conformal Einstein scale is neutral under the null-spinor little group.  The raw coefficient `x`, however, has weight `a^{-1}`.

This is not a problem for the Sturm/projective equation, because all solutions in the same frame acquire the same common scale and therefore projective ratios are unchanged.  It *is* a problem for the earlier overly strong wording

`E_sky = T_gamma^aligned/<Z_gamma>`

as an untwisted vector-bundle equality.

The invariant finite object is

`lambda tensor (x,p)`

because

`(a lambda) tensor (a^{-1}x,a^{-1}p) = lambda tensor (x,p)`.

Formalized in:

`GppVerify/CelestialHolography/PenroseQuotientTautologicalTwist.lean`

commit `a51465cf4a24fcc44b50ae17d244f8e8e7cad042`.

A concrete Lean theorem also proves that raw `x` changes under a nontrivial little-group rescaling, so this is an actual obstruction, not terminology.

## 3. Correct bundle-level target

The correct comparison is therefore projective/twisted:

`P(E_sky,gamma) = P(Q_Penrose,gamma)`

where

`Q_Penrose,gamma := T_gamma^aligned/<Z_gamma>`.

At vector-bundle level the candidate is schematically

`E_sky ?= L_ray^* tensor Q_Penrose`

where `L_ray` is the tautological unprimed null-spinor line (exact dual/convention to be fixed globally).

This is strongly compatible with the historical Penrose clue that googly data was naturally projective and required an additional scale prescription.  The old “which scale is the correct googly scale?” issue may be precisely the failure to separate the invariant projective system from the tautological line twist.

The opposite/dual chiral construction should carry the analogous primed tautological line.  This suggests an ambidextrous neutral object may be obtainable from either chiral quotient after cancelling its corresponding line factor.  This remains a conjectural bundle identification, not a proved equality.

## 4. Sky/incidence descent isolated exactly

A separate new module formalizes the bare gluing logic:

`GppVerify/CelestialHolography/RayFieldSkyDescent.lean`

commit `13769196755fdd5654c3a5eb9702ac4a0958e81d`.

For a surjective incidence map `pointOf : Sample -> Point`, a raywise field `f : Sample -> K` descends to a unique spacetime field iff it is constant on every fibre of `pointOf`, i.e. iff all ray samples representing the same spacetime point agree.

This is the exact set-theoretic content of “sky compatibility / transverse gluing”.

The null-surface formulation gives the concrete differential version: the raywise second-order Einstein-bundle equation is not enough; metricity equations in the celestial directions are required so that one metric `g^{ab}(x)` descends and becomes independent of the direction labels.  The old 1994 NSF paper explicitly says the null-contracted Einstein equation is true for every celestial direction and becomes equivalent to the full Einstein equations only after the metricity conditions are added.  Modern NSF formulations state the same geometry in bundle/Pfaffian language.

## 5. LeBrun correspondence-space comparison

Modern presentations of LeBrun's Einstein bundle state:

- `E -> G` is a rank-two holomorphic bundle over complex null-geodesic/ambitwistor space;
- nonvanishing holomorphic sections correspond to Einstein metrics in the conformal class;
- historically the bundle is defined most naturally by its inverse image on correspondence space;
- in a right-flat presentation, a conformally invariant second-order operator `Delta` acts on a conformal density line and its fibrewise kernel defines `E`;
- the operator contains two powers of the projective spinor coordinate, so homogeneity/line-bundle weights are essential rather than cosmetic.

This makes the new tautological-twist correction especially relevant.  The next exact comparison must track **both** conformal density weight and null-spinor homogeneity.

## 6. Current hard theorem

The corrected frontier is:

1. identify the precise tautological line factor and its holomorphic transition functions over ray/ambitwistor space;
2. construct the opposite/dual chiral quotient and show both untwist to the same neutral projective rank-two system;
3. prove NSF metricity / sky compatibility gives the transverse descent of those raywise systems;
4. compare the resulting holomorphic rank-two bundle with LeBrun's `E` and its correspondence-space kernel operator.

The key conceptual improvement is that Penrose local-twistor transport, modern sky projective geometry, and NSF now agree **projectively along each ray**, while the remaining mismatch has been localized to a concrete line-bundle weight plus transverse gluing problem.

Updated formal spine commit: `4ab2c1b876513193e3c57776b187a897eaf946bf`.

No CI certification claimed.
