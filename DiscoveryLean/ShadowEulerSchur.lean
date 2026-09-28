import Mathlib.Tactic

/-!
Algebraic core of the Shadow Euler / Schur-complement bridge.

1. The scalar parallel sum k*N/(k+N) is the effective stiffness obtained by
   minimizing k*x^2 + N*y^2 under x+y=z.
2. The conformal-Casimir defect is exactly the square distance from 1/2:
      1/4 - s(1-s) = (s-1/2)^2.
-/

namespace DiscoveryLean.ShadowEulerSchur

theorem casimir_defect_square (s : ℝ) :
    (1 / 4 : ℝ) - s * (1 - s) = (s - 1 / 2) ^ 2 := by
  ring

theorem parallel_sum_energy_identity
    (k N x y z : ℝ)
    (hkN : k + N ≠ 0)
    (hxy : x + y = z) :
    k * x^2 + N * y^2
      =
      (k * N / (k + N)) * z^2
      + ((k + N) * x - N * z)^2 / (k + N) := by
  field_simp [hkN]
  nlinarith [hxy]

theorem parallel_sum_lower_bound
    (k N x y z : ℝ)
    (hk : 0 < k)
    (hN : 0 < N)
    (hxy : x + y = z) :
    (k * N / (k + N)) * z^2 ≤ k * x^2 + N * y^2 := by
  have hkN : 0 < k + N := add_pos hk hN
  rw [parallel_sum_energy_identity k N x y z (ne_of_gt hkN) hxy]
  have hsq : 0 ≤ (((k + N) * x - N * z)^2 / (k + N)) := by
    positivity
  linarith

theorem parallel_sum_attained
    (k N z : ℝ)
    (hkN : k + N ≠ 0) :
    let x := N * z / (k + N)
    let y := k * z / (k + N)
    x + y = z ∧
    k * x^2 + N * y^2 = (k * N / (k + N)) * z^2 := by
  dsimp
  constructor
  · field_simp [hkN]
    ring
  · field_simp [hkN]
    ring

end DiscoveryLean.ShadowEulerSchur
