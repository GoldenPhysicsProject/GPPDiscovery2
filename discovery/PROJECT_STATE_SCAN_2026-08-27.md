# Codex project-state scan — 2026-08-27

This record reconstructs the active Golden Physics Project formalization state after thread splitting. Source of truth: `GPPVerify2/codex/lean-workbench`, `GPPDiscovery2/codex/discovery-workbench`, website `CODEX.md`, Codex Supabase records, and the Google Drive `GPP` research folder. Claude-tagged material was not inspected.

## Grassmannian / twistor / holographic chain

The live Verify2 branch already contains a genuine set-level `Gr24` type of complex 2-planes in `C^4`, orthogonal-complement `shadow : Gr24 -> Gr24`, involutivity/bijectivity, and projective Plucker frame covariance. `HolographicChain.lean` contains actual Hodge-star matrix algebra on `∧² C⁴`, explicit SD/ASD eigenvectors, Plucker relation, SD/ASD balance, Minkowski 2x2 Hermitian determinant, and Cayley-Dickson counting. Remaining genuine geometry includes the complex homogeneous-space/manifold/projective Grassmannian structure, descent of Plucker coordinates to an honest projective embedding, canonical `U(4)`-invariant measure on `Gr(2,4)`, and twistor incidence/Penrose-Ward/sheaf-cohomology infrastructure.

`TwistorGoogly.lean` has an exact celestial shadow/helicity theorem: shadow sends `(Delta,J)` to `(2-Delta,-J)` and exchanges graviton helicities ±2. The old identification of shadow with time reversal alone is not valid; time reversal preserves massless helicity. The remaining geometric bridge should identify the SD/ASD twistor exchange with the celestial shadow through the appropriate parity/CPT/reality structure, not by asserting `shadow = T`.

## Standard Model / quantum information

`StandardModel` contains exact algebraic modules for complementary pairs, Kappa shadow structure, Majorana conditions, mass-orientation coupling, Koide algebra, and related counting. The `HalfFlip.no_enactment` vacuous placeholder has already been replaced by the actual theorem that matrix transpose on `M_2(C)` is not completely positive, using the Choi/SWAP formalization in `QuantumInformation`.

During this scan, `ThreeGenerations.lean` still contained theorem-shaped vacuity (`3 = 3`, `True`). Verify2 commit `b86fa99a07c1d7a26d7aa9543c99322a5e5015de` retires those signatures. The file now proves the substantive conditional chain: if `c2 = kappa*c4`, `kappa>0`, and `c2=0`, then `c4=0`; with an explicit anomaly-counting hypothesis `c4=0 -> nGen=3`, one obtains `nGen=3`. This does not claim the QFT/celestial Link-6 input is formalized.

The next Standard Model target is to replace the remaining QFT theorem-shaped placeholders in `Link6.lean` (`Weinberg`, `Cachazo-Strominger`, `Capper-Duff`, `Adler-Bardeen` represented as `True`) by explicit mathematical interfaces and then formalize the actual OPE/anomaly calculations rather than leaving them as decorative theorems.

## Celestial cuts / amplitudes

The scalar-box regulator chain is closed through the structured mixed-log physical convergence theorem. Four-dimensional stripped MHV external numerator transfer is also formalized. This is not yet a full Yang-Mills amplitude theorem: coupling/color/global-phase and D-dimensional rational-state reconstruction remain separate. Gravity remains blocked by the honest four-uncut-propagator KLT angular/dispersion reduction; the scalar two-denominator regulator theorem cannot simply be reused.

Tree-loop topology for generalized cuts is already formalized. The analytic all-loop celestial gap is the inverse-Mellin shadow-pair sewing identity.

## RH / explicit formula / principal series

The branch contains the `Delta=2s` half-density/principal-series dictionary, critical-line unitarity/Hermitian shadow, completed-zeta shadow-odd response, positive-type Euler/von-Mangoldt half-plane kernels, Cutkosky-Weil operator compression, support-ladder infrastructure, and the RH-equivalent finite zero-pairing PSD endpoint.

The unresolved global theorem remains the genuine Mellin/Fourier/classical explicit-formula assembly identifying the local prime and Archimedean operators with the actual Weil quadratic form on an adequate test class and proving that global form positive unconditionally. If that closes all the way to the existing paired-form criterion, it is an RH proof and should be claimed as such.

## Prime-gas thermodynamics

The real Gibbs domain `beta>1` now includes exact partition/energy/entropy/free-energy identities, variance/Fisher positivity, strict antitonicity, positive third cumulant, and the cumulant derivative program. No sign statement is transported into the critical strip by analytic continuation.

## Spectral / Mehler-Fock / Wiener-Hopf

The shifted sech convolution has advanced beyond the earlier queue: the nonzero-parameter whole-line formula `2*lambda/sinh(pi*lambda)` is kernel-checked, with the lambda=0 removable value still to be proved separately in Lean. Gamma half-shift/modulus identities, collapsed Mehler-Fock weights, Wiener-Hopf factor/phase symmetry, and Gamma-Plancherel defect positivity are present. The old H-infinity inner-function interpretation remains retracted.

## Other top-level domains

Verify2 also contains active `GeneralRelativity`, `Cosmology`, `QuantumGravity`, `QuantumInformation`, and `NumberTheory` folders. These should be treated as first-class formalization fronts rather than ignored while RH/cuts are active. In particular, older high-level files must be audited for theorem-shaped placeholders, axioms standing in for physical derivations, and numerological identities that can now be replaced by genuine structures.

## Google Drive source corpus

The connected Google Drive `GPP` folder is part of the source corpus. Its root contains the `Everything` and `Verification Code` folders plus focused material including the Kerr two-twistor paper, GGC YM/QM/SM+cosmology/gravity papers, Riemann thermodynamics, Weil references, and historical proof drafts. The folder should be consulted for source derivations when promoting missing links. Claude-tagged files are excluded unless Daniel explicitly authorizes inspection.

## Immediate frontiers

1. Finish CI certification of the substantive `ThreeGenerations` stub retirement.
2. Replace incorrect/vacuous twistor-googly placeholders with exact conditional/geometric interfaces, beginning with removal of the `shadow = time reversal` framing and then genuine twistor incidence/Penrose-Ward structure.
3. Promote `Gr(2,4)` from set-level subspaces toward the homogeneous-space/projective Plucker object and canonical invariant measure.
4. Attack `Link6` QFT placeholders with explicit OPE/anomaly interfaces.
5. Continue the existing RH global explicit-formula/Weil transport, honest YM/gravity cut numerators, Gibbs cumulant geometry, and spectral closure in parallel.
