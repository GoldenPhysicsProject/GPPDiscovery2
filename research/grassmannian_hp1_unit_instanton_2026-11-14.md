# Quaternionic unit instanton in Gr₂(C⁴): what the U(2) boundary no-go does and does not exclude

**Discovery2 research result, 2026-11-14. Evidence:** complete elementary clutching and connection calculation, cross-checked by exact symbolic matrix arithmetic. Not yet Lean formalized or independently audited. This is the standard quaternionic Hopf/BPST geometry, applied here to the Shadow Framework's boundary obstruction.

## Statement

There is a canonical smooth embedding
\[
j:\mathbb H P^1\cong S^4\hookrightarrow\operatorname{Gr}_2(\mathbb C^4)
\]
defined by regarding a right quaternionic line in \(\mathbb H^2\) as a right \(\mathbb C_i\)-linear two-plane in \(\mathbb C_i^4\). If \(\mathcal S\) is the universal complex rank-two tautological bundle on the Grassmannian, then \(j^*\mathcal S\) is the quaternionic Hopf line bundle, viewed as a complex \(SU(2)\) bundle, and
\[
  |\langle c_2(j^*\mathcal S),[S^4]\rangle|=1.
\]
The induced tautological connection is the standard charge-one BPST instanton (self-duality sign depends on orientation).

This is **compatible** with the proved boundary statement: \(\mathcal S\) restricted to the graph Shilov boundary \(U(2)\) has a global frame and the canonical half-Maurer curvature there satisfies \(F\wedge F=0\). A trivialized boundary restriction may still be the clutching locus of a nontrivial bundle over the larger four-sphere.

## Explicit construction

Fix \(i\in\mathbb H\). Identify \(\mathbb H^2\) with \(\mathbb C_i^4\), respecting multiplication by \(\mathbb C_i\) on the right. A quaternionic line \([v]\in \mathbb HP^1\) is a 2-dimensional complex plane, defining \(j\).

Write \(q=a+bi+cj+dk\) and let its complex \(2\times2\) left-multiplication matrix be
\[
Q(q)=\begin{pmatrix}a+bi&c+di\\-c+di&a-bi\end{pmatrix},\qquad
Q^\dagger Q=|q|^2I,\qquad \det Q=|q|^2.
\]
On the affine quaternionic chart, put \(r=|q|\) and
\[
V_0(q)=\frac1{\sqrt{1+r^2}}\begin{pmatrix}I\\Q\end{pmatrix}.
\]
It is a global orthonormal complex rank-two frame over this *chart*, not over all \(S^4\).

On the infinity chart, \(q'=q^{-1}\), use
\[
V_\infty(q)=\frac1{\sqrt{1+r^{-2}}}\begin{pmatrix}Q^{-1}\\I\end{pmatrix}.
\]
On the overlap the transition function is
\[
V_\infty(q)=V_0(q)\,g(q)^{-1},\qquad
g(q)=Q(q)/r\in SU(2).
\]
Restrict to \(r=1\), the equatorial \(S^3\). Then \(g:S^3\to SU(2)\simeq S^3\) is the identity map of unit quaternions, with degree \(+1\) in compatible conventions. The clutching classification \(\pi_3(SU(2))\cong\mathbb Z\) gives \(|c_2|=1\).

The Grassmannian graph Shilov boundary is \(U(2)\), specified by \(Z^\dagger Z=I\) in the graph chart. On the quaternionic subspace \(Z=Q(q)\), this is exactly \(r=1\): its intersection with the \(S^4\) is the **\(S^3=SU(2)\) clutching equator**. Thus the three-dimensional boundary winding, not a four-form on \(U(2)\), records the ambient instanton.

## Curvature and Chern number

The induced unitary connection in the \(V_0\) gauge is
\[
A=V_0^\dagger dV_0
=\frac{Q^\dagger dQ-r\,dr\,I}{1+r^2}
=\frac{\operatorname{Im}(Q^\dagger dQ)}{1+r^2}\in\mathfrak{su}(2).
\]
Its curvature is the BPST field
\[
F=dA+A\wedge A
=\frac{dQ^\dagger\wedge dQ}{(1+r^2)^2}.
\]
With the orientation \(da\wedge db\wedge dc\wedge dd\) and the fundamental complex trace,
\[
\operatorname{tr}(F\wedge F)
=\frac{48}{(1+r^2)^4}\,da\wedge db\wedge dc\wedge dd.
\]
The radial integral is
\[
\int_{\mathbb R^4}\frac{d^4q}{(1+|q|^2)^4}
=2\pi^2\int_0^\infty\frac{r^3\,dr}{(1+r^2)^4}
=\frac{\pi^2}{6},
\]
and therefore
\[
\frac1{8\pi^2}\int_{S^4}\operatorname{tr}(F\wedge F)=1.
\]
For the standard Chern–Weil normalization of a trace-free anti-Hermitian rank-two connection, this is \(\langle c_2,[S^4]\rangle=1\) in the chosen orientation. The restriction to the \(S^3\) equator necessarily has \(F\wedge F=0\) (indeed any 4-form on \(S^3\) vanishes), but
\[
\frac1{24\pi^2}\int_{S^3}\operatorname{tr}[(g^{-1}dg)^3]=\pm1
\]
depending on trace/orientation convention. This is the topological transgression between local four-dimensional Chern density and three-dimensional boundary Chern–Simons/winding information.

**Independent symbolic spot-check:** the quaternionic matrix representation gives all six curvature components \(F_{\mu\nu}(0)=\partial_\mu Q^\dagger\partial_\nu Q-\partial_\nu Q^\dagger\partial_\mu Q\); summing pairwise wedge terms gives \(\operatorname{tr}(F\wedge F)(0)=48\,d^4q\). The closed formula \(F_{\mu\nu}(q)=F_{\mu\nu}(0)/(1+r^2)^2\) was checked at \(q=(1,2,3,4)\). The clutching proof independently fixes the integer without numerical integration.

## Implication and exact limit

- **Established:** the full Grassmannian carries a geometric \(SU(2)\) bundle whose canonical connection has nonzero second Chern number on an embedded \(S^4\). The earlier boundary \(F\wedge F=0\) no-go excludes the charge for the restricted \(U(2)\) connection, **not** for its ambient extension with nontrivial chart gluing. The boundary retains winding data on its \(SU(2)\) three-sphere.
- **Not established:** the physical electroweak gauge field equals this geometric connection, the full dynamical space of Yang–Mills connections is generated, fermion interactions or couplings are fixed, or \(SU(3)\) QCD instanton sectors follow. The earlier \(G_2/SU(3)=S^6\) pure-pullback \(c_2=0\) obstruction remains valid. The \(SU(2)\) instanton above is a different ambient construction.
- **Precise next physical obligation:** identify the relevant physical compactification/Euclidean cycle and construct a gauge-covariant bundle/connection functor that preserves the nontrivial clutching sectors *and* admits independent local \(\mathfrak{su}(2)\), \(\mathfrak{su}(3)\), and \(\mathfrak u(1)\) connection variations with kinetic dynamics. The HP¹ example is a topology benchmark, not a Standard Model derivation.

## References

The quaternionic Hopf bundle \(S^7\to S^4\), its principal \(Sp(1)=SU(2)\) structure, and the BPST connection are standard; see G. Naber, *Topology, Geometry and Gauge Fields*; J. Dittmann and O. Rudolph, *Journal of Geometry and Physics* 10 (1992/93), 93–...; and the mathematical discussion in *G₂-instantons on the 7-sphere* (J. London Math. Soc.). The present contribution is the explicit reconciliation with the Shilov \(U(2)\) result and the typed Grassmannian/physical-gauge distinction.

Related internal note: \`research/boundary_color_instanton_obstruction_2026-11-14.md\`. Related verified pointwise algebra: GPPVerify \`GppVerify/NoGo/BoundaryU2PontryaginDensity.lean\`.
