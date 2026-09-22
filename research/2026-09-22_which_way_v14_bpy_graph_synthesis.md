# Which Way v14 -> BPY shadow graph: exact synthesis and remaining theorem

Date: 2026-09-22

This note completes the audit begun on 2026-09-18: does the upgraded orientation/Haar
architecture determine the missing BPY odd-transfer contraction, or only expose it more
canonically?

Answer: it exposes the correct fixed polarization and physical quotient, but it does NOT
force contractivity. The remaining inequality is still the non-circular RH theorem.

## 1. Exact BPY two-copy geometry

For omega>0 the BPY construction has a positive Hilbert space H_omega=L2(mu_omega), the
swap involution

  (Jf)(t,x,y)=f(t,y,x),

and exponential states

  Phi_z(t,x,y)=exp(i z ((1-t)y-tx)).

The de Branges kernel is exactly

  L_omega(z,w)=<J Phi_w,Phi_z>.

With

  P_+=(I+J)/2,
  P_-=(I-J)/2,

one has for every finite exponential combination f

  <Jf,f>=||P_+f||^2-||P_-f||^2.

Hence de Branges positivity is equivalent to

  ||P_-f|| <= ||P_+f||

on the closed exponential subspace M_omega.

If P_+ is injective on M_omega, M_omega is the graph of the odd transfer

  C_omega : P_+ M_omega -> H_-,
  C_omega(P_+f)=P_-f,

and

  RH iff ||C_omega||<=1 for every omega>0.

## 2. What Which Way v14 contributes

The upgraded orientation paper supplies three exact structural principles relevant here.

A. Haar/deck projection is equal-weight projection, not mere symmetry:
   P_D=(I+D)/2.

This is exactly the abstract form of P_+=(I+J)/2.

B. Symmetry is not enough:
   commuting observables can retain off-diagonal coherence, so the quotient must be a
   genuine gauge/deck reduction or dynamical restriction.

This matches the BPY situation: the involution J alone does not imply J-positivity of
M_omega.

C. Signed first-order generator versus positive magnitude:
   L=Qh with Q^2=1 and h>=0.

This identifies the correct order of construction: keep the odd/even sign structure before
forming the positive square.

## 3. The key conclusion

The Haar/orientation quotient DOES NOT determine C_omega.

The reason is elementary. P_+ fixes the even component of a vector, but the embedding of
the analytic exponential subspace M_omega into H_+ direct-sum H_- determines which odd
component accompanies it. Many graph subspaces

  Graph(C)={x direct-sum Cx}

have exactly the same fixed involution J and the same even Haar projector P_+, with C
ranging over arbitrary closed operators compatible with the domain.

Thus orientation symmetry selects the decomposition

  H_omega=H_+ direct-sum H_-,

but arithmetic/analytic structure selects the graph C_omega.

Contractivity

  C_omega^* C_omega <= I

is additional information. It is exactly equivalent to positivity of the BPY/de Branges
kernel and cannot be obtained from the Z2 quotient alone without circularity.

This is the infinite-dimensional analogue of the finite four-prime calculation where the
Haar-even compression becomes Hermitian but can remain indefinite.

## 4. Explicit center/relative form

Put

  u=x+y,
  v=x-y.

Then

  P_+ Phi_z = exp(i z(1-2t)u/2) cos(zv/2),
  P_- Phi_z = -i exp(i z(1-2t)u/2) sin(zv/2).

Thus C_omega is the analytic map carrying the cosine channel to the sine channel on the
special BPY exponential span.

For a single fixed z the pointwise ratio is formally

  -i tan(zv/2),

but C_omega is NOT a multiplication operator on the full graph, because linear combinations
with different z share the same weighted two-copy measure. Proving ||C_omega||<=1 is
therefore a genuine coupled integral inequality, not a local trigonometric bound.

## 5. Fixed-Haar metric rigidity still matters

Although it does not prove the contraction, the fixed-Haar metric rules out an otherwise
fatal loophole: fitting the metric to an off-critical spectral parameter.

The finite theorem in CayleyHaarMetricRigidity.lean says that for a reciprocal shadow
block Q_a, any nondegenerate swap-invariant metric which makes Q_a skew-adjoint forces

  a^-1=conj(a),

hence |a|=1. For a=beta(s), Re(s)=1/2.

Therefore if the global arithmetic resonance is realized in the fixed Haar Hilbert space
with functional shadow acting as the Hilbert adjoint, criticality follows automatically.
The missing step is arithmetic admissibility/causality of that resonance, not metric
selection.

## 6. Co-Poisson charged-Kahler structure

On the completed Mellin boundary

  A_xi=M_Xi R

has the exact polar form

  A_xi=Q_xi h_xi,
  h_xi=M_|Xi|>=0,
  Q_xi=M_sgn(Xi) R.

Together with Sigma=sgn(T), one has

  Q_xi Sigma=-Sigma Q_xi,

so

  K_xi=Q_xi Sigma

is skew-adjoint with

  K_xi^2=-I,
  K_xi^4=I.

Thus the completed arithmetic boundary already has the same two-lift/quarter-turn algebra
as Which Way v14.

However, A_a=M_{xi(a+it)}R is self-adjoint for every real a, so this polar/quaternionic
structure alone does not select a=1/2. Causal Hardy compatibility remains essential.

## 7. Prime/Koszul and Archimedean status

The finite Mobius/Koszul bulk provides the correct sign/orientation algebra but its raw
Hodge determinant is additive-energy, not the zeta Euler determinant.

A grading-twisted completion satisfies

  (D_p+i m Gamma)^2=D_p^2-m^2 I

when Gamma anticommutes with D_p. This escapes the earlier positive-square completion
no-go but does not identify m with the actual Archimedean channel.

The correct scalar arithmetic determinant already appears instead as the bordered
prime-Archimedean Schur response. Therefore the Fock/Koszul sector should be treated as
internal orientation/cancellation structure feeding a boundary transfer, not as the
characteristic determinant itself.

## 8. Final sharpened target

The remaining theorem can now be stated in one line:

  Prove that the explicitly constructed BPY analytic graph M_omega is a contractive graph
  over its Haar-even projection for every omega>0.

Equivalently,

  ||P_- f||^2 <= ||P_+ f||^2  for all f in M_omega.

Equivalent forms already obtained:
- positivity of the de Branges defect kernel;
- innerness/isometry of the completed causal transfer;
- vanishing incoming Julia defect;
- absence of the bad-zero model space K_B;
- RH.

Which Way v14 materially strengthens the geometry and fixes the polarization, but it does
not by itself prove this inequality.

## 9. Best constructive subtarget

The explicit relative-coordinate weight is

  r_u(v)=q((u+v)/2) q((u-v)/2),

with even ground state Psi_u=sqrt(r_u(v)) and SUSY operator

  A_u=d/dv-Psi_u'/Psi_u,
  H_u=A_u^*A_u>=0.

The next non-circular analytic target is a uniform inequality on the restricted analytic
exponential span comparing sine and cosine channels:

  integral |sum c_j e^{iz_j(1-2t)u/2} sin(z_j v/2)|^2 dmu
  <=
  integral |sum c_j e^{iz_j(1-2t)u/2} cos(z_j v/2)|^2 dmu.

A proof must exploit the special BPY weight and analyticity jointly; pointwise sin/cos
bounds, symmetry alone, or generic SUSY positivity are insufficient.

This is the exact frontier.
