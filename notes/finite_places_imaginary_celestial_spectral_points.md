# Finite places as imaginary celestial spectral points

Date: 2026-09-26
Status: exact consequence of the existing finite-place Cayley coordinate and the celestial dictionary. Physical interpretation is proposed; RH is not proved.

## 1. Existing finite-place Cayley point

For a local parameter \(q>1\), the arithmetic-shadow construction has
\[
a_q=q^{-1/2},
\qquad
r_q=\frac{\sqrt q-1}{\sqrt q+1},
\qquad
\mu_q=\frac{2}{\sqrt{q-1}}.
\]
Matching the Riemann Cayley coordinate
\[
\beta(s)=\frac{s-1}{s}
\]
to \(r_q\) gives the exact real point
\[
\boxed{
s_q=\frac{\sqrt q+1}{2}.
}
\]
Its folded Casimir is
\[
\boxed{
u_q=s_q(s_q-1)=\frac{q-1}{4},
\qquad
\mu_q^2=\frac1{u_q}.
}
\]

## 2. Insert the celestial dictionary

For the scalar celestial principal-series coordinate,
\[
\Delta=2s=1+i\lambda.
\]
Therefore
\[
i\lambda=2s-1.
\]
At the finite-place Cayley point,
\[
i\lambda_q
=
2s_q-1
=
\boxed{\sqrt q}.
\]
Equivalently,
\[
\boxed{
\lambda_q=-i\sqrt q,
\qquad
q=-\lambda_q^2.
}
\]

So every finite local parameter \(q\) lands on the imaginary analytic
continuation of the same celestial spectral variable.

For an actual prime place \(q=p\),
\[
\boxed{
i\lambda_p=\sqrt p.
}
\]

The unitary celestial principal series has \(\lambda\in\mathbf R\).  The
finite-place points therefore do not lie on the physical unitary axis; they
are hyperbolic/evanescent analytic-continuation points of the same Casimir
family.

## 3. Casimir and local mass in the same variable

The celestial/arithmetic Casimir is
\[
s(1-s)=\frac{1+\lambda^2}{4}.
\]
At \(\lambda_p=-i\sqrt p\),
\[
\boxed{
s_p(1-s_p)
=
-\frac{p-1}{4}.
}
\]
Equivalently,
\[
s_p(s_p-1)=\frac{p-1}{4}.
\]

The finite-place mass becomes
\[
\boxed{
\mu_p
=
\frac{2}{\sqrt{p-1}}
=
\frac1{\sqrt{s_p(s_p-1)}}.
}
\]

The Poisson radius is simultaneously
\[
\boxed{
a_p=p^{-1/2}=\frac1{i\lambda_p}.
}
\]

Thus four previously separate local coordinates are one datum:
\[
\boxed{
p
\longleftrightarrow
i\lambda_p=\sqrt p
\longleftrightarrow
a_p=(i\lambda_p)^{-1}
\longleftrightarrow
s_p(s_p-1)=\frac{p-1}{4}
\longleftrightarrow
\mu_p^2=\frac4{p-1}.
}
\]

## 4. Why \(p=5\) is golden

At \(p=5\),
\[
i\lambda_5=\sqrt5,
\qquad
s_5=\frac{1+\sqrt5}{2}=\varphi,
\]
and
\[
1-s_5=-\varphi^{-1}.
\]
Also
\[
s_5(s_5-1)=1,
\qquad
\mu_5=1,
\qquad
\kappa_5=\log\varphi,
\qquad
r_5=\varphi^{-2}.
\]

So the observation \(i\lambda=\sqrt5\) is not an isolated numerical
coincidence.  It is the \(q=5\) member of the exact family
\[
\boxed{i\lambda_q=\sqrt q}.
\]
The prime \(5\) is distinguished because this family crosses unit Casimir /
unit transfer mass there.

## 5. Proposed physical reading

The resulting picture is:

- the Archimedean/celestial sector carries the continuous unitary line
  \(\lambda\in\mathbf R\);
- each finite prime place \(p\) supplies a discrete evanescent point
  \(\lambda_p=-i\sqrt p\);
- prime repetitions are propagation lengths \(m\log p\), not new places;
- the completed adelic theory sews the discrete finite-place channels to the
  continuous real-place principal series.

This suggests a sharper physical phrase:

> primes are discrete imaginary-momentum local channels of the same
> analytically continued principal-series Casimir whose real-momentum axis
> carries the unitary global spectrum.

This interpretation is not yet a theorem of celestial QFT.  The equations
above are exact consequences of the project's Cayley matching and
\(\Delta=2s\) dictionary.

## 6. RH relevance

If the completed adelic sewing converts the finite evanescent channels into a
closed conservative boundary problem, its allowed global normal-mode
frequencies should live on the real \(\lambda\) axis.  Under
\[
\lambda=2t,
\]
those frequencies are candidates for the Riemann ordinates.

The missing theorem remains the same: prove that the zeta zero condition is a
normal-mode condition of that closed unitary sewing rather than an open
analytic resonance condition.


## 7. The Riemann Cayley map is literally the celestial spectral Cayley map

Using
\[
s=\frac{1+i\lambda}{2},
\]
the arithmetic Cayley coordinate becomes
\[
\boxed{
\beta(s)=\frac{s-1}{s}
=\frac{i\lambda-1}{i\lambda+1}.
}
\]

This is the ordinary Cayley transform of the spectral variable \(i\lambda\).

For physical principal-series \(\lambda\in\mathbf R\),
\[
\left|\frac{i\lambda-1}{i\lambda+1}\right|=1,
\]
so the unitary celestial axis maps exactly to the boundary of the Cayley disk.

For the finite-place point \(i\lambda_p=\sqrt p\),
\[
\beta_p
=
\frac{\sqrt p-1}{\sqrt p+1}
=
r_p,
\]
the finite-place impedance contraction already derived independently.

Hence the diagram closes exactly:
\[
\boxed{
\lambda\in\mathbf R
\ \longleftrightarrow\
|\beta|=1
}
\]
for the unitary continuum, while
\[
\boxed{
i\lambda_p=\sqrt p
\ \longleftrightarrow\
\beta_p=r_p\in(0,1)
}
\]
for finite prime channels.

Since
\[
a_p=p^{-1/2},
\qquad
r_p=\frac{1-a_p}{1+a_p},
\]
one also has
\[
a_p=\frac1{i\lambda_p},
\qquad
r_p=\frac{i\lambda_p-1}{i\lambda_p+1}.
\]

Thus the Poisson radius, impedance radius, Riemann Cayley coordinate, and
analytically continued celestial spectral parameter form one exact Möbius
coordinate system.

In hyperbolic coordinates,
\[
a_p=\tanh\kappa_p
\]
gives
\[
\boxed{
i\lambda_p=\coth\kappa_p,
\qquad
r_p=e^{-2\kappa_p}.
}
\]
At \(p=5\),
\[
\coth(\log\varphi)=\sqrt5,
\qquad
e^{-2\log\varphi}=\varphi^{-2}.
\]

This is the cleanest explanation so far of why the user's
\(i\lambda=\sqrt5\) observation hit the golden transfer point exactly.


## 8. Prime axis versus zero axis in the same spectral plane

For any complex Riemann parameter \(s\), define the celestial/1D spectral
coordinate by
\[
\lambda=-i(2s-1).
\]
A hypothetical zeta zero
\[
\rho=\frac12+\eta+i\gamma
\]
therefore maps to
\[
\boxed{
\lambda_\rho=2\gamma-2i\eta.
}
\]
Hence
\[
\mathrm{RH}
\iff
\lambda_\rho\in\mathbf R
\quad\text{for every nontrivial zero.}
\]

By contrast, a finite prime place maps to
\[
\boxed{
\lambda_p=-i\sqrt p,
}
\]
which is purely imaginary.

Thus, in this common \(\lambda\)-plane, the proposed adelic geometry has two
orthogonal spectral loci:

\[
\boxed{
\text{finite prime channels: }\lambda=-i\sqrt p
\quad\text{(discrete imaginary axis),}
}
\]
\[
\boxed{
\text{unitary global modes: }\lambda\in\mathbf R
\quad\text{(continuous principal-series axis).}
}
\]

At the level of the Casimir,
\[
C(\lambda)=\frac{1+\lambda^2}{4},
\]
finite places have
\[
C_p=-\frac{p-1}{4}<0,
\]
whereas a critical zero ordinate has
\[
C_\gamma=\frac14+\gamma^2>0.
\]

This resembles the standard scattering separation between evanescent/bound
spectral data on an imaginary momentum axis and propagating unitary data on a
real momentum axis.  That is an interpretation, not yet a constructed
scattering theorem.  The project already has the required positive prime
operator \(Qe_p=pe_p\); in functional-calculus language,
\[
i\lambda_{\rm finite}=\sqrt Q.
\]
The next structural target is therefore a zero-independent boundary coupling
whose scattering/normal-mode operator takes the positive prime spectrum of
\(Q\) into the real principal-series spectrum while preserving the completed
Archimedean channel.
