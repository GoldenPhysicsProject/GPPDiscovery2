# RH prime heat term as diffusion of TFD phase intensity

Date: 2026-09-27
Status: exact local and finite-prime identities. Global RH positivity remains open.

## 1. Circle heat kernel

Let

[
H_	au(	heta)
=
1+2sum_{mge1}e^{-m^2	au}cos(m	heta),
qquad 	au>0,
]

normalized so that

[
int_0^{2pi}H_	au(	heta),rac{d	heta}{2pi}=1.
]

This is the heat kernel on the unit circle in the convention where Fourier mode (m) decays as (e^{-m^2	au}).

For the Poisson kernel

[
mathcal P_r(	heta)
=
1+2sum_{mge1}r^mcos(m	heta),
]

normalized circular convolution gives

[
oxed{
(mathcal P_r*H_	au)(0)
=
1+2sum_{mge1}r^m e^{-m^2	au}.
}
]

## 2. Exact prime contribution to the arithmetic heat trace

For prime (p), write

[
L_p=log p,
qquad
r_p=p^{-1/2}.
]

The prime-(p) term in the completed arithmetic heat trace is

[
B_p(t)
=
sum_{mge1}
L_p r_p^m
exp!left[-rac{m^2L_p^2}{4t}ight].
]

Set

[
	au_p(t)=rac{L_p^2}{4t}.
]

Then

[
oxed{
B_p(t)
=
rac{L_p}{2}
left[
(mathcal P_{r_p}*H_{	au_p(t)})(0)-1
ight].
}
]

Because (mathcal P_{r_p}) is exactly the canonical phase intensity of the prime TFD state, the prime heat contribution is the modular energy times the excess phase intensity after circular heat diffusion.

Thus the full positive prime part is

[
oxed{
B_{m p}(t)
=
rac12
sum_pL_p
left[
(mathcal P_{r_p}*H_{L_p^2/(4t)})(0)-1
ight].
}
]

The completed RH heat trace is

[
mathscr K(t)
=
rac1{sqrt{4pi t}}
left[
B_infty(t)-B_{m p}(t)
ight],
]

where (B_infty(t)) is the already exact renormalized Archimedean term.

## 3. Brownian interpretation

Let (Theta_	au) be circle Brownian motion started at (0), with transition density (H_	au). Then

[
(mathcal P_r*H_	au)(0)
=
mathbb Eig[mathcal P_r(Theta_	au)ig].
]

Hence

[
oxed{
B_p(t)
=
rac{L_p}{2}
left(
mathbb Eig[mathcal P_{r_p}(Theta_{L_p^2/(4t)})ig]-1
ight).
}
]

The Gaussian factor in logarithmic prime-power length is therefore equivalent to phase diffusion of the local prime TFD/Blaschke channel.

This is not a metaphor: it is Fourier diagonalization of the same kernel.

## 4. Edge-length form

The TFD massive-edge half-length is

[
ell_p=rac12L_p.
]

Therefore

[
	au_p(t)=rac{ell_p^2}{t}.
]

The arithmetic heat parameter (t) and the local phase-diffusion time are reciprocal:

[
oxed{
	au_p(t)=ell_p^2/t.
}
]

At small global heat time (t), each local phase distribution is strongly diffused toward the uniform baseline and the prime term is suppressed.

At large (t), local diffusion time tends to zero and the phase measurement resolves the undiffused TFD peak.

## 5. Positivity before Archimedean subtraction

At the observation point (	heta=0),

[
(mathcal P_r*H_	au)(0)-1
=
2sum_{mge1}r^m e^{-m^2	au}>0.
]

Therefore every local (B_p(t)) is positive.

The RH problem is not local positivity. It is exactly the global domination problem

[
oxed{
B_infty(t)ge B_{m p}(t)
}
]

together with all higher complete-monotonicity/Gram conditions after the massive resolvent transform.

The diffusion representation shows that the prime side is a sum of positive local phase-excess observables. The missing theorem must therefore come from the global Archimedean/rational sewing, not from repairing any finite prime channel.

## 6. Relation to the Plancherel random-time regularizer

The existing principal-series preconditioner satisfies

[
P(x)=racpi2,mathbb E,g_S(x),
]

so the regularized RH trace averages the global heat time:

[
mathscr K_P(t)=mathbb E_S,mathscr K(t+S).
]

Combining with the prime identity above gives a nested stochastic representation:

[
oxed{
	ext{Plancherel regularization}
=
	ext{random global heat time}
quad	ext{acting on}quad
	ext{prime TFD phase diffusion}.
}
]

For each prime, the induced local diffusion time becomes

[
	au_p(t+S)
=
rac{L_p^2}{4(t+S)}.
]

Thus the celestial Plancherel measure and the arithmetic prime heat kernel act on different but explicitly linked diffusion variables.

## 7. Constructive target

The exact finite-place part of the RH heat criterion can now be realized on a direct sum of circle phase spaces:

[
mathcal H_{m phase}
=
igoplus_p L^2(S^1,d	heta/2pi),
]

with:
- local state given by the TFD Poisson density (mathcal P_{r_p}),
- modular angular velocity (L_p=log p),
- heat semigroup (e^{	aupartial_	heta^2}),
- observation functional at (	heta=0).

The next target is to realize the Archimedean term on a continuum phase/edge space in the same language and identify the completed difference as a Schur complement or conditional covariance.

If such a positive parent phase-diffusion system can be constructed independently of the zeros, the RH Gram kernel would arise as an ordinary covariance of the parent system rather than as an unexplained signed explicit-formula distribution.
