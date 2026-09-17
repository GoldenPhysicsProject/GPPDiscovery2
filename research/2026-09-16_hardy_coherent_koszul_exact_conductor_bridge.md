# Hardy / coherent-state / Koszul bridge from exact Ramanujan conductors

## Exact conductor Mellin source

For each m>=2, the Ramanujan source has Mellin/Dirichlet transform

D_m(s)=sum_{n>=1} r_m(n)n^{-s}=zeta(s) A_m(s),

with

A_m(s)=sum_{d|m} mu(m/d)d^{1-s}
      =m^{1-s} prod_{p|m}(1-p^{s-1}).

This factorization is exact and zero-independent.

On the unitary line s=1/2+it,

p^{s-1}=p^{-1/2} exp(i t log p).

Hence every distinct prime divisor contributes the local factor

1-r_p exp(i t log p),   r_p=p^{-1/2}.

These are exactly the coherent-state annihilation/precision factors found independently in the one-prime Fock module.

Thus exact conductor m is the product of local coherent precision factors over p|m acting on one common zeta boundary field.

## Cayley-Hardy unitary

Use the Cayley coordinate

beta=(s-1)/s,

so s=1/(1-beta). On the critical line s=1/2+it, |beta|=1 and

|d arg beta|=dt/(t^2+1/4).

The Casimir negative graph norm of a source with spectral function D(s) is

||D||_C^2=(1/(2 pi)) int_R |D(1/2+it)|^2 dt/(t^2+1/4).

Therefore

D(s) -> D(1/(1-beta))

is a unitary identification of the Casimir source space with standard Hardy H^2(D).

The target source delta_0 has D_0(s)=1, so it becomes the Hardy vacuum 1.

Consequently the Casimir-Nyman criterion is exactly

1 in closure span{D_m(beta): m>=2} in H^2(D).

This is the source-level intertwiner between the Casimir graph and the known Nyman/Hardy ghost model.

## Vacuum matrix element and von Mangoldt

At s=1,

D_m(1)=-Lambda(m).

Indeed if m=p^k then A_m has a simple zero at s=1 and zeta has a simple pole, leaving -log p; if m has at least two distinct prime factors the zero order of A_m is at least two and the product vanishes.

Thus Lambda is literally the vacuum matrix element

<1,D_m>_{H^2}=D_m(0 in beta)=-Lambda(m).

## Exact Koszul degree

Let omega(m) be the number of distinct prime divisors of m. Near s=1,

A_m(s)
~(-1)^{omega(m)}(s-1)^{omega(m)} prod_{p|m} log p.

Since zeta(s)~1/(s-1) and beta~s-1,

D_m(beta)
~(-1)^{omega(m)} beta^{omega(m)-1} prod_{p|m} log p.

Therefore

D_m in beta^{omega(m)-1} H^2.

This is an exact grading by distinct-prime number minus one:

* prime powers are degree 0 and couple directly to the vacuum;
* two-prime conductors begin in Hardy degree 1;
* three-prime conductors begin in degree 2;
* etc.

The mixed-prime conductors that appeared as Schur-complement auxiliaries are therefore the higher Koszul/fermionic sectors of the same Hardy system.

## Prime-power translation towers

For p prime define the normalized tower

E_{p,k}=p^{-k/2} R_{p^{k+1}},  k>=0,

where R_m is the Casimir Ramanujan source distribution. Then

E_{p,k}=tau_{k log p} R_p,

so the Gram matrix is Toeplitz in k.

The target coordinates are

<delta_0,E_{p,k}>=-(log p)p^{-k/2}.

Thus the target restricted to a p-tower is exactly the Szego/coherent vector

-(log p)(1,r_p,r_p^2,...),   r_p=p^{-1/2}.

## Exact coherent precision factor in the Toeplitz symbol

For the prime seed,

D_p(s)=zeta(s)(p^{1-s}-1).

On s=1/2+it,

p^{1-s}-1
=sqrt(p) exp(-it log p)(1-r_p exp(it log p)).

Hence the Casimir spectral density of the prime seed contains

p |1-r_p exp(i theta)|^2

with theta=t log p.

After folding theta modulo 2 pi, the prime-tower Toeplitz symbol is

sigma_p(theta)=p |1-r_p e^{i theta}|^2 Sigma_p(theta),

where

Sigma_p(theta)
=(1/log p) sum_{ell in Z}
 |zeta(1/2+i(theta+2 pi ell)/log p)|^2
 / (((theta+2 pi ell)/log p)^2+1/4).

Therefore, at Toeplitz-operator level,

T_p
=p (I-r_p S^*) T_{Sigma_p} (I-r_p S),

with the usual Hardy shift convention, whenever the symbols are interpreted in the standard quadratic-form sense.

The local factor is exactly the coherent-state precision operator. The residual factor is the periodized universal critical-line measure.

## Interpretation

The same local object has now appeared independently in:

1. critical zeta coherent states;
2. Nyman exact-conductor Ramanujan sources;
3. the finite Mobius/Koszul bulk;
4. the Hardy/Cayley boundary model.

The common local factor is 1-p^{-1/2} e^{i theta}. Composite conductors are products of these factors, while the target is supported on the prime-power vacuum sector through Lambda(p^k)=log p.

## Constructive triangular cancellation

Because the degree is omega(m)-1, conductors can be ordered triangularly by prime-support size. Formally one may:

* use prime powers to fix the constant Hardy coefficient;
* use two-prime conductors to cancel degree 1;
* use three-prime conductors to cancel degree 2;
* continue recursively.

This coefficient-by-coefficient construction is exact at the formal power-series level. It does not by itself prove RH because Hardy/Casimir norm convergence is the entire missing theorem. A test using the primorial chain shows that matching the first several Hardy jets does not automatically produce a small global norm error, so local jet cancellation is not a shortcut.

## Status

No RH proof is claimed. The gain is an exact identification of the prime coherent-state precision factors with the local factors of the Ramanujan/Nyman conductor fields, together with a precise Hardy/Koszul grading and the vacuum formula D_m(1)=-Lambda(m). The next target is a norm-level no-escape theorem for the multi-prime precision network, not another algebraic factorization.