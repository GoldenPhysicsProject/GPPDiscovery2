import Mathlib.Tactic

/-!
# Division-algebra flag to chiral five-mode representation: finite tests

Research-stage Discovery2 checker for the selected internal flag
C_i ⊂ H ⊂ O giving the EXTERNAL real carrier
(C_i^perp ⊂ O) ⊕ H ≅ C^3 ⊕ C^2.

If the Hermitian metric, the 3+2 splitting and only the COMBINED
complex volume are preserved, the common stabilizer is
S(U(3) × U(2)). The finite tests below recover the primitive
traceless U(1) direction and the even-exterior one-family
weights. These algebraic statements do NOT produce an equivariant
boundary flag or independent physical gauge fields.

The geometric and topological obstructions appear in the companion
research note, not as Lean-proved theorems in this file.
-/

namespace DiscoveryLean.OctonionicFlagSM

open Finset

/-- Primitive central generator in the five-dimensional complex carrier. -/
def h6 (i : Fin 5) : ℤ := if i.val < 3 then -2 else 3

theorem five_mode_trace_free :
    (∑ i : Fin 5, h6 i) = 0 := by
  decide

/-- The traceless block-scalar direction is necessarily one-dimensional. -/
theorem block_trace_free_iff (a b : ℚ) :
    3 * a + 2 * b = 0 ↔
      ∃ t : ℚ, a = -2 * t ∧ b = 3 * t := by
  constructor
  · intro h
    refine ⟨b / 3, ?_, ?_⟩ <;> linarith
  · rintro ⟨t, rfl, rfl⟩
    ring

/-- Even occupation subsets of the five internal fermionic modes. -/
def evenFock : Finset (Finset (Fin 5)) :=
  (Finset.univ : Finset (Fin 5)).powerset.filter
    (fun s => s.card % 2 = 0)

/-- Occupied modes belonging to the complex color three-space. -/
def colorOccupation (s : Finset (Fin 5)) : ℕ :=
  (s.filter (fun i : Fin 5 => i.val < 3)).card

/-- Primitive six-times-hypercharge on an exterior basis state. -/
def sixY (s : Finset (Fin 5)) : ℤ :=
  3 * (s.card : ℤ) - 5 * (colorOccupation s : ℤ)

/-- The degree/color subspace is a genuine set of occupation states. -/
def inSector (degree nColor : ℕ) : Finset (Finset (Fin 5)) :=
  evenFock.filter
    (fun s => s.card = degree && colorOccupation s = nColor)

/-- Positive-chirality Spin(10) Fock space has sixteen basis states. -/
theorem even_fock_has_sixteen : evenFock.card = 16 := by
  decide

/-- Multiplets Q, u^c, d^c, L, e^c, nu^c, with no inserted charge table. -/
theorem six_standard_model_sectors :
    (inSector 0 0).card = 1 ∧
    (inSector 2 0).card = 1 ∧
    (inSector 2 1).card = 6 ∧
    (inSector 2 2).card = 3 ∧
    (inSector 4 2).card = 3 ∧
    (inSector 4 3).card = 2 := by
  decide

/-- The six multiplets partition every even occupation state. -/
theorem sector_exhaustion :
    ∀ s ∈ evenFock,
      s ∈ inSector 0 0 ∨
      s ∈ inSector 2 0 ∨
      s ∈ inSector 2 1 ∨
      s ∈ inSector 2 2 ∨
      s ∈ inSector 4 2 ∨
      s ∈ inSector 4 3 := by
  decide

/-- Hypercharge weights: nu^c, e^c, Q, u^c, d^c, L. -/
theorem six_sector_weights :
    (∀ s ∈ inSector 0 0, sixY s = 0) ∧
    (∀ s ∈ inSector 2 0, sixY s = 6) ∧
    (∀ s ∈ inSector 2 1, sixY s = 1) ∧
    (∀ s ∈ inSector 2 2, sixY s = -4) ∧
    (∀ s ∈ inSector 4 2, sixY s = 2) ∧
    (∀ s ∈ inSector 4 3, sixY s = -3) := by
  decide

/-- Cancellation of U(1)-gravitational anomaly from the actual weights. -/
theorem one_family_linear_anomaly :
    (∑ s ∈ evenFock, sixY s) = 0 := by
  decide

/-- Cancellation of cubic U(1) anomaly from the actual weights. -/
theorem one_family_cubic_anomaly :
    (∑ s ∈ evenFock, (sixY s) ^ 3) = 0 := by
  decide

/-- The conventional SU(5)-normalized hypercharge trace. -/
theorem five_mode_Y_norm :
    3 * ((-(1 : ℚ) / 3) ^ 2) +
      2 * (((1 : ℚ) / 2) ^ 2) = 5 / 6 := by
  norm_num

/-- The traceless weak-isospin Cartan trace. -/
theorem five_mode_T3_norm :
    (((1 : ℚ) / 2) ^ 2) + ((-(1 : ℚ) / 2) ^ 2) = 1 / 2 := by
  norm_num

/-- The common-coupling tree-level GUT mixing-angle relation. -/
theorem common_coupling_weak_angle :
    ((1 : ℚ) / 2) / (1 / 2 + 5 / 6) = 3 / 8 := by
  norm_num

end DiscoveryLean.OctonionicFlagSM

#print axioms DiscoveryLean.OctonionicFlagSM.block_trace_free_iff
#print axioms DiscoveryLean.OctonionicFlagSM.six_standard_model_sectors
#print axioms DiscoveryLean.OctonionicFlagSM.one_family_cubic_anomaly
