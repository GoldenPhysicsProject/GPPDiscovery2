# Klein–Clifford / tractor / ambitwistor synthesis

Date: 2026-09-05
Status: mixed — internal exact algebra + external geometric theorems + GPP synthesis

## Executive result

The earlier attempt to construct a canonical pointwise `V* -> V` polarity was targeting the wrong object. In split four-dimensional conformal geometry,

- `Spin(3,3) ≅ SL(4,R)`;
- the six-dimensional vector representation is `Λ²V` with the epsilon/Klein quadratic form;
- the two four-dimensional half-spinor representations are `V` and `V*`.

A Klein bivector `p ∈ Λ²V` therefore acts canonically between the two twistor chiralities. The GPPVerify coordinate calculation now proves

`cMinus(p) ∘ cPlus(p) = cPlus(p) ∘ cMinus(p) = -Q_Klein(p) id`.

For a spacetime point `p ∈ Gr(2,4)`, `Q_Klein(p)=0`, so this is a nilpotent incidence operator. Its kernels are exactly the twistor line `W` and the annihilator dual-twistor line `W°`.

This gives the metric-free support chain

`Fourier support = annihilator incidence = epsilon-dual Plücker plane = chiral Clifford kernel`.

No ambient symmetric metric on twistor `V` is required.

## Cosmological infinity-twistor family

Define in the current Plücker coordinates

`I_Λ = (Λ,0,0,0,0,1)`.

Then exactly

`Q_Klein(I_Λ)=Λ`,

and hence

`cMinus(I_Λ)cPlus(I_Λ)=cPlus(I_Λ)cMinus(I_Λ)=-Λ id`.

For `Λ ≠ 0`, the two chiral maps are invertible with inverse `(-1/Λ)` times the opposite Clifford map. For `Λ=0`, `I_0` is the standard flat infinity point and the isomorphism degenerates to the previously proved exact two-periodic complex.

This reproduces the standard twistor normalization `I_{AC} I^{BC}=Λ δ_A^B` at the level of the GPP finite-dimensional algebra.

## Curved interpretation from standard conformal geometry

External theorem/input:

In four-dimensional spin conformal geometry the complexified standard tractor bundle is naturally isomorphic to the second exterior power of the local-twistor bundle. Under this identification a parallel scale tractor is the infinity twistor. A nonzero parallel standard tractor is equivalent to an almost-Einstein scale; on the nonzero-scale region the corresponding metric is Einstein.

Thus the six-dimensional Klein object formalized above is the same representation that carries the curved conformal-Einstein selector.

Modern form of the selector:

`(∇_a∇_b σ + P_ab σ)_0 = 0`

is equivalent to a parallel standard tractor `I=Dσ`; where `σ≠0`, `g_E=σ^{-2}g` is Einstein. The tractor norm fixes the Einstein scalar-curvature/cosmological parameter up to convention.

This provides a cleaner modern interpretation of the old ambitwistor `Einstein bundle` obstruction: ambitwistor data reconstruct the conformal class, while a parallel tractor/infinity-twistor datum selects an Einstein scale.

## Ambitwistor reformulation of the nonlinear googly problem

External classical theorem/input (LeBrun; Baston–Mason; later curved refinement):

Projective ambitwistor space — the contact space of complex null geodesics, flat model `Z·W=0` in `PT × PT*` — determines the local conformal spacetime. Contact-preserving deformations correspond to conformal deformations. Formal-neighbourhood extension conditions detect Bach-flatness and, under algebraic-generality hypotheses, conformally Einstein geometry; LeBrun's 1991 curved theorem uses vanishing Bach and Eastwood–Dighton tensors.

Consequently the nonlinear target should not be a deterministic map from one chiral twistor space to the other. Generic gravity needs both chiral sectors. The natural state space is ambidextrous incidence/ambitwistor data, with ordinary twistor and dual twistor as two projections.

The sharpened GPP target is therefore:

1. reconstruct/encode the full conformal structure on projective ambitwistor space;
2. impose the Einstein selector as a parallel tractor/infinity-twistor condition (or an equivalent intrinsic ambitwistor formal-neighbourhood condition);
3. identify the two chiral projections with the split half-Fourier/light-transform sectors;
4. identify the physical parity/orientation involution as exchange of the two chiral projections, distinct from full celestial shadow.

## What is proved internally

Current focused GPPVerify branch contains exact Lean algebra for:

- `KleinSpinorIncidence.lean` — Clifford square and exact incidence kernels;
- `EpsilonAnnihilatorDuality.lean` — epsilon middle-degree dual equals annihilator plane;
- `FourierEpsilonCliffordSupport.lean` — Fourier support iff Clifford kernel;
- `KleinNullInfinityBoundary.lean` — flat null infinity as tangent Klein hyperplane section;
- `FlatInfinityChiralComplex.lean` — exact flat-infinity two-periodic complex;
- `FlatInfinityCelestialFactorization.lean` — two celestial spinor factors and null momentum;
- `EinsteinInfinityTwistorFamily.lean` — `Q(I_Λ)=Λ`, nonzero-Λ inverse, flat rank drop.

Latest integration commit at time of this note: `6958d067d308ba859dd2a5493a9b2d4b05bf9c15`.

## What remains open

- The analytic homogeneous/projective Fourier–Penrose intertwiner is not formalized in Lean.
- The half-Fourier/light-transform analytic square is external, not Lean-certified.
- The full nonlinear ambitwistor-to-Einstein construction is not formalized.
- An intrinsic `PA`-side description of the parallel tractor/infinity-twistor selector should be sought rather than silently reconstructing spacetime first.
- The exact parity/orientation action on curved ambitwistor/contact + Einstein data must still be derived.
- No claim is made that a black-hole event horizon equals null infinity. Their commonality is null/characteristic rank-drop geometry, not global identity.
