# The det3 threshold is the first-three-mode tail of the universal SU(1,1) coherent state

Date: 2026-09-27
Status: exact local and global convergence identities. No RH proof.

## 1. Universal compact/noncompact transform

Use the k=1/2 SU(1,1) module K=l2(N0), with compact basis e_n and noncompact spectral transform U.

For the normalized coherent state
[
Omega_r=sqrt{1-r^2}sum_{nge0}r^n e_n,qquad 0<r<1,
]
the K1 spectral image is
[
UOmega_r(x)
=
sqrt{1-r^2}sum_{nge0}r^nP_n(x)
=
sqrt{cos(2alpha)}e^{2alpha x},
qquad r=	analpha,
]
in
[
L^2(mathbb R,operatorname{sech}(pi x),dx).
]

The first compact modes are
[
P_0(x)=1,
qquad
P_1(x)=2x,
qquad
P_2(x)=2x^2-rac12.
]
They are orthonormal for the hyperbolic-secant vacuum measure.

## 2. Exact tail norm theorem

Let
[
Pi_{<m}=sum_{n=0}^{m-1}|e_nanglelangle e_n|.
]

Because the compact basis is orthonormal,
[
egin{aligned}
|(I-Pi_{<m})Omega_r|^2
&=
(1-r^2)sum_{nge m}r^{2n}\
&=r^{2m}.
end{aligned}
]

Therefore
[
oxed{
|(I-Pi_{<m})Omega_r|=r^m.
}
]

The same identity holds after the K1 transform:
[
oxed{
left|
UOmega_r
-sqrt{1-r^2}sum_{n=0}^{m-1}r^nP_n
ight|_{L^2(operatorname{sech}pi x,dx)}
=r^m.
}
]

This is an exact remainder formula, not an asymptotic expansion.

## 3. Prime family and the Schatten threshold

At real part sigma, use
[
r_{p,sigma}=p^{-sigma}.
]

Then
[
sum_p
|(I-Pi_{<m})Omega_{p,sigma}|
=
sum_p p^{-msigma}
=
P(msigma),
]
where P is the prime zeta function.

Hence
[
oxed{
sum_p
|(I-Pi_{<m})Omega_{p,sigma}|<infty
iff
msigma>1.
}
]

But the diagonal Euler operator
[
D(s)e_p=p^{-s}e_p
]
satisfies
[
D(s)inmathfrak S_m
iff
mRe s>1.
]

Therefore
[
oxed{
D(s)inmathfrak S_m
iff
	ext{the prime SU(1,1) coherent tails after removing modes }0,ldots,m-1
	ext{ are absolutely summable}.
}
]

This gives a representation-theoretic meaning to the regularized determinant order.

## 4. Why det2 fails and det3 succeeds at the critical boundary

At
[
sigma=rac12,
qquad r_p=p^{-1/2},
]
removing only the vacuum and first mode leaves
[
|(I-Pi_{<2})Omega_p|
=r_p^2
=rac1p.
]

Thus
[
sum_p|(I-Pi_{<2})Omega_p|
=
sum_prac1p
=
infty.
]

This is the coherent-state version of
[
D(1/2+it)
otinmathfrak S_2.
]

But removing the vacuum and the first two nonvacuum modes gives
[
|(I-Pi_{<3})Omega_p|
=
r_p^3
=
p^{-3/2},
]
so
[
oxed{
sum_p|(I-Pi_{<3})Omega_p|
=
P(3/2)<infty.
}
]

This is exactly the coherent-state version of
[
oxed{
D(1/2+it)inmathfrak S_3.
}
]

Thus the critical determinant threshold m=3 is not an abstract trace-ideal accident. It is the minimal compact-mode subtraction that makes the universal prime coherent-state tails absolutely summable.

## 5. The two RH boundary channels are the first two nonvacuum K0 modes

The Euler det3 identity isolates precisely the repetition terms m=1 and m=2.

The coherent-state tail theorem identifies the same obstruction as the first two compact excitations
[
oxed{
e_1,qquad e_2.
}
]

Under the exact prime-to-Archimedean Jacobi transform these become the explicit orthonormal functions
[
oxed{
P_1(x)=2x,
qquad
P_2(x)=2x^2-rac12.
}
]

So the previously abstract two-channel Archimedean completion can be sharpened:

[
oxed{
	ext{renormalize/sew only the }P_1	ext{ and }P_2	ext{ sectors of the universal }K_1	ext{ spectral line;}
}
]

the tail orthogonal to
[
operatorname{span}{P_0,P_1,P_2}
]
is already absolutely summable across primes at the critical boundary.

## 6. Jet interpretation

The exact spectral wavefunction is
[
f_alpha(x)
=
sqrt{cos2alpha},e^{2alpha x}.
]

At the vacuum alpha=0,
[
f_0=P_0,
]
[
f'_0=P_1=2x,
]
and
[
rac12f''_0
=
2x^2-1
=
P_2-rac12P_0.
]

Thus:
- the primitive m=1 obstruction is the tangent direction of the SU(1,1) coherent orbit at the vacuum;
- the m=2 obstruction is its quadratic curvature/normalization jet;
- m>=3 is the trace-controlled nonlinear tail.

This matches the earlier Gaussian-cumulant interpretation: the first two divergent Euler cumulants are the first two jets of the same coherent-state manifold.

## 7. Concrete next target

The real place is already represented by the same k=1/2 SU(1,1) module:
- K0 gives the positive Gamma/digamma resolvent tower;
- K1 gives the celestial Plancherel spectral measure.

Therefore the unresolved global sewing should be tested as a finite-rank completion on the explicit low-mode space
[
mathcal E_{m bdry}
=
operatorname{span}{P_1,P_2}
]
coupled to the already convergent m>=3 tail.

A successful construction would replace the vague phrase "two-channel completion" by an explicit 2x2 Archimedean counterterm/Schur block in the universal SU(1,1) representation.

This note does not prove that such a 2x2 completion is positive or has the correct xi Weyl function. It proves that no additional local repetition modes need independent renormalization at the critical boundary.
