# Raised-box simplex majorant: exact Beta reduction

Codex/GPT continuation, 2026-08-28. No Claude material consulted.

## Target

For `0 < δ < 1`, the majorant required by the raised-box dominated-convergence proof is

\[
(x_1x_3)^{-\delta}
\]

on the standard 3-simplex. In affine coordinates `x4 = 1-x1-x2-x3`, its integral is

\[
I_\delta
=\int_{x_1,x_2,x_3\ge0\atop x_1+x_2+x_3\le1}
 x_1^{-\delta}x_3^{-\delta}\,dx_1dx_2dx_3.
\]

Since the integrand is independent of `x2`, integrate `x2` first:

\[
I_\delta
=\int_0^1 x_1^{-\delta}
  \int_0^{1-x_1} x_3^{-\delta}(1-x_1-x_3)\,dx_3\,dx_1.
\]

For fixed `x1`, substitute `x3=(1-x1)y`. Then

\[
\int_0^{1-x_1}x_3^{-\delta}(1-x_1-x_3)\,dx_3
=(1-x_1)^{2-\delta}B(1-\delta,2).
\]

Therefore

\[
I_\delta
=B(1-\delta,2)
  \int_0^1x_1^{-\delta}(1-x_1)^{2-\delta}\,dx_1
=B(1-\delta,2)B(1-\delta,3-\delta).
\]

Using `B(a,b)=Γ(a)Γ(b)/Γ(a+b)`, the middle Gamma factors cancel:

\[
B(1-\delta,2)B(1-\delta,3-\delta)
=\frac{Γ(1-\delta)Γ(2)}{Γ(3-\delta)}
 \frac{Γ(1-\delta)Γ(3-\delta)}{Γ(4-2\delta)}
=\boxed{\frac{Γ(1-\delta)^2}{Γ(4-2\delta)}}.
\]

`Γ(2)=1`. Positivity of `1-δ`, `2`, and `3-δ` gives convergence of both Beta integrals directly.

## Lean route

Mathlib already provides in `Mathlib.Analysis.SpecialFunctions.Gamma.Beta`:

- `Complex.betaIntegral`
- `Complex.betaIntegral_scaled`
- `Complex.betaIntegral_convergent`
- `Complex.betaIntegral_eq_Gamma_mul_div`

So the efficient formalization path is not a new multidimensional Dirichlet theorem. It is:

1. encode the affine 3-simplex as nested interval integrals;
2. integrate the `x2` coordinate, producing `1-x1-x3`;
3. use `betaIntegral_scaled` for the `x3` integral;
4. identify the `x1` integral with a second Beta integral;
5. collapse the Beta product with `betaIntegral_eq_Gamma_mul_div` and Gamma nonvanishing for positive real part;
6. combine with the already-formal pointwise limit and majorant to invoke dominated convergence.

This yields the exact remaining analytic input

\[
J(\epsilon)\to \operatorname{vol}(\Delta_3)=1/6,
\]

which feeds the already-certified Gamma residue `ε Γ(ε) -> 1` and dimension-shift assembly, hence the scalar `mu^4` rational coefficient `-1/6`.

## Boundary

This note does **not** claim the multidimensional integral is already Lean-certified. The new result is the exact two-Beta reduction and a concrete Mathlib-compatible formalization route. The remaining proof-engineering work is the nested interval-integral representation and real/complex power coercions.
