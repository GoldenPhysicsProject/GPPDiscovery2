# A solvable holonomy model for mass-gap closure under orientation-pair sewing

Date: 2026-09-27
Status: exact toy-model spectral mechanism. It is not yet a derivation of black-hole horizon dynamics or Standard Model masses.

## 1. Mass from a twisted internal Dirac cycle

Take an internal circle/interval coordinate y of length L and the self-adjoint one-dimensional Dirac generator

D_alpha = -i d/dy

with quasi-periodic boundary condition

psi(y+L)=e^(i alpha) psi(y).

The normalized eigenmodes are

psi_n(y)=L^(-1/2) exp(i k_n y),

with

k_n L = 2 pi n + alpha.

Hence

boxed:
k_n=(2 pi n+alpha)/L.

For a massless higher-dimensional Dirac parent, separation on this internal mode gives the four-dimensional mass magnitude

boxed:
m_n = (hbar/c)|k_n|
    = (hbar/(cL)) |2 pi n+alpha|.

Thus the mass gap is exactly the spectral cost of nontrivial holonomy.

## 2. Lowest gap

Let

d(alpha,2 pi Z)
=
min_{n in Z}|alpha+2 pi n|.

Then

boxed:
m_gap(alpha)
=
(hbar/(cL))
d(alpha,2 pi Z).

So:

alpha not congruent 0 mod 2 pi
 -> positive gap;

alpha congruent 0 mod 2 pi
 -> zero mode allowed.

This is an exact boundary-condition mechanism by which holonomy creates an intrinsic Compton scale.

## 3. Compton and zitter clocks

For the lowest mode,

bar lambda_C
=
hbar/(m_gap c)
=
L/d(alpha,2 pi Z),

whenever the gap is nonzero.

The proper-time Compton frequency is

omega_C
=
m_gap c^2/hbar
=
(c/L)d(alpha,2 pi Z),

and the Dirac positive/negative-frequency beat is

boxed:
omega_Z
=
2 omega_C
=
(2c/L)d(alpha,2 pi Z).

Thus the twist angle, mass gap, Compton ruler, and zitter clock are exactly the same spectral datum in four units.

## 4. Orientation reversal preserves the one-sheet mass

Reverse the orientation holonomy:

alpha -> -alpha.

Since

d(-alpha,2 pi Z)=d(alpha,2 pi Z),

boxed:
m_gap(-alpha)=m_gap(alpha).

So, exactly as in the SU(1,1) transfer model, reversing the orientation does not make either individual sheet massless.

It only reverses the oriented holonomy.

## 5. Sew inverse holonomies

The two orientation holonomies are

U_+=e^(i alpha),
U_-=e^(-i alpha)=U_+^(-1).

Their product is

boxed:
U_pair=U_+ U_-=1.

If the branch-point sewing identifies the two internal transports into one composed cycle, the resulting boundary condition is untwisted:

psi(y+L_pair)=psi(y).

The composite Dirac operator therefore admits the n=0 mode

boxed:
k_0=0.

Hence the sewn pair has a zero spectral gap even though each separated orientation sector had the same nonzero gap.

This is the compact-unitary analogue of the earlier SU(1,1) identity

G(kappa)G(-kappa)=I,

whose composite trace discriminant is zero.

## 6. What this says about the horizon idea

The exact lesson is subtler than “a fermion reaches c and becomes massless.”

A mathematically consistent mechanism is:

separated orientation sectors
 -> inverse nontrivial holonomies
 -> each sector has a nonzero spectral mass gap;

branch-point sewing
 -> holonomies compose to identity
 -> relative/internal gap closes;

gapless output
 -> its four-dimensional dispersion can be null.

Schematically,

boxed:
inverse orientation holonomies
 + fixed-point sewing
 => trivial composite holonomy
 => zero internal Dirac eigenvalue
 => massless/null channel.

This is an actual solvable model realizing the qualitative idea.

## 7. Relation to energy conservation

Gap closure does not itself destroy the incoming rest energy.

A time-dependent or boundary interaction that changes the holonomy can transfer the energy stored in the massive mode into excitations of the gapless/outgoing sector.

Therefore the physical horizon model still needs a unitary conversion Hamiltonian or boundary condition implementing

massive paired input -> null radiation output

while preserving the relevant gauge charges and total stress-energy.

The spectral result supplies the missing kinematic possibility: inverse-orientation sewing can close the mass gap without requiring either incoming constituent to have zero mass beforehand.

## 8. Generalization target

The next non-toy version should replace U(1) by the actual orientation/internal connection K:

D_K^2
=
nabla_K^* nabla_K
+
curvature terms,

with opposite sheets carrying inverse parallel transports.

The desired theorem would show that the physical branch-point quotient trivializes the relative holonomy sector while retaining a positive outgoing null sector.

That would join:

orientation coupling,
internal Dirac mass,
curvature/confinement,
zitter frequency,
and horizon t-flip

in one operator construction.
