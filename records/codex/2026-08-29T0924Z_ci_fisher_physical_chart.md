# Codex/GPT continuation — CI, Fisher geometry, physical-chart cut reduction

Date: 2026-08-29
Track: Codex/GPT only
Verify branch: `codex/lean-workbench`
Discovery branch: `codex/discovery-workbench`

## CI repair

The prior universal-NOT repair remained red.  The finite-core log showed that the only unresolved algebraic residue in `pauliSum_eq` was `Complex.I ^ 2`.  The proof has now been made explicit with

```lean
have hI : Complex.I ^ 2 = (-1 : ℂ) := by
  simpa [pow_two] using Complex.I_mul_I
```

and the matrix expression is normalized only after `Matrix.vecMul` / `dotProduct` unfolding.  Verify commit:

`b4e3e6147c51da2c472d935ff79a1729824da607`

The previous head `a847ad95...` is superseded and should not be described as certified.

## Prime-gas two-parameter strictness

The existing all-order theorem already proves strict positivity of the actual von-Mangoldt Fisher polynomial Gram form on every `β>1`.  A direct two-statistic specialization has now been added:

```text
scorePolynomial(a,b)(x) = a x + b x^2.
```

For every `β>1` and every nonzero coefficient pair `(a,b)`, the target theorem is

```text
0 < Σ' n, fisherWeight β n *
      (a log n + b (log n)^2)^2.
```

This is the strict quadratic-form statement for the sufficient statistics `(log n,(log n)^2)`, stronger than determinant nonnegativity alone.  Verify commit:

`f18401c3b0c6d9a7e804f428910b8d5beca03d1a`

At record time this new module is source-level formalization awaiting CI certification.

## Honest massive-vector cut: physical-chart reduction

The generic massive-vector tree audit is explicitly not the old threshold 3:1 identity.  Starting from its exact rational expressions, a new executable audit rewrites the two cleanest generic pieces into the physical chart

```text
β = |p|/E,
ρ = μ/E,
c = cos θ,
u = β² sin² θ,
β² + ρ² = 1.
```

It verifies exactly

```text
C_same^(V_m) - 3 C_same^S
  = 16 β² / (1-β c)²,

C_mixed^S
  = u² / (1-β c)².
```

This connects the generic tree-state audit directly to the rational physical chart used by the celestial cut / regulator machinery.  Discovery commit:

`6eced5ae27b7714039a11118202f77ed7c5ddc5a`

The complete vector mixed-helicity numerator still requires analytic reduction of the exact generic tree expression; no Ward/projector shortcut is assumed.

## Spectral / principal-series status

No new theorem was required on this pass.  The dedicated sech/Gamma lane was green on the previous head, certifying the finite-chamber positive square factorization and exact recurrence threshold.  Arithmetic OS and Gibbs differential thermodynamics were also green before the new commits.

The critical-line statement remains local/structural: `Δ=2s` identifies `Re Δ=1` with `Re s=1/2`, and the completed-zeta logarithmic response is tangent there away from zeros.  This is not a global zero-exclusion theorem.

## Operating-file note

No `CODEX.md` file is present on either Codex workbench repository under that exact name, and a File Library search did not locate one.  Existing Codex run records and repository operating conventions were therefore used.  No Claude records were inspected.

## Next frontier

1. Certify or repair `b4e3e614...` and `f18401c3...` under the global CI lanes.
2. Package the two-statistic strict quadratic form into positive-definiteness / determinant strictness if not already subsumed by a current theorem.
3. Reduce the generic mixed-helicity massive-vector sewing to the physical `(β,ρ,c,u)` chart and combine with scalar subtraction to obtain the honest `D_s=4` cut numerator.
4. Feed that numerator into the already-closed scalar-box regulator/dispersion chain.
5. Continue the prime–Archimedean explicit-formula / Wiener-Hopf identification; RH remains unproved until the correctly signed global Weil quadratic form is identified with the positive construction.
