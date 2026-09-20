# BPY graph is unconditional; exact SUSY representation of the odd transfer

Date: 2026-09-20

This sharpens the v34 two-copy BPY reflection colligation and continues the 2026-09-19
Dirac/log-concavity analysis.

## 1. Characteristic coordinates

For

Phi_z(t,x,y)=exp(i z ((1-t)y-tx)),

put

u=x+y,
v=x-y,
c=(1-2t)u/2,
a=c-v/2,
b=c+v/2.

Then

Phi_z=exp(i z a),
J Phi_z=exp(i z b),

where J swaps x and y.

Thus every vector in the closed BPY exponential subspace M_omega lies in the closed
sigma(a)-measurable subspace: it has the form F(a) for an L2 equivalence class F in the
appropriate marginal space.

## 2. Pushforward to (a,b) has strictly positive density

The BPY measure is

dmu_omega
=
(x+y)sinh(omega(x+y)) q(x)q(y) dt dx dy.

The change of variables above gives, after integrating the remaining u coordinate and
pairing u with -u,

dnu_omega(a,b)
=
H_omega(a,b) da db,

where exactly

H_omega(a,b)
=
2 int_{|(a+b)/2|}^infinity
sinh(2 omega r)
q(r+(a-b)/2)
q(r-(a-b)/2) dr.

This is the coordinate kernel already occurring in v34.

The BPY density q is positive almost everywhere (in the explicit BPY law it is smooth
positive), and for omega>0 the displayed integrand is positive for r>|a+b|/2.
Consequently

H_omega(a,b)>0

for every real a,b.

## 3. Unconditional injectivity of P_+ on M_omega

Let P_+=(I+J)/2. Suppose f in M_omega and P_+ f=0.

Write f=F(a). Then

F(a)+F(b)=0

for mu_omega-a.e. point, hence for nu_omega-a.e. (a,b). Since H_omega(a,b)>0 everywhere,
this holds for Lebesgue-a.e. pair (a,b).

By Fubini, for almost every b the equality holds for almost every a. Choosing two such
values b1,b2 gives

F(a)=-F(b1)=-F(b2)

for almost every a, so F is a.e. constant. Substituting back gives 2F=0, hence F=0.

Therefore

boxed(
ker(P_+ | M_omega) = {0}
)

for every omega>0.

The phrase "whenever P_+ is injective" in v34 can therefore be removed.

## 4. The BPY subspace is an honest closed operator graph

Define

D(C_omega)=P_+ M_omega

and

C_omega(P_+ f)=P_- f.

Injectivity above makes C_omega well-defined.

The unitary decomposition

f -> (P_+f,P_-f)

maps the closed subspace M_omega onto graph(C_omega). Hence graph(C_omega) is closed.
Therefore C_omega is a canonical closed operator before RH is assumed.

The Krein form on its graph is

[Jf,f]
=
||P_+f||^2-||P_-f||^2
=
||g||^2-||C_omega g||^2.

Thus RH is exactly the statement that this already-defined closed graph is contractive:

boxed(
RH iff ||C_omega g|| <= ||g||
for every g in D(C_omega), every omega>0.
)

No graph-existence hypothesis remains.

## 5. Exact 1+1 first-order system

Pair +/-u and put y=v/2. For fixed u>0 define

rho_u(y)=q(u/2+y)q(u/2-y),
Psi_u=sqrt(rho_u),
W_u=Psi_u'/Psi_u.

For f=F(c-y),

g=P_+f=[F(c-y)+F(c+y)]/2,
h=P_-f=[F(c-y)-F(c+y)]/2.

Exactly,

partial_c g + partial_y h = 0,
partial_c h + partial_y g = 0.

Let

G=Psi_u g,
H=Psi_u h,
A_u=partial_y-W_u.

Because Psi_u is independent of c,

boxed(
A_u H = -partial_c G,
A_u G = -partial_c H.
)

Parity is fixed:
G is even in y,
H is odd in y,
Psi_u is even,
W_u is odd.

## 6. Uniform SUSY partner gap and exact inverse formula

The 2026-09-19 strong-log-concavity calculation gives

partial_y^2 log rho_u <= -20

uniformly in u,y, hence

W_u'<=-10.

Therefore

A_u A_u^*
=
-partial_y^2 + W_u^2-W_u'
>=10 I.

In particular A_u A_u^* is invertible and

||(A_u A_u^*)^(-1)|| <= 1/10.

The kernel of A_u is span{Psi_u}, which is even. Since H is odd, H is orthogonal to ker A_u.

From

A_u H=-partial_c G

and the standard Moore-Penrose identity on ker(A_u)^perp,

A_u^*(A_u A_u^*)^(-1) A_u H=H.

Hence

boxed(
H
=
-A_u^*(A_u A_u^*)^(-1) partial_c G.
)

This is the exact slice representation of the BPY odd graph coordinate.

Taking norms gives the exact quadratic identity

boxed(
||H||_y^2
=
<partial_c G,
 (A_u A_u^*)^(-1) partial_c G>_y
)

and therefore the unconditional estimate

boxed(
||H||_y^2 <= (1/10)||partial_c G||_y^2.
)

After integration over c,u with the positive factor 2sinh(omega u), the same inequality
holds globally.

## 7. What remains after the gap

This does NOT yet prove

||H|| <= ||G||.

It proves that the odd leakage is a center-derivative energy filtered through the inverse
relative SUSY Hamiltonian.

For a pure center Fourier frequency k, the sufficient estimate is

k^2 < 10.

Thus the entire unresolved RH content has been pushed into the ultraviolet center-frequency
sector.

The second first-order equation prevents G from being arbitrary, but fixed-u slices are known
to have sign-changing reflected Fourier transforms. Therefore no argument that simply drops
the u/c wedge coupling can close the theorem.

The sharpened target is now:

prove on the analytic BPY graph subspace, with the full wedge |c|<=u/2 and u-weight
2sinh(omega u), that

<partial_c G,(A_u A_u^*)^(-1)partial_c G>
<=
||G||^2.

Equivalently, show that the center derivative is contractive relative to the variable
relative-SUSY metric selected by the BPY density.

This is a concrete first-order energy inequality, not an abstract positivity slogan.

## 8. Canonical real structure

Coefficient conjugation

(Kf)(t,x,y)=conj(f(t,x,y))

is antiunitary, commutes with J, and maps

K Phi_z = Phi_{-conj(z)}.

Since z in C_+ implies -conj(z) in C_+, K preserves M_omega.

Therefore K preserves the even and odd sectors and the graph operator is real:

C_omega K_+ = K_- C_omega

on its domain.

This supplies the exact anti-linear real structure predicted by the orientation-carrier
analysis, but it imposes symmetry, not contractivity.

Status: exact analytic derivation, zero-independent, no RH claim.
