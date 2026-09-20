# BPY two-copy exponential space as a first-order doubled transport system

Date: 2026-09-20

This note continues the first-order sign program and uses the center/relative coordinates of
the exact BPY reflection colligation.

For u=x+y and v=x-y, set

a=((1-2t)/2)u.

For each spectral parameter z define

F_+(a,v;z)=exp(i z a) cos(zv/2),
F_-(a,v;z)=-i exp(i z a) sin(zv/2).

These are exactly the J-even and J-odd components P_+ Phi_z and P_- Phi_z after the
center-coordinate change. Every finite linear combination satisfies the same equations.

## 1. Exact first-order transport equations

Direct differentiation gives

partial_a F_+ + 2 partial_v F_- = 0,
partial_a F_- + 2 partial_v F_+ = 0.

Define the chiral combinations

G_L=F_+ + F_-,
G_R=F_+ - F_-.

Then

G_L=exp(i z(a-v/2)),
G_R=exp(i z(a+v/2)),

and therefore

(partial_a + 2 partial_v) G_L=0,
(partial_a - 2 partial_v) G_R=0.

Thus the BPY reflection pair is an exact two-channel null transport system on the diamond

|a|<=|u|/2.

No RH assumption enters.

## 2. Weighted SUSY gauge

For fixed u put

r_u(v)=q((u+v)/2) q((u-v)/2),
Psi_u=sqrt(r_u),

and

A_u=partial_v-Psi_u'/Psi_u.

Then

A_u(Psi_u f)=Psi_u partial_v f.

Writing

psi_+=Psi_u F_+,
psi_-=Psi_u F_-,

the transport system becomes

partial_a psi_+ + 2 A_u psi_- = 0,
partial_a psi_- + 2 A_u psi_+ = 0.

Equivalently

psi_L=psi_++psi_-,
psi_R=psi_+-psi_-

obey

(partial_a+2A_u)psi_L=0,
(partial_a-2A_u)psi_R=0.

This is a literal first-order doubled Dirac/transport form, structurally parallel to the
doubled first-order systems in Which Way Is Forward? v14.

## 3. Why local SUSY positivity does not prove the BPY contraction

The desired J-form is

||psi_+||^2-||psi_-||^2
=
Re <psi_L,psi_R>.

Differentiate at fixed u:

d/da Re<psi_L,psi_R>
=
2 Re <psi_L,(A_u-A_u^*)psi_R>.

Since

A_u=partial_v-W_u,
A_u^*=-partial_v-W_u,
W_u=Psi_u'/Psi_u,

one has

A_u-A_u^*=2 partial_v.

Therefore the first-order reflection flux is controlled by the SKEW part of A_u, not by
the positive SUSY Hamiltonian

H_u=A_u^*A_u>=0.

This exactly explains why the v34 local SUSY construction did not imply

||P_- f||<=||P_+ f||.

The positive square is the wrong observable for the missing sign.

## 4. Exact characteristic transport

Since A_u is gauge-equivalent to plain differentiation,

G_L(a,v)=g_L(v-2a),
G_R(a,v)=g_R(v+2a).

Thus the two channels propagate along opposite characteristics of the same parent diamond.

Under

xi=v-2a,
eta=v+2a,

one has da dv=(1/4)d xi d eta and the condition |a|<=u/2 becomes

|eta-xi|<=2u

for u>0.

Hence the u-slice reflection form is a weighted cross-channel scattering form on a finite
causal diamond. The RH problem is precisely the assertion that the arithmetic weight
r_u(v), after the remaining u integration with sinh(omega u), makes this cross-channel
form nonnegative on the analytic BPY boundary data.

## 5. Consequence for the orientation program

The upgraded orientation paper contributes the correct first-order interpretation:
two opposite lifts/channels and a fixed exchange symmetry.

It does NOT justify quotienting out the odd BPY channel. Doing so would replace the
de Branges form by a different positive object.

The theorem to prove is instead a genuine flux/contraction theorem for the original
analytic subspace:

||P_-f||<=||P_+f||.

Any proof that uses only H_u=A_u^*A_u>=0 has already discarded the relevant first-order
current and cannot close RH by itself.
