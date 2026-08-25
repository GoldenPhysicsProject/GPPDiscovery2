# Fixed-prime prime-power Poisson fiber closure

Codex/GPT discovery track, 2026-08-25.

For a prime p, a>1, and real t, define

r = p^{-a},   theta = t log p.

The prime-power contribution to the real von-Mangoldt response is

S_p(a,t) = sum_{m>=1} (log p) exp(-m a log p) cos(m t log p).

Since exp(-a log p)=p^{-a}=r,

exp(-m a log p)=r^m,

and therefore

S_p(a,t)=(log p) sum_{m>=1} r^m cos(m theta).

For |r|<1 the elementary Poisson-kernel identity gives

2 sum_{m>=1} r^m cos(m theta)
  = (1-r^2)/(1-2 r cos theta+r^2)-1.

Thus

2 S_p(a,t)
 = (log p) [K_r(theta)-1]
 = W_{p,a}(t).

Hence each fixed prime tower is already exactly the local radial Poisson response. The only remaining global step is summing this identity over primes, justified by the absolute-convergence/Fubini theorem already established on a>1.

This is an identity in the honest convergence half-plane only; it contains no analytic continuation or RH assertion.
