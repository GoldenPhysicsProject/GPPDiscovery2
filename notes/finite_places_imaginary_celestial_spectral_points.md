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
