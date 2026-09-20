# Fermionic wedge-square decomposition of the BPY measure

Date: 2026-09-20

A new exact decomposition emerges from the first-order/orientation analysis.

## 1. Separate the iid orientation parent from the relative metric

Let u=x+y. The BPY weight is

u sinh(omega u)
=
cosh(omega u) k_omega(u),

where

k_omega(u)=u tanh(omega u)>=0.

The cosh factor has the exact two-lift product decomposition

cosh(omega(x+y))
=
(1/2) sum_{eta=+/-1}
 e^{eta omega x} e^{eta omega y}.

Thus before k_omega is inserted, the two q copies form a positive mixture of iid
exponentially tilted laws with one common orientation bit eta.

## 2. k_omega is a complete Bernstein function of u^2

The Mittag-Leffler expansion

tanh x / x
=
sum_{n>=1} 2/[x^2+pi^2(n-1/2)^2]

gives

x tanh x
=
2 sum_{n>=1}
 x^2/[x^2+a_n^2],

a_n=pi(n-1/2).

Therefore

k_omega(u)
=
(2/omega) sum_{n>=1}
 u^2/[u^2+(a_n/omega)^2].

Using

u^2/(u^2+b^2)
=
b int_0^infinity e^{-b lambda}(1-cos(lambda u)) d lambda,

one obtains the exact Levy representation

boxed(
k_omega(u)
=
int_0^infinity
(1-cos(lambda u))
nu_omega(lambda) d lambda
),

with

boxed(
nu_omega(lambda)
=
[pi/(2 omega^2)]
 cosh(pi lambda/(2 omega))
 / sinh^2(pi lambda/(2 omega))
)>0.

Thus k_omega is conditionally negative definite on the additive line.

## 3. Reflect one copy and obtain a wedge square

Put y'=-y. Since q is even,

u=x-y',

and the cosh parent becomes

cosh(omega(x-y'))
=
(1/2) sum_eta
 e^{eta omega x} e^{-eta omega y'}.

Also

1-cos(lambda(x-y'))
=
(1/2)|e^{i lambda x}-e^{i lambda y'}|^2.

Hence, up to the fixed overall normalization,

boxed(
d mu_omega
=
(1/4) sum_{eta=+/-1}
 int_0^infinity nu_omega(lambda)
 e^{eta omega x}q(x)
 e^{-eta omega y'}q(y')
 |e^{i lambda x}-e^{i lambda y'}|^2
 d lambda dt dx dy'
).

The phase difference is the 2x2 Slater determinant

e^{i lambda x}-e^{i lambda y'}
=
det [[e^{i lambda x},1],
     [e^{i lambda y'},1]].

Therefore the exact positive BPY measure is a continuum superposition of two-orbital
fermionic wedge-square channels, with opposite orientation tilts on the two reflected
copies.

This is an exact algebraic bridge to the exterior/Koszul sign architecture.

## 4. Reflection sign of the purified amplitude

For a fixed eta,lambda define the unsquared amplitude schematically by

Psi_{eta,lambda}(x,y')
=
sqrt(e^{eta omega x}q(x)e^{-eta omega y'}q(y'))
 [e^{i lambda x}-e^{i lambda y'}].

The original BPY swap becomes in reflected coordinates

J':(x,y')->(-y',-x).

The difference factor transforms as

e^{i lambda(-y')}-e^{i lambda(-x)}
=
-conj(e^{i lambda x}-e^{i lambda y'}).

Thus the wedge amplitude carries one exact reflection minus sign.

Because reflection plus coefficient conjugation is anti-linear, multiplication by i changes
this anti-linear eigen-sign. This is another literal occurrence of the project's
"- times - gives +" / spinorial-quarter-turn mechanism.

However reflection covariance of the purification is NOT by itself OS positivity.

## 5. Important no-go: fixed lambda channels are not individually positive

The tempting stronger claim would be that every fixed wedge mode (eta,lambda) already gives
a positive BPY reflection kernel, so that the lambda integral proves global positivity term
by term.

Direct zero-independent numerical evaluation using F(z)=xi(1/2+z)/xi(1/2) rejects this.
For example at omega=0.2, eta=+1, lambda=3 and a small real exponential test set
z={0,0.7,1.4,2.1}, the symmetrized fixed-lambda Gram matrix has a negative eigenvalue of
approximately -1.98e-3. Similar behavior occurs at omega=0.5, lambda=3.

This numerical diagnostic is not used as a theorem. Its role is to block an invalid
termwise-positivity proof strategy.

The full positive/negative cancellations across the continuum Levy measure are essential.

## 6. Current significance

The decomposition nevertheless gives a concrete first-order microscopic architecture:

common orientation tilt eta
+
antisymmetric two-copy phase wedge
+
positive continuum spectral measure nu_omega
=
BPY positive parent measure.

The missing RH statement is not positivity of the measure. It is positivity of the
one-step orientation-exchange Markov operator after this continuum of fermionic wedge modes
has been assembled.

A successful proof must therefore exploit the full lambda integral, likely through an exact
operator-valued Herglotz/Dirichlet-form identity, rather than prove positivity mode by mode.