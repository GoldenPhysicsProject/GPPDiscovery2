import Mathlib.Tactic

/-!
A disposable finite-dimensional checker for the gap-transfer mechanism.

For a symmetric 2x2 block form
  a x^2 + 2 b x y + c y^2,
a positive bulk coefficient a and a positive Schur-complement margin
  a (c - m) >= b^2
force the physical y-channel to retain the gap m.

This is the scalar core of
  S = C - B A^{-1} B^*
used in the RH/Yang--Mills vacuum-quotient gap note.
-/

namespace DiscoveryLean.SchurGapTransfer

theorem scalar_schur_gap
    (a b c m x y : ℝ)
    (ha : 0 < a)
    (hSchur : b ^ 2 ≤ a * (c - m)) :
    m * y ^ 2 ≤ a * x ^ 2 + 2 * b * x * y + c * y ^ 2 := by
  have hdefect : 0 ≤ a * (c - m) - b ^ 2 := by
    nlinarith
  have hy2 : 0 ≤ y ^ 2 := sq_nonneg y
  have hprod : 0 ≤ (a * (c - m) - b ^ 2) * y ^ 2 :=
    mul_nonneg hdefect hy2
  have hsq : 0 ≤ (a * x + b * y) ^ 2 := sq_nonneg (a * x + b * y)
  have ha0 : 0 < a := ha
  nlinarith

theorem normalized_poincare_gives_nonnegative_defect
    (energy variance : ℝ)
    (h : variance ≤ energy) :
    0 ≤ energy - variance := by
  linarith

end DiscoveryLean.SchurGapTransfer
