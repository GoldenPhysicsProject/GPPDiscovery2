import Mathlib.Tactic

/-!
Quick-check formalization for current Discovery2 experiments.
This sandbox is intentionally small and disposable; mature theorems move to GPPVerify.
-/

namespace DiscoveryLean.PrimeModularCovariance

def thermalCov (q : ℝ) : ℝ := q / (1 - q)
def normalCov (r : ℝ) : ℝ := r ^ 2 / (1 - r ^ 2)
def anomalousCov (r : ℝ) : ℝ := r / (1 - r ^ 2)

theorem thermalCov_prime (p : ℝ) (hp0 : p ≠ 0) (hp1 : p ≠ 1) :
    thermalCov (1 / p) = 1 / (p - 1) := by
  unfold thermalCov
  field_simp
  ring

theorem casimirMassSq_prime (p : ℝ) (hp0 : p ≠ 0) (hp1 : p ≠ 1) :
    4 * thermalCov (1 / p) = 4 / (p - 1) := by
  rw [thermalCov_prime p hp0 hp1]

theorem anomalous_sq_eq_normal_mul (r : ℝ) (h : 1 - r ^ 2 ≠ 0) :
    anomalousCov r ^ 2 = normalCov r * (1 + normalCov r) := by
  unfold anomalousCov normalCov
  field_simp [h]
  ring

theorem normal_ordered_det (r : ℝ) (h : 1 - r ^ 2 ≠ 0) :
    normalCov r ^ 2 - anomalousCov r ^ 2 = - normalCov r := by
  unfold normalCov anomalousCov
  field_simp [h]
  ring

theorem vacuum_completed_det (r : ℝ) (h : 1 - r ^ 2 ≠ 0) :
    (normalCov r + 1 / 2) ^ 2 - anomalousCov r ^ 2 = 1 / 4 := by
  unfold normalCov anomalousCov
  field_simp [h]
  ring

theorem completed_minus_eigenvalue (r : ℝ)
    (h1 : 1 - r ^ 2 ≠ 0) (hp : 1 + r ≠ 0) :
    normalCov r + 1 / 2 - anomalousCov r =
      (1 - r) / (2 * (1 + r)) := by
  unfold normalCov anomalousCov
  field_simp [h1, hp]
  ring

theorem completed_plus_eigenvalue (r : ℝ)
    (h1 : 1 - r ^ 2 ≠ 0) (hm : 1 - r ≠ 0) :
    normalCov r + 1 / 2 + anomalousCov r =
      (1 + r) / (2 * (1 - r)) := by
  unfold normalCov anomalousCov
  field_simp [h1, hm]
  ring

theorem odd_even_repetition_split (x : ℝ)
    (h1 : 1 - x ≠ 0) (h2 : 1 - x ^ 2 ≠ 0) :
    x / (1 - x) = x / (1 - x ^ 2) + x ^ 2 / (1 - x ^ 2) := by
  field_simp [h1, h2]
  ring

end DiscoveryLean.PrimeModularCovariance
