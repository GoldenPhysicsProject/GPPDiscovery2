# Exact number-circle / prime-Fock duality and Archimedean heat reconstruction

Date: 2026-09-27
Status: exact zero-independent operator identities and completed-theta reconstruction. No RH claim. This note was motivated by Daniel's "number circle -> holographic complex bulk -> vacuum spectrum" picture and by the current requirement to replace the singular Euler evaluation with an honest completed reconstruction.

## 1. One Hilbert space, two exact descriptions

Let H_circ be the positive-frequency Hardy sector of L2(S1), with orthonormal basis

e_n(theta)=exp(i n theta),  n>=1.

Let D=-i d/dtheta on this sector. Then

D e_n = n e_n,

and the circle Laplacian Delta=D^2 has

Delta e_n=n^2 e_n.

Define the arithmetic Hamiltonian

H_ar = log D = (1/2) log Delta,

so

boxed:
H_ar e_n=(log n)e_n.

Now let

F_pr = incomplete tensor product_p ell2(N_0)

with finite-occupation basis |(k_p)> and number operators N_p.

Unique factorization gives a canonical basis unitary

U : H_circ -> F_pr,

U e_n = tensor_p e_{nu_p(n)}.

Since log n=sum_p nu_p(n) log p,

boxed:
U H_ar U^{-1}
=
sum_p (log p) N_p

on the finite-occupation core.

This is an exact additive/multiplicative dual description of the same operator.

## 2. Zeta is simultaneously a circle spectral trace and a prime-gas partition function

For Re(s)>1,

Tr exp(-s H_ar)
=
sum_n n^{-s}
=
zeta(s).

On the full nonzero circle spectrum, Delta has the +/-n degeneracy, so

boxed:
zeta(s)
=
(1/2) Tr' Delta^{-s/2}.

Under the prime-Fock unitary,

boxed:
zeta(s)
=
Tr_Fpr exp[-s sum_p(log p)N_p]
=
product_p (1-p^{-s})^{-1}.

Therefore the Euler product and the spectral zeta of the number circle are not two analogies. They are two exact traces of the same diagonal spectrum under the unique-factorization unitary.

Equivalently,

boxed:
log |D|
<--> 
sum_p (log p) N_p.

The integer Fourier mode n is the same state as the prime occupation vector (nu_p(n)).

## 3. The singular boundary state and the arithmetic TFD

Let formally

|B> = sum_{n>=1} e_n.

This is not a Hilbert vector. In the prime-Fock basis it is the formal product

|B> = tensor_p (sum_{k>=0}|k>_p).

Arithmetic thermal regularization gives

exp(-beta H_ar/2)|B>
=
sum_n n^{-beta/2}e_n
=
tensor_p sum_{k>=0}p^{-beta k/2}|k>_p.

Its squared norm is

zeta(beta),

so it is normalizable iff beta>1.

After normalization this is exactly the global arithmetic TFD / Gibbs purification already derived from the prime factors.

Thus the ubiquitous critical half-density is the point where the distributional boundary state stops becoming a normalizable vector under logarithmic/arithmetic radial evolution.

## 4. A second regularization of the SAME boundary state gives the Jacobi theta kernel

Instead use the local circle heat semigroup. For t>0,

|B_t>
=
exp(-pi t Delta/2)|B>
=
sum_{n>=1} exp(-pi t n^2/2)e_n

is a genuine Hilbert vector and

||B_t||^2
=
sum_{n>=1}exp(-pi t n^2).

Therefore with the Jacobi theta function

vartheta(t)=sum_{n in Z}exp(-pi n^2 t),

boxed:
vartheta(t)-1=2||B_t||^2.

So the ordinary theta heat trace is literally the norm-square of the heat-regularized arithmetic boundary state.

Under the prime-Fock unitary,

Delta=D^2=exp(2H_ar),

hence

boxed:
exp(-pi t Delta/2)
=
exp[-(pi t/2) exp(2H_ar)].

The Archimedean heat regulator is therefore a non-factorizing function of the total prime energy. It couples the otherwise factorized prime occupations at the level of the global thermal weight.

This supplies a precise physical reason the completed response can have collective resonances not attributable to any single prime.

## 5. The completed xi function is the modular Mellin transform of the heat-regularized boundary norm

For Re(s)>1,

Lambda(s)
:=
pi^{-s/2} Gamma(s/2) zeta(s)
=
(1/2) int_0^infinity [vartheta(t)-1] t^(s/2) dt/t.

Use the exact Poisson/modular identity

vartheta(t)=t^(-1/2)vartheta(1/t).

Splitting at t=1 and reflecting the interval (0,1) gives the entire continuation

boxed:
Lambda(s)
=
1/[s(s-1)]
+
(1/2) int_1^infinity
[vartheta(t)-1]
[t^(s/2)+t^((1-s)/2)]
dt/t.

Therefore

boxed:
xi(s)
=
1/2
+
(1/4)s(s-1)
int_1^infinity
[vartheta(t)-1]
[t^(s/2)+t^((1-s)/2)]
dt/t.

Using vartheta(t)-1=2||B_t||^2,

boxed:
xi(s)
=
1/2
+
(1/2)s(s-1)
int_1^infinity
||B_t||^2
[t^(s/2)+t^((1-s)/2)]
dt/t.

This is an exact entire reconstruction from positive Hilbert norms. It uses no zeta zeros and no singular point evaluation after the heat regularization.

The functional equation xi(s)=xi(1-s) is manifest: it is the exchange of the two modular/Mellin sheets in the bracket.

## 6. The completed reconstruction really regularizes the all-ones functional

For any c=(c_n) in ell2, define the heat-regularized scalar evaluation

E_t(c)
=
sum_n exp(-pi t n^2/2)c_n.

This is bounded for every t>0, with

|E_t(c)|
<=
[sum_n exp(-pi t n^2)]^(1/2) ||c||_2
=
||B_t|| ||c||_2.

So the Archimedean heat evolution converts the singular all-ones evaluation into an honest bounded Hilbert functional before scalarization.

This is exactly the construction principle demanded by the Bohr-Hardy half-plus-half obstruction.

Important limitation: the formula for xi above is the reconstruction of the singular boundary state itself, not yet a positive Fredholm determinant. A Mellin/Fourier transform of positive norms can still have off-axis Fisher zeros.

## 7. Two regularizations, two physical polarizations

The SAME formal boundary state |B> admits two distinguished evolutions:

Arithmetic/logarithmic:
exp(-beta H_ar/2)|B>
  -> zeta Gibbs/TFD state
  -> prime factorization
  -> critical normalizability boundary beta=1.

Geometric/Archimedean:
exp(-pi t Delta/2)|B>
  -> theta heat state
  -> Poisson modular reflection t<->1/t
  -> completed xi response.

Since Delta=exp(2H_ar), these are two functional calculi of one positive circle momentum operator.

This gives an exact meaning to the idea that the prime gas and the conformal circle are two holographic descriptions of one number system.

## 8. Why primes are microscopic and zeros are collective

In prime variables,

H_ar=sum_p(log p)N_p

is additive and the zeta Gibbs state factorizes.

But the heat operator entering the Archimedean completion is

exp[-(pi t/2) exp(2 sum_p(log p)N_p)].

This does not factor into independent prime heat operators. It depends nonlinearly on the total prime energy.

Thus:
- primes are elementary occupation modes of the multiplicative Hamiltonian;
- integer Fourier modes are the geometric momentum basis;
- Archimedean heat completion globally couples those modes;
- xi is the modular Mellin response of the coupled heat system;
- any Riemann-zero "vacuum spectrum" must therefore be collective.

This is a concrete operator mechanism, not only a metaphor.

## 9. Mixed heat/Dirichlet family

Define for t>0

Z(s,t)=sum_{n>=1} n^{-s} exp(-pi n^2 t).

For every fixed t>0 this is entire in s, because of Gaussian decay.

It obeys the exact shift-flow equation

boxed:
partial_t Z(s,t) = -pi Z(s-2,t).

As t decreases to zero, Z(s,t)->zeta(s) only in the ordinary Dirichlet domain Re(s)>1. The modular heat completion is therefore the mechanism needed to cross the scalar boundary.

This two-parameter family is a natural numerical and analytic workbench for studying how collective zeros emerge from a heat-regularized, everywhere-entire approximation without confusing finite-t zero patterns with the completed limit.

## 10. Naive-no-go audit

Several conclusions are explicitly NOT justified:

1. The positivity of ||B_t||^2 does not imply the Mellin transform xi has only critical zeros.
2. The circle Laplacian eigenvalues n^2 are not Riemann-zero ordinates.
3. zeta being a spectral zeta of S1 does not prove RH.
4. The prime-Fock/circle equivalence is a basis/unitary equivalence of the free arithmetic Hamiltonian; the RH-bearing information enters through completed reconstruction / modular sewing.
5. The modular theta identity gives an honest reconstruction that avoids raw E_0, but positive Fredholm/canonical-system structure remains missing.

The gain is that the "completed reconstruction map" is no longer abstract: the canonical Archimedean candidate is the circle heat semigroup followed by modular Mellin sewing.
