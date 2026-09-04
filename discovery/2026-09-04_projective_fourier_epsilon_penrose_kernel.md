# Projective Fourier, ambient epsilon, and the Penrose-kernel quotient

## Why this matters

The remaining linear googly problem is no longer the finite-dimensional geometry. On the split big cell we now have an explicit chain

\[
D_{\rm Fourier\ support}\sim D_{\rm annihilator}\sim D_{\rm polarity}=D_{\rm Gr}=D_{\rm Hodge}
\]

up to the central projective sign induced by the split musical map `V* -> V`.

The remaining issue is to descend the full four-dimensional Fourier transform from homogeneous distributions on `R^4` to projective twistor/X-ray data.

## Same ambient four-form

The standard projective twistor top form is

\[
D^3Z=\epsilon_{ABCD}Z^A\,dZ^B\wedge dZ^C\wedge dZ^D,
\]

with projective homogeneity `+4`.  Thus

\[
K_{PT}=\mathcal O(-4).
\]

The projective full Fourier transform pairs source and target homogeneities by

\[
\boxed{k\mapsto-k-4}.
\]

This is exactly the same canonical reflection already derived in the GPP epsilon spine.  Consequently the `-4` is not a separate twistor convention inserted by hand: it is the projective residue of ambient rank four / the epsilon top form.

For doubled helicity `n=2h`,

\[
k=n-2\quad\Longrightarrow\quad-k-4=-n-2=2(-h)-2.
\]

Hence the projective full Fourier transform lands at the ordinary twistor homogeneity assigned to opposite helicity.

For gravity:

\[
\boxed{\mathcal O(2)\leftrightarrow\mathcal O(-6)}.
\]

## Distributional necessity

A nonzero homogeneous twistor function cannot in general be Schwartz in the radial direction.  The naive full Fourier integral therefore fails to converge simultaneously at zero and infinity.  The correct transform is distributional/projective.

This is not an incidental nuisance.  It is precisely why the field-level googly map should be formulated on cohomology/distribution classes rather than as a pointwise map on projective twistor points.

## Penrose-null ambiguity

Standard projective Fourier formulas acquire a polynomial ambiguity for certain integer weights.  The relevant Penrose/X-ray transform annihilates this ambiguity, so distinct projective Fourier representatives can determine the same bulk field.

This suggests the correct physical codomain is not a raw function space but a quotient by the Penrose kernel:

\[
f\sim g\quad\Longleftrightarrow\quad P(f)=P(g).
\]

Then for any `q` with `P(q)=0`,

\[
P(f+q)=P(f).
\]

This quotient logic is now formalized in

`GppVerify/CelestialHolography/ProjectiveFourierPenroseQuotient.lean`.

The module also proves the exact homogeneity bookkeeping

\[
\operatorname{sourceWeight}(n)=-n-4=\operatorname{serreWeight}(n),
\]

with involutive return and the graviton pair `2 <-> -6`.

## Relation to Daniel's diagonal/orbit idea

This is a stronger mathematical form of the operational quotient idea than treating `-- = ++` as arithmetic signs.  The relevant statement is instead

\[
[f]=[f+q]\qquad(q\in\ker P),
\]

or for orientation/projective representatives

\[
[p]=[-p].
\]

The duality may change the upstairs representative, homogeneous description, or chirality label while leaving the downstairs Penrose/Einstein observable unchanged.

## Exact remaining linear theorem

The high-value theorem is now the projective distributional Fourier-slice identity:

\[
\boxed{P_{\rm dual}\circ\mathcal F_{\rm proj}=P_{\rm source}}
\]

on the appropriate quotient classes, followed by split musical/polarity identification and orientation relabelling.

At vector-Schwartz level the expected Fourier-slice calculation is

\[
R_AF=R_{A^\circ}(\widehat F),
\]

because integration over the graph plane imposes exactly the two support constraints defining the annihilator plane.  Those support constraints and their exact annihilator parameterization are already formalized in `FourierSliceSupportGeometry.lean`.

What remains analytically is:

1. homogeneous tempered-distribution Fourier transform;
2. degree `k -> -k-4` at the actual transform level;
3. projective X-ray descent;
4. proof that any regularization ambiguity is Penrose-null;
5. orientation/chirality identification of the reconstructed bulk field.

If these close, the linear Penrose googly square is no longer conditional.

## External status

The relevant split-twistor literature already contains the full Fourier transform between twistor and dual-twistor homogeneous data, the `k -> -k-4` homogeneity law, distributional projective treatment, and X-ray/Penrose interpretation.  Those results are external checks and technical ingredients, not the source of the GPP geometry.  The GPP-specific synthesis is the identification of their support geometry with ambient-four annihilator/polarity/Grassmannian/Hodge duality and the one-geometry/two-oriented-lifts interpretation.
