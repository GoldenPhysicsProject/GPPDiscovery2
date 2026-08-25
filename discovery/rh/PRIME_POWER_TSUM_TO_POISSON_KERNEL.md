# Prime-power double tsum to the global prime-Poisson kernel

Codex/GPT discovery track, 2026-08-25.

The current Lean workbench now proves, for real `a>1`,

\[
\operatorname{Re}\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_{p}\sum_{m\ge1}
(\log p)\,e^{-ma\log p}\cos(mt\log p),
\]

where the formal representation is a single `tsum` over `Nat.Primes × ℕ`, with `m=k+1`.

For one prime put

\[
r=p^{-a}=e^{-a\log p},\qquad \theta=t\log p.
\]

Since `a>1` and `p>1`, `0<r<1`. The geometric series gives

\[
\sum_{m\ge1} r^m e^{im\theta}
=\frac{re^{i\theta}}{1-re^{i\theta}}.
\]

Taking real parts,

\[
\sum_{m\ge1}r^m\cos(m\theta)
=\operatorname{Re}\frac{re^{i\theta}}{1-re^{i\theta}}.
\]

The already-formalized local Poisson identity is

\[
K_r(\theta)-1
=2\operatorname{Re}\frac{re^{i\theta}}{1-re^{i\theta}},
\]

therefore

\[
\boxed{
\sum_{m\ge1}p^{-am}\cos(mt\log p)
=\frac12\left[K_{p^{-a}}(t\log p)-1\right].
}
\]

Multiplying by `log p` gives the exact local tower collapse

\[
\boxed{
\sum_{m\ge1}(\log p)p^{-am}\cos(mt\log p)
=\frac12 W_{p,a}(t),
}
\]

where

\[
W_{p,a}(t)=\log p\,[K_{p^{-a}}(t\log p)-1].
\]

Thus, once absolute summability justifies converting the existing product `tsum` into an iterated prime/tower `tsum`, the global identity is

\[
\boxed{
2\operatorname{Re}\!\left[-\frac{\zeta'}{\zeta}(a+it)\right]
=\sum_p W_{p,a}(t),\qquad a>1.
}
\]

## Exact convergence estimate for the Fubini step

Absolute values obey

\[
\sum_{m\ge1}(\log p)p^{-am}|\cos(mt\log p)|
\le (\log p)\sum_{m\ge1}p^{-am}
=\frac{(\log p)p^{-a}}{1-p^{-a}}.
\]

For `a>1`, the sum over primes of the right side converges because it is precisely the positive prime-power expansion of `-ζ'(a)/ζ(a)`:

\[
\sum_p\frac{(\log p)p^{-a}}{1-p^{-a}}
=\sum_{p,m\ge1}(\log p)p^{-am}
=-\frac{\zeta'(a)}{\zeta(a)}<\infty.
\]

So the Fubini/Tonelli requirement is not an extra conjecture; it is already supplied by absolute convergence in the honest half-plane.

## Formal boundary

The remaining Lean work is now sharply localized:

1. prove summability of the product-indexed geometric-cosine function from the existing von-Mangoldt summability;
2. apply the product-tsum/Fubini theorem to write `∑' (p,k)` as `∑' p, ∑' k`;
3. prove the one-prime geometric complex series;
4. reuse `KrClosed_sub_one_eq_two_mul_re` / `WpA_eq_two_mul_re_minusLogDerivZetaP` to identify each inner `tsum`.

No continuation to `a=1/2` is used here. The result lives entirely in `a>1`.
