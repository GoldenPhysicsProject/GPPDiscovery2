# Local SU(1,1) closure of the prime TFD, Euler factor, Blaschke channel, and mass coordinate

Date: 2026-09-27
Status: exact local representation-theoretic package plus a global adelic target. No external literature search used.

## 1. Two-mode arithmetic TFD is an SU(1,1) coherent state

For one prime introduce two oscillator copies with

[
K_+=a_+^dagger a_-^dagger,qquad
K_-=a_+a_-,
qquad
K_0=rac12(N_++N_-+1).
]

They satisfy

[
[K_0,K_pm]=pm K_pm,
qquad
[K_+,K_-]=-2K_0.
]

Thus the doubled oscillator carries an (mathfrak{su}(1,1)) representation.

For any (zinmathbb D),

[
|zangle
=
sqrt{1-|z|^2}
sum_{mge0}z^m|m,mangle
]

is the normalized coherent-state orbit of the doubled vacuum.

For the critical prime state,

[
oxed{
z_p=p^{-1/2}.
}
]

More generally, for Gibbs inverse temperature (eta),

[
z_{p,eta}=p^{-eta/2}.
]

## 2. Mellin/modular time is angular motion on the disk

Let

[
L_p=log p.
]

The doubled modular generator is

[
mathcal L_p
=
L_p(N_+-N_-),
]

and the one-sided phase evolution of the coherent coordinate is

[
z_p(t)
=
p^{-1/2}e^{-itL_p}
=
oxed{p^{-1/2-it}}.
]

Thus on the critical line

[
s=rac12+it,
]

the local Euler variable is literally the moving SU(1,1)-disk coordinate

[
oxed{
z_p(t)=p^{-s}.
}
]

For general (s=sigma+it), the radius is (p^{-sigma}) and the angle is (-tlog p).

So:
- (Re s) is a radial coordinate;
- (Im s) is modular angular time.

## 3. The local Euler factor is the boundary phase wavefunction

On the paired subspace define the phase vector

[
|	hetaangle
=
sum_{mge0}e^{-im	heta}|m,mangle.
]

Then

[
langle	heta|zangle
=
rac{sqrt{1-|z|^2}}
{1-ze^{i	heta}}.
]

Choose (z=p^{-sigma}) and (	heta=-tL_p) according to phase convention. Then

[
oxed{
zeta_p(sigma+it)
=
rac1{1-p^{-sigma-it}}
=
rac{
langle	heta_p(t)|Omega_{p,2sigma}angle
}{
sqrt{1-p^{-2sigma}}
}.
}
]

Therefore

[
oxed{
(1-p^{-2sigma})
|zeta_p(sigma+it)|^2
=
mathcal P_{p^{-sigma}}(tlog p),
}
]

where (mathcal P_r) is the Poisson kernel.

The local Euler factor is thus an unnormalized boundary phase amplitude of the local arithmetic TFD coherent state.

## 4. The Blaschke transfer is the hyperbolic translation to vacuum

Let

[
a_p=p^{-1/2}.
]

The exact local transfer function already used in the arithmetic scattering construction is

[
mathcal T_p(w)
=
rac{w-a_p}{1-a_pw}.
]

This is the real-axis SU(1,1) disk automorphism that sends

[
oxed{a_pmapsto0.}
]

So the same number (a_p) is simultaneously:
- the critical TFD coherent-state radius;
- the local Euler half-density amplitude;
- the fixed interior point removed by the Blaschke scattering channel.

The local scattering colligation is therefore the hyperbolic translation that moves the prime coherent state to the vacuum origin.

## 5. Group delay is the boundary Jacobian of that hyperbolic translation

On (|w|=1),

[
rac{d}{d	heta}
arg mathcal T_p(e^{i	heta})
=
rac{1-a_p^2}
{1-2a_pcos	heta+a_p^2}
=
oxed{mathcal P_{a_p}(	heta)}.
]

This is exactly:
- the Blaschke boundary Jacobian;
- the local group-delay kernel;
- the canonical phase probability density of the TFD coherent state, up to (2pi).

Thus the earlier scattering and TFD constructions are not merely analogous. They are the same SU(1,1) disk geometry viewed from the interior state and boundary transfer pictures.

## 6. Hyperbolic distance, Cayley coordinate, entanglement, and mass

Write

[
a=	anhkappa.
]

The standard Poincare distance from (0) to (a) is

[
d_H=2operatorname{artanh}a=2kappa.
]

For the prime state,

[
oxed{
d_{H,p}
=
2kappa_p
=
E_{N,p},
}
]

the pure two-mode logarithmic negativity.

The Cayley coordinate is

[
q_p
=
rac{1-a_p}{1+a_p}
=
e^{-2kappa_p},
]

hence

[
oxed{
q_p=e^{-d_{H,p}}=e^{-E_{N,p}}.
}
]

The finite-place mass coordinate is

[
mu_p=2sinhkappa_p,
]

so

[
oxed{
mu_p
=
2sinhrac{d_{H,p}}2.
}
]

Thus mass, entanglement, Cayley contraction, and hyperbolic translation length are exact functions of one SU(1,1) invariant radial coordinate.

The Fisher metric of the phase distributions is one half of the Poincare metric, so

[
d_H=sqrt2,D_F.
]

Therefore

[
oxed{
mu
=
2sinh(D_F/sqrt2),
qquad
E_N=sqrt2D_F.
}
]

## 7. Shadow becomes reciprocal radial reflection

For

[
s=sigma+it,
qquad
z_p(s)=p^{-s},
]

the arithmetic shadow is

[
smapsto1-ar s.
]

It acts on the disk coordinate as

[
oxed{
z_p
mapsto
rac{1}{p,overline{z_p}}.
}
]

The fixed circle is

[
|z_p|=p^{-1/2},
]

which is exactly the critical TFD radius.

Rescale to

[
w_p
=
sqrt p,z_p
=
p^{1/2-s}.
]

Then shadow becomes

[
oxed{
w_pmapstorac1{overline{w_p}},
}
]

and the critical line becomes

[
oxed{|w_p|=1.}
]

Thus the local principal/critical condition is literally the unit-circle fixed locus of reciprocal conjugation in the rescaled SU(1,1) transfer coordinate.

This is a local symmetry statement only; it does not prove that every global zeta zero must occupy the fixed locus.

## 8. Finite product intensity

For (sigma>1), where the Euler product converges absolutely,

[
prod_p
(1-p^{-2sigma})
|zeta_p(sigma+it)|^2
=
prod_p
mathcal P_{p^{-sigma}}(tlog p).
]

Since

[
prod_p(1-p^{-2sigma})
=
rac1{zeta(2sigma)},
]

we obtain

[
oxed{
rac{|zeta(sigma+it)|^2}{zeta(2sigma)}
=
prod_p
mathcal P_{p^{-sigma}}(tlog p),
qquad
sigma>1.
}
]

So in the Euler half-plane the normalized zeta intensity is literally the product of the local SU(1,1)/TFD phase intensities.

The formula is not asserted as an Euler product in the critical strip, where absolute convergence fails.

## 9. Representation-theoretic global target

The local finite-place structure has now collapsed to one SU(1,1) object:

[
oxed{
egin{array}{c}
	ext{interior coherent state }z_p\
Updownarrow\
	ext{TFD entanglement covariance}\
Updownarrow\
	ext{Blaschke disk automorphism}\
Updownarrow\
	ext{boundary Poisson/group-delay kernel}\
Updownarrow\
	ext{Euler prime-power coefficients}.
end{array}
}
]

The Archimedean side already carries the principal-series Plancherel weight on the boundary.

This suggests a sharper adelic sewing target: construct an explicit intertwiner from the direct sum/product of finite-place SU(1,1) coherent-state channels to the Archimedean principal-series boundary representation, with the rational/functional-equation quotient providing the shadow identification.

If that intertwiner makes the completed Weil form a positive boundary norm, RH follows through the already established Stieltjes/heat criterion. The intertwiner itself remains unconstructed.
