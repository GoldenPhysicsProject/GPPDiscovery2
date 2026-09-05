# Horizon orientation / bifurcation diagnostic

## Motivation

Daniel's current hypothesis is that the black-hole horizon may be where the forward-oriented description of a massive fermion encounters its conjugate reverse-oriented description, converting the massive state into massless radiation.  This note separates the exact Schwarzschild/Kruskal geometry from the new Shadow mechanism.

## Exact ordinary geometry

In Schwarzschild units c=1 with horizon radius r_s=2GM,

f(r)=1-r_s/r,

g(K,K)=-f(r)

for the stationary Killing field K=∂_t.  Hence

- r>r_s: K is timelike,
- r=r_s: K is null,
- 0<r<r_s: K is spacelike.

For a geodesic dropped from rest at infinity, the local speed measured by the exterior static-observer family obeys

v_static^2=r_s/r,

so v_static→1 as r→r_s^+.  This is not an invariant local collision condition: the static observer family itself becomes null in the horizon limit and no timelike static observer exists on r=r_s.  Therefore any Shadow annihilation trigger should be formulated using invariant horizon structure (for example K^2=0, null expansion, or a covariant boundary operator), not the phrase 'the infaller reaches c'.

In Painleve-Gullstrand / river coordinates, an outgoing radial null ray has

dr/dt_P=1-sqrt(r_s/r).

At r=r_s this equals zero.  Thus a classical outgoing photon exactly on the future event horizon is a horizon generator, not an escaping ray.  Escape to future null infinity requires emission at r>r_s (or a genuine modification of the classical horizon geometry).  This matches the safer formulation already used in `The Shadow Horizon`, which proves escape and finite affine propagation only for r_e>r_s.

## Kruskal orientation structure

In the maximally extended eternal Schwarzschild solution,

r=r_s  iff  U=0 or V=0.

The branch U=0 is the future black-hole horizon H^+, the branch V=0 is the past white-hole horizon H^-, and they meet at U=V=0, the bifurcation two-sphere (angular factors suppressed).

This is the cleanest ordinary-GR object resembling Daniel's phrase 'future orientation runs into past orientation'.  However it is crucial that a realistic collapse black hole contains H^+ but not the past white-hole branch H^- of the eternal Kruskal extension.  Therefore a universal Shadow mechanism cannot simply identify an astrophysical horizon with the eternal bifurcation sphere.  The missing reverse-oriented branch would have to be supplied by the Shadow/dual representation itself.

## Connection to the current googly programme

This suggests a sharper target.  The same duality D_epsilon that is being constructed on twistor/Grassmannian data could induce a conjugate horizon datum without requiring a second classical white-hole region:

x on H^+  ->  D_epsilon x in the conjugate orientation representation.

The desired boundary condition would then identify the two representatives on the physical horizon quotient while allowing a massless radiation channel:

[x]=[D_epsilon x],

A_H(x,D_epsilon x) -> gamma_+ ⊕ gamma_-.

This would implement 'both halves are here' as representation duality at one geometric future horizon rather than as two literal spacetime interiors.

## Hard falsifiers

1. The boundary-annihilation vertex must be covariant and cannot be triggered merely by the static-frame limiting speed v→c.
2. A photon created exactly on a classical future event horizon cannot escape to larger r; the exterior photon channel must originate at r_s+epsilon, from a stretched/quantum horizon, or from modified causal structure.
3. A collapse spacetime has no classical H^- branch.  The conjugate branch must arise from the Shadow duality/field representation if the mechanism is to be universal.
4. The mechanism must conserve local gauge charge, energy, angular momentum and fermion parity, and it must reproduce Hawking thermality rather than assume the Planck factor.
5. The claim 'from the photon's perspective' should be replaced by the invariant statement ds^2=0; photons have no rest frame.

## Formalization

Added `GppVerify/CelestialHolography/HorizonOrientationDiagnostics.lean` on `codex/orientation-mass-time-formalization`.  It proves the exact Killing-norm sign change, the horizon value of the exterior static-frame speed diagnostic, the zero river-coordinate radial speed of an outgoing horizon generator, and the future/past Kruskal branch intersection algebra.  No boundary annihilation physics is assumed.
