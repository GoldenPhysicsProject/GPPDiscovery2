# Global integrated-heat Ward kernel

Date: 2026-09-14
Status: exact zero-independent RH-equivalent criterion and factorization target; not a proof of RH

## Summary

The screw–heat bridge gives a bounded/integrated version of the arithmetic heat trace. After one boundary subtraction it produces a positive-kernel target with exactly the same `(1-e^{-a\lambda})` structure as the local BPY/Schoenberg boundary defect, but now carrying the full completed prime–Archimedean data.

This note proves that positivity of that global Ward kernel is **equivalent to RH**. It also identifies its test vectors explicitly as time-integrated heat-boundary flux vectors. The missing global positivity theorem can therefore be stated as one concrete convolution-square factorization problem.

## 1. Integrated arithmetic heat function

Let

\[
g_t(x)=\frac{e^{-x^2/(4t)}}{\sqrt{4\pi t}},
\qquad
\mathscr K(t)=\langle\mathcal W,g_t\rangle.
\]

Define

\[
\boxed{
\mathscr B(t):=\int_0^t\mathscr K(s)\,ds.}
\]

The companion note proves the equivalent screw representation

\[
\boxed{
\mathscr B(t)=\int_0^\infty\Psi(L)g_t(L)\,dL,}
\]

where `Psi` is Suzuki's completed screw/box functional.

Put

\[
h_t(x):=\int_0^t g_s(x)\,ds.
\]

Then, distributionally in the completed explicit-formula pairing,

\[
\boxed{
\mathscr B(t)=\langle\mathcal W,h_t\rangle.}
\]

A useful closed form is

\[
h_t(x)
=\sqrt{\frac t\pi}e^{-x^2/(4t)}
-\frac{|x|}{2}\operatorname{erfc}\!\left(\frac{|x|}{2\sqrt t}\right).
\]

With the Fourier convention of the current manuscript,

\[
\boxed{
\widehat h_t(\xi)=\frac{1-e^{-t\xi^2}}{\xi^2},}
\]

with the removable value at `xi=0` understood by continuity.

## 2. The global boundary-subtracted Ward kernel

For `a,b>0`, define

\[
\boxed{
\mathscr J(a,b)
:=\mathscr B(a)+\mathscr B(b)-\mathscr B(a+b).}
\]

Equivalently,

\[
\mathscr J(a,b)
=\left\langle\mathcal W,
 h_a+h_b-h_{a+b}\right\rangle.
\]

Its Fourier multiplier factorizes:

\[
\begin{aligned}
\widehat{h_a+h_b-h_{a+b}}(\xi)
&=\frac{1-e^{-a\xi^2}-e^{-b\xi^2}+e^{-(a+b)\xi^2}}{\xi^2}\\
&=\frac{(1-e^{-a\xi^2})(1-e^{-b\xi^2})}{\xi^2}.
\end{aligned}
\]

Define `f_a in L^2(R)` by

\[
\boxed{
\widehat f_a(\xi)=\frac{1-e^{-a\xi^2}}{|\xi|}.}
\]

This is square-integrable: near zero it is `O(|xi|)`, while at infinity it is `O(|xi|^{-1})`. Therefore

\[
\boxed{
h_a+h_b-h_{a+b}=f_a*\widetilde f_b,}
\]

and hence

\[
\boxed{
\mathscr J(a,b)
=\langle\mathcal W,f_a*\widetilde f_b\rangle.}
\]

This is an exact zero-independent completed Weil pairing on a canonical one-parameter family of convolution-square test vectors.

## 3. RH implies Ward-kernel positivity

Under RH,

\[
\mathscr K(t)=\sum_{\gamma>0}m_\gamma e^{-\gamma^2t},
\]

so

\[
\mathscr B(t)=\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2}
(1-e^{-\gamma^2t}).
\]

Consequently

\[
\boxed{
\mathscr J(a,b)
=\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2}
(1-e^{-a\gamma^2})(1-e^{-b\gamma^2}).}
\]

Thus, for every finite set `a_1,...,a_N>0`, the matrix

\[
\boxed{
J^{(N)}_{ij}=\mathscr J(a_i,a_j)}
\]

is positive semidefinite.

The feature map is explicit:

\[
\Phi_a(\gamma)
=\frac{\sqrt{m_\gamma}}{\gamma}
(1-e^{-a\gamma^2}).
\]

## 4. Converse: Ward-kernel positivity forces complete monotonicity

Assume

\[
\boxed{
(\mathscr J(a_i,a_j))_{i,j=1}^N\succeq0}
\]

for every finite positive-time set.

Because a positive-definite kernel admits a Hilbert-space Gram realization, applying the same forward difference in each variable preserves positivity. Passing to the smooth limit gives

\[
\boxed{
-\mathscr B''(a+b)=-\mathscr K'(a+b)}
\]

as a positive-definite additive-semigroup kernel.

Equivalently, `-K'` is exponentially convex. By the Bernstein–Widder theorem there is a positive measure `mu` on the real spectral line such that

\[
-\mathscr K'(t)=\int e^{-\lambda t}\,\mu(d\lambda).
\]

The current manuscript already proves the unconditional locally-normal zero expansion of `K`. Together with the classical zero-free compact region around the real segment, it gives

\[
\mathscr K(t)\to0,
\qquad
\mathscr K'(t)\to0
\qquad (t\to\infty).
\]

Because `mu` is positive, this decay excludes negative `lambda` (which would grow exponentially) and an atom at `lambda=0`. Hence

\[
\operatorname{supp}\mu\subset(0,\infty).
\]

Using `K(infinity)=0`,

\[
\begin{aligned}
\mathscr K(t)
&=\int_t^\infty[-\mathscr K'(s)]\,ds\\
&=\int_{(0,\infty)}\frac{e^{-\lambda t}}{\lambda}\,\mu(d\lambda).
\end{aligned}
\]

Therefore `K` is completely monotone. The exact heat-trace criterion in the current manuscript then gives RH.

We have proved the exact equivalence

\[
\boxed{
\mathrm{RH}
\iff
(\mathscr J(a_i,a_j))_{i,j=1}^N\succeq0
\quad\text{for every finite positive-time set}.}
\]

This is also the semigroup negative-definiteness/Bernstein characterization in concrete form: `B` is a Bernstein function exactly when its additive boundary defect has the corresponding positive kernel (up to the harmless linear component, fixed here by the arithmetic decay at infinity).

## 5. Exact relation to the BPY/Schoenberg boundary defect

The BPY analysis produced, for `0<alpha<1`,

\[
J_\alpha(a,b)
=a^\alpha+b^\alpha-(a+b)^\alpha
\]

with the exact Gram factorization

\[
J_\alpha(a,b)
=\frac{\alpha}{\Gamma(1-\alpha)}
\int_0^\infty
(1-e^{-ta})(1-e^{-tb})\frac{dt}{t^{1+\alpha}}.
\]

The new arithmetic kernel has precisely the same structural form under RH:

\[
\mathscr J(a,b)
=\int_{(0,\infty)}
(1-e^{-a\lambda})(1-e^{-b\lambda})\,\eta(d\lambda),
\]

where

\[
\eta
=\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2}\delta_{\gamma^2}.
\]

So the local fractional BPY boundary subtraction and the global arithmetic Ward kernel are instances of the same Bernstein/Schoenberg cocycle architecture.

The distinction is decisive: the BPY fractional defect already has an explicit positive Gamma–Plancherel measure, whereas proving positivity of the global arithmetic measure `eta` is exactly RH.

## 6. Boundary-flux interpretation

The causal heat analysis in v34 defines the Dirichlet boundary-flux vector `kappa_s` whose sine transform is

\[
(\mathcal S\kappa_s)(k)
=\sqrt{\frac2\pi}\,k e^{-sk^2}.
\]

Integrating the boundary flux from `0` to `a` gives

\[
F_a:=\int_0^a\kappa_s\,ds,
\]

with

\[
\boxed{
(\mathcal SF_a)(k)
=\sqrt{\frac2\pi}\frac{1-e^{-ak^2}}k.}
\]

Apart from the even/full-line versus sine/half-line realization, this is exactly the feature multiplier defining `f_a` above.

Therefore the global Ward vectors are not ad hoc test functions. They are the **time-integrated boundary fluxes of the same Dirichlet heat system already used in the causal prime–Archimedean construction**.

This is the cleanest operator meaning found so far for the boundary subtraction.

## 7. Why this may be a better closure target

The older Gaussian OS criterion uses

\[
G(a,b)=\mathscr K(a+b)
=\langle\mathcal W,g_a*g_b\rangle.
\]

The new integrated Ward criterion uses

\[
\mathscr J(a,b)
=\langle\mathcal W,f_a*\widetilde f_b\rangle,
\]

where each feature has an additional inverse-frequency factor. Under RH this corresponds to the trace-class inverse-energy weighting `1/gamma^2`.

This aligns directly with the Fredholm target `H^{-1}` rather than only with the heat semigroup `e^{-tH}`. In particular,

\[
\mathscr B(\infty)
=\operatorname{Tr}(H^{-1}),
\]

and the same reciprocal spectrum generates the BPY cumulants.

Thus a potentially sharper proof strategy is:

1. construct the integrated boundary-flux map `a -> F_a` zero-independently;
2. identify the completed prime–Archimedean pairing of these fluxes with a positive quotient norm after the global Tate/Poisson boundary condition;
3. obtain `J>=0` directly;
4. use the theorem above to recover complete monotonicity of `K`, OS reconstruction, and RH;
5. set `A=H^{-1}` to obtain the Fredholm determinant.

This asks for positivity after **one integrated boundary subtraction**, which may be more compatible with the existing Gamma–Plancherel/Schoenberg resolution than trying to prove positivity of the unsmoothed relative heat trace directly.

## 8. No proof claim

The exact convolution-square identity does not itself prove positivity because the completed Weil distribution `W=nu_infty-nu_p` is signed. The unresolved theorem is still the global prime–Archimedean polarization/no-ghost statement. What has changed is the target: it is now an explicit, trace-class-weighted, boundary-flux Gram family whose positivity is exactly equivalent to RH and whose local BPY analogue is already positively factorized.

## Reference for the abstract semigroup statement

The standard background is the characterization of Bernstein functions as continuous nonnegative negative-definite functions on the additive half-line, equivalently through the Levy–Khintchine representation. See Schilling, Song, and Vondracek, *Bernstein Functions: Theory and Applications*, chapter on positive and negative definite functions.
