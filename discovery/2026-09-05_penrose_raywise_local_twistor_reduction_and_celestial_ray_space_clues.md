# Penrose raywise local-twistor reduction and celestial ray-space clues

Date: 2026-09-05
Status: primary-source historical synthesis + exact finite reduction + externally established celestial/ambitwistor geometry; global nonlinear bundle identification remains open

## 1. Historical pattern in Penrose's googly programme

A recurring feature of Penrose's own work is that when a single global curved twistor threefold fails to encode generic vacuum gravity, the surviving structures migrate toward null rays, cuts/skies, transport, projective parameters, charges, and extra Einstein/I-structure.

Important pressure points:

- the nonlinear graviton solves one chiral half exactly, but generic complex vacuum curvature has independent SD and ASD sectors;
- hypersurface/null-infinity constructions frequently lose roughly half of the data;
- asymptotic twistor constructions encode one radiative chirality cleanly while the other and the real structure become problematic;
- local-twistor spaces can be defined along each null ray, but different raywise fibres are not canonically identifiable in generic curvature;
- even if a candidate twistor carrier is found, reconstructing spacetime points from it is a separate incidence problem;
- Penrose repeatedly returns to `S^2` families of rays through a point, local-twistor transport, spin-3/2 charges, good cuts, and contact/Legendrian structures.

These are no longer being interpreted as unrelated failed tricks.  They line up with the modern intrinsic datum `(N,H,Sigma)`: light-ray space, its contact distribution, and the distinguished family of skies.

## 2. Specific Penrose clues

### TN31 (1990): preferred/projective parameter near-miss

Penrose's `Twistor theory for vacuum space-times: a new approach` appears in the same issue immediately before Bailey--Eastwood's `Preferred parameters on curves in conformal manifolds`.  Bailey--Eastwood show that a conformal curve has a projective parameter class related by fractional-linear transformations and linearized by a second-order ODE.  This is mathematically adjacent to the modern sky-projective mechanism now used by GPP.  No claim is made that Penrose explicitly connected the two in that issue; it is a historical near-miss candidate.

### TN37: the construction is “too linear”

In `Spin 3/2 fields and local twistors`, Penrose/Mason-type discussion says the desired general twistor space should not retain ordinary vector-space linearity and that the full generalization remains elusive.  This is consistent with the current conclusion that the hard part is nonlinear transverse gluing/descent of raywise linear systems, not the existence of each local linear fibre.

### TN39: point reconstruction is a separate problem

Penrose explicitly separates two questions: first find a twistor space for a general Ricci-flat spacetime; second determine how spacetime points are represented/reconstructed in it.  This strongly anticipates the modern role of the sky family `Sigma`, where a point is encoded by the family of null rays through it rather than by one twistor point.

### TN40: holomorphic one-sided data miss the opposite radiative chirality/reality

In `New Ideas for the Googly Graviton`, Penrose says the asymptotic twistor construction appears to encode only one radiative chirality and remarks that the information is being encoded holomorphically while the usual conjugation/reality operation is unavailable.  This matches the present GPP correction: four-orientation/reality cannot be manufactured from a single chiral holomorphic quotient.  The full ray/sky geometry is orientation-blind and the Hodge labels are imposed on the reconstructed full field.

### TN45: contact/Legendrian null-infinity geometry

The null-infinity Legendre-transform programme derives twistors from contact geometry and describes dual good-cut data by Legendrian surfaces.  This is a clear precursor of the modern null-ray/contact/sky language.

## 3. Penrose 2015 Palatial Twistor Theory

Penrose's later programme moves decisively to the global manifold of null rays and a separate local-twistor space `T_gamma` attached to each ray by conformally natural local-twistor transport.  In generic curvature the different `T_gamma` fibres are not canonically identifiable; local trivializations are non-unique.  A spacetime point should be reconstructed by the `S^2` family of all rays through it, with strong consistency of the raywise twistor structure over that family.  Einstein/vacuum structure is represented by additional `I`-structure preserved by transport/patching.

This is strikingly close to the current GPP architecture:

`(N,H,Sigma)` + raywise rank-two projective system + transverse sky/metricity gluing.

## 4. New exact reduction of Penrose's raywise local-twistor transport

Penrose's transport along a null ray has schematic spinor form

`D omega^B = -i k^{BB'} pi_{B'}`,
`D pi_{B'} = -i k^{AA'} P_{AA'BB'} omega^B`.

Take an affinely parametrized null ray

`k^{AA'} = lambda^A lambdatilde^{A'}`

with parallel spinors and restrict to the natural null-incidence line

`omega^A = f lambda^A`.

Define the contracted second component

`g = lambdatilde^{A'} pi_{A'}`.

The system reduces to

`f' = -i g`,
`g' = -i kappa f`,

where `kappa` is the null contraction of Penrose's curvature coefficient.  Therefore

`f'' + kappa f = 0`.

After `p := -i g`,

`f' = p`,
`p' = -kappa f`,

which is exactly the same rank-two `SL(2)` projective/Sturm generator already obtained from the sky-projective and null almost-Einstein analysis.

Important convention caveat: Penrose's displayed `P_ab` in the 2015 paper has the opposite displayed sign from many modern Schouten conventions (and Riemann-sign conventions also differ).  The reduction itself is exact; identifying `kappa` with modern `P(k,k)` requires translating conventions.

Formalized in:

`GppVerify/CelestialHolography/PenroseLocalTwistorRayReduction.lean`

commit `17e1484f8a1ae150a0b9d51d07b7fd32b7882438`.

Wired into `SkyEinsteinIntrinsicSpine.lean` at commit

`346dace4edf1b8f89696a1b95d87175b3349a122`.

Current targeted chain:

`E_sky ?= incidence-restricted Penrose T_gamma system ?= E_LeBrun`.

The first equality now holds at the local scalar-equation/generator level modulo curvature convention.  The global holomorphic/transverse bundle identification remains open.

## 5. Celestial/ambitwistor clues

Modern celestial holography reinforces the same ambidextrous structure rather than restoring a single chiral `PT`:

- split twistor half-Fourier transforms become the two celestial light transforms;
- the two celestial factors are the left/right `SL(2,R)` factors of the split screen at null infinity;
- full Fourier corresponds to the product of the two light transforms/full shadow at the representation-label level while preserving the physical momentum-state helicity;
- four-dimensional ambitwistor space is the space of null geodesics and is naturally tied to the cotangent/contact geometry of null infinity;
- a spacetime point gives a `CP1 x CP1` family of null directions in the complex split picture, i.e. the complex sky;
- soft/BMS and `w_{1+infinity}` structures act Hamiltonianly on the null-ray/twistor phase space;
- modern twistor sigma-model treatments obtain full-helicity perturbative gravity around a self-dual background without requiring a generic second globally integrable curved twistor threefold.

A potentially important distinction is now explicit:

1. celestial `SL(2)_L x SL(2)_R` acts on **direction/generator labels**;
2. the sky-projective `SL(2)` acts on the **projective parameter along each null ray**.

These are different structures.  The nonlinear metricity/descent equations may be precisely what couples the angular/directional and along-ray projective layers.

## 6. Null-surface formulation convergence

The null-surface formulation (NSF) has a linear second-order conformal-scale equation along the affine ray coordinate and separate metricity equations coupling angular/celestial dependence.  After curvature-sign translation, its ray equation matches the null almost-Einstein/sky Sturm equation.  This strongly suggests that NSF metricity equations may realize the transverse descent condition missing from a naive direct sum of independent raywise solution spaces.

Do not infer historical identity from the shared phrase “Einstein bundle equation”; the older NSF usage is attributed to Kozameh--Newman rather than LeBrun.  The significance is mathematical: same raywise scale problem plus explicit transverse compatibility equations.

## 7. Penrose cosmological-constant clue

Penrose has said retrospectively that a googly construction he once abandoned because it assumed `Lambda=0` later appeared more promising once `Lambda != 0` was observationally relevant.  This deserves focused investigation because GPP's exact infinity-twistor algebra has a parallel structural transition:

- `I_Lambda` is non-null and gives an invertible Clifford/Pin bridge for `Lambda != 0`;
- at `Lambda=0` the infinity twistor becomes null and the pointwise bridge degenerates to an exact complex/projective correspondence.

This resemblance is **not yet an identification**.  The next task is to inspect Penrose's actual nonzero-Lambda mechanism and compare operators, not slogans.

## 8. Current interpretation

The historical evidence increasingly supports a revised formulation of the googly problem:

The missing object is probably not a canonical nonlinear point map from one chiral twistor threefold to the other.  Generic curvature does not supply two such global quotient spaces.  The invariant nonlinear carrier is closer to

`(null-ray/contact space, sky incidence family, raywise local-twistor/projective transport, Einstein/I-structure, transverse metricity/descent)`.

The chiral twistor spaces arise as special integrable projections/limits.  Four-orientation reversal then swaps the two Hodge labels of the already reconstructed full curvature rather than generating an independent missing field.

This is a strong structural synthesis, not yet the final googly theorem.
