# Massive-vector cut: Sym^2 little-group state-sum reduction

Codex/GPT discovery track, 2026-08-25.

The integer-dimensional reconstruction route reduces the nonzero-mu `D_s=4` gauge cut to a four-dimensional massive-vector cut minus one real adjoint-scalar cut.  The remaining vector sewing is finite-dimensional because a 4D massive spin-1 state transforms as `Sym^2` of the SU(2) massive little-group doublet.

For the parity-paired all-minus/all-plus massive-vector trees, isolate the two little-group bracket matrices

\[
A_{IJ}=\langle \ell_1^I\,\ell_2^J\rangle,
\qquad
B^{IJ}=[\ell_1^I\,\ell_2^J],
\]

with index placement/crossing fixed only after a definite all-outgoing massive-spinor convention is chosen.  The spin-one tree numerator is the symmetric square of the corresponding spin-one-half matrix.  Therefore the sum over the three physical vector states on the sewn pair is the trace of the induced endomorphism on `Sym^2(C^2)`.

For any 2 by 2 matrix `C`,

\[
\boxed{
\operatorname{Tr}_{\mathrm{Sym}^2}(C)
=\frac12\big[(\operatorname{tr}C)^2+\operatorname{tr}(C^2)\big]
=(\operatorname{tr}C)^2-\det C.
}
\]

The second equality is the 2 by 2 Cayley-Hamilton identity

\[
\operatorname{tr}(C^2)=(\operatorname{tr}C)^2-2\det C.
\]

Thus the full massive-vector polarization contraction is reduced to only two scalar little-group invariants, `tr C` and `det C`, with `C` the convention-correct product of the left and right bracket matrices.

This is useful for dimensional reconstruction because

\[
C^{(D_s=4)}(\mu)=C^{(V_m)}(\mu)-C^{(S)}(\mu),
\]

and the scalar contribution is already isolated.  The vector numerator no longer requires an explicit three-polarization basis; it requires only the Lorentz reduction of `tr C` and `det C`.

## Boundary

This note deliberately does not yet assert numerical Lorentz values for `tr C` or `det C`.  Those depend on the precise momentum-reversal and little-group index conventions for the two cut legs.  The next calculation is to fix one explicit massive-spinor convention, derive these two invariants from completeness, and audit the result in a center-of-mass frame before inserting it into the cut kernel.
