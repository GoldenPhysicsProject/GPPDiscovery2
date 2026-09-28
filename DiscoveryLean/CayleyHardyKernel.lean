import Mathlib.Tactic

/-!
Disposable algebra check for the Cayley transform behind the
right-half-plane Hardy kernel.

For real variables this proves the rational identity underlying

  1/(z + conjugate w)
    ~ 1/(1 - u conjugate v)

after the Cayley substitution z=(1+u)/(1-u).

The complex/antiholomorphic bookkeeping is not encoded here; this file
checks only the load-bearing rational algebra.
-/

namespace DiscoveryLean.CayleyHardyKernel

theorem cayley_sum_identity
    (u v : ℝ) (hu : 1 - u ≠ 0) (hv : 1 - v ≠ 0) :
    (1 + u) / (1 - u) + (1 + v) / (1 - v)
      =
    2 * (1 - u * v) / ((1 - u) * (1 - v)) := by
  field_simp [hu, hv]
  ring

theorem cayley_kernel_identity
    (u v : ℝ)
    (hu : 1 - u ≠ 0) (hv : 1 - v ≠ 0)
    (huv : 1 - u * v ≠ 0) :
    1 / ((1 + u) / (1 - u) + (1 + v) / (1 - v))
      =
    ((1 - u) * (1 - v)) / (2 * (1 - u * v)) := by
  rw [cayley_sum_identity u v hu hv]
  field_simp [huv]

end DiscoveryLean.CayleyHardyKernel
