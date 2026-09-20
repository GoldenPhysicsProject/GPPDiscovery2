# Exact four-lift orientation algebra on the Haar principal-series boundary

Date: 2026-09-20

This is a zero-independent infinite-dimensional realization of the finite orientation algebra
from Which Way Is Forward? v14 directly on the RH multiplicative-Haar spectral carrier.

## 1. Haar spectral space

Work on

H=L^2(R,dt).

Define the linear unitary involutions

(R f)(t)=f(-t),
(Sigma f)(t)=sgn(t) f(t),

and the standard antiunitary conjugation

(C f)(t)=conj(f(t)).

Ignoring the null set t=0,

R^2=Sigma^2=I,
R Sigma=-Sigma R,
C R=R C,
C Sigma=Sigma C.

## 2. Two commuting complex structures

Define

Iq_H=R Sigma,
It_H=i I.

Then

Iq_H^2
=
R Sigma R Sigma
=
-I,

and

It_H^2=-I.

Since It_H is scalar,

[Iq_H,It_H]=0.

Thus these are two commuting quarter-turn structures on the underlying real Hilbert space.

Their relative product is

chi_H=-Iq_H It_H
     =-i R Sigma.

Because Iq_H and It_H commute and each squares to -I,

chi_H^2=I.

Moreover Iq_H^*=-Iq_H, so

chi_H^*=chi_H.

Thus chi_H is a self-adjoint Z2 grading.

## 3. Critical real structure

Define the antiunitary involution

D_H=R C.

Then

D_H^2=I.

Because D_H is anti-linear,

D_H It_H=-It_H D_H.

Also

D_H Iq_H
=
R C R Sigma
=
C Sigma,

whereas

Iq_H D_H
=
R Sigma R C
=
-Sigma C.

Since C and Sigma commute,

D_H Iq_H=-Iq_H D_H.

Consequently

D_H chi_H=chi_H D_H.

Therefore the exact v14 algebra holds:

Iq_H^2=It_H^2=-I,
[Iq_H,It_H]=0,
chi_H=-Iq_H It_H,
D_H^2=I,
{D_H,Iq_H}=0,
{D_H,It_H}=0,
[D_H,chi_H]=0.

This is an exact infinite-dimensional realization on the Haar/principal-series carrier.
No zeta zero and no RH assumption appears.

## 4. Fixed real form

D_H f=f iff

f(-t)=conj(f(t)).

This is the standard Hermitian-symmetry condition.  The negative-frequency half is determined
by the positive-frequency half.

Under Fourier transform t -> u, D_H becomes ordinary coefficient conjugation:

F D_H F^{-1} g(u)=conj(g(u)),

up to the chosen Fourier normalization convention.

Thus the D_H-fixed real form is simply the real-valued logarithmic-time carrier.

This is the infinite Haar analogue of the finite D-fixed real form.

## 5. Time-domain form of the relative grading

Let H_u denote the ordinary Hilbert transform in logarithmic time, whose Fourier multiplier
is -i sgn(t).

Under Fourier transform,

Sigma_t <-> i H_u,
R_t <-> R_u.

Therefore

chi_H=-i R_t Sigma_t

becomes

chi_H <-> R_u H_u

(up to the Fourier sign convention).

Since reflection anticommutes with the Hilbert transform and H_u^2=-I,

(R_u H_u)^2=I.

So the relative orientation grading has a concrete Cauchy/Hilbert-transform realization in
logarithmic time.

This may be useful for comparing the orientation algebra to Hardy causality, but it is not
itself the Hardy projection.

## 6. Completed xi boundary operator is odd for the grading

On the critical line define

Xi(t)=xi(1/2+it),

which is real and even, and the completed co-Poisson boundary operator

A_xi=M_Xi R.

Then

A_xi^*=A_xi,

A_xi^2=M_{Xi^2}>=0.

The canonical orientation operators satisfy

[A_xi,D_H]=0,
[A_xi,It_H]=0,
{A_xi,Iq_H}=0,
{A_xi,chi_H}=0.

Proof of the nontrivial relation:

A_xi Iq_H
=
M_Xi R R Sigma
=
M_Xi Sigma,

while

Iq_H A_xi
=
R Sigma M_Xi R
=
M_Xi R Sigma R
=
-M_Xi Sigma,

because Xi is even.

Thus A_xi is an ODD self-adjoint first-order coupling between the chi_H=+1 and chi_H=-1
orientation sectors.

Its positive magnitude is

|A_xi|=M_|Xi|.

Hence it has the charged-Kahler form

A_xi=Q_xi h_xi,

where

h_xi=M_|Xi|>=0

and, away from the measure-zero real zero set,

Q_xi=M_{sgn Xi} R

is a self-adjoint involution.

## 7. Exact locking/decoupling interpretation

Because {A_xi,chi_H}=0, A_xi maps the two chi_H sectors into one another.

For a fixed t pair, the coupling magnitude is |Xi(t)|.

When Xi(t)!=0, the two orientation sectors are coupled.

At a critical-line zero Xi(gamma)=0, the coupling vanishes on that spectral fiber and the
two sectors decouple.

This is algebraically the same locking pattern as the v14 eight-component first-order
factorization:
nonzero transverse scalar locks two chiral halves, while zero scalar decouples them.

No physical identity between Xi and mass is claimed.  The exact common structure is a
grading-odd first-order coupling whose square is a positive scalar magnitude.

## 8. Vertical-line no-go and a line-selection identity

For any real a set

A_a=M_{f_a}R,
f_a(t)=xi(a+it).

Reality of xi makes A_a self-adjoint for every a.

But the canonical Haar complex structure Iq_H=R Sigma satisfies

A_a Iq_H + Iq_H A_a
=
M_{f_a(t)-f_a(-t)} Sigma.

Using the functional equation,

f_a(-t)
=
xi(a-it)
=
xi(1-a+it).

Hence

boxed(
{A_a,Iq_H}
=
M_{xi(a+it)-xi(1-a+it)} Sigma.
)

At a=1/2 this vanishes identically.

If it vanished for all t at some other real a, the entire function
z -> xi(a+z)-xi(1-a+z)
would vanish identically, making xi periodic with real period 1-2a.  Since xi is nonconstant
and has nonperiodic real-axis growth, this forces a=1/2.

Therefore the critical vertical line is the unique vertical line on which the completed
reflected xi operator is globally odd with respect to the canonical Haar orientation
complex structure.

This is a genuine line-selection theorem for the OPERATOR FAMILY A_a.

It is NOT RH: at an individual off-line zero rho=a+i gamma, both xi(rho) and xi(conj rho)
vanish, so the anticommutator also vanishes at that single spectral point.  Global
anticommutation of the whole vertical-line operator is stronger than pointwise vanishing
at one zero.

## 9. Refined RH target

The exact missing theorem can now be stated in the language of the orientation algebra:

Every nontrivial arithmetic zero/resonance must arise as a decoupling mode of the canonical
Haar four-lift boundary system, rather than as a resonance of a non-unitary/off-axis
continuation.

Equivalently, one must prove arithmetic admissibility of every zero in the fixed D_H-real
principal-series carrier.

This is the same hard spectral-admissibility/no-ghost theorem as before, now with a
canonical zero-independent orientation algebra attached to it.
