# Single off-line folded pair: exact order-two Loewner obstruction

Date: 2026-09-14
Status: exact finite algebra; zero-side diagnostic, **not a proof of RH**

## Setup

Use the safe quadratic fold

\[
t_\rho=1-(\rho-\tfrac12)^2.
\]

For a nontrivial zero candidate

\[
\rho=\frac12+\delta+i\gamma
\]

its reflection partner \(\rho^\#=1-\bar\rho\) gives

\[
t_\rho=a+ib,\qquad t_{\rho^\#}=a-ib,
\]

with

\[
a=1+\gamma^2-\delta^2>\frac34,
\qquad b=-2\delta\gamma.
\]

Because nontrivial zeta zeros are nonreal, \(\gamma\ne0\), hence

\[
b=0\iff\delta=0\iff\Re\rho=\frac12.
\]

Take one conjugate folded pair with equal positive multiplicity normalized to one. Its contribution to the safe Pick/Löwner function is

\[
\phi_{a,b}(u)
=\frac{ut}{u+t}+\frac{u\bar t}{u+\bar t}
=\frac{2u(u+a)}{(u+a)^2+b^2},
\qquad u>0.
\]

## Exact two-point Löwner determinant

For distinct \(u,v>0\), form

\[
L_{a,b}(u,v)=
\begin{pmatrix}
\phi'_{a,b}(u)&\dfrac{\phi_{a,b}(u)-\phi_{a,b}(v)}{u-v}\\[2mm]
\dfrac{\phi_{a,b}(u)-\phi_{a,b}(v)}{u-v}&\phi'_{a,b}(v)
\end{pmatrix}.
\]

Direct rational simplification gives

\[
\boxed{
\det L_{a,b}(u,v)
=-\frac{4b^2(a^2+b^2)(u-v)^2}
{\big((u+a)^2+b^2\big)^2\big((v+a)^2+b^2\big)^2}.}
\]

Therefore, for \(a>0\), \(b\ne0\), and \(u\ne v\),

\[
\boxed{\det L_{a,b}(u,v)<0.}
\]

So a single off-line reflection pair violates matrix monotonicity already at order two, for **every** pair of distinct safe positive sampling points. The obstruction vanishes exactly at \(b=0\), i.e. at the critical line in the zeta fold.

## Confluent/local form

Let \(v\to u\). The standard two-point expansion has

\[
\det L(u,u+h)
=\frac{h^2}{12}
\left(2\phi'(u)\phi'''(u)-3\phi''(u)^2\right)+O(h^3).
\]

For the conjugate pair,

\[
\boxed{
2\phi'_{a,b}(u)\phi'''_{a,b}(u)-3\phi''_{a,b}(u)^2
=-\frac{48b^2(a^2+b^2)}{\big((u+a)^2+b^2\big)^4}<0.}
\]

Equivalently, wherever \(\phi'>0\), the order-two condition is concavity of

\[
\frac1{\sqrt{\phi'(u)}};
\]

indeed

\[
\left(\phi'^{-1/2}\right)''
=-\frac{2\phi'\phi'''-3(\phi'')^2}{4(\phi')^{5/2}}.
\]

An off-line pair bends this quantity in the wrong direction everywhere.

## What this does and does not prove

This is stronger than the previous qualitative statement that a nonreal folded pole gives an indefinite reflection block. It shows that an *isolated* bad pair is detected by the smallest nontrivial Löwner test, globally in \((u,v)\).

It does **not** show that order-two positivity of the full zeta kernel is enough for RH. Additional positive-real modes and other conjugate pairs can alter the nonlinear order-two determinant, so a bad pair may in principle be masked at order two. The existing finite Cauchy congruence remains the exact general statement: with sufficiently many resolvent samples, the full finite Löwner matrix has the same inertia as the reflection metric and therefore cannot hide any negative pair.

The next useful question is whether the special arithmetic ordering/multiplicity of the folded zeta spectrum prevents such masking, or whether one can construct a zero-independent adaptive resolvent combination that isolates each conjugate pair from boundary data. The latter aligns with the existing adaptive Hardy/Hankel recovery mechanism.
