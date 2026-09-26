# Math-first horizon/AFT synthesis: boost orientation, prime TFD, and boundary conversion

Date: 2026-09-26
Status: exact local identities plus explicitly marked hypotheses. No external literature search used in deriving this note.

## 0. Recovery anchor

The pre-Lean-transfer research target was:

> derive the profinite mass-square operator
> \[
> \mathsf M_f^2(X)=4M_*^2\sum_p \frac{v_p(X)}{p-1}
> \]
> from the same global adelic/celestial operator that produces the zeta scattering problem.

The critical Haar law and finite-place Casimir data are
\[
\Pr(N_p=a)=(1-p^{-1})p^{-a},\qquad
\langle N_p\rangle=\frac1{p-1},
\]
\[
\mu_p=\frac{2}{\sqrt{p-1}},\qquad
\mu_p^2=\frac4{p-1}.
\]

## 1. Exact Rindler sign structure

Work in \(1+1\) Minkowski space with \(c=1\),
\[
ds^2=-dT^2+dX^2.
\]

The boost Killing vector is
\[
K=X\partial_T+T\partial_X,
\]
with norm
\[
K^2=T^2-X^2.
\]

Hence:
- right wedge \(X>|T|\): \(K^2<0\), so \(K\) is timelike;
- horizons \(X=\pm T\): \(K^2=0\), so \(K\) is null;
- future/past wedges \(|T|>|X|\): \(K^2>0\), so \(K\) is spacelike;
- left wedge \(X<-|T|\): \(K\) is timelike again but has the opposite time orientation relative to a fixed global Minkowski time.

This is the clean mathematical core behind the statement that the exterior stationary time direction becomes null at the horizon, spacelike in the interior-type wedge, and reappears with opposite orientation in the opposite exterior.

Right-wedge coordinates
\[
T=\rho\sinh\eta,\qquad X=\rho\cosh\eta
\]
give
\[
ds^2=-\rho^2d\eta^2+d\rho^2.
\]

After Euclidean continuation \(\eta=-i\theta\),
\[
ds_E^2=d\rho^2+\rho^2d\theta^2.
\]
Smoothness at \(\rho=0\) requires
\[
\boxed{\theta\sim\theta+2\pi.}
\]

Thus the \(2\pi\) modular normalization is already encoded by regularity of the null fixed point.

## 2. Exact arithmetic-TFD / horizon-TFD match

For one prime, the critical Haar state is
\[
\rho_p=(1-p^{-1})\sum_{a\ge0}p^{-a}|a\rangle\langle a|.
\]

Its canonical purification is
\[
|\Omega_p\rangle
=
\sqrt{1-p^{-1}}\sum_{a\ge0}p^{-a/2}|a,a\rangle.
\]

A bosonic modular/Rindler TFD mode at dimensionless boost frequency \(\omega\) has the same geometric-series form with amplitude
\[
e^{-\pi\omega a}.
\]

Therefore the exact coefficient match is
\[
\boxed{
p^{-1/2}=e^{-\pi\omega_p}
}
\]
or
\[
\boxed{
\omega_p=\frac{\log p}{2\pi}.
}
\]

Equivalently,
\[
\boxed{
\log p=2\pi\omega_p.
}
\]

So the arithmetic modular energy \(\log p\) is exactly the \(2\pi\)-normalized boost/modular frequency under this dictionary.

Then
\[
\langle N_p\rangle
=
\frac1{p-1}
=
\frac1{e^{2\pi\omega_p}-1},
\]
which is exactly the Bose occupation at inverse modular temperature \(2\pi\).

Therefore
\[
\boxed{
\mu_p^2
=
4\langle N_p\rangle
=
\frac4{e^{2\pi\omega_p}-1}.
}
\]

This turns the finite-place Casimir mass-square coordinate into four times the thermal occupation of the corresponding discrete modular mode.

The other local variables become
\[
\sqrt p=e^{\pi\omega_p},
\]
\[
r_p=\frac{\sqrt p-1}{\sqrt p+1}
=\boxed{\tanh\frac{\pi\omega_p}{2}},
\]
\[
\kappa_p=\operatorname{artanh}(e^{-\pi\omega_p}),
\]
\[
\mu_p=2\sinh\kappa_p.
\]

Thus the entire finite-place hyperbolic/Cayley dictionary is expressible as ordinary modular thermal functions of the single frequency
\[
\omega_p=\frac{\log p}{2\pi}.
\]

## 3. New derivation target for the mass-square operator

For a harmonic oscillator,
\[
\langle N\rangle_\beta
=
\frac1{e^{\beta\omega}-1}.
\]

At \(\beta=2\pi\),
\[
\mu_p^2=4\langle N_p\rangle.
\]

For the normalized quadrature
\[
Q=\frac{a+a^\dagger}{\sqrt2},
\]
one has
\[
\langle Q^2\rangle_\beta=\langle N\rangle_\beta+\frac12.
\]
Hence the normal-ordered thermal excess is
\[
\langle :Q^2:\rangle_\beta=\langle N\rangle_\beta.
\]

Therefore
\[
\boxed{
\mu_p^2
=
4\langle :Q_p^2:\rangle_{\beta=2\pi}.
}
\]

This is a concrete route to deriving, rather than postulating, the profinite mass-square operator:
\[
\boxed{
\mathsf M_f^2
=
4M_*^2\sum_p N_p\,\langle :Q_p^2:\rangle_{\rm mod}
}
\]
or a closely related second-quantized covariance operator, depending on which occupation operator is being summed.

The important point is that \(1/(p-1)\) is no longer an arbitrary weight. It is the exact modular thermal occupation associated with \(\log p=2\pi\omega_p\).

## 4. Branched exterior and the microscopic time-orientation sign

For the folded black-mirror radial coordinate
\[
r(\sigma)=r_h+\frac{\sigma^2}{8M},
\]
the sheet involution is
\[
D_H:\sigma\mapsto-\sigma,
\]
and the fixed point is
\[
\sigma=0,\qquad r=r_h.
\]

A natural hypothesis is
\[
\boxed{
t=\operatorname{sgn}\sigma.
}
\]

Then sheet exchange forces
\[
\boxed{t\mapsto-t}
\]
without inserting an independent charge conjugation.

If the physical relational grading is
\[
\chi=qt,
\]
then
\[
\boxed{
(q,t)\mapsto(q,-t)
\quad\Longrightarrow\quad
\chi\mapsto-\chi.
}
\]

Thus a geometrically forced time-orientation half-flip is sufficient to exchange the two relational matter sectors.

## 5. Fixed-point regularity and odd sections

Let the sheet involution act on a doubled field by
\[
(J\Psi)(\sigma)=U\,\Psi(-\sigma),
\]
where \(U^2=1\).

Decompose
\[
\Psi_\pm=\frac12(1\pm J)\Psi.
\]

At the fixed point \(\sigma=0\), any genuinely odd scalar component satisfies
\[
\boxed{\Psi_-(0)=0.}
\]

This is an exact branch-point statement.

It does **not** by itself imply that rest mass vanishes at the horizon. In the doubled-null-parent model,
\[
m^2c^2=k^2
\]
is a relative momentum invariant, and a relative coordinate can vanish while its conjugate momentum remains nonzero.

Therefore a horizon-annihilation theory needs an actual boundary conversion interaction; fixed-point kinematics alone is insufficient.

## 6. Minimal unitary boundary-conversion requirement

A charged fermion cannot simply disappear into photons. Global charge and fermion parity require the incoming boundary state to be a neutral even state.

Thus the relevant incoming object must be a paired/conjugate sector, schematically
\[
|\psi\rangle\otimes J|\psi\rangle,
\]
not one independent charged one-particle state.

A boundary conversion map
\[
V_H:\mathcal H_{\rm pair}\to\mathcal F_{\rm null,+}\otimes\mathcal F_{\rm null,-}
\]
should satisfy at minimum
\[
\boxed{
V_H^\dagger V_H=I_{\mathcal H_{\rm pair}}
}
\]
on the paired physical subspace, together with conservation of the globally defined gauge charges and stress energy.

This makes “annihilation” a unitary channel change from a neutral paired massive sector to null radiation, not destruction of information.

## 7. Zitter frequency as the relative orientation beat

The two oriented proper-time phases are
\[
d\phi_t=-t\,\frac{mc^2}{\hbar}\,d\tau.
\]

For \(t=\pm1\),
\[
\frac{d}{d\tau}(\phi_+-\phi_-)
=
-\frac{2mc^2}{\hbar}.
\]

Hence
\[
\boxed{
\omega_{\rm relative}
=
\frac{2mc^2}{\hbar}
=
\omega_Z.
}
\]

So the standard zitter factor two is exactly the beat frequency of the two opposite proper-time phase orientations.

This does not prove that Zitterbewegung is literally motion between black-hole sheets. It does show that the orientation-doublet interpretation reproduces the correct internal frequency without an adjustable factor.

## 8. One modular architecture

The exact identities now line up as

\[
\boxed{
\log p
=
2\pi\omega_p
}
\]
(arithmetic energy = modular boost energy),

\[
\boxed{
\frac1{p-1}
=
\frac1{e^{2\pi\omega_p}-1}
}
\]
(Haar occupation = Bose modular occupation),

\[
\boxed{
\mu_p^2
=
4\langle N_p\rangle
}
\]
(finite-place Casimir mass-square = entanglement occupation),

and for an ordinary massive fermionic orientation doublet,

\[
\boxed{
\omega_Z=2mc^2/\hbar
}
\]
(relative phase beat = zitter clock).

This suggests a master spectral picture:

\[
\text{paired local sectors}
\to
\text{modular generator}
\to
\text{entanglement covariance}
\to
\text{positive transverse/orientation gap}.
\]

The arithmetic sector supplies discrete modular frequencies \(\log p/(2\pi)\); the particle sector should arise from the spectrum of the same kind of positive off-diagonal/orientation coupling after gauge/internal sewing.

## 9. RH / dark-sector implication

The earlier profinite operator
\[
\mathsf M_f^2(X)
=
4M_*^2\sum_p\frac{v_p(X)}{p-1}
\]
can now be read as a modular-entanglement observable:
\[
\boxed{
\frac{\mathsf M_f^2(X)}{M_*^2}
=
4\sum_p v_p(X)\,
n_B\!\left(\frac{\log p}{2\pi};\beta=2\pi\right).
}
\]

This is the first non-ad-hoc route found so far from the arithmetic modular Hamiltonian \(H_p=(\log p)N_p\) to the previously postulated finite-place mass-square weight \(4/(p-1)\).

The next load-bearing theorem target is to construct this covariance/mass-square observable directly inside the same OS/modular standard form whose global determinant/scattering function contains the completed zeta data.

If successful, the RH no-ghost problem and the finite-place dark-sector mass operator really would descend from one modular operator rather than merely share similar arithmetic.
