# RH relative-Higgs kernel and inverse order parameter
## Date: 2026-09-24
## Status: exact finite causal convolution identities; structural reduction, not RH

This note refines RH_RELATIVE_HIGGS_CONDENSATE_2026-09-24.md.

Let
Z_ar = sum_{n<e^L} n^(-1/2) delta_{log n}
in the causal convolution algebra on [0,L), and
M_vac = delta_0 - e^(-y/2) 1_(0,L)(y) dy.
The relative Higgs field is H_L=M_vac*Z_ar.

## 1. Exact kernel

Convolution gives
dH_L(y)
=
sum_{n<e^L} n^(-1/2) delta_{log n}(dy)
-
e^(-y/2) floor(e^y) dy,
for 0<=y<L.

Indeed each atom at log n contributes
n^(-1/2)e^{-(y-log n)/2}=e^(-y/2)
to the continuous tail once y>=log n.

Thus the relative field is exactly the discrepancy between the discrete half-density counting measure and its elementary counting continuum.

## 2. Uniformly bounded primitive

For x=e^y put
S(x)=sum_{n<=x} n^(-1/2).
The cumulative mass of H_L up to y is
C(y)=S(x)-int_1^x floor(t)t^(-3/2)dt.

Stieltjes integration by parts gives
S(x)=floor(x)/sqrt(x)+(1/2)int_1^x floor(t)t^(-3/2)dt,
hence
C(y)=2 floor(x)/sqrt(x)-S(x).

Elementary integral comparison for the decreasing function t^(-1/2) gives
S(x)=2 sqrt(x)+O(1).
Therefore
C(y)=O(1)
uniformly in y and L.

No PNT, zeta zero information, or Möbius cancellation is used.

Consequently the relative Higgs source has no exponential coherent primitive. Its current numerator [X,H_L], whose kernel is y dH_L(y), has at most polynomial-in-L primitive growth.

## 3. Exact inverse kernel

The arithmetic inverse is
M_ar=sum_{n<e^L} mu(n)n^(-1/2) delta_{log n},
and
Z_vac=delta_0+e^(y/2)dy.

Since H_L=M_vac Z_ar,
H_L^(-1)=M_ar Z_vac.

Convolution gives
dH_L^(-1)(y)
=
sum_{n<e^L} mu(n)n^(-1/2) delta_{log n}(dy)
+
e^(y/2) M_1(e^y) dy,
where
M_1(x)=sum_{n<=x} mu(n)/n.

Indeed each atom mu(n)n^(-1/2) at log n contributes
mu(n)n^(-1/2)e^((y-log n)/2)
=
e^(y/2) mu(n)/n
to the continuous tail.

Thus the inverse-Higgs susceptibility is governed exactly by the weighted Mertens order parameter M_1.

The RH-strength scale is
e^(L/2) M_1(e^L)=e^{o(L)}
(up to the usual epsilon/polylog formulation). Via partial summation this is equivalent in strength to the classical Mertens form M(x)=O(x^(1/2+epsilon)) for every epsilon>0.

Therefore the relative-Higgs construction has not hidden RH in an abstract norm: it exposes the precise inverse-field order parameter.

## 4. Mass-gap limitation

The many-prime causal Hodge gap
||D_L^{-1}||=O(sqrt(L)e^(-L/2))
does not by itself bound H_L^{-1}.

A finite-dimensional model shows why. For N scalar local Higgs factors t_j with |t_j|>=c>0, the CAR Dirac has
D^2=(sum_j |t_j|^2)I >= Nc^2 I,
so ||D^-1||<=1/(c sqrt N).
But the determinant-line inverse is
(prod_j t_j)^(-1),
which may grow like c^(-N).

Hence collective Hodge mass does not control determinant-line susceptibility without an additional connected/torsion/free-energy theorem. This is the mass-versus-entropy barrier.

## 5. Renormalized scalar approximants: useful no-go

The elementary continuum-subtracted Dirichlet approximant is
H_X(s)
=
1+(s-1)/s [
 sum_{n<=X}n^(-s)-1-int_1^X x^(-s)dx
]
=
[X^(1-s)+(s-1)sum_{n<=X}n^(-s)]/s.

Euler summation gives local uniform convergence
H_X(s)->((s-1)/s) zeta(s)
for Re s>0.

However the finite H_X are not zero-pinned to Re s=1/2. Near the first critical zero, high-precision root finding gives representative roots:
X=10:     0.5516511201 + 14.30883258 i
X=30:     0.5571391392 + 14.05560055 i
X=100:    0.5437031226 + 14.16347536 i
X=300:    0.4810313412 + 14.09910714 i
X=1000:   0.5166999080 + 14.12830610 i
X=3000:   0.4877801307 + 14.13790107 i.

They oscillate across the critical line while converging toward the physical zero. Therefore continuum subtraction plus Hurwitz is not a proof mechanism. A self-adjoint/canonical-system/Higgs stability input is genuinely necessary.

## 6. Current frontier

The Higgs mechanism has now achieved three exact simplifications:

1. raw discrete half-density field = continuum condensate + bounded-primitive relative field;
2. raw prime current = continuum vacuum current + relative logarithmic current;
3. inverse relative field = explicit Möbius field + e^(y/2) M_1(e^y) dy.

The remaining theorem must control the inverse/connected susceptibility, not the source.

Candidate routes:
- a supersymmetric/torsion Ward identity that turns the many-prime Hodge mass into cancellation of the weighted Möbius supertrace;
- a canonical-system realization of the relative current whose Weyl function is automatically Herglotz;
- or the corrected Nevanlinna/Hermite escape route.

Any argument using only the bulk gap, without controlling determinant-line entropy, is insufficient.
