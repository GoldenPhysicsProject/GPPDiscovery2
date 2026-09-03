# Epsilon duality spine for the split-signature googly program

## Result of the current investigation

A stronger internal route has emerged that does not use Sharma's twistor action as the construction.

Let V be a four-dimensional complex twistor vector space with a nonzero volume form epsilon in det(V*) = Λ^4 V*. The same epsilon has two standard descendants.

1. On Λ^2 V, wedge product gives a symmetric bilinear pairing

   B_epsilon(alpha,beta) = epsilon(alpha wedge beta).

   In Pluecker coordinates (01,02,03,12,13,23), its diagonal is twice the Klein quadratic form

   p01 p23 - p02 p13 + p03 p12.

   The null cone is the Klein quadric Gr(2,4) in P(Λ^2 V). Choosing the split real slice and metric gives the real Hodge complement already formalized in SplitSignatureHodgeGrassmannian.lean.

2. On P(V)=CP^3, contraction of epsilon with the Euler vector produces the standard projective holomorphic top form D^3 Z. It has homogeneous weight +4. Equivalently K_CP3 = O(-4). Therefore canonical/Serre duality sends a twistor line-bundle degree k to -k-4.

Under the standard Penrose helicity convention k=2h-2, this is exactly h -> -h.

Thus the following three facts are not independent numerical coincidences:

- the Grassmannian lives in the middle exterior power Λ^2 of a four-dimensional space;
- the Klein polarity/complement comes from the ambient alternating 4-form;
- the twistor canonical shift is -4, again from the same ambient rank/volume form.

For gravity, k=2 -> -6. For Yang-Mills, k=0 -> -4.

## What is actually proved versus conjectured

Standard geometry supports that one ambient epsilon determines both the Λ^2 wedge pairing and the projective weight-4 volume form. GPPVerify now formalizes the coordinate and weight consequences in AmbientFourDualitySpine.lean.

What is NOT yet proved is the strong googly identification that the induced Grassmannian complement, twistor canonical duality, and physical SD/ASD exchange are literally one functorial involution through the Penrose correspondence.

The precise missing theorem is an intertwining statement. Schematically, with D_Gr the epsilon-induced complement/polarity and D_Tw the canonical-dual transform,

    Penrose_- o D_Tw = D_Hodge o Penrose_+

or an equivalent correspondence-space formulation.

If this can be established without adding an independent bilinear identification V ~= V*, then the GPP googly mechanism would be intrinsic to the oriented four-dimensional twistor vector space. If an identification V ~= V* is required, that extra structure must be named explicitly (e.g. infinity twistor, metric, or real structure) rather than hidden.

## Important conceptual correction

A volume form canonically identifies Λ^2 V with (Λ^2 V)*, but it does NOT canonically identify V with V*. Therefore there is a canonical polarity on the Klein quadric, while a pointwise PT -> PT* identification still requires extra structure. This is exactly where the field-level integral/Fourier correspondence can enter without pretending that twistor points are canonically self-dual.

## New formalization

GPPVerify branch codex/orientation-mass-time-formalization:

- GppVerify/CelestialHolography/AmbientFourDualitySpine.lean
- commit ca3b0d5f48ca64a3a7e065e4730bd3eff2ff7b26

The module proves:

- ambient rank 4 -> projective dimension 3 and canonical degree -4;
- the polarized epsilon/Klein pairing;
- B_epsilon(p,p)=2 KleinQ(p);
- split Hodge star preserves the epsilon pairing;
- k -> -k-4 is involutive;
- graviton 2 <-> -6 and gauge 0 <-> -4;
- with k=n-2, the same reflection gives doubled-helicity n -> -n.

Do not call the analytic googly problem solved until the Penrose intertwiner is constructed/proved.
