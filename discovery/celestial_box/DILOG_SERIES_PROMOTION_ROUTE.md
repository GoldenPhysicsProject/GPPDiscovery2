# Direct dilogarithm-series route for the scalar-box remainder

Codex/GPT discovery track, 2026-08-25.

The regulated scalar-box remainder uses only small real dilogarithm arguments after the exact endpoint transformations have been made. Mathlib v4.19.0 does not provide a ready-made `Li_2` API suitable for the proof, but the required local estimate can be built directly from the defining power series.

For `|x|<1`, define

\[
\operatorname{Li}_{2,\mathrm{ser}}(x)
:=\sum_{n=0}^{\infty}\frac{x^{n+1}}{(n+1)^2}.
\]

Absolute convergence follows immediately from

\[
\left|\frac{x^{n+1}}{(n+1)^2}\right|
\le |x|^{n+1}
\]

and the geometric series. Therefore

\[
\begin{aligned}
|\operatorname{Li}_{2,\mathrm{ser}}(x)|
&\le \sum_{n=0}^{\infty}\frac{|x|^{n+1}}{(n+1)^2}\\
&\le \sum_{n=0}^{\infty}|x|^{n+1}\\
&=\frac{|x|}{1-|x|}.
\end{aligned}
\]

Hence the exact bound needed in `REGULATOR_EXPLICIT_REMAINDER.md` is available without any special-function library:

\[
\boxed{
|\operatorname{Li}_{2,\mathrm{ser}}(x)|\le\frac{|x|}{1-|x|},
\qquad |x|<1.
}
\]

In particular, for `0<=x<1`,

\[
|\operatorname{Li}_{2,\mathrm{ser}}(\pm x)|\le\frac{x}{1-x}.
\]

## Formalization decomposition

The regulator proof can therefore be separated into two logically different layers:

1. **Local series layer**: define `Li2Series`, prove absolute convergence and the geometric majorant above. This is elementary and should be Lean-friendly.
2. **Functional-equation layer**: prove the real Spence identity and the inversion identity on precisely the domains used by the scalar-box endpoints. These are still genuine analytic work; the local series estimate does not replace them.

This removes the earlier statement that the complete regulator promotion is blocked merely because Mathlib has no built-in dilogarithm. The missing built-in API can be bypassed. The remaining hard content is the functional equations plus their domain/branch bookkeeping.
