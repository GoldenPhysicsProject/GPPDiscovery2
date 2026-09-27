# Universal SU(1,1) character behind prime covariance and celestial Plancherel weight

Date: 2026-09-27
Status: exact representation-algebra identities. The proposed finite-to-Archimedean intertwiner remains open.

## 1. The paired oscillator carries the lowest-weight k=1/2 representation

On the equal-occupation subspace

[
mathcal K_{m pair}
=
overline{mathrm{span}}{|n,nangle:nge0},
]

define

[
K_+=a_+^dagger a_-^dagger,
qquad
K_-=a_+a_-,
qquad
K_0=rac12(N_++N_-+1).
]

Then

[
K_0|n,nangle
=
left(n+rac12ight)|n,nangle.
]

The lowest weight is therefore

[
oxed{k=rac12.}
]

The quadratic SU(1,1) Casimir has value

[
oxed{
mathcal C=k(k-1)=-rac14.
}
]

## 2. Exact match to the half-density conformal Casimir threshold

The one-dimensional conformal/principal-series weight is

[
s=rac12+i	au.
]

Its conventional quadratic Casimir is

[
s(s-1)
=
-left(rac14+	au^2ight).
]

At the center (	au=0),

[
oxed{
s(s-1)=-rac14,
}
]

exactly the same Casimir value as the paired-oscillator (k=1/2) SU(1,1) representation.

This equality of Casimir values is exact. It does not make the lowest-weight discrete representation and the principal series equivalent representations; they are not being identified here.

The useful fact is that the paired arithmetic TFD sector sits exactly at the (-1/4) threshold from which the principal-series Casimir continues as

[
-rac14-	au^2.
]

## 3. One universal character

For (ell>0), the compact-generator heat character is

[
chi_{1/2}(ell)
:=
operatorname{Tr}_{mathcal K_{m pair}}
e^{-2ell K_0}.
]

Using the spectrum (n+1/2),

[
chi_{1/2}(ell)
=
sum_{nge0}
e^{-2ell(n+1/2)}
=
oxed{
rac1{2sinhell}.
}
]

But this is exactly the universal anomalous TFD covariance

[
A(ell)=rac1{2sinhell}.
]

Therefore

[
oxed{
A(ell)
=
chi_{1/2}(ell).
}
]

The anomalous covariance is literally the (k=1/2) SU(1,1) heat character.

## 4. Finite prime channel

For prime (p),

[
ell_p=rac12log p.
]

Then

[
oxed{
A_p
=
chi_{1/2}(ell_p)
=
rac1{2sinhell_p}
=
rac{sqrt p}{p-1}.
}
]

The normal covariance is

[
C_p
=
e^{-ell_p}chi_{1/2}(ell_p)
=
rac1{p-1}.
]

Thus the two local covariance channels are one universal SU(1,1) character and its half-density tilt.

## 5. Archimedean celestial channel

Set

[
ell_infty=pilambda.
]

The celestial principal-series spectral weight is

[
P(lambda)
=
rac{pilambda}{sinh(pilambda)}.
]

Hence

[
oxed{
P(lambda)
=
2ell_infty,
chi_{1/2}(ell_infty).
}
]

So the Archimedean Plancherel weight and the finite-prime anomalous covariance are evaluations of the same (k=1/2) character:

[
oxed{
	ext{finite place: }chi_{1/2}(ell_p),
qquad
	ext{real place: }2ell_inftychi_{1/2}(ell_infty).
}
]

The extra factor (2ell_infty) is the modular-energy/density factor already present in the celestial transfer measure.

## 6. Euler factor as a shifted character

For arbitrary complex (s) in the local convergence region,

[
operatorname{Tr}
e^{-sL_pK_0}
=
sum_{nge0}
p^{-s(n+1/2)}
=
p^{-s/2}zeta_p(s).
]

Therefore

[
oxed{
zeta_p(s)
=
p^{s/2}
operatorname{Tr}
e^{-sL_pK_0}.
}
]

The local Euler factor is a zero-point-shifted heat character of the same paired oscillator representation.

At the critical half-density this zero-point factor is exactly the square-root Gibbs amplitude.

## 7. Why the half-integer oscillator in the celestial weight is not accidental

The exact identity

[
P(lambda)
=
2pilambda
sum_{nge0}
e^{-2pilambda(n+1/2)}
]

is now read as

[
oxed{
P(lambda)
=
2pilambda,
operatorname{Tr}
e^{-2pilambda K_0}
}
]

on the same (k=1/2) paired Hilbert space.

Thus:
- the finite arithmetic TFD uses the (K_0) occupation basis;
- the celestial real-place weight uses the heat character of that same universal spectrum;
- the conformal critical center shares its Casimir value (-1/4).

This is a stronger common representation-theoretic core than the earlier observation that both formulas contain (sinh).

## 8. Potential finite-to-real intertwiner

The same SU(1,1) algebra also contains noncompact self-adjoint generators such as

[
K_1=rac12(K_++K_-),
qquad
K_2=rac1{2i}(K_+-K_-).
]

Their spectral decompositions are continuous even though (K_0) has the discrete spectrum (n+1/2).

This suggests a concrete new target:

construct the Archimedean principal-series transform as the noncompact-generator spectral transform of the universal paired (k=1/2) module, while the finite primes enter through discrete modular evolution lengths

[
L_p=log p.
]

If this can be made exact, the discrete occupation/prime picture and the continuous Archimedean principal-series picture would be two spectral decompositions of one SU(1,1)-based local parent structure.

This is a target, not a proved identification. In particular, equality of the Casimir threshold alone does not establish representation equivalence or RH.
