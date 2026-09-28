# Natural Archimedean heat-Gram candidates are nearly rank one: a density-matrix no-go

Date: 2026-09-27
Status: exact candidate definitions plus high-precision/numerical falsification against the zero-independent BPY cumulant target. No Riemann-zero data are used.

The current RH-equivalent Fredholm target is

F(z)=xi(1/2+z)/xi(1/2)=det(I+z^2 A),

with A>=0 trace class to be constructed without zero input.

The trace invariants required by xi are determined directly by derivatives at z=0:

Tr A = kappa_2/2,
Tr A^2 = -kappa_4/12,
Tr A^3 = kappa_6/240,

where kappa_j=d^j/dz^j log F(z)|_{z=0}.

Numerically from xi itself,

Tr A = 0.02310499311541897,
Tr A^2 = 3.717259928526969e-5,
Tr A^3 = 1.441739314009733e-7.

Hence the scale-free target ratios are

boxed:
Tr A^2/(Tr A)^2 = 0.06963238060969087,

boxed:
Tr A^3/(Tr A)^3 = 0.01168878070417578.

The normalized target density matrix rho=A/Tr A would therefore have purity about 0.06963 and effective rank

boxed:
1/Tr(rho^2) about 14.36.

This is a useful zero-independent fingerprint of any proposed vacuum operator.

## 1. Cheapest natural candidate from the theta boundary state

The number-circle reconstruction introduced

B_t(n)=exp(-pi t n^2/2), t>=1,

with

||B_t||^2=sum_n exp(-pi t n^2).

At s=1/2 the exact theta reconstruction uses the positive weight t^(-3/4)dt. So the most naive positive Gram candidate is

A_heat
=
int_1^infinity t^(-3/4) |B_t><B_t| dt,

up to an overall scale.

Its matrix entries are exact:

(A_heat)_{mn}
=
int_1^infinity
t^(-3/4)
exp[-pi(m^2+n^2)t/2] dt

=
a_{mn}^(-1/4) Gamma(1/4,a_{mn}),

a_{mn}=pi(m^2+n^2)/2.

The scale is irrelevant for purity ratios.

Numerical evaluation is already converged by the first few circle modes and gives

boxed:
Tr A_heat^2/(Tr A_heat)^2
=
0.9999855740427964,

boxed:
Tr A_heat^3/(Tr A_heat)^3
=
0.9999783610641947.

So A_heat is essentially rank one and is completely incompatible with the required collective density matrix.

No rescaling can repair this because the ratios are scale invariant.

## 2. The same failure occurs for the positive Riemann-density feature vectors

For u>=0 Riemann's Fourier density is termwise positive:

Phi(u)
=
sum_n
[
2 pi^2 n^4 exp(9u/2)
-
3 pi n^2 exp(5u/2)
]
exp[-pi n^2 exp(2u)].

Define the exact positive feature vector

C_u(n)
=
sqrt(
2 pi^2 n^4 exp(9u/2)
-
3 pi n^2 exp(5u/2)
)
*
exp[-pi n^2 exp(2u)/2],

so

boxed:
Phi(u)=||C_u||^2, u>=0.

The equally natural positive Gram operator

A_Phi=int_0^infinity |C_u><C_u| du

is again overwhelmingly dominated by n=1. Numerical quadrature gives

Tr A_Phi^2/(Tr A_Phi)^2 about 0.9996540,
Tr A_Phi^3/(Tr A_Phi)^3 about 0.9994810.

Again the target is 0.06963 and 0.01169.

## 3. Meaning of the failure

This is a useful killed route.

The Archimedean heat completion is enough to:
- regularize the singular all-ones boundary state;
- produce theta modularity;
- reconstruct xi exactly as a Mellin response.

But its simplest positive Gram operators have essentially one effective degree of freedom. The RH-equivalent Fredholm state requires an effective rank of order 14 already at the level of its first purity invariant.

Therefore the collective vacuum spectrum cannot come from a naive positive mixture of one-sided Archimedean heat states alone.

The missing spectral richness must arise from genuinely global prime/Archimedean interference, a two-sided modular quotient, a de Branges/canonical-system construction, or another nontrivial sewing operation.

This is an example of the project heuristic "a positive parent may be far too small even when it reproduces the right scalar response."

## 4. New falsification test for future density-operator candidates

For any candidate positive trace-class A_cand proposed as the arithmetic vacuum fluctuation operator, compute first, before any large proof attempt:

P2(A_cand)=Tr A_cand^2/(Tr A_cand)^2,
P3(A_cand)=Tr A_cand^3/(Tr A_cand)^3.

It must match the zero-independent xi targets

P2=0.06963238060969087,
P3=0.01168878070417578.

A mismatch kills the candidate even if it has the correct trace or reproduces one scalar xi identity.
