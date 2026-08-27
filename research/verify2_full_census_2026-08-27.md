# GPPVerify2 full project census — 2026-08-27

Branch audited: `codex/lean-workbench`.

This census was performed folder-by-folder from the Git tree before resuming theorem work. It is a map of what is actually present, not a claim that every imported physics interpretation is unconditional.

## Top-level formalization islands

- `CelestialHolography/`: largest amplitude/celestial/twistor island. Contains the regulated scalar-box analytic chain, physical regulator convergence, external numerator transfer, dispersion reconstruction, tree-loop sewing combinatorics, D-dimensional radial integrals and dimension-shift algebra, four-point Yang–Mills/gravity rational algebra, principal-series/shadow files, Mehler–Fock weights, exact sech/Wiener–Hopf convolution, and the Gr(2,4)/Plücker/googly projective-shadow development.
- `RiemannHypothesis/`: largest arithmetic/spectral island. Contains adelic and p-adic Haar infrastructure, completed-zeta symmetry/response, global von Mangoldt and prime Poisson positive type, finite and global Weil-positivity infrastructure, Cutkosky–Weil local kernels, Yakaboylu kernels, the finite zero paired-form criterion equivalent to RH, extensive Gibbs thermodynamics/information geometry, and several alternate spectral/heat-trace criteria.
- `QuantumGravity/`: Gamma/Mehler–Fock/spectral-rho recurrence and chamber identities, Wiener–Hopf factors, local shadow kernels, thermal/Planck integrals, and several larger physics packages (`AllLoopFiniteness`, `WightmanAxioms`) that require separate dependency audits before physical promotion.
- `NumberTheory/`: finite/corrective arithmetic results (BSD point-count data, Euler sums, Gauss sums, zeta negative integers, Weyl Casimir, E8/perfect-number facts, Zagier recurrence correction, etc.).
- `StandardModel/`: complementary-pair combinatorics, Majorana/half-flip algebra, Koide phase identity, mass-orientation coupling, DM abundance, three-generation package. Some interpretations remain linked to open/axiomatized Link 6 input.
- `QuantumInformation/`: finite-dimensional Choi/SWAP/transpose-not-CP core. This is one of the cleanest self-contained islands.
- `Cosmology/`: Abel halo pair, dark energy, gamma-ratio dark matter, unified dipole.
- `GeneralRelativity/`: one `Rigidity.lean` module.
- `StringTheory/`: one `DivisionAlgebras.lean` module.
- `YangMills/`: one `MassGap.lean` module; importantly, the honest modern cut/amplitude work is mostly in `CelestialHolography/`, not this folder.
- `ThreadWeilParity/`: separate substantial spectral-parity/ground-order thread (`CrossResolvent`, `OddEigenpairLift`, `StrictParityInterlacing`, etc.).
- `ThreadWeilSemibound/`: one localized ground-order theorem.
- `ThreadS/`: signature-inertia theorem plus reconstruction/source notes.
- `ThreadHT/`: arithmetic-principal-series survey markdown rather than a Lean theorem island.

Root standalone modules include `CoreTheorems`, `HaarSelfDuality`, `GrassmannianMass`, `GrassmannianJacobian`, and `RHSpectralMultiplicity`.

## Important dependency boundaries found in the root aggregate

`GppVerify.lean` is a useful aggregate but a green root build must not be read as saying every physical interpretation is unconditional. The root comments themselves record these boundaries:

1. `Link6.lean` is formalized using physics axioms; downstream three-generation statements depending on Link 6 remain conditional/open at that bridge.
2. `TreeLoopSewing.lean` proves the graph-theoretic cycle-rank sewing theorem for all loop orders, but the analytic celestial sewing identity remains a local hypothesis and does not discharge the older shadow-discontinuity amplitude stubs.
3. `DispersionReconstruction.lean` proves the generic Sokhotski–Plemelj mechanism, while specialization to the actual six-point celestial tree still requires the named H1–H3 inputs.
4. `PadicMultiplicativeMeasure.lean` defines the density but does not yet prove full multiplicative invariance; `PadicScalingHaar.lean` gets the pushed Haar measure but leaves exact scalar identification as a later step.
5. `YakaboyluPositivityKernel.lean` proves the finite algebraic kernel but deliberately does not supply the deep unbounded-operator PSD compression.
6. `WeilPositivityCriterion.lean` proves the exact finite zero paired-form criterion equivalent to RH, but this is a criterion: the analytic explicit-formula transport supplying its positivity is still the unresolved RH bridge.

## Active fronts after stale-item retirement

### Amplitudes

Already formalized: scalar-box regulated dilog identities, physical structured convergence, four-dimensional external Yang–Mills numerator transfer, general radial `mu^(2k)` family, and the exact algebraic dimension-shift reduction

`-ε(1-ε) I(ε) = -(1-ε) [ε I(ε)]`.

Therefore the honest analytic target is only the scaled raised-box residue

`ε I_4^(8-2ε) -> 1/6`,

not a full Laurent expansion. A promising Feynman-parameter proof is

`I_4^(8-2ε) = Γ(ε) ∫_{Δ_3} Q(x)^(-ε) dx`,

then dominated convergence to `Vol(Δ_3)=1/6`, using `Q >= S x1 x3` and an integrable square-root boundary majorant. Gravity still needs the genuine four-uncut-denominator/generalized-cut reduction.

### RH / Weil

Already formalized: `Delta=2s`/critical-line principal-series dictionary, completed-zeta symmetry and critical response, global prime/von-Mangoldt positive-type results on `Re s>1`, untruncated Poisson-kernel vacuum subtraction positivity, and the finite zero paired-form criterion equivalent to RH.

Therefore the missing theorem is now sharply the completed explicit-formula/Mellin-Fourier-adelic transport from the positive prime/cut test object to the actual zero paired form, including the critical-boundary/interpolation step. No local-kernel positivity should be promoted into RH before that transport exists.

### Gibbs number thermodynamics

Already formalized: partition/free energy/internal energy, entropy derivative, Fisher variance, strict positivity and strict monotonicity, information geometry/KL/Bregman structure, `κ_2'=-κ_3`, and genuine `κ_3>0`. The zeta derivative hierarchy is all-order and has an explicit fourth derivative specialization. On this run the real L-series moment bridge was extended from three to four logarithmic insertions. Next target is the genuine fourth cumulant and `κ_3'=-κ_4`, with positivity supplied by the global prime-power/von-Mangoldt expansion rather than by an unjustified generic-cumulant sign claim.

### Spectral / Mehler–Fock / Wiener–Hopf

The exact sech self-convolution is now closed for every real shift, including the removable origin. The project also contains Mehler–Fock gamma-collapsed weights, spectral-rho recurrence/chamber products, beta bridges, and Gamma Wiener–Hopf factors. The next productive work here is to unify those existing recurrence/chamber files around the all-real normalized weight rather than re-prove the convolution.

## New Lean work during this census

Verify2 commit `f7aabeee5982fc8bf55a77b85329061eb27aa723` extends `ZetaGibbsMomentBridge.lean` to the exact fourth real log-energy moment bridge.

Verify2 commit `35548d239a6b096cedb865e4f93ac2d877f30e42` extends `VonMangoldtCumulantDerivativeBridge.lean` to an all-order derivative theorem and an explicit third-derivative/fourth-cumulant raw response:

`(-ζ'/ζ)''' = - LSeries(logMul^3 Λ)` on `Re s>1`.

Both are pending CI at the time of this census.

## Nonclaims

- No RH proof is claimed from local/global prime positivity alone.
- No D-dimensional Yang–Mills or gravity rational term is claimed before the raised-box residue/generalized-cut analytic input is formalized.
- No Link-6-dependent Standard Model statement is promoted beyond its actual hypotheses.
- No all-loop-finiteness or Wightman physics interpretation is promoted merely because its Lean wrapper compiles; those modules need dependency/axiom audits if they become an active claim frontier.
