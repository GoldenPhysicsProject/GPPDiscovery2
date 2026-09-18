# Canonical global Julia colligation and identification of the bad-zero defect channel

Date: 2026-09-18

Let Theta_omega be the shifted completed shadow quotient on the real boundary and let

U_omega=M_{Theta_omega}

on L2(R). Since |Theta_omega|=1 on R, U_omega is unitary.

Let P=Pi_+ be the upper Hardy projection and define the causal Toeplitz compression and anticausal Hankel leakage

T_omega=P U_omega | H2_+,
H_omega=(I-P) U_omega | H2_+.

## 1. Exact input defect identity

Unitarity of U gives for f in H2_+:

||T_omega f||^2+||H_omega f||^2=||f||^2.

Therefore

T_omega^* T_omega + H_omega^* H_omega = I.

The input defect operator is

D_omega=(I-T_omega^*T_omega)^(1/2)
       =(H_omega^*H_omega)^(1/2).

RH is equivalent to D_omega=0 for every omega>0.

## 2. Global first-order skew Dirac

Define on H2_+ direct-sum H2_+

Q_omega=
[[0,-T_omega^*],
 [T_omega,0]].

Then Q_omega^*=-Q_omega and

-Q_omega^2
=
diag(T_omega^*T_omega, T_omega T_omega^*)
>=0.

On the incoming copy,

I+Q_omega^2 = I-T_omega^*T_omega = D_omega^2 = H_omega^*H_omega.

Thus the failure of the first-order skew operator to be an exact complex structure is exactly the positive ghost/leakage defect.

This is the first-order global counterpart of the local identity X^*=-X -> -X^2=X^*X>=0.

## 3. Canonical Julia/Halmos unitary colligation

For any contraction T define

D_T=(I-T^*T)^(1/2),
D_{T^*}=(I-TT^*)^(1/2).

The Julia operator

J(T)=
[[T, D_{T^*}],
 [D_T, -T^*]]

is unitary. Taking T=T_omega gives a canonical ZERO-INDEPENDENT global multichannel unitary colligation constructed directly from the arithmetic function xi through Theta_omega.

The local prime colligation

S_p=
[[a_p,b_p],
 [b_p,-a_p]],
a_p=p^-1/2,
b_p=sqrt(1-a_p^2),

is exactly J(T) in the scalar case T=a_p. Thus the local Euler shadow beam splitter and the global Hardy boundary colligation are instances of the same Julia construction.

This supplies the matrix-valued positive completion that v34 identified abstractly as necessary; however its input defect D_omega is precisely the unresolved RH channel, so unitarity of the enlarged colligation alone does not prove RH.

## 4. Bad-zero inner factor gives the input defect projection exactly

Suppose the shifted boundary function has canonical inner quotient factorization

Theta_omega = I_omega / B_omega

on the boundary, where I_omega is inner and B_omega is the Blaschke product of poles of Theta in the upper half-plane, equivalently zeros of xi to the right of the shifted line Re(s)=1/2+omega.

Boundary-wise 1/B=conj(B), and since I is analytic inner,

T_omega = T_{I_omega} T_{B_omega}^*.

Because T_I is an isometry,

T_omega^*T_omega
=
T_B T_I^* T_I T_B^*
=
T_B T_B^*.

For inner B,

T_B T_B^*=P_{B H2},

hence

I-T_omega^*T_omega
=
P_{K_B},

where

K_B=H2_+ minus B H2_+.

Therefore

D_omega^2=P_{K_{B_omega}},
and since a projection is its own positive square root,

D_omega=P_{K_{B_omega}}.

Thus the canonical Julia input defect space is EXACTLY the Nyman-Burnol bad-zero model space. This unifies:
- anticausal Hardy leakage;
- the input defect of the global Julia colligation;
- the Nyman ghost space K_B;
- failure of the order-four law;
- poles of the shifted shadow quotient.

RH is exactly the statement that the global Julia colligation has no incoming defect channel for every omega>0.

## 5. Output defect is different and survives RH

The output defect

D_{T^*}^2=I-TT^*

need not vanish under RH. If Theta is inner, T_Theta is an isometry but generally not onto; its output defect is the model space

H2_+ minus Theta H2_+,

which encodes the ordinary critical-line zero spectrum.

Hence the Julia colligation separates two kinds of defect cleanly:

INPUT defect D_T:
  bad/off-line zeros; vanishes iff RH.

OUTPUT defect D_{T^*}:
  ordinary model-space spectral content; may remain nonzero under RH.

This resolves a recurring confusion in earlier 'unitarity' arguments. One must prove isometry of the causal transfer, not surjectivity.

## 6. Ghost entropy and vacuum leakage

Because D_omega=P_{K_B},

||D_omega 1||^2
=
||P_{K_B}1||^2
=
1-|B(0)|^2.

With

S_ghost=-log|B(0)|^2,

this is

||D_omega1||^2=1-exp(-S_ghost).

Thus the previously defined ghost entropy is literally the vacuum coupling probability into the Julia input-defect channel.

## 7. First-order sign principle

The global causal transfer T is the first-order object. Squaring gives

T^*T=I-P_{K_B}.

If one starts only from the positive operator T^*T, the phase/orientation data of how the defect arose can be lost. The Julia colligation retains T and its two defect channels before squaring.

The project target is therefore sharpened:
construct T_omega from the prime-Archimedean first-order network in a way that makes the incoming defect channel visibly absent, rather than trying to infer RH from an already-squared positive form.

## 8. Next calculation

Identify the v34 'escaped boundary heat trace' with a regularized trace on the input defect model space K_B, using the compressed shift/model operator on K_B. If exact, the no-escaped-trace criterion becomes literal conservation of the Julia input channel.