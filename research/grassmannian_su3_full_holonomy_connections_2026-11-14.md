# Full SU(3) holonomy in every Grassmannian-derived bundle class on S4

**Mathematical construction.** 2026-11-14. Source: the HP1/S4 quaternionic tautological bundle, its SU(3) extension, and standard connection/holonomy theory. This note is a paper-level result; no Lean formalization is claimed.

## Statement

Let \(\mathcal S\to \mathrm{Gr}_2(\mathbb C^4)\) be the tautological complex rank-two bundle and \(j:\mathbb HP^1\simeq S^4\hookrightarrow\mathrm{Gr}_2(\mathbb C^4)\) the quaternionic-line embedding. For each integer \(k\), choose a smooth map \(f_k:S^4\to\mathbb HP^1\) of degree \(k\) (with compatible choices of orientations), and put
\[
E_{3,k}=(j\circ f_k)^*\mathcal S\oplus\underline{\mathbb C}.
\]
This has its natural SU(3) structure with \(c_1=0\) and \( \langle c_2(E_{3,k}),[S^4]\rangle=k\) in the chosen convention. The family represents all principal SU(3) bundle classes over \(S^4\).

**Proposition.** Every \(E_{3,k}\) has smooth SU(3) connections with full restricted holonomy group SU(3), even though \(E_{3,k}\) admits an SU(2) structure-group reduction. These connections are not constrained to preserve that reduction. The space of connections is the affine space
\[
\operatorname{Conn}(P_k)=A^{(0)}+\Omega^1(S^4,\operatorname{ad}P_k),
\]
and changing \(A\) leaves the topological class \(c_2=k\) unchanged. The result constructs independent local \(\mathfrak{su}(3)\) connection variables on the fixed topological bundle, but does not derive a dynamical Yang--Mills field theory from the Grassmannian.

## Construction and proof

The topological classification is the clutching calculation already established in \`grassmannian_hp1_unit_instanton_2026-11-14.md\`: \(SU(2)\to SU(3)\to S^5\) gives \(\pi_3(SU(2))\cong\pi_3(SU(3))=\mathbb Z\); the extension \(\mathcal S\oplus\mathbb C\) preserves \(c_2\); degree-\(k\) maps supply all integers.

Any smooth principal SU(3) bundle over the compact smooth base admits a connection \(A^{(0)}\). The difference of two connections is a global adjoint-valued one-form. On overlapping local trivializations related by \(g_{\alpha\beta}\), the connection one-forms obey
\[
A_\beta=g_{\alpha\beta} A_\alpha g_{\alpha\beta}^{-1}
           +g_{\alpha\beta}\,d g_{\alpha\beta}^{-1},
\qquad
a_\beta=g_{\alpha\beta}a_\alpha g_{\alpha\beta}^{-1}.
\]
In particular, any smooth adjoint-valued one-form supported strictly inside one coordinate ball extends by zero to a global connection perturbation. This works in all topological sectors.

We now construct a connection with full SU(3) holonomy, not merely formal local freedom. Let \(E_{ij}\) be the standard matrix units and take the explicitly skew-Hermitian trace-free matrices
\[
X=i\,\mathrm{diag}(1,2,-3),\qquad
Y=i(E_{12}+E_{21}+E_{23}+E_{32}).
\]
**Lemma.** \(X,Y\) generate all of \(\mathfrak{su}(3)\) under real linear combinations and Lie brackets.

Indeed, writing \(Y=Y_{12}+Y_{23}\) for its two simple-root contributions,
\[
(\operatorname{ad}X)^2Y_{12}=-Y_{12},\qquad
(\operatorname{ad}X)^2Y_{23}=-25Y_{23}.
\]
Thus both \(Y_{12}\) and \(Y_{23}\) are real linear combinations of \(Y\) and \((\operatorname{ad}X)^2Y\). Commuting each with \(X\) produces the corresponding antisymmetric simple-root matrices. Their brackets produce the 13-root matrices, and each root pair generates a diagonal Cartan direction. These eight independent matrices span \(\mathfrak{su}(3)\).

Pick a small trivializing 4-ball centered at \(p\), with real coordinates \(x^1,\ldots,x^4\) and \(x(p)=0\). In an even smaller ball, choose the local connection
\[
A=X\,x^1 dx^2+Y\,x^3 dx^4.
\]
Glue this to an arbitrary background connection through a smooth cutoff supported in the larger ball; the affine connection law ensures the result is a global connection on \(P_k\). At \(p\), \(A(p)=0\), so its curvature satisfies
\[
F_A(p)(\partial_1,\partial_2)=X,\qquad
F_A(p)(\partial_3,\partial_4)=Y.
\]
The Ambrose--Singer holonomy theorem puts these curvature values in the restricted holonomy Lie algebra. This algebra contains \(X,Y\), so it contains their full Lie closure \(\mathfrak{su}(3)\). Being a subalgebra of \(\mathfrak{su}(3)\), it equals \(\mathfrak{su}(3)\), and the connected restricted holonomy group is SU(3). This proves the proposition for every \(k\).

## Topology survives genuine connection fluctuations

For \(A_t=A+t a\), define \(F_t=F_A+t d_Aa+t^2 a\wedge a\). The Bianchi identity and invariance of trace give
\[
\frac{d}{dt}\mathrm{tr}(F_t\wedge F_t)
=2\,d\,\mathrm{tr}(a\wedge F_t).
\]
Integrating \(t\) from 0 to 1 yields the **exact Chern--Weil transgression**
\[
\mathrm{tr}(F_{A+a}\wedge F_{A+a})-\mathrm{tr}(F_A\wedge F_A)
=d\left[
2\mathrm{tr}(a\wedge F_A)
+\mathrm{tr}(a\wedge d_Aa)
+\frac23\mathrm{tr}(a\wedge a\wedge a)
\right].
\]
On closed \(S^4\) the integral of the right side is zero, hence \(c_2(P_k)=k\) is unchanged by all independent connection variations. A full-holonomy connection is therefore compatible with the same bundle that arose via SU(2) block extension from the Grassmannian.

With an **additional** Euclidean metric and the **separately specified** positive Yang--Mills action
\[
S_{\mathrm{YM}}(A)=
-\frac{1}{2g^2}\int_{S^4}\mathrm{tr}(F_A\wedge *F_A),
\]
variations give the Yang--Mills equation \(d_A *F_A=0\). This is a conventional dynamical choice, not something established by the topological result.

## Relevance and limits

This settles a narrow but important mathematical concern: extending an SU(2) Grassmannian bundle to SU(3) does **not** confine all possible connections to an embedded SU(2). Full SU(3) local curvature and holonomy are available in *every* instanton sector \(k\). The earlier pure \(G_2/SU(3)=S^6\) pullback obstruction concerns a different construction and still holds.

This does **not** derive the physical color gauge group, the Yang--Mills action or coupling, a local gauge principle from the Shadow Framework, matter representations/chirality, quantum existence, confinement, or a mass gap. It makes the next missing step precise: specify a physical principle selecting the independent connection degrees of freedom and their dynamics, then a bulk--boundary functor that relates them to actual celestial observables.

**Exact symbolic check:** \`experiments/su3_holonomy_generation_check.py\` verifies \(\mathfrak{su}(3)\) Lie closure dimensions \(2,3,5,8\) using exact SymPy arithmetic. The mathematical proof above is independent of the computation.

**Verification status:** mathematical derivation and exact symbolic check, pending independent Turbo/Claude audit; not Lean certified.
