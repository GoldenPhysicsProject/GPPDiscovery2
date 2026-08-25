# Complete-monotone Fisher metric and strict prime-power Hankel geometry

## Domain and notation

Work only on the honest Gibbs half-line `beta > 1`.

Let

\[
A(\beta)=\log \zeta(\beta),\qquad
\kappa_r(\beta)=(-1)^r A^{(r)}(\beta),\quad r\ge 1.
\]

For the arithmetic Gibbs ensemble `P_beta(n)=n^{-beta}/zeta(beta)`, `kappa_r` is the `r`th cumulant of the energy `E_n=log n`. In particular

\[
U=\kappa_1=-\frac{\zeta'}{\zeta},\qquad
g=\kappa_2=\operatorname{Var}_\beta(\log n).
\]

No statement below is analytically continued into the critical strip.

## Exact prime-power / von-Mangoldt representation

Absolute convergence of the Euler product on `beta>1` gives

\[
A(\beta)=\sum_p\sum_{k\ge1}\frac{p^{-k\beta}}{k}.
\]

Termwise differentiation yields, for every integer `r>=1`,

\[
\boxed{\
\kappa_r(\beta)
 =\sum_p\sum_{k\ge1} k^{r-1}(\log p)^r p^{-k\beta}
 =\sum_{n\ge2}\Lambda(n)(\log n)^{r-1}n^{-\beta}>0.
\ }
\]

Strict positivity is immediate because every summand is nonnegative and the `n=2` term is strictly positive.

## New structural consequence: the Fisher metric is strictly completely monotone

Since `g=kappa_2`, repeated differentiation gives

\[
g^{(m)}(\beta)=(-1)^m\kappa_{m+2}(\beta).
\]

Therefore for every `m>=0`,

\[
\boxed{\ (-1)^m g^{(m)}(\beta)>0\qquad(\beta>1).\ }
\]

Thus the zeta-Gibbs Fisher metric is not merely positive and decreasing: it is **strictly completely monotone**. In particular

\[
g>0,\qquad g'=-\kappa_3<0,\qquad g''=\kappa_4>0,
\]

and all higher derivatives alternate strictly in sign.

Equivalently, `g` is the Laplace transform of the positive discrete prime-power measure

\[
\boxed{\
 d\nu(x)=\sum_{n\ge2}\Lambda(n)\log n\,\delta_{\log n}(dx),
 \qquad
 g(\beta)=\int_0^\infty e^{-\beta x}\,d\nu(x).
\ }
\]

This is an exact Bernstein/Laplace structure, not an analogy.

## Strict log-convexity and the first nontrivial Hankel determinant

From the same measure,

\[
\kappa_{m+2}(\beta)=\int x^m e^{-\beta x}\,d\nu(x).
\]

Cauchy-Schwarz gives

\[
\kappa_2\kappa_4-\kappa_3^2\ge0.
\]

The inequality is strict because the support of `nu` contains at least two distinct points (`log 2` and `log 3`), so `x` is not constant `nu_beta`-almost everywhere. Hence

\[
\boxed{\
\kappa_2(\beta)\kappa_4(\beta)-\kappa_3(\beta)^2>0.
\ }
\]

Equivalently,

\[
\boxed{\ (\log g)''
 =\frac{g g''-(g')^2}{g^2}
 =\frac{\kappa_2\kappa_4-\kappa_3^2}{\kappa_2^2}>0.\ }
\]

So the Fisher metric is **strictly log-convex** on `beta>1`.

## All finite Hankel moment matrices

Define

\[
m_j(\beta)=\kappa_{j+2}(\beta)
 =\int x^j e^{-\beta x}\,d\nu(x).
\]

For any real coefficients `c_0,...,c_N`,

\[
\sum_{i,j=0}^N c_i c_j m_{i+j}
 =\int\left(\sum_{i=0}^N c_i x^i\right)^2 e^{-\beta x}\,d\nu(x)\ge0.
\]

Because the support contains infinitely many distinct prime-power logarithms, a nonzero polynomial cannot vanish on the entire support. Therefore every finite Hankel matrix

\[
H_N(\beta)=\big[\kappa_{i+j+2}(\beta)\big]_{i,j=0}^N
\]

is in fact **positive definite** for `beta>1`.

This is the clean global countable analogue of the already formalized finite weighted polynomial Gram theorem. It supplies a precise target for promotion to Lean: first summability of every weighted moment, then the integral/tsum polynomial-square identity, then strictness from infinitely many prime support points.

## Directed KL consequence

For `1<beta<gamma`, the zeta-Gibbs directed divergences have the exact triangular Fisher representations

\[
D(\beta\|\gamma)=\int_\beta^\gamma(\gamma-x)g(x)\,dx,
\]

\[
D(\gamma\|\beta)=\int_\beta^\gamma(x-\beta)g(x)\,dx.
\]

Since `g` is strictly decreasing,

\[
\boxed{\ D(\beta\|\gamma)>D(\gamma\|\beta).\ }
\]

The strict monotonicity input is now arithmetic and exact: `g'=-kappa_3<0` follows from the positive von-Mangoldt expansion.

## Physical-temperature correction and curvature

With `T=1/beta` and physical Helmholtz free energy

\[
F(T)=-T\log\zeta(1/T),
\]

one has

\[
F'(T)=-S(T),\qquad
F''(T)=-\frac{C(T)}{T}=-\beta^3 g(\beta)<0,
\]

where `C=beta^2 g>0`. Thus `F(T)` is strictly concave on `0<T<1`. This corrects the older typo `F'=-C/T`; the latter quantity is `F''`.

## Scope boundary

These results are exact only on `beta>1`. Complete monotonicity, Hankel positivity, and Gibbs information geometry do **not** extend by analytic continuation as positivity statements, and they do not prove RH. The useful bridge to the RH program is structural: the same positive prime-power measure controls the half-plane logarithmic response, while a successful Weil bridge still requires the completed global explicit-formula quadratic form and its critical-line test-function interface.
