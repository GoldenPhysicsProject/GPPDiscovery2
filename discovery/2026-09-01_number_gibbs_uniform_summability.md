# Two-parameter number-Gibbs: explicit all-beta log-moment summability

For

w_n(beta,eta) = n^{-beta} exp(-eta (log n)^2),

with eta > 0, every fixed logarithmic raw moment is absolutely summable for every real beta:

sum_{n>=1} n^{-beta} exp(-eta (log n)^2) (log n)^r < infinity

for every natural r.

## Explicit comparison

Let

A = |beta| + r + 2.

For x = log n >= 1,

x^r <= exp(r x),

because log x <= x. If in addition x >= A/eta, then

exp(-eta x^2) <= exp(-A x).

Therefore, for every

n >= exp(max(1, A/eta)),

we have

n^{-beta} exp(-eta (log n)^2) (log n)^r
<= exp((-beta + r - A) log n)
= n^{-beta+r-A}.

Since

-beta + r - A
= -beta - |beta| - 2
<= -2,

we obtain the uniform tail bound

0 <= n^{-beta} exp(-eta (log n)^2) (log n)^r <= n^{-2}.

Hence the series converges by comparison with zeta(2), for arbitrary real beta and every eta > 0.

## Consequences

1. The partition function Z(beta,eta) is finite for all beta in R whenever eta>0.
2. Raw log moments through every finite order exist, in particular orders 0 through 4 required by the two-observable Fisher determinant for X=log n and X^2.
3. The countable moment-limit hypotheses needed for the fixed (1,2,3) quantitative Fisher witness therefore have an elementary, explicit domination route; there is no need to assume beta>1 once eta>0.
4. The same comparison gives a reusable Lean theorem schema: choose an integer threshold N with log N >= max(1,(|beta|+r+2)/eta), prove the tail is bounded by n^-2, and invoke summability of n |-> (n:Real)^(-2).

This is stronger than the one-parameter zeta-Gibbs condition beta>1: the quadratic log confinement regularizes every polynomial power n^{-beta}, including negative beta.

No RH/Weil inference is involved.