# Exact Bohr-Hilbert lift of the arithmetic shadow phase

Date: 2026-09-20

This starts from the already proved causal Möbius identity but does NOT form the
reflected/casual convolution term-by-term in ordinary total variation.

For real sigma>1/2 let

z_sigma = sum_{n>=1} n^-sigma delta_{log n},
m_sigma = sum_{m>=1} mu(m)m^-sigma delta_{log m}.

Formally, z_sigma^vee * m_sigma has a contribution at

log(m/n).

Group the pairs by the reduced rational

m/n=r/s,  gcd(r,s)=1,

so m=kr and n=ks.

## 1. Exact reduced-rational coefficient

The coefficient attached to q=r/s is

a_sigma(r/s)
=
(rs)^(-sigma) sum_{k>=1} mu(kr) k^(-2sigma).

The k-series converges absolutely for sigma>1/2.

If r is not squarefree then mu(kr)=0 for every k, so a_sigma(r/s)=0.

If r is squarefree,

mu(kr)=
  mu(r)mu(k),  gcd(k,r)=1,
  0,            gcd(k,r)>1.

Hence

sum_k mu(kr) k^(-2sigma)
=
mu(r) prod_{p not| r}(1-p^(-2sigma))
=
mu(r)/
[zeta(2sigma) prod_{p|r}(1-p^(-2sigma))].

Therefore

boxed(
a_sigma(r/s)
=
mu(r) (rs)^(-sigma)
/
[zeta(2sigma) prod_{p|r}(1-p^(-2sigma))]
)

for reduced r/s with r squarefree.

## 2. Exact l2 normalization

Put x=2sigma>1. Then

sum_{(r,s)=1}|a_sigma(r/s)|^2

=
1/zeta(x)^2
sum_{r squarefree}
 r^-x/prod_{p|r}(1-p^-x)^2
 sum_{(s,r)=1}s^-x.

But

sum_{(s,r)=1}s^-x
=
zeta(x) prod_{p|r}(1-p^-x).

Thus the norm square is

1/zeta(x)
sum_{r squarefree}
 r^-x/prod_{p|r}(1-p^-x).

The remaining squarefree Euler product is

prod_p [1+p^-x/(1-p^-x)]
=
prod_p(1-p^-x)^-1
=
zeta(x).

Consequently

boxed(
sum_{q in Q_+^x}|a_sigma(q)|^2=1
)

for every sigma>1/2.

This is zero-independent.

## 3. Local prime state

Let rho_p=p^-sigma.  On the local exponent basis

{ |+1>, |0>, |-1>, |-2>, ... }

define

|Omega_{p,sigma}>
=
-rho_p |+1>
+
(1-rho_p^2)|0>
+
(1-rho_p^2) sum_{m>=1} rho_p^m |-m>.

Its norm is exactly one:

rho^2+(1-rho^2)^2+
(1-rho^2)^2 sum_{m>=1}rho^(2m)
=1.

The coefficient of |0> is 1-p^-2sigma, and

sum_p [1-<0|Omega_{p,sigma}>]
=
sum_p p^-2sigma<infinity

exactly for sigma>1/2.

Therefore the infinite tensor product

|Omega_sigma>=tensor_p |Omega_{p,sigma}>

exists in the incomplete tensor product based at the local vacuum for every
sigma>1/2.

Its coefficient at the finite exponent vector representing a reduced rational r/s is
exactly a_sigma(r/s).

Thus the l2 identity above is not accidental: it is the norm of an explicit all-prime
tensor product state.

## 4. Local unitary boundary phase

On |z|=1 the local Fourier series is

theta_{p,sigma}(z)
=
(1-rho^2)-rho z
+(1-rho^2) sum_{m>=1}rho^m z^-m

=
boxed((1-rho z)/(1-rho z^-1)).

Therefore

|theta_{p,sigma}(z)|=1.

At a finite prime set P and on the arithmetic one-parameter orbit
z_p=p^(-it),

prod_{p in P} theta_{p,sigma}(p^-it)
=
prod_{p in P}
(1-p^(-sigma-it))/(1-p^(-sigma+it)),

which is exactly the finite Euler shadow quotient, up to the chosen orientation convention.

So the all-prime state is the Bohr/Fourier lift of the local Euler shadow factors.

## 5. Why this does not yet prove RH

The Pontryagin dual of Q_+^x is the infinite prime torus T^P.  The global tensor state
defines an L2(T^P) function of norm one for every sigma>1/2.

The physical scalar zeta quotient is obtained by restricting that multivariable boundary
function to the arithmetic Kronecker orbit

t -> (p^-it)_p.

Restriction of a generic L2(T^P) function to this one-dimensional orbit is NOT a bounded
operation.  Equivalently, evaluating the Fourier coefficient vector by summing its
amplitudes requires l1 rather than l2 control.

Indeed:
- l2 convergence starts at sigma>1/2;
- absolute/l1 Euler convergence starts only at sigma>1.

This is the exact topology wall.

The construction therefore gives a canonical positive arithmetic parent Hilbert space all
the way to the principal-series boundary, but not yet the bounded physical section that
recovers the analytically continued scalar zeta quotient in 1/2<sigma<=1.

This is strikingly parallel to Which Way Is Forward? v14:
an ambient doubled/covering carrier can be exact while the physical Poincare/observer
section remains the decisive theorem.

## 6. Boundary behavior

The vacuum amplitude is

<0|Omega_sigma>
=
prod_p(1-p^-2sigma)
=
1/zeta(2sigma).

Hence as sigma->1/2+,

<0|Omega_sigma> -> 0

while ||Omega_sigma||=1.

Probability/norm does not disappear; it escapes into arbitrarily complicated rational
prime sectors. This is an exact arithmetic orthogonality catastrophe at the half-density
boundary.

This matches the previously observed coherent-state vacuum fidelity 1/zeta(2sigma) and
gives it a stronger shadow/Mobius interpretation.

## 7. New sharp target

Let B_sigma denote this Bohr-Hilbert arithmetic phase on the infinite prime torus and let
iota(t)=(p^-it)_p be the arithmetic flow.

The remaining theorem can be phrased as construction of a CLOSED pullback/trace map on the
specific completed prime-Archimedean graph space,

Tr_iota : H_graph -> H^2(boundary),

such that for sigma>1 its action agrees with the ordinary Euler quotient and such that the
Gamma completion makes the pullback bounded for every sigma>1/2.

If that trace map exists with the required causal orientation, analytic uniqueness carries
the Euler-half-plane identity into the strip. A pole of the scalar quotient would then be
incompatible with bounded Hardy pullback.

The generic L2 trace is impossible; the graph norm and Archimedean coupling must supply the
missing half derivative / boundary regularity. This is the exact functional-analytic place
where the proof must live.
