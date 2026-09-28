# Direct finite-place construction: the zeta logarithmic current is a TFD vacuum expectation of the Möbius connection

Date: 2026-09-28
Status: exact zero-independent identities in the Gibbs half-plane, with a canonical finite-prime critical limit. No RH claim.

## 1. Arithmetic Fock space and its thermofield double

Let H_ar=ell2(N) with basis |n> and Hamiltonian H|n>=(log n)|n>. Let S_d be the multiplicative isometry S_d|n>=|dn>.

For beta>1 define the normalized arithmetic thermofield double

  |Omega_beta> = zeta(beta)^(-1/2) sum_{n>=1} n^(-beta/2) |n,n>.

On the doubled space define the diagonal multiplicative shift

  V_d = S_d tensor S_d.

Then V_m V_n=V_mn.

## 2. Exact TFD half-density matrix coefficient

A direct basis calculation gives

  <Omega_beta, V_d Omega_beta>
    = zeta(beta)^(-1) sum_{n>=1} (dn)^(-beta/2)n^(-beta/2)
    = d^(-beta/2).

Hence

  boxed: <Omega_beta,V_d Omega_beta>=d^(-beta/2).

At beta=1 the global vector ceases to exist, but this matrix coefficient has the unambiguous finite-local limit d^(-1/2). Thus the critical arithmetic half-density is literally a TFD coherence amplitude.

## 3. Modular time supplies the logarithmic arithmetic frequency

Evolve only one copy with the arithmetic Hamiltonian. Since

  exp(itH) S_d exp(-itH)=d^(it) S_d,

the corresponding one-sided doubled evolution satisfies

  <Omega_beta, V_d(t) Omega_beta>
    = d^(-beta/2+it)

up to the fixed sign convention for time.

So the TFD two-point function has an atom at frequency log d and amplitude d^(-beta/2). At beta=1 this is exactly the principal-series character d^(-1/2+it).

## 4. Möbius gauge and the operator-valued logarithmic connection

For Re z>1 define the semigroup-valued Dirichlet series

  Z(z)=sum_{n>=1} n^(-z) V_n,
  M(z)=sum_{n>=1} mu(n)n^(-z) V_n.

Because V_mV_n=V_mn and mu*1=epsilon,

  M(z)Z(z)=Z(z)M(z)=I.

Differentiating gives the exact logarithmic connection

  P(z):=-M(z)Z'(z)
      =sum_{n>=1} Lambda(n)n^(-z)V_n.

This is the same Dirichlet-log gauge identity already present in the scalar, shift, and Gaussian-decimation versions of the project, now on the literal arithmetic TFD Hilbert space.

## 5. Vacuum expectation is exactly the zeta current with the KMS half-density

For beta>1 and Re z sufficiently large to justify the operator series,

  <Omega_beta,P(z)Omega_beta>
   = sum_n Lambda(n)n^(-z) dTFD(n)
   = sum_n Lambda(n)n^(-(z+beta/2))
   = -zeta'/zeta(z+beta/2).

Therefore

  boxed:
  <Omega_beta,P(z)Omega_beta>
  = -zeta'/zeta(z+beta/2).

In particular the critical beta->1 finite-local limit centers the arithmetic current automatically:

  zeta argument = 1/2 + z.

The factor 1/2 is not inserted into P(z); it comes from the thermofield/KMS state.

## 6. Prime decomposition is a Cayley transform of contractions

For each prime p let V_p be the isometry above. Then

  P_p(z)=(log p) sum_{k>=1} p^(-kz)V_p^k.

For Re z>0 the operator X_p(z)=p^(-z)V_p is a strict contraction. Hence

  C_p(z)=(I+X_p(z))(I-X_p(z))^(-1)

has positive real part, and

  boxed:
  P_p(z)=(log p)/2 [ C_p(z)-I ].

Thus every prime logarithmic-current channel is the normal-ordered part of a positive-real/passive Cayley transfer. The obstruction is entirely in the infinite vacuum subtraction and global completion, not in local prime dynamics.

## 7. Exact relation to the Weil prime measure

Smearing modular time with a test function whose Fourier transform is h gives, at beta=1 formally and rigorously for finite prime sets before the limit,

  sum_n Lambda(n)n^(-1/2) h(log n).

This is precisely the finite-place half-density measure in the Weil explicit formula.

So the prime side of Weil reflection positivity has now been realized as a TFD/KMS spectral measure of the logarithmic connection of the multiplicative semigroup.

## 8. Why this is not yet RH

The local Cayley transfers C_p are passive, but P_p contains the subtraction of the identity. Summing those vacuum subtractions over all primes is divergent. The real-place and rational/pole sectors must supply the exact global renormalization. Difference of positive-real functions need not remain positive-real.

Therefore the remaining theorem is extremely specific:

  add the Archimedean SU(1,1) modular channel to the TFD logarithmic connection and prove that the COMPLETED renormalized expectation is positive-real on Re z>0.

That completed expectation is xi'/xi(1/2+z); positive-realness there is RH-equivalent.

## 9. Why this is useful

This directly couples the three structures that had previously been separate:

  unique factorization / Mobius inversion -> P(z),
  thermofield/KMS midpoint -> n^(-1/2),
  modular time -> frequency log n.

No zeros, analytic continuation, or assumed Weil positivity enter the construction of the finite-place current.