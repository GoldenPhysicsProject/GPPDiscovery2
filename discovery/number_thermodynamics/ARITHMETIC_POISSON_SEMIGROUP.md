# The arithmetic response is an exact Poisson semigroup

Codex/GPT discovery track, 2026-08-24.

## 1. Global response

For `a>1`, define

\[
\Phi(a,t):=\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_{n\ge2}\Lambda(n)e^{-a\log n}\cos(t\log n).
\]

The series and all derivatives used below converge normally on every closed half-plane `a>=1+epsilon`.

## 2. Fourier spectral measure

Define the positive symmetric atomic measure on frequency space

\[
\boxed{
\mu_0:=\frac12\sum_{n\ge2}\Lambda(n)
\left(\delta_{\log n}+\delta_{-\log n}\right).
}
\]

Formally `mu_0` has infinite total mass, but after Poisson damping by `a>1`,

\[
d\mu_a(\xi)=e^{-a|\xi|}d\mu_0(\xi)
\]

is finite because

\[
\int d\mu_a
=\sum_{n\ge2}\Lambda(n)n^{-a}<\infty.
\]

Then exactly

\[
\boxed{
\Phi(a,t)=\int_{\mathbb R}e^{it\xi}e^{-a|\xi|}\,d\mu_0(\xi)
=\int_{\mathbb R}e^{it\xi}\,d\mu_a(\xi).
}
\]

Thus the arithmetic response is the ordinary Poisson semigroup applied to its undamped arithmetic boundary spectrum.

## 3. First-order Poisson-semigroup equation

Let `|D_t|` denote the Fourier multiplier with symbol `|xi|`. Since differentiation in `a` multiplies each Fourier mode by `-|xi|`,

\[
\boxed{
\partial_a\Phi(a,t)=-|D_t|\Phi(a,t).
}
\]

Equivalently,

\[
\boxed{
\Phi(a+h,\cdot)=e^{-h|D_t|}\Phi(a,\cdot),\qquad h>0.
}
\]

The semigroup law is the elementary identity

\[
e^{-(a+h)|\xi|}=e^{-h|\xi|}e^{-a|\xi|}.
\]

Because the Poisson semigroup preserves positive spectral measures, positive type in `t` is automatic throughout the convergent region.

## 4. Harmonic extension

Applying another `a` derivative gives the multiplier `|xi|^2=xi^2`, while `partial_t^2` gives `-xi^2`. Hence

\[
\boxed{
(\partial_a^2+\partial_t^2)\Phi(a,t)=0.
}
\]

So `Phi` is literally a harmonic extension in the upper-half-plane variables `(t,a)`, not merely the real part of a holomorphic function by abstract complex analysis.

## 5. Local primes are periodic Poisson semigroups

For a single prime `p`, the local response is

\[
W_{p,a}(t)
=2\log p\sum_{k\ge1}e^{-a k\log p}\cos(k t\log p).
\]

Writing

\[
r_p(a)=e^{-a\log p}=p^{-a},
\]

this becomes

\[
W_{p,a}(t)=\log p\,[K_{r_p(a)}(t\log p)-1].
\]

Thus the local periodic Poisson kernel is simply the restriction of the global Poisson semigroup to the arithmetic frequency lattice

\[
\{k\log p:k\in\mathbb Z\setminus\{0\}\}.
\]

The global von-Mangoldt response and the finite-prime `KrClosed` construction are therefore not analogous structures. They are the **same Poisson semigroup**, resolved once by integers/prime powers and once by local prime frequency lattices.

## 6. Hankel moments as semigroup-generator moments

At `t=0`,

\[
(-1)^r\partial_a^r\Phi(a,0)
=\int |\xi|^r e^{-a|\xi|}\,d\mu_0(\xi)
=\sum_{n\ge2}\Lambda(n)(\log n)^r n^{-a}.
\]

Thus the Hankel moment sequence is the sequence of moments of the positive generator `|D_t|` in the arithmetic spectral measure.

This gives an operator interpretation of the previously found total/Hankel positivity: it is positivity of powers of the nonnegative Poisson generator on the convergent arithmetic spectrum.

## 7. Critical-line boundary

The formal value `a=1/2` would correspond to evolving the undamped arithmetic boundary spectrum by `e^{-|D|/2}`. The resulting total mass

\[
\sum_{n\ge2}\Lambda(n)n^{-1/2}
\]

diverges. Therefore the global positive-measure Poisson semigroup cannot simply be evaluated at the critical radius.

The completed explicit formula must first remove/renormalize the continuum density associated with the zeta pole and add the Archimedean contribution. In the shifted description of the companion note, that operation replaces the positive arithmetic measure by a signed discrepancy measure.

So the obstruction is now especially concrete:

**local and convergent global evolution are positivity-preserving Poisson flow; the hard step is constructing the correctly completed renormalized boundary datum whose half-density evolution reproduces the Weil functional.**

No RH claim is made here.
