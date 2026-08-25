# Massive-vector three-polarization sewing: conserved-current reduction

Codex/GPT discovery track, 2026-08-26.

## Exact projector identity

For a four-dimensional massive cut momentum `L` with `L^2 = mu^2 > 0`, the sum over the three physical vector polarizations is

\[
\sum_{\lambda=1}^{3}\varepsilon^{(\lambda)}_\mu(L)\,
\varepsilon^{(\lambda)*}_\nu(L)
=
-\eta_{\mu\nu}+\frac{L_\mu L_\nu}{\mu^2}
\]

in mostly-minus conventions (with the overall sign adjusted in the opposite metric convention).

Let the two tree amplitudes on a two-particle cut expose the cut-vector polarization through currents `J_L` and `J_R`. The sewn state sum is therefore

\[
\mathcal S_V
=
J_L^\mu\left(-\eta_{\mu\nu}+\frac{L_\mu L_\nu}{\mu^2}\right)J_R^\nu
=
-J_L\!\cdot J_R
+\frac{(L\!\cdot J_L)(L\!\cdot J_R)}{\mu^2}.
\]

Hence, whenever the on-shell tree currents obey the Ward identities

\[
L\cdot J_L=0,
\qquad
L\cdot J_R=0,
\]

the longitudinal term vanishes exactly and the full three-polarization sum collapses to

\[
\boxed{\mathcal S_V=-J_L\cdot J_R.}
\]

This is not a high-energy or small-`mu` approximation: it is an exact consequence of the massive polarization completeness relation plus current conservation.

## Consequence for the `D_s=4`, nonzero-`mu` baseline

The previously established reconstruction is

\[
C^{(4)}(\mu)=C^{(V_m)}(\mu)-C^{(S)}(\mu).
\]

Therefore the massive-vector bottleneck can be attacked without constructing three explicit polarization vectors. For each cut line, keep the tree amplitude as a Lorentz current, contract the two sides with the massive projector, prove the relevant Ward identities, and then replace the projector by the metric contraction. Only after this contraction subtract the known real-scalar state.

For a two-particle cut with two internal massive vectors, the raw state sum contains two projectors,

\[
J_L^{\mu\nu}P_{\mu\rho}(L_1)P_{\nu\sigma}(L_2)J_R^{\rho\sigma},
\qquad
P_{\mu\nu}(L)=-\eta_{\mu\nu}+L_\mu L_\nu/\mu^2.
\]

If the tree tensor is transverse in each cut leg,

\[
L_{1\mu}J_L^{\mu\nu}=L_{2\nu}J_L^{\mu\nu}=0
\]

and similarly on the right tree, then both longitudinal pieces disappear and the three-by-three state sum reduces exactly to the double metric contraction

\[
\boxed{
J_L^{\mu\nu}\eta_{\mu\rho}\eta_{\nu\sigma}J_R^{\rho\sigma}
}
\]
(up to the two convention signs, which multiply to `+`).

## What remains to be proved for the MHV cut

The decisive next calculation is therefore not an explicit helicity-basis sum. It is:

1. construct the color-ordered two-massive-vector/two-gluon tree tensor entering the adjacent MHV cut;
2. verify transversality in each massive cut leg before imposing a polarization basis;
3. perform the double metric contraction;
4. subtract `C^(S)` to obtain the honest nonzero-`mu` `D_s=4` baseline;
5. restore general `D_s` through `C^(D_s)=C^(V_m)+(D_s-5)C^(S)`.

## Boundary / non-claim

The projector reduction is exact conditional on the required Ward identities for the tree tensor. This note does **not** yet claim that the particular massive-vector tree representation currently used in the project has been checked to satisfy those identities term by term, nor does it provide the final MHV numerator. Contact terms and any Goldstone/Stueckelberg representation used to realize the massive vector must be organized so that the complete on-shell tree tensor is transverse. The next executable check should test these Ward contractions explicitly before the numerator is promoted to Lean.