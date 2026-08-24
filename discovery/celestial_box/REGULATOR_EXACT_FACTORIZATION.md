# Exact regulator factorization for the scalar box

For fixed `S,U>0` and regulator `m>0`, define

\[
R^2=\frac{U}{U+4m},\qquad
\kappa^2=1+\frac{4m}{U}-\frac{4m^2}{SU},
\]
\[
q=\frac{1-R}{1+R},\qquad
a=\frac{\kappa-1}{\kappa+1}.
\]

The endpoint/pole geometry admits exact factorizations that are stronger than the previously used formal Taylor series.

First,

\[
q=\frac{4m}{U\bigl(\sqrt{1+4m/U}+1\bigr)^2},
\]

and

\[
a=\frac{4m(S-m)}{SU(1+\kappa)^2}.
\]

More importantly,

\[
q-a=\frac{2(1-\kappa R)}{(1+R)(1+\kappa)}.
\]

Since

\[
(\kappa R)^2
=1-\frac{4m^2}{S(U+4m)},
\]

one gets the exact `m^2` factor

\[
\boxed{
q-a=
\frac{8m^2}
{S(U+4m)(1+\kappa R)(1+R)(1+\kappa)}
}.
\]

Dividing by the exact formula for `a` yields

\[
\boxed{
\frac qa-1=
\frac{2mU(1+\kappa)}
{(U+4m)(1+\kappa R)(1+R)(S-m)}
}.
\]

Equivalently,

\[
\frac{q/a-1}{m/S}
=
\frac{2SU(1+\kappa)}
{(U+4m)(1+\kappa R)(1+R)(S-m)}
\longrightarrow 1.
\]

Thus the two logarithmic scales are now exposed by exact identities rather than asymptotic fitting:

\[
a=\frac mU\,[1+O(m)],\qquad
\frac qa-1=\frac mS\,[1+O(m)],
\]

while the raw endpoint-pole distance is exactly `m^2` times a positive smooth factor.

For publication-grade remainder control it is enough to choose

\[
0<m<m_0:=\min\{S/2,U/8\},
\]

so every denominator above stays uniformly away from zero and the multiplicative ratios are trapped in a compact positive interval. Then the elementary inequalities

\[
|\log(1+x)|\le 2|x|\quad (|x|\le 1/2),
\]

and, for `0<x<=1/2`,

\[
|\operatorname{Li}_2(-x)|\le x,
\]
\[
\left|\operatorname{Li}_2(1-x)-\frac{\pi^2}{6}\right|
\le 2x\bigl(1+|\log x|\bigr)
\]

reduce every previously informal `o(1)` term in the exact primitive to `O(m|log m|)`. The last dilogarithm estimate follows from

\[
\operatorname{Li}_2(1-x)=\frac{\pi^2}{6}-\operatorname{Li}_2(x)-\log x\log(1-x)
\]

plus `Li_2(x)<=x/(1-x)` and `|log(1-x)|<=x/(1-x)`.

This supplies the clean route to the controlled theorem

\[
J(-S,-U;m)=
\frac{2\log(S/m)\log(U/m)+\log^2(U/m)-\pi^2/3}{SU}
+O_{S,U}(m|\log m|^2),
\]

where the displayed error rate is a conservative target: the exact factorization already shows the dominant logarithmic perturbations are `O(m|log m|)`, while multiplication by `1/\kappa-1=O(m)` against the leading `log^2 m` term contributes `O(m|log m|^2)`. The constant in the big-O has not yet been made explicit in Lean or interval arithmetic.

Status: exact algebraic factorization is verified by `regulator_exact_factorization.py`; the final uniform analytic error bound remains to be written as a theorem with explicit constants before promotion to GPPVerify2.
