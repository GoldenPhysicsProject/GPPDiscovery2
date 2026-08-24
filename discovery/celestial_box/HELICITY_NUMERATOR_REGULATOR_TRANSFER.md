# External-helicity numerator transfer through the scalar regulator theorem

Codex/GPT discovery track, 2026-08-24.

## General transfer lemma

The regulated scalar dispersion object satisfies, for fixed `S,U>0` and

\[
0<m\le m_0:=\min\{S/4,U/16\},
\]

\[
\left|
J(-S,-U;m)-J_{\rm asy}(S,U;m)
\right|
\le C(S,U)m(1+|\log m|^2),
\]

where

\[
J_{\rm asy}(S,U;m)
=
\frac{2\log(S/m)\log(U/m)+\log^2(U/m)-\pi^2/3}{SU}.
\]

Let `N(S,U)` be any quantity independent of the cut integration variable and of the regulator `m`. Then exactly,

\[
\boxed{
\left|
N(S,U)J(-S,-U;m)-N(S,U)J_{\rm asy}(S,U;m)
\right|
\le |N(S,U)|C(S,U)m(1+|\log m|^2).
}
\]

Thus an external-only helicity numerator does not alter the endpoint/pole boundary-layer mechanism. It only multiplies the already-controlled scalar remainder.

## Yang--Mills application: the channel map is now fixed

The scalar derivation is explicitly a fixed-`u` dispersion relation with

\[
s=-S,\qquad u=-U,\qquad S,U>0.
\]

For massless four-point kinematics,

\[
s+t+u=0,
\]

so in this continuation

\[
\boxed{t=S+U}.
\]

The honest four-dimensional MHV cut derived from Parke--Taylor trees is

\[
\frac{C_s^{\rm YM}}{A_4^{\rm tree}}
=-i\,\frac{s t}{D_1D_2}
\]

in the chosen stripped convention. Therefore the external numerator is

\[
\boxed{st=(-S)(S+U)=-S(S+U)}.
\]

If the scalar cut normalization is used for the `1/(D_1D_2)` factor, the corresponding regulated Yang--Mills dispersion object is

\[
\frac{\mathcal J_{\rm YM}(m)}{A_4^{\rm tree}}
=(-i s t)J(-S,-U;m)
=iS(S+U)J(-S,-U;m).
\]

Substituting the scalar asymptotic gives the explicit helicity-weighted result

\[
\boxed{
\frac{\mathcal J_{\rm YM}(m)}{A_4^{\rm tree}}
=
 i\,\frac{S+U}{U}
\left[
2\log\frac Sm\log\frac Um
+\log^2\frac Um
-\frac{\pi^2}{3}
\right]
+R_{\rm YM}(m)
}
\]

with the rigorous inherited remainder bound

\[
\boxed{
|R_{\rm YM}(m)|
\le S(S+U)C(S,U)m(1+|\log m|^2).
}
\]

The important structural cancellation is that the physical MHV numerator supplies one power of `S`, cancelling the `1/S` in the scalar box prefactor. The double-log infrared structure remains, but its kinematic prefactor is now the helicity-derived rational factor `(S+U)/U` rather than the scalar `1/(SU)`.

The overall factor of `i` follows the amplitude/cut convention used in the MHV-cut note. A different convention can change that global phase/sign without changing the invariant kinematic content.

## Gravity application and limitation

The four-dimensional MHV gravity cut obtained from tree-level KLT has

\[
\frac{C_s^{\rm GR}}{M_4^{\rm tree}}
=i\,\frac{s^3tu}{D_1D_2D_3D_4}.
\]

Unlike the Yang--Mills single-box cut factor, this contains four uncut propagators from the two KLT orderings. Consequently it is **not** obtained merely by multiplying the same scalar two-denominator dispersion kernel by an external numerator. A gravity celestial regulator theorem therefore needs the corresponding four-denominator angular/dispersion geometry, or a justified partial-fraction/integral reduction, before the scalar remainder estimate can be reused.

This distinction matters: the Yang--Mills MHV cut directly inherits the scalar-box regulator analysis at the cut-integrand level; the gravity KLT cut does not do so without an additional reduction theorem.

## Boundary

This transfer statement remains four-dimensional and cut-constructible. D-dimensional `mu^2` numerator information and rational terms require the equal-mass `H^3` cut geometry and the actual D-dimensional state sum.
