# Safe quadratic fold and reflection-resolvent compression

Date: 2026-09-14
Status: exact spectral-side synthesis + zero-independent arithmetic target; **not a proof of RH**

## 1. Purpose

The old Abel/Cesàro route and the newer shifted Stieltjes/Loewner route are not independent ideas. The old route regularizes the **linear** half-density displacement and hits a pole whenever a zero is off the critical line. The shifted route repairs that problem by first applying a quadratic spectral fold which sends the whole critical strip into a uniformly accretive right half-plane. The resulting safe resolvent kernel is exactly a compression of the Weil/Yakaboylu reflection metric.

This note records that synthesis.

---

## 2. The safe quadratic spectral coordinate

For a nontrivial zero write

\[
\rho=\frac12+\delta+i\gamma,
\qquad |\delta|<\frac12.
\]

Define

\[
\boxed{
 t_\rho
 :=1-\left(\rho-\frac12\right)^2.}
\]

Then

\[
\boxed{
 t_\rho
 =1+\gamma^2-\delta^2-2i\delta\gamma.}
\]

Because `|delta|<1/2`, independently of the height `gamma`,

\[
\boxed{\Re t_\rho>\frac34.}
\]

Thus every nontrivial-zero parameter is mapped into a fixed right half-plane, and for every `u>0`

\[
 u+t_\rho\ne0.
\]

No zero-free theorem and no RH assumption is needed for this safety margin.

This is precisely why the shift by one in the current massive/Stieltjes variable is structurally useful: it converts the entire critical strip into a uniformly accretive resolvent domain.

---

## 3. Reflection becomes ordinary complex conjugation

The functional-equation/reality involution used by the Weil/Yakaboylu reflection form is

\[
\rho\longmapsto \rho^\#:=1-\bar\rho.
\]

In centered coordinates this sends

\[
\zeta:=\rho-\frac12
\longmapsto -\bar\zeta.
\]

Therefore

\[
\boxed{
 t_{\rho^\#}
 =1-(-\bar\zeta)^2
 =\overline{t_\rho}.}
\]

So the quadratic fold turns arithmetic reflection into ordinary complex conjugation in the safe `t`-plane.

For a nontrivial zero `gamma != 0`,

\[
\Im t_\rho=-2\delta\gamma,
\]

hence

\[
\boxed{
 t_\rho\in\mathbb R
 \iff \delta=0
 \iff \Re\rho=\frac12.}
\]

Since `Re t_rho>3/4`, RH is equivalently the statement that all folded zero parameters lie on the positive real ray.

This is the geometric content of the shifted Stieltjes criterion.

---

## 4. The old Abel barrier versus the safe quadratic fold

The old Abel self-pairing uses the linear exponent

\[
\alpha_{\rm Abel}=2\delta
\]

and the positive integral exists only for

\[
\varepsilon>2|\delta|.
\]

An off-line zero therefore inserts a pole directly between the positive regulator domain and `epsilon=0`.

The quadratic fold instead replaces `delta` by

\[
 t_\rho=1-\zeta^2,
\]

whose real part is uniformly positive for every zero in the critical strip. The safe resolvent variable

\[
\frac1{u+t_\rho},
\qquad u>0,
\]

can therefore be studied entirely inside the absolutely convergent/right-half-plane regime.

The repair principle is:

> do not try to drag the linear Abel regulator through the off-line pole. Fold the spectral parameter quadratically into an accretive half-plane and test whether the resulting resolvent family admits a positive reflection metric.

---

## 5. Safe logarithmic-derivative impedance

Let

\[
F(z)=\frac{\xi(1/2+z)}{\xi(1/2)},
\qquad
r=\sqrt{1+u}>1.
\]

The safe shifted impedance is

\[
\boxed{
 m_*(u)
 =\frac{F'(r)}{2rF(r)}
 =\frac{1}{2\sqrt{1+u}}
 \frac{\xi'}{\xi}\!\left(\frac12+\sqrt{1+u}\right).}
\]

In the unconditional paired zero expansion,

\[
\boxed{
 m_*(u)
 =\sum_{[\rho]}\frac{m_\rho}{u+t_\rho},}
\]

where the indexing identifies the centered pair `zeta ~ -zeta`, so that the remaining reflection acts by `t -> conjugate(t)`.

Under RH,

\[
t_\rho=1+\gamma^2>0,
\]

and `m_*` becomes an ordinary positive Stieltjes transform.

---

## 6. The Loewner kernel is a resolvent compression of the reflection metric

Define

\[
\phi(u):=u\,m_*(u).
\]

Its divided difference is

\[
\boxed{
\phi^{[1]}(u,v)
=\sum_{[\rho]}m_\rho
\frac{t_\rho}{(u+t_\rho)(v+t_\rho)}.}
\]

Let the coefficient space carry the reflection involution

\[
W e_\rho=e_{\rho^\#},
\]

which is the spectral-coordinate version of the Weil/Bombieri/Yakaboylu metric. Choose square roots compatibly so that

\[
\sqrt{t_{\rho^\#}}
=\overline{\sqrt{t_\rho}}.
\]

Define the safe resolvent vector

\[
\boxed{
 d_u(\rho)
 =\sqrt{m_\rho}\,
 \frac{\sqrt{t_\rho}}{u+t_\rho}.}
\]

Then

\[
\begin{aligned}
\langle d_u,Wd_v\rangle
&=\sum_{[\rho]}
 \overline{d_u(\rho^\#)}d_v(\rho)\\
&=\sum_{[\rho]}m_\rho
\frac{t_\rho}{(u+t_\rho)(v+t_\rho)}.
\end{aligned}
\]

Therefore

\[
\boxed{
\phi^{[1]}(u,v)=\langle d_u,Wd_v\rangle.}
\]

This is the exact bridge between the current safe Loewner criterion and the old reflected-zero metric.

The arithmetic function `phi` is zero-independent and evaluated for `s>3/2`; the representation by `W` is the spectral-side interpretation. Proving the arithmetic Loewner kernel positive is therefore precisely a zero-independent route to positivity of the reflected spectral metric.

---

## 7. Finite truncations: exact Cauchy congruence

Take finitely many distinct folded parameters

\[
t_1,\ldots,t_N,
\qquad \Re t_j>0,
\]

closed under conjugation, with multiplicities/weights `m_j>0`. Choose any distinct positive sample points

\[
u_1,\ldots,u_N>0.
\]

Let

\[
D_{ji}
=\sqrt{m_jt_j}\,(u_i+t_j)^{-1}.
\]

This is a diagonally weighted Cauchy matrix. Its determinant is nonzero:

\[
\det D
=\left(\prod_j\sqrt{m_jt_j}\right)
\frac{\prod_{i<k}(u_k-u_i)\prod_{j<\ell}(t_\ell-t_j)}
{\prod_{i,j}(u_i+t_j)}
\]

up to the conventional Cauchy sign. Hence the finite resolvent vectors span the whole truncated coefficient space.

If `W_N` is the finite reflection permutation matrix, the finite Loewner matrix satisfies

\[
\boxed{
L_N=D^*W_ND.}
\]

By Sylvester inertia under invertible congruence,

\[
\boxed{
\operatorname{inertia}(L_N)=\operatorname{inertia}(W_N).}
\]

Thus a non-fixed conjugate pair contributes one negative direction to the finite reflected metric and therefore to the fully resolved finite Loewner kernel. A fixed point `t_j=\bar t_j` contributes a positive direction.

This finite statement is exact. In the full infinite problem, one still needs the global convergence/density argument; the arithmetic Loewner criterion supplies precisely that completion.

---

## 8. The integrated Ward kernel is the same reflection metric with heat-filtered vectors

The unconditional heat expansion gives

\[
\mathscr K(t)=\sum_{[\rho]}m_\rho e^{-t t_\rho+ t?}
\]

with the convention used in the current program more cleanly expressed through the unshifted exponent

\[
\alpha_\rho=t_\rho-1=-\left(\rho-\frac12\right)^2.
\]

The integrated Ward kernel is

\[
\boxed{
\mathscr J(a,b)
=\sum_{[\rho]}m_\rho
\frac{(1-e^{-a\alpha_\rho})(1-e^{-b\alpha_\rho})}{\alpha_\rho}.}
\]

With compatible square roots define

\[
c_a(\rho)
=\sqrt{m_\rho}
\frac{1-e^{-a\alpha_\rho}}{\sqrt{\alpha_\rho}}.
\]

Then exactly

\[
\boxed{
\mathscr J(a,b)
=\langle c_a,Wc_b\rangle.}
\]

Thus the heat/Ward and safe-resolvent/Loewner criteria are two different cyclic families compressing the **same** reflected-zero metric `W`.

The double Laplace transform relating the two families is the already derived identity

\[
\int_0^\infty\!\int_0^\infty
 e^{-ua-vb}\mathscr J_*(a,b)\,da\,db
=\frac{\phi^{[1]}(u,v)}{uv}.
\]

---

## 9. Relation to the current Yakaboylu operator

The latest Yakaboylu revision constructs directly

\[
\hat W=\sum_\rho
|\Phi_{1-\bar\rho}\rangle\langle\Phi_\rho|
\]

on the biorthogonal zero subspace and proves that its positivity is equivalent to RH. In coefficient coordinates its quadratic form is the same reflection form

\[
Q(c)=\sum_\rho\overline{c_{1-\bar\rho}}c_\rho.
\]

The present calculation identifies the GPP safe Loewner kernel as an explicit resolvent compression of this metric. Hence the two constructions fit as follows:

1. Yakaboylu supplies a concrete spectral carrier and reflected zero metric;
2. GPP supplies a zero-independent prime--Archimedean impedance `phi` in a safe Euler domain;
3. the Loewner kernel of `phi` is exactly the resolvent-orbit compression of the reflected metric;
4. proving that kernel positive from the arithmetic side would therefore supply the missing positivity of the spectral metric without assuming the zero locations.

---

## 10. Research conclusion

The old Haar/Yakaboylu idea was not fundamentally aiming at the wrong object. Its linear Abel implementation tried to approach the reflected zero metric through a regulator that develops poles exactly when Hardy causality fails.

The shifted quadratic fold removes that domain defect:

\[
\rho\mapsto
 t_\rho=1-(\rho-1/2)^2
\]

puts every possible nontrivial zero parameter safely in `Re t>3/4`, turns reflection into conjugation, and turns RH into the statement that the safe poles are actually positive-real.

The current Loewner/Ward positivity problem is therefore a genuine minimal repair of the old proof architecture, not a replacement of its core idea.

The remaining theorem is still hard but sharply stated:

\[
\boxed{
\text{prove the zero-independent arithmetic kernel }
\phi^{[1]}(u,v)
\text{ is positive definite on }(0,\infty).}
\]

Equivalently, construct the positive passive/conservative prime--Archimedean realization whose boundary impedance is `phi`.

No RH proof is claimed.
