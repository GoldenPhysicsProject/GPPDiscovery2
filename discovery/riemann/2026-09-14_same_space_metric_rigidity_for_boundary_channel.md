# Same-space metric rigidity for the rank-one arithmetic boundary channel

Date: 2026-09-14
Status: abstract operator theorem + conditional arithmetic application; not a proof of RH

## Purpose

The companion note `2026-09-14_causal_heat_laplace_rank_one_boundary_channel.md` shows that the Laplace-time transform of the finite completed causal heat operator is the rank-one family

\[
R_{\sigma,L}=|u_{\sigma,L}\rangle\langle v_\sigma|,
\qquad \sigma>0,
\]

on the sine-space `H=L^2(R_+)`, with

\[
u_{\sigma,L}(k):=u_{\sigma,L}(k)
=\sqrt{\frac2\pi}\frac{q_L(k)}{\sigma+k^2},
\qquad
v_\sigma(k)=\sqrt{\frac2\pi}\frac{k}{\sigma+k^2}.
\]

A natural question was whether the failure of ordinary self-adjointness could be repaired merely by replacing the sine-space inner product by a bounded positive nonlocal metric `G` on the **same** Hilbert space.

The answer is rigid: if one metric makes the whole positive-parameter family positive, then, under the natural cyclicity hypothesis, it is forced to be multiplication by `k/q_L(k)` up to one scalar. Thus allowing a nonlocal bounded metric on the same multiplicity-one sine space does not create extra freedom. If the local multiplier fails positivity/boundedness/coercivity, the repair must genuinely enlarge or dilate the state space (or change spectral multiplicity), not merely alter the inner product on the existing channel.

No arithmetic positivity is asserted here.

## 1. Abstract setup

Let

\[
\mathcal H=L^2(0,\infty;dk),
\qquad
(Mf)(k)=k^2f(k),
\qquad
S_\sigma=(\sigma+M)^{-1},\quad \sigma>0.
\]

Let real measurable functions `q,p` be such that

\[
u_\sigma:=u_\sigma=S_\sigma q\in\mathcal H,
\qquad
v_\sigma=S_\sigma p\in\mathcal H
\]

for every `sigma>0`. In the arithmetic application `p(k)=k` and `q=q_L`.

Define

\[
A_\sigma:=|u_\sigma\rangle\langle v_\sigma|.
\]

Assume `G` is bounded, positive, self-adjoint, and boundedly invertible on `H`, and suppose

\[
\boxed{GA_\sigma\ge0\qquad\text{for every }\sigma>0.}
\]

This means that every boundary channel is positive in the `G`-inner product.

## 2. Rank-one positivity fixes each metric image up to a positive scalar

Since

\[
GA_\sigma
=|Gu_\sigma\rangle\langle v_\sigma|,
\]

positivity of this nonzero rank-one operator implies

\[
\boxed{Gu_\sigma=c_\sigma v_\sigma}
\]

for some `c_sigma>0`.

This point matters. Mere self-adjointness does **not** justify setting `c_sigma=1`; the scalar must be controlled rather than silently normalized away.

## 3. Self-adjointness of the metric makes the scalar independent of sigma

Because `q,p` are real and both resolvents are multiplication operators,

\[
I(\sigma,\tau)
:=\langle u_\sigma,v_\tau\rangle
=\int_0^\infty
\frac{q(k)p(k)}{(\sigma+k^2)(\tau+k^2)}\,dk
\]

is real and symmetric in `sigma,tau` whenever the pairing is defined.

Using `G=G^*`,

\[
\begin{aligned}
c_\tau I(\sigma,\tau)
&=\langle u_\sigma,Gu_\tau\rangle\\
&=\langle Gu_\sigma,u_\tau\rangle\\
&=c_\sigma I(\sigma,\tau).
\end{aligned}
\]

Therefore

\[
I(\sigma,\tau)\ne0
\quad\Longrightarrow\quad
c_\sigma=c_\tau.
\]

On the diagonal,

\[
\langle u_\sigma,Gu_\sigma\rangle
=c_\sigma I(\sigma,\sigma)>0,
\]

so `I(sigma,sigma)>0`. Continuity of `I` implies `I(sigma,tau)>0` for `tau` sufficiently close to `sigma`. Hence `c_sigma` is locally constant. Since `(0,infinity)` is connected,

\[
\boxed{c_\sigma=c>0\quad\text{for all }\sigma>0.}
\]

After replacing `G` by `G/c`, one may therefore normalize **globally and legitimately** to

\[
\boxed{Gu_\sigma=v_\sigma\quad\text{for every }\sigma>0.}
\]

## 4. The resolvent orbit forces G to commute with M

Fix `sigma_0>0` and write `u_0=u_{sigma_0}`, `v_0=v_{sigma_0}`. Pointwise,

\[
q=(\sigma_0+M)u_0,
\]

so the resolvent identity gives

\[
\boxed{
u_\sigma=u_\sigma
=u_0+(\sigma_0-\sigma)S_\sigma u_0.}
\]

Likewise

\[
v_\sigma=v_0+(\sigma_0-\sigma)S_\sigma v_0.
\]

Since `Gu_sigma=v_sigma` and `Gu_0=v_0`, subtraction yields, for `sigma != sigma_0`,

\[
\boxed{G S_\sigma u_0=S_\sigma G u_0.}
\]

Now use the resolvent identity once more. For `sigma != tau`,

\[
S_\sigma S_\tau
=\frac{S_\sigma-S_\tau}{\tau-\sigma}.
\]

Therefore `G S_sigma = S_sigma G` on the linear span of the resolvent orbit

\[
\mathcal D:=\operatorname{span}\{S_\tau u_0:\tau>0\}.
\]

Assume the natural cyclicity condition

\[
\boxed{\overline{\mathcal D}=\mathcal H.}
\]

Because `G` and every `S_sigma` are bounded, the commutation extends to all of `H`:

\[
\boxed{GS_\sigma=S_\sigma G\qquad(\sigma>0).}
\]

Hence `G` lies in the commutant of the spectral algebra of the multiplicity-one multiplication operator `M=k^2`. Consequently `G` itself is a multiplication operator:

\[
(Gf)(k)=w(k)f(k)
\]

for some essentially bounded positive real `w`, bounded away from zero because `G` is boundedly invertible.

## 5. Arithmetic specialization: the metric is forced to be k/q_L(k)

Now take

\[
p(k)=k,
\qquad q(k)=q_L(k).
\]

The normalized identity `Gu_{sigma_0}=v_{sigma_0}` gives

\[
w(k)\frac{q_L(k)}{\sigma_0+k^2}
=\frac{k}{\sigma_0+k^2}
\]

almost everywhere. Therefore

\[
\boxed{w(k)=\frac{k}{q_L(k)}\quad\text{a.e.}}
\]

up to the single positive global scalar removed in the normalization.

Thus:

> **Same-space metric rigidity.** If the resolvent orbit of `q_L` is cyclic and a bounded positive boundedly-invertible metric on the same sine space makes every rank-one arithmetic boundary channel `A_{sigma,L}` positive, then that metric is necessarily a positive scalar multiple of multiplication by `k/q_L(k)`.

There is no additional bounded nonlocal same-space freedom.

## 6. Cyclicity criterion

For the multiplication operator `M=k^2`, a sufficient condition is

\[
u_0(k):=u_0(k)\ne0\quad\text{for a.e. }k>0.
\]

Indeed, if `f` is orthogonal to `S_sigma u_0` for every `sigma>0`, then the finite complex measure obtained from `conj(f(k))u_0(k)dk` (after the change of variable `x=k^2`) has Stieltjes transform zero on the positive real resolvent set. Uniqueness of the Stieltjes transform forces the measure to vanish; if `u_0` is nonzero almost everywhere, then `f=0` almost everywhere.

For a finite cutoff `L`, the explicit arithmetic phase `q_L` is a nontrivial smooth/analytic-type sine superposition after the completed real-place subtraction. Establishing `q_L != 0` almost everywhere is therefore a small auxiliary condition, but it should be checked explicitly rather than hidden inside the theorem statement.

## 7. Consequences and no-go content

The theorem does **not** prove that the forced multiplier is impossible for every cutoff `L`. It says exactly what must be checked:

\[
\frac{k}{q_L(k)}>0\ \text{a.e.},
\qquad
\frac{k}{q_L(k)}\in L^\infty,
\qquad
\frac{q_L(k)}k\in L^\infty.
\]

If any of these fails, then no bounded coercive metric on the original sine space can make the entire positive-parameter boundary family positive.

This strengthens the preceding local-metric observation. The issue is not merely that multiplication metrics are restrictive. Under the all-`sigma` positivity requirement and cyclicity, **every** bounded same-space metric collapses to that multiplication metric.

The correct escape routes are therefore structural:

1. enlarge to a conservative/self-adjoint dilation space;
2. use a genuine multichannel Schur complement in which prime/Archimedean modes become internal states;
3. change spectral multiplicity;
4. use an unbounded graph metric/domain, with the domain and trace passage proved explicitly.

This is consistent with the independent scalar-passive no-go in the current manuscript: scalar passive products cannot subtract the diverging local Clark phase, so the needed cancellation must occur through multichannel compression/Schur reduction.

## 8. Relation to the RH closure target

The scalar trace of the rank-one boundary family already converges in the safe region to

\[
\frac{1}{2\sqrt\sigma}
\frac{\xi'}{\xi}\!\left(\frac12+\sqrt\sigma\right).
\]

The companion screw–heat–Fredholm note shows that a true closure should instead produce one positive infinite-dimensional operator `H` satisfying

\[
\mathscr K(t)=\operatorname{Tr}e^{-tH},
\qquad
F(z)=\det(I+z^2H^{-1}).
\]

The present rigidity theorem says that `H` cannot be obtained merely by declaring the existing rank-one boundary transfer family self-adjoint in some clever bounded inner product on the same sine-space channel. The full prime–Archimedean Hilbert–Pólya object, if it exists in this program, must arise as a dilation/completion whose **boundary Weyl channel** is the rank-one family.

## 9. Formalization target

A useful finite-dimensional Lean analogue is:

- for a family `A_s=|u_s><v_s|`, positivity of `G A_s` gives `G u_s=c_s v_s`, `c_s>0`;
- if cross pairings `<u_s,v_t>` are real symmetric and nonzero on a connected overlap graph, then all `c_s` agree;
- a finite simple-spectrum resolvent orbit spanning the space then forces `G` to commute with the diagonal spectral operator and hence be diagonal;
- the diagonal entries are fixed by the componentwise ratio `v/u`.

This can be formalized without asserting anything about the arithmetic sign of `q_L` and would certify the algebraic rigidity used above.
