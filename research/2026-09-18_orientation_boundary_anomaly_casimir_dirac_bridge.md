# Orientation boundary anomaly and the discrete Casimir-Dirac bridge

Date: 2026-09-18

Status: exact operator identities plus a new project-internal synthesis. No RH proof is claimed.

## 1. Motivation from Which Way Is Forward v13

The orientation paper has an exact doubled first-order factorization

D_- D_+ = -(Q_K + |q|^2) I_8,

with q=0 giving decoupled four-component incidence equations and q!=0 locking them. Mass is interpreted there as a transverse norm.

The current RH attack independently produced the unilateral discrete Casimir Laplacian

L = 2I - S - S*

on l2(N), with every strictly positive mass killing the dual ghost and only the zero-mass threshold remaining.

The two structures admit an exact common first-order form.

## 2. Massive causal factor

Let S be the unilateral shift, S* S = I and S S* = I - P_0. For 0<r<1 define

A_r = r^{-1/2}(I-rS).

Then

A_r* A_r
= r^{-1}(I-rS*)(I-rS)
= L + m_r^2 I,

where

m_r^2 = r + r^{-1} - 2 = (1-r)^2/r.

The reverse ordering gives

A_r A_r*
= r^{-1}(I-rS)(I-rS*)
= L + m_r^2 I - r P_0.

Therefore

A_r* A_r - A_r A_r* = r P_0.

The entire causal/adjoint asymmetry is a rank-one boundary projection.

## 3. Doubled discrete Dirac operator

Define the self-adjoint doubled first-order operator

D_r = [[0, A_r*], [A_r, 0]].

Then

D_r^2
= diag(A_r* A_r, A_r A_r*)
= diag(L+m_r^2 I, L+m_r^2 I-rP_0).

This is the exact discrete counterpart of a first-order doubled factorization whose square is kinetic plus mass-squared. The two partner sectors agree in the bulk and differ only by the boundary anomaly rP_0.

At r<1, A_r is boundedly invertible:
A_r^{-1} = sqrt(r) sum_{n>=0} r^n S^n,
with exact norm ||A_r^{-1}|| = sqrt(r)/(1-r) = 1/m_r.
Thus positive mass is exactly bounded invertibility/coercivity of the first-order causal factor.

At r->1, m_r->0, A_r->I-S and the inverse becomes unbounded. This is the zero-mass threshold where the RH ghost can escape.

## 4. Golden self-consistent point

The unit-mass condition m_r^2=1 is

(1-r)^2/r = 1,

equivalently

r=(1-r)^2,

so

r=phi^{-2}, 1-r=phi^{-1}.

At this point

||A_r^{-1}||=1.

Thus the golden contraction is the unique causal factor for which the normalized discrete Dirac mass is one and the inverse first-order factor has unit norm.

This is the same r=phi^{-2} independently obtained from:
- the minimal trace-3 hyperbolic SL2(Z) sector;
- the q=5 finite-place shadow kernel;
- the unit-mass Casimir transfer recurrence.

## 5. Orientation reversal = causal/adjoint dualization

On the bilateral spectral variable z=e^{i theta}, the causal symbol is

a_r(z)=r^{-1/2}(1-rz).

Orientation reversal theta -> -theta, equivalently z -> z^{-1}=conj(z) on |z|=1, sends

a_r(z) -> a_r(z^{-1}) = conjugate(a_r(z)),

which is the adjoint first-order factor.

The orientation-even bulk product is

a_r(z^{-1}) a_r(z)
= m_r^2 + 2 - z - z^{-1}.

This realizes, inside the RH operator model, the orientation paper's exact principle that reversal of a one-dimensional unitary character sends it to its dual/adjoint.

## 6. Bulk orientation blindness versus boundary witness

On the bilateral shift U on l2(Z), U*U=UU*=I, hence causal and adjoint orderings coincide:

A_r* A_r = A_r A_r*.

On the unilateral/casual Hardy shift S on l2(N), the compression creates

S*S - SS* = P_0,

and consequently

A_r* A_r - A_r A_r* = rP_0.

Thus orientation order is invisible in the translation-invariant bulk and becomes detectable only after imposing a causal boundary. The boundary vacuum P_0 is the complete witness of the ordering/orientation choice.

This is a precise operator model for the paper's question "Which way is forward?": without a boundary the two factor orderings are equivalent; after causal half-space compression, forward/backward factorization differs by a rank-one boundary index.

## 7. Relation to the RH ghost

Previous results in this research cycle show:
- every m_r^2>0 graph kills the dual Nyman ghost;
- a nonzero obstruction can only be a zero-mass threshold resonance;
- normalized arithmetic decimation drives finite Casimir bulk energy to zero while a hypothetical ghost must retain its boundary charge.

The present factorization explains that geometry: the zero-mass limit destroys bounded invertibility of the causal first-order operator while the rank-one boundary witness survives. Therefore the RH obstruction is naturally interpreted as a boundary/threshold defect of an otherwise orientation-dual bulk factorization.

This is not yet a proof. The required theorem remains: show that the full multiplicative dilation constraints cannot support a nonzero threshold boundary charge.

## 8. Direct relation to the doubled Lorentzian/transverse-mass paper

The structural dictionary is now:

Which Way Is Forward:
  first-order doubled Klein/Clifford maps D_±
  square -> Q_K + |q|^2
  q=0 decouples half-spin sectors
  q!=0 locks them
  mass = transverse norm

RH/Casimir:
  first-order causal factors A_r, A_r*
  square -> L + m_r^2
  m=0 loses coercivity and admits threshold escape
  m>0 locks/inverts the causal channel
  causal vs adjoint order differs only by boundary P_0

This is an exact operator-level correspondence of architecture. No identification of the physical mass |q| with the arithmetic regulator m_r is claimed yet. A genuine unification would require an intertwiner between the finite-dimensional doubled Klein carrier and the Hardy/Casimir boundary representation.

## 9. Next attack

1. Build the quarter-turn on the doubled Hardy carrier:
   J(f,g)=(-g,f), J^2=-I, J^4=I.
2. Compute how J and the sector-swap conjugate D_r, A_r and A_r*.
3. Identify the boundary projection P_0 as the obstruction to exact orientation/deck symmetry after unilateral compression.
4. Combine with multiplicative decimation U_m and the ghost constraints.
5. Seek a theorem that all-m dilation covariance annihilates the surviving P_0 threshold charge.

