# Orientation-blind ambitwistor geometry and the Einstein correspondence selector

Date: 2026-09-05
Status: mixed exact finite algebra + externally verified geometric input; nonlinear intrinsic Einstein-bundle identification still open

## 1. Orientation reversal does not move intrinsic ambitwistor points

The space of light rays / null geodesics and its canonical contact structure depend on the conformal class, not on the four-dimensional spacetime orientation. Therefore reversing the 4-orientation leaves each unparametrized null geodesic fixed and leaves the intrinsic ambitwistor/contact manifold unchanged.

This corrects an earlier candidate identification: flat factor exchange `(Z,W)<->(W,Z)` is **not** literally the spacetime orientation reversal. It is a distinct parity/contragredient symmetry of the flat twistor/dual-twistor presentation.

On the bulk two-form/Weyl side, orientation reversal is exactly

`star_o -> -star_o`.

For generic complexified fields the Hodge projectors are

`P_+^o = 1/2 (1 - i star_o)`,
`P_-^o = 1/2 (1 + i star_o)`.

Hence

`P_+^{-o}(F)=P_-^o(F)`,
`P_-^{-o}(F)=P_+^o(F)`

for the **same underlying field** `F`.

Lean: `OrientationProjectorSwap.lean`, commit `58743839a644a54274d61698305427d18752f0fd`.

## 2. LeBrun/Bailey Einstein bundle and correspondence-space operator

External literature confirms:

- LeBrun's ambitwistor space is the space of complex null geodesics and its complex/contact geometry encodes the conformal structure.
- LeBrun's rank-2 holomorphic Einstein bundle has nonvanishing holomorphic sections in one-to-one correspondence with Einstein metrics in the conformal class.
- Bailey explicitly states that the open problem is to characterize this Einstein bundle intrinsically from ambitwistor geometry.
- A later technical treatment writes the pullback condition on correspondence space as a second-order spinorial operator of schematic form

  `Delta_AB = lambda^{A'} lambda^{B'} (nabla_{AA'} nabla_{BB'} + curvature/Schouten term)`

  acting on an appropriate conformal scale bundle.

This is the spinor/correspondence-space form of the almost-Einstein tensor equation.

## 3. Exact finite algebra connecting the correspondence operator to null-cone rigidity

In split signature every null tangent vector is a rank-one matrix

`X_{AA'} = lambda_A lambdatilde_{A'}`.

New Lean module `SpinorEinsteinCorrespondenceSelector.lean` proves the converse too:

`det X = 0` iff `X = lambda tensor lambdatilde` for some real two-spinors.

Therefore a quadratic tensor polynomial vanishes on every spinor pair iff it vanishes on the entire null cone. Combining with `NullConeEinsteinSelector.lean` gives:

`T(lambda tensor lambdatilde, lambda tensor lambdatilde)=0 for all spinors`

iff

`T` is a scalar multiple of the split determinant metric (pure trace).

This is exactly the finite linear-algebra core behind the statement that the correspondence-space spinor selector recovers the trace-free almost-Einstein equation.

Lean commit: `f520b560fa05e09fd49fd8e8d93bccae11a3124e`.

## 4. Current operation taxonomy

The following are now explicitly distinct:

1. **4-orientation reversal**: identity on intrinsic light rays/contact space; `star -> -star`; swaps generic Hodge/Weyl projectors.
2. **Flat factor exchange** `(Z,W)<->(W,Z)`: anti-contact in the flat incidence presentation; parity/contragredient exchange, not orientation reversal itself.
3. **Non-null Pin/Klein reflection**: actual determinant `-1` orthogonal reflection in the 6D Klein/tractor module, with odd Clifford spinor lift.
4. **Celestial light/shadow transforms**: normalized Weyl intertwiners on principal-series field representations; not pointwise spacetime orientation maps.
5. **Full Fourier PT<->PT***: cross-side same-physical-state representation transform; not generic nonlinear chirality generation.

Capstone correction commit: `83bbb1fc202cd05b15fc01bec9a6aae6a5884d5f`.

## 5. Nonlinear frontier

The historical googly problem is **not** solved merely by orientation relabelling. Orientation reversal trivially exchanges the chiral labels of an already existing full conformal curvature, and Einstein-ness is orientation-blind.

The real nonlinear problem is to reconstruct/encode generic interacting left and right chiral data intrinsically on the single curved ambitwistor/contact geometry, or equivalently to recognize LeBrun's Einstein bundle and its field data directly from that intrinsic geometry rather than through its correspondence-space pullback or through one integrable self-dual twistor quotient.

This is now the precise target.
