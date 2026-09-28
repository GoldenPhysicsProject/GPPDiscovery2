import Mathlib.Tactic

/-!
Quick checks for the exact CFT1 -> celestial scalar doubling, written in
(real part, imaginary part) coordinates to keep this disposable checker tiny.

  s = (1/2, tau),
  (h,hbar) = (s,s),
  Delta = 2s = (1,2 tau),
  simultaneous chiral shadow s -> 1-s gives Delta -> 2-Delta.

This is only the algebraic parameter map. It does not assert an RH spectral
realization or construct the PSL(2,R) -> PSL(2,C) intertwiner.
-/

namespace DiscoveryLean.PrincipalSeriesDoubling

noncomputable def arithmeticWeight (tau : ℝ) : ℝ × ℝ := (1 / 2, tau)

def celestialDelta (w : ℝ × ℝ) : ℝ × ℝ :=
  (2 * w.1, 2 * w.2)

def shadow1 (w : ℝ × ℝ) : ℝ × ℝ :=
  (1 - w.1, -w.2)

def shadow2 (w : ℝ × ℝ) : ℝ × ℝ :=
  (2 - w.1, -w.2)

theorem critical_line_doubles (tau : ℝ) :
    (celestialDelta (arithmeticWeight tau)).1 = 1 := by
  norm_num [celestialDelta, arithmeticWeight]

theorem spectral_parameter_doubles (tau : ℝ) :
    (celestialDelta (arithmeticWeight tau)).2 = 2 * tau := by
  rfl

theorem simultaneous_shadow (w : ℝ × ℝ) :
    celestialDelta (shadow1 w) = shadow2 (celestialDelta w) := by
  rcases w with ⟨a, b⟩
  simp [celestialDelta, shadow1, shadow2]
  ring

theorem critical_shadow_fixed_real_part (tau : ℝ) :
    (shadow1 (arithmeticWeight tau)).1 = 1 / 2 := by
  norm_num [shadow1, arithmeticWeight]

end DiscoveryLean.PrincipalSeriesDoubling
