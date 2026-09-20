# Cesaro Gram = discrete Casimir Green operator; exact principal-series spectrum

Date: 2026-09-20

This is a new synthesis of the reciprocal Brownian/Casimir kernel already present in the
RH program with the classical Cesaro averaging operator.  All elementary identities below
are derived directly.  The full spectral diagonalization is independently cross-checked
against Frantisek Stampach, "The Hilbert L-matrix", arXiv:2107.10694, special case nu=1.

No RH claim is made.

## 1. The reciprocal Brownian kernel is exactly a Cesaro Gram operator

On l2(N), N={1,2,...}, define the Cesaro averaging operator

(Cx)_n = (1/n) sum_{k=1}^n x_k.

Its matrix is

C_{nk}=1/n  if k<=n,
C_{nk}=0    otherwise.

Therefore

(CC^*)_{mn}
=
sum_{k<=min(m,n)} 1/(mn)
=
min(m,n)/(mn)
=
boxed(1/max(m,n)).

But the RH/Casimir program already obtained exactly the same kernel from the logarithmic
half-line Green function:

(ij)^(-1/2) G_C(log i,log j)=1/max(i,j).

Hence the discrete Casimir/Brownian Green operator is

boxed(G = C C^*).

This is an exact operator identity, not an analogy.

## 2. The inverse is the discrete Casimir Jacobi operator

On finite sequences define

(Dh)_n = n h_n-(n-1)h_{n-1},  h_0=0.

Then D is the algebraic inverse of C:

D C = C D = I

on finite sequences.

Consequently

L := G^(-1) = D^* D

on the natural closed form domain.

Its Jacobi action is

boxed(
(Lh)_n
=
2n^2 h_n
-
n(n-1)h_{n-1}
-
n(n+1)h_{n+1}
),

with h_0=0.

Equivalently,

(Lh)_n
=
n(n+1)(h_n-h_{n+1})
+
n(n-1)(h_n-h_{n-1}).

The quadratic form is therefore

boxed(
<h,Lh>
=
sum_{n>=1} n(n+1)|h_n-h_{n+1}|^2
=
||D h||_2^2
).

This is exactly the discrete Casimir energy that arose independently in the ghost/capacity
calculation.

## 3. Sharp 1/4 spectral floor

The classical l2 Hardy/Cesaro inequality is

||C||=2.

Therefore

||G||=||CC^*||=4,

and on the inverse form domain

boxed(
L >= (1/4) I
).

Equivalently,

boxed(
sum_{n>=1} n(n+1)|h_n-h_{n+1}|^2
>=
(1/4) sum_{n>=1}|h_n|^2
).

The constant 1/4 is sharp.  The threshold generalized profile is n^(-1/2); slowly cut-off
versions produce Rayleigh quotients tending to 1/4.

Thus the critical half-density 1/2 and the Casimir floor 1/4 arise from the sharp Hardy
constant of the exact discrete Green operator.

## 4. Exact identification with the Hilbert L-matrix

Stampach studies

(L_nu)_{mn}=1/(max(m,n)+nu),  m,n>=0.

Our G on indices M,N>=1 becomes, after M=m+1, N=n+1,

G_{MN}=1/max(M,N)=1/(max(m,n)+1).

Hence

boxed(G = L_1)

under the index shift.

The inverse J_1 in that paper has b_n=(n+1)(n+2), which after the same shift is precisely
the Jacobi operator L above.

The published spectral theorem therefore applies exactly:

boxed(
sigma(L)=sigma_ac(L)=[1/4,infinity),
)

with simple multiplicity and no point spectrum.

Equivalently,

sigma(G)=sigma_ac(G)=[0,4].

This is the exact zero-independent principal-series continuum required by the Casimir fold.

## 5. Generalized eigenfunctions and the Casimir parameter s(1-s)

The eigenvalue equation

L h = lambda h

has the asymptotic indicial law

lambda=s(1-s),

because inserting h_n~n^(-s) into the Jacobi recurrence gives

L n^(-s)=s(1-s)n^(-s)+O(n^(-s-1)).

The critical continuum is therefore

s=1/2+i t,

lambda(t)=s(1-s)=1/4+t^2.

This is exactly the project's Casimir fold.

Stampach's Jost solutions have asymptotics

phi_n(z) ~ n^(-z-1/2)/Gamma(1+2z),

and the continuous spectrum corresponds to z=i t.  Thus the two asymptotic channels are

n^(-1/2-it), n^(-1/2+it),

the multiplicative principal-series characters on the integer boundary.

## 6. Elementary generating-function solution

The same spectral parameterization can be obtained directly.

Let

H(z)=sum_{n>=1}h_n z^n.

The Jacobi recurrence gives

boxed(
-z(1-z)^2 H''(z)+2z(1-z)H'(z)=lambda H(z).
)

Put

w=z/(1-z).

Then the equation collapses to

boxed(
-w(1+w) H_{ww}=lambda H.
)

Writing H=w F and x=-w gives the Gauss hypergeometric equation

x(1-x)F''+[2-2x]F'-lambda F=0.

Thus if lambda=s(1-s), the solution normalized by h_1=1 is

boxed(
H_s(w)
=
w * 2F1(s,1-s;2;-w).
)

This gives a direct generating-function realization of the principal-series Casimir
eigenfunctions without reference to zeta zeros.

## 7. The Green vector and the old 1/n harmonic tail

Since G e_1 has components

(G e_1)_n=1/n,

one has exactly

boxed(
L(1/n)=e_1
)

in the Green/distributional sense.

Thus the recurrent 1/n Casimir-harmonic tail found in the Mobius boundary-capacity problem
is the first Green column of the discrete principal-series operator.

Under the spectral transform U below,

U e_1 = 1,

so

U(1/n)=lambda^(-1).

This identifies the canonical harmonic endpoint completion as the zero-energy resolvent
profile of the same operator whose continuum begins at 1/4.

## 8. Exact continuous-dual-Hahn spectral measure

For the boundary vector e_1, the spectral variable is

lambda=1/4+t^2,  t>=0.

After the index shift, Stampach's nu=1 diagonalization gives

dmu(lambda)
=
rho(lambda) d lambda,

rho(lambda)
=
pi lambda
sinh(pi sqrt(lambda-1/4))
/
cosh^2(pi sqrt(lambda-1/4)).

Equivalently in t,

boxed(
dmu_C(t)
=
2 pi t (1/4+t^2)
[sinh(pi t)/cosh^2(pi t)] dt.
)

The corresponding orthogonal polynomials are the continuous dual Hahn specialization
(a,b,c)=(1/2,1/2,3/2).

The density has the Gamma representation

boxed(
dmu_C(t)
=
(1/(2 pi))
| Gamma(1/2+i t)^2 Gamma(3/2+i t) / Gamma(2 i t) |^2 dt.
)

## 9. Exact bridge to the celestial modular weight

The project's celestial principal-series spectral weight is

P(t)=Gamma(1+i t)Gamma(1-i t)=pi t/sinh(pi t).

Therefore the discrete arithmetic Casimir measure factors EXACTLY as

boxed(
dmu_C(t)
=
2(1/4+t^2) tanh^2(pi t) P(t) dt.
)

This is a direct bridge among:

- reciprocal Brownian/Casimir geometry;
- the l2 Cesaro operator;
- the principal-series Casimir lambda=1/4+t^2;
- continuous dual Hahn harmonic analysis;
- the same modular/Plancherel weight P(t)=pi t/sinh(pi t) used in the celestial sewing program.

The extra factor is precisely the Casimir eigenvalue times a thermal tanh^2 dressing.

No physical identification is asserted yet; the equality of measures is exact.

## 10. A useful sum rule

Because G_{11}=1,

<e_1,L^(-1)e_1>=1.

In the spectral representation this is

int_{1/4}^infinity lambda^(-1) rho(lambda)d lambda=1.

In t variables,

boxed(
2 pi int_0^infinity
t sinh(pi t)/cosh^2(pi t) dt
=1.
)

This follows directly by integrating the derivative of sech(pi t).

## 11. What this does and does not solve

This construction supplies, unconditionally and zero-independently:

1. a canonical positive self-adjoint discrete Casimir operator;
2. exact spectrum [1/4,infinity);
3. multiplicity-one principal-series generalized eigenstates;
4. a Gamma/thermal spectral measure;
5. the exact 1/n harmonic Green tail;
6. the exact Brownian/Nyman reciprocal kernel.

It does NOT put zeta zeros into that spectrum.

The RH problem is now naturally phrased as an arithmetic boundary/scattering problem on this
already-correct principal-series carrier:

construct the zero-independent arithmetic boundary vector/domain (Ramanujan/Mobius/co-Poisson
data) and prove that its completed characteristic/scattering determinant is xi while the
self-adjoint Casimir carrier is retained.

The proof-bearing missing theorem is therefore an intertwiner/boundary condition, not the
ambient Hilbert-Polya continuum.  An off-line zero would have to appear as a non-self-adjoint
resonance or an escaped boundary channel, exactly matching the existing Hardy ghost picture.

## Literature sanity check

The exact operator G is the nu=1 Hilbert L-matrix after the index shift. Stampach proves the
nu=1 inverse is the continuous-dual-Hahn Jacobi operator and diagonalizes it with simple
purely absolutely continuous spectrum [1/4,infinity). This confirms the derivation above but
is not used to motivate the RH interpretation.

Status: exact operator synthesis + literature-verified spectral theorem; no RH claim.


## 12. Hyperbolic radial form

The elementary generating-function equation

-w(1+w) H_{ww}=lambda H

has a direct hyperbolic coordinate.

Put

w=sinh^2(r/2).

Then

w(1+w)=(1/4)sinh^2 r,

and direct differentiation gives

boxed(
-H_{rr}+coth(r) H_r=lambda H.
)

Now make the half-density gauge

H(r)=sqrt(sinh r) psi(r).

The first derivative disappears and one obtains

boxed(
[-d^2/dr^2 + 1/4 + 3/(4 sinh^2 r)] psi
=
lambda psi.
)

This is exactly the one-dimensional Schrodinger form of the angular-momentum-one radial
Casimir equation on the hyperbolic plane.  In particular the threshold 1/4 and the
principal-series parameter lambda=1/4+t^2 are built into the geometry.

The discrete Jacobi operator, its Gauss hypergeometric generating equation, and this
hyperbolic radial problem are therefore three realizations of the same Casimir spectral
parameter.

This is an exact differential-equation equivalence.  It is not, by itself, a unitary
equivalence of the original l2 space with a radial hyperbolic L2 space; the unitary
spectral transform is the continuous-dual-Hahn transform in Section 8.

## 13. Exact principal-series scattering phase

Use

s=1/2+i t,
lambda=s(1-s)=1/4+t^2.

The normalized generating solution is

H_s(w)=w 2F1(s,1-s;2;-w).

As w->infinity, Gauss connection formula gives

H_s(w)
~
A_-(s) w^(1-s)
+
A_+(s) w^s,

with

A_-(s)=Gamma(1-2s)/[(1-s)Gamma(1-s)^2],

A_+(s)=Gamma(2s-1)/[s Gamma(s)^2].

Since w~e^r/4 and psi=H/sqrt(sinh r), these become the two scattering waves

e^(-i t r), e^(+i t r).

With the convention S_C(t)=outgoing/incoming, the ratio is

S_C(t)
=
4^(1-2s) A_+(s)/A_-(s).

Using the duplication formula and s=1/2+i t gives the exact simplification

boxed(
S_C(t)
=
-
[Gamma(1+i t)/Gamma(1-i t)]
[Gamma(3/2-i t)/Gamma(3/2+i t)].
)

Hence

|S_C(t)|=1

for real t, as required by the self-adjoint Casimir problem.

The first factor is the phase associated with the same Gamma(1+i t) whose modulus square is
the celestial modular weight

P(t)=|Gamma(1+i t)|^2=pi t/sinh(pi t).

The second half-integer Gamma ratio is the extra K-type-one boundary phase of this radial
problem.

Thus the exact spectral-measure bridge from Section 9 and the scattering phase are two
sides of one principal-series Gamma structure.

## 14. Interpretation for the RH program

The zero-independent ambient problem is now exceptionally rigid:

- discrete Green operator: G=C C^*;
- self-adjoint Casimir: L=G^(-1);
- exact spectrum: [1/4,infinity);
- asymptotic characters: n^(-1/2 +/- i t);
- hyperbolic radial equation: K-type-one principal series;
- Gamma scattering phase: S_C(t);
- continuous-dual-Hahn spectral transform;
- celestial modular factor P(t) sitting explicitly in the spectral density.

The arithmetic problem should therefore be treated as a boundary/intertwining problem on
this carrier, not as a search for another ambient spectral operator.

A high-value next step is to transform the Ramanujan/Mobius boundary generators through
the continuous-dual-Hahn spectral map and determine whether their closed span can be
described by an explicit inner/scattering multiplier.  If that multiplier is precisely the
Nyman bad-zero Blaschke factor, the Hardy ghost and the discrete Casimir pictures become
literally the same spectral boundary defect.

