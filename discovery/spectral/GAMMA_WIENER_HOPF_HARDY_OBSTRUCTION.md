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

It is tempting to call `B` an upper-half-plane inner function. That is false without an additional normalization.

## Stirling growth

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

Thus `B` is unbounded in every horizontal line of the upper half-plane with `y>0` and is not an `H^infty` inner function, despite its unimodular boundary values and its upper-half-plane analyticity.

## Consequence for canonical Wiener--Hopf factorization

The exact real-axis Gamma factorization remains correct. What fails is the stronger identification of the raw quotient with a canonical Hardy/inner scattering factor. A further analytic renormalization must remove the Stirling power growth before an inner/outer factorization can be claimed.

For the integer convolution chamber `m`, the obstruction scales linearly in `m`:

\[
|B(z)^m|\sim |x/(2\pi)|^{2my/\pi}.
\]

This is a useful negative result: the missing Hardy-space step is genuine analytic content rather than a routine corollary of the Gamma reflection identity.
