# Raised-box full one-channel majorant mass

## Status

Exact analytic reduction plus executable numerical cross-check. This note does not claim that the concrete Lean dominated-convergence theorem has been completed.

## Setup

For the concrete raised-box moment with Euclidean `S,T>0`, the existing one-channel estimate is

\[
Q^{-\varepsilon}\le 1+(Sx_1x_3)^{-\delta},\qquad
0\le\varepsilon\le\delta,\quad 0<\delta<1,
\]

on the affine simplex

\[
0\le x_1\le1,\quad
0\le x_2\le1-x_1,\quad
0\le x_3\le1-x_1-x_2.
\]

The constant term has simplex mass `1/6`. The singular term can be integrated exactly.

## Exact reduction

For fixed `x1,x2`,

\[
\int_0^{1-x_1-x_2}(Sx_1x_3)^{-\delta}\,dx_3
=(Sx_1)^{-\delta}\frac{(1-x_1-x_2)^{1-\delta}}{1-\delta}.
\]

The next affine slice gives

\[
\int_0^{1-x_1}(1-x_1-x_2)^{1-\delta}\,dx_2
=\frac{(1-x_1)^{2-\delta}}{2-\delta}.
\]

Hence the singular mass is

\[
\frac{S^{-\delta}}{(1-\delta)(2-\delta)}
\int_0^1 x^{-\delta}(1-x)^{2-\delta}\,dx.
\]

The remaining integral is

\[
B(1-\delta,3-\delta)
=\frac{\Gamma(1-\delta)\Gamma(3-\delta)}{\Gamma(4-2\delta)}.
\]

Using

\[
\Gamma(3-\delta)=(2-\delta)(1-\delta)\Gamma(1-\delta),
\]

the complete singular mass collapses to

\[
S^{-\delta}\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)}.
\]

Therefore the full one-channel DCT majorant has explicit finite mass

\[
\boxed{
\mathcal M_\delta(S)
=\frac16
+S^{-\delta}\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)}
},\qquad S>0,\;0<\delta<1.
\]

This is the real DCT mass corresponding to the Gamma ratio already certified on the auxiliary nested Beta/Gamma side. It makes the remaining formal task sharper: the Lean proof no longer needs to discover an integrable majorant or its finite value; it needs to assemble the existing real slice integrability/inequalities into the nested affine-simplex measure statement, remove boundary faces almost everywhere, and invoke DCT.

## Endpoint behavior

The formula also exposes why the physical condition `delta<1` is sharp for this one-channel bound. As `delta -> 1-`, `Gamma(1-delta)^2` diverges quadratically, so this particular majorant loses finite mass at the endpoint. Nothing in this argument permits `delta=1`.

## Executable check

`discovery/raised_box_full_majorant_mass.py` compares the boxed formula against the independently reduced real outer integral. It uses

\[
x=t^{1/(1-\delta)},
\]

so that

\[
x^{-\delta}\,dx=\frac{dt}{1-\delta},
\]

which removes the singular endpoint from numerical quadrature. Local high-precision checks agreed at the working precision for `delta=0.2,0.7,0.95,0.99`, including the near-endpoint case.

## Promotion boundary

Do not promote the boxed formula as a substitute for the missing concrete DCT theorem. The existing Lean chain already contains:

- concrete pointwise interior convergence of the physical integrand;
- the one-channel majorant inequality;
- inner-channel interval integrability and its exact integral;
- the middle affine integral;
- outer-kernel nonnegativity and domination by `x^(-delta)`;
- the complex Beta/Gamma exact evaluation;
- the zero-regulator simplex volume `1/6`.

The next Verify2 target is the real nested `L1`/Fubini-Tonelli assembly plus AE boundary disposal, followed by `simplexMoment epsilon S T -> 1/6` as `epsilon -> 0+`.

## Other-front boundary check

No change in this run to the honest physical boundary: Yang-Mills/gravity still requires the fixed-loop-momentum nonzero-`mu` tree sewing numerator after scalar regulator closure. Likewise the all-order prime-Hankel positivity and Gamma/Mehler-Fock chamber hierarchy remain exact finite/arithmetic or real-axis results; they do not supply the missing global Weil quadratic-form identification or RH positivity theorem.
