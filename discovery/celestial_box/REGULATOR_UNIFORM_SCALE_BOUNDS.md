# Uniform regulator-scale bounds for the scalar box

Fix `S,U>0` and impose the concrete small-regulator domain

\[
0<m\le m_0:=\min\{S/4,U/16\}.
\]

Introduce the dimensionless parameters

\[
\delta=\frac{4m}{U},\qquad \eta=\frac{m}{S},
\]

so `0<δ<=1/4` and `0<η<=1/4`.  With

\[
R^2=\frac1{1+\delta},\qquad
\kappa^2=1+\delta(1-\eta),
\]

one has the elementary rational bounds

\[
1\le\kappa\le\frac98,\qquad
\frac89\le R\le1,
\]

and, using

\[
(\kappa R)^2=1-\frac{\delta\eta}{1+\delta},
\]

also

\[
\frac{15}{16}\le\kappa R\le1.
\]

These bounds are deliberately slightly weaker than the sharp square-root constants; the rational values make subsequent interval estimates simple.

## Multiplicative scale errors

Write

\[
a=\frac mU A,\qquad q=\frac mU Q,
\]

where the exact factorizations give

\[
A=\frac{4(1-\eta)}{(1+\kappa)^2},\qquad
Q=\frac4{(1+\sqrt{1+\delta})^2}.
\]

Then

\[
\frac{192}{289}\le A\le1,
\qquad
\frac{256}{289}\le Q\le1.
\]

Let `e=κ-1`.  Rationalization gives `0<=e<=δ/2`.  Hence

\[
0\le1-A
=\frac{4\eta+4e+e^2}{(1+\kappa)^2}
\le \eta+\frac{33}{64}\delta.
\]

Likewise, if `r=sqrt(1+δ)-1`, then `0<=r<=δ/2` and

\[
Q=\frac1{1+r+r^2/4},
\]

so

\[
0\le1-Q\le\frac{33}{64}\delta.
\]

Using `-log x <= (1-x)/x` for `0<x<=1` gives explicit logarithmic errors:

\[
\boxed{
\left|\log a-\log\frac mU\right|
\le
\frac{289}{192}\left(\eta+\frac{33}{64}\delta\right)
}
\]

and

\[
\boxed{
\left|\log q-\log\frac mU\right|
\le
\frac{289}{256}\frac{33}{64}\delta.
}
\]

## Pole-endpoint ratio

Define

\[
B:=\frac{q/a-1}{m/S}.
\]

The exact factorization from `REGULATOR_EXACT_FACTORIZATION.md` becomes

\[
B=
\frac{2(1+\kappa)}
{(1+\delta)(1+\kappa R)(1+R)(1-\eta)}.
\]

Set

\[
N=\frac{1+\kappa}{2},\quad
D_2=\frac{1+\kappa R}{2},\quad
D_3=\frac{1+R}{2}.
\]

Then `B=N/[(1+δ)D_2D_3(1-η)]`.  The rationalizations

\[
0\le\kappa-1\le\frac\delta2,
\qquad
0\le1-R\le\frac\delta2,
\]

and

\[
0\le1-\kappa R
\le\frac{16}{31}\delta\eta
\]

therefore give

\[
\boxed{
|\log B|
\le
\frac{91}{60}\delta
+\frac{16}{61}\delta\eta
+\frac43\eta.
}
\]

Consequently

\[
\boxed{
\left|\log\left(\frac qa-1\right)-\log\frac mS\right|
\le
\frac{91}{60}\delta
+\frac{16}{61}\delta\eta
+\frac43\eta.
}
\]

A coarse direct bound, useful for the endpoint dilogarithm, is

\[
0<B\le\frac{48}{31},
\qquad
0<\frac qa-1\le\frac{12}{31}<\frac12.
\]

Also `0<a<=m/U<=1/16` and `0<q<=m/U<=1/16`, so `aq<=1/256`. Thus every small dilogarithm argument appearing in the exact primitive lies uniformly inside the elementary `x<=1/2` regime.

## Consequence for the remaining regulator proof

The two logarithmic replacements are now quantitatively controlled:

\[
\log a=\log(m/U)+O(\delta+\eta),
\qquad
\log(q/a-1)=\log(m/S)+O(\delta+\eta),
\]

with the displayed constants above.  Since `|1/κ-1|<=δ/2`, multiplying the leading `log^2 m` term by the prefactor `1/κ` contributes at most `O(δ |log m|^2)`.  The remaining dilogarithm terms are uniformly controlled by `q/a-1<1/2`, `a<1/2`, and `aq<1/2`, using the elementary inequalities already recorded in `REGULATOR_EXACT_FACTORIZATION.md`.

This removes the previously informal logarithmic-scale `O(m^2)` substitutions from the massless asymptotic derivation.  The only remaining publication-grade step is to collect the endpoint and lower-limit dilogarithm estimates into one explicit bound for `F(q)-F(1)`, and then combine it with the prefactor estimate to state a single constant `C(S,U)` in

\[
|J-J_{\rm asymp}|\le C(S,U)m(1+|\log m|^2).
\]

Status: exact inequalities derived analytically; this file is discovery documentation pending formal Lean/interval promotion of the complete remainder theorem.
