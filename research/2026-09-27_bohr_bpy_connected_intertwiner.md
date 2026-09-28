# Exact Bohr-to-BPY connected intertwiner: the singular scalar evaluation is one rank-one vacuum mode

Date: 2026-09-27
Status: exact zero-independent Hilbert-space construction from previously proved BPY covariance bounds. No RH claim.

This note joins two structures already derived independently:
1. the compact prime-torus Hardy space H2(K_ar), with basis chi_n;
2. the BPY Gaussian decimation representation U_n and centered vectors.

The result makes the "cancel before scalarization" principle precise.

## 1. Arithmetic Hardy basis

Let

K_ar = product_p S1

and let chi_n be the character associated with the prime-exponent vector of n. Then

H_ar := H2_+(K_ar)

has orthonormal basis {chi_n:n>=1}, hence H_ar is canonically ell2(N).

Let S_d be the multiplicative shift

S_d chi_n = chi_{dn}.

## 2. BPY centered decimation vectors

For a fixed complex parameter s in a compact set inside Re(s)>0, the existing BPY construction has

Omega_s = Q^(s/2),
a(s)=<1,Omega_s>=2 xi(s),

and multiplicative Gaussian Koopman isometries

U_m U_n = U_{mn},
U_d 1 = 1.

Define

tildeOmega_{n,s}
=
U_n Omega_s - a(s) 1.

The previously proved covariance estimate is

boxed:
|<tildeOmega_{m,s},tildeOmega_{n,s}>|
<=
C_K (m,n)^4/(m^2 n^2)

uniformly for s in each compact K subset {Re s>0}.

## 3. New Schur bound for the GCD kernel

Set

G(m,n)=(m,n)^4/(m^2 n^2).

For fixed m, write n=g k with g=(m,n), so g|m and (k,m/g)=1. Then

sum_n G(m,n)
=
sum_{g|m} sum_{(k,m/g)=1}
g^2/(m^2 k^2)

<=
zeta(2) sum_{g|m} g^2/m^2.

But

sum_{g|m} g^2/m^2
=
sum_{d|m} d^(-2)
<=
zeta(2).

Hence

boxed:
sup_m sum_n G(m,n) <= zeta(2)^2.

By symmetry the same column bound holds. Therefore the Schur test gives

boxed:
||G||_{ell2->ell2} <= zeta(2)^2.

## 4. Bounded connected synthesis

For finite arithmetic Hardy polynomials

f=sum_n c_n chi_n,

define

C_s f
=
sum_n c_n tildeOmega_{n,s}.

Using the covariance estimate and the Schur bound,

||C_s f||_2^2
<=
C_K <|c|,G|c|>
<=
C_K zeta(2)^2 ||c||_2^2.

Thus C_s extends uniquely to a bounded operator

boxed:
C_s : H2_+(K_ar) -> L2(P),

with

boxed:
||C_s|| <= zeta(2) sqrt(C_K).

This is a zero-independent bounded map from the compact arithmetic Hardy boundary into the connected BPY Hilbert sector.

## 5. Exact semigroup intertwining

On basis vectors,

C_s S_d chi_n
=
tildeOmega_{dn,s}.

On the other hand,

U_d C_s chi_n
=
U_d(U_n Omega_s-a(s)1)
=
U_{dn}Omega_s-a(s)1
=
tildeOmega_{dn,s}.

Therefore

boxed:
C_s S_d = U_d C_s

for every d>=1.

So C_s is not merely a bounded synthesis map. It exactly intertwines the multiplicative arithmetic shifts with the Gaussian/BPY decimation isometries.

This is the sought direct representation-theoretic bridge between the prime-torus/Peter-Weyl picture and the BPY field.

## 6. The uncentered map is exactly "singular evaluation + bounded connected part"

Formally define on finite Hardy polynomials

T_s chi_n = U_n Omega_s.

Then for

f=sum_n c_n chi_n,

T_s f
=
sum_n c_n U_n Omega_s

=
a(s)(sum_n c_n)1
+
C_s f.

But

sum_n c_n = f(alpha_0),

where

alpha_0=(1,1,...)

is the scalar Euler boundary point of the prime torus.

Hence

boxed:
T_s f
=
a(s) E_0(f) 1 + C_s f,

where E_0 is point evaluation at alpha_0.

The connected part C_s is bounded. E_0 is not bounded on H2(K_ar): on the N-term normalized polynomial N^(-1/2)sum_{n<=N}chi_n, its value is sqrt(N).

Thus the entire failure of the naive uncentered Bohr-to-BPY synthesis is a SINGLE rank-one coherent vacuum channel carrying the singular scalar evaluation.

This is a precise operator version of the project's repeated "one ghost / one vacuum escape" pattern.

## 7. Möbius state: the singular product renormalizes exactly to the Archimedean factor

For Re(s)>1, take the Bohr-Hardy Möbius vector

M_s = sum_n mu(n)n^(-s) chi_n.

Ordinary scalar evaluation gives

E_0(M_s)=1/zeta(s).

Therefore

T_s M_s
=
a(s)/zeta(s) 1 + C_s M_s.

Since

a(s)=2 xi(s)
=
[s(s-1) pi^(-s/2) Gamma(s/2)] zeta(s),

the singular scalar factors cancel exactly:

boxed:
a(s) E_0(M_s)
=
A_infty(s)
:=
s(s-1) pi^(-s/2) Gamma(s/2).

Hence

boxed:
T_s M_s
=
A_infty(s)1 + C_s M_s.

The right-hand side continues as an honest Hilbert-valued object to Re(s)>1/2 because:
- A_infty is explicit analytic completion data;
- M_s belongs to H2(K_ar) for Re(s)>1/2;
- C_s is bounded there (indeed locally for Re s>0).

This recovers the previously constructed connected BPY continuation, but now as the image of the prime-torus Hardy state under one bounded intertwiner plus one explicitly renormalized singular boundary evaluation.

## 8. Why this matters for the holographic reconstruction problem

The new Bohr-Hardy theorem said that internally

Z_s M_s = 1 in H1/L1

throughout Re(s)>1/2, while scalar evaluation is singular.

This note identifies a concrete field-theoretic replacement for the singular evaluation:
center first, map through C_s, and restore only the explicit Archimedean vacuum coefficient A_infty(s).

The prime side therefore already has:
- compact Peter-Weyl arithmetic modes;
- exact boson/Mobius cancellation;
- a bounded zero-independent map into the BPY Gaussian field;
- exact multiplicative-semigroup covariance;
- an explicit rank-one description of what scalarization loses.

The RH-bearing step is no longer "find some Hilbert space for the primes." It is:

boxed:
show that the completed physical observable / Schur quotient can be expressed using C_s and A_infty(s) without reintroducing the unbounded evaluation E_0.

If that can be done while retaining the exact completed xi response, the connected sector already has the correct half-plane domain.

## 9. Naive no-go audit

This result also corrects several possible overreactions.

- Failure of ordinary scalar evaluation at Re(s)<=1 does NOT mean the prime state fails; the internal H2 state and its connected BPY image both survive to Re(s)>1/2.
- Weak escape of the coherent vacuum does NOT imply all information escapes; the centered sector is bounded.
- The BPY map is not an arbitrary analogy: it is an exact semigroup intertwiner.
- None of this proves RH. The missing completed observable could still fail positivity/causality or could reintroduce an off-critical model-space defect.

The correct cheap falsifier for any proposed closure is now:
does it use E_0 again, explicitly or disguised as an uncontrolled all-ones coefficient functional?
If yes, the half-density obstruction has simply been reintroduced.
