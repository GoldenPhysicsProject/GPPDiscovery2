# Shadow-paired Gamma factor as a positive Casimir resolvent determinant — 2026-09-16

Status: exact Archimedean factorization. No RH proof claimed.

Let

\[
A(s)=\pi^{-s/2}\Gamma\!\left(1+\frac s2\right),
\qquad
F_1(s)=(s-1)\zeta(s),
\]

so that

\[
\xi(s)=A(s)F_1(s).
\]

Introduce the shadow-invariant physical Casimir variable

\[
t=s(1-s),
\qquad s=\frac12+r,
\qquad r^2=\frac14-t.
\]

Then

\[
A(s)A(1-s)
=\pi^{-1/2}
\Gamma\!\left(\frac54+\frac r2\right)
\Gamma\!\left(\frac54-\frac r2\right).
\]

Use the exact paired Gamma product

\[
\frac{\Gamma(z+a)\Gamma(z-a)}{\Gamma(z)^2}
=\prod_{n=0}^\infty
\left(1-\frac{a^2}{(n+z)^2}\right)^{-1}.
\]

At \(z=5/4\), \(a=r/2\), define

\[
\lambda_n=(2n+2)(2n+3).
\]

Since

\[
4(n+5/4)^2=\lambda_n+\frac14,
\qquad
r^2=\frac14-t,
\]

one obtains

\[
\boxed{
\frac{A(s)A(1-s)}{A(1/2)^2}
=\prod_{n=0}^\infty
\frac{\lambda_n+1/4}{\lambda_n+t}.
}
\]

Thus if \(L_\infty\) is the positive diagonal operator

\[
L_\infty e_n=\lambda_n e_n,
\]

then the shadow-paired Archimedean factor is the relative resolvent determinant

\[
\boxed{
\frac{A(s)A(1-s)}{A(1/2)^2}
=\det_{\rm rel}\!\left[(L_\infty+1/4)(L_\infty+t)^{-1}\right].
}
\]

The poles lie at

\[
t=-\lambda_n.
\]

These coincide exactly with the folded locations of the trivial zeta zeros. Indeed, for \(m=n+1\),

\[
s=-2m\quad\Longrightarrow\quad t=s(1-s)=-2m(2m+1)=-\lambda_n,
\]

and the shadow root \(s=1+2m\) gives the same \(t\).

The shadow-doubled arithmetic factor

\[
P_{\rm ar}(t)=F_1(s)F_1(1-s)
\]

is single-valued in \(t\), and its trivial-zero sector cancels these Archimedean poles in

\[
\boxed{\xi(s)^2=A(s)A(1-s)P_{\rm ar}(t).}
\]

This is analytic shadow doubling, not ordinary Hermitianization to \(|\xi|^2\). It preserves the analytic zero divisor. The sequence

\[
\lambda_n=(2n+2)(2n+3)=\ell(\ell+1),\qquad \ell=2,4,6,\ldots,
\]

is the even spherical-Casimir sequence.

## Structural consequence

The completed square can be viewed as an exact relative determinant in which:

1. the Archimedean sector supplies a positive diagonal Casimir operator \(L_\infty\);
2. the arithmetic shadow product supplies zeros at the negative spectral points \(-\lambda_n\);
3. those trivial channels cancel exactly;
4. the surviving zero divisor is the nontrivial folded divisor.

A genuinely operator-theoretic closure would require implementing this scalar pole-zero cancellation by a zero-independent partial isometry / supersymmetric pairing between the Archimedean modes and the trivial arithmetic boundary modes, then proving that the quotient physical Casimir pencil is self-adjoint positive. The scalar determinant identity alone does not supply that positive quotient.