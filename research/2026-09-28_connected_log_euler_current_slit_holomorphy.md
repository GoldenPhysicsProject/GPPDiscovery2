# Connected logarithmic Euler current: the slit-plane obstruction is scalar, not Hilbert-valued

Date: 2026-09-28
Status: exact zero-independent Hilbert-space theorem and reduction. No RH claim.

This note attacks the current minimal RH target from
\`2026-09-28_slit_resolvent_minimal_rh_criterion.md\`.

## 1. Prime-power logarithmic current

Let
\[
\mathcal H_{\rm pp}=\ell^2\{(p,k): p\ {\rm prime},\ k\ge1\}
\]
with orthonormal basis \(e_{p,k}\). For \(z\in\mathbb C\) with
\(a=\Re z>0\), define
\[
J(z)=\sum_{p}\sum_{k\ge1}
(\log p)\,p^{-k(1/2+z)}e_{p,k}.
\]

This is the orthogonal Hilbertization of the full von-Mangoldt prime-power
current at half-density.

Its norm is exactly
\[
\|J(z)\|^2
=
\sum_p(\log p)^2
\frac{p^{-1-2a}}{1-p^{-1-2a}}.
\]

Writing \(m=p^k\), each prime power has a unique pair \((p,k)\), and
\(\log p\le\log m\). Hence
\[
\|J(z)\|^2
\le
\sum_{m\ge2}\frac{(\log m)^2}{m^{1+2a}}
=
\zeta''(1+2a).
\]

Therefore
\[
\boxed{J(z)\in\mathcal H_{\rm pp}\quad\text{for every }\Re z>0.}
\]

This uses no PNT, no zero-free region, and no RH input.

## 2. Holomorphy and local boundedness on the full square-root half-plane

For every derivative order \(j\ge0\),
\[
\partial_z^j\!\left[(\log p)p^{-k(1/2+z)}\right]
=
(-1)^j(\log p)(k\log p)^j p^{-k(1/2+z)}.
\]
Since \(k\log p=\log(p^k)=\log m\),
\[
\sum_{p,k}\left|\partial_z^j c_{p,k}(z)\right|^2
\le
\sum_{m\ge2}
\frac{(\log m)^{2j+2}}{m^{1+2a}}<\infty.
\]

On every compact set \(\Re z\ge\delta>0\), the same majorant with
\(a=\delta\) works uniformly. Thus the vector series and all fixed
derivative series converge locally uniformly in Hilbert norm. Hence
\[
\boxed{
J:\{\Re z>0\}\to\mathcal H_{\rm pp}
\text{ is Hilbert-valued holomorphic and locally bounded.}
}
\]

Under the principal square root \(z=\sqrt u\), the slit plane
\(\mathbb C\setminus(-\infty,0]\) maps to \(\Re z>0\). Therefore
\[
\boxed{
u\mapsto J(\sqrt u)
}
\]
is already a locally bounded Hilbert-valued object on the ENTIRE physical
Casimir slit plane.

This is precisely the normal-family domain demanded by the current minimal
resolvent strategy, but at the connected/vector level rather than after
scalarization.

## 3. Why the scalar Euler wall is at Re z = 1/2

The scalar logarithmic Euler current is
\[
P(z)
=
\sum_{p,k}
(\log p)p^{-k(1/2+z)}
=
-\frac{\zeta'}{\zeta}(\tfrac12+z)
\]
in its absolute Euler domain.

Absolute scalar summability is an \(\ell^1\) requirement, and it requires
\[
\Re(\tfrac12+z)>1,
\qquad\text{i.e.}\qquad
\Re z>\tfrac12.
\]

By contrast, the Hilbert current requires only square summability and hence
\[
2\Re(\tfrac12+z)>1,
\qquad\text{i.e.}\qquad
\Re z>0.
\]

So the familiar Euler wall is exactly the difference between a coherent
\(\ell^1\) scalar evaluation and the connected \(\ell^2\) arithmetic field:
\[
\boxed{
\text{scalar wall: }\Re z>\tfrac12,
\qquad
\text{Hilbert wall: }\Re z>0.
}
\]

The half-unit gain is not heuristic. It is the same half-density mechanism
seen independently in the BPY connected Möbius state.

## 4. Relation to the previous BPY connected theorem

The 2026-09-25 BPY theorem proved that the centered Möbius-decimated field is
Hilbert-valued holomorphic for \(\Re s>1/2\), while the non-summable piece is
the coherent vacuum coefficient. Here the logarithmic derivative exhibits the
same phenomenon in an even simpler orthogonal prime-power carrier:

- the connected prime-power current is already Hilbert-valued throughout
  \(\Re(s-1/2)>0\);
- only the all-ones/coherent scalar reconstruction has the stricter Euler
  threshold;
- therefore changing the bulk Hilbert carrier again cannot solve RH;
- the remaining issue is the completed boundary functional / quotient that
  combines this current with the Archimedean and pole channels without
  reintroducing the illegal all-ones evaluation.

This independently confirms the heuristic:
**after stable Hilbertization, the ghost lives in reconstruction, not in the
prime field.**

## 5. Sharpened smallest load-bearing theorem

The previous minimal slit-resolvent target asked for local boundedness of the
whole finite completed scalar family \(m_P(u)\).

The present theorem removes the prime bulk from that burden. The prime current
already has the required local boundedness in a canonical Hilbert space.

Thus the remaining RH-bearing statement can be sharpened to:

> Construct a zero-independent completed reconstruction functional
> \(\mathcal B_u\), incorporating the Archimedean/pole/Poisson quotient, such
> that for every compact \(K\subset\mathbb C\setminus(-\infty,0]\),
> \[
> \sup_{u\in K}\|\mathcal B_u\|_{\mathcal H_{\rm pp}^*\to\mathbb C}<\infty,
> \]
> and in the Euler region
> \[
> \mathcal B_u[J(\sqrt u)]
> =
> \frac1{2\sqrt u}\frac{\xi'}{\xi}
> (\tfrac12+\sqrt u)
> -
> h_{\rm explicit}(u),
> \]
> with \(h_{\rm explicit}\) slit-holomorphic.

Equivalently: prove the Poisson/product-formula completion turns the formal
all-ones evaluation into a bounded functional on the CONNECTED physical
quotient.

If such \(\mathcal B_u\) exists, then the scalar response is slit-holomorphic,
hence every nontrivial zero is principal-series and RH follows.

This is strictly smaller than proving positivity, Stieltjes structure,
Fredholm positivity, or even a new self-adjoint bulk operator: the bulk prime
current is already in the correct Hilbert class.

## 6. Falsifier / no-go inherited automatically

Any proposed completion that, after rewriting, still pairs \(J(z)\) with the
raw all-ones vector
\[
\Omega_{\rm coh}=\sum_{p,k}e_{p,k}
\]
without a proved quotient/renormalized extension has not crossed the Euler
wall; it has merely hidden the original \(\ell^1\) scalarization.

Therefore every candidate reconstruction should be audited by asking whether
its boundary functional is genuinely bounded on the connected Hilbert carrier
for all \(\Re z>0\).

## 7. Formalization target

Immediate Lean core:

1. for \(a>0\), the square-majorant
   \[
   \sum_{n\ge1}\frac{(\log(n+1))^2}{(n+1)^{1+2a}}
   \]
   is summable;
2. for \(a>1/2\), the scalar majorant
   \[
   \sum_{n\ge1}\frac{\log(n+1)}{(n+1)^{1/2+a}}
   \]
   is summable.

GPPVerify already contains the general zeta-Gibbs log-moment summability
machinery, so these are clean specializations rather than new analytic axioms.

The infinite prime-power Hilbertization should then be formalized as a
comparison/subseries theorem on top of that majorant.
