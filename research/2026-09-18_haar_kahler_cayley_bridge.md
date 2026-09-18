# Haar–Kähler–Cayley bridge on the RH principal-series carrier

Date: 2026-09-18

This note incorporates the exact charged-Kähler structure and doubled-orientation lessons from
Which Way Is Forward? v14 into the RH first-order program.

## 1. Fixed Haar Hilbert space

Use logarithmic scale

u=log r

on the multiplicative Haar group R_+^x. Then dr/r=du and the canonical Hilbert space is

H = L^2(R,du).

The Stone generator of scale translations is

A=-i d/du

with its standard self-adjoint domain H^1(R).

Let

h=|A|,
Q=sgn(A).

Since A has no L2 zero eigenvector on R, Q^2=I and

A=Q h,
h>=0,
[Q,h]=0.

Thus the canonical Haar dilation generator is already in the exact charged-Kähler normal
form L=Qh emphasized in Which Way Is Forward v14.

On the realification of H define

J=iI,
I_K=iQ.

Then

J^2=I_K^2=-I,
[I_K,J]=0,
-I_K J=Q.

So the same "two commuting quarter turns -> relative Z2 sign" algebra occurs canonically
on the RH principal-series Haar carrier, with Q the sign of the dilation frequency.

This is an exact operator identity and uses no zeta zeros.

## 2. Reflection leaves the positive magnitude invariant and flips the sign

Let R be logarithmic orientation reversal,

(Rf)(u)=f(-u).

Then R is a unitary involution and

R A R=-A.

Functional calculus therefore gives

R h R=h,
R Q R=-Q.

Hence the positive spectral magnitude is orientation-even while the first-order frequency
sign is orientation-odd. This is the infinite-dimensional Haar analogue of the signed
frequency/positive energy theorem in ChargedKahlerDynamicalSign.lean.

## 3. The RH Cayley coordinate is the operator Cayley transform of A

Define the bounded Cayley transform

U_beta=(2A+iI)(2A-iI)^(-1).

Because A is self-adjoint, U_beta is unitary.

On the generalized Fourier mode exp(i gamma u), A has eigenvalue gamma, hence

U_beta exp(i gamma u)
=
[(2 gamma+i)/(2 gamma-i)] exp(i gamma u).

But

beta(1/2+i gamma)
=
[(1/2+i gamma)-1]/[1/2+i gamma]
=
(2 gamma+i)/(2 gamma-i).

Therefore

U_beta(gamma)=beta(1/2+i gamma).

This is the exact operator realization of the scalar Cayley coordinate used in
CayleyShadowAdjointBridge.lean.

Moreover

R U_beta R
=
(-2A+i)(-2A-i)^(-1)
=
(2A-i)(2A+i)^(-1)
=
U_beta^*
=
U_beta^(-1).

Thus on the FIXED Haar metric, scale reflection is literally Hilbert adjoint for the Cayley
transfer.

This is stronger than the scalar statement: the metric, the self-adjoint generator, and the
reflection are all fixed before any arithmetic spectral parameter is inserted.

## 4. Off-line labels are complex frequencies

For

s=1/2+delta+i gamma,

the associated half-density character is

chi_s(u)=exp((s-1/2)u)=exp(delta u) exp(i gamma u).

Formally

A chi_s=(gamma-i delta) chi_s.

Thus an off-critical displacement delta is exactly the imaginary part of the generalized
frequency of the self-adjoint Haar generator.

If delta!=0, chi_s grows exponentially in one direction and is not a tempered distribution.
This analytic statement is already formally proved in

GppVerify/RiemannHypothesis/ExpNotTempered.lean

and packaged as

GppRH.temperedness_iff_critical_line.

Hence any nonzero arithmetic resonance that is genuinely realized as a tempered generalized
eigenstate of this fixed self-adjoint Haar generator must have delta=0.

## 5. Exact remaining theorem

The non-circular RH target can now be stated sharply:

ARITHMETIC HAAR ADMISSIBILITY.
For every nontrivial zeta zero rho=1/2+delta+i gamma, the zero contribution to the explicit
formula is represented by a nonzero tempered generalized state of the fixed Haar dilation
generator A in the arithmetic GNS/rigged-Hilbert completion.

Combined with the proved temperedness theorem, this would force delta=0.

This is NOT yet proved. It is the same hard bridge that earlier appeared as
Meyer spectral admissibility / zero-evaluation temperedness. The new gain is that the target
operator and its polarization are no longer ambiguous.

## 6. Why the old Haar/Wightman paper does not close the bridge

Haar Positivity: From Weil to Wightman constructs a positive Hilbert form after assuming

omega(Theta(A)A)>=0.

In the arithmetic specialization this is precisely Weil positivity, hence RH-equivalent.
Therefore that paper is a correct unification of positivity languages but cannot supply
arithmetic admissibility by itself.

The first-order program must instead construct the zero/resonance channel in the fixed Haar
space before invoking positivity.

## 7. Strengthened finite metric rigidity from Which Way v14

Which Way v14 correctly stresses that Z2 symmetry alone allows off-diagonal coherence.
Accordingly one must not assume a diagonal shadow-pair metric.

Let

D=[[0,1],[1,0]],
Q_a=[[0,-a^-1],[a,0]],

and let G be any nondegenerate metric with

D^* G D=G.

Swap invariance forces only G_11=G_00; off-diagonal terms may remain.

If Q_a is skew-adjoint in this SAME metric,

Q_a^*G+GQ_a=0,

the (0,1) entry gives

conj(a) G_11 - G_00/a=0.

Using G_11=G_00!=0 gives

a^-1=conj(a),

hence |a|=1.

For a=beta(s), this forces Re(s)=1/2.

This result is formalized in

GppVerify/RiemannHypothesis/CayleyHaarMetricRigidity.lean

on the active branch.

## 8. Hardy folding / doubled-parent interpretation

For the shifted completed boundary quotient Theta_omega, multiplication U_omega=M_Theta on
boundary L2 is unitary independently of RH. Split the boundary into causal and anticausal
Hardy halves.

For f in H2_+,

U_omega f = T_omega f + H_omega f,

with T_omega in H2_+ and H_omega in H2_-.

Unitarity gives

T_omega^*T_omega + H_omega^*H_omega=I.

With

M_omega=|H_omega|=(H_omega^*H_omega)^(1/2),

the reduced causal channel obeys

T_omega^*T_omega + M_omega^2=I.

This is an exact operator-valued "folded parent" identity:
- the full boundary parent is lossless/unitary;
- the causal observed sector is reduced;
- the transverse/hidden channel is the anticausal Hankel leakage;
- its positive magnitude M_omega locks the two Hardy orientations;
- RH is exactly M_omega=0 for every omega>0.

This is structurally parallel to the v14 null-parent/massive-locking theorem, where a
positive transverse norm locks two chiral halves. No physical identification is claimed;
the exact common algebra is a unitary parent whose reduced sector acquires a positive
transverse coupling.

## 9. Immediate next target

Construct the prime–Archimedean arithmetic transfer as a strong limit of finite multichannel
lossless colligations in the FIXED Haar metric.

If finite causal transfers T_N are isometries and

T_N -> T_omega strongly,

then

||T_omega f||=lim ||T_N f||=||f||

for every f, so T_omega is an isometry and H_omega=0.

This would prove the required no-leakage statement without starting from Weil positivity.

Naive scalar prime cascades cannot do this because of the already-proved excess Clark
density. Therefore the finite approximants must use the Möbius/Koszul internal channels and
the Archimedean coupling before scalar compression.

That finite-to-global strong-isometry theorem is now the primary constructive target.
