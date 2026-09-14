# Causal heat Laplace transform: exact rank-one boundary channel

Date: 2026-09-14
Status: exact finite-cutoff operator calculation / structural no-go, not a proof of RH

## Input

The current arithmetic principal-series manuscript constructs finite completed causal operators `C^{cpl}_{t,L}` whose sine-transform kernel is

\[
\widehat{\mathcal C}^{\rm cpl}_{t,L}(k,\ell)
=\frac{2}{\pi}q_L(k)\,\ell
\int_0^t e^{-(t-s)k^2-s\ell^2}\,ds,
\qquad k,\ell>0.
\]

Their traces converge pointwise in heat time to the zero-independent arithmetic heat function

\[
\operatorname{Tr}\mathcal C^{\rm cpl}_{t,L}\to\mathscr K(t).
\]

The manuscript correctly calls this a relative boundary trace and does not exhibit `C^{cpl}_{t,L}` as a positive heat semigroup. The calculation below makes the distinction sharper.

## Theorem 1: Laplace-time rank-one collapse

For `sigma>0`, define the Laplace-time transform

\[
\mathcal R_{\sigma,L}
:=\int_0^\infty e^{-\sigma t}\mathcal C^{\rm cpl}_{t,L}\,dt,
\]

initially in the sine representation. Then

\[
\boxed{
\widehat{\mathcal R}_{\sigma,L}(k,\ell)
=\frac{2}{\pi}
\frac{q_L(k)}{\sigma+k^2}
\frac{\ell}{\sigma+\ell^2}.}
\]

Hence `R_{sigma,L}` is rank one:

\[
\boxed{
\mathcal R_{\sigma,L}
=|u_{\sigma,L}\rangle\langle v_\sigma|,}
\]

with

\[
u_{\sigma,L}(k):=u_{\sigma,L}(k)
=\sqrt{\frac2\pi}\frac{q_L(k)}{\sigma+k^2},
\qquad
v_\sigma(k)=\sqrt{\frac2\pi}\frac{k}{\sigma+k^2}.
\]

### Proof

Set `t=r+s` in the time integral. Then

\[
\begin{aligned}
&\int_0^\infty e^{-\sigma t}
\int_0^t e^{-(t-s)k^2-s\ell^2}\,ds\,dt\\
&=\int_0^\infty\int_0^\infty
 e^{-(\sigma+k^2)r}e^{-(\sigma+\ell^2)s}\,dr\,ds\\
&=\frac1{(\sigma+k^2)(\sigma+\ell^2)}.
\end{aligned}
\]

Substitution proves the factorization. Since `q_L(k)=O_L(k)` near zero and has at most linear growth at infinity at fixed `L`, both displayed vectors are in `L^2(R_+)` for `sigma>0`.

## Corollary 2: exact scalar Weyl response

The trace is

\[
\boxed{
\operatorname{Tr}\mathcal R_{\sigma,L}
=\frac2\pi\int_0^\infty
\frac{kq_L(k)}{(\sigma+k^2)^2}\,dk.}
\]

Equivalently,

\[
\operatorname{Tr}\mathcal R_{\sigma,L}
=\int_0^\infty e^{-\sigma t}
\operatorname{Tr}\mathcal C^{\rm cpl}_{t,L}\,dt.
\]

Where the cutoff limit and Laplace integral are justified (in particular in the safe region `sigma>1` already controlled by the current manuscript),

\[
\boxed{
\lim_{L\to\infty}\operatorname{Tr}\mathcal R_{\sigma,L}
=\int_0^\infty e^{-\sigma t}\mathscr K(t)\,dt
=\frac1{2\sqrt\sigma}\frac{\xi'}{\xi}
\!\left(\frac12+\sqrt\sigma\right).}
\]

Thus the finite causal construction is naturally a rank-one boundary realization of the scalar Weyl response.

## Structural no-go: this is not the Hilbert–Pólya resolvent

A resolvent `(H+sigma)^{-1}` of a densely defined self-adjoint operator on an infinite-dimensional Hilbert space is injective and has dense range. It cannot have rank one. Therefore

\[
\boxed{
\mathcal R_{\sigma,L}\neq(H_L+\sigma)^{-1}}
\]

for any ordinary infinite-dimensional self-adjoint `H_L` carrying the desired spectral theory.

Likewise, the limiting scalar identity

\[
\operatorname{Tr}\mathcal R_{\sigma,L}\to m(\sigma)
\]

does **not** mean that the operators `C^{cpl}_{t,L}` converge to `e^{-tH}`. They realize the trace/Weyl channel. A dilation or Schur completion is still required to manufacture the full state space.

This is consistent with the manuscript's existing warning that the prime–Archimedean formula is a relative boundary trace, not the trace of an exhibited positive heat operator.

## Corollary 3: ordinary self-adjointness of the rank-one channel is too strong

For real `q_L`, the rank-one operator

\[
|u_{\sigma,L}\rangle\langle v_\sigma|
\]

is self-adjoint iff `u_{sigma,L}` and `v_sigma` are real proportional. Because their denominators are identical, this requires

\[
\boxed{q_L(k)=c_L k\quad\text{a.e.}}
\]

for some real scalar `c_L`.

The completed arithmetic phase is not linear in `k`. Therefore ordinary sine-space self-adjointness cannot be the missing positivity mechanism.

## Corollary 4: local multiplication metrics are extremely restrictive

Suppose one seeks a positive multiplication metric `G=M_w`, independent of `sigma`, satisfying

\[
G\mathcal R_{\sigma,L}
=\mathcal R_{\sigma,L}^*G
\]

for all `sigma>0`. Kernel comparison gives

\[
w(k)q_L(k)\ell=kq_L(\ell)w(\ell),
\]

hence

\[
\boxed{
\frac{w(k)q_L(k)}k=\text{constant a.e.}}
\]

and therefore

\[
w(k)=C\frac{k}{q_L(k)}.
\]

Thus a positive local metric can exist only if `q_L(k)/k` has one sign almost everywhere (apart from null sets and zeros handled by the domain). This is a stringent extra condition, not established here. In particular, a generic sign-changing arithmetic phase cannot be repaired by a positive multiplication weight. Any successful completion is therefore expected to require the nonlocal metric/polarization already indicated by the independent prime–Archimedean no-go results.

## Interpretation

This calculation locates the missing object more precisely.

- `C^{cpl}_{t,L}` is an exact finite boundary/commutator representation.
- Its heat trace tends to the correct arithmetic `K(t)`.
- Its Laplace transform is a rank-one transfer/Weyl channel.
- The desired positive `H` must therefore be a **conservative/self-adjoint dilation or Schur completion** whose boundary Weyl function is the scalar limit above.
- Proving positivity of that dilation is the same global polarization problem seen in the BPY, Nyman–Burnol, Maass–Selberg, and Mobius–Archimedean formulations.

This also explains why unconditional scalar positivity of the shifted Weyl function does not solve RH: a scalar rank-one transfer response can be positive on the real axis while failing the full Stieltjes/Pick hierarchy required for a positive self-adjoint dilation.

## Relation to the screw–heat–Fredholm note

The companion note `2026-09-14_screw_heat_bernstein_fredholm_bridge.md` shows that a successful closure should yield one positive operator `H` with

\[
\mathscr K(t)=\operatorname{Tr}e^{-tH},
\qquad
F(z)=\det(I+z^2H^{-1}).
\]

The present note shows that `H` cannot simply be identified with the current finite causal commutator operators. Those operators provide a boundary transfer representation of the Weyl data from which `H` would have to be reconstructed.

## Next attack

Treat the rank-one family as boundary data in the language of passive/conservative system realizations or boundary triples. Search for an explicit **zero-independent nonlocal positive metric/dilation** of the arithmetic transfer channel. A candidate must simultaneously:

1. be independent of the spectral parameter `sigma`;
2. realize the full Stieltjes/Pick kernel, not just scalar positivity;
3. retain the Tate/Nyman boundary cokernel;
4. reproduce the same completed prime–Archimedean Weyl function;
5. generate an infinite-dimensional positive `H` whose inverse is trace class.

That is substantially sharper than asking the existing coupled trace operators themselves to converge to a heat semigroup.
