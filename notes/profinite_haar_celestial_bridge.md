# Profinite Haar / celestial principal-series bridge

Status: exact lemmas proved algebraically below; RH remains open.

## 1. Critical Haar boundary

Let
[
widehat{mathbf Z}=prod_p mathbf Z_p
]
with normalized additive Haar probability measure (mu), and let
(Omega=1in L^2(widehat{mathbf Z},mu)).

For (mge1), define
[
(V_m f)(x)=sqrt m,mathbf 1_{mwidehat{mathbf Z}}(x),f(x/m).
]

Because (mu(mE)=m^{-1}mu(E)), (V_m) is an isometry and
(V_mV_n=V_{mn}).

Moreover
[
V_mOmega=sqrt m,mathbf 1_{mwidehat{mathbf Z}},
qquad
langleOmega,V_mOmegaangle=m^{-1/2}.
]

For (m,nge1),
[
egin{aligned}
langle V_mOmega,V_nOmegaangle
&=sqrt{mn},mu(mwidehat{mathbf Z}cap nwidehat{mathbf Z})\
&=rac{sqrt{mn}}{operatorname{lcm}(m,n)}\
&=rac{gcd(m,n)}{sqrt{mn}}\
&=prod_p p^{-rac12|v_p(m)-v_p(n)|}.
end{aligned}
]

Thus the critical GCD kernel is exactly the Gram kernel of normalized
divisibility-cylinder vectors in the Haar boundary.  Prime-by-prime it is the
tensor product of the local Toeplitz/Poisson kernels with radius (p^{-1/2}).

The ghost cylinder law
[
mu(v_p=a)=(1-p^{-1})p^{-a}
]
is therefore literally Haar measure on (widehat{mathbf Z}), not merely
analogous to it.

## 2. Half-density from unitary dilation

Let (mathbf A_f) be the finite adeles with additive Haar measure.  For
(minmathbf Q_+^	imes), define
[
(U_mF)(x)=sqrt m,F(x/m).
]
For integer (m), the finite-adelic modulus satisfies (|m|_f=m^{-1}),
hence (U_m) is unitary.  If (P) denotes projection from
(L^2(mathbf A_f)) onto (L^2(widehat{mathbf Z})), then
[
P U_m P = V_m.
]

So the unilateral arithmetic isometries are compressions of genuine unitary
finite-adelic dilations.  The coefficient (m^{-1/2}) is fixed by Haar
normalization.

Introduce the gauge/dilation phase
[
alpha_t(V_m)=m^{-it}V_m.
]
Then
[
langleOmega,alpha_t(V_m)Omegaangle
=m^{-1/2-it}.
]
Hence the critical Mellin character (m^{-s}), (s=1/2+it), is an exact
vacuum matrix coefficient of the Haar-normalized dilation system.  Replacing
(1/2) by a different real part changes the Haar normalization and destroys
unitarity.

For finite (L),
[
leftlangleOmega,
sum_{log nle L}Lambda(n)alpha_t(V_n)Omega
ightangle
=
sum_{log nle L}rac{Lambda(n)}{sqrt n},e^{-itlog n},
]
which is exactly the finite prime current appearing in the completed
arithmetic phase (J_L).

## 3. Doubled Gibbs / cross-boundary form

For (eta>1), with
[
|Psi_etaangle=
zeta(eta)^{-1/2}sum_{nge1}n^{-eta/2}|n,nangle,
]
and multiplicative isometries (V_m|nangle=|mnangle),
[
langlePsi_eta|V_motimes V_n|Psi_etaangle
=delta_{mn}m^{-eta/2}.
]
Therefore, for finite
[
A_L=sum_{log nle L}sqrt{Lambda(n)},V_n,
]
one has
[
langlePsi_eta|
alpha_t(A_L)otimes A_L
|Psi_etaangle
=
sum_{log nle L}Lambda(n)n^{-eta/2}e^{-itlog n}.
]
At the boundary (etadownarrow1), every finite cutoff gives the exact
half-density prime current.  The prime term is therefore a genuine
cross-boundary correlation of the doubled arithmetic state.

## 4. Exact celestial Casimir dictionary

Set
[
h=s,qquad Delta=2s,qquad 
u=h-1=s-1.
]
Then
[
Deltamapsto2-Delta
iff
smapsto1-s
iff

umapsto-
u-1,
]
and identically
[
-
u(
u+1)=s(1-s).
]

On the unitary principal series,
[
s=rac12+it,qquad
Delta=1+ilambda,qquad
lambda=2t,
]
so
[
-
u(
u+1)=s(1-s)=rac14+t^2=rac{1+lambda^2}{4}.
]

Thus the celestial conical/Legendre Casimir and the arithmetic massive
half-density Casimir are the same quadratic spectral invariant under the
dictionary.  The (1/4) floor is the same half-density shift that appears in
unitary dilation.

## 5. What this does and does not prove

This identifies a concrete common architecture:

- finite-place Haar geometry produces the (p^{-1/2}) critical local radius;
- the global critical GCD kernel is a Haar Gram kernel;
- prime powers are matrix coefficients of compressed unitary dilations;
- the von Mangoldt current is an energy-weighted boundary correlation;
- celestial shadow and arithmetic functional reflection act by the same
  (sleftrightarrow1-s) / (
uleftrightarrow-
u-1) involution;
- both carry the same Casimir (s(1-s)).

It does **not** yet prove RH.  The remaining load-bearing statement is still a
global no-escape / completeness theorem: the completed prime--Archimedean
scattering response must have no resonance contribution outside the unitary
principal-series carrier.  Equivalently, the Hardy incoming defect/model
space for bad zeros must vanish.

The new result sharpens the target: the missing intertwiner should connect the
profinite Haar dilation system (finite places) and the Archimedean/celestial
principal-series Casimir, while preserving the completed prime--Archimedean
current.  If that intertwiner makes the completed causal transfer an
isometry, the existing Hardy-leakage theorem gives RH.
