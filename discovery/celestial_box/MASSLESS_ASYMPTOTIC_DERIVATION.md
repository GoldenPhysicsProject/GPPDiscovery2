# Analytic derivation of the regulated scalar-box massless asymptotic

We start from the exact reduced fixed-`u` dispersion integral

\[
J(-S,-U;m)=\frac{8}{SU}\int_0^R\frac{\operatorname{atanh}r}{1-\kappa^2r^2}\,dr,
\]

with

\[
R^2=\frac{U}{U+4m},\qquad
\kappa^2=\frac{S(U+4m)-4m^2}{SU},\qquad S,U,m>0.
\]

Here `m` is the common mass-squared regulator.

## 1. Endpoint/pole variables

Set

\[
x=\frac{1-r}{1+r},\qquad
q=\frac{1-R}{1+R},\qquad
a=\frac{\kappa-1}{\kappa+1}.
\]

Then

\[
r=\frac{1-x}{1+x},\qquad
\operatorname{atanh}r=-\frac12\log x,
\]

and

\[
1-\kappa^2r^2
=\frac{(1+\kappa)^2(x-a)(1-ax)}{(1+x)^2}.
\]

Therefore

\[
I:=\int_0^R\frac{\operatorname{atanh}r}{1-\kappa^2r^2}\,dr
=\frac1{4\kappa}\int_1^q\log x\left(\frac1{x-a}+\frac{a}{1-ax}\right)dx.
\]

The exact primitive can be taken as

\[
F(x)=\log a\,\log\!\left(\frac xa-1\right)
-\operatorname{Li}_2\!\left(1-\frac xa\right)
+\operatorname{Li}_2(1-ax)
+\log a\,\log(1-ax),
\]

so that

\[
I=\frac{F(q)-F(1)}{4\kappa}.
\]

All arguments are real on the physical interval because `0<a<q<1` for sufficiently small positive `m`.

## 2. Two regulator scales

The endpoint and pole approach one another at parametrically different orders. Expanding the exact definitions gives

\[
a=\frac mU+O(m^2),\qquad
q=\frac mU+O(m^2),
\]

but

\[
\frac qa-1=\frac mS+O(m^2).
\]

Equivalently,

\[
\log a=\log\frac mU+o(1),\qquad
\log\left(\frac qa-1\right)=\log\frac mS+o(1),
\]

with the errors small enough that their products with `log m` vanish (`m log m -> 0`). This is the origin of the two logarithmic scales: the endpoint displacement is `O(m)`, while the pole-endpoint separation is `O(m^2)` in the original `r` coordinate.

## 3. Endpoint value

Since `q/a-1 -> 0`, `aq -> 0`, and `a -> 0`,

\[
-\operatorname{Li}_2\!\left(1-\frac qa\right)=o(1),
\qquad
\operatorname{Li}_2(1-aq)=\frac{\pi^2}{6}+o(1),
\qquad
\log a\,\log(1-aq)=o(1).
\]

Hence

\[
F(q)=\log a\,\log\left(\frac qa-1\right)+\frac{\pi^2}{6}+o(1).
\]

## 4. Lower-limit value

At `x=1`,

\[
F(1)=\log a\left[2\log(1-a)-\log a\right]
-\operatorname{Li}_2\left(1-\frac1a\right)
+\operatorname{Li}_2(1-a).
\]

Use the real dilogarithm inversion identity, for `y>0`,

\[
\operatorname{Li}_2(-y)+\operatorname{Li}_2(-1/y)
=-\frac{\pi^2}{6}-\frac12\log^2 y,
\]

with `y=(1-a)/a`. Since `Li_2(-1/y)=o(1)` and `Li_2(1-a)=pi^2/6+o(1)`, one obtains

\[
F(1)=-\frac12\log^2 a+\frac{\pi^2}{3}+o(1).
\]

Therefore

\[
F(q)-F(1)
=\log a\,\log\left(\frac qa-1\right)
+\frac12\log^2a
-\frac{\pi^2}{6}+o(1).
\]

Since `kappa -> 1`,

\[
I=
\frac14\left[
\log a\,\log\left(\frac qa-1\right)
+\frac12\log^2a
-\frac{\pi^2}{6}
\right]+o(1).
\]

Finally, multiplying by `8/(SU)` and inserting the scale limits gives

\[
\boxed{
J(-S,-U;m)
=\frac{2\log(S/m)\log(U/m)+\log^2(U/m)-\pi^2/3}{SU}+o(1)
}
\]

as `m -> 0+` for fixed `S,U>0`.

In particular,

\[
J(-S,-U;m)
=\frac{3}{SU}\log^2\frac1m
+\frac{2\log S+4\log U}{SU}\log\frac1m
+O(1).
\]

## Status and remaining rigor boundary

The asymptotic mechanism and constant term are analytically derived from the exact primitive. For publication-grade rigor, the remaining task is to replace the displayed `O(m^2)` expansions and `o(1)` dilogarithm statements by explicit inequalities uniform on `0<m<m_0(S,U)`. No symmetry in `S,U` is asserted: this is the fixed-`u` representation and is intrinsically asymmetric in the chosen variables.
