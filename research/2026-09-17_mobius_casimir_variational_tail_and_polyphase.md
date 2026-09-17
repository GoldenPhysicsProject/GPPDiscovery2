# Möbius–Casimir threshold state, polyphase dilation, and golden variational tail

Date: 2026-09-17
Status: exact algebra/operator identities plus one PNT input for the limiting boundary value. No RH claim.

## 1. Exact cell-incidence factorization

Let x=(x_n)_{n>=1} be the logarithmic-cell input coefficients for the zeta channel

Y_n(s)=zeta(s)(n^{1-s}-(n+1)^{1-s}).

For a finitely supported x, the Dirichlet coefficient a_m of sum_n x_n Y_n is

a_m = sum_{n|m} n x_n - sum_{n+1|m} (n+1)x_n.

Set

g_1=x_1,
g_d=x_d-x_{d-1} for d>=2.

Then exactly

a_m = sum_{d|m} d g_d.

Hence the channel factors as

x --Delta--> g --diag(d)--> b_d=d g_d --divisibility-zeta--> a_m=sum_{d|m}b_d.

The Hardy vacuum 1 has Dirichlet coefficients a_1=1 and a_m=0 for m>1. Möbius inversion therefore forces

b_d=mu(d),

g_d=mu(d)/d.

Thus the canonical formal inverse is

x_n=M_1(n):=sum_{d<=n} mu(d)/d.

This is zero-independent and uses only the incidence algebra.

## 2. Exact zero-mass Casimir energy

With x_0=0,

x_n-x_{n-1}=mu(n)/n.

The half-line Casimir/Dirichlet energy is therefore

E_C(x)=sum_{n>=1}|x_n-x_{n-1}|^2
      =sum_{n>=1}mu(n)^2/n^2
      =zeta(2)/zeta(4)
      =15/pi^2.

So the canonical Möbius inverse is an unconditional finite-energy zero-mass threshold state. It need not lie in l^2; the missing l^2 property is precisely why positive-mass regularity is stronger.

PNT gives M_1(n)->0.

## 3. Finite exact arithmetic truncations

For fixed N, impose the exact local arithmetic constraints

g_d=mu(d)/d, 1<=d<=N.

Then x_n=M_1(n) for n<=N. Any continuation beyond N leaves the first N output Dirichlet coefficients exactly equal to the vacuum coefficients, because every divisor of m<=N is <=N.

The abrupt compactly supported continuation x_{N+1}=0 has the extra gradient -M_1(N), so

E_C(x^(N))=sum_{d<=N}mu(d)^2/d^2+|M_1(N)|^2 -> 15/pi^2.

Thus there is a uniformly bounded zero-mass graph-energy sequence matching arbitrarily many arithmetic coefficients exactly.

## 4. Positive-mass optimal continuation

Fix a mass M>0 and a boundary value c=x_N. Among all tails y_k=x_{N+k}, k>=0, with y_0=c and y in l^2, minimize

E_M^tail(y)=sum_{k>=0}|y_{k+1}-y_k|^2 + M^2 sum_{k>=1}|y_k|^2.

The Euler-Lagrange recurrence is

y_{k+1}-(2+M^2)y_k+y_{k-1}=0, k>=1.

Let r_M in (0,1) be the stable root

r_M+r_M^{-1}=2+M^2,

or equivalently

M^2=(1-r_M)^2/r_M.

The unique l^2 minimizer is

y_k=c r_M^k.

Substitution gives the exact Dirichlet-to-Neumann cost

min E_M^tail=(1-r_M)|c|^2.

Therefore the unique minimum-energy continuation of the finite exact Möbius inverse is

x_{N+k}=M_1(N) r_M^k.

This is an intrinsic variational origin of the causal geometric tail.

## 5. Golden unit-mass continuation

At unit mass M^2=1,

r+r^{-1}=3,
r^2-3r+1=0,

so the stable root is

r=phi^{-2},

and

1-r=phi^{-1}.

Hence the unit-mass optimal arithmetic tail is

x_{N+k}=M_1(N) phi^{-2k},

with minimal tail cost

phi^{-1}|M_1(N)|^2.

Thus phi^{-2} is not inserted by hand: it is the unique stable continuation ratio selected by the unit-mass Casimir variational problem applied to the exact finite Möbius inverse.

## 6. Finite-place mass family

For the already formalized finite-place center kernel

K_q=(sqrt(q)+1)/(sqrt(q)-1),

set

r_q=K_q^{-1}=(sqrt(q)-1)/(sqrt(q)+1),
M_q^2=4/(q-1).

Then

r_q+r_q^{-1}=2+M_q^2.

Therefore the finite-place kernel selects exactly the minimum-energy tail ratio for mass M_q. At q=5,

M_5^2=1,
r_5=phi^{-2},
K_5=phi^2.

The old finite-place/shadow result and the new arithmetic variational continuation are therefore the same stable/unstable pair at q=5.

## 7. Prime coherent radius and finite-place rapidity

The exact-conductor coherent-state factor uses

a_q=q^{-1/2}.

The finite-place contraction is its Cayley transform:

r_q=(1-a_q)/(1+a_q),
a_q=(1-r_q)/(1+r_q).

Equivalently, with eta_q=artanh(a_q),

r_q=e^{-2 eta_q},
K_q=e^{2 eta_q}.

At q=5,

artanh(1/sqrt(5))=log phi,

hence

r_5=e^{-2 log phi}=phi^{-2},
K_5=e^{2 log phi}=phi^2.

So the prime coherent radius, finite-place shadow kernel, and golden thermal/Casimir transfer are linked by one exact hyperbolic rapidity map.

## 8. Coherent precision extrema

For 0<a<1, the normalized one-prime precision symbol is

P_a(theta)=|1-a e^{i theta}|^2/(1-a^2)
          =(1+a^2-2a cos theta)/(1-a^2).

If r=(1-a)/(1+a), then

min_theta P_a(theta)=r,
max_theta P_a(theta)=r^{-1}.

Thus for a=q^{-1/2},

min P_a = K_q^{-1},
max P_a = K_q.

At q=5 the local precision interval is exactly

[phi^{-2}, phi^2],

the same stable/unstable eigenvalue pair as the minimal hyperbolic SL2(Z) matrix and the unit-mass Casimir transfer.

## 9. Polyphase form of arithmetic decimation

Let q=(q_n) be a zero-mass Casimir finite-energy sequence and define its gradient

d_0=q_1,
d_n=q_{n+1}-q_n, n>=1.

Then

E_C(q)=sum_{n>=0}|d_n|^2.

For m>=1 define the arithmetic decimation

(U_m q)_k=q_{mk}.

Its gradient is the non-overlapping block-sum transform

(B_m d)_k=sum_{j=mk}^{m(k+1)-1}d_j, k>=0.

Consequently

E_C(U_m q)=||B_m d||_2^2.

Cauchy-Schwarz on each block gives

||B_m d||_2 <= sqrt(m)||d||_2.

Let A_m=m^{-1/2}B_m. Then A_m A_m^*=I, so A_m is a coisometry. Its adjoint embeds a coarse sequence as a constant vector on each block of length m, and A_m^*A_m is the block-average projection.

For every fixed d in l^2,

A_m d -> 0 strongly as m->infinity.

Proof: for finite-support d this is immediate once m exceeds the support; then use density and ||A_m||=1.

Hence

E_C(U_m q)/m -> 0.

A hypothetical RH ghost therefore has vanishing normalized bulk energy under large arithmetic decimation while its exact arithmetic boundary functional remains nonzero. The obstruction is a pure boundary-concentration phenomenon.

The basic shift-decimation intertwiner is

U_m S^m = S U_m.

This is the correct polyphase/Hecke algebra in which additive Casimir dynamics and multiplicative arithmetic dilation meet.

## 10. Haar/profinite interpretation of the ghost equation

For a ghost h with h_1 != 0,

sum_{k>=1} h_{mk}=h_1/m, m>=1.

Normalize nu_n=h_n/h_1. Then

sum_{m|n} nu_n = 1/m.

Thus the conditionally summable atomic weights nu_n reproduce the Haar cylinder mass of the set of profinite integers divisible by m. If nu were absolutely summable and nonnegative, it would define a genuine probability measure on N with the same divisibility cylinder masses as Haar measure on Zhat, which is impossible because Haar is non-atomic on the embedded copy of N. Therefore any ghost must exploit conditional/sign cancellation and boundary escape. This is an interpretation, not a new proof, because finite Casimir energy alone does not imply l^1 or positivity.

## 11. Honest boundary and next targets

Nothing above proves RH. It sharpens the target in three ways:

1. the formal arithmetic inverse is a canonical finite-energy zero-mass Möbius threshold state with exact action 15/pi^2;
2. positive-mass optimal continuation is unique and geometric, with the unit-mass continuation ratio phi^{-2};
3. large arithmetic decimation drives normalized Casimir bulk energy to zero, so a nonzero ghost must concentrate entirely in the singular boundary functional.

Next targets:

- derive a quantitative boundary-concentration profile for the functional int_0^1 D_m(t)/(1-t)dt under block-sum decimation;
- combine all m simultaneously, seeking a large-sieve/Bessel estimate that would make a fixed nonzero boundary value incompatible with finite Casimir energy;
- compare the finite-place/coherent precision family to the optimal Möbius continuation and determine whether the prime-product/Koszul network supplies the missing uniform boundary regularity;
- formalize the exact finite-dimensional/algebraic pieces in GPPVerify once the operator target stabilizes.
