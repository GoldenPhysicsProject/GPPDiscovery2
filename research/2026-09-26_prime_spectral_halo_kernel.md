# Prime spectral halo kernel from the finite-place mass/weight law

Date: 2026-09-26
Status: exact arithmetic asymptotic for a candidate real-place kernel. The identification of this kernel with physical halo density is a hypothesis, not yet derived.

## 1. Candidate spectral kernel

The conditional cold-fluid model gives two arithmetic ingredients:

\[
m_p=\frac{2M_*}{\sqrt{p-1}},
\qquad
w_p=\frac4{(p-1)^2}.
\]

The weight \(w_p\) is the product of the critical Haar occupation scale
\((p-1)^{-1}\) and the finite-place mass-square scale
\(4(p-1)^{-1}\), normalized to a unit Archimedean reference mode.

A minimal static real-place spectral kernel is therefore

\[
\boxed{
K_{M_*}(r)
=
4\sum_{p}
\frac{
\exp\!\left[-2M_*r/\sqrt{p-1}\right]
}{
(p-1)^2
}.
}
\]

This is absolutely convergent for every \(r\ge0\).

At the origin,

\[
\boxed{
K_{M_*}(0)
=
C_{\rm adelic}
=
4\sum_p\frac1{(p-1)^2}
\approx5.500260.
}
\]

Hence any density proportional to \(K_{M_*}\) has a finite central core.

## 2. Large-radius asymptotic

For large primes,

\[
m_p\sim\frac{2M_*}{\sqrt p},
\qquad
w_p\sim\frac4{p^2}.
\]

By the prime number theorem,

\[
\sum_p f(p)
\sim
\int_2^\infty \frac{f(x)}{\log x}\,dx
\]

for the smooth tail relevant here.  Therefore

\[
K_{M_*}(r)
\sim
4\int_2^\infty
\frac{x^{-2}e^{-2M_*r/\sqrt x}}{\log x}\,dx.
\]

Set

\[
y=\frac{2M_*r}{\sqrt x},
\qquad
x=\frac{4M_*^2r^2}{y^2}.
\]

Then

\[
4x^{-2}|dx|
=
\frac{2y}{M_*^2r^2}\,dy,
\]

and

\[
\log x
=
2\log\frac{2M_*r}{y}.
\]

Thus

\[
K_{M_*}(r)
\sim
\frac1{M_*^2r^2}
\int_0^\infty
\frac{y e^{-y}}
{\log(2M_*r/y)}\,dy.
\]

Since the integral is concentrated at \(y=O(1)\),

\[
\boxed{
K_{M_*}(r)
\sim
\frac1{
M_*^2r^2\log(2M_*r)
}
\qquad
(M_*r\to\infty),
}
\]

up to the usual slowly varying logarithmic corrections.

This is the central structural result:

\[
\boxed{
\text{finite prime spectrum}
+
m_p\propto p^{-1/2}
+
w_p\propto p^{-2}
\Longrightarrow
K(r)\sim \frac1{r^2\log r}.
}
\]

The \(r^{-2}\) behavior is the isothermal-halo power law; the arithmetic sparsity
of the primes contributes the extra logarithmic running.

## 3. Conditional halo interpretation

If the adelic real-place reconstruction produces

\[
\rho_{\rm DM}(r)
=
\rho_* K_{M_*}(r),
\]

then

\[
\rho_{\rm DM}(0)
=
\rho_* C_{\rm adelic}<\infty,
\]

while at large radius

\[
\boxed{
\rho_{\rm DM}(r)
\sim
\frac{\rho_*}
{M_*^2r^2\log(2M_*r)}.
}
\]

So the same prime tower gives both:

- a finite-density inner core;
- a quasi-isothermal outer halo.

The enclosed mass then obeys

\[
M_{\rm DM}(<r)
=
4\pi\int_0^r s^2\rho_{\rm DM}(s)\,ds
\sim
\frac{4\pi\rho_*}{M_*^2}
\frac{r}{\log(2M_*r)},
\]

and hence

\[
\boxed{
v_c^2(r)
=
\frac{GM_{\rm DM}(<r)}{r}
\sim
\frac{4\pi G\rho_*}
{M_*^2\log(2M_*r)}.
}
\]

The rotation speed is therefore asymptotically almost flat, with only a very slow
logarithmic decline.

This is qualitatively different from inserting a pseudo-isothermal profile by hand:
the power law follows from the prime counting density.

## 4. Why the exponent is rigid

More generally, suppose

\[
m_p\asymp p^{-1/2},
\qquad
w_p\asymp p^{-\alpha}.
\]

The same PNT calculation gives a Laplace tail scaling approximately as

\[
K_\alpha(r)
\asymp
\frac{
r^{\,2-2\alpha}
}{
\log r
}.
\]

Thus an isothermal \(r^{-2}\) tail requires

\[
2-2\alpha=-2,
\]

or

\[
\boxed{\alpha=2.}
\]

But \(\alpha=2\) is exactly what the arithmetic cold-fluid model produced:

\[
w_p
\propto
\underbrace{(p-1)^{-1}}_{\text{Haar occupation}}
\underbrace{(p-1)^{-1}}_{\text{Casimir mass}^2}.
\]

So the halo exponent is not independently tuned once those two previously derived
finite-place laws are accepted.

## 5. Prime sparsity leaves an observable logarithmic signature

If the internal labels were all positive integers rather than primes, the density of
labels would be \(dx\), and the same spectrum/weight law would give a pure \(r^{-2}\)
tail.

Restricting to primes replaces \(dx\) by \(dx/\log x\), yielding

\[
\boxed{
\rho(r)\propto\frac1{r^2\log r}.
}
\]

Therefore the logarithmic departure from an exactly flat rotation curve is a potential
number-theoretic signature of the construction rather than a nuisance correction.

A serious phenomenological test would fit the predicted slowly running outer slope to
galaxy rotation curves and weak/strong lensing without allowing an arbitrary halo
exponent.

## 6. What is still unproved

The arithmetic asymptotic above is robust.  The physical identification

\[
\rho_{\rm DM}(r)\propto K_{M_*}(r)
\]

is not.

A valid derivation must show that the real-place two-point function, static response,
or stress-energy obtained by integrating the finite adelic places has precisely this
positive spectral Laplace form.

Different real-place kernels can insert additional powers of \(m_p\), \(r\), or
Yukawa factors and thereby change the halo exponent.  Therefore this note identifies
a sharp reconstruction target rather than declaring the halo solved.

The next calculation should derive the static kernel from an explicit quadratic adelic
action and determine whether the physical stress tensor selects \(K_{M_*}\), a derivative
of it, or a different spectral transform.
