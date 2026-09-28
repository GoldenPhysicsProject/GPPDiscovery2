import Mathlib.Tactic

/-!
Quick-check algebra for the positive Fredholm-factor target

  1 + a z^2 = 0,  a > 0.

Writing z = x + i y gives the real/imaginary equations below.
The point is deliberately small: a positive quadratic determinant factor
can vanish only on the imaginary axis, and the squared frequency is fixed
by a*y^2 = 1.

This is the finite local algebra used by the arithmetic-vacuum Fredholm
interpretation.  It does not construct the global operator A.
-/

namespace DiscoveryLean.PositiveFredholmFactor

theorem positive_factor_no_real_zero
    (a x : ℝ) (ha : 0 < a) :
    1 + a * x ^ 2 ≠ 0 := by
  have hnonneg : 0 ≤ a * x ^ 2 :=
    mul_nonneg (le_of_lt ha) (sq_nonneg x)
  nlinarith

theorem positive_quadratic_factor_zero_real_part
    (a x y : ℝ) (ha : 0 < a)
    (hre : 1 + a * (x ^ 2 - y ^ 2) = 0)
    (him : 2 * a * x * y = 0) :
    x = 0 := by
  by_contra hx
  have haxy : a * x * y = 0 := by
    nlinarith [him]
  rcases mul_eq_zero.mp haxy with hax | hy
  · rcases mul_eq_zero.mp hax with ha0 | hx0
    · exact (ne_of_gt ha) ha0
    · exact hx hx0
  · rw [hy] at hre
    have hnonneg : 0 ≤ a * x ^ 2 :=
      mul_nonneg (le_of_lt ha) (sq_nonneg x)
    norm_num at hre
    nlinarith

theorem positive_quadratic_factor_zero_frequency
    (a x y : ℝ) (ha : 0 < a)
    (hre : 1 + a * (x ^ 2 - y ^ 2) = 0)
    (him : 2 * a * x * y = 0) :
    a * y ^ 2 = 1 := by
  have hx : x = 0 :=
    positive_quadratic_factor_zero_real_part a x y ha hre him
  rw [hx] at hre
  norm_num at hre
  nlinarith

end DiscoveryLean.PositiveFredholmFactor
