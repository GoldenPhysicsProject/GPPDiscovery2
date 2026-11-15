# Four-dimensional gauge action and WWIF orientation doubling: exact conditional identities

**Shadow Framework / Discovery 2 research note (2026-11-14).** Mathematical statement about classical gauge theory, not a derivation of WWIF spacetime or of quantum Yang--Mills. This supplements \`grassmannian_su3_full_holonomy_connections_2026-11-14.md\`.

## 1. What local symmetry determines

Let \(M\) be an oriented Riemannian four-manifold and \(P\to M\) a principal \(SU(3)\)-bundle. Let \(A\) be any independent connection with curvature \(F_A\in\Omega^2(M,\operatorname{ad}P)\).

**Conditional classification.** Assume the local gauge-field Lagrangian is (i) invariant under local SU(3) gauge transformations and orientation-preserving orthonormal frame changes, (ii) a metric-dependent polynomial **quadratic in curvature** \(F_A\), (iii) built without additional matter fields, background tensors or derivatives of curvature. Then, at each point, all invariant terms are real linear combinations of
\[
-\operatorname{tr}(F_A\wedge *_g F_A)
\quad\text{and}\quad
\operatorname{tr}(F_A\wedge F_A).
\]
For simple \(\mathfrak{su}(3)\) the invariant symmetric Lie-algebra pairing is unique up to scale. In four Euclidean dimensions \(\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-\), and an \(SO(4)\)-invariant quadratic pairing has one coefficient on each irreducible summand. Equivalently, the two basis terms are the metric energy and the orientation-odd Pontryagin density. This proves the classification under the stated hypotheses; higher-derivative, nonpolynomial, matter-dependent or curvature-dependent couplings are outside its scope.

Thus the standard candidate action has two coefficients:
\[
S(A)=\frac{1}{2g^2}\int_M-\operatorname{tr}(F_A\wedge *_gF_A)
+\frac{\theta}{8\pi^2}\int_M\operatorname{tr}(F_A\wedge F_A).
\]
In a Euclidean path integral the topological contribution is normally written with an additional factor \(i\); the displayed real action is only a convenient bookkeeping of classical invariants. The second term is constant under smooth variations of \(A\) on a closed \(M\), so it does not alter the local Yang--Mills Euler--Lagrange equation \(d_A *_g F_A=0\).

The kinetic density is conformally invariant in exactly four dimensions: for \(g'=\Omega^2g\), the Hodge star on \(p\)-forms scales as \(*_{g'}=\Omega^{4-2p}*_g\), hence \(*\) on two-forms is unchanged. Neither classical conformal invariance nor the uniqueness classification determines \(g\) or its quantum running.

## 2. Exact cancellation/addition for an orientation-reversed pair

Write \(\bar M\) for the same smooth four-manifold with *opposite orientation* but the same Riemannian metric \(g\), and use the same underlying \(P,A\) data under the identity map. The oriented integration functional changes sign:
\[
\int_{\bar M}\alpha=-\int_M\alpha
\quad\text{for four-forms }\alpha.
\]
The orientation-defined Hodge star changes sign, including on two-forms:
\[
*_{\bar M}\beta=-*_M\beta.
\]
Therefore the quadratic energy **adds**, while the signed second Chern number **cancels**:
\[
\int_{\bar M}-\operatorname{tr}(F_A\wedge *_{\bar M}F_A)
=\int_M-\operatorname{tr}(F_A\wedge *_M F_A),
\]
\[
Q(\bar M,P,A)
=\frac{1}{8\pi^2}\int_{\bar M}\operatorname{tr}(F_A\wedge F_A)
=-Q(M,P,A).
\]
In particular for any \(k\in\mathbb Z\) represented by the Grassmannian-derived \(SU(3)\) bundles on \(S^4\), the paired data \((S^4,P_k,A)\sqcup(\overline{S^4},P_k,A)\) have \(Q_{\rm total}=k-k=0\), but \(E_{\rm total}=2E\), not zero.

This is an **orientation-pair identity**. It does not presume that WWIF's sector labels \((q,t)\sim(-q,-t)\) actually identify such oriented manifolds, nor that the physical pair contains a second independent vacuum sector. Establishing such a physical realization requires a separate bundle/state-space map, a genuine orientation-reversing relation on the gauge field, and a correctly normalized physical action.

## 3. Why this does not solve the strong CP problem

Cancellation of \(\int F\wedge F\) in the total two-sector action does not force the effective theta angle of **one observed sector** to vanish. If the sectors are dynamically decoupled, local CP-odd observables may remain nonzero, regardless of the cancellation of global topological charges. The orientation argument by itself also does not distinguish \(\theta=0\) from other symmetry-compatible values such as \(\pi\) modulo \(2\pi\) in quantum theories. A physical cross-sector coupling and observable algebra would need to be constructed before attributing a CP solution to WWIF.

## 4. What is gained

The HP1/Grassmannian construction supplies every topological \(SU(3)\) class over \(S^4\). The independent connection construction supplies full local non-Abelian curvature/holonomy in each class. The conditional invariant classification fixes the familiar two-term four-dimensional local quadratic action once a metric and gauge principle are supplied. The orientation doublet is then mathematically capable of retaining positive gauge kinetic energy while cancelling an orientation-odd topological charge.

The unproved physical bridge is the derivation of the independent SU(3) bundle, gauge principle, matter representation, metric, action coefficient, and orientation-doublet identification from the Shadow Framework / WWIF. None follows automatically from Haar invariance, Grassmannian topology, or the sign identity.

**Conventional references:** E. Frenkel, *Gauge theory and Langlands duality*, Bourbaki seminar (https://math.berkeley.edu/~frenkel/bourbaki-gauge.pdf); standard Chern--Weil theory and 4D SO(4) decomposition. These external facts are used as standard mathematical background, not claimed as original discoveries.

**Status:** exact conditional classical result, paper level; no new Lean certification, no Yang--Mills quantum existence/mass-gap claim.
