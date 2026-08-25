# Massive-vector three-polarization sewing: corrected 5D Ward reduction

Codex/GPT discovery track, 2026-08-26.

## Correction to the earlier shortcut

The earlier version of this note proposed reducing the massive projector by proving the four-dimensional transversality conditions

\[
p\cdot J_{4D}=0.
\]

That condition is **not generically true** for the four-dimensional massive vector obtained from a five-dimensional massless gauge field.  The executable audit in
`massive_vector_5d_ward_reconstruction.py` verifies the full five-dimensional Ward identity while finding nonzero four-dimensional longitudinal contractions.

Write the null five-dimensional cut momentum as

\[
K^A=(p^\mu,\kappa),\qquad K^2=0,\qquad p^2=\kappa^2=\mu^2.
\]

For a five-dimensional gauge current \(J^A=(J^\mu,J^5)\), the correct Ward identity is

\[
K_AJ^A=0
\quad\Longrightarrow\quad
p_\mu J^\mu=\kappa J^5
\]

in mostly-minus signature.  Thus the longitudinal part of the four-dimensional massive-vector completeness projector does **not** vanish.  Instead,

\[
\frac{(p\cdot J_L)(p\cdot J_R)}{\mu^2}
=J_L^5J_R^5
\]

when the same signed fifth momentum is used in the sewn orientation. Therefore

\[
\boxed{
-J_{L,4}\cdot J_{R,4}
+\frac{(p\cdot J_{L,4})(p\cdot J_{R,4})}{\mu^2}
=
-J_{L,4}\cdot J_{R,4}+J_L^5J_R^5
=
-J_{L,5D}\cdot J_{R,5D}.
}
\]

This is the correct exact reduction.  It is better than the discarded four-dimensional-current shortcut because it reconstructs the ordinary five-dimensional metric contraction directly from the three physical massive-vector states.

## Exact projector identity

For a four-dimensional massive cut momentum `p` with `p^2 = mu^2 > 0`, the sum over the three physical vector polarizations is

\[
\sum_{\lambda=1}^{3}\varepsilon^{(\lambda)}_\mu(p)\,
\varepsilon^{(\lambda)*}_\nu(p)
=
-\eta_{\mu\nu}+\frac{p_\mu p_\nu}{\mu^2}
\]

in mostly-minus conventions.

Hence for two exposed four-dimensional currents,

\[
\mathcal S_V
=
-J_{L,4}\!\cdot J_{R,4}
+\frac{(p\!\cdot J_{L,4})(p\!\cdot J_{R,4})}{\mu^2}.
\]

Using the five-dimensional Ward identities converts this exactly to

\[
\boxed{\mathcal S_V=-J_{L,5D}\cdot J_{R,5D}.}
\]

No high-energy or small-`mu` approximation is involved.

## Consequence for the `D_s=4`, nonzero-`mu` baseline

The previously established reconstruction remains

\[
C^{(4)}(\mu)=C^{(V_m)}(\mu)-C^{(S)}(\mu).
\]

The vector term `C^(V_m)` should therefore be calculated as the five-dimensional massless-vector sewing, with the fifth component retained. There is no need to construct an explicit three-polarization basis, but neither may the longitudinal projector contribution be dropped.

For a two-particle cut with two internal massive vectors, apply the same identity independently to each cut leg. The two four-dimensional massive projectors reconstruct two five-dimensional metric contractions once the complete five-dimensional tree tensor satisfies its Ward identities.

## What remains for the MHV cut

The decisive calculation is now:

1. construct the complete color-ordered five-dimensional four-gluon tree tensor with the two KK momenta corresponding to the massive cut legs;
2. verify the full five-dimensional Ward identities in each cut leg;
3. sew the two trees with the five-dimensional metric contractions;
4. interpret the result as the three-polarization four-dimensional massive-vector state sum;
5. subtract `C^(S)` to obtain the honest nonzero-`mu` `D_s=4` baseline;
6. restore general `D_s` through
   \[
   C^{(D_s)}=C^{(V_m)}+(D_s-5)C^{(S)}.
   \]

## Verified discovery evidence

`massive_vector_5d_ward_reconstruction.py` builds the complete color-ordered five-dimensional four-gluon tree from the cubic and quartic Yang-Mills vertices. On deterministic generic transverse states it verifies all four five-dimensional Ward replacements to floating-point residuals while explicitly finding nonzero `p.J_4D`. It also verifies

\[
p\cdot J_{4D}-\kappa J^5=0
\]

numerically.  This is discovery evidence for the tensor implementation and an exact algebraic guide; the final MHV cut numerator is not yet promoted to Lean.
