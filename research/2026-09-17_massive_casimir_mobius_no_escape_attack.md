# Massive Casimir / Möbius no-escape attack

Date: 2026-09-17
Status: active derivation. Exact reductions recorded; no RH claim.

## Starting point

The reciprocal-Nyman/Casimir ghost is a sequence h_n with h_n -> 0, finite energy

E(h)=sum_{n>=1} n(n+1)|h_n-h_{n+1}|^2 < infinity,

nonzero boundary amplitude h_1, and arithmetic dilation constraints

sum_{k>=1} h_{mk}=h_1/m   for every m>=1.

Set q_n=n h_n. The ground-state transform gives

E(h)=|q_1|^2+sum_{n>=1}|q_{n+1}-q_n|^2 = <q,Lq>,

with half-line discrete Laplacian L=2I-S-S*.

The exact finite-place massive family found in the golden-Casimir note is

L+m_q^2 I = r_q^{-1}(I-r_q S*)(I-r_q S),

r_q=(sqrt(q)-1)/(sqrt(q)+1),

m_q^2=4/(q-1).

At q=5, m_q^2=1 and r_q=phi^{-2}; the transfer polynomial is x^2-3x+1 and the transfer matrix is SL2(Z)-conjugate to the previously formalized minimal hyperbolic matrix [[2,1],[1,1]].

## Why positive mass is relevant

For any m^2>0, the massive form

E_m(q)=<q,(L+m^2 I)q>=E(h)+m^2 ||q||_2^2

is coercive on l^2. Thus any sequence with finite massive energy automatically has q in l^2.

If q in l^2 and the dilation constraints hold, then

h_1 = sum_{k>=1} q_{mk}/k.

By Cauchy-Schwarz,

|h_1| <= (sum_{k>=1}|q_{mk}|^2)^(1/2) (sum_{k>=1}1/k^2)^(1/2).

As m->infinity, the subsequence tail sum sum_k |q_{mk}|^2 tends to 0 for every q in l^2. Hence h_1=0.

Therefore:

THEOREM (massive no-ghost, conditional only on finite massive energy):
Any ghost satisfying the exact dilation constraints and E_m(q)<infinity for some m>0 has h_1=0. In particular no nonzero RH ghost can lie in any positive-mass Casimir graph space.

This is elementary but important: the entire obstruction is forced to live exactly at the massless boundary m=0. The positive-mass family removes the ultraviolet escape completely.

## Stronger conclusion once h_1=0

The constraints become

sum_{k>=1} h_{mk}=0.

If q in l^2 then h_n=q_n/n and the series is absolutely summable by Cauchy-Schwarz:

sum_k |h_{mk}| <= (1/m)(sum_k |q_{mk}|^2)^(1/2)(sum_k 1/k^2)^(1/2).

Möbius inversion can then be justified on finite truncations with vanishing tails, forcing h_n=0 for all n. Thus finite massive energy annihilates the entire ghost, not only its boundary amplitude.

## Exact location of the RH difficulty

A genuine RH obstruction, if it exists, must satisfy

E(h)<infinity

but

q notin l^2.

Equivalently, it is a zero-energy threshold resonance of the half-line Laplacian L, excluded by every positive mass but potentially surviving at m=0.

This sharpens the problem to a threshold-resonance exclusion theorem using the arithmetic dilation constraints.

## Next attack

1. Derive quantitative estimates for massive regularizations q^(m)=(L+m^2 I)^(-1/2) L^(1/2) q or related resolvent damping that are defined for every finite-energy ghost.
2. Transport the exact dilation equations through the resolvent/factorization and compute the commutator error with dilation operators.
3. Show the error is controlled strongly enough as m->0 that the massive no-ghost theorem passes to the threshold.
4. Exploit the finite-place parameterization m_q^2=4/(q-1) and the causal factor r_q to seek an arithmetic monotonicity or positivity estimate unavailable for a generic mass parameter.
5. At q=5, test whether the SL2(Z)/phi fixed point gives an especially strong boundary trace inequality, but do not assume q=5 alone closes the massless limit.
