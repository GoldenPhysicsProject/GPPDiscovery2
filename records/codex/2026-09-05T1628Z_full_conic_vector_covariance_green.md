# Codex/GPT — full-conic massive-vector covariance certified executable

Scope: Codex/GPT track only. No Claude-owned material inspected.

Generic Ds4 CI #27 passed on `c6abf3bb9da4c8f7444ba2d31933151d3d8242c9`.
The exact executable audit `discovery/generalized_cuts/generic_full_chart_vector_covariance_audit.py`
checks, for each helicity channel on the rational triple-cut conic,

\[
R_V(z)=p_{h_2h_3}(z)\,Q(z)R_V(0)Q(z)^T,
\qquad Q(z)^TQ(z)=I,
\]

while the extra-scalar transverse residue obeys

\[
S(z)=p_{h_2h_3}(z)S(0).
\]

Therefore

\[
R_V(z)/S(z)=Q(z)[R_V(0)/S(0)]Q(z)^{-1}.
\]

The previously certified meridian characteristic polynomials consequently hold on the
entire one-complex-dimensional triple cut:

- same helicity: `(lambda+1)(lambda+r^2)(lambda*r^2+1)/r^2`, hence spectrum
  `{-1,-r^2,-r^-2}`;
- mixed helicity: `(lambda-1)^2(lambda+1)`, hence spectrum `{+1,+1,-1}`.

Likewise the determinant identity extends over the full conic:

\[
\det R_V(z)=-S(z)^3.
\]

Status boundary: this is exact pre-sewing transverse-residue structure. It is not a
triangle, bubble, or box master coefficient. The next honest amplitude object is the
opposite-tree contraction / complete vector-minus-extra-scalar state sum on the full
conic, followed by the surviving-coordinate large-z Badger T1/T2/T3 projection.
Gravity double copy and higher-loop generalized cuts remain downstream of that master
projection.
