# Global von Mangoldt cosine series and prime Poisson regrouping

For `a > 1` and `t in R`, the absolutely convergent Dirichlet series gives

\[
-\frac{\zeta'}{\zeta}(a+it)
=\sum_{n\ge 2}\frac{\Lambda(n)}{n^{a+it}}.
\]

Because the series is absolutely convergent, real part may be taken termwise. For positive integer `n`,

\[
n^{-(a+it)}=n^{-a}e^{-it\log n},
\]

hence

\[
\boxed{
\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_{n\ge2}\Lambda(n)n^{-a}\cos(t\log n).
}
\]

Using `Lambda(n)=log p` exactly when `n=p^k` is a prime power, absolute convergence permits regrouping:

\[
\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_p\log p\sum_{k\ge1}p^{-ak}\cos(k t\log p).
\]

Set

\[
r_p=p^{-a},\qquad \theta_p=t\log p.
\]

For `0<r<1`, the Poisson kernel is

\[
K_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}
=1+2\sum_{k\ge1}r^k\cos(k\theta).
\]

Therefore

\[
\boxed{
2\Re\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_p \log p\,[K_{p^{-a}}(t\log p)-1],
\qquad a>1.
}
\]

The convergence justification is inherited from the von Mangoldt Dirichlet series:

\[
\sum_p\sum_{k\ge1}\log p\,p^{-ak}
=\sum_{n\ge2}\Lambda(n)n^{-a}<\infty.
\]

Thus Tonelli/Fubini rearrangement is legitimate on the honest half-plane `a>1`.

This identity is an exact bridge between the global logarithmic derivative and the infinite sum of local prime Poisson responses. It makes no claim of positivity after continuation into the critical strip and no RH claim.
