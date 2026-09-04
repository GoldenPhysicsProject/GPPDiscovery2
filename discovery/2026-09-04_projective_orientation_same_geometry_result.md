# Projective orientation invariance result

A useful exact consequence emerged from the split Hodge/polarity analysis.

Reversing orientation sends the Hodge operator

\[
*_{\mathfrak o}\mapsto -*_{\mathfrak o}.
\]

For any Plucker representative `p`, the two Hodge images therefore differ only by the central sign:

\[
*_{-\mathfrak o}p=-*_{\mathfrak o}p.
\]

But Plucker coordinates are projective.  Hence

\[
[p]=[-p].
\]

Therefore the complement plane selected by Hodge/polarity is unchanged as a projective Grassmannian point when the orientation is reversed, even though its Hodge eigenvalue label changes sign.

For a self-dual representative

\[
*_{\mathfrak o}p=p,
\]

one has

\[
*_{-\mathfrak o}p=-p.
\]

Thus the same projective geometry is labelled ASD in the reversed orientation:

\[
\boxed{[p]\ \text{unchanged},\qquad SD_{\mathfrak o}\leftrightarrow ASD_{-\mathfrak o}.}
\]

This is now formalized in

`GppVerify/CelestialHolography/ProjectiveOrientationInvariance.lean`

on the focused branch.

This is a precise finite-dimensional realization of the phrase “same geometry, opposite chirality label.”  It does not identify orientation reversal with Wigner time reversal, CPT, or any dynamical operation.

Combined with the split-polarity result,

\[
D_{\rm polarity}=D_{\rm Gr}=D_{\rm Hodge}
\]

on the big cell, orientation reversal changes the lift/label rather than creating a second Grassmannian geometry.  This materially strengthens the one-geometry/two-oriented-lifts interpretation.
