# Codex continuation — scalar AE / Lean 4.19 NoAtoms repair

Scope: Codex/GPT track only. No Claude material inspected or used.

## Verify2 CI diagnosis

Verify2 `codex/lean-workbench` head `ed36c072afed564ef6b547a974dfe65ef7bee579` failed changed-Lean run `33579108873`. Source-sorry, toolchain, Lake cache, and Mathlib cache steps passed; failure was isolated to changed-module compilation of the newly added raised-box AE layer.

The pinned project uses Mathlib `v4.19.0`, revision `c44e0c8ee63ca166450922a373c7409c5d26b00b`. At that revision the nonatomic API is still `MeasureTheory.NoAtoms`, in `Mathlib/MeasureTheory/Measure/Typeclasses/NoAtoms.lean`; there is no `NullSingletonClass` file and there is no `Measure.ae_ne` lemma. The available exact theorem is `Set.Countable.ae_not_mem` under `[NoAtoms μ]`.

## Repair

Pushed Verify2 commit `fe8c43f52ab3a0bf1268b2b543d56a236733b6e8`.

`RaisedBoxInnerAE.lean` now imports `Mathlib.MeasureTheory.Measure.Typeclasses.NoAtoms` and removes the sole exceptional inner endpoint using

```lean
have hne : ∀ᵐ x3 : ℝ ∂volume, x3 ≠ 1 - x1 - x2 := by
  simpa using (Set.countable_singleton (1 - x1 - x2)).ae_not_mem volume
```

The mathematical statement is unchanged: for strict base-point data `0<x1`, `0<x2`, `x1+x2<1`, the regulated integrand tends to one for volume-a.e. `x3 ∈ Ioc 0 (1-x1-x2)`. The only excluded point is the upper endpoint.

Fresh changed-Lean run: `33582986546` (in progress when recorded).

## Scalar next theorem

If this AE layer is green, the next justified theorem is the actual inner interval dominated-convergence passage. Inputs already present in Verify2 are: strict-interior pointwise convergence, one-channel majorant, inner-slice interval integrability, and the AE endpoint removal proved here. No additional Beta/Gamma surrogate should be added before attempting the interval DCT.

## Other active fronts

Number thermodynamics remains at the certified normalized covariance/Fisher determinant stage; the next non-algebraic step is differentiation under the quadratically confined tsum and identification of the `log Z` Hessian with the covariance matrix.

Principal-series / completed-zeta and Gamma / Mehler-Fock / Wiener-Hopf / chamber results remain local/Archimedean exact structure. No global Weil positivity or RH theorem is promoted absent a prime-plus-Archimedean quadratic form identified with the actual Weil criterion.

Honest `D_s=4, μ≠0` Yang-Mills sewing remains downstream of scalar regulator closure. No triangle/bubble/rational-sector absence is assumed.
