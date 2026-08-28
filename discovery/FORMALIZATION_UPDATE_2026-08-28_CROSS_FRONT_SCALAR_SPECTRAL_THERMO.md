# Codex/GPT cross-front formalization update — 2026-08-28

This note records only Codex/GPT work. No Claude work was inspected.

## 1. Celestial cuts / scalar box / YM-gravity

The active-front map had conflated two regulator problems.

### Structured massive scalar box

`ScalarBoxStructuredPhysicalConvergence.lean` already contains the one-sided physical regulator theorem

`tendsto_physical_structured_scalarBox_core_zero`.

It composes the exact physical kinematic relations for `R, κ, q, a, x, δ, η, ρ, B, t` with the mixed-logarithm majorant and the `1/κ` prefactor remainder. Thus the explicit structured massive scalar-box core has a formal regulator-removal theorem under its stated eventual physical chamber/defining relations.

This is stronger than the earlier status line saying that the scalar-box regulator limit itself still awaited the simplex DCT.

### Raised-box dimensional-regulator layer

The separate `RaisedBoxSimplexMajorantAlgebra.lean` proves only the pointwise Euclidean majorant

`Q^(-ε) <= 1 + (A x1 x3)^(-δ)`

for `0 <= ε <= δ`, with the channel monomial lower bound. Its own module header correctly states that integrability of the majorant over the 3-simplex remains a separate Dirichlet/Beta integral layer.

Therefore the open DCT problem belongs to the raised-box / dimension-shift residue route, not to the already-assembled structured massive scalar-box core.

### Honest gauge/gravity numerator boundary

`MassiveVectorStateSumReconstruction.lean` still explicitly does not compute the required `Ds=4, μ != 0` gluon sewing numerator. It proves only state-count/reconstruction algebra. No scalar reconstruction identity may be promoted into a vector numerator. The next genuine amplitudes target remains an explicit tree-product state sum or Ward-complete massive-vector cut numerator before generalized/higher-loop cuts.

## 2. Positive-real principal series / completed zeta

The exact dictionary is already formalized:

- `criticalReflection(s)=1-s`;
- `celestialWeight(s)=2s`;
- `Re s=1/2 <-> Re Δ=1`;
- on `Re s=1/2`, reflection equals complex conjugation;
- `Δ=2s` intertwines `s -> 1-s` with scalar shadow `Δ -> 2-Δ`.

`CompletedZetaPrincipalSeriesResponse.lean` then proves, away from poles/zeros where the logarithmic derivative is defined,

- the celestial completed-zeta logarithmic response is purely imaginary on `Re Δ=1`;
- it is odd under shadow globally;
- on the principal axis it is odd under conjugation.

These are structural unitarity/functional-equation statements only. They do not constrain zero locations by themselves. The missing global arithmetic step remains the explicit-formula/Weil/Wiener-Hopf positivity or admissible interpolation bridge.

## 3. Prime-gas thermodynamics

The honest Gibbs domain `β>1` already has the exact differential hierarchy:

- `A'(β)=-U(β)`;
- `U'(β)=-κ₂(β)`;
- `S'(β)=-β κ₂(β)=-C(β)/β`;
- `C'(β)=2β κ₂(β)-β² κ₃(β)`;
- `κ₂'(β)=-κ₃(β)` and `κ₂''(β)=κ₄(β)>0` through the existing cumulant chain.

Strict thermodynamic stability is also formalized: `κ₂>0`, `C>0`, and `S'<0` on `β>1`.

No global sign for `C'` or `S''` is justified. The useful remaining frontier is not another algebraic rewrite but a uniform/renormalized quantity with a controlled `β -> 1+` limit that can be compared to the causal-diamond Kubo-Mori/Fisher form.

## 4. Spectral Gamma / Mehler-Fock / Wiener-Hopf

The dedicated sech/Wiener-Hopf CI lane failed after the convolution endpoint, closed-form, and basic Wiener-Hopf modules had already compiled. The actual dependency failure was in `SpectralRhoRecurrence.lean`, not `SpectralGammaPairRecurrence.lean` as the earlier map stated.

The failing normalization subgoal was purely algebraic:

`2^(2*k+1) * 4 = 4 * 2^(2*k+1)`.

The proof has been repaired by adding ring normalization after the power expansion. Verify2 commit:

`9a86b44a12fb2fa707530c62178137cfca20ba63`

The repaired theorem is the exact recurrence

`rhoGamma (k+1) x = R_k(x) * rhoGamma k x`,

with

`R_k(x)=2(((k+1)^2+x^2))/((k+1)(2k+3))`.

The previously formalized threshold remains exact:

- `R_k(x)>1 <-> k+1 < 2x^2`;
- `R_k(x)<1 <-> 2x^2 < k+1`;
- equality at `2x^2=k+1`.

CI certification is being rechecked. If green, the next mathematical issue is to distinguish this algebraic chamber product from an actual iterated convolution operator identity; no convolution interpretation should be asserted without that operator theorem.

## Corrected immediate priorities

1. Close the raised-box 3-simplex integrability / Beta-Gamma quotient and DCT residue layer.
2. Derive the honest `Ds=4, μ != 0` vector sewing numerator; only then extend generic YM/gravity cuts and higher loops.
3. Seek a uniform `β -> 1+` Gibbs/Fisher renormalization rather than unproved heat-capacity signs.
4. After spectral CI is green, build only genuine Mehler-Fock/Wiener-Hopf operator identities, keeping algebraic Gamma recurrences separate from physical convolution claims.
5. Principal-series work remains at the exact structural bridge: unitary-axis/shadow/conjugation is proved; arithmetic positivity is not.
