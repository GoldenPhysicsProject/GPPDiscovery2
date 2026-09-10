# Drive mining delta — 2026-09-10

## Scope and promotion rule

This pass focused on the Standard-Model/gauge branch of the time-layered GPP archive because it intersects several requested fronts at once: SU(1)/SU(2)/SU(3), bosonic versus fermionic structure, Grassmannian provenance, mass/orientation geometry, and upgradeability of the formal repository.

The comparison was between the older ONON Standard-Model-from-Grassmannian layer (ONON v14 through at least the integrated v19 line) and the later July 2026 correction `sm_shadow_closure_v1`. Only independently checkable mathematics from the repaired layer is promoted below.

## 1. Supersession: the direct Standard Model subgroup of SU(4) is impossible

The older ONON layer states

\[
SU(3)\times SU(2)\times U(1)\subset SU(4)
\]

and even displays a branching

\[
\mathbf4\to(\mathbf3,\mathbf1)_{1/3}\oplus(\mathbf1,\mathbf2)_{-1/2}.
\]

Both statements fail elementary checks.

First, compact connected subgroup rank cannot exceed ambient rank, while

\[
\operatorname{rank}SU(3)+\operatorname{rank}SU(2)+\operatorname{rank}U(1)
=2+1+1=4,
\]

but

\[
\operatorname{rank}SU(4)=3.
\]

Quotient by a finite central subgroup does not change rank, so even

\[
[SU(3)\times SU(2)\times U(1)]/\Gamma
\]

cannot inject as a connected compact subgroup of SU(4).

Second, the displayed defining-representation branching is dimensionally impossible:

\[
4\neq3+2.
\]

Therefore the old claims that bare Gr(2,4), through its SU(4) transitive symmetry, directly contains the Standard Model gauge product or directly derives the quark/lepton split must not be promoted.

The July `sm_shadow_closure_v1` manuscript explicitly identifies and repairs both errors. This is a genuine supersession in the archive, not merely a reinterpretation.

## 2. Surviving replacement: the minimal 2+3 rank-five stabilizer

Let V \cong C^4 be the twistor vector space and let

\[
L:=\det V=\Lambda^4V.
\]

After choosing the SU(V) volume structure, L is a one-dimensional trivial SU(V)-representation. Define

\[
E:=V\oplus L,
\qquad \dim_C E=5.
\]

For a Grassmannian plane \Lambda\in Gr(2,V), the Hermitian structure gives

\[
V=\Lambda\oplus\Lambda^\perp,
\]

hence

\[
E=\Lambda\oplus(\Lambda^\perp\oplus L),
\]

with block dimensions 2+3.

The determinant-one unitary block stabilizer is exactly

\[
S(U(2)\times U(3)).
\]

The standard map

\[
\Phi:SU(3)\times SU(2)\times U(1)\to S(U(3)\times U(2)),
\]

\[
\Phi(A,B,z)=\operatorname{diag}(z^{-2}A,z^3B)
\]

is surjective. Its kernel is determined by

\[
z^6=1,\qquad A=z^2I_3,\qquad B=z^{-3}I_2,
\]

so

\[
\ker\Phi\cong\mu_6\cong Z_6.
\]

Therefore

\[
\boxed{S(U(3)\times U(2))\cong
[SU(3)\times SU(2)\times U(1)]/Z_6.}
\]

I independently checked the determinant condition and kernel calculation. This is the correct global Standard Model group structure in the repaired branch.

Complex dimension five is also minimal for a faithful simultaneous 3+2 block realization simply because the two blocks require dimensions 3 and 2.

## 3. Hypercharge normalization survives exactly

A central traceless generator compatible with the 3+2 block has form

\[
Y=\operatorname{diag}(a,a,a,b,b),
\]

with

\[
3a+2b=0.
\]

Using the conventional minimal normalization gives

\[
\boxed{Y=\operatorname{diag}(-1/3,-1/3,-1/3,1/2,1/2),}
\]

unique up to overall sign once the normalization convention is fixed.

What is geometrically forced is the ratio

\[
a:b=-2:3,
\]

not the absolute normalization by itself.

## 4. Fermionic structure: the chiral 16 follows from exterior algebra

For the rank-five E, form

\[
W=E\oplus E^*.
\]

The Clifford algebra acts on the fermionic Fock space \Lambda^\bullet E by wedge and contraction, and chirality is exterior parity. Thus

\[
S^+=\Lambda^{\mathrm{even}}E
=\Lambda^0E\oplus\Lambda^2E\oplus\Lambda^4E,
\]

with

\[
\dim_C S^+=1+10+5=16.
\]

Let E=A\oplus B with dim A=3, dim B=2 and

\[
Y_A=-1/3,\qquad Y_B=1/2.
\]

Then

\[
\Lambda^2E=\Lambda^2A\oplus(A\otimes B)\oplus\Lambda^2B
\]

and, since det E is trivial on the determinant-one subgroup,

\[
\Lambda^4E\simeq E^*=A^*\oplus B^*.
\]

The resulting representation is

\[
\boxed{
(3,2)_{1/6}\oplus(\bar3,1)_{-2/3}\oplus(\bar3,1)_{1/3}
\oplus(1,2)_{-1/2}\oplus(1,1)_1\oplus(1,1)_0.}
\]

This is exactly one Standard Model generation in left-handed notation, including a sterile right-handed neutrino.

The hypercharges follow directly by addition under exterior products:

* A\otimes B: -1/3+1/2=1/6;
* \Lambda^2A: -2/3;
* \Lambda^2B: +1;
* A^*: +1/3;
* B^*: -1/2;
* \Lambda^0E: 0.

This is the strongest surviving boson/fermion link from this branch: the gauge group comes from a unitary block stabilizer, while a fermion generation comes from the chiral exterior/Clifford module. It does not derive three generations.

## 5. Anomaly cancellation is exact

For the representation above, the manuscript gives and I independently checked the standard anomaly sums:

\[
A_{SU(3)^3}=2-1-1=0,
\]

\[
A_{SU(3)^2Y}
=2(1/6)(1/2)-(2/3)(1/2)+(1/3)(1/2)=0,
\]

\[
A_{SU(2)^2Y}
=3(1/6)(1/2)-(1/2)(1/2)=0,
\]

\[
6(1/6)+3(-2/3)+3(1/3)+2(-1/2)+1=0,
\]

and

\[
6(1/6)^3+3(-2/3)^3+3(1/3)^3+2(-1/2)^3+1=0.
\]

There are four left-handed SU(2) doublets counting color multiplicity, so the Witten SU(2) global anomaly parity is even.

Thus the one-generation representation content and its anomaly cancellation survive independently of the older false SU(4) embedding.

## 6. SU(1), SU(2), SU(3): corrected status

Nothing in this branch gives a nontrivial role to SU(1); SU(1) is the trivial group.

The archive must distinguish three structures:

1. the physical internal gauge product (globally quotient-corrected)
   \[
   [SU(3)\times SU(2)\times U(1)]/Z_6;
   \]
2. the spacetime/twistor transitive group SU(4) acting on Gr(2,4), which is not the Standard Model gauge group;
3. nested exceptional/stabilizer chains such as Spin(8) -> G2 -> SU(3) -> ... , which do not preserve earlier factors as simultaneous gauge factors merely because they are nested.

This separation prevents the recurring mistake of reading a nested subgroup chain as a direct-product gauge decomposition.

## 7. Exact Grassmannian shadow half-split survives and is separate from gauge completion

On the compact Grassmannian

\[
X=Gr(2,4)=U(4)/(U(2)\times U(2)),
\]

let

\[
J(\Lambda)=\Lambda^\perp.
\]

For a fixed reference plane \Lambda_0 with projector P_0, define

\[
f_{\Lambda_0}(\Lambda)=\operatorname{tr}(P_\Lambda P_0)-1.
\]

Because

\[
P_{\Lambda^\perp}=I-P_\Lambda,
\qquad \operatorname{tr}P_0=2,
\]

one has exactly

\[
\boxed{f(J\Lambda)=-f(\Lambda).}
\]

J preserves the normalized invariant measure, and the zero set of the nonconstant real-analytic f has measure zero. Therefore

\[
\boxed{\mu(f>0)=\mu(f<0)=1/2.}
\]

Also U(4)-invariance forces

\[
\boxed{\mathbb E_\mu[P_\Lambda]=\tfrac12I.}
\]

This is an exact geometric half-split. It does not imply equal matter/antimatter abundance unless a physical state is additionally invariant under the corresponding lifted involution.

This result is a better replacement for earlier vague “Grassmannian Haar self-duality gives equal sectors” language because the measurable sectors and the odd function are explicit.

## 8. Relation to mass-time-charge orientation

The later repaired paper lifts the label map as

\[
\Theta(\Lambda,\gamma,R)
=(\Lambda^\perp,\gamma^{-1},R^*).
\]

At label level

\[
\Theta^2=id
\]

using complement twice, path inversion twice, and R** ~= R.

This is compatible with the independently surviving orientation-representation quotient

\[
(\gamma,R)\sim(\gamma^{-1},R^*)
\]

and its U(1) invariant ct.

The exact conceptual connection is therefore a product of three involutive label dualities. This still does not identify celestial shadow, Wigner T, charge conjugation, path reversal, or the Grassmannian complement as the same operator on one Hilbert space. An intertwiner/state implementation remains separate data.

## 9. Formalization and upgradeability consequences

Current Verify2 code search did not reveal a formal implementation of the repaired S(U(3)xU(2)) / Z6 stabilizer, chiral-16 decomposition, or anomaly sums. This makes the July correction unusually attractive as an upgradeability target because most of its core can be formalized without deep analytic infrastructure.

Recommended decomposition:

1. elementary rank obstruction `4 > 3` as a bookkeeping theorem attached to the Lie-rank assumptions rather than as a fake proof of the general compact subgroup theorem;
2. finite-dimensional block determinant and hypercharge arithmetic;
3. exterior-dimension identities 1+10+5=16;
4. exact charge-addition table producing the six Standard Model representations;
5. anomaly rational-arithmetic identities;
6. separately, a homogeneous-space/invariant-measure formalization of the explicit complement-odd half-split.

The first five are low-dependency formal targets and could replace or prevent several vacuous Standard-Model numerology statements elsewhere in the repository. The sixth connects directly to the active Grassmannian/Haar upgradeability front.

## 10. Promotion ledger

Promote:

* rank obstruction to SM gauge product embedding in SU(4);
* impossibility of the old 4 -> 3+2 branching;
* minimal rank-five 2+3 block stabilizer S(U(3)xU(2));
* quotient isomorphism with [SU(3)xSU(2)xU(1)]/Z6;
* hypercharge ratio and conventional normalized generator;
* chiral exterior module dimension 16 and one-generation branching;
* explicit anomaly cancellation;
* exact Grassmannian complement-odd 1/2 measure split;
* orientation/representation/complement product involution at the label level.

Do not promote:

* SU(3)xSU(2)xU(1) as a subgroup of SU(4);
* 4 -> 3+2 branching;
* bare Gr(2,4) as a derivation of the Standard Model gauge product;
* the number of colors as derived merely from `dim Gr(2,4)`;
* exactly three generations from Schubert cells or Spin(8) triality alone;
* equal physical abundance from invariant measure alone;
* any identification of the label involution with Wigner T or celestial shadow without an explicit intertwiner.

## Cross-front consequence

This correction clarifies the architecture rather than adding another speculative unification:

\[
\text{Gr(2,4) spacetime geometry}
\longrightarrow
\text{2+3 completed internal fibre}
\longrightarrow
S(U(3)\times U(2))
\longrightarrow
\Lambda^{even}E\;\text{fermion generation},
\]

while

\[
\Lambda\mapsto\Lambda^\perp
\]

remains an independent geometric involution with an exact 1/2 invariant-measure split. The corrected architecture therefore separates spacetime symmetry, internal gauge symmetry, fermionic Fock structure, and shadow/orientation symmetry instead of deriving all four from one SU(4) identification.
