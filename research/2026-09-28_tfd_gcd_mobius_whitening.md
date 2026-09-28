# Critical arithmetic TFD Gram kernel: exact GCD covariance, Möbius whitening, and the Hagedorn null vector

Date: 2026-09-28
Status: exact zero-independent Hilbert identities for beta>1 plus canonical beta->1 finite-local limit. No RH claim.

## 1. The doubled multiplicative shifts have the exact GCD Gram kernel

Let H=ell2(N), S_d e_n=e_{dn}, and on H tensor H let V_d=S_d tensor S_d. For beta>1 take

  Omega_beta=zeta(beta)^(-1/2) sum_{n>=1} n^(-beta/2)e_n tensor e_n.

For m,n>=1, write g=gcd(m,n), m=ga, n=gb with gcd(a,b)=1. Directly from the basis expansion,

  <V_m Omega_beta, V_n Omega_beta>
   = (ab)^(-beta/2)
   = (g/sqrt(mn))^beta.

Therefore

  boxed: K_beta(m,n)=(gcd(m,n)/sqrt(mn))^beta

is literally the TFD shift Gram kernel.

At beta=1 the canonical finite-local KMS limit is the critical GCD kernel

  K_1(m,n)=gcd(m,n)/sqrt(mn).

So the GCD/Poisson metric is not merely analogous to the arithmetic TFD: it is its exact two-point function.

## 2. Prime factorization of the kernel

If a_p=v_p(m), b_p=v_p(n), then

  K_beta(m,n)=product_p p^[-beta |a_p-b_p|/2].

Thus each prime carries the Toeplitz covariance

  K_{p,beta}(a,b)=r_p^|a-b|,  r_p=p^(-beta/2).

The global GCD kernel is their tensor product.

## 3. Local precision and Möbius factor are the same object

On ell2(N_0), let S be the unilateral shift. The inverse of the local covariance is

  boxed:
  K_{p,beta}^(-1)
  = (I-r_p S)(I-r_p S*)/(1-r_p^2).

Thus the local Möbius factor I-r_p S is a Cholesky/whitening factor for the inverse TFD covariance.

The normalized local TFD vector is

  Omega_{p,beta}=sqrt(1-r_p^2)(I-r_p S)^(-1)e_0,

so

  boxed:
  (I-r_p S)Omega_{p,beta}=sqrt(1-r_p^2)e_0.

This is the exact local algebra behind 'Möbius inversion removes the thermal prime cloud'.

## 4. Global Möbius whitening

For a finite set P of primes define

  M_{P,beta}=product_{p in P}(I-p^(-beta/2) V_p).

Using the prime tensor factorization,

  ||M_{P,beta} Omega_beta||^2
   = product_{p in P}(1-p^(-beta)).

As P increases through all primes, beta>1 gives

  boxed:
  ||M_beta Omega_beta||^2=1/zeta(beta),

where M_beta is understood as the state-specific strong limit of the finite-prime whitening products. This limit exists on Omega_beta even in regimes where the corresponding raw Dirichlet operator series is not operator-norm convergent.

In fact the cancellation is exact:

  boxed:
  M_beta Omega_beta=zeta(beta)^(-1/2) e_1 tensor e_1.

This extends the identity M(s)Z(s)=I to the thermal vector by canceling prime-by-prime before taking a global operator norm.

## 5. The critical state is a genuine null vector of the Möbius whitening metric

As beta decreases to 1,

  ||M_beta Omega_beta||^2=1/zeta(beta) -> 0.

After dividing by this vanishing norm, the state is exactly the bare arithmetic vacuum for every beta>1. Thus the critical Hagedorn escape is concentrated in one coherent Möbius-null direction.

This is the TFD/GCD version of the independently found rank-one scalarization obstruction.

## 6. The von Mangoldt current is the logarithmic susceptibility of this positive norm

Differentiating the exact positive fidelity gives, for beta>1,

  boxed:
  d/d beta log ||M_beta Omega_beta||^2
  = -zeta'(beta)/zeta(beta)
  = sum_{n>=1} Lambda(n)n^(-beta).

Equivalently primewise, the local 2x2 Gram determinant

  G_{p,beta}=[[1,r_p],[r_p,1]]

has

  det G_{p,beta}=1-p^(-beta),

and

  d/d beta log det G_{p,beta}
  = (log p)/(p^beta-1)
  = sum_{k>=1}(log p)p^(-k beta).

So the entire von Mangoldt prime-power current is the logarithmic derivative of a PRODUCT OF POSITIVE TFD GRAM DETERMINANTS on the real Gibbs ray.

## 7. Exact completed free-energy ratio

Let A_infty(s)=s(s-1)pi^(-s/2)Gamma(s/2). For real beta>1,

  2 xi(beta)=A_infty(beta) zeta(beta)
            = A_infty(beta)/||M_beta Omega_beta||^2.

At beta=1 both A_infty(beta) and the Möbius-whitened TFD norm vanish linearly and their ratio remains finite. Thus the pole cancellation in completed zeta is exactly a cancellation between an Archimedean null factor and the critical Möbius/TFD null factor.

## 8. Why this is closer to the RH operator but not yet the proof

On the real Gibbs ray all finite-place factors are genuine positive Gram determinants. Analytic zeta needs the chiral continuation 1-p^(-s), whereas the positive doubled Gram determinant naturally retains only the Hermitian modulus information. Recovering the analytic chiral determinant while preserving reflection positivity is exactly the sheet-sewing problem.

The new target is therefore more specific: construct the Archimedean sheet so that the ratio in section 7 is the CHIRAL determinant of a self-adjoint doubled Fredholm system, not merely an analytic continuation of a positive real norm.

That is where a positive collective operator A could emerge.