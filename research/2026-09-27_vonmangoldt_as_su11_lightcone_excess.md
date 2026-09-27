# Von Mangoldt current as excess SU(1,1) lightcone momentum

Date: 2026-09-27
Status: exact local SU(1,1) identities and an exact Euler-logarithmic-derivative identity for real s>1. Complex continuation is a holomorphic symbol, not a Hermitian expectation. No RH proof.

## 1. Coherent-state hyperboloid

In the k=1/2 SU(1,1) module use the real coherent state
[
|Omega_rangle
=
sqrt{1-r^2}sum_{nge0}r^n e_n,
qquad 0<r<1.
]

With
[
K_0e_n=left(n+rac12ight)e_n,
]
and the noncompact generator K1 used in the Jacobi transform, the exact expectations are
[
langle K_0angle_r
=
rac{1+r^2}{2(1-r^2)},
]
[
langle K_1angle_r
=
rac{r}{1-r^2}.
]

Write
[
r=	anhkappa.
]

Then
[
oxed{
2langle K_0angle_r=cosh2kappa,
qquad
2langle K_1angle_r=sinh2kappa.
}
]

Thus the coherent orbit lies on the unit future hyperbola
[
oxed{
(2langle K_0angle)^2-(2langle K_1angle)^2=1.
}
]

## 2. Null/lightcone coordinates

Define
[
X_pm
=
2langle K_0pm K_1angle_r.
]

Then
[
oxed{
X_+
=
rac{1+r}{1-r}
=
e^{2kappa},
}
]
and
[
oxed{
X_-
=
rac{1-r}{1+r}
=
e^{-2kappa}.
}
]

Therefore
[
oxed{X_+X_-=1.}
]

These are the two lightcone coordinates of the SU(1,1) coherent-state hyperboloid.

They are also exactly the antipodal Poisson intensities:
[
oxed{
X_+=mathcal P_r(0),
qquad
X_-=mathcal P_r(pi).
}
]

The Cayley coordinate is therefore
[
oxed{
q(r)=X_-=e^{-2kappa},
}
]
while
[
X_+=q^{-1}.
]

## 3. The Euler geometric series is the forward-null excess above vacuum

The vacuum r=0 has
[
langle K_0+K_1angle_0=rac12.
]

For general r,
[
egin{aligned}
langle K_0+K_1angle_r-rac12
&=
rac12left(rac{1+r}{1-r}-1ight)\
&=
oxed{
rac{r}{1-r}
}\
&=
sum_{mge1}r^m.
end{aligned}
]

Hence the complete local repetition tower is one lightcone expectation:
[
oxed{
sum_{mge1}r^m
=
langle K_0+K_1angle_r-rac12.
}
]

Likewise
[
rac12-langle K_0-K_1angle_r
=
oxed{
rac{r}{1+r}
}
=
r-r^2+r^3-r^4+cdots.
]

## 4. Odd/even TFD covariances are lightcone combinations

Let
[
A(r)=rac{r}{1-r^2},
qquad
C(r)=rac{r^2}{1-r^2}.
]

Define the forward excess and backward deficit
[
N_+(r)=rac{r}{1-r},
qquad
N_-(r)=rac{r}{1+r}.
]

Then
[
oxed{
A(r)=rac{N_+(r)+N_-(r)}2,
}
]
and
[
oxed{
C(r)=rac{N_+(r)-N_-(r)}2.
}
]

So:
- anomalous/odd covariance is the symmetric lightcone combination;
- normal/even covariance is the antisymmetric lightcone combination;
- their sum A+C is the full positive Euler return tower.

This unifies the parity and null-coordinate descriptions.

## 5. Exact logarithmic derivative of zeta

For real s>1 set
[
r_p=p^{-s},
qquad
L_p=log p.
]

Then
[
-rac{zeta'(s)}{zeta(s)}
=
sum_p L_prac{p^{-s}}{1-p^{-s}}.
]

Using the lightcone identity,
[
oxed{
-rac{zeta'(s)}{zeta(s)}
=
sum_p
L_p
left(
langle K_0+K_1angle_{r_p}
-rac12
ight).
}
]

Thus the von-Mangoldt current is exactly the total modular-energy-weighted **forward-null excess** of the prime SU(1,1) coherent channels.

Expanding the expectation gives
[
L_p
left(
langle K_0+K_1angle_{r_p}
-rac12
ight)
=
sum_{mge1}(log p)p^{-ms},
]
hence the coefficient of p^m is Lambda(p^m)=log p.

For complex s the same formula remains as the holomorphic scalar symbol
[
rac{z}{1-z},
qquad z=p^{-s},
]
but it should not be called an expectation of a Hermitian operator unless z is real.

## 6. Prime critical geometry

At the critical real half-density,
[
r_p=p^{-1/2}=	anhkappa_p.
]

Then
[
X_{-,p}
=
oxed{
rac{sqrt p-1}{sqrt p+1}
}
=q_p,
]
and
[
X_{+,p}
=
q_p^{-1}.
]

The finite mass coordinate is
[
mu_p=2sinhkappa_p.
]

Therefore
[
oxed{
mu_p^2
=
2(cosh2kappa_p-1)
=
X_{+,p}+X_{-,p}-2
=
rac{(1-q_p)^2}{q_p}.
}
]

So the finite-place mass coordinate is the hyperbolic displacement away from the vacuum point X_+=X_-=1.

## 7. Structural connection to the orientation/horizon program

The pair
[
K_0+K_1,qquad K_0-K_1
]
are the two null directions of the SU(1,1) adjoint Lorentzian geometry.

This supplies a mathematically precise two-arrow structure inside the arithmetic TFD module:
[
oxed{
	ext{paired state}
leftrightarrow
	ext{two null SU(1,1) directions}
leftrightarrow
	ext{boost rapidity }2kappa.
}
]

The arithmetic mass coordinate measures the boost/hyperbolic displacement between these null coordinates.

This is structurally compatible with the separate particle/horizon orientation-double program, where mass is a coupling of two opposite proper-time orientations and a null boundary exchanges them. No physical identification of the two constructions is proved here.

## 8. New global target

The prime part of the completed logarithmic derivative is now not merely a sum of positive local occupations. It is a sum of positive local **null excesses**.

The real-place completion should therefore be tested as a continuum null-momentum background for the same SU(1,1) module.

Combined with the one-ghost reduction
[
dpsi-dy,
]
this suggests a sharper global question:

Can the completed prime-versus-continuum discrepancy be realized as a relative lightcone-momentum operator in one doubled SU(1,1) standard form, with the Archimedean K0/K1 polarizations supplying the vacuum completion?

If yes, the remaining RH positivity would become a no-negative-relative-null-energy theorem. That theorem is not established here.
