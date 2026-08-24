# Explicit remainder theorem for the regulated scalar box

Fix `S,U>0` and

\[
0<m\le m_0:=\min\{S/4,U/16\}.
\]

Use the exact variables

\[
R^2=\frac{U}{U+4m},\qquad
\kappa^2=\frac{S(U+4m)-4m^2}{SU},\qquad
q=\frac{1-R}{1+R},\qquad
a=\frac{\kappa-1}{\kappa+1},
\]

and set

\[
t:=\frac qa-1,\qquad z:=aq.
\]

The exact primitive from `MASSLESS_ASYMPTOTIC_DERIVATION.md` gives

\[
J(-S,-U;m)=\frac{2}{SU\kappa}\,[F(q)-F(1)].
\]

## 1. Exact cancellation identities

Let `\ell_a=\log a` and `c=\log(1-a)`.  Applying the real dilogarithm inversion identity at the lower endpoint and then Euler's Spence identity

\[
\operatorname{Li}_2(a)+\operatorname{Li}_2(1-a)
=\frac{\pi^2}{6}-\log a\log(1-a)
\]

gives the exact simplification

\[
\boxed{
F(1)=
-\frac12\ell_a^2+\frac{\pi^2}{3}
+\frac12c^2
+\operatorname{Li}_2\!\left(-\frac{a}{1-a}\right)
-\operatorname{Li}_2(a)
}.
\]

Thus the apparent lower-endpoint term `\log a\log(1-a)` cancels exactly.

At the moving endpoint, applying the same Spence identity to `\operatorname{Li}_2(1-z)` gives

\[
\boxed{
F(q)=
\ell_a\log t+\frac{\pi^2}{6}
-\operatorname{Li}_2(-t)
-\operatorname{Li}_2(z)
-\log q\log(1-z)
}.
\]

Therefore

\[
F(q)-F(1)
=\ell_a\log t+\frac12\ell_a^2-\frac{\pi^2}{6}+E,
\]

where

\[
E=E_q-E_1,
\]

\[
E_q=-\operatorname{Li}_2(-t)-\operatorname{Li}_2(z)-\log q\log(1-z),
\]

\[
E_1=\frac12\log^2(1-a)
+\operatorname{Li}_2\!\left(-\frac{a}{1-a}\right)
-\operatorname{Li}_2(a).
\]

This exact decomposition is the key analytic closure: every term in `E` has a uniformly small argument.

## 2. Uniform elementary bounds

Put

\[
\delta=\frac{4m}{U},\qquad \eta=\frac mS.
\]

From `REGULATOR_UNIFORM_SCALE_BOUNDS.md`,

\[
0<a,q\le\frac1{16},\qquad
0<t\le\frac{12}{31},\qquad
0<z=aq\le\frac1{256},
\]

and in fact

\[
t\le\frac{48}{31}\eta.
\]

For `0\le x<1`, the power series immediately gives

\[
|\operatorname{Li}_2(\pm x)|\le \frac{x}{1-x},
\qquad
|\log(1-x)|\le\frac{x}{1-x}.
\]

Hence

\[
|\operatorname{Li}_2(-t)|\le\frac{48}{19}\eta,
\]

\[
|\operatorname{Li}_2(z)|\le\frac{16}{255}\delta^2,
\]

and, with

\[
L:=|\log m|,\qquad u:=|\log U|,\qquad c_q:=\log\frac{289}{256},
\]

\[
|\log q\log(1-z)|
\le
\frac{16}{255}\delta^2(L+u+c_q).
\]

For the lower endpoint,

\[
|\log(1-a)|\le\frac{4}{15}\delta,
\]

so

\[
\frac12\log^2(1-a)\le\frac{8}{225}\delta^2,
\]

while

\[
\left|\operatorname{Li}_2\!\left(-\frac a{1-a}\right)\right|
\le\frac{2}{7}\delta,
\qquad
|\operatorname{Li}_2(a)|\le\frac{4}{15}\delta.
\]

Using `\delta\le1/4`, hence `\delta^2\le m/U`, one obtains

\[
|E|\le m\,C_E(S,U)(1+L^2),
\]

with the explicit admissible constant

\[
\boxed{
C_E(S,U)=
\frac{48}{19S}
+\frac1U\left(
\frac{16}{255}
+\frac{232}{105}
+\frac{8}{225}
+\frac{16}{255}\left(u+c_q+\frac12\right)
\right).
}
\]

Here we used `L\le(1+L^2)/2`.

## 3. Logarithmic scale replacement

Define

\[
\ell_U:=\log\frac mU,\qquad
\ell_S:=\log\frac mS.
\]

The already-proved scale bounds give

\[
|\ell_a-\ell_U|\le mA_1,
\]

with

\[
\boxed{
A_1=\frac{289}{192}
\left(\frac1S+\frac{33}{16U}\right),
}
\]

and

\[
|\log t-\ell_S|\le mB_1,
\]

where, using `m\le U/16` to reduce the mixed `\delta\eta` term,

\[
\boxed{
B_1=
\frac{91}{15U}
+\left(\frac4{61}+\frac43\right)\frac1S.
}
\]

Let

\[
s:=|\log S|,\qquad u:=|\log U|.
\]

Then

\[
\left|
\ell_a\log t+\frac12\ell_a^2
-\left(\ell_U\ell_S+\frac12\ell_U^2\right)
\right|
\le
m\,[K_1+m_0K_2](1+L^2),
\]

where one admissible choice is

\[
\boxed{
K_1=A_1(s+u+1)+B_1\left(u+\frac12\right),
\qquad
K_2=A_1B_1+\frac12A_1^2.
}
\]

## 4. Prefactor

Because `1\le\kappa` and `\kappa-1\le\delta/2`,

\[
\left|\frac1\kappa-1\right|\le\frac{2m}{U}.
\]

Set

\[
D_0:=
\ell_U\ell_S+\frac12\ell_U^2-\frac{\pi^2}{6}.
\]

Then

\[
|D_0|\le K_0(S,U)(1+L^2),
\]

with

\[
\boxed{
K_0=
\frac32+\frac{s+2u}{2}+su+\frac{u^2}{2}+\frac{\pi^2}{6}.
}
\]

## 5. Explicit regulator theorem

Combining the exact decomposition, scale errors, dilogarithm bounds, and prefactor estimate yields

\[
\boxed{
\left|
J(-S,-U;m)
-\frac{2\log(S/m)\log(U/m)+\log^2(U/m)-\pi^2/3}{SU}
\right|
\le
C(S,U)\,m(1+|\log m|^2)
}
\]

for every `0<m\le m_0`, where the following completely explicit constant is admissible:

\[
\boxed{
C(S,U)=\frac{2}{SU}
\left[
K_1+m_0K_2+C_E(S,U)+\frac{2K_0}{U}
\right].
}
\]

Consequently

\[
J(-S,-U;m)=
\frac{2\log(S/m)\log(U/m)+\log^2(U/m)-\pi^2/3}{SU}
+O_{S,U}(m(1+|\log m|^2)),
\]

and in particular the previously stated `o(1)` massless asymptotic follows rigorously.

## Status

This is an analytic discovery-level proof with all constants exposed and no fitted asymptotic step.  The exact Möbius `m^2` factorization has already passed Lean CI in `GPPVerify2`; the present logarithm/dilogarithm inequalities and final assembled remainder constant have not yet been promoted to Lean.  A separate high-precision audit script numerically checks the stated bound over randomized positive `(S,U,m)` points in the permitted domain.
