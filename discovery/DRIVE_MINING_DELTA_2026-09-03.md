# GPP Drive mining delta — 2026-09-03

This note records only new chronology/formalization consequences found after the 2026-09-02 pass. It does not revive superseded claims.

## 1. New chronology correction: what Gr(2,4) actually parametrizes

The June 4 googly manuscript (`toupin_googly_lmp_submission-1.pdf`) describes `Gr(2,4)` as the complexification of the space of null lines and uses that identification as part of a proposed route from Haar self-duality to celestial shadow symmetry.

That identification is not correct as stated.

The durable geometric statement is the one used in the later July `mass_orientation_coupling_v3.pdf`: the complex Grassmannian `Gr(2,4)` is the Klein/Grassmannian model of conformally compactified complexified Minkowski spacetime. A spacetime point corresponds to a projective twistor line `L_x ≅ CP^1` in `PT = CP^3`; the Grassmannian parametrizes those projective lines / 2-planes in `C^4`.

This distinction matters dimensionally and structurally:

- `Gr(2,4)` has complex dimension `2(4-2)=4`;
- the celestial sphere of null directions is `CP^1`, complex dimension 1;
- therefore `Gr(2,4)` cannot simply be the celestial sphere or the space of null directions.

The later July manuscript is the corrected provenance layer here. Its big-cell matrix coordinate `A` is a spacetime/2-plane coordinate, and the exact map

`tau(A) = (det A)^(-1) A epsilon`

should be interpreted first as Grassmannian/spacetime geometry. Any additional identification with a null-ray orientation, celestial shadow, CPT, or particle state is a separate dictionary theorem and must not be smuggled into the geometry.

## 2. Formalization audit: the old “Grassmannian Haar self-duality” theorem was not a Grassmannian theorem

`GppVerify/HaarSelfDuality.lean` contained a valid theorem:

- if `G` is a compact second-countable topological **group**,
- `mu` is Haar measure on `G`, and
- `phi : G ≃* G` is a bicontinuous group automorphism,

then `Measure.map phi mu = mu`.

The proof is mathematically sound.

But the legacy theorem `grassmannian_haar_self_duality` had exactly the same group hypotheses and merely re-exported the generic compact-group theorem while comments called it a `Gr(2,4)` instance. That interpretation is invalid: `Gr(2,4) = U(4)/(U(2)×U(2))` is a homogeneous space, not itself a group. A correct Grassmannian invariant-measure theorem needs the quotient/homogeneous-space action and its invariant probability measure, not the compact-group Haar theorem verbatim.

A second correction is coupled to this: inversion `g ↦ g^-1` is not a group automorphism on a general nonabelian group; it is an anti-automorphism. It becomes a multiplicative automorphism in the commutative case. This is why the separate idèle-class theorem in `RiemannHypothesis/HaarMeasure.lean` correctly assumes `CommGroup G`.

Formal action taken in Verify2:

- corrected `HaarSelfDuality.lean` documentation;
- retained the legacy theorem name for API stability;
- made explicit that it proves only compact-group automorphism invariance and does not instantiate `Gr(2,4)` or the celestial shadow transform.

Verify2 commit: `6466bab739a5a4a262e70e4422c74aa0b095a508`.

This changes no Lean term and therefore does not weaken any actual theorem; it removes a false interpretation from the verified surface.

## 3. Consequence for googly/shadow provenance

The June googly paper had three conceptually distinct steps compressed into one chain:

1. invariant measure / duality geometry on a Grassmannian;
2. the celestial shadow map `(Delta,J) -> (2-Delta,-J)`;
3. Wigner time reversal `T`.

The archive chronology now separates all three.

The later July mass-orientation manuscript gives the robust celestial statement directly:

`(h,hbar) -> (1-h,1-hbar)`, hence `Delta -> 2-Delta` and `J -> -J`,

with internal charge labels untouched.

Previous mining already established that ordinary Wigner `T` reverses both spin and momentum and therefore preserves helicity. Therefore the June identity `shadow = T` is not restored by the Haar argument; the underlying Grassmannian premise itself was also overstated.

The surviving research question is narrower and cleaner: construct a genuine equivariant map between the relevant Grassmannian/twistor duality and celestial shadow data. That requires a theorem on the homogeneous-space action and the induced representation, not merely uniqueness of Haar measure on a compact group.

## 4. Mass/time/charge orientation survives independently

Nothing in this correction damages the exact July orientation results already isolated:

- massive momentum as a sum of two null spinor squares;
- `det p = m^2` in the Hermitian bispinor representation;
- `tau^2 = -id`, `tau^4 = id` on the stated big-cell map;
- `charpoly(d tau_A)(t) = t^4 - (det A)^(-4)` after independent symbolic checking;
- rest-frame Dirac frequencies `omega_C = mc^2/hbar` and `omega_Z = 2mc^2/hbar`;
- celestial shadow flips the spin/helicity label while leaving internal charge labels untouched.

The orientation-representation quotient found in the companion July material also remains independent: for an oriented Wilson line, dualizing the representation and reversing the path give the same datum, and in the `U(1)` reduction the binary signs enter through the product `ct`.

Thus the durable mass-time-charge picture is an orientation/representation quotient plus a distinct Grassmannian `Z4` geometry. It is not a proof that shadow, Wigner `T`, charge conjugation, and proper-time reversal are the same operation.

## 5. Scaled versus scale invariant: a useful new geometric reading

The corrected Grassmannian interpretation makes the exact differential spectrum more informative:

`spec(d tau_A) = { zeta (det A)^(-1) : zeta^4 = 1 }`.

This decomposes the linearized action into two logically separate pieces:

- a discrete phase/orientation factor `zeta^4 = 1`;
- a homogeneous scale factor `(det A)^(-1)`.

On the unit-determinant locus the differential is pure `Z4` phase. Away from it there is a scale dilation as well. This is a precise instance of the archive's “scaled versus scale invariant” distinction: the fourth-root structure is scale-free only after fixing/removing the determinant magnitude; the general map is homogeneous rather than scale invariant.

This parallels the independently derived celestial scalar-box result, where scale independence occurs only on the zero-homogeneity locus `Delta_5 + Delta_6 = 2`.

No stronger physical identification of `det A` with a universal fermion mass is promoted without its dictionary hypotheses.

## 6. Bosonic versus fermionic structure

No new equality of bosonic and fermionic sectors emerged. The surviving common structure remains representation-theoretic:

- vector/spinor/cospinor triality in Spin(8) with equal quadratic Casimir in the checked normalization;
- spinorial double-cover / `2pi` sign and `4pi` closure;
- Grassmannian `Z4` orientation structure;
- possible real-versus-quaternionic antiunitary square classes.

These are comparison structures. They do not make a fermion “half a boson” and do not make equal Casimir eigenvalues a theorem of equal statistics or equal conformal weights.

## 7. SU(1)/SU(2)/SU(3)

No new archive evidence supports a nontrivial `SU(1)` gauge sector. The mathematically meaningful gauge sequence remains `U(1)`, `SU(2)`, `SU(3)` or a stabilizer/rank chain. Literal `SU(1)` is trivial.

The new Grassmannian correction reinforces a useful discipline here: do not infer a group structure merely because a homogeneous space is written as `G/H`. `Gr(2,4)=U(4)/(U(2)×U(2))` is exactly such a quotient and is not itself `U(4)` or another gauge group.

## 8. Arithmetic wave-particle / RH front

No new RH theorem was found beyond the v34 layer already isolated. The most concrete surviving arithmetic “wave-particle” structure remains:

- discrete prime-power atoms with von Mangoldt weights;
- Dirichlet/Fourier-Poisson oscillatory representations;
- the causal Dirichlet-heat boundary anomaly

`Tr(E_t V_a - V_a E_t) = a / sqrt(4 pi t) * exp(-a^2/(4t))`,

which after logarithmic prime translations yields the complete prime-power Gaussian term

`(4 pi t)^(-1/2) sum_{n>=2} Lambda(n)/sqrt(n) exp(-(log n)^2/(4t))`.

The remaining global obstruction is still the prime-Archimedean relative-trace cancellation and positivity / semilocal-Weil / Suzuki norm-square realization.

The Grassmannian correction is conceptually relevant here: both the arithmetic and celestial programs now have the same methodological rule — an invariant measure or formal symmetry is not enough. The missing theorem must identify the actual representation/operator on the actual space carrying the spectral data.

## 9. Axiom/stub and upgradeability consequences

The highest-value cleanup found today is not deletion of another `True := trivial` theorem but removal of a false verified interpretation:

- `HaarSelfDuality.lean` has zero new axioms and keeps its valid compact-group theorem;
- the purported `Gr(2,4)` specialization is now explicitly marked absent;
- a future formal Grassmannian result should be built through homogeneous-space invariant measure, not by coercing `Gr(2,4)` into `[Group G]`.

Stale repository documentation still exists outside the Lean source (`DependencyMap.md`, blueprint prose, root import comments, and the generated index) that describes `grassmannian_haar_self_duality` as a literal Grassmannian theorem and/or describes the corrected `CoreTheorems.lean` as proving physical googly/T statements. Those are documentation supersession targets, not mathematical dependencies, and should be corrected without changing theorem terms.

For Lean upgradeability this correction is favorable: the actual proof depends only on stable Mathlib Haar-measure interfaces for compact groups. The missing Grassmannian theorem should be introduced as a new, properly typed homogeneous-space layer rather than entangling it with the existing compact-group lemma.
