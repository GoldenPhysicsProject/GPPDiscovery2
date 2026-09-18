# The RH ghost as the Hagedorn/profinite boundary of the number Gibbs state

Date: 2026-09-18

Status: exact consequences of the current dual ghost equations plus elementary Euler-product probability identities. No RH proof is claimed.

## 1. Honest number Gibbs state

For beta>1 define

P_beta(n)=n^{-beta}/zeta(beta), n>=1.

This is a probability distribution on N. Its Shannon entropy is exactly the project's number entropy

S_N(beta)=log zeta(beta)-beta zeta'(beta)/zeta(beta).

For every m>=1,

P_beta(m divides n)
=
sum_{k>=1}(mk)^{-beta}/zeta(beta)
=
m^{-beta}.

Hence for every prime p and a>=0,

P_beta(v_p(n)=a)
=
p^{-a beta}-p^{-(a+1)beta}
=
(1-p^{-beta})p^{-a beta}.

For a finite prime set P, the valuation variables are independent:

P_beta(v_p(n)=a_p for p in P)
=
product_{p in P}(1-p^{-beta})p^{-a_p beta}.

This is just unique factorization written probabilistically.

## 2. The dual ghost has exactly the beta=1 cylinder law

The current Ramanujan/Casimir dual ghost equations are

H(m):=sum_{k>=1}h_{mk}=h_1/m.

For one prime,

sum_{v_p(n)=a}h_n
=
H(p^a)-H(p^{a+1})
=
h_1(1-p^{-1})p^{-a}.

For a finite prime set P, finite inclusion-exclusion gives

sum_{v_p(n)=a_p for all p in P}h_n
=
h_1 product_{p in P}(1-p^{-1})p^{-a_p}.

Thus if h_1!=0, the normalized divisibility marginals of any ghost are exactly

lim_{beta downarrow 1} P_beta(v_p=a_p, p in P).

This is a zero-independent algebraic consequence of the ghost equations.

## 3. Local coherent state and finite-place shadow kernel

For each prime define

Omega_{p,beta}
=
sqrt(1-p^{-beta}) sum_{a>=0} p^{-a beta/2}|a>.

Then ||Omega_{p,beta}||=1 and

S_p* Omega_{p,beta}=p^{-beta/2}Omega_{p,beta}.

At the Hagedorn boundary beta=1,

Omega_p
=
sqrt(1-p^{-1}) sum_{a>=0}p^{-a/2}|a>.

Its phase generating function is

B_p(e^{i theta})
=
sqrt(1-p^{-1})/(1-p^{-1/2}e^{i theta}),

and

|B_p(e^{i theta})|^2
=
(1-p^{-1})/(1+p^{-1}-2p^{-1/2}cos theta),

which is exactly the finite-place shadow/Poisson kernel K_{p,1}(1/2+i theta/log p).

Therefore the finite-place shadow kernel is the spectral density of the square-root amplitude of the ghost's forced local valuation law.

## 4. Global Fock transition at beta=1

For beta>1,

sum_p P_beta(v_p>0)=sum_p p^{-beta}<infinity.

Hence under the product valuation law only finitely many primes are occupied almost surely. The product state is supported on ordinary finite integers, and the global coherent state has vacuum fidelity

|<0|Omega_beta>|^2
=
product_p(1-p^{-beta})
=
1/zeta(beta)>0.

As beta downarrow1,

1/zeta(beta)->0

and

sum_p p^{-1}=infinity.

The limiting product valuation law has infinitely many occupied primes almost surely. It is no longer supported on ordinary N; it belongs naturally to the profinite/supernatural boundary. The vacuum fidelity vanishes.

Thus beta=1 is exactly the point at which the number Gibbs/coherent state leaves the ordinary arithmetic Fock sector.

## 5. Escape of mass from N

For every fixed n,

P_beta(n)=n^{-beta}/zeta(beta)->0

as beta downarrow1, while total mass remains one. More generally every finite subset of N loses all mass.

Nevertheless every finite divisibility cylinder has a nontrivial limit, namely the Haar valuation law in section 2. Hence the correct critical limit is not a probability on N but a boundary probability carrying the local p-adic Haar marginals.

This is the precise measure-theoretic meaning of 'mass escape to the arithmetic boundary'.

## 6. Finite-variation obstruction

Suppose a nonzero ghost h defined a finite-total-variation atomic complex measure on N:

sum_n |h_n|<infinity.

Normalize h_1=1. Its exact valuation cylinders have the beta=1 Haar masses.

For a fixed integer n, prescribe the exact valuations v_p(n) for all primes in a growing finite set P. These cylinder sets decrease to {n}. Their masses equal a fixed finite factor from primes dividing n times

product_{p in P, p not dividing n}(1-p^{-1}),

which tends to zero.

Continuity from above of a finite complex measure gives mass({n})=0 for every n. Countable additivity then gives mass(N)=0, contradicting H(1)=1.

Therefore every nonzero ghost necessarily has

sum_n|h_n|=infinity.

If q_n=n h_n belongs to l2, then

sum_n|h_n|
<=
(sum_n|q_n|^2)^{1/2}(sum_n n^{-2})^{1/2}<infinity,

so q in l2 implies no ghost.

This gives a measure-theoretic proof of the previously obtained l2 no-ghost theorem.

## 7. Number entropy interpretation

The Shannon entropy of P_beta is exactly

S_N(beta)=log zeta(beta)-beta zeta'(beta)/zeta(beta).

Its Hagedorn expansion at beta=1+epsilon is

S_N(1+epsilon)
=
epsilon^{-1}-log epsilon+(1-gamma)+O(epsilon).

Thus the project constant 1-gamma is the finite part of the entropy of the Gibbs family precisely at the boundary where the putative ghost state escapes from ordinary integers into the profinite sector.

This does not identify 1-gamma with the RH ghost entropy -log|B(0)|^2; they are distinct canonical scalars attached to two different boundary defects.

## 8. q=5 local Hagedorn channel and the golden rapidity

At beta=1 the p=5 local coherent radius is

a_5=5^{-1/2}.

Cayley-transform it by

r=(1-a)/(1+a),

and define kappa=artanh(a). Then

a_5=tanh(log phi)=1/sqrt5,
r_5=e^{-2 log phi}=phi^{-2},
mu_5=2sinh(log phi)=1.

So the q=5 Hagedorn local channel is exactly the unit-mass/golden-rapidity channel of the discrete Casimir-Dirac factorization.

## 9. Current interpretation and target

A nonzero RH ghost would have to be all of the following at once:

1. finite in the homogeneous Casimir energy;
2. outside the l2/local-Dirichlet sector;
3. infinite in atomic total variation;
4. locally indistinguishable, on every finite set of p-adic valuation observables, from the beta=1 Haar/Hagedorn number state;
5. supported only as a threshold/boundary object after the ordinary integer Gibbs sector loses normalizability.

This sharply identifies the no-escape theorem still needed. One must prove that the completed prime-Archimedean/shadow physical Hilbert space does not admit this critical boundary state as an arithmetic ghost. The finite Hodge-Koszul complex already excludes all finite-cutoff cohomology; the only possible class is therefore a boundary-at-infinity class.
