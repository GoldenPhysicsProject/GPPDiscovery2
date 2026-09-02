# Diagonal charge-orientation googly test

## New structural hit

The user's proposed transformation is not orientation reversal alone. It is a diagonal reversal of a representation/charge character together with orientation. At the twistor line-bundle level, this has a striking exact analogue.

On PT ≃ CP^3, K_PT = O(-4). A field of line-bundle degree k has canonical/Serre dual degree

    k ↦ -k - 4.

This decomposes algebraically as

    representation dualization: k ↦ -k,
    canonical/top-form shift:    k ↦ k - 4,

so their combination is k ↦ -k - 4.

For gravity,

    O(2) ↔ O(-6),

which is exactly the standard pair of twistor graviton fields h and g/B/tilde h.
For Yang-Mills,

    O(0) ↔ O(-4).

This is much stronger than saying the two helicities happen to have complementary weights: the opposite-helicity field type is precisely the canonical dual of the deformation field type.

## Relation to known twistor actions

Modern twistor gravity writes the self-dual Poisson-BF action schematically as

    S[g,h] = ∫ g ∧ (∂̄h + 1/2{h,h}) ∧ D^3Z,

with

    h ∈ Ω^{0,1}(PT,O(2)),
    g ∈ Ω^{0,1}(PT,O(-6)),
    D^3Z ∈ Ω^{3,0}(PT,O(4)).

Thus the weights close exactly:

    (-6) + (2) + (4) = 0.

The `g` field is therefore the natural dual/cotangent-type field that pairs with the integrability curvature of `h`. This makes it misleading to call it an arbitrary unrelated second geometric sector.

However, bundle-level canonical duality does NOT by itself determine a section g from a section h. The section spaces are dual representations but still independent off shell unless extra structure supplies a map

    g = G[h].

Potential sources of such extra structure:

1. equations of motion of full GR,
2. a real/split-signature pairing,
3. a symplectic/Poisson pairing on twistor space,
4. orientation/charge lift before quotient,
5. boundary conditions/polarization.

## Refined hypothesis

The user's diagonal idea can now be stated precisely:

There exists an enlarged oriented twistor datum H whose two standard chiral fields are projections

    h = Π_+ H,
    g = Π_- H,

and a diagonal involution D that acts simultaneously by representation dualization and orientation reversal such that

    Π_- D(H) = G(Π_+ H)

with bundle degree forced by

    O(2) ↦ K_PT ⊗ O(2)^∨ = O(-6).

This would mean that the apparent independent opposite-helicity field is the canonical conjugate lift of the same underlying oriented object, not a second spacetime.

## Hard falsifier

Degree matching is now passed exactly. The next nontrivial test is section-level and nonlinear:

- derive the full twistor equations of motion for h and g/B;
- ask whether they imply an on-shell reconstruction map g = G[h] modulo gauge;
- count functional degrees of freedom before and after quotient;
- check whether G is compatible with the split-signature half-Fourier/light-transform map and with orientation reversal of the Hodge decomposition.

If generic solutions admit independent variations δg at fixed h even after all equations/gauge constraints, the diagonal-single-object hypothesis fails.
If instead g is fixed (possibly nonlocally) by h plus orientation/boundary data, the hypothesis gains real force.

## Important correction

Do not identify the canonical -4 shift with physical Wigner time reversal. The exact mathematics is line-bundle dualization plus the canonical bundle of CP^3. The physical interpretation as charge-orientation diagonal reversal is a hypothesis to be derived, not assumed.
