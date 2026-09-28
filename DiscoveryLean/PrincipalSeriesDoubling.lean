import Mathlib.Tactic
import Mathlib.Data.Complex.Basic

/-!
Quick checks for the exact CFT1 -> celestial scalar doubling:

  s = 1/2 + i tau,
  (h,hbar) = (s,s),
  Delta = h+hbar = 2s,
  simultaneous chiral shadow s -> 1-s gives Delta -> 2-Delta.

This is only the algebraic parameter map.  It does not assert an RH spectral
realization or construct the PSL(2,R) -> PSL(2,C) intertwiner.
-/

namespace DiscoveryLean.PrincipalSeriesDoubling

def celestialDelta (s : ℂ) : ℂ := 2 * s

theorem left_right_sum (s : ℂ) :
    s + s = celestialDelta s := by
  simp [celestialDelta, two_mul]

theorem simultaneous_shadow (s : ℂ) :
    celestialDelta (1 - s) = 2 - celestialDelta s := by
  simp [celestialDelta]
  ring

theorem critical_line_doubles (tau : ℝ) :
    (celestialDelta ((1 / 2 : ℂ) + Complex.I * tau)).re = 1 := by
  simp [celestialDelta]
  norm_num

theorem critical_shadow_is_conjugate (tau : ℝ) :
    1 - ((1 / 2 : ℂ) + Complex.I * tau) =
      Complex.conj ((1 / 2 : ℂ) + Complex.I * tau) := by
  apply Complex.ext <;> simp
  · norm_num
  · ring

end DiscoveryLean.PrincipalSeriesDoubling
