# Googly resolution: hard target for the orientation/mass program

Date: 2026-09-02

## Status correction

The current `GPPVerify/CelestialHolography/TwistorGoogly.lean` does **not** formalize a googly resolution. It proves only finite dimension/counting identities plus the elementary involution `Δ ↦ 2-Δ`; the Penrose/Ward/cohomology/googly statements are honest `open_... : True := trivial` stubs.

The historical framework route `googly = Haar inversion = T = shadow` must therefore be treated as a conjectural chain until an actual map is constructed and shown to intertwine the nonlinear field equations. In particular, the shortcut `ω ↦ -ω ⇒ Δ ↦ 2-Δ` is invalid and remains retired.

Current literature check (2026-09-02): Penrose's googly problem is still described as the difficulty of encoding the opposite-helicity/non-self-dual sector nonperturbatively in twistor geometry. A July 2026 paper by Adamo–Araneda–Seet–Sharma gives a twistor-space construction for the particular non-self-dual Schwarzschild solution and explicitly presents it as the first such instance, not a general solution. This raises the bar for any GPP claim of a full resolution.

## What counts as a real solution

Let `PT_+` denote the twistor space naturally encoding one chiral sector and `PT_-` the dual/conjugate structure encoding the other. A GPP resolution must construct from one canonical geometric datum `X` (not by simply postulating an independent second twistor theory) two projections/realizations

    P_+ : X -> PT_+
    P_- : X -> PT_-

and a canonical orientation/shadow operation

    G : X -> X

such that the following are proved.

1. **Chiral exchange:** `P_- ∘ G` is the correct opposite-helicity Penrose/Ward datum associated to `P_+`.
2. **Field-equation compatibility:** the induced transform exchanges SD and ASD solutions and preserves the full nonlinear Yang–Mills or Einstein equations in the appropriate sense.
3. **Reality/orientation compatibility:** the map respects the Lorentzian real structure and the actual spacetime orientation/time-orientation data; it is not merely a complex-algebra involution.
4. **Amplitude normalization:** at the linearized/scattering level the map sends MHV data to anti-MHV data with the correct helicity, phases, little-group weights, and normalizations.
5. **Closure:** applying the operation twice/four times has the claimed gauge/diffeomorphism/deck behavior, proved rather than inferred by analogy.
6. **No doubled independent geometry:** the opposite sector is reconstructed canonically from the same datum `X`; introducing `PT*` by hand and renaming it a shadow sector does not solve the problem.

A minimal commuting-square target is

    X  --G-->  X
    |          |
   P+         P-
    v          v
   SD  --C--> ASD

where `C` is the mathematically correct chirality/orientation conjugation on fields.

## Relation to the current orientation/mass work

The exact structures already established are potentially useful but are not yet a googly solution:

- Grassmannian chart map `τ_Gr^2 = -id`, `τ_Gr^4 = id` on the big cell;
- cleared Jacobian polynomial identity `N^4 = D^4 I`;
- half-flip quotient `(Z2 x Z2)/diag(Z2) ≅ Z2`;
- Hodge/chirality fact to formalize: reversing spacetime orientation sends `* -> -*`, hence exchanges the ±i eigenspaces of Lorentzian 2-forms;
- celestial shadow: `(Δ,J) -> (2-Δ,-J)`;
- anti-linear shadow/conjugation composition: `Δ -> 2-conj(Δ)`, with principal-series fixed locus `Re Δ=1`.

The most promising route is therefore **orientation first**, not `T` first:

    spacetime orientation reversal
       -> Hodge star sign reversal
       -> SD <-> ASD
       -> induced twistor/dual-twistor map
       -> celestial helicity/shadow action

Only after this chain is explicit should one ask whether the physical antiunitary Wigner/CPT operation implements the same map on the relevant real slice.

## Immediate theorem targets

### A. Lorentzian Hodge exchange theorem

Formalize for an oriented four-dimensional Lorentzian vector space:

    *^2 = -1 on 2-forms,
    *_{-o} = -*_o,

therefore

    *F = +iF  <=>  *_{-o}F = -iF.

This is the clean mathematical operation that genuinely exchanges SD and ASD sectors.

### B. Plucker/Hodge theorem on Gr(2,4)

For a decomposable bivector `P = u ∧ v` representing a point of `Gr(2,4)` in the Klein quadric, construct the complementary-plane map and prove exactly how it acts on Plücker coordinates. Determine whether it is literally the Hodge star for a chosen bilinear form/orientation or only related after metric identification. Do not assume equality.

### C. Penrose incidence intertwiner

Construct the induced map on incidence relations

    ω^A = i x^{AA'} π_{A'}

(or the chosen convention) and determine whether complementary-plane/orientation reversal maps twistor incidence to dual-twistor incidence. This is the first real candidate for the missing `P_- ∘ G` map.

### D. Linearized cohomology test

Before attempting nonlinear gravity, prove the map on massless free-field cohomology with correct line-bundle weights. For spin 1 and spin 2 verify that the transform exchanges the relevant SD/ASD helicity classes with exact normalization.

### E. Nonlinear test

Only after A-D: test whether the construction carries the integrability/deformation conditions of the nonlinear graviton/Ward correspondence into the opposite sector. Failure here means the construction is a linearized duality, not a googly resolution.

## Falsifiers

The proposed GPP route fails as a full googly solution if any of these occurs:

- the Grassmannian complementary-plane operation does not induce dual-twistor incidence;
- it exchanges helicity only at the free-field level but not nonlinear deformation data;
- it requires an independently specified `PT*` rather than reconstructing it;
- the induced celestial action is not the standard shadow transform with correct weights;
- Lorentzian reality conditions break the proposed orientation identification;
- MHV/anti-MHV normalizations or little-group weights disagree.

This is now the standard for the flagship paper: no `googly solved` language unless the commuting construction and nonlinear compatibility are actually obtained.
