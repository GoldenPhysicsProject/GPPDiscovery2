# Prime Poisson kernel / Hankel-moment bridge

Codex/GPT discovery track, 2026-08-24.

## Exact identity on the absolute-convergence half-plane

Let `a>1` and `t` be real. Mathlib already identifies the global von Mangoldt L-series with the genuine logarithmic derivative on this half-plane,

\[
-\frac{\zeta'}{\zeta}(s)=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},\qquad \Re s>1.
\]

At `s=a+it`, using

\[
n^{-a-it}=n^{-a}e^{-it\log n},
\]

and absolute convergence, taking real parts termwise gives the first global form

\[
\boxed{
\Phi(a,t):=\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_{n\ge2}\Lambda(n)n^{-a}\cos(t\log n).
}
\]

Since `Lambda(n)` is supported on prime powers, regrouping the absolutely convergent series gives

\[
\Phi(a,t)
=\sum_p \log p\sum_{k\ge1}p^{-ka}\cos(k t\log p).
\]

For `0<r<1`, the Poisson kernel is

\[
K_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}
=1+2\sum_{k\ge1}r^k\cos(k\theta).
\]

Therefore, with `r_p(a)=p^{-a}`,

\[
\boxed{
\Phi(a,t)
=\frac12\sum_p \log p\,[K_{p^{-a}}(t\log p)-1].
}
\]

### Absolute convergence

The global von Mangoldt series is absolutely convergent for `a>1`. The prime-power form has the elementary majorant

\[
\sum_p\log p\sum_{k\ge1}p^{-ka}
=\sum_p\frac{\log p}{p^a-1}
= -\frac{\zeta'(a)}{\zeta(a)}<\infty.
\]

Since `|cos|<=1`, this controls the oscillatory series uniformly in `t` for fixed `a>1`. Hence taking real parts, regrouping by prime powers, and replacing the geometric Fourier series by the Poisson closed form are legitimate operations in the ordinary absolutely convergent sense. No analytic continuation or summability prescription occurs here.

At `t=0`,

\[
-\frac{\zeta'}{\zeta}(a)
=\frac12\sum_p\log p\,[K_{p^{-a}}(0)-1]
=\sum_p\log p\sum_{k\ge1}p^{-ka}.
\]

## Radial derivatives are the Hankel moments

Differentiating termwise on every closed half-plane `a>=1+epsilon` gives, for every integer `r>=0`,

\[
\boxed{
(-1)^r\frac{d^r}{da^r}\left[-\frac{\zeta'}{\zeta}(a)\right]
=\sum_p(\log p)^{r+1}\sum_{k\ge1}k^r p^{-ka}
=\sum_{n\ge2}\Lambda(n)(\log n)^r n^{-a}.
}
\]

Equivalently these are the radial derivatives, at `theta=0`, of the prime Poisson-kernel family:

\[
(-1)^r\frac{d^r}{da^r}\left[-\frac{\zeta'}{\zeta}(a)\right]
=\frac12\sum_p\log p\,(-1)^r\frac{d^r}{da^r}[K_{p^{-a}}(0)-1].
\]

Thus the previously identified Hankel moment matrices are not an unrelated positivity gadget. They are the radial-moment Gram matrices of the same local positive-type kernels whose angular variable encodes the finite-prime explicit-formula oscillations.

## Two-variable positive-kernel viewpoint

For each fixed `a>1`, every local summand is positive type as a function of `t` because its Fourier coefficients are nonnegative:

\[
K_{p^{-a}}(t\log p)-1
=2\sum_{k\ge1}p^{-ka}\cos(k t\log p).
\]

Absolute convergence allows the prime sum to preserve positive type. Thus

\[
\Phi(a,\cdot)
\]

is itself a positive-type function on the real `t` axis for every `a>1`.

Along `t=0`, all alternating radial derivatives are strictly positive and form the moment sequence used by the Hankel construction. This supplies a canonical two-variable bridge:

- angular variable `t` <-> prime-frequency / explicit-formula oscillation;
- radial variable `a` <-> thermodynamic damping / cumulant-Hankel moments.

The critical-line local kernel used elsewhere corresponds to the radial value `a=1/2` at each individual prime, whereas the global prime sum is absolutely convergent only for `a>1`. Moving the *global* identity from `a>1` toward `a=1/2` therefore remains a genuine analytic-continuation/explicit-formula problem; local positivity alone does not justify that passage.

## Consequence for the RH program

This bridge ties two independently positive constructions together before zeros enter. It does **not** prove Weil positivity or RH. The missing global theorem remains an unconditional completed explicit-formula identity on an adequate test class, including the Archimedean term and the correct regularization/continuation of the prime contribution.

## Formalization target

1. `DONE`: arbitrary-radial local identity
   \[
   W_{p,a}(t)=2\Re[-\zeta_p'/\zeta_p(a+it)].
   \]
2. `IN CI`: finite-prime summation of the arbitrary-radial identity.
3. On `a>1`, connect the infinite limit to the existing `GlobalVonMangoldtBridge` and prove the real cosine-series form.
4. Prove positive-type preservation under the absolutely convergent prime sum.
5. Differentiate at `t=0` to connect radial derivatives with the Hankel moments.

No critical-strip positivity is claimed.
