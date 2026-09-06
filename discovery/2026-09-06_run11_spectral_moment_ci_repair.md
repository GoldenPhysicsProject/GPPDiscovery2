# Codex/GPT research rotation — spectral moment CI repair

Date: 2026-09-06

## Verify2 CI diagnosis

Verify2 head `76ddc06a5344a092f0accb60e7ab0db616e42ca2` failed full Build #2087 in `GppVerify/QuantumGravity/SpectralWeightIdentities.lean` while the source-sorry gate passed. The failure was not mathematical: Lean could not compile two real-valued definitions because they depend on real division and were declared computable.

Exact failing declarations:

- `normalizedMoment (a0 ak : ℝ) : ℝ := ak / a0`
- `varianceFromRawMoments (a0 a1 a2 : ℝ) : ℝ := normalizedMoment a0 a2 - (normalizedMoment a0 a1)^2`

Both were repaired by marking them `noncomputable`. No theorem statement or hypothesis was changed.

New Verify2 head: `99819d3ec80dc58d8928ef00e820d1f9482e203a`.

Build #2088 is running on that exact head. PR #22 remains open, draft, and mergeable; it must not be merged until exact-head full gates pass and branch divergence is reconciled.

## Spectral-weight result retained

The principal-series normalized moment package remains:

- raw inputs: `A0 = 1/4`, `A1 = 1/8`, `A2 = 1/8`;
- normalized mean: `A1/A0 = 1/2`;
- normalized second raw moment: `A2/A0 = 1/2`;
- variance: `A2/A0 - (A1/A0)^2 = 1/4 > 0`.

The Lean theorem package formalizes only this exact algebraic consequence of the analytic raw-moment evaluations; it does not claim to formalize the integral evaluations themselves.

## Active-front boundaries

### Celestial cut / amplitudes

Scalar cut -> dispersion -> raised-box regulator endpoint remains closed at `J_ε(S,T) -> 1/6`.

No Yang-Mills master coefficient, gravity numerator, or higher-loop analytic coefficient was promoted. The outstanding physical object remains the factor-preserving opposite crossed full-conic tree, with all uncut propagators retained before topology subtraction and Badger extraction.

### Positive-real / completed-zeta / Weil

Positive-real half-density, `Δ = 2s`, critical-line unitarity, completed-zeta symmetry/response, finite Weil-form criteria, and local Gamma/Wiener-Hopf positivity remain available. No RH promotion: unconditional completed prime-plus-Archimedean explicit-formula/Weil positivity is still missing.

### Prime gas

Certified thermodynamic/fluctuation package remains intact, including `F' = S/β²`, `S' = -β κ₂`, `C = β² κ₂`, strict free-energy concavity, and the countable curvature bound `R(β,η) < 1/2` for `η > 0`.

### Spectral/chamber

The continuous Gamma-chamber crossing, transport, and pairwise alignment layers remain intact. The next analytic target is measure-theoretic covariance symmetrization and the normalized-Gamma chamber-order theorem, followed by the arbitrary-real convolution semigroup / Gamma-density identification.

No Claude-owned work was inspected.
