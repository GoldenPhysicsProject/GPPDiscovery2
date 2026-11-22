# Finite transverse radius and spinorial angular charge force a nonzero reduced mass

**Date:** 2026-11-22  
**Status:** Exact conditional theorem in the real transverse phase-plane; symbolic regression checked. Not a derivation of nonzero mass from orientation symmetry alone.

## Setting

In the doubled-null parent used by *Which Way Is Forward?* v29, take a transverse canonical pair
[
y=(y_1,y_2),qquad k=(k_1,k_2)
]
with the standard Euclidean normal-plane norm. The parent null constraint
[
Q_8=Q_K+|k|^2=0
]
gives the four-dimensional mass shell
[
Q_K=-m^2c^2,qquad |k|=mc.
]
The canonical angular momentum is
[
J_perp=y_1k_2-y_2k_1.
]

## Theorem: transverse-angular mass lower bound

Suppose (c>0), (hbar>0), (0<R<infty), (|y|le R), (m=|k|/c), and
[
|J_perp|gehbar/2.
]
Then
[
oxed{mge rac{hbar}{2cR}>0.}
]

**Proof.** The two-dimensional Lagrange identity is
[
|y|^2|k|^2=(y_1k_2-y_2k_1)^2+(y_1k_1+y_2k_2)^2.
]
Therefore (|J_perp|le |y||k|le Rmc), hence (mgehbar/(2cR)>0).

The bound is sharp: (y=(R,0)), (k=(0,hbar/(2R))) gives (J_perp=hbar/2) and equality. No circular trajectory, constant-radius dynamics, or vanishing radial momentum is needed for the inequality itself.

For any prescribed nonzero (J_perp) and a finite value of (|y|), the same identity already forces (m>0). A **uniform** lower bound requires a uniform finite radius (R).

## Connection to the transverse spin cover

WWIF v29 derives the transverse canonical one-form
[
k_aDy^a=p_rdr+J_perp(d	heta-Omega)
]
and describes spinorial transverse angular weights (n_perp=2J_perp/hbar) as odd. **If** the physical sector has an actual nonzero transverse spinorial weight (n_perpin 2mathbb Z+1), then (|J_perp|gehbar/2); combined with a finite transverse-radius bound, the theorem excludes (m=0).

This strengthens the paper's conditional constant-radius, purely angular zitter construction: a **positive lower bound** follows without postulating an orbit.

But the assumptions matter:

1. A nontrivial **Lorentz spin** representation does not by itself imply nonzero **orbital canonical transverse angular momentum** (J_perp=y	imes k). Their identification would require the genuine bundle/intertwining construction.
2. No finite physical radius (R) has yet been derived from the double-sheet boundary sewing or from the projective quotient. Without (R), the fixed-(J) family (y=(r,0), k=(0,hbar/(2r))) has (m=hbar/(2cr)	o0) as (r	oinfty).
3. The diagonal orientation quotient, normal-current gluing condition (U^dagger G U=G), and uniqueness of the *form* (M=mu sigma_1) all admit (mu=0). A nonzero scale does **not** follow from those symmetries alone.
4. The inequality establishes a kinematic **mass gap for a sector satisfying the stipulated transverse charge and size conditions**, not the observed Standard Model spectrum, not electroweak mass generation, and not an interacting QFT construction.

## Exact countermodel to an unconditional mass claim

Take (k=(0,0)), any finite (y), and (m=0). Then (J_perp=0) and the parent null constraint becomes (Q_K=0). No orientation-identification or boundary-current cancellation condition described above excludes this configuration by itself. Thus the statement "diagonal self-duality or boundary gluing alone forces (m>0)" is false without an additional assumption or dynamical selection rule.

## Reproduction

Run `python discovery/mass_time/transverse_spin_mass_bound.py` (SymPy). It verifies the polynomial identity, the sharp equality witness, an allowed massless zero-mode, and the unbounded-radius no-gap limit exactly.

**Relevant formal predecessors in GPPVerify:** `StandardModel/NullPairMassContactBridge.lean`, `UniqueContactMassCoupling.lean`, `MassOrderParameterLocksOrientation.lean`, `DoubledDiracBoundaryGluingCriterion.lean`, and `MasslessDoesNotImplyPremetric.lean`. The present result is an independent conditional inequality; it has **not** been checked by Lean.
