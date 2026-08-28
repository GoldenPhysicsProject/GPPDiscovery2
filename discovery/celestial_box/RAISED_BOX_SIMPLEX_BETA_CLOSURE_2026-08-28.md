# Raised-box simplex Beta closure — 2026-08-28

Codex/GPT only. No Claude work inspected.

For the Euclidean raised-box majorant, the open integrability factor is

\[
I_\delta=\int_{\substack{x_1,x_2,x_3\ge0\\x_1+x_2+x_3\le1}}
x_1^{-\delta}x_3^{-\delta}\,dx_1dx_2dx_3,
\qquad 0\le\delta<1.
\]

Integrating the spectator coordinate `x2` first gives

\[
I_\delta=\int_0^1 dx_1\,x_1^{-\delta}
\int_0^{1-x_1}dx_3\,x_3^{-\delta}(1-x_1-x_3).
\]

Set `x3=(1-x1)t`.  The inner integral is

\[
(1-x_1)^{2-\delta}B(1-\delta,2).
\]

Therefore

\[
I_\delta=B(1-\delta,2)B(1-\delta,3-\delta).
\]

Using `B(a,b)=Gamma(a)Gamma(b)/Gamma(a+b)`, the intermediate `Gamma(3-delta)` cancels exactly:

\[
I_\delta
=\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)}.
\]

At `delta=0`,

\[
I_0=\frac1{\Gamma(4)}=\frac16,
\]

the affine 3-simplex volume.  The endpoint singularities are integrable precisely for `delta<1`; this is the correct analytic domain needed by the existing pointwise majorant theorem.

Executable symbolic check: `discovery/celestial_box/raised_box_simplex_beta.py` (`sympy.expand_func` followed by exact simplification returns zero for the difference between the two-Beta product and the Gamma quotient, and returns `1/6` at `delta=0`).

## Status

This closes the exact analytic reduction of the majorant integral at discovery level.  It does **not** yet constitute the Lean measure-theoretic theorem or the full dominated-convergence proof.  The remaining formal layer is:

1. represent the affine 3-simplex as nested interval integrals;
2. invoke/prove the two scaled Beta integral identities on `0 <= delta < 1`;
3. transport the exact Gamma quotient into an `Integrable` certificate for the existing raised-box majorant;
4. apply dominated convergence to the raised-box dimensional regulator and recover the `1/6` limit.

No claim about the honest Yang-Mills vector numerator is advanced here; that remains a separate next amplitudes frontier after the scalar raised-box residue layer is formalized.
