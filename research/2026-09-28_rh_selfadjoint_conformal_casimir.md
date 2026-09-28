# Direct principal-series reformulation: RH as self-adjoint conformal-Casimir spectrality

Date: 2026-09-28
Status: exact reformulation / theorem target. No RH proof. The central new point is that one does not need to construct a first-order Hilbert--Polya operator if the completed zeta divisor can instead be realized as the spectrum of a self-adjoint 1D conformal Casimir.

## 1. Completed zeta factors exactly through the conformal Casimir variable

Let
\[
\Xi(z)=\frac{\xi(\tfrac12+z)}{\xi(\tfrac12)}.
\]
The functional equation gives
\[
\Xi(-z)=\Xi(z).
\]

Because \(\Xi\) is entire and even, its Taylor series contains only even powers:
\[
\Xi(z)=\sum_{n\ge0}a_n z^{2n}.
\]
Hence there is a unique entire function \(G(w)\) such that
\[
\Xi(z)=G(z^2).
\]

Now introduce the 1D conformal Casimir variable
\[
\boxed{
c=s(1-s)=\frac14-z^2,
\qquad
s=\frac12+z.
}
\]

Define
\[
\mathcal X(c)
=
G\!\left(\frac14-c\right).
\]
Then
\[
\boxed{
\frac{\xi(s)}{\xi(\tfrac12)}
=
\mathcal X\!\bigl(s(1-s)\bigr).
}
\]

This is an exact zero-independent consequence of the functional equation.

Thus the completed zeta function is already naturally a function of the quadratic \(PSL(2,\mathbb R)\) Casimir eigenvalue, not fundamentally of the first-order spectral parameter.

## 2. Why the Casimir is the right principal-series coordinate

For a scalar 1D conformal weight \(\Delta\), use the Casimir convention
\[
\boxed{
\mathcal C(\Delta)=\Delta(1-\Delta).
}
\]

On the unitary principal series
\[
\Delta=\frac12+i\lambda,
\qquad \lambda\in\mathbb R,
\]
one has
\[
\boxed{
\mathcal C
=
\frac14+\lambda^2
\in
\left[\frac14,\infty\right).
}
\]

So the principal series is precisely the branch of the conformal weight for which the Casimir is real and lies above the threshold \(1/4\).

## 3. Self-adjoint Casimir reality already forces the critical line

Let a nontrivial zero be
\[
\rho=\beta+i\gamma.
\]
Then
\[
\rho(1-\rho)
=
\beta(1-\beta)+\gamma^2
+
i\,\gamma(1-2\beta).
\]

Nontrivial zeta zeros have \(\gamma\ne0\). Therefore
\[
\boxed{
\rho(1-\rho)\in\mathbb R
\quad\Longrightarrow\quad
\beta=\frac12.
}
\]

Indeed the imaginary part is \(\gamma(1-2\beta)\).

This is the key simplification:

\[
\boxed{
\text{To prove RH, it is enough to prove that the Casimir values attached to the zeros are spectral values of a self-adjoint operator.}
}
\]

One does NOT first need a self-adjoint operator whose eigenvalues are the ordinates \(\gamma\).

The second-order route is enough.

## 4. Stronger principal-series form

If the relevant self-adjoint operator \(C_{\rm phys}\) also satisfies
\[
C_{\rm phys}\ge\frac14 I,
\]
then any zero represented by its spectrum obeys
\[
\rho(1-\rho)
=
\frac14+\lambda^2
\]
with real \(\lambda\), hence
\[
\boxed{
\rho=\frac12\pm i\lambda.
}
\]

So the desired theorem can be stated exactly as:

> Construct, without zero data, a self-adjoint physical \(PSL(2,\mathbb R)\) Casimir \(C_{\rm phys}\ge1/4\) whose relative spectral determinant is the completed zeta function.

That would prove that every nontrivial zero belongs to the unitary principal series of the 1D conformal theory.

## 5. Exact equivalence with the existing positive Fredholm target

The current RH-equivalent target is
\[
\Xi(z)=\det(I+z^2A),
\qquad A\ge0
\]
with \(A\) positive trace class and constructed without zero input.

Put
\[
c=\frac14-z^2.
\]
Then
\[
\Xi(z)
=
\det\!\left(I+\left(\frac14-c\right)A\right).
\]

Assume \(A\) is injective on its physical support and define the unbounded positive operator
\[
\boxed{
C_{\rm phys}
=
\frac14 I+A^{-1}.
}
\]

Then
\[
C_{\rm phys}-\frac14 I=A^{-1}
\]
and therefore
\[
\boxed{
\Xi(z)
=
\det\!\left[
(C_{\rm phys}-c)
(C_{\rm phys}-\tfrac14)^{-1}
\right].
}
\]

So the old positive-Fredholm problem and the new conformal-Casimir problem are exactly the same theorem in dual variables.

The zero condition becomes
\[
c\in\operatorname{spec}(C_{\rm phys}),
\]
with
\[
c=\frac14+\gamma^2
\]
under RH.

## 6. Why this may be easier than Hilbert--Polya

A first-order Hilbert--Polya operator \(H\) would require
\[
\operatorname{spec}(H)=\{\gamma_n\}.
\]

The Casimir route only requires a positive self-adjoint second-order operator
\[
\boxed{
C_{\rm phys}
=
\frac14+H^2
}
\]
at the level of spectral data.

Second-order positive operators are exactly what the current programme already knows how to generate:
- Hodge Laplacians \(D^2=dd^*+d^*d\);
- Schur/Feshbach complements of positive block operators;
- OS reconstructed positive Hamiltonian squares;
- reversible Poincare generators;
- positive Fredholm density operators via inversion.

Thus the RH problem is much better aligned with the machinery already shared with Yang--Mills and Hodge theory than the usual first-order Hilbert--Polya formulation suggests.

## 7. Connection to the RH/YM/BSD spectral trichotomy

The emerging master architecture now sharpens further.

The natural universal object is not necessarily a first-order arithmetic Hamiltonian. It may be a physical Hodge/Casimir operator \(C_{\rm phys}\).

For RH:
\[
\boxed{
C_{\rm phys}\ge1/4
}
\]
and the completed zeta divisor is its relative spectrum.

For Yang--Mills:
a corresponding positive Hodge operator must have
\[
L_{\rm YM}\ge m^2
\]
on physical cohomology-perp.

For BSD:
the analogous operator has a protected kernel whose dimension is the arithmetic rank.

So the same second-order technology naturally addresses:
- spectral threshold / principal-series support;
- physical mass gap;
- cohomological nullity.

## 8. Free arithmetic Casimir is NOT enough

The microscopic number-circle Hamiltonian is
\[
H_0=\log|D|
\]
with eigenvalues \(\log n\).

Its naive conformal Casimir
\[
C_0=\frac14+H_0^2
\]
has spectrum
\[
\frac14+(\log n)^2,
\]
not
\[
\frac14+\gamma_n^2.
\]

Therefore the zeta zeros are not the free arithmetic principal-series modes.

The missing operator must be the COLLECTIVE physical Casimir after prime--Archimedean sewing and quotient:
\[
\boxed{
C_{\rm phys}
=
\text{physical Schur/Hodge/OS completion of the microscopic arithmetic system}.
}
\]

This is precisely consistent with the earlier distinction between microscopic prime energies and collective vacuum resonances.

## 9. The direct proof target

Stop asking merely:

"Why should the zeros have real ordinates?"

Ask instead:

\[
\boxed{
\text{Can the completed arithmetic response be realized as the relative determinant of a self-adjoint conformal Casimir }C_{\rm phys}\ge1/4?
}
\]

Concretely, seek a zero-independent operator construction satisfying
\[
\boxed{
\frac{\xi(s)}{\xi(\tfrac12)}
=
\det_{\rm rel}\!\left(
C_{\rm phys}-s(1-s),
\,
C_{\rm phys}-\frac14
\right).
}
\]

If this identity is obtained with \(C_{\rm phys}\) self-adjoint and bounded below by \(1/4\), RH follows immediately and the zeros are literally principal-series spectral points of the 1D field.

This is the most direct current formulation of Daniel's statement "prove the zeros are in the principal series of the 1D field."
