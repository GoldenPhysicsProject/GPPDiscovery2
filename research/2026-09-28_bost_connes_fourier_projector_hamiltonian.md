# Critical Bost-Connes finite Fourier Gram equals the divisibility projectors: exact ax+b -> number-circle Hamiltonian

Date: 2026-09-28
Status: exact zero-independent finite-group/KMS theorem. This is a new synthesis of the previously separate Bost-Connes midpoint Gram and number-circle/von-Mangoldt DtN construction. No RH claim.

## 1. Finite additive level

Fix N>=1 and work on the finite subgroup

  G_N=(1/N)Z/Z subset Q/Z.

Assume n|N. For r in G_N use the opposite-ordered Bost-Connes channel

  B_{n,r}=e(r) mu_n.

At the critical beta=1 midpoint, the exact Gram identity is

  <B_{n,r},B_{n,s}>_mid
   = n^(-1/2) 1_{ n(r-s)=0 in Q/Z }.

Now apply the extra quarter-density normalization

  C_{n,r}=n^(-1/4) B_{n,r}.

Then

  boxed:
  <C_{n,r},C_{n,s}>_mid
   = (1/n) 1_{r-s in H_n},

where H_n is the n-torsion subgroup of G_N, of cardinality n.

## 2. The Gram operator is EXACTLY an orthogonal Fourier projector

Let K_{n,N} be the Gram operator on ell2(G_N):

  (K_{n,N} f)(r)
   =(1/n) sum_{s: r-s in H_n} f(s).

This is normalized averaging over the subgroup H_n, hence is an orthogonal projection.

The characters of G_N are

  chi_k(r)=exp(2 pi i k r),  k in Z/NZ.

Since

  (1/n) sum_{h in H_n} chi_k(h)
   = 1 if n|k,
     0 otherwise,

we obtain

  boxed:
  K_{n,N} chi_k = 1_{n|k} chi_k.

So the quarter-density normalized CRITICAL KMS Gram of the n-th multiplicative channel is literally the projector onto additive Fourier modes divisible by n.

This is the exact finite ax+b coupling that was missing from the prime-torus-only picture.

## 3. Von Mangoldt sum gives the logarithmic Hamiltonian

Define the positive finite-level operator

  H_N = sum_{n|N, n>=2} Lambda(n) K_{n,N}.

On a Fourier character chi_k,

  H_N chi_k
   = [sum_{n|N, n|k} Lambda(n)] chi_k
   = log(gcd(k,N)) chi_k.

Therefore

  boxed:
  H_N chi_k = log(gcd(k,N)) chi_k.

In particular, whenever k|N,

  boxed:
  H_N chi_k = (log k) chi_k.

Along any cofinal sequence N_j divisible by every fixed integer eventually (for example N_j=j!), each fixed Fourier mode stabilizes exactly:

  H_{N_j} chi_k -> (log k) chi_k.

Hence the arithmetic number-circle/DtN Hamiltonian

  H chi_k=(log k)chi_k

is the inductive-limit operator of POSITIVE critical-KMS Gram operators built from the full Bost-Connes ax+b algebra.

## 4. Why the n^(-1/4) normalization is forced

The raw midpoint Gram carries n^(-1/2). The subgroup H_n has n elements. To turn its convolution matrix into a projection requires an additional factor n^(-1/2) at the Gram level, i.e. n^(-1/4) on each vector.

So the quarter-density appears again, now as the unique normalization that balances:

  KMS half-density n^(-1/2)
  x additive torsion multiplicity n
  -> unit Fourier projector.

This is the same quarter-density that appears in the BPY radial insertion Q^(1/4).

## 5. Exact bridge now obtained

The following chain is no longer heuristic:

  Bost-Connes critical KMS standard form
   -> multiplicative channel mu_n + additive n-torsion
   -> normalized midpoint Gram K_{n,N}
   -> divisibility projector on finite Fourier modes
   -> sum Lambda(n) K_{n,N}
   -> log(gcd(k,N))
   -> cofinal limit log k
   -> number-circle DtN Hamiltonian log|D|.

This couples Euler multiplicativity and additive Fourier/Pontryagin self-duality in ONE positive construction, exactly the structural requirement highlighted by the Beurling/Davenport-Heilbronn filters.

## 6. Relation to the existing positive projection decomposition

Earlier we had, abstractly on ell2(N),

  H=sum_{d>=2} Lambda(d) P_d,

with P_d the projector onto integer modes divisible by d.

The present theorem identifies each P_d itself as a critical Bost-Connes MIDPOINT GRAM operator on a finite additive self-dual level.

So the previous positive parent is now derived from the arithmetic KMS ax+b system rather than postulated as a basis projection.

## 7. What this buys and what remains

Because every H_N is positive and diagonalized by the finite Fourier transform, its heat and functional calculus are automatically positive. The finite additive levels therefore give a canonical sequence of genuinely self-dual positive arithmetic systems whose limit is the free number-circle bulk.

This still does not locate the Riemann zeros: the free spectrum is log k. The RH-bearing step remains the COMPLETED fluctuation/OS operator after Archimedean modular sewing.

But the hard 'Euler product + lattice self-duality in one step' requirement is now solved at the microscopic operator level. The next attack should build the Archimedean/Poisson completion as a compatible limit of the functional calculus of H_N, rather than sewing an unrelated real-place Hilbert space onto the primes by hand.