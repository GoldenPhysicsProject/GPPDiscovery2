# Finite-place shadow kernel as a positive Cayley real part

Date: 2026-09-18

For 0<a<1 let S be the unilateral shift and define the regularized Cayley operator

C_a=(I+aS)(I-aS)^(-1).

Then

C_a^*=(I-aS^*)^(-1)(I+aS^*).

Putting the two terms over the common denominator gives

C_a+C_a^*
=
(I-aS^*)^(-1)
[(I-aS^*)(I+aS)+(I+aS^*)(I-aS)]
(I-aS)^(-1).

Since S^*S=I, the middle factor equals

2(1-a^2)I.

Therefore

Re C_a
=
(C_a+C_a^*)/2
=
(1-a^2)(I-aS^*)^(-1)(I-aS)^(-1).

Equivalently, with

R_a=sqrt(1-a^2)(I-aS)^(-1),

one has the exact positive factorization

Re C_a=R_a^*R_a >=0.

On the unit-circle symbol z=e^{i theta},

Re [(1+az)/(1-az)]
=
(1-a^2)/[(1-az)(1-a z^(-1))]
=
(1-a^2)/|1-ae^{i theta}|^2.

For a=q^(-1/2), this is exactly the finite-place shadow kernel

K_{q,1}(1/2+i theta/log q)
=
(1-q^(-1))/(1+q^(-1)-2q^(-1/2)cos theta).

Thus the finite-place shadow kernel is the positive real part of a Cayley/Herglotz transfer and also an adjoint-times-original square.

Interpretation of the sign mechanism:
the local first-order denominator I-aS is paired with its shadow/adjoint I-aS^*. The two sign-reversed factors combine into the positive square R_a^*R_a. In scalar half-density coordinates the same mechanism is X^*=-X -> -X^2=X^*X>=0.

At the center theta=0,

C_a(1)=(1+a)/(1-a)=K_{q,1}(1/2).

For q=5 this is phi^2.

This gives a direct operator bridge among:
- local Euler/shadow pairing,
- finite-place Poisson kernel,
- Herglotz/Cayley positivity,
- the causal Hardy resolvent,
- and the q=5 golden transfer.

The global RH problem is then the question whether the completed prime-Archimedean assembly retains this local adjoint-square positivity after the singular critical completion. Local positivity alone is not enough because inner Hardy factors are invisible to boundary modulus.