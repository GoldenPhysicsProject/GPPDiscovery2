# GPP Drive mining delta — 2026-08-30

This note records only new surviving mathematics, corrections, provenance, and formalization consequences found after the 2026-08-29 synthesis. It does not revive superseded confidence claims.

## 1. Charge, time orientation, and shadow separate more cleanly than before

A July 24 manuscript, `orientation_representation_quotient_v1`, supplies an exact gauge-theoretic structure that was not recorded in yesterday's synthesis.

For an oriented gauge line `gamma` carrying a representation `R`, path reversal and representation dualization obey

`U_R(gamma^{-1}) = U_R(gamma)^{-1}`

and

`U_{R*}(gamma) = U_R(gamma)^{-T}`.

For a closed Wilson line this gives the exact quotient relation

`W_{R*}(gamma) = W_R(gamma^{-1})`.

In the Abelian U(1) reduction, if `c = +/-1` is the charge-sign label relative to a chosen reference charge and `t = +/-1` is worldline orientation relative to a chosen arrow, the Wilson phase depends only on the product

`m = c t`.

The simultaneous inversion `(c,t) -> (-c,-t)` therefore leaves the oriented gauge datum invariant; among the four multiplicative binary characters `1,c,t,ct`, only `1` and `ct` descend to the quotient, so `ct` is the unique nontrivial binary character.

This materially sharpens the earlier orientation discussion:

- celestial shadow remains `(Delta,J) -> (2-Delta,-J)` and does not itself flip internal charge labels;
- fixed-arrow charge conjugation `R -> R*` changes the oriented-gauge quotient class;
- simultaneous representation dualization and worldline-orientation reversal preserves the oriented Wilson datum;
- proper-time/worldline orientation is not Wigner antiunitary time reversal `T`.

Hence the strongest surviving statement is not `shadow = C = T`. The exact structure is a commuting family of distinct reversals whose relations depend on which bundle/base orientation is reversed.

This also supplies a precise candidate meaning for the user's `mass-time-charge orientation` phrase: mass controls the coupling/clock between spinorial orientation components, while charge sign is relational to worldline orientation at the level of gauge transport. These are mathematically connected through orientation data but are not the same operation.

## 2. Bosonic versus fermionic structure: what is exact and what is not

The July `mass_orientation_coupling_v3` manuscript explicitly warns against identifying a fermion as half a boson. The exact representation-theoretic facts that survive are:

- null four-momenta admit spinor square roots via the double cover `SL(2,C) -> SO^+(3,1)`;
- spinorial states have the familiar sign under a `2 pi` rotation and close after `4 pi`;
- on the current Gr(2,4) big-cell map, `tau^2 = -id` and therefore `tau^4 = id` on the nondegenerate domain;
- tensoring two spin-1/2 representations gives integer-spin sectors `0 + 1`, not a statement that either constituent is literally half of a boson.

The useful boson/fermion research distinction is therefore representation type: ordinary/projective integer-spin representations versus spinorial double-cover representations, and more generally whether a lifted reversal/complex structure squares to `+1` or `-1`. No universal theorem equating that sign with all bosonic/fermionic sectors has been established in the archive.

## 3. Scaled versus scale invariant: the clean homogeneity statement

The August scalar-box v19 paper explicitly supersedes the v14-v18 shadow-residue mechanism. Its two-particle cut Mellin factor is

`Phi(Delta5,Delta6;M) = (1/8pi) (M/2)^(Delta5+Delta6-2) Gamma(Delta5)Gamma(Delta6)/Gamma(Delta5+Delta6)`.

Therefore the shadow pairing locus `Delta5 + Delta6 = 2` is exactly the zero-homogeneity locus with respect to the total scale `M`: the scale factor disappears there. It is not a residue-producing pole.

This gives a reusable formal principle: `scaled` versus `scale invariant` should be represented by an exact homogeneity degree. Mass/Compton data are scale-carrying; projective ratios and the shadow-paired cut are degree zero. This language can unify the scalar-box regulator, Mellin weights, and Grassmannian projective variables without claiming common dynamics.

## 4. Spectral weight provenance is now closed

The August `spectral_weight_v2` manuscript explicitly supersedes `haar_qg_paper_v2.1.5.1`. The weight

`P(lambda) = pi lambda / sinh(pi lambda)`

is not the scalar `SL(2,C)` Plancherel density and is not a replacement loop measure. Its exact origin is the phase-space Gamma factor on the shadow locus:

`Gamma(1+i lambda) Gamma(1-i lambda) = P(lambda)`.

It also has the exact Fourier pair

`P(lambda) <-> (1/4) sech^2(x/2)`

with the paper's Fourier normalization, and exact Planck-form identities. Thus the correct conceptual chain is

`two-particle phase space -> Mellin Gamma factor -> principal-series shadow locus -> P(lambda) -> sech^2 Fourier kernel`.

This is a genuine bridge among the celestial-cut and spectral-weight fronts. It should replace all older language that treated `P` as a fundamental Haar/Plancherel loop density.

## 5. Arithmetic wave-particle duality gets a second exact transform layer

The August arithmetic-principal-series v34 result already gave the causal Dirichlet-heat boundary anomaly

`Tr(E_t V_a - V_a E_t) = a / sqrt(4 pi t) * exp(-a^2/(4t))`

and, after logarithmic prime translations/resolvents,

`sum_p Tr[E_t,R_p] = 1/sqrt(4 pi t) sum_{n>=2} Lambda(n)/sqrt(n) exp(-(log n)^2/(4t))`.

Combining that with the current Verify2 convergence-half-plane identity gives two exact continuous representations of the same discrete prime-power data:

1. oscillatory/Fourier-Poisson response for `Re(s)>1`;
2. causal Gaussian heat-boundary response at logarithmic prime-power positions.

So `arithmetic wave-particle duality` can now be made precise as a transform family on the prime-power atomic measure, not merely an analogy. The RH-level step remains the completed prime-Archimedean relative trace / positive spectral representation. That boundary must remain explicit.

## 6. New stub-reduction target found in Verify2

Current `GppVerify/StandardModel/MassOrientationCoupling.lean` still contains

`theorem tau_pow_four_remark : True := trivial`

for the second clause of Theorem 3.3(i), despite `GppVerify/GrassmannianMass.lean` already proving

`transition_transition_eq_neg`

for every nonzero determinant. Applying that theorem to the negated tuple immediately yields the literal fourth-iterate identity, because

`(-a)(-d) - (-b)(-c) = ad - bc`.

Therefore this `True` marker is now mathematically retireable without any new axiom. The exact replacement should state the fourth transition explicitly and prove it by `simpa` from `transition_transition_eq_neg (-a) (-b) (-c) (-d)` with the inherited nonzero-determinant hypothesis.

The separate `differential_charpoly : True := trivial` in the same file is different: it should not be retired merely from `tau^4=id`. `GrassmannianJacobian.lean` proves the cleared Jacobian polynomial identity `N^4 = D^4 I`, but converting that to a complete characteristic-polynomial/eigenvalue theorem still requires the relevant matrix spectral machinery. Keep these two obligations separate.

## 7. SU(1), SU(2), SU(3): archive verdict

The old E8/GPM lineage contains `SU(3) x SU(2) x U(1)` gauge language, but no defensible literal `SU(1) -> SU(2) -> SU(3)` derivation was found. `SU(1)` is mathematically trivial. The only safe interpretations of a remembered `1,2,3` ladder are currently:

- `U(1), SU(2), SU(3)` as the Standard Model gauge factors;
- rank/dimension counts rather than special-unitary groups;
- a stabilizer/subgroup chain that must be stated explicitly if reconstructed.

Do not formalize an `SU(1)` gauge stage from historical prose.

## 8. Active-front consequences

- **Grassmannian / zitterbewegung:** retire the literal `tau^4` True marker; preserve the exact order-4 chart/orientation result.
- **Mass-time-charge orientation:** use the orientation-representation quotient for charge/worldline bookkeeping; keep Wigner `T` separate.
- **Celestial cuts:** treat `Delta5+Delta6=2` as exact scale invariance and `P(lambda)` as derived phase-space weight.
- **Spectral weight:** use the exact `P <-> sech^2/4` Fourier transform where useful; never call `P` the `SL(2,C)` Plancherel density.
- **RH / prime gas:** formalize the Dirichlet-heat translation commutator and von-Mangoldt anomaly as the next zero-independent causal transform target; do not revive finite-prime Koszul or bilateral-heat Tate homotopies.
- **Axiom/stub discipline:** distinguish theorem-level consequences already implied by existing Lean lemmas from genuinely new analytic/spectral work. `tau^4` is the former; the completed positive relative trace is the latter.
- **Upgradeability:** prefer small algebraic theorems derived from existing Mathlib/Verify2 lemmas over bespoke structures when retiring stubs, so future Lean upgrades have fewer custom dependencies.
