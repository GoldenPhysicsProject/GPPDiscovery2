import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Tactic

/-!
# Minimal principal-series criterion for RH

This file deliberately avoids positivity, Fredholm determinants, Pick functions, and
Weil forms.  It isolates the exact algebraic statement needed to put a complex spectral
parameter on the unitary principal series.

For s = sigma + i t define the centered square
  u(s) = (s - 1/2)^2.
Then

  u(s) is real and <= 0  <->  Re s = 1/2.

Equivalently,
  s = 1/2 + i lambda for some real lambda.

Thus RH is equivalent to saying that every critical-strip zero has centered square on
the non-positive real axis.  Any analytic/operator construction that proves that property
is sufficient; no positivity mechanism is assumed here.
-/

namespace DiscoveryLean.PrincipalSeriesZeroCriterion

open Complex

noncomputable section

/-- Centered-square / Casimir-defect coordinate. -/
def centeredSq (s : ℂ) : ℂ := (s - (1 / 2 : ℂ)) ^ 2

/-- Imaginary part of the centered square. -/
theorem centeredSq_im (s : ℂ) :
    (centeredSq s).im = 2 * (s.re - 1 / 2) * s.im := by
  simp [centeredSq, pow_two, mul_im] <;> ring

/-- Real part of the centered square. -/
theorem centeredSq_re (s : ℂ) :
    (centeredSq s).re = (s.re - 1 / 2)^2 - s.im^2 := by
  simp [centeredSq, pow_two, mul_re] <;> ring

/-- The non-positive real centered-square ray is exactly the critical line. -/
theorem centeredSq_nonpos_real_iff_critical (s : ℂ) :
    ((centeredSq s).im = 0 ∧ (centeredSq s).re ≤ 0) ↔ s.re = 1 / 2 := by
  rw [centeredSq_im, centeredSq_re]
  constructor
  · rintro ⟨him, hre⟩
    have hprod : (s.re - 1 / 2) * s.im = 0 := by
      linarith
    rcases mul_eq_zero.mp hprod with ha | hb
    · linarith
    · rw [hb] at hre
      nlinarith [sq_nonneg (s.re - 1 / 2)]
  · intro h
    rw [h]
    constructor
    · ring
    · nlinarith [sq_nonneg s.im]

/-- Principal-series witness formulation. -/
def OnPrincipalSeries (s : ℂ) : Prop :=
  ∃ lam : ℝ, s = (1 / 2 : ℂ) + (lam : ℂ) * I

theorem onPrincipalSeries_iff_critical (s : ℂ) :
    OnPrincipalSeries s ↔ s.re = 1 / 2 := by
  constructor
  · rintro ⟨lam, rfl⟩
    simp
  · intro h
    refine ⟨s.im, Complex.ext ?_ ?_⟩
    · simpa [h]
    · simp

theorem centeredSq_nonpos_real_iff_principal (s : ℂ) :
    ((centeredSq s).im = 0 ∧ (centeredSq s).re ≤ 0) ↔ OnPrincipalSeries s := by
  rw [centeredSq_nonpos_real_iff_critical, onPrincipalSeries_iff_critical]

/-- RH in the open critical strip, using Mathlib's analytically continued zeta. -/
def RHStrip : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → 0 < s.re → s.re < 1 → s.re = 1 / 2

/-- Minimal Casimir statement: every critical-strip zero has a non-positive real
centered-square. -/
def ZeroCasimirAdmissible : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → 0 < s.re → s.re < 1 →
    (centeredSq s).im = 0 ∧ (centeredSq s).re ≤ 0

/-- **Exact equivalence.**  RH is nothing more and nothing less than centered-square
admissibility of every strip zero. -/
theorem rhStrip_iff_zeroCasimirAdmissible :
    RHStrip ↔ ZeroCasimirAdmissible := by
  constructor
  · intro rh s hz h0 h1
    exact (centeredSq_nonpos_real_iff_critical s).2 (rh s hz h0 h1)
  · intro h s hz h0 h1
    exact (centeredSq_nonpos_real_iff_critical s).1 (h s hz h0 h1)

/-- Equivalent principal-series formulation of RH. -/
def EveryStripZeroPrincipal : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → 0 < s.re → s.re < 1 → OnPrincipalSeries s

theorem rhStrip_iff_everyStripZeroPrincipal :
    RHStrip ↔ EveryStripZeroPrincipal := by
  constructor
  · intro rh s hz h0 h1
    exact (onPrincipalSeries_iff_critical s).2 (rh s hz h0 h1)
  · intro h s hz h0 h1
    exact (onPrincipalSeries_iff_critical s).1 (h s hz h0 h1)

end DiscoveryLean.PrincipalSeriesZeroCriterion
