# Phase UV asymptotic and bounded same-space metric no-go

Date: 2026-09-14
Status: exact asymptotic from the zero-independent finite-cutoff phase; structural no-go, not a proof of RH

## 1. Input

For fixed `L>0`, the current arithmetic principal-series manuscript defines

\[
q_L(k)
=A_\infty(1)k
+\int_0^L w_\infty(a)
\left(\frac{\sin(ka)}a-e^{-a}k\right)\,da
-\sum_{m\log p\le L}\frac{p^{-m/2}}m\sin(km\log p),
\]

and

\[
q_L'(k)
=A_\infty(1)
+\int_0^Lw_\infty(a)(\cos(ka)-e^{-a})\,da
-\sum_{m\log p\le L}(\log p)p^{-m/2}\cos(km\log p).
\]

The real-place density has the exact ultraviolet expansion already proved/used in the manuscript,

\[
\boxed{w_\infty(a)=-\frac1{2a}+\frac74+O(a)}
\qquad(a\downarrow0).
\]

The prime-power sum is finite for fixed `L`.

## 2. Theorem: universal fixed-cutoff ultraviolet asymptotic

For every fixed `L>0`,

\[
\boxed{q_L'(k)=\frac12\log k+O_L(1)}
\qquad(k\to+\infty),
\]

and therefore

\[
\boxed{q_L(k)=\frac12 k\log k+O_L(k)}.
\]

The same leading asymptotic holds for the sharp-corrected phase

\[
\widetilde q_L(k)=q_L(k)-r_Lk,
\]

because the correction is exactly linear in `k`.

### Proof

Write

\[
w_\infty(a)=-\frac1{2a}+h(a),
\]

where `h` extends continuously (hence integrably) to `[0,L]`, with `h(0)=7/4`.

Then

\[
\begin{aligned}
q_L'(k)
={}&A_\infty(1)
-\frac12\int_0^L\frac{\cos(ka)-e^{-a}}a\,da\\
&+\int_0^L h(a)(\cos(ka)-e^{-a})\,da
-\sum_{m\log p\le L}(\log p)p^{-m/2}\cos(km\log p).
\end{aligned}
\]

Split the singular integral as

\[
\int_0^L\frac{\cos(ka)-e^{-a}}a\,da
=
\int_0^L\frac{\cos(ka)-1}a\,da
+\int_0^L\frac{1-e^{-a}}a\,da.
\]

Using

\[
\int_0^L\frac{\cos(ka)-1}a\,da
=\operatorname{Ci}(kL)-\gamma-\log(kL),
\]

we obtain

\[
-\frac12\int_0^L\frac{\cos(ka)-e^{-a}}a\,da
=
\frac12\log k+C_L-\frac12\operatorname{Ci}(kL),
\]

where

\[
C_L=\frac12\left(\gamma+\log L-
\int_0^L\frac{1-e^{-a}}a\,da\right)
\]

is independent of `k`.

Now `Ci(kL)=O_L(k^{-1})` along the positive real axis. By the Riemann--Lebesgue lemma,

\[
\int_0^L h(a)\cos(ka)\,da=o_L(1),
\]

while `-int h(a)e^{-a} da` is a constant. Finally the finite prime-power cosine sum is uniformly bounded in `k`. Therefore

\[
q_L'(k)=\frac12\log k+O_L(1).
\]

Integrating in `k` gives

\[
q_L(k)=\frac12(k\log k-k)+O_L(k)
=\frac12k\log k+O_L(k).
\]

## 3. Correction to one sentence in v34

The proof of the finite sine normal form currently says that “the Gaussian kills [the] at-most-linear growth” of `q_L` for fixed `L` when integrating by parts.

The phrase **at-most-linear** is too strong. The correct growth is

\[
q_L(k)=\frac12k\log k+O_L(k).
\]

This does **not** damage the integration-by-parts argument: for every `t>0`,

\[
k\log k\,e^{-tk^2}\to0
\]

rapidly, and the derivative has only logarithmic growth. Thus the trace identity and all subsequent Gaussian formulas survive unchanged. Only the stated growth estimate should be corrected.

## 4. Cyclicity of the finite arithmetic phase orbit

The integrand

\[
w_\infty(a)
\left(\frac{\sin(ka)}a-e^{-a}k\right)
\]

has its apparent `a=0` singularity canceled: uniformly for `k` in compact complex sets,

\[
\frac{\sin(ka)}a-e^{-a}k=O(a)
\qquad(a\downarrow0).
\]

After this cancellation the finite-interval integral defines an entire odd function of `k`; the finite prime sum is entire as well. Hence `q_L` is entire and odd.

The ultraviolet asymptotic shows that `q_L` is not identically zero. Therefore its real zeros away from the origin are discrete. In particular

\[
q_L(k)\ne0\quad\text{for a.e. }k>0.
\]

Consequently, for any `sigma_0>0`,

\[
u_0(k)=\frac{q_L(k)}{\sigma_0+k^2}
\]

is nonzero almost everywhere. For the multiplicity-one multiplication operator `M=k^2`, this is the sufficient cyclicity condition used in the companion same-space metric rigidity theorem.

Thus the cyclicity hypothesis of that theorem is satisfied by every nontrivial finite arithmetic cutoff.

## 5. Theorem: no bounded coercive metric on the original sine space

The companion rigidity theorem proves:

> If one bounded positive boundedly-invertible metric `G` on the original sine space makes every positive-parameter rank-one boundary channel positive, then, up to one global positive scalar,
> \[
> (Gf)(k)=\frac{k}{q_L(k)}f(k).
> \]

But the ultraviolet asymptotic gives

\[
\frac{q_L(k)}k=\frac12\log k+O_L(1),
\]

hence

\[
\boxed{
\frac{k}{q_L(k)}
=\frac{2}{\log k}\left(1+O_L\left(\frac1{\log k}\right)\right)
\longrightarrow0.}
\]

Therefore the forced multiplication metric has no positive lower bound. Equivalently its inverse multiplier `q_L(k)/k` is unbounded.

We conclude:

\[
\boxed{
\text{For every fixed }L>0,\text{ no bounded positive boundedly-invertible metric on }L^2(\mathbb R_+)\text{ can make the entire family }A_{\sigma,L}\text{ positive.}}
\]

This is independent of any finite numerical zero table and uses no RH assumption.

If `q_L` has additional positive-frequency zeros, the obstruction is even stronger because `k/q_L(k)` becomes singular there; no such extra zero is needed for the theorem.

## 6. Interpretation

The current causal construction has successfully produced a zero-independent **boundary Weyl/transfer channel**, but the positive Hilbert--Pólya state space cannot be obtained by any bounded coercive change of inner product on that same one-channel sine space.

The missing construction must therefore use one of the genuinely structural escapes already indicated elsewhere in the program:

1. a conservative/self-adjoint dilation on a larger Hilbert space;
2. a multichannel prime--Archimedean Schur complement with hidden internal modes;
3. changed spectral multiplicity;
4. an unbounded graph metric/domain whose closability, self-adjointness, trace passage, and no-escaped-sector theorem are all proved.

This aligns exactly with the manuscript's independent scalar-passive no-go: positive scalar inner factors can only add Clark phase and cannot cancel the divergent prime phase. The cancellation has to occur through an internal multichannel reduction.

## 7. Why this is useful for the RH attack

This closes a whole family of tempting “repair the existing channel by a clever metric” attempts. The next operator construction should not spend effort searching the bounded commutant of the sine-space channel.

Instead, the rank-one family should be treated as **boundary data** for the enlarged operator `H` required by the screw–heat–Fredholm synthesis:

\[
\mathscr K(t)=\operatorname{Tr}e^{-tH},
\qquad
\mathscr B(t)=\operatorname{Tr}(H^{-1}(I-e^{-tH})),
\qquad
F(z)=\det(I+z^2H^{-1}).
\]

The new global Ward kernel then provides the trace-class-weighted positive boundary family that such a dilation must realize.
