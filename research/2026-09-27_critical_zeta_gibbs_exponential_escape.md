# Critical zeta Gibbs escape: an exponential boundary mode

Date: 2026-09-27
Status: exact asymptotic theorem from the zeta pole. No RH assumption and no external search.

## 1. Zeta Gibbs ensemble

For beta>1 put epsilon=beta-1 and define the probability law on positive integers

P_beta(N=n)=n^(-beta)/zeta(beta).

By unique factorization this is the product law of independent geometric prime occupations

N_p=v_p(N),
P_beta(N_p=a)=(1-p^(-beta))p^(-beta a).

The arithmetic Hamiltonian is

H=log N=sum_p (log p) N_p.

For every fixed finite set of primes the occupations have a regular critical limit as beta decreases to 1,

P_beta(N_p=a) -> (1-p^(-1))p^(-a).

The global integer law itself has no pointwise probability limit because zeta(beta) diverges.

## 2. Exact critical scaling limit

Define the scaled escaping energy

Y_epsilon = epsilon H = epsilon log N.

For s with Re(s)>=0,

E exp(-s Y_epsilon)
= zeta(1+epsilon(1+s))/zeta(1+epsilon).

Using only the Laurent expansion

zeta(1+z)=1/z + gamma + O(z),

we obtain locally uniformly for Re(s)>=0 on compact sets

boxed:
E exp(-s Y_epsilon) -> 1/(1+s).

Therefore

boxed:
epsilon log N  =>  Exp(1)

in distribution as epsilon decreases to zero.

Equivalently, for the modular characteristic kernel,

zeta(1+epsilon+i epsilon y)/zeta(1+epsilon)
-> 1/(1+i y)
= integral_0^infty exp(-x) exp(-i y x) dx.

Thus the critical coherent boundary layer is the one-sided causal exponential kernel.

At every fixed nonzero macroscopic frequency t,

zeta(1+epsilon+i t)/zeta(1+epsilon) -> 0.

So coherence collapses at fixed modular time, while the rescaled window t=epsilon y has the universal causal profile 1/(1+i y).

## 3. Joint limit with finite prime occupations

Let F be any fixed finite set of primes and let z_p be bounded generating variables. Exact factorization gives

E[ exp(-s epsilon H) prod_{p in F} z_p^(N_p) ]

= zeta(1+epsilon(1+s))/zeta(1+epsilon)
  prod_{p in F}
  (1-p^(-1-epsilon(1+s)))
  /(1-z_p p^(-1-epsilon(1+s))).

Hence

boxed:
(Y_epsilon, (N_p)_{p in F})
=>
(Y, (N_p^crit)_{p in F})

with Y~Exp(1), critical geometric occupations
P(N_p^crit=a)=(1-p^-1)p^-a,
and Y independent of every fixed finite collection of prime occupations.

This is a projective statement: the escaping global energy becomes asymptotically independent of all finite local prime data.

## 4. Interpretation for the critical KMS boundary

The beta=1 obstruction is therefore more specific than “the state does not exist.”

1. The finite-prime cylinder marginals have a perfectly good quasi-local critical state.
2. The unscaled global arithmetic energy escapes to infinity.
3. After the canonical scaling epsilon H, that escape is a single universal Exp(1) boundary mode.
4. The boundary mode is asymptotically independent of every finite prime cylinder.

This gives a natural compactified critical object:

critical quasi-local Haar/KMS state
tensor
independent exponential escape mode.

No RH statement is used.

## 5. Relation to the Archimedean pole channel

The completed real-place impedance contains the rational terms

1/(r-1/2) + 1/(r+1/2).

These are Laplace transforms of the reflected pair

exp(+x/2), exp(-x/2).

The growing exp(+x/2) term is exactly the analytic shape expected from a critical Gibbs mass-escape mode, while its reflected partner is forced by the completed shadow symmetry.

This does not yet identify the entire Archimedean completion with the escape variable; the digamma/metaplectic tower remains a separate real-place channel. But it gives a canonical probabilistic origin for the formerly mysterious anti-midpoint trivial direction.

## 6. Consequence for the RH program

The beta->1 problem should be split into two distinct questions:

(A) critical state compactification — now explicit at the scalar Gibbs level via the independent Exp(1) escape mode;

(B) global Poisson/Archimedean sewing of the nonlocal arithmetic tangent directions — still the RH-bearing problem.

In particular, divergence of zeta(beta) by itself cannot be the RH obstruction. The divergence is carried by a universal boundary mode whose scaling law is completely explicit and independent of finite prime occupations.

The next target is to build this escape mode into the same Archimedean/metaplectic standard form that produces the pole and Gamma terms of the explicit formula, then ask whether the remaining prime deficit is the Schur complement of a positive completed covariance.
