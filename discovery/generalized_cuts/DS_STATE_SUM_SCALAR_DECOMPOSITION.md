# D_s-dimensional gluon state sum as 4D helicities plus adjoint scalars

Codex/GPT discovery track, 2026-08-25.

For a massless internal gauge boson whose spin states live in `D_s` dimensions, the physical polarization space has dimension

\[
D_s-2.
\]

Choose the external kinematics and the four-dimensional component of each cut momentum in a fixed 4D subspace. The polarization space then splits orthogonally into

\[
(D_s-2)=2+(D_s-4),
\]

namely the two ordinary four-dimensional helicities and `D_s-4` transverse polarization directions. Each transverse polarization couples to four-dimensional gluons exactly as an adjoint scalar species.

Therefore a two-particle cut state trace decomposes as

\[
\boxed{
C^{(D_s)}=C^{(4\mathrm{D\ helicity})}+(D_s-4)\,C^{(\mathrm{one\ real\ adjoint\ scalar})}.
}
\]

The coefficient is `D_s-4`, not `(D_s-4)^2`, because the scalar flavour index is transported across the cut and traced once: the two cut legs carry the same extra-dimensional species around the loop.

If the scalar-tree convention packages two real adjoint scalars into one complex scalar, then

\[
C^{(D_s)}=C^{(4\mathrm{D\ helicity})}+\frac{D_s-4}{2}\,C^{(\mathrm{one\ complex\ adjoint\ scalar})}.
\]

This convention distinction must be fixed before numerical amplitude coefficients are quoted.

The loop momentum dimension `D=4-2\epsilon` and spin dimension `D_s` are conceptually separate. The decomposition above concerns the state sum. The already-isolated massive scalar sector arises because a D-dimensional loop momentum obeys

\[
L=\ell+L_\perp,\qquad \ell^2=\mu^2,
\]

and therefore the scalar trees carry the non-four-dimensional numerator information, including the MHV box term

\[
C_s^{\rm scalar}\propto \mu^4.
\]

Thus the honest D-dimensional sewing problem factorizes into two interfaces:

1. the spin-state trace, controlled by `D_s-4` scalar species;
2. the transverse loop-momentum dependence, controlled by the massive four-dimensional scalar trees and powers of `mu^2`.

For the 't Hooft-Veltman choice `D_s=D=4-2\epsilon`, the scalar-state multiplicity is analytically `-2\epsilon`. For schemes with `D_s=4`, there are no extra spin polarizations, but D-dimensional loop momentum can still generate `mu^2` dependence; therefore setting `D_s=4` is not the same as setting `mu=0`.

Boundary: this note fixes the state-counting structure only. It does not yet determine the exact external helicity factor `Xi`, scalar real/complex normalization used by every tree convention, triangle/bubble subtraction coefficients, or the integrated pure-Yang--Mills rational remainder.
