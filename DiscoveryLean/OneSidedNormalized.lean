import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Tactic.Linarith

/-!
Finite one-sided normalized quadratic form criterion, with an explicit
Hermitian hypothesis. The arbitrary off-diagonal signed energy is allowed
to have large POSITIVE directions; only the lower bound by minus the
identity energy is needed.

The general congruence theorem below separates this spectral statement
from the independent algebraic obligation M = Sᴴ (I+T) S, required to
identify it with a particular completed prime-Archimedean Gram matrix.
No claim of global Weil positivity is made.
-/

namespace GppOneSidedNormalized

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The one-sided energy bound, unlike a two-sided operator norm bound,
allows arbitrarily large positive eigenvalues of T. -/
theorem normalized_psd_of_one_sided
    (T : Matrix n n ℝ)
    (hHerm : (1 + T).IsHermitian)
    (hLower : ∀ v : n → ℝ,
      -(star v ⬝ᵥ v) ≤ star v ⬝ᵥ (T *ᵥ v)) :
    (1 + T).PosSemidef := by
  apply Matrix.PosSemidef.of_dotProduct_mulVec_nonneg hHerm
  intro v
  have h := hLower v
  have heq : star v ⬝ᵥ ((1 + T) *ᵥ v) =
      star v ⬝ᵥ v + star v ⬝ᵥ (T *ᵥ v) := by
    simp only [Matrix.add_mulVec, Matrix.one_mulVec, Matrix.dotProduct_add]
  rw [heq]
  linarith

/-- General congruence transport of normalized one-sided positivity.
The exact factorization is an explicit hypothesis, never inferred from
positive diagonal entries alone. -/
theorem congruent_psd_of_one_sided
    (M S T : Matrix n n ℝ)
    (hFactor : M = Sᴴ * (1 + T) * S)
    (hHerm : (1 + T).IsHermitian)
    (hLower : ∀ v : n → ℝ,
      -(star v ⬝ᵥ v) ≤ star v ⬝ᵥ (T *ᵥ v)) :
    M.PosSemidef := by
  rw [hFactor]
  exact (normalized_psd_of_one_sided T hHerm hLower).conjTranspose_mul_mul_same S

end GppOneSidedNormalized
