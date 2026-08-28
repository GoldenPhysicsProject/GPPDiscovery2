# Googly exchange lifts to an explicit antiunitary twistor involution

Codex/GPT continuation, 2026-08-28. No Claude material consulted.

The existing Verify2 googly exchange on the ordered Plücker basis

\[
(p_{01},p_{02},p_{03},p_{12},p_{13},p_{23})
\]

acts by

\[
(+\overline{\phantom z},+\overline{\phantom z},+\overline{\phantom z},
-\overline{\phantom z},-\overline{\phantom z},-\overline{\phantom z}).
\]

A direct twistor-level lift exists.  Define an anti-linear map on \(\mathbb C^4\) by

\[
\Theta(Z_0,Z_1,Z_2,Z_3)
=
(i\overline Z_0,-i\overline Z_1,-i\overline Z_2,-i\overline Z_3).
\]

The phase factors are

\[
r_0=i,\qquad r_1=r_2=r_3=-i.
\]

Their pair products are exactly

\[
r_0r_1=r_0r_2=r_0r_3=+1,
\qquad
r_1r_2=r_1r_3=r_2r_3=-1.
\]

Therefore for every two-frame \((v_1,v_2)\),

\[
\boxed{
P(\Theta v_1,\Theta v_2)
=
G(P(v_1,v_2))
}
\]

where \(P\) is the six-component Plücker vector and \(G\) is the previously formalized googly exchange.

Also,

\[
\Theta^2=1,
\]

because each phase has unit modulus and
\(r_i\overline{r_i}=1\).  The map is antiunitary coordinatewise and conjugate-linear:

\[
\Theta(cZ)=\overline c\,\Theta(Z).
\]

This is stronger than the previous projective-quadric preservation theorem: the bivector googly operation now has an explicit origin on underlying twistor coordinates.

Verify2 candidate: `GppVerify/CelestialHolography/GooglyTwistorLift.lean`.

Important remaining distinction: this frame-level antiunitary lift is not yet a kernel-checked self-map of the `Gr24` subtype of complex submodules.  Descending an anti-linear map to complex subspaces requires packaging it as a suitable semilinear equivalence (complex conjugation automorphism) or proving directly that the image set is again a complex submodule of dimension two.  Once that is done, compare the resulting plane map with the existing Hermitian orthogonal-complement `shadow`; equality is not assumed.
