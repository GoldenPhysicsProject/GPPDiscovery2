# Natural Casimir fold and the boundary-ghost quotient

Date: 2026-09-14
Status: exact algebra + new target architecture; **not a proof of RH**

## 1. The natural safe coordinate is not an arbitrary massive shift

Put

\[
s=\frac12+r,
\qquad
u:=s(s-1)=r^2-\frac14.
\]

The involution `s -> 1-s` sends `r -> -r` and leaves `u` fixed.  Thus `u` is the intrinsic shadow-invariant quadratic coordinate.  It is also the quadratic principal-series/Casimir variable already present elsewhere in the GPP program.

For the safe Euler branch

\[
s(u)=\frac{1+\sqrt{1+4u}}2,
\qquad u>0,
\]

we have `s(u)>1`, so the Euler product and the logarithmic derivative of zeta are absolutely convergent.  No analytic continuation through the critical strip is needed to *define* the arithmetic side of the target.

## 2. Folded zero parameters

For a nontrivial zero candidate

\[
\rho=\beta+i\gamma,
\qquad 0<\beta<1,
\]

define

\[
\boxed{t_\rho:=\rho(1-\rho).}
\]

Then

\[
\boxed{
 t_\rho
 =\beta(1-\beta)+\gamma^2
 +i\gamma(1-2\beta).}
\]

Hence

\[
\Re t_\rho=\beta(1-\beta)+\gamma^2>0
\]

throughout the open critical strip.  Functional reflection gives

\[
t_{1-\bar\rho}=\overline{t_\rho}.
\]

For a nonreal zeta zero (`gamma != 0`),

\[
\Im t_\rho=0
\quad\Longleftrightarrow\quad
\beta=\frac12.
\]

Under RH,

\[
t_\rho=\frac14+\gamma^2\in[1/4,\infty).
\]

Thus RH is equivalent to saying that every folded zero pole lies on the positive real ray, with the stronger support threshold `>=1/4`.

## 3. Casimir impedance

Define

\[
\boxed{
m_C(u)
:=
\frac1{2s(u)-1}\frac{\xi'}{\xi}(s(u)),
\qquad u>0.}
\]

Since

\[
\frac{du}{ds}=2s-1,
\]

this is literally

\[
m_C(u)=\frac{d}{du}\log \xi(s(u)).
\]

The centered Hadamard product gives, in paired form,

\[
\boxed{
m_C(u)=\sum_{[\rho]}\frac{m_\rho}{u+t_\rho}.}
\]

Therefore

\[
\mathrm{RH}
\iff
m_C\text{ is Stieltjes with support in }[1/4,\infty).
\]

Equivalently, for

\[
\boxed{\phi_C(u):=u\,m_C(u),}
\]

RH is equivalent to positive operator monotonicity of `phi_C`, or positivity of every Löwner matrix

\[
\left[\phi_C^{[1]}(u_i,u_j)\right]\succeq0,
\qquad u_i>0.
\]

The same finite Cauchy-congruence argument as for the earlier shifted fold applies, now with the canonical folded poles `t_rho = rho(1-rho)`.

## 4. Exact collapse of the two elementary completion poles

Use

\[
\frac{\xi'}{\xi}(s)
=\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
+\frac{\zeta'}\zeta(s).
\]

The two elementary completion terms satisfy the exact identity

\[
\boxed{
\frac1{2s-1}
\left(\frac1s+\frac1{s-1}\right)
=\frac1{s(s-1)}
=\frac1u.}
\]

Thus the completion-pole contribution to the Casimir impedance is a single boundary resolvent `1/u`.

Multiplying by `u`,

\[
\phi_{\rm pole}(u)=u\cdot\frac1u=1.
\]

Therefore its divided difference vanishes identically:

\[
\boxed{
\phi_{\rm pole}^{[1]}(u,v)=0.}
\]

This is the key new structural simplification.  In the older additive/Gamma defect decompositions the `s=0` and `s=1` terms appeared as two negative pole channels.  In the natural shadow-invariant Casimir coordinate they coalesce into one zero-energy boundary mode, and the operator-monotonicity/Löwner test quotients it out automatically.

The theta Ward identity had already shown that the elementary completion factor is a boundary index at partition-function level.  The Casimir fold shows the same fact at the logarithmic-derivative/Löwner level: the completion index is a constant gauge mode and carries no Löwner curvature.

## 5. Resolvent operator form

Let

\[
H_C=-\partial_x^2+\frac14,
\qquad
R_u=(H_C+u)^{-1}.
\]

With

\[
r=\sqrt{u+\frac14},
\]

the half-line/full-line Green kernel at the boundary has the usual factor

\[
G_u(0,x)=\frac{e^{-rx}}{2r}.
\]

Accordingly the completed boundary distribution `W` gives the canonical realization

\[
\boxed{
m_C(u)=\langle\delta_0,R_u\mathcal W\rangle.}
\]

The resolvent identity yields

\[
\boxed{
\phi_C^{[1]}(u,v)
=\langle\delta_0,H_C R_uR_v\mathcal W\rangle.}
\]

Thus the missing RH theorem is now a positive-kernel statement for the **canonical Casimir Hamiltonian** `H_C`, with the elementary completion boundary mode already removed.

## 6. Relation to the single bad-pair obstruction

Write

\[
t_\rho=a+ib,
\qquad
a=\beta(1-\beta)+\gamma^2>0,
\qquad b=\gamma(1-2\beta).
\]

For one reflected conjugate pair the contribution remains

\[
\phi_{a,b}(u)
=\frac{2u(u+a)}{(u+a)^2+b^2}.
\]

Hence the exact order-two determinant derived in the companion note becomes

\[
\det L_{a,b}(u,v)
=-\frac{4b^2(a^2+b^2)(u-v)^2}
{((u+a)^2+b^2)^2((v+a)^2+b^2)^2}.
\]

Since a nontrivial zero has `gamma != 0`, this is strictly negative for every distinct `u,v>0` exactly when `beta !=1/2`.

So the natural Casimir fold preserves the strongest feature of the previous safe fold while improving the geometry:

- the safe domain is exactly the Euler half-plane `s>1`;
- the folded real part is automatically positive on the whole critical strip;
- shadow symmetry is built into the coordinate;
- the completion factor `s(s-1)` becomes the coordinate itself;
- the two elementary pole ghosts become Löwner-null.

## 7. What remains

After quotienting the completion pole mode, the unresolved kernel is the coupled Gamma/prime part.  It is **not** legitimate to conclude that the remaining pieces are separately positive; the prime contribution is signed in the explicit formula, and previous fixed-Mellin no-go results rule out naive local compensation.

But the target has become cleaner: construct a global prime--Archimedean Gram/Schur factorization for

\[
\phi_C^{[1]}(u,v)
\]

on `u,v>0`.  There are no elementary pole channels left to manage.  Any remaining negative direction must come from the genuine arithmetic/Archimedean competition, i.e. exactly the RH content.

This coordinate should replace the arbitrary `+1` fold as the preferred canonical formulation unless a later obstruction appears.
