# Continuous Gamma chamber flow: all-order cumulants

Status: exact analytic consequence of the discovery-level Barnes transform identity; not yet Lean-certified.

The continuous chamber family is

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2,\qquad c>0,
\]

with characteristic/Fourier transform

\[
\widehat\rho_c(t)=\operatorname{sech}^{2c}(t/2).
\]

The integer chamber family is recovered at `c = k+1`.

## All even cumulants

Use the convergent Taylor expansion near the origin

\[
\log\cosh z
 =\sum_{n\ge1}\frac{2^{2n}(2^{2n}-1)B_{2n}}{2n(2n)!}z^{2n}.
\]

Therefore

\[
\log\widehat\rho_c(t)
=-2c\log\cosh(t/2)
=-\sum_{n\ge1}\frac{c(2^{2n}-1)B_{2n}}{n(2n)!}t^{2n}.
\]

For a centered symmetric law,

\[
\log\widehat\rho_c(t)
=\sum_{n\ge1}\frac{(-1)^n\kappa_{2n}}{(2n)!}t^{2n}.
\]

Since `B_{2n}=(-1)^{n+1}|B_{2n}|`, coefficient comparison gives the exact all-order law

\[
\boxed{\kappa_{2n}(c)=\frac{c(2^{2n}-1)|B_{2n}|}{n}},\qquad n\ge1,
\]

and every odd cumulant vanishes.

Checks:

\[
\kappa_2=\frac c2,\qquad
\kappa_4=\frac c4,\qquad
\kappa_6=\frac c2,
\]

matching the previously recorded low-order expansion.

## Gaussianization hierarchy

Because every nonzero even cumulant is linear in the convolution parameter `c`, while

\[
\kappa_2(c)=c/2,
\]

the standardized cumulants satisfy

\[
\frac{\kappa_{2n}(c)}{\kappa_2(c)^n}
=\frac{2^n(2^{2n}-1)|B_{2n}|}{n}\,c^{1-n}.
\]

Thus all standardized cumulants of order `2n>2` decay exactly like `c^{1-n}`. In particular,

\[
\gamma_2=\frac{\kappa_4}{\kappa_2^2}=\frac1c.
\]

For the discrete chambers `c=k+1`, this gives a quantitative central-limit hierarchy under increasing convolution order:

\[
\frac{\kappa_{2n}(k+1)}{\kappa_2(k+1)^n}=O((k+1)^{1-n}).
\]

This is stronger than the earlier variance/excess-kurtosis observation: the entire standardized cumulant tower Gaussianizes at explicit powers of the chamber parameter.

## Exact semigroup consistency

The transform law also gives

\[
\rho_c*\rho_d=\rho_{c+d}.
\]

The all-order cumulant formula is exactly additive:

\[
\kappa_{2n}(c+d)=\kappa_{2n}(c)+\kappa_{2n}(d),
\]

as required for a convolution semigroup. This is an independent structural consistency check on the coefficient formula.

## Formalization boundary

Do not promote this to a theorem about the existing Lean chamber densities until the following are formalized:

1. the arbitrary-positive-`c` Barnes Fourier-Gamma transform;
2. normalization/Fourier uniqueness needed to identify convolution laws;
3. the Taylor/Bernoulli expansion of `log cosh` (or an equivalent derivative recursion) sufficient to extract cumulants.

The current claim is exact conditional on the Barnes transform identity already numerically and symbolically audited in Discovery2. It is not a Weil-positivity theorem and has no RH consequence by itself.
