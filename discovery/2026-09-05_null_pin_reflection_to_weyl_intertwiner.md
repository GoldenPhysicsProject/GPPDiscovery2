# Null Pin reflection to Weyl intertwiner mechanism

Date: 2026-09-05
Status: exact finite-dimensional core + externally supported representation-theoretic interpretation; analytic degeneration theorem still open.

## Exact internal algebra

The GPP Klein/Clifford model now has the following pieces.

For `p in Lambda^2 V`, the odd Clifford action on `V + V*` satisfies

`C(p)^2 = -Q_Klein(p) id`.

The cosmological infinity-twistor family

`I_Lambda = (Lambda,0,0,0,0,1)`

has `Q_Klein(I_Lambda)=Lambda`.

For `Lambda != 0`, `C(I_Lambda)` is therefore invertible and exchanges the two half-spinor modules.  Independently, the same non-null Klein vector defines the orthogonal reflection

`r_I(q)=q-B_epsilon(q,I)/Q(I) I`,

whose active `(p01,p23)` block is

`(x,y) -> (-Lambda y,-x/Lambda)`

and has determinant `-1`.

New module `KleinCliffordPinConjugation.lean` formalizes the polarized Clifford anticommutator

`C(p)C(q)+C(q)C(p)=-B_epsilon(p,q) id`

and the coordinate Pin-adjoint identity

`(1/Q(v)) C(v) C(q) C(v) = C(r_v(q))`.

Because `C(v)^(-1)=-C(v)/Q(v)`, this is exactly

`-C(v)C(q)C(v)^(-1)=C(r_v(q))`.

If the module compiles, the vector-side reflection and spinor-side chirality exchange are no longer merely parallel applications of external Pin theory; they are one internally proved Clifford conjugation theorem.

For positive-square parameter `Lambda=t^2`, `KleinWeylReflectionConjugacy.lean` proves

`R_{t^2}=a_t w a_t^{-1}`

on the active hyperbolic plane, with fixed Weyl element `w(x,y)=(-y,-x)` and split dilation `a_t(x,y)=(tx,y/t)`.

## Flat degeneration

At `Lambda=0`, the pointwise orthogonal reflection is undefined because its normal is null.  The chiral Clifford map does not disappear; it becomes the exact two-periodic complex already formalized in `FlatInfinityChiralComplex.lean`:

`V -> V* -> V`, with `im = ker` on each side.

Each kernel is two-dimensional.  Projectivization gives an `RP^1` celestial factor.

`FlatNullWeylFiberGeometry.lean` now proves the elementary rank-one geometry on this factor:

- affine representative `(1,u)`;
- unipotent translation orbit `n(a):(1,u)->(1,u+a)`;
- Weyl spinor action `w(x,y)=(-y,x)`;
- `w^2=-id`, hence projective order two;
- affine projective action `u -> -1/u`;
- the whole affine orbit remains in the corresponding flat Clifford kernel.

## Representation-theoretic interpretation

This corrects an earlier overstrong idea.  The normalized Knapp--Stein operator is not simply the strong `Lambda -> 0` limit of the point transformation `a_t w a_t^{-1}`.  Standard principal-series theory constructs the Weyl intertwiner by integrating over the appropriate unipotent orbit.  This is exactly the kind of non-pointlike operation forced by the flat kernel geometry.

Brown--Gowdy--Spence, *Celestial Twistor Amplitudes* (Phys. Rev. D 108, 066009, 2023; arXiv:2212.01327), show in split signature that the normalized light transform is the Weyl intertwiner on one `SL(2,R)` factor and that the half-Fourier transform commutes with it after chiral Mellin transform.  Their light transform is an integral over `RP^1` with kernel

`|w-z|^(2h-2) sgn(w-z)^s_h`,

and the normalized transform is self-inverse.  Thus the analytic field-level operation acts on precisely the projectivized chiral kernel factor produced by the null Clifford complex.

The safe mechanism is therefore:

non-null Pin reflection / chirality isomorphism

`->` null rank drop

`->` projective kernel/unipotent orbit

`->` normalized Weyl/Knapp--Stein integral intertwiner.

The last arrow is externally standard at the representation level, but an explicit theorem identifying it as a renormalized `Lambda -> 0` degeneration of the GPP `I_Lambda` family has NOT yet been proved.

## Principal-series normalization cross-check

For the GPP conical block, with `h=(1+i lambda)/2`, the prefactor is

`c(h)=2 Gamma(2h)/Gamma(h)^2`

and

`|c(h)|^2=(2 lambda/pi)coth(pi lambda/2)`.

The odd `Z2` split principal-series/light sector has Plancherel/light density proportional to

`(lambda/(2 pi)) coth(pi lambda/2)`,

so the internally formalized closed-form relation is

`|c(h)|^2 = 4 rho_odd(lambda)`

in the normalization used in `PrincipalSeriesLightPlancherelMatch.lean`.

Using Brown--Gowdy--Spence's explicit odd light prefactor `kappa_1`, the stronger complex relation on the unitary axis is

`c(h) = -2 i [Gamma(conj h)/Gamma(h)] kappa_1(1-h)`.

The bracketed Gamma ratio has unit modulus.  Hence the conical block prefactor is twice the normalized odd light amplitude times a pure principal-series scattering phase, not literally the same complex normalization.

## Current open theorem

Construct the analytic renormalized degeneration connecting the non-null `I_Lambda` Pin action to the flat principal-series Knapp--Stein/light intertwiner, ideally through the parabolic/unipotent boundary orbit or a distributional limit.  Do not replace this by the false statement that the pointwise matrices themselves converge.
