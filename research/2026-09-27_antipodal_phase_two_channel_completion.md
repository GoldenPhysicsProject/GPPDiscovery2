# Antipodal phase decomposition of the two RH boundary channels

Date: 2026-09-27
Status: exact local algebra; proposed global compression target. No external literature search used.

## 1. One positive Poisson kernel contains both covariance channels

Let

[
mathcal P_r(	heta)
=
rac{1-r^2}{1-2rcos	heta+r^2},
qquad 0<r<1.
]

At the two antipodal phase points,

[
mathcal P_r(0)=rac{1+r}{1-r},
qquad
mathcal P_r(pi)=rac{1-r}{1+r}.
]

Define the TFD normal and anomalous covariances

[
C(r)=rac{r^2}{1-r^2},
qquad
A(r)=rac{r}{1-r^2}.
]

Then

[
oxed{
A(r)
=
rac14left[
mathcal P_r(0)-mathcal P_r(pi)
ight],
}
]

and

[
oxed{
C(r)
=
rac14left[
mathcal P_r(0)+mathcal P_r(pi)-2
ight].
}
]

Thus the anomalous/pairing and normal/occupation channels are respectively the antipodal difference and the centered antipodal sum of one positive phase intensity.

## 2. Odd and even prime-power repetitions are phase parity

Using

[
mathcal P_r(	heta)
=
1+2sum_{mge1}r^mcos(m	heta),
]

we get

[
mathcal P_r(0)
=
1+2sum_{mge1}r^m,
]

while

[
mathcal P_r(pi)
=
1+2sum_{mge1}(-1)^m r^m.
]

Therefore

[
rac14igl(mathcal P_r(0)-mathcal P_r(pi)igr)
=
r+r^3+r^5+cdots
=
A(r),
]

and

[
rac14igl(mathcal P_r(0)+mathcal P_r(pi)-2igr)
=
r^2+r^4+r^6+cdots
=
C(r).
]

So the old odd/even repetition split is literally the discrete Fourier transform on the two-point phase set

[
oxed{{0,pi}.}
]

The two-channel RH boundary problem is therefore locally the (mathbb Z_2) phase decomposition of one positive Poisson/TFD channel.

## 3. TFD covariance diagonalizes in the same antipodal basis

The completed covariance is

[
Gamma(r)
=
egin{pmatrix}
C+rac12&A\
A&C+rac12
end{pmatrix}.
]

Its symmetric/antisymmetric eigenvectors are

[
v_+=rac1{sqrt2}(1,1),
qquad
v_-=rac1{sqrt2}(1,-1).
]

The corresponding eigenvalues are

[
lambda_+
=
C+rac12+A
=
oxed{rac12mathcal P_r(0)},
]

[
lambda_-
=
C+rac12-A
=
oxed{rac12mathcal P_r(pi)}.
]

Hence

[
oxed{
HGamma(r)H^*
=
rac12
egin{pmatrix}
mathcal P_r(0)&0\
0&mathcal P_r(pi)
end{pmatrix},
}
]

where (H) is the (2	imes2) Hadamard transform.

The same (mathbb Z_2) transform simultaneously:
- diagonalizes the doubled covariance;
- separates symmetric/antisymmetric sheet modes;
- separates even/odd repetition parity;
- turns the two channels into evaluations of one positive phase kernel.

## 4. The celestial Plancherel weight is the antipodal contrast

For a modular edge length (ell>0), set

[
r=e^{-ell}.
]

Then

[
A(r)
=
rac1{2sinhell}.
]

The universal energy-weighted anomalous channel is

[
2ell,A(r)
=
rac{ell}{sinhell}.
]

Using the antipodal identity,

[
oxed{
rac{ell}{sinhell}
=
rac{ell}{2}
left[
mathcal P_{e^{-ell}}(0)
-
mathcal P_{e^{-ell}}(pi)
ight].
}
]

At the Archimedean place (ell=pilambda),

[
oxed{
P(lambda)
=
rac{pilambda}{sinh(pilambda)}
=
rac{pilambda}{2}
left[
mathcal P_{e^{-pilambda}}(0)
-
mathcal P_{e^{-pilambda}}(pi)
ight].
}
]

So the celestial principal-series Plancherel weight is exactly the energy-weighted antipodal phase contrast of the same Poisson/TFD family.

For a prime, (ell_p=rac12log p), the resummed odd prime channel has the identical universal form.

## 5. Cayley coordinate and antipodal ratio

The ratio of the two phase intensities is

[
rac{mathcal P_r(pi)}{mathcal P_r(0)}
=
left(rac{1-r}{1+r}ight)^2.
]

With the finite-place Cayley coordinate

[
q(r)=rac{1-r}{1+r}=e^{-2kappa},
]

we obtain

[
oxed{
rac{mathcal P_r(pi)}
{mathcal P_r(0)}
=
q(r)^2.
}
]

Equivalently,

[
oxed{
q(r)
=
sqrt{
rac{mathcal P_r(pi)}
{mathcal P_r(0)}
}.
}
]

Thus the Cayley contraction is the square root of the antipodal phase-intensity ratio.

Since (q=e^{-E_N}) for the pure two-mode TFD state,

[
oxed{
E_N
=
rac12
lograc{mathcal P_r(0)}{mathcal P_r(pi)}.
}
]

The logarithmic negativity is therefore exactly half the log-contrast between the two antipodal phase intensities.

## 6. Relation to the horizon/orientation double

A sheet-exchange involution has the same eigenbasis

[
v_pm=(1,pm1)/sqrt2.
]

Therefore the arithmetic TFD double and the proposed horizon time-orientation double share the same exact (mathbb Z_2) decomposition:
- symmetric mode (v_+);
- antisymmetric mode (v_-).

If a horizon fixed-point condition kills an odd section, it acts on the (v_-) sector. This is structurally compatible with the earlier branch-point analysis, but no physical identification of the arithmetic prime double with a black-hole horizon is claimed here.

## 7. Sharpened global RH target

The previously isolated primitive/double-prime completion problem can now be reformulated.

Rather than constructing two unrelated boundary channels (mathcal K_1) and (mathcal K_2), seek one positive phase/TFD parent channel whose two antipodal evaluations generate the required parity sectors under the Hadamard transform.

The Archimedean Plancherel channel already has exactly this form.

Therefore the missing sewing may be constrained to preserve a universal (2	imes2) positive parent covariance while the observed explicit-formula object is a relative/centered combination of its symmetric and antisymmetric outputs.

This does not establish the global positivity required for RH. It reduces the local freedom of the two-channel completion to one positive Poisson family plus a fixed (mathbb Z_2) transform.
