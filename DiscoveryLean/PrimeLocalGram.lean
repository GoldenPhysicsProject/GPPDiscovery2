import Mathlib.Tactic

/-!
Local two-state algebra behind the finite self-dual divisor/KMS geometry.

For one prime the critical Gram block is
  [[1,r],[r,1]],  r = p^(-1/2).
The identity below diagonalizes its quadratic form into Fourier-even and
Fourier-odd channels with eigenvalues 1+r and 1-r.
-/

namespace DiscoveryLean.PrimeLocalGram

theorem gram_even_odd_decomposition
    (r x y : ℝ) :
    x^2 + 2*r*x*y + y^2
      =
      ((1+r)/2) * (x+y)^2
      + ((1-r)/2) * (x-y)^2 := by
  ring

theorem gram_pos
    (r x y : ℝ)
    (hlo : -1 ≤ r)
    (hhi : r ≤ 1) :
    0 ≤ x^2 + 2*r*x*y + y^2 := by
  rw [gram_even_odd_decomposition]
  have hp : 0 ≤ (1+r)/2 := by linarith
  have hm : 0 ≤ (1-r)/2 := by linarith
  positivity

theorem antisymmetric_eigenvalue_positive
    (r : ℝ) (hr : r < 1) :
    0 < 1-r := by
  linarith

end DiscoveryLean.PrimeLocalGram
