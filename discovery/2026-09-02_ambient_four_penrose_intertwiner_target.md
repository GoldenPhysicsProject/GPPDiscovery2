# Ambient-four Penrose intertwiner target

Date: 2026-09-02

## Purpose

Continue the GPP googly attack from Daniel's own geometry rather than using Sharma's twistor action as the construction. Sharma remains a benchmark/falsifier only.

## Current geometric spine

Let the ambient twistor vector space be an oriented four-dimensional complex vector space `V` with volume form `epsilon`.

The same ambient 4-form has two descendants:

1. On `Λ² V`, wedge followed by `epsilon` yields the symmetric middle-degree pairing. In Plücker coordinates its diagonal is twice the Klein quadratic form. This controls the polarity/complement operation on `Gr(2,4)`.
2. On `P(V)=CP^3`, contraction of `epsilon` with the Euler vector gives the projective top form of homogeneous weight `+4`, hence `K_CP3 = O(-4)`. Canonical duality therefore sends `O(k)` to `O(-k-4)`, which under `k=2h-2` is exactly `h -> -h`.

Thus the Grassmannian polarity and the twistor helicity weight reflection are not unrelated arithmetic coincidences: both descend from the same oriented ambient rank-four exterior algebra.

## Important obstruction

A volume form canonically identifies the middle exterior power with its dual,

`Λ² V ≅ (Λ² V)*`,

but it does not canonically identify `V` with `V*`. Therefore the googly transform should not be sought as a pointwise map `PT -> PT*` from orientation alone. The natural target is a field-level / Penrose / correspondence intertwiner.

## Exact theorem target

Introduce a lifted field space `Lift` with an involution `D`, plus and minus projections, and an orientation reversal `R` on bulk fields. The desired theorem is

`P_- (Π_- (D x)) = R (P_+ (Π_+ x))`.

If physical observables additionally satisfy

`O(D x) = O(x)`,

then the two points in the `D` orbit are two oriented/conjugate representatives of one operational class. The opposite chirality is then a second projection of the same lifted geometry, rather than a separately manufactured field.

Applying the same relation to `D x` and using `D²=1` gives

`P_- (Π_- x) = R (P_+ (Π_+ (D x)))`.

If also `R²=1`, then

`P_+ (Π_+ x) = R (P_- (Π_- (D x)))`.

These are exact categorical consequences. The open hard theorem is to construct the actual analytic field-level `D` induced by the ambient `epsilon` geometry and prove that the Penrose transforms intertwine it with spacetime orientation reversal.

## Formalization

Created on `GPPVerify:codex/orientation-mass-time-formalization`:

`GppVerify/CelestialHolography/AmbientFourPenroseIntertwiner.lean`

The file deliberately makes the analytic intertwining relation a structure hypothesis and proves only the consequences. This avoids disguising the open Penrose theorem as a Lean proof.

## Interpretation relative to Daniel's diagonal hypothesis

Daniel's proposed diagonal reversal is structurally represented by `D`: both conjugate/internal sign and orientation sign are reversed upstairs while observables descend to the quotient orbit. This is stronger than orientation reversal alone and is not refuted by the existing orientation-only no-go.

The next mathematical task is to replace the abstract `D` hypothesis with an explicit transform built from the ambient rank-four exterior algebra and the split-signature Penrose/X-ray correspondence.
