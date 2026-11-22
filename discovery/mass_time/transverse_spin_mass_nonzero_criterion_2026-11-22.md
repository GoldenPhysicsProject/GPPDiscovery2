# Finite transverse radius and spinorial angular charge force a nonzero reduced mass

**Date:** 2026-11-22  
**Status:** Exact conditional theorem in the real transverse phase-plane; symbolic regression checked. Not a derivation of nonzero mass from orientation symmetry alone.

## Setting

In the doubled-null parent of *Which Way Is Forward?* v29, let

$$
y=(y_1,y_2),\qquad k=(k_1,k_2)\in\mathbb R^2.
$$

The parent null constraint $Q_8=Q_K+|k|^2=0$ gives $Q_K=-m^2c^2$ when the reduced mass is defined by $|k|=mc$. The canonical transverse angular momentum is

$$
J_\perp=y_1k_2-y_2k_1.
$$

## Theorem: transverse angular mass lower bound

Suppose $c>0$, $\hbar>0$, $0<R<\infty$, $|y|\le R$, $m=|k|/c$, and

$$
|J_\perp|\ge\hbar/2.
$$

Then

$$
\boxed{m\ge \frac{\hbar}{2cR}>0.}
$$

**Proof.** The two-dimensional Lagrange identity states

$$
|y|^2|k|^2=(y_1k_2-y_2k_1)^2+(y_1k_1+y_2k_2)^2.
$$

Consequently $|J_\perp|\le |y||k|\le Rmc$, yielding the bound.

The bound is sharp: choose $y=(R,0)$ and $k=(0,\hbar/(2R))$. Then $J_\perp=\hbar/2$ and $m=\hbar/(2cR)$. No circular trajectory, constant-radius dynamics, or vanishing radial momentum is needed for the inequality.

For any prescribed nonzero $J_\perp$ and finite $|y|$, the same identity forces $m>0$. A **uniform** positive mass bound requires a uniform finite radius $R$.

## Connection to the transverse spin cover

WWIF v29 derives the transverse canonical one-form

$$
k_aDy^a=p_rdr+J_\perp(d\theta-\Omega)
$$

and proposes that spinorial transverse angular weights $n_\perp=2J_\perp/\hbar$ are odd. **If** the physical sector has a genuine nonzero transverse spinorial weight $n_\perp\in 2\mathbb Z+1$, then $|J_\perp|\ge\hbar/2$. Combined with a finite transverse-radius bound, the theorem excludes $m=0$.

This strengthens the paper's conditional constant-radius, purely angular zitter construction: a positive mass lower bound follows without postulating an orbit.

### Exact boundaries of the result

1. A nontrivial **Lorentz spin** representation does not by itself force nonzero **canonical transverse orbital angular momentum** $J_\perp=y\times k$. Their physical identification requires an independent bundle and operator intertwiner.
2. No finite physical radius $R$ has yet been derived from double-sheet boundary sewing or the projective quotient. Without it, the fixed-$J$ family $y=(r,0)$ and $k=(0,\hbar/(2r))$ has $m=\hbar/(2cr)\to0$ as $r\to\infty$.
3. The diagonal orientation quotient, the finite boundary-current gluing condition $U^\dagger G U=G$, and the uniqueness of the operator *form* $M=\mu\sigma_1$ all permit $\mu=0$. The scale does **not** follow from those symmetries alone.
4. The conditional bound is not the observed Standard Model mass spectrum, a proof that all fermions are massive, a Higgs/Yukawa construction, or an interacting QFT.

## Exact countermodel to unconditional mass generation

Let $k=(0,0)$, take any finite $y$, and put $m=0$. Then $J_\perp=0$ and the parent null constraint reduces to $Q_K=0$. The diagonal orientation quotient and finite current-cancellation sewing criterion do not by themselves exclude this configuration. Therefore **boundary orientation symmetry alone does not force positive mass**.

## Reproduction

Run the adjacent Python file, discovery/mass_time/transverse_spin_mass_bound.py (SymPy). It symbolically verifies the Lagrange identity, a sharp equality witness, a massless zero-mode, and the no-gap unbounded-radius limit.

Relevant predecessors in GPPVerify: StandardModel/NullPairMassContactBridge.lean, UniqueContactMassCoupling.lean, MassOrderParameterLocksOrientation.lean, DoubledDiracBoundaryGluingCriterion.lean, and MasslessDoesNotImplyPremetric.lean.

**Verification status:** paper proof and exact SymPy identity tests; **not** compiled in Lean.
