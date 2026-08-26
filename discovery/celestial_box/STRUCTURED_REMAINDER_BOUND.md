# Structured remainder bound for the regulated scalar box

Codex/GPT discovery track, 2026-08-26.

The explicit `C(S,U) m(1+|log m|^2)` theorem in
`REGULATOR_EXPLICIT_REMAINDER.md` is correct but unnecessarily awkward for Lean.
A better formal target keeps the dimensionless regulator variables visible until the
last corollary.

Fix

\[
S,U>0,\qquad 0<m\le \min\{S/4,U/16\},
\]

and define

\[
\rho=\frac mU,\qquad
\delta=\frac{4m}{U}=4\rho,\qquad
\eta=\frac mS.
\]

Let

\[
\ell_U=\log\frac mU,\qquad
\ell_S=\log\frac mS,
\]

and let

\[
d_a=\log a-\ell_U,
\qquad
d_t=\log t-\ell_S,
\qquad t=\frac qa-1.
\]

## 1. Scale errors

The promoted / in-progress Lean bounds give

\[
|d_a|\le A_*:=
\frac{289}{192}
\left(\eta+\frac{33}{64}\delta\right),
\]

and a deliberately coarse pole-scale estimate

\[
|d_t|\le B_*:=
\frac{103}{68}\delta
+\frac13\delta\eta
+\frac43\eta.
\]

Both are manifestly `O(m)` for fixed `S,U`.

## 2. Small special-function remainder

Using the exact endpoint decomposition

\[
F(q)-F(1)=
\log a\log t+\frac12\log^2a-\frac{\pi^2}{6}+E,
\]

with

\[
E=
-\operatorname{Li}_2^-(-t)
-\operatorname{Li}_2(aq)
-\log q\log(1-aq)
-\frac12\log^2(1-a)
-\operatorname{Li}_2^-\!\left(-\frac a{1-a}\right)
+\operatorname{Li}_2(a),
\]

the existing endpoint and series bounds imply the following clean structured estimate.

Because

\[
t\le\frac{48}{31}\eta<\frac12,
\]

\[
|\operatorname{Li}_2^-(-t)|
\le\frac{t}{1-t}
\le\frac{48}{19}\eta.
\]

Since `a<=rho<=1/16`,

\[
\left|\operatorname{Li}_2^-\!\left(-\frac a{1-a}\right)\right|
\le\frac{a}{1-2a}
\le\frac87\rho,
\]

and

\[
|\operatorname{Li}_2(a)|
\le\frac{a}{1-a}
\le\frac{16}{15}\rho.
\]

Thus their combined linear lower-endpoint contribution is

\[
\frac87\rho+\frac{16}{15}\rho
=\frac{232}{105}\rho.
\]

The already formalized product endpoint estimates give

\[
|\operatorname{Li}_2(aq)|
\le\frac{648}{289}\rho^2,
\]

\[
\frac12\log^2(1-a)
\le\frac98\rho^2,
\]

and

\[
|\log(1-aq)|
\le\frac{486}{289}\rho^2.
\]

Finally the exact moving-endpoint scale

\[
q=\rho Q,
\qquad
Q=\left(\frac{2R}{1+R}\right)^2
\]

with `8/9<=R<=1` gives the convenient coarse estimate

\[
|\log Q|\le\frac{81}{128}\delta
=\frac{81}{32}\rho.
\]

Therefore

\[
|\log q|
\le |\log\rho|+\frac{81}{32}\rho.
\]

Putting these together,

\[
\boxed{
\begin{aligned}
|E|\le E_*:={}&
\frac{48}{19}\eta
+\frac{232}{105}\rho
+\left(\frac{648}{289}+\frac98\right)\rho^2\\
&+\frac{486}{289}\rho^2
\left(|\log\rho|+\frac{81}{32}\rho\right).
\end{aligned}
}
\]

## 3. Core logarithmic assembly

Define

\[
D=\log a\log t+\frac12\log^2a-\frac{\pi^2}{6}+E,
\]

\[
D_0=\ell_U\ell_S+\frac12\ell_U^2-\frac{\pi^2}{6}.
\]

The exact identity from `scalar_box_remainder_assembly_exact.py` is

\[
D-D_0=
 d_a(\ell_S+\ell_U)
+\ell_Ud_t+d_ad_t+\frac12d_a^2+E.
\]

Hence

\[
\boxed{
|D-D_0|\le
A_*(|\ell_S|+|\ell_U|)
+|\ell_U|B_*
+A_*B_*+\frac12A_*^2+E_*.
}
\]

This is a direct triangle-inequality theorem and should be much easier for Lean than a
single expanded constant.

## 4. Prefactor assembly

The regulated integral is

\[
J(-S,-U;m)=\frac{2D}{SU\kappa}.
\]

From `1<=kappa` and `kappa-1<=delta/2`,

\[
\left|\frac1\kappa-1\right|
=\frac{\kappa-1}{\kappa}
\le\frac\delta2.
\]

Using

\[
\frac D\kappa-D_0
=\frac{D-D_0}{\kappa}
+\left(\frac1\kappa-1\right)D_0
\]

and `1/kappa<=1`,

\[
\boxed{
\left|\frac D\kappa-D_0\right|
\le
|D-D_0|+\frac\delta2|D_0|.
}
\]

Therefore

\[
\boxed{
\left|
J(-S,-U;m)-\frac{2D_0}{SU}
\right|
\le
\frac{2}{SU}
\left[
A_*(|\ell_S|+|\ell_U|)
+|\ell_U|B_*
+A_*B_*+\frac12A_*^2+E_*
+\frac\delta2|D_0|
\right].
}
\]

This is the recommended primary Lean theorem.  Every term on the right visibly tends
to zero as `m -> 0+` for fixed positive `S,U`.  The previously advertised
`C(S,U)m(1+|log m|^2)` estimate should then be a corollary, not the primary formal
statement.
