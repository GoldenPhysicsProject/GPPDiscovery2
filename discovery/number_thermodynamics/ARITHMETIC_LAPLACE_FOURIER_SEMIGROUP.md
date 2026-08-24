# Arithmetic Laplace--Fourier semigroup behind the zeta response

Codex/GPT discovery track, 2026-08-24.

## Positive arithmetic spectral measure

Define the positive discrete measure on the logarithmic energy axis

\[
\boxed{
\nu:=\sum_{n\ge2}\Lambda(n)\,\delta_{\log n}.
}
\]

For every complex `s` with `Re s>1`, the ordinary absolutely convergent von Mangoldt Dirichlet series is exactly the Laplace transform of this measure:

\[
\boxed{
-\frac{\zeta'}{\zeta}(s)
=\int_0^\infty e^{-sx}\,d\nu(x).
}
\]

Indeed, evaluating the atomic integral gives

\[
\sum_{n\ge2}\Lambda(n)e^{-s\log n}
=\sum_{n\ge2}\Lambda(n)n^{-s}.
\]

No continuation is used here.

## Two-variable response

Write

\[
s=a+it,\qquad a>1,
\]

and define

\[
\Phi(a,t):=\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right].
\]

Then

\[
\boxed{
\Phi(a,t)
=\int_0^\infty e^{-ax}\cos(tx)\,d\nu(x)
=\sum_{n\ge2}\Lambda(n)n^{-a}\cos(t\log n).
}
\]

Thus `a` is literally a Laplace damping/radial variable and `t` is literally the Fourier/spectral variable conjugate to logarithmic arithmetic energy `x=log n`.

## Positive type in t

For fixed `a>1`, define the finite positive tilted measure

\[
d\nu_a(x):=e^{-ax}d\nu(x).
\]

Its total mass is

\[
\nu_a([0,\infty))
=\sum_{n\ge2}\Lambda(n)n^{-a}
=-\frac{\zeta'(a)}{\zeta(a)}<\infty.
\]

Symmetrize it to a finite positive measure on `R`:

\[
d\mu_a(x)
:=\frac12d\nu_a(x)+\frac12d\nu_a(-x).
\]

Then

\[
\boxed{
\Phi(a,t)=\int_{\mathbb R}e^{itx}\,d\mu_a(x).
}
\]

Therefore `Phi(a,.)` is positive definite / positive type by the elementary Fourier-transform-of-a-positive-measure argument. This gives the global `a>1` positive-type theorem directly, independently of grouping the atoms into local prime Poisson kernels.

The local prime-Poisson decomposition and this global von-Mangoldt measure representation are two resolutions of the same positive object.

## Complete monotonicity in a

At fixed `t=0`,

\[
\Phi(a,0)=\int_0^\infty e^{-ax}\,d\nu(x).
\]

Hence for every integer `r>=0`, termwise differentiation on `a>=1+epsilon` gives

\[
\boxed{
(-1)^r\partial_a^r\Phi(a,0)
=\int_0^\infty x^r e^{-ax}\,d\nu(x)
=\sum_{n\ge2}\Lambda(n)(\log n)^r n^{-a}>0.
}
\]

These are exactly the positive moment sequences entering the Hankel Gram matrices.

So complete monotonicity of the radial response is simply positivity of moments of the exponentially tilted arithmetic measure.

## Spectral derivatives and the same moments

Because `mu_a` is symmetric, odd `t` derivatives vanish at the origin. For every `m>=0`,

\[
\boxed{
(-1)^m\partial_t^{2m}\Phi(a,0)
=\sum_{n\ge2}\Lambda(n)(\log n)^{2m}n^{-a}>0.
}
\]

More generally,

\[
\boxed{
(-1)^{r+m}\partial_a^r\partial_t^{2m}\Phi(a,0)
=\sum_{n\ge2}\Lambda(n)(\log n)^{r+2m}n^{-a}>0.
}
\]

Thus the radial Hankel moments and the even spectral derivatives are not merely analogous: they are literally the same arithmetic moments accessed in two coordinate directions.

## Harmonicity

Every atom contributes

\[
e^{-ax}\cos(tx),
\]

which satisfies

\[
(\partial_a^2+\partial_t^2)\,[e^{-ax}\cos(tx)]=0.
\]

Absolute convergence of the differentiated series on `a>=1+epsilon` gives

\[
\boxed{
(\partial_a^2+\partial_t^2)\Phi(a,t)=0,
\qquad a>1.
}
\]

This is of course equivalent to the fact that `Phi` is the real part of the holomorphic function `-zeta'/zeta(s)` on the zero-free half-plane `Re s>1`, but the measure representation explains the same fact directly in the radial/angular kernel variables.

## Semigroup viewpoint

Let `T_a` denote multiplication of the positive spectral measure by `e^{-ax}`. Then increasing `a` composes multiplicatively:

\[
e^{-(a+b)x}=e^{-ax}e^{-bx}.
\]

The family is therefore an ordinary positive Laplace semigroup acting on the arithmetic spectral measure. The local prime radius

\[
r_p(a)=p^{-a}=e^{-a\log p}
\]

is exactly the semigroup damping factor evaluated at the prime frequency `log p`.

This explains why the prime Poisson radius, Gibbs inverse temperature, von-Mangoldt cumulant moments, and positive Fourier coefficients all use the same exponential parameter.

## RH boundary

Everything above is unconditional only in the absolute-convergence domain `a>1`. The representation does **not** justify evaluating the global positive measure transform at `a=1/2`: the total tilted mass diverges long before that point. A completed/regularized explicit-formula object must replace this naive positive measure if one wants to cross the pole and reach critical-line geometry.

That is exactly where the global RH difficulty remains.
