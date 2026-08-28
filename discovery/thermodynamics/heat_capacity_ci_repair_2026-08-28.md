# Heat-capacity CI repair and frontier checkpoint — 2026-08-28

Codex/GPT-only checkpoint.

## CI finding

The dedicated Gibbs workflow failed only in `ZetaGibbsHeatCapacityDerivative.lean` while all preceding cumulant modules passed. The mathematical identity was not at fault. Lean elaborated the derivative of `x^2` through `id`, leaving the syntactic residual goal

`β * 2 = id β * 2`.

The proof was repaired by deriving `x^2` as `x*x` from `(hasDerivAt_id β).mul (hasDerivAt_id β)` and then normalizing algebraically. No theorem statement or physics/mathematics claim was weakened.

Target identity remains

`C'(β) = 2 β κ₂(β) - β² κ₃(β)` for `β > 1`.

## Certified state before repair

Build #1116 succeeded and sech #219 succeeded. Therefore the new finite polynomial interpolation / pair-support reduction, scalar-box pointwise regulator limit, and exact spectral chamber threshold trichotomy are in the green full build. Gibbs #293 failed only at the new heat-capacity module after the cumulant hierarchy, quartic von Mangoldt positivity, and strict third-cumulant derivative all compiled successfully.

## Active frontiers

1. Scalar box: finish the Dirichlet/Beta simplex integrability theorem and dominated convergence to `J(ε) -> 1/6`; Gamma residue and dimension-shift assembly are already formal.
2. Weil/RH: convert polynomial finite interpolation into the concrete admissible Mellin/Paley-Wiener transform class via polynomial-multiplier closure plus a nonvanishing seed on finite pair-support.
3. Prime gas: after heat-capacity CI repair, continue response geometry; the exact cumulant ladder through `κ₄ > 0` is already formal.
4. Spectral: exact chamber recurrence, all-real Mehler-Fock form, positivity/evenness, and amplification/suppression threshold are formal; next useful target is integrated chamber normalization/convolution rather than more pointwise algebra.
5. Amplitudes: generic YM/gravity massive state-sum numerators remain the honest obstruction beyond the closed special four-point sectors.
