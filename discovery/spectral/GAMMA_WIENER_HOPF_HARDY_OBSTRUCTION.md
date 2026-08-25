# Gamma Wiener--Hopf ratio: exact Hardy-space obstruction

Codex/GPT discovery track, 2026-08-25.

For the normalized half-Gamma factors

\[
H_+(z)=\frac{\Gamma\!\left(\frac12-\frac{i z}{2\pi}\right)^2}{\pi},
\qquad
H_-(z)=\frac{\Gamma\!\left(\frac12+\frac{i z}{2\pi}\right)^2}{\pi},
\]

the real-axis factorization already formalized in Lean is

\[
H_+(k)H_-(k)=\operatorname{sech}^2(k/2),\qquad k\in\mathbb R.
\]

The pole lattices are

\[
H_+:\ z=-i\pi(2n+1),\qquad
H_-:\ z=+i\pi(2n+1),\qquad n\ge0,
\]
with double poles. Hence

\[
B(z):=\frac{H_+(z)}{H_-(z)}
\]

is holomorphic in the open upper half-plane: `H_+` has no poles there and `1/H_-` is entire with double zeros at `i pi(2n+1)`. On the real axis,

\[
H_-(k)=\overline{H_+(k)},
\qquad |B(k)|=1.
\]

It is tempting to call `B` an upper-half-plane inner function. That is false.

## 1. Stirling growth

Set `z=x+i y` with fixed `y>0`. Then

\[
\frac12-\frac{i z}{2\pi}
=\frac12+\frac{y}{2\pi}-i\frac{x}{2\pi},
\]

and

\[
\frac12+\frac{i z}{2\pi}
=\frac12-\frac{y}{2\pi}+i\frac{x}{2\pi}.
\]

For fixed real `sigma`, Stirling on vertical lines gives

\[
|\Gamma(\sigma+i t)|
\sim \sqrt{2\pi}\,|t|^{\sigma-1/2}e^{-\pi |t|/2}.
\]

The exponential factors cancel in the quotient, while the power factors do not. Therefore

\[
\left|
\frac{\Gamma(\frac12+\frac{y}{2\pi}-i\frac{x}{2\pi})}
     {\Gamma(\frac12-\frac{y}{2\pi}+i\frac{x}{2\pi})}
\right|
\sim
\left|\frac{x}{2\pi}\right|^{y/\pi},
\]

and after squaring,

\[
\boxed{
|B(x+i y)|
\sim
\left|\frac{x}{2\pi}\right|^{2y/\pi}
}
\qquad (|x|\to\infty,\ y>0\ \text{fixed}).
\]

Thus `B` is unbounded on every horizontal line in the upper half-plane with `y>0` and is not an `H^infty` inner function, despite its unimodular boundary values and upper-half-plane analyticity.

## 2. Stronger obstruction: the zero divisor violates the Blaschke condition

The zeros of `B` in the upper half-plane are exactly

\[
z_n=i\pi(2n+1),\qquad n\ge0,
\]

with multiplicity two. Zeros of any nonzero bounded analytic function on the upper half-plane must satisfy the half-plane Blaschke condition

\[
\sum_n \frac{\operatorname{Im} z_n}{1+|z_n|^2}<\infty.
\]

Here

\[
\frac{\operatorname{Im} z_n}{1+|z_n|^2}
=
\frac{\pi(2n+1)}{1+\pi^2(2n+1)^2}
\sim \frac{1}{2\pi n},
\]

so

\[
\boxed{
\sum_{n\ge0}
\frac{\operatorname{Im} z_n}{1+|z_n|^2}=\infty.
}
\]

Therefore the obstruction is not merely the particular Stirling normalization of the raw Gamma quotient. No bounded nonzero analytic function on the upper half-plane can have this same zero divisor.

In particular, multiplying `B` by a zero-free analytic outer/exponential factor cannot turn it into an `H^infty` inner function while preserving the zeros: a zero-free multiplier leaves the divergent zero divisor unchanged.

## Consequence for Wiener--Hopf/scattering language

The exact real-axis Gamma factorization remains correct. What fails is the stronger Hardy-inner interpretation of the scattering ratio `B`. If one wants an `H^infty` inner object, the zero structure itself must be modified/cancelled; a mere zero-free growth renormalization is insufficient.

For the integer convolution chamber `m`, the same obstruction is amplified:

\[
|B(x+i y)^m|\sim |x/(2\pi)|^{2my/\pi},
\]

and every zero acquires multiplicity `2m`, so the Blaschke divergence persists.

This is a genuine negative structural result: the missing Hardy-space step cannot be obtained as a routine normalization of the exact Gamma reflection factorization.
