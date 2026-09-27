# Prime TFD = local Euler Blaschke scattering, and exact adelic phase sewing

Date: 2026-09-27
Status: exact local algebra and exact meromorphic global ratio identity. This does not prove RH. The gain is that the TFD/Blaschke channel and the previously derived local Euler functional-equation transfer are literally the same object.

## 1. One local variable

For a prime p define

L_p = log p,
a_p = p^(-1/2),

and the centered multiplicative spectral coordinate

z_p(s) = p^(1/2-s).

Then the arithmetic shadow reflection satisfies

z_p(1-s) = z_p(s)^(-1).

On the critical line Re(s)=1/2,

|z_p(s)|=1.

Thus the critical line is exactly the unit circle in every local multiplicative coordinate.

## 2. The local Euler transfer is exactly a Blaschke automorphism

Let

B_a(z) = (z-a)/(1-a z).

Using

p^(-s) = a_p z_p(s),
p^(s-1) = a_p / z_p(s),

we get

z_p(s) zeta_p(s)/zeta_p(1-s)
=
z_p(s) (1-p^(s-1))/(1-p^(-s))
=
(z_p(s)-a_p)/(1-a_p z_p(s)).

Therefore

[
oxed{
p^{1/2-s}rac{zeta_p(s)}{zeta_p(1-s)}
=
B_{p^{-1/2}}!left(p^{1/2-s}ight).
}
]

This is exactly the local transfer function already isolated in the arithmetic principal-series program.

So the local functional-equation scattering channel is not merely analogous to the prime TFD/Blaschke mode: it is the same disk automorphism.

## 3. TFD Schmidt ratio = Blaschke zero

The critical prime TFD state is

|Omega_p> = sqrt(1-a_p^2) sum_{n>=0} a_p^n |n,n>,

with

a_p = p^(-1/2).

The same number a_p is the zero of the local transfer B_{a_p}.

Hence

[
oxed{
	ext{TFD Schmidt ratio}
=
	ext{local scattering zero in disk coordinates}.
}
]

Equivalently, the modular squeeze parameter

a_p = tanh(kappa_p)

is the SU(1,1) parameter of the local Euler scattering automorphism.

## 4. Shadow reciprocity is exact local scattering reciprocity

A direct calculation gives

B_a(z^{-1}) = B_a(z)^{-1}.

Since z_p(1-s)=z_p(s)^(-1),

[
oxed{
T_p(1-s)=T_p(s)^{-1}.
}
]

On the critical line, 1-s = conjugate(s), so because the local coefficients are real,

[
oxed{
|T_p(1/2+it)|=1.
}
]

Thus each prime channel is individually a unitary SU(1,1)/Blaschke scattering factor on the critical line.

This is local boundary unitarity only; it does not constrain the global zeta zeros.

## 5. Dressed/free quotient is exactly the local Euler-factor ratio

The Blaschke transfer can be written

T_p(s)
=
z_p(s)
rac{zeta_p(s)}{zeta_p(1-s)}.

The factor z_p(s) is the bare logarithmic delay.

Therefore

[
oxed{
rac{T_p(s)}{z_p(s)}
=
rac{zeta_p(s)}{zeta_p(1-s)}.
}
]

So the relative TFD-dressed/free-delay scattering amplitude is precisely the local Euler functional-equation ratio.

This explains why subtracting the bare delay from the de Branges defect produces the von-Mangoldt current.

## 6. Relative group delay gives the prime-power current

On the critical line write

s=1/2+it,
z_p=e^{-iL_p t}.

The boundary phase derivative of B_{a_p}(z_p) is, up to orientation sign,

L_p P_{a_p}(L_p t),

where

P_a(theta)=(1-a^2)/(1-2a cos(theta)+a^2)

is the Poisson kernel.

Subtract the free delay L_p:

[
L_p(P_{a_p}(L_p t)-1)
=
2L_psum_{m>=1} a_p^m cos(mL_p t).
]

Hence

[
oxed{
rac12,	au^{rel}_p(t)
=
sum_{m>=1}
rac{Lambda(p^m)}{sqrt{p^m}}
cos(tlog p^m).
}
]

Thus the local explicit-formula current is exactly the relative Wigner-Smith/de Branges delay of the Euler-TFD scattering factor.

## 7. The finite-place mass coordinate is encoded in delay anisotropy

The extremal Poisson intensities are

P_a(0)=(1+a)/(1-a)=e^{2kappa},

P_a(pi)=(1-a)/(1+a)=e^{-2kappa}.

They satisfy

P_a(0)P_a(pi)=1.

For the prime mass coordinate

mu_p=2 sinh(kappa_p),

[
oxed{
mu_p^2
=
P_{a_p}(0)+P_{a_p}(pi)-2.
}
]

Equivalently, if tau_p(theta)=L_p P_{a_p}(theta),

[
oxed{
mu_p^2
=
rac{	au_p(0)+	au_p(pi)}{L_p}-2.
}
]

So the finite-place mass-square coordinate is exactly the hyperbolic anisotropy of the same local scattering delay whose Fourier harmonics generate the prime-power current.

Mass covariance and arithmetic scattering are therefore two observables of one local SU(1,1) channel.

## 8. Exact global meromorphic phase sewing

Formally multiplying the relative dressed/free factors gives

[
prod_p rac{T_p(s)}{z_p(s)}
=
prod_p rac{zeta_p(s)}{zeta_p(1-s)}.
]

In the common convergence region this is the Euler-product ratio, and by meromorphic continuation

[
oxed{
rac{zeta(s)}{zeta(1-s)}
=
pi^{s-1/2}
rac{Gamma((1-s)/2)}{Gamma(s/2)}.
}
]

Therefore the complete finite-place relative scattering phase is sewn exactly to the Archimedean Gamma scattering ratio.

This is an exact scalar adelic sewing identity.

It also explains why scalar scattering unitarity alone cannot prove RH: the nontrivial zeros appear as paired zero/pole data and cancel from this completed ratio through the functional equation.

## 9. Why the Hilbert-space defect remains nontrivial

At scalar determinant level the finite and Archimedean relative phases cancel into the functional equation.

At defect-kernel level, however, one retains the internal delay-line states

L^2([0,log p])

and their TFD dressing.

The RH problem therefore lives not in the scalar product of local S-matrices, which is already fixed, but in the positivity of the global compressed/relative Hilbert-space kernel after the free backgrounds are quotiented.

This sharpens the earlier warning:

[
oxed{
	ext{adelic scalar unitarity is automatic;}
qquad
	ext{global defect-kernel positivity is the RH content}.
}
]

## 10. Concrete next target

Use the exact local feature maps

F_{p,t}(z)
=
e^{itz}
rac{sqrt{1-p^{-1}}}{1-p^{-1/2}e^{iL_pz}}

and the Archimedean SU(1,1) K0/K1 realization to construct a renormalized direct-integral feature map whose Gram kernel is the completed de Branges/Weil kernel.

The scalar sewing is now known exactly. The missing theorem is to lift that scalar identity to a positive operator-valued sewing after the paired K0 trivial sector and free-delay background are removed.
