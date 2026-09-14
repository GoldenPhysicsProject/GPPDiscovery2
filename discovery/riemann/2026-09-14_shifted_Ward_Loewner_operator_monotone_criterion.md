# Shifted Ward–Loewner operator-monotone criterion

Date: 2026-09-14
Status: exact zero-independent reformulation built from the current shifted Stieltjes theorem; not a proof of RH

## 1. Safe shifted heat system

The current manuscript defines

\[
 m_*(u)
 =\frac{1}{2\sqrt{1+u}}
 \frac{\xi'}{\xi}\!\left(\frac12+\sqrt{1+u}\right),
 \qquad u>0,
\]

and proves the exact zero-independent subordination identity

\[
 m_*(u)=\int_0^\infty e^{-(1+u)t}\mathscr K(t)\,dt.
\]

Define the safely shifted heat function

\[
\boxed{\mathscr K_*(t):=e^{-t}\mathscr K(t).}
\]

Then

\[
\boxed{m_*(u)=\int_0^\infty e^{-ut}\mathscr K_*(t)\,dt.}
\]

All real values `u>0` evaluate xi strictly to the right of `3/2`, so the arithmetic prime sums are absolutely convergent.

The manuscript already proves

\[
\boxed{
\mathrm{RH}
\iff
m_*\text{ is a Stieltjes function with representing measure supported in }[1,\infty).}
\]

Under RH,

\[
 m_*(u)=\sum_{\gamma>0}\frac{m_\gamma}{u+1+\gamma^2}.
\]

## 2. Complete-Bernstein / operator-monotone reformulation

Put

\[
\boxed{\phi(u):=u\,m_*(u).}
\]

A standard theorem for Stieltjes and complete Bernstein functions says

\[
 g\text{ Stieltjes}
 \iff
 u\mapsto u g(u)\text{ is a complete Bernstein function}.
\]

Nonnegative complete Bernstein functions on `(0,infinity)` are exactly the positive operator-monotone functions on that half-line (equivalently, their holomorphic continuations are Pick/Nevanlinna functions with the appropriate positivity).

The current manuscript also proves unconditional scalar positivity `m_*(u)>0`, hence `phi(u)>0` for `u>0`.

If `phi` is operator monotone, then `phi(u)/u=m_*(u)` is Stieltjes with a positive measure on `[0,infinity)`. The actual xi expression for `m_*` is holomorphic through the interval `(-1,0]`; Stieltjes inversion therefore excludes representing mass in `[0,1)`. Finiteness at `u=0` excludes an atom at zero. Consequently the measure is supported in `[1,infinity)`, and the shifted Stieltjes theorem gives RH.

Thus

\[
\boxed{
\mathrm{RH}
\iff
\phi(u)=
\frac{u}{2\sqrt{1+u}}
\frac{\xi'}{\xi}\!\left(\frac12+\sqrt{1+u}\right)
\text{ is operator monotone on }(0,\infty).}
\]

This criterion uses only safe real-axis arithmetic data; no critical-line limiting value is inserted.

## 3. Loewner matrix hierarchy

By Loewner's theorem, operator monotonicity is equivalent to positivity of every finite divided-difference matrix

\[
\boxed{
L_{ij}
=\phi^{[1]}(u_i,u_j),
\qquad u_i>0,}
\]

where

\[
\phi^{[1]}(u,v)
=
\begin{cases}
\dfrac{\phi(u)-\phi(v)}{u-v},&u\ne v,\\[1.2ex]
\phi'(u),&u=v.
\end{cases}
\]

Therefore

\[
\boxed{
\mathrm{RH}
\iff
[\phi^{[1]}(u_i,u_j)]_{i,j=1}^N\succeq0
\quad\text{for every finite positive set }\{u_i\}.}
\]

Under RH, writing

\[
\lambda_\gamma=1+\gamma^2,
\]

one has

\[
\phi(u)
=\sum_{\gamma>0}m_\gamma\frac{u}{u+\lambda_\gamma},
\]

so

\[
\boxed{
\phi^{[1]}(u,v)
=\sum_{\gamma>0}m_\gamma
\frac{\lambda_\gamma}
{(u+\lambda_\gamma)(v+\lambda_\gamma)}.}
\]

This is the explicit Gram representation with feature

\[
\Phi_u(\gamma)
=\frac{\sqrt{m_\gamma\lambda_\gamma}}
{u+\lambda_\gamma}.
\]

## 4. Exact cross-resolvent arithmetic form

The manuscript gives

\[
 m_*(u)=\langle\delta_0,R_u\mathcal W\rangle,
\qquad
R_u=(H_0+u)^{-1},
\qquad
H_0=-\partial_x^2+1.
\]

Using the resolvent identity,

\[
\frac{uR_u-vR_v}{u-v}
=H_0R_uR_v.
\]

Hence the Loewner kernel is exactly

\[
\boxed{
\phi^{[1]}(u,v)
=\langle\delta_0,H_0R_uR_v\mathcal W\rangle.}
\]

This is a zero-independent two-resolvent prime–Archimedean kernel. The RH problem is therefore equivalent to positivity of every finite matrix formed from these cross-resolvent pairings.

This is more structured than asking only for the scalar inequalities `m_*(u)>0`: it is precisely the Pick/Loewner hierarchy required of a passive positive impedance.

## 5. Shifted integrated Ward kernel

Define

\[
\mathscr B_*(t):=\int_0^t\mathscr K_*(s)\,ds
\]

and

\[
\boxed{
\mathscr J_*(a,b)
:=\mathscr B_*(a)+\mathscr B_*(b)-\mathscr B_*(a+b).}
\]

Let

\[
g_s(x)=\frac{e^{-x^2/(4s)}}{\sqrt{4\pi s}},
\qquad
h_t^*(x)=\int_0^t e^{-s}g_s(x)\,ds.
\]

Then

\[
\mathscr B_*(t)=\langle\mathcal W,h_t^*\rangle,
\]

and, with the Fourier convention used in the manuscript,

\[
\boxed{
\widehat h_t^*(\xi)
=\frac{1-e^{-t(1+\xi^2)}}{1+\xi^2}.}
\]

Therefore

\[
\widehat{h_a^*+h_b^*-h_{a+b}^*}(\xi)
=
\frac{(1-e^{-a(1+\xi^2)})(1-e^{-b(1+\xi^2)})}
{1+\xi^2}.
\]

If

\[
\boxed{
\widehat f_a^*(\xi)
=\frac{1-e^{-a(1+\xi^2)}}{\sqrt{1+\xi^2}},}
\]

then `f_a^* in L^2(R)` and

\[
\boxed{
\mathscr J_*(a,b)
=\langle\mathcal W,f_a^**\widetilde f_b^*\rangle.}
\]

Thus the safe shifted Ward vectors are **massive integrated boundary-flux vectors** for `H_0=-partial^2+1`.

Under RH,

\[
\boxed{
\mathscr J_*(a,b)
=\sum_{\gamma>0}\frac{m_\gamma}{1+\gamma^2}
(1-e^{-a(1+\gamma^2)})(1-e^{-b(1+\gamma^2)}),}
\]

so the Ward matrices are positive semidefinite.

Conversely, Ward positivity gives the shifted complete-monotonicity/Stieltjes property and hence RH, exactly as in the unshifted companion note. Therefore this safely shifted Ward kernel is itself an exact RH criterion.

## 6. Double Laplace transform = Loewner kernel

The bridge between the time-domain Ward form and the safe impedance is exact. Since

\[
\mathcal L[\mathscr B_*](u)=\frac{m_*(u)}u,
\]

a direct two-variable Laplace calculation gives, for `u != v`,

\[
\begin{aligned}
&\int_0^\infty\!\int_0^\infty
 e^{-ua-vb}\mathscr J_*(a,b)\,da\,db\\
&=\frac{m_*(u)}{uv}+\frac{m_*(v)}{uv}
-\frac{m_*(v)/v-m_*(u)/u}{u-v}\\
&=\boxed{
\frac{u m_*(u)-v m_*(v)}{uv(u-v)}}\\
&=\boxed{
\frac{\phi^{[1]}(u,v)}{uv}}.
\end{aligned}
\]

The diagonal is obtained by continuity.

Hence the shifted Ward kernel and the Loewner kernel are not merely equivalent RH tests. They are two transforms of the **same passive-system Gram object**:

\[
\mathscr J_*(a,b)
\xleftrightarrow[\text{double Laplace}]{}
\frac1{uv}\phi^{[1]}(u,v).
\]

Under RH this is transparent from the common positive measure `lambda_gamma=1+gamma^2`.

## 7. Implication for the multichannel Schur/dilation program

The finite M"obius/Hodge--Koszul construction already supplies:

- a positive acyclic prime bulk;
- exact local Euler cancellation in cohomology;
- a co-Poisson Archimedean boundary involution;
- a self-adjoint completed boundary symbol;
- a rank-one boundary/Weyl transfer channel whose scalar trace is the correct `m_*` data.

The missing global theorem can now be targeted in standard passive-realization form:

> Construct a positive conservative multichannel dilation whose driving-point impedance is `phi(u)=u m_*(u)`, or equivalently whose boundary resolvent Gram is `phi^{[1]}(u,v)`.

If such a positive dilation is obtained zero-independently, operator monotonicity follows automatically, hence `m_*` is Stieltjes and RH follows.

Conversely, the same-space metric no-go proves that this realization cannot be obtained by a bounded coercive reweighting of the existing one-channel sine space. It must use the internal prime/Archimedean states of the multichannel completion.

This identifies a precise interface between the arithmetic Schur architecture and classical passive-system realization theory.

## 8. Immediate low-order tests

The `1x1` Loewner condition is

\[
\boxed{
\phi'(u)=m_*(u)+u m_*'(u)\ge0
\qquad(u>0).}
\]

The `2x2` condition is

\[
\phi'(u)\phi'(v)
\ge
\left(\frac{\phi(u)-\phi(v)}{u-v}\right)^2.
\]

These are necessary but not sufficient separately. They are useful diagnostic identities for any proposed finite multichannel completion: failure at low order immediately kills the candidate, while success does not establish RH without the full hierarchy.

## References for the function-class step

Standard complete-Bernstein theory gives `g Stieltjes iff x g(x) is complete Bernstein`; Loewner theory identifies positive operator-monotone functions on `(0,infinity)` with the corresponding Pick/complete-Bernstein class. The project should cite a primary or standard monograph source when this criterion is promoted into the paper.
