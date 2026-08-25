# Real-integral route to the scalar-box Spence identity

Codex/GPT discovery track, 2026-08-25.

The local power-series layer is now certified and supplies all small-argument bounds needed after endpoint transformations.  The remaining functional-equation layer can be separated into a purely real Spence theorem and a later inversion theorem.

For `0 < x < 1`, use the real integral representation

\[
L_2(x):=-\int_0^x \frac{\log(1-t)}{t}\,dt.
\]

The integrand has a removable singularity at `t=0`, since

\[
-\frac{\log(1-t)}{t}\to 1.
\]

Hence `L_2` is differentiable on `(0,1)` with

\[
L_2'(x)=-\frac{\log(1-x)}{x}.
\]

Define

\[
F(x)=L_2(x)+L_2(1-x)+\log x\log(1-x).
\]

For `0<x<1`, direct differentiation gives

\[
\begin{aligned}
F'(x)
&=-\frac{\log(1-x)}x
 +\frac{\log x}{1-x}
 +\frac{\log(1-x)}x
 -\frac{\log x}{1-x}\\
&=0.
\end{aligned}
\]

Therefore `F` is constant on `(0,1)`.  Evaluating at `x=1/2` or taking the endpoint limit gives

\[
\boxed{
L_2(x)+L_2(1-x)=\frac{\pi^2}{6}-\log x\log(1-x),
\qquad 0<x<1.
}
\]

For formalization the clean decomposition is:

1. define the removable real kernel at `0`;
2. prove interval integrability and the fundamental-theorem derivative of `L_2` on `(0,1)`;
3. prove `F'=0` and hence constancy on each connected interval;
4. identify the constant using the already-available zeta value `\zeta(2)=\pi^2/6`, together with equality of the integral and power-series definitions on `|x|<1`;
5. only after real Spence is closed, formalize the negative/reciprocal inversion identity required by the remaining endpoint transformation.

This route avoids complex logarithm branch bookkeeping for Spence entirely.  Branch control is confined to the inversion layer, where it is genuinely unavoidable.
