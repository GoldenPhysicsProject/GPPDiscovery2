# Casimir square-root resolvent and the real-place Gamma scattering factor

Date: 2026-09-20

This continues research/2026-09-19_adjacent_cell_divisibility_factorization.md.

The discrete Casimir-harmonic endpoint profile selected there is

k(x)=1/(1+x),

whose Mellin transform is the shadow-paired beta kernel

int_0^infinity x^{-s}/(1+x) dx
=
Gamma(s)Gamma(1-s)
=
pi/sin(pi s).

The half-density topology suggests taking the positive square root of the resolvent before
forming the Archimedean state.

## 1. Exact shadow-paired real Gamma factor

Define the standard real-place factor

gamma_R(s)=pi^(-s/2) Gamma(s/2).

For 0<Re(s)<1,

gamma_R(s) gamma_R(1-s)
=
pi^(-1/2) Gamma(s/2) Gamma((1-s)/2).

Since

B(a,b)
=
int_0^infinity t^(a-1)(1+t)^(-a-b) dt

and here

a=s/2,
b=(1-s)/2,
a+b=1/2,

one gets the exact identity

boxed(
gamma_R(s) gamma_R(1-s)
=
int_0^infinity
t^(s/2-1) / sqrt(1+t) dt
).

With t=r^2,

boxed(
gamma_R(s) gamma_R(1-s)
=
2 int_0^infinity
r^(s-1) / sqrt(1+r^2) dr
).

Thus the shadow-paired Riemann real-place magnitude is the Mellin transform of the
square-root resolvent profile

(1+r^2)^(-1/2).

This is the positive spectral square root of the elementary Casimir resolvent profile

(1+r^2)^(-1).

It gives an exact analytic reason that the natural RH graph topology repeatedly appears at
the H_C^(-1/2) level.

No identification of the discrete conductor variable with r is assumed here; the exact
statement is the shared resolvent hierarchy and Mellin transform.

## 2. Oriented Archimedean scattering ratio

Define

S_infty(s)
=
gamma_R(1-s)/gamma_R(s)
=
pi^(s-1/2)
Gamma((1-s)/2)/Gamma(s/2).

Then

boxed(
S_infty(1-s)=S_infty(s)^(-1)
).

On the critical line s=1/2+it,

gamma_R(1-s)=gamma_R(conj(s))=conj(gamma_R(s)),

so

boxed(
|S_infty(1/2+it)|=1
).

Therefore the same real-place factor naturally separates into:

- an even shadow-paired magnitude
  gamma_R(s)gamma_R(1-s);
- an oriented reciprocal scattering ratio
  gamma_R(1-s)/gamma_R(s).

This is the scalar Archimedean version of the project's first-order rule:
retain reciprocal orientation separately from positive magnitude.

## 3. Logarithmic derivative and the existing Gamma tower

The v34 real-place logarithmic derivative is

g_infty(s)
=
-1/2 log(pi)+1/2 psi(s/2).

This is exactly

boxed(
g_infty(s)=d/ds log gamma_R(s)
).

Consequently

d/ds log[gamma_R(s)gamma_R(1-s)]
=
g_infty(s)-g_infty(1-s),

while

boxed(
d/ds log S_infty(s)
=
-[g_infty(s)+g_infty(1-s)].
)

Thus the positive Gamma-Plancherel defect already present in v34 is the infinitesimal
response of the same square-root-resolvent real-place factor.

## 4. The two endpoint poles are the oriented Casimir resolvents

The completed local factor entering xi is

c_infty(s)
=
s(s-1) gamma_R(s).

Its logarithmic derivative is

boxed(
d/ds log c_infty(s)
=
1/s + 1/(s-1) + g_infty(s).
)

The previous Casimir-harmonic calculation derived the first two terms from the two oriented
endpoint resolvents:

1/s - 1/(1-s)
=
1/s + 1/(s-1).

Thus the entire elementary real-place logarithmic derivative has now been reconstructed in
two pieces from the boundary geometry:

1. full Casimir endpoint Green response:
   1/s + 1/(s-1);

2. half-density square-root resolvent:
   g_infty(s)=d log gamma_R(s)/ds.

This is an exact prime-independent decomposition.

## 5. Functional-equation phase cancellation

Away from zeros and poles, the zeta functional equation may be written

zeta(1-s)/zeta(s)
=
gamma_R(s)/gamma_R(1-s)
=
S_infty(s)^(-1)

after the polynomial factor s(s-1), which is shadow-invariant, is separated in the
completed xi normalization.

Hence the arithmetic and real-place oriented scattering ratios cancel exactly in the
completed functional equation.

This cancellation holds independently of RH. It therefore cannot by itself eliminate the
Hardy bad-zero inner factor. Its role is to identify the fixed zero-free Archimedean
orientation channel against which the causal arithmetic channel must be compared.

## 6. Consequence for the Casimir-completed Mobius approximant

The canonical tail

M_N^C(s)
=
sum_{d<=N} mu(d)d^(-s)
-
(N+1)M_1(N) sum_{d>N}d^(-s)/(d+1)

already contains the full Green endpoint smoothing, whose scaled limit is 1/s.

The next completion should NOT append an arbitrary Gamma multiplier.  The exact hierarchy
above says the real-place half-density correction is the spectral square root of the same
resolvent geometry.

The concrete next target is therefore to place the Casimir-harmonic tail in the
H_C^(-1/2) graph norm and compare its spectral square-root boundary response directly with
the Gamma-Plancherel feature map of v34.

If that comparison is an isometry or a controlled contraction, the endpoint tail and the
Gamma tower are two representations of one completed boundary channel rather than unrelated
counterterms.

Status: exact transform identities and structural synthesis; no RH claim.
