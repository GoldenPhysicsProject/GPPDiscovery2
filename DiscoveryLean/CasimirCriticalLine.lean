import Mathlib.Tactic

/-!
Tiny checker for the conformal-Casimir reduction of RH.

For rho = beta + i gamma, the Casimir
  rho (1-rho)
has imaginary part gamma (1 - 2 beta).
Thus, for a nonreal zero (gamma != 0), reality of the Casimir forces
  beta = 1/2.

This is the algebraic core of the self-adjoint-Casimir strategy.
-/

namespace DiscoveryLean.CasimirCriticalLine

theorem real_casimir_forces_half
    (beta gamma : ℝ)
    (hgamma : gamma ≠ 0)
    (him : gamma * (1 - 2 * beta) = 0) :
    beta = 1 / 2 := by
  rcases mul_eq_zero.mp him with hg | hb
  · exact (hgamma hg).elim
  · linarith

theorem principal_series_casimir
    (lambda : ℝ) :
    (1 / 2 : ℝ) * (1 - 1 / 2) + lambda ^ 2
      = 1 / 4 + lambda ^ 2 := by
  ring

end DiscoveryLean.CasimirCriticalLine
