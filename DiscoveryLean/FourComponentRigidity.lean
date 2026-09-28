import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
Tiny algebraic checker for the four-component rigidity observation.

Inside the number-circle Gaussian ansatz:
  E Q_d = d * pi / 12,
while the BPY normalization gives
  2 xi(2) = pi / 3.

The theorem below checks that matching these two quantities forces d = 4.
It does not formalize the BPY identity itself.
-/

namespace DiscoveryLean.FourComponentRigidity

theorem component_count_forced (d : ℝ)
    (h : d * Real.pi / 12 = Real.pi / 3) :
    d = 4 := by
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  field_simp [hpi] at h
  nlinarith

end DiscoveryLean.FourComponentRigidity
