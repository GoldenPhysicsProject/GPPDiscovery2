# Prime de Branges defect as a TFD-dressed causal delay line

Date: 2026-09-27
Status: corrected exact local Hilbert-space factorization. No RH proof.

> Correction: the first version of this note used an additive composition formula for the Blaschke defect. That was wrong. The correct defect of a composition is multiplicative in the rank-one Blaschke dressing. The diagonal/group-delay conclusions survive; the feature map is corrected below.

## 1. The logarithmic prime length is an inner delay

Fix a prime p and write

[
L_p=log p,qquad a_p=p^{-1/2}.
]

The exponential

[
phi_p(z)=e^{iL_p z}
]

maps the upper half-plane into the unit disk. Its Schur/de Branges defect is

[
D_{phi_p}(z,w)
=
rac{1-phi_p(z)overline{phi_p(w)}}{-i(z-ar w)}
=
int_0^{L_p}e^{itz}overline{e^{itw}},dt.
]

Thus the bare prime is a causal delay line with Hilbert space (L^2([0,L_p])).

## 2. Exact Blaschke dressing identity

Let

[
B_a(zeta)=rac{zeta-a}{1-azeta},qquad
f_a(zeta)=rac{sqrt{1-a^2}}{1-azeta}.
]

Direct algebra gives

[
oxed{
rac{1-B_a(zeta)overline{B_a(eta)}}{1-zetaareta}
=
f_a(zeta)overline{f_a(eta)}.
}
]

For

[
Theta_p^{m in}(z)
=
B_{a_p}(phi_p(z)),
]

the correct upper-half-plane defect therefore is

[
oxed{
D_{Theta_p^{m in}}(z,w)
=
f_{a_p}(phi_p(z))
overline{f_{a_p}(phi_p(w))}
D_{phi_p}(z,w).
}
]

Using the delay-line Gram representation,

[
oxed{
D_{Theta_p^{m in}}(z,w)
=
int_0^{L_p}
F_{p,t}(z)overline{F_{p,t}(w)},dt,
}
]

with the corrected feature map

[
oxed{
F_{p,t}(z)
=
rac{sqrt{1-p^{-1}}}
{1-p^{-1/2}e^{iL_pz}}
,e^{itz}.
}
]

So the TFD factor **multiplicatively dresses every point of the causal delay line**. It is not an extra additive rank-one channel.

## 3. Diagonal = positive group delay

For real x,

[
|f_a(e^{i	heta})|^2
=
rac{1-a^2}{1-2acos	heta+a^2}
=:mathcal P_a(	heta).
]

Hence

[
oxed{
D_{Theta_p^{m in}}(x,x)
=
L_pmathcal P_{a_p}(L_px)
=
rac{d}{dx}argTheta_p^{m in}(x).
}
]

Thus the de Branges defect density, TFD Poisson kernel, and Wigner--Smith group delay are the same positive local object.

## 4. Free-delay subtraction gives the von Mangoldt half-density current

The bare delay has

[
D_{phi_p}(x,x)=L_p.
]

Therefore

[
D_{Theta_p^{m in}}(x,x)-D_{phi_p}(x,x)
=
L_pigl[mathcal P_{a_p}(L_px)-1igr].
]

Since

[
mathcal P_a(	heta)-1
=
2sum_{mge1}a^mcos(m	heta),
]

we get

[
oxed{
rac12
left(
D_{Theta_p^{m in}}(x,x)-D_{phi_p}(x,x)
ight)
=
sum_{mge1}
rac{Lambda(p^m)}{sqrt{p^m}}
cos(xlog p^m).
}
]

This exact diagonal identity was unaffected by the correction.

## 5. The relative ghost is the multiplicative dressing minus the identity

Off diagonal, define

[
R_p(z,w)
=
D_{Theta_p^{m in}}(z,w)-D_{phi_p}(z,w).
]

The corrected factorization is

[
oxed{
R_p(z,w)
=
left[
f_{a_p}(phi_p(z))
overline{f_{a_p}(phi_p(w))}
-1
ight]
D_{phi_p}(z,w).
}
]

Thus both the dressed and bare delay kernels are positive, while their relative/background-subtracted kernel need not be positive.

This is the exact scattering analogue of normal ordering:
the full TFD covariance is positive, but subtracting the vacuum/background creates the indefinite relative form required by the explicit formula.

## 6. Finite cascades are positive before relative subtraction

For inner functions (Theta_1,Theta_2),

[
oxed{
D_{Theta_1Theta_2}
=
D_{Theta_1}
+
Theta_1(z)overline{Theta_1(w)}
D_{Theta_2}.
}
]

Iterating over a finite ordered prime set gives a positive sum of transported dressed delay-line Gram kernels.

Therefore no local prime channel is the source of the RH sign problem. The sign appears only after the free/background system is quotiented and the infinite prime system is sewn to the real place.

## 7. Corrected global target

The prime Hilbert spaces are explicit:

[
L^2([0,log p],dt),
]

and the correct local feature map is

[
F_{p,t}(z)
=
f_{p^{-1/2}}(e^{i(log p)z})e^{itz}.
]

The missing theorem is to construct the renormalized infinite prime--Archimedean quotient such that the completed relative defect becomes positive on the physical analytic subspace.

Equivalently: lift the already exact scalar adelic functional equation to a positive operator-valued sewing of these multiplicatively dressed causal delay lines.

That remains the global RH step.
