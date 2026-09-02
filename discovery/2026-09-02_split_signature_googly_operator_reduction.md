# Split-signature reduction of the googly problem

Date: 2026-09-02

## Source-corpus correction

Daniel's `Celestial_Holography_v8_COMPLETE.pdf` explicitly switched the working real slice to split signature `(2,2)` after complexifying first.  It states that no reality condition is imposed until the end and uses the fact that on real 2-forms

`star^2 = +1`

in split signature, versus `star^2=-1` in Lorentzian signature.

Therefore the current googly attack should use complexified twistor geometry with a split real slice as the calculational foundation.  Lorentzian reality/polarity is a final descent/analytic-continuation condition, not the fundamental helicity-exchange mechanism.

## External operator that already exists

Brown--Gowdy--Spence, *Celestial Twistor Amplitudes* (arXiv:2212.01327 / PRD 108, 066009), works precisely in split signature and gives the operator architecture we were trying to rediscover:

- independent real spinors `lambda` and `lambda_tilde`;
- Lorentz group `SL(2,R)_L x SL(2,R)_R`;
- celestial torus `RP^1 x RP^1`;
- left light transform `L: (h,hbar)->(1-h,hbar)`;
- right/dual light transform `Lbar: (h,hbar)->(h,1-hbar)`;
- normalized `L^2 = Lbar^2 = 1`;
- `L` and `Lbar` preserve the discrete `Z2` parity weights;
- the full shadow is the product of the commuting light transforms;
- half-Fourier transforms to twistor and dual-twistor space are self-inverse;
- chiral Mellin + half-Fourier commutes with light transform;
- the full Fourier transform maps twistor space to dual twistor space and induces the corresponding conformal-algebra automorphism, including helicity reversal.

Hence at the representation/state level the split-signature googly candidate is not an unknown Fourier/Radon transform.  A natural twistor<->dual-twistor Fourier operator already exists and its celestial image is the product `L Lbar`, i.e. shadow.

This does **not** prove `shadow = Wigner T`, nor does it prove the nonlinear googly problem.

## Exact label factorization

With

`Delta = h+hbar`, `J=h-hbar`,

we have

`L Lbar : (h,hbar) -> (1-h,1-hbar)`

and therefore

`Delta -> 2-Delta`, `J -> -J`.

So ordinary celestial shadow factorizes in split signature into two commuting chiral reflections.  This is cleaner than the old slogan `shadow=T`.

The discrete sign-representation labels remain fixed.  Thus helicity/spin reversal and the even/odd `Z2` representation are distinct pieces of data.

## Signature-sensitive Grassmannian correction

For split metric `diag(+,+,-,-)` and orientation `0123`, on Plucker coordinates ordered `(01,02,03,12,13,23)`,

`star_split(p) = (p23,p13,-p12,-p03,p02,p01)`.

This has `star_split^2=1` and preserves the Klein quadric.

For the graph plane `[I|A]`, this induces

`C_split(A) = A^{-T}`,

whereas the Euclidean Hodge convention previously formalized induces `-A^{-T}`.  The central sign is signature-dependent and must not be silently identified.

The existing Grassmannian map `tau` factors in split signature as

`tau = Q o C_split`,

where

`Q(a,b,c,d)=(c,d,-a,-b)`, `Q^2=-I`,

and `Q` commutes with `C_split`.  Hence

`tau^2=-I`, `tau^4=I`.

This yields a clean order-two/order-four separation:

- Hodge/complement downstairs: order 2;
- fixed chart quarter-turn lift: square `-1`;
- combined Grassmannian `tau`: order 4.

No physical identification of `Q` with spin is yet justified.

## Important retraction / operator-order correction

Earlier we elevated the speculative target

`G^2 = orientation reversal`, hence `G^4=1`,

partly motivated by Neiman's higher-spin star-product formulation where the Penrose transform is described as a square root of CPT.

That is **not** presently the best target for the split-signature celestial/twistor googly operator.  Brown--Gowdy--Spence normalize the relevant Fourier, half-Fourier, light and shadow transforms to be self-inverse.  These are different operator categories.

Current evidence therefore favors:

- state/celestial googly Fourier-shadow operator: order 2;
- Grassmannian `tau` lift: order 4;
- any relation between them must be proved as a projection/quotient/lift theorem rather than assumed.

Keep `GooglySquareRoot.lean` only as an abstract conditional algebra result.

## The remaining linear googly theorem is now narrow

We need to prove the Penrose/orientation commuting square for the *known* split-signature full Fourier operator:

```
Twistor data  --F-->  Dual-twistor data
    | P_-                  | P_+
    v                      v
 ASD bulk     --R_o-->    SD bulk
```

where `R_o` is orientation reversal, equivalently `star_o -> -star_o` on the split real slice.

Required work:

1. Choose a rigorous class of twistor representatives/cohomology/distributions on which the full Fourier transform is defined.
2. Prove it descends to the Penrose cohomology quotient with the correct homogeneity.
3. Compute the Penrose transform before and after Fourier and prove equality with orientation-reversed curvature, including normalization.
4. Track the discrete split-signature parity labels.
5. Verify MHV <-> anti-MHV phases/sign factors in the ambidextrous basis.
6. Only after the linear square is exact, investigate nonlinear Ward/nonlinear-graviton compatibility.

## Caveats from native split representation theory

The split little group is `R* = R_+ x Z2`.  Brown--Gowdy--Spence's native unitary split representations use continuous imaginary helicity together with a discrete parity label.  Fixed physical integer/half-integer helicity amplitudes in `(2,2)` are treated by analytic continuation from `(1,3)`.

Therefore older CH language treating physical `J=+/-2` as though it were automatically a native split-unitary label needs auditing.  The analytic continuation may be perfectly valid, but the distinction must be explicit.

Likewise the split celestial boundary is a torus `RP^1 x RP^1`, not literally the Lorentzian celestial sphere `S^2`.  Any CH section mixing these without analytic-continuation qualification should be corrected.

## Nonlinear literature checkpoint

Mason, *Gravity from holomorphic discs and celestial Lw_{1+infinity} symmetries* (arXiv:2212.10895), gives a fully nonlinear encoding of asymptotically flat self-dual gravity in split signature through a real homogeneous function deforming `RP^3` inside `CP^3`.  Full non-self-dual Einstein gravity amplitudes arise as correlators of a chiral twistor sigma model / holomorphic-disc theory.

This is highly relevant, but amplitudes for full Einstein gravity are not yet the same as a general metric-by-metric nonlinear googly reconstruction theorem.  Do not overclaim.

## Formalization commits

On `GPPVerify:codex/orientation-mass-time-formalization`:

- `SplitSignatureGooglyFactorization.lean` — `1ed23b2257ef4320e3fb3eb83e3dd6111b7681b8`
- `SplitSignatureHodgeGrassmannian.lean` — final current version at `acc2cee004107650803fd6bc12bde8c8908bb1be`
- `SplitSignatureLightParity.lean` — `46478bdc2600f716a59198b68d44f3c30bfb7f70`

Exact CI must still pass before these are called kernel-certified.
