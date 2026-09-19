# Uniform strict log-concavity of the Riemann/BPY density

Date: 2026-09-19

This is an unconditional analytic property of Riemann's Fourier density Phi.  It is useful
for the BPY relative-coordinate supersymmetric operator but does not by itself prove RH.

Recall for u>=0

Phi(u)
=
sum_{n>=1}
[4 pi^2 n^4 e^(9u/2)-6 pi n^2 e^(5u/2)]
e^(-pi n^2 e^(2u)).

Every summand is positive for u>=0.

Put

x=pi e^(2u) >= pi >3

and write Phi=sum phi_n.  Up to an irrelevant common positive constant,

phi_n
=
n^2 x^(5/4)(2 n^2 x-3)e^(-n^2 x).

Let

a_n=n^2 x,
ell_n=log phi_n.

Then differentiation with respect to u gives the exact formulas

ell_n'
=
5/2 + 4a_n/(2a_n-3)-2a_n
=
9/2 + 6/(2a_n-3)-2a_n,

and

boxed(
ell_n''
=
-4a_n - 24a_n/(2a_n-3)^2
<=
-4a_n
<=
-4x
).

## Mixture curvature identity

Let

p_n=phi_n/Phi.

Then

boxed(
(log Phi)''
=
sum_n p_n ell_n''
+
Var_p(ell_n')
).

The first term is at most -4x.

It remains to bound the slope variance.

Use a_1=x and, for n>=2,

r_n:=phi_n/phi_1
=
n^2 (2n^2x-3)/(2x-3)
e^(-(n^2-1)x).

Since x>=3,

boxed(
r_n
<=
2 n^4 e^(-(n^2-1)x)
).

Also

ell_n'-ell_1'
=
-2x(n^2-1)
+
6/(2n^2x-3)
-
6/(2x-3),

so

|ell_n'-ell_1'|
<=
2x(n^2-1)+2.

Because x(n^2-1)>=9,

boxed(
|ell_n'-ell_1'|
<=
(20/9)x(n^2-1)
).

Since variance is minimized over constants,

Var_p(ell_n')
<=
sum_{n>=2} p_n |ell_n'-ell_1'|^2
<=
sum_{n>=2} r_n |ell_n'-ell_1'|^2.

Therefore

Var_p(ell_n')
<=
(800/81)x^2
sum_{n>=2}
n^4(n^2-1)^2
e^(-(n^2-1)x).

For n>=2 the function

x^2 e^{-(n^2-1)x}

is decreasing on x>=3. Hence

Var_p(ell_n')
<=
(800/9) S,

where

S
=
sum_{n>=2}
n^4(n^2-1)^2 e^{-3(n^2-1)}.

The n=2 contribution is

144 e^{-9}<0.018.

For n>=3,

n^4(n^2-1)^2<n^8,

and the terms

t_n=n^8 e^{-3(n^2-1)}

have ratio

t_{n+1}/t_n
=
((n+1)/n)^8 e^{-3(2n+1)}
<=
(4/3)^8 e^{-21},

so the entire n>=3 tail is far below 0.002. Thus the very conservative bound

boxed(S<1/50)

holds.

Consequently

Var_p(ell_n') < 16/9.

Combining with x>=3 gives

(log Phi)''
<
-12 + 16/9
=
-92/9
<
-10

for u>=0.

Phi is even, so the same holds on u<=0. At u=0 the even derivative is smooth and the
same estimate applies by continuity.

Therefore

boxed(
(log Phi(u))'' <= -10
for all real u
)

with substantial numerical margin.  The constant 10 is not optimized.

Since q=Phi/Xi(0), the same estimate holds for the BPY density q.

## Relative-slice consequence

For

rho_u(y)=q(u/2+y)q(u/2-y),

one has

partial_y^2 log rho_u(y)
=
(log q)''(u/2+y)
+
(log q)''(u/2-y)
<=
-20.

Thus every relative BPY slice is uniformly strongly log-concave, independent of u.

Let

Psi_u=sqrt(rho_u),
W_u=partial_y log Psi_u.

Then

boxed(
W_u'(y)
=
1/2 partial_y^2 log rho_u(y)
<=
-10
).

In particular W_u is odd, strictly decreasing, and

y>0 => W_u(y)<0.

## Uniform SUSY partner gap

For

A_u=partial_y-W_u,

one has

A_u^*=-partial_y-W_u

on the standard flat L2 core, and hence

A_u A_u^*
=
-partial_y^2+W_u^2-W_u'.

Since -W_u'>=10,

boxed(
A_u A_u^* >= 10 I
)

as a quadratic-form inequality on the core, and therefore after Friedrichs closure.

The even state Psi_u satisfies A_u Psi_u=0.  Supersymmetry then implies that the nonzero
spectrum of A_u^*A_u is bounded below by 10 as well. In particular the odd relative sector,
which is orthogonal to the even ground state, has a uniform gap at least 10.

## Meaning for the RH attack

This materially strengthens the BPY Dirac reformulation:

- the relative coordinate has an exact even ground state;
- every slice is uniformly confining;
- the odd local channel has a uniform positive SUSY gap.

However this still does NOT prove the BPY contractivity inequality.  The analytic
exponential subspace contains arbitrarily large c-frequencies, and a local Poincare/gap
estimate controls the odd component by c-derivative energy rather than directly by the even
L2 norm.

The remaining task is therefore much narrower:
combine this uniform relative gap with the wedge geometry |c|<=u/2 and the u-weight
sinh(omega u).  A proof must be genuinely two-variable; fixed-u positivity is false as a
route.

This is the first quantitative coercive input currently available for that two-variable
Dirac problem.
