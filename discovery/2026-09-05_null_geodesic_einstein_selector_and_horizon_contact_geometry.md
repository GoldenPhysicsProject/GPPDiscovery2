# Null-geodesic Einstein selector and horizon contact geometry

Date: 2026-09-05
Status: exact split-signature algebra + standard external differential/contact geometry; LeBrun-bundle identification still incomplete.

## 1. Almost-Einstein equation as null-geodesic transport

Let

`T_ab = nabla_a nabla_b sigma + P_ab sigma`,

where `P_ab` is the Schouten tensor.  The almost-Einstein equation is

`(T_ab)_0 = 0`,

i.e. `T_ab` is pure trace.

For an affinely parametrized null geodesic with tangent `k^a`, contraction removes the pure trace and gives

`sigma'' + P(k,k) sigma = 0`.

The new GPPVerify module `NullConeEinsteinSelector.lean` proves the algebraic converse in split signature.  Identify a tangent vector with

`X=[[a,b],[c,d]] in M_2(R)`

and the conformal quadratic form with `det X = ad-bc`.  If any real quadratic form `Q_T(X)` vanishes on every rank-one/null matrix, then

`Q_T(X)=mu det X`.

Thus, pointwise in split signature,

`T(k,k)=0 for every null k  <=>  T is pure trace`.

Consequently the almost-Einstein PDE is equivalent, at the level of its symmetric 2-tensor condition, to the family of scalar second-order equations along all null directions.  Differential-geometrically, along affine null geodesics these are the ODEs above.

## 2. Relation to the historical Einstein bundle

LeBrun's ambitwistor Einstein bundle is a rank-two holomorphic vector bundle over the space of complex null geodesics; nonvanishing holomorphic sections correspond to Einstein metrics in the conformal class.  Toby Bailey's 1990 paper *Some geometry associated with the Einstein bundle* explicitly studies null-geodesic geometry toward an intrinsic characterization of this bundle.

Independent null-surface formulations of the Einstein equations call a linear second-order ODE for the conformal factor along the null parameter the "Einstein bundle equation".  This is strong evidence that the two-dimensional local solution space of

`sigma'' + P(k,k) sigma = 0`

is the correspondence-space realization of the rank-two Einstein-bundle fibre.

However, the exact bundle isomorphism (including conformal weight, holomorphic structure, connection/monodromy, and compatibility across intersecting null geodesics) has not yet been derived.  Do NOT state that identification as proved.

## 3. Null hypersurfaces as Legendrian wavefront data

For a smooth light-ray space `N` of a four-dimensional spacetime, `N` is five-dimensional and carries the canonical contact structure.  Standard results of Low, Natario--Tod, Chernov and others imply:

- skies of spacetime points are two-dimensional Legendrian submanifolds;
- a Legendrian map on a spacelike slice generates a mapped null hypersurface;
- conversely, intersecting a mapped null hypersurface with a spacelike hypersurface gives a Legendrian map;
- singularities/caustics are naturally treated as Legendrian wavefront singularities rather than requiring an embedded smooth surface.

Therefore every smooth portion of a black-hole event horizon determines a two-dimensional Legendrian family of its null generators in the physical light-ray/contact space.  At crease/nondifferentiable sets the correct object is a Legendrian map/wavefront.

Event horizons are globally achronal, null-geodesically ruled topological hypersurfaces and need not be differentiable everywhere.

## 4. Precise relationship to future null infinity

Do not identify `H+` with `I+`.

`H+ = boundary J^-(I+)`

is an interior causal boundary in the physical spacetime.  `I+` is attached in the conformal completion and is a smooth null hypersurface of the unphysical metric in the standard asymptotically-flat vacuum setting.  Physical escaping null rays end at `I+`; the intrinsic null generators lying along `I+` belong to the conformal boundary itself.

Hence there are two useful contact arenas:

1. In the physical light-ray space, the horizon generators form a Legendrian ray family; `I+` acts as an endpoint boundary condition for escaping physical rays.
2. In a sufficiently regular conformal completion, both the image of the horizon and `I+` are null hypersurfaces of the unphysical conformal geometry, so each has its own null-generator/Legendrian wavefront data in the completion's light-ray geometry.

The conformal invariance of unparametrized null geodesics/contact light-ray geometry connects these descriptions in the interior, but the generators of `I+` should not be confused with physical rays that merely terminate there.

## 5. Rejected stronger claim

A tempting statement was that the horizon Legendrian `L_H` is simply the boundary in light-ray space between rays reaching `I+` and rays not reaching it.  This is not valid in general.

The event horizon is the boundary in **spacetime starting events** of the causal past of `I+`.  Boundaries between escaping and infalling *directions* in a celestial sphere can instead contain trapped/photon-region null geodesics (as explicit Kerr analyses show).  Thus contact geometry captures the null wavefront/congruence, while causal order relative to `I+` supplies the global event-horizon condition.

## 6. Current synthesis

The emerging nonlinear architecture is:

`ambitwistor/light-ray contact geometry` -> full conformal null structure,

plus

`rank-2 null-geodesic Einstein-scale transport` -> candidate intrinsic Einstein selector,

plus

`causal relation to I+` -> distinguishes event horizons from generic null wavefronts.

This is a more precise realization of the phrase "same arena, different sections": black-hole horizons and null infinity are not the same boundary, but null hypersurfaces are represented by Legendrian/wavefront data in the common contact geometry of light rays (with the conformal-completion caveat for `I+`).

GPPVerify relevant new commit: `72701d89297d5b3bd69139eddca8a0bcbaca6346` (`NullConeEinsteinSelector.lean`).  Current modules are not CI-certified.
