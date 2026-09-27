# Prime TFD phase geometry: Poisson kernels, Fisher hyperbolic metric, and mass as information distance

Date: 2026-09-27
Status: exact local/finite-prime identities and a global interpretation target. No external literature search used.

## 1. Canonical phase POVM of the paired prime mode

For one prime let

[
r_p=p^{-1/2},qquad L_p=log p.
]

On the paired diagonal subspace
[
mathcal K_p=overline{mathrm{span}}{|m,mangle:mge0}congell^2(mathbb N_0),
]
the critical TFD vector is

[
|Omega_pangle
=
sqrt{1-r_p^2}
sum_{mge0}r_p^m|m,mangle.
]

Introduce the distributional phase vectors

[
|	hetaangle
=
sum_{mge0}e^{-im	heta}|m,mangle,
qquad 0le	heta<2pi.
]

They resolve the identity in the standard weak POVM sense,

[
int_0^{2pi}rac{d	heta}{2pi}
|	hetaanglelangle	heta|
=I_{mathcal K_p}.
]

The TFD phase amplitude is

[
langle	heta|Omega_pangle
=
rac{sqrt{1-r_p^2}}
{1-r_p e^{i	heta}}.
]

Hence its phase probability density is the Poisson kernel:

[
oxed{
f_p(	heta)
=
rac1{2pi}
rac{1-r_p^2}
{1-2r_pcos	heta+r_p^2}
=
rac1{2pi}mathcal P_{r_p}(	heta).
}
]

Thus the same Poisson kernel previously obtained as the local Blaschke group delay is literally the canonical phase intensity of the prime TFD state.

## 2. Von Mangoldt half-density current = centered TFD phase intensity

The Poisson expansion is

[
mathcal P_r(	heta)
=
1+2sum_{mge1}r^mcos(m	heta).
]

Setting (	heta=tL_p) and (r=r_p=p^{-1/2}),

[
oxed{
sum_{mge1}
(log p)p^{-m/2}cos(mtlog p)
=
rac{L_p}{2}
left[
mathcal P_{r_p}(tL_p)-1
ight].
}
]

Equivalently,

[
oxed{
	ext{prime-power current}
=
	ext{modular energy}
	imes
	ext{TFD phase intensity above its uniform vacuum baseline}.
}
]

The Fourier moments are

[
int_0^{2pi}e^{im	heta}f_p(	heta),d	heta
=
r_p^m
=
p^{-m/2}.
]

Therefore

[
oxed{
rac{Lambda(p^m)}{sqrt{p^m}}
=
L_p
int e^{im	heta}f_p(	heta),d	heta.
}
]

This gives a direct quantum/statistical realization of every von Mangoldt half-density coefficient.

## 3. Full complex local current is a Caratheodory function

For (z=re^{i	heta}) in the unit disk,

[
H(z)=rac{1+z}{1-z}
]

has

[
Re H(z)
=
rac{1-r^2}{|1-z|^2}
=
mathcal P_r(	heta)>0.
]

Also

[
rac{z}{1-z}
=
rac12(H(z)-1).
]

Hence the local Euler logarithmic derivative is a positive-real function minus its vacuum baseline:

[
oxed{
L_prac{z}{1-z}
=
rac{L_p}{2}H(z)-rac{L_p}{2}.
}
]

On the critical line (z=p^{-1/2-it}), the positive real part is exactly the prime TFD phase intensity/group delay. The sign-indefinite arithmetic current appears only after subtracting the free half-energy baseline.

This makes the local no-ghost statement precise: every prime channel is passive/positive before relative vacuum subtraction.

## 4. Finite-prime modular flow is a torus flow

For distinct primes (p_1,dots,p_k), the logarithms
[
log p_1,dots,log p_k
]
are linearly independent over (mathbb Q): an integer relation would contradict unique factorization.

Therefore the flow

[
tmapsto
(tlog p_1,dots,tlog p_k)
pmod{2pi}
]

is equidistributed on the finite torus.

For the centered finite-prime current

[
J_{mathcal P}(t)
=
sum_{pinmathcal P}
sum_{mge1}
L_p r_p^mcos(mL_pt),
]

the long-time mean is exactly

[
oxed{langle J_{mathcal P}angle=0.}
]

Its autocorrelation is

[
oxed{
lim_{T	oinfty}rac1T
int_0^T
J_{mathcal P}(t)J_{mathcal P}(t+	au),dt
=
rac14sum_{pinmathcal P}
L_p^2
left[
mathcal P_{1/p}(L_p	au)-1
ight].
}
]

In particular,

[
oxed{
operatorname{Var}(J_{mathcal P})
=
rac12sum_{pinmathcal P}
rac{(log p)^2}{p-1}.
}
]

The radius in the second-order kernel is (r_p^2=1/p): the half-density amplitude squares to the Haar/Gibbs occupation parameter.

## 5. Fisher metric of the prime phase family

Consider the full two-parameter Poisson family

[
f_{r,phi}(	heta)
=
rac{1-r^2}
{2pi,[1-2rcos(	heta-phi)+r^2]},
qquad 0<r<1.
]

Direct integration of the score functions gives

[
I_{rr}
=
rac{2}{(1-r^2)^2},
qquad
I_{phiphi}
=
rac{2r^2}{(1-r^2)^2},
qquad
I_{rphi}=0.
]

Thus the Fisher-Rao metric is

[
oxed{
ds_F^2
=
rac{2,(dr^2+r^2dphi^2)}
{(1-r^2)^2}.
}
]

This is exactly one half of the standard Poincare-disk metric. Its Gaussian curvature is therefore

[
oxed{K_F=-2.}
]

So the prime TFD/Blaschke family is not merely hyperbolic by analogy: its canonical statistical metric is a constant-negative-curvature disk.

## 6. Squeeze, entanglement, Cayley coordinate, and Fisher distance

Write

[
r=	anhkappa.
]

The radial Fisher distance from the uniform state (r=0) is

[
D_F(r)
=
int_0^rrac{sqrt2,du}{1-u^2}
=
oxed{sqrt2,kappa}.
]

For the prime state,

[
kappa_p=operatorname{artanh}(p^{-1/2}).
]

The pure two-mode logarithmic negativity is

[
E_{N,p}=2kappa_p,
]

hence

[
oxed{
E_{N,p}
=
sqrt2,D_{F,p}.
}
]

The finite-place Cayley coordinate

[
q_p
=
rac{1-r_p}{1+r_p}
]

therefore satisfies

[
oxed{
q_p
=
e^{-2kappa_p}
=
e^{-sqrt2 D_{F,p}}
=
e^{-E_{N,p}}.
}
]

So the Cayley contraction is exactly the exponential of minus the entanglement distance, and the Fisher radial distance is the same hyperbolic coordinate up to a universal factor.

## 7. Mass is a hyperbolic information-distance coordinate

The finite-place mass coordinate is

[
mu_p
=
2sinhkappa_p
=
rac{2}{sqrt{p-1}}.
]

Using (D_F=sqrt2kappa),

[
oxed{
mu
=
2sinh!left(rac{D_F}{sqrt2}ight).
}
]

Equivalently,

[
oxed{
mu^2
=
4sinh^2!left(rac{D_F}{sqrt2}ight).
}
]

Thus, within the finite-place model, mass-square is an exact monotone function of Fisher distance from the unentangled/uniform phase state.

The reduced purity becomes

[
oxed{
operatorname{Tr}ho_p^2
=
operatorname{sech}(2kappa_p)
=
operatorname{sech}(sqrt2 D_{F,p}).
}
]

The vacuum fidelity is

[
F_{0,p}
=
|langle0,0|Omega_pangle|^2
=
1-rac1p,
]

and

[
oxed{
rac{mu_p^2}{4}
=
rac{1-F_{0,p}}{F_{0,p}}.
}
]

So the occupation/mass coordinate is also the odds ratio against the TFD vacuum fidelity.

## 8. Schur elimination produces a mass resolvent

The completed two-mode covariance is

[
Gamma_p
=
egin{pmatrix}
C_p+rac12&A_p\
A_p&C_p+rac12
end{pmatrix},
]

with

[
C_p=rac{mu_p^2}{4},
qquad
A_p^2=C_p(1+C_p),
qquad
detGamma_p=rac14.
]

Eliminating one sheet gives

[
S_p
=
C_p+rac12
-
rac{A_p^2}{C_p+1/2}.
]

Using the pure-state identity,

[
oxed{
S_p
=
rac{1}{mu_p^2+2}.
}
]

But the earlier edge calculation also gave

[
S_p
=
rac12operatorname{Tr}ho_p^2.
]

Hence

[
oxed{
rac{1}{mu_p^2+2}
=
rac12operatorname{Tr}ho_p^2.
}
]

This is a literal Stieltjes/resolvent-shaped response generated by integrating out one member of the local doubled state.

## 9. Interpretation and next target

The exact local dictionary is now

[
oxed{
egin{array}{c}
	ext{prime }p\
downarrow\
r_p=p^{-1/2}\
downarrow\
	ext{TFD phase density }f_p=mathcal P_{r_p}/(2pi)\
downarrow\
D_{F,p}=sqrt2,operatorname{artanh}r_p\
downarrow\
E_{N,p}=sqrt2D_{F,p}\
downarrow\
mu_p=2sinh(D_{F,p}/sqrt2).
end{array}
}
]

Meanwhile the von Mangoldt current is the energy-weighted centered phase intensity of these same states.

This supplies a concrete information-geometric meaning for the finite-place mass coordinate, but it does not identify these dimensionless arithmetic masses with Standard Model particle masses.

The next global target is to determine whether the completed Archimedean sewing can be written as a relative Fisher/phase-POVM frame operator whose Schur complement is the already exact RH Weyl function (m_*(u)). If so, the missing positivity problem would become a global frame/conditional-covariance theorem rather than an abstract sign inequality.
