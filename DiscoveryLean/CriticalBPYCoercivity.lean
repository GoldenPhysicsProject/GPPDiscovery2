import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Tactic

namespace DiscoveryLean.CriticalBPYCoercivity

theorem pi_square_between :
    (9 : ℝ) < Real.pi ^ 2 ∧ Real.pi ^ 2 < 10 := by
  constructor
  · have h : (3 : ℝ) < Real.pi := by
      linarith [Real.pi_gt_d2]
    nlinarith [Real.pi_pos]
  · have h : Real.pi < (3.15 : ℝ) := Real.pi_lt_d2
    have hp : 0 < Real.pi := Real.pi_pos
    nlinarith

theorem critical_tail_constant_lt_one :
    ((Real.pi ^ 2 / 6 - 1) *
      (1 + 63 / (16 * Real.pi ^ 2)) : ℝ) < 1 := by
  rcases pi_square_between with ⟨h9, h10⟩
  have hp2 : 0 < Real.pi ^ 2 := sq_pos_of_pos Real.pi_pos
  have hpoly : 16 * (Real.pi ^ 2)^2 - 129 * Real.pi ^ 2 - 378 < 0 := by
    have hderiv_region : (129 : ℝ) / 32 < Real.pi ^ 2 := by
      linarith
    nlinarith
  field_simp [ne_of_gt hp2]
  nlinarith

end DiscoveryLean.CriticalBPYCoercivity
