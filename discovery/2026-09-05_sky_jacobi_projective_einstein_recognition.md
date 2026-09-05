# Sky–Jacobi projective recognition of Einstein geometry

Date: 2026-09-05
Status: exact finite algebra + externally established sky/Jacobi geometry; proposed identification with LeBrun's Einstein bundle remains a targeted conjecture

## 1. Contact space alone is not the full intrinsic datum

For a strongly causal sky-separating spacetime, the light-ray space `N` carries a canonical contact distribution `H`, but modern light-ray reconstruction results emphasize that the bare contact manifold is not sufficient by itself to recover the conformal spacetime.  The distinguished family of skies

`Sigma = { S(x) subset N : x in M }`

is essential.

The correct real intrinsic arena for the present programme is therefore

`(N, H, Sigma)`

rather than bare `(N,H)`.

## 2. A null geodesic carries a sky Jacobi curve

Fix a light ray `gamma in N`.  For each point `x=gamma(s)` on the ray, its sky `S(x)` is Legendrian and contains the same point `gamma` of light-ray space.  Hence

`L_s := T_gamma S(gamma(s)) subset H_gamma`.

Bautista–Ibort–Lafuente's 2025 Jacobi-curve paper states explicitly that

`Gamma(s) = T_gamma(S(gamma(s)))`

is a Jacobi curve in the Lagrangian Grassmannian of the contact hyperplane `H_gamma`.

New finite Lean model:

`GppVerify/CelestialHolography/FlatSkyJacobiCurve.lean`

commit `ab65cec2a1f9c72c83d9f08e15432450d4905b5c`.

In flat transverse screen coordinates a Jacobi field is `J(s)=a+s b`.  The sky tangent at `s` is exactly

`L_s = {(-s v,v)}`,

and the module proves:

- `J(s)=0` iff its initial-data state lies in `L_s`;
- each `L_s` is isotropic for the Wronskian symplectic form;
- the screen map `v -> (-s v,v)` is injective;
- distinct affine parameters give distinct parametrized sky planes;
- flat Jacobi transport preserves the symplectic form and transports the sky curve.

## 3. The sky curve carries a canonical projective parameter class

The 2022 sky-invariant paper defines the trace `Ric_gamma` of its conformal Jacobi curvature.  A parameter is called projective precisely when

`Ric_gamma = 0`.

All projective parameters on the same ray differ by a Möbius transformation.

The paper uses a Schwarzian convention equal to one-half the standard Schwarzian.  In four dimensions its equation gives, in standard Schwarzian notation,

`{tau,s}_std = - Ric_gamma(s)`.

For an affine null geodesic, `Ric_gamma` is the trace of the transverse optical tidal operator `J -> R(k,J)k`; in the usual optical convention this is `-Ric_spacetime(k,k)`.  Therefore

`{tau,s}_std = Ric_spacetime(k,k) = 2 P(k,k)`

for null `k` in four dimensions.

## 4. Exact match with the almost-Einstein null-ray ODE

The almost-Einstein equation contracts along an affine null geodesic to

`sigma'' + P(k,k) sigma = 0`

(up to the global curvature-sign convention).

For two independent solutions `sigma_1,sigma_2` of `y''+q y=0`, the ratio satisfies

`{sigma_1/sigma_2,s}_std = 2q`.

Putting `q=P(k,k)` gives exactly the sky projective Schwarzian equation.

Thus the rank-two ODE previously derived independently by GPP is precisely the linearization of the intrinsic projective structure carried by the sky Jacobi curve.

This is stronger than the earlier dimension match.

## 5. Einstein iff affine null parameters are sky-projective

For an affine null geodesic, the trace of the `2x2` optical tidal matrix is proportional to `Ric(k,k)`; in a standard convention it is `-Ric(k,k)`.

Therefore:

`g is Einstein`

iff

`Ric_g(k,k)=0 for every null k`

iff

`every g-affine null-ray parameter belongs to the intrinsic sky-projective class`.

The converse uses the algebraic fact that a symmetric quadratic form vanishing on the entire split null cone is proportional to the metric.

This is now formalized at the finite split-coordinate level in

`GppVerify/CelestialHolography/SkyProjectiveEinsteinCriterion.lean`

commit `60f20d18394963c745769bd9f643f70dc059e214`.

The Lean theorem is deliberately algebraic: it formalizes the null-cone/pure-trace iff.  The differential-geometric identification of the algebraic `skyAffineTrace` with the optical Jacobi trace is external input.

## 6. Candidate intrinsic rank-two bundle

A one-dimensional projective structure canonically determines a rank-two flat `SL(2)` local system: locally, if the projective connection is `2q`, its sections solve

`y'' + q y = 0`,

and the developing/projective coordinate is the ratio of two independent solutions.

This suggests an intrinsic rank-two object over light-ray space:

`E_sky(gamma) := solution space of the Sturm/projective equation determined by the sky Jacobi curve of gamma`.

It has the correct rank and its local equation is exactly the null-ray almost-Einstein equation.

### Current status of the LeBrun identification

**Not proved.**  LeBrun's Einstein bundle `E -> G` is rank two and its nonzero holomorphic sections select Einstein metrics in the conformal class.  Bailey's 1990 paper explicitly identifies intrinsic recognition of `E` from ambitwistor geometry as the missing step for a full nonlinear-graviton-like solution of the Einstein equations.  Wolf's later correspondence-space presentation gives the pullback of the bundle as the kernel of a second-order spinorial operator, but in the explicit form inspected it is written in a right-flat/superconformal specialization.

The new sky result makes the following test precise:

`E ?= E_sky`

where `E_sky` is built from the family of projective Jacobi curves `T_gamma S(gamma(s))`.

The evidence is now structural rather than numerical:

1. both are rank two;
2. both are conformally natural;
3. both linearize a projective/second-order scale equation;
4. contraction of the correspondence-space Einstein operator along a null spinor pair gives the same null-ray equation;
5. the sky projective equation gives exactly the same Sturm/Schwarzian potential.

What remains is the global complex/holomorphic gluing theorem across neighboring rays and proof that the resulting bundle and connection agree with LeBrun's `E`, not merely fibrewise with the same scalar ODE.

## 7. Consequence for the googly programme

The correct nonlinear target is no longer a pointwise map from one curved twistor chirality to another.

The emerging structure is:

`(N,H,Sigma)`

→ each ray has an intrinsic Lagrangian sky Jacobi curve

→ that curve has a canonical projective structure

→ its rank-two linearization is the candidate Einstein fibre

→ an Einstein representative is characterized by agreement of its affine null parameters with those projective structures on every ray.

Orientation reversal remains a separate, simpler operation: it fixes the underlying ray/sky geometry and swaps the two Hodge/Weyl labels of the same full curvature.

This does **not** yet reconstruct a generic interacting Einstein metric from one chiral twistor quotient.  It does, however, provide a concrete intrinsic route to the historically missing Einstein-bundle recognition problem.
