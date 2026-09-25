# RH discovery: causal Koszul curvature and half-density coercivity
## Corrected same-interval Hodge gap

**Date:** 2026-09-24  
**Status:** exact finite/operator algebra plus an unconditional large-cutoff asymptotic corollary using standard prime-counting estimates. This does not prove RH. It repairs the interrupted many-prime Hodge-gap argument by retaining the mixed adjoint commutators that were previously omitted.

## 1. Setup on the actual causal interval

Let
\[
H_L=L^2(0,L),
\]
and for \(0\le a\le L\) let \(V_a\) be the causal right shift
\[
(V_af)(x)=
\begin{cases}
f(x-a),&x\ge a,\\
0,&x<a.
\end{cases}
\]

Then
\[
V_aV_b=V_bV_a=V_{a+b}
\]
with the convention \(V_c=0\) for \(c\ge L\). The adjoints also commute:
\[
V_a^*V_b^*=V_b^*V_a^*.
\]

For a finite prime set \(P_X=\{p\le X\}\), write
\[
a_p=\log p,
\qquad
r_p(s)=p^{-s},
\qquad
T_p(s)=I-r_p(s)V_{a_p}.
\]

For \(\Re s\ge 1/2\),
\[
|r_p(s)|\le p^{-1/2}<1.
\]

Let \(\varepsilon_p,\iota_p\) be fermionic creation and contraction operators on
\(\Lambda(\mathbb C^{P_X})\), satisfying the CAR. Define
\[
d_s=\sum_{p\le X}T_p(s)\otimes\varepsilon_p,
\qquad
D_s=d_s+d_s^*.
\]

Because the \(T_p\) commute, \(d_s^2=0\). Because the \(T_p^*\) commute, \((d_s^*)^2=0\).

## 2. Correction to the interrupted argument

The previous interrupted derivation implicitly treated commuting \(T_p\) as though they also commuted with \(T_q^*\). On the causal interval that is false.

The exact Hodge square is
\[
\boxed{
D_s^2
=
\sum_p
\Big(
T_p^*T_p\otimes\iota_p\varepsilon_p
+
T_pT_p^*\otimes\varepsilon_p\iota_p
\Big)
+
\sum_{p\ne q}
[T_p,T_q^*]\otimes\varepsilon_p\iota_q .
}
\tag{1}
\]

Thus the omitted term is a genuine prime--prime boundary curvature.

For \(p\ne q\),
\[
[T_p,T_q^*]
=
r_p(s)\overline{r_q(s)}
[V_{a_p},V_{a_q}^*].
\tag{2}
\]

This is not a nuisance term to discard: it is exactly the failure of the causal shift semigroup to be doubly commuting, hence an intrinsic boundary interaction.

## 3. Exact causal commutator bound

A direct support calculation gives, for \(a,b\in[0,L]\),
\[
(V_aV_b^*f)(x)
=
1_{[a,\,\min(L,L+a-b)]}(x)f(x+b-a),
\]
and
\[
(V_b^*V_af)(x)
=
1_{[\max(0,a-b),\,L-b]}(x)f(x+b-a).
\]

The two operators use the same translated value and differ only by a multiplier taking values in \(\{-1,0,1\}\). Therefore
\[
\boxed{
\|[V_a,V_b^*]\|\le1.
}
\tag{3}
\]

Consequently
\[
\boxed{
\|[T_p,T_q^*]\|
\le
|r_p(s)r_q(s)|.
}
\tag{4}
\]

At and to the right of the critical line,
\[
\|[T_p,T_q^*]\|
\le
(pq)^{-1/2}.
\tag{5}
\]

## 4. Positive diagonal Hodge energy

Since \(\|V_{a_p}\|\le1\),
\[
\|T_p(s)f\|
\ge
(1-|r_p(s)|)\|f\|.
\]

Hence both
\[
T_p^*T_p\ge(1-|r_p|)^2I,
\qquad
T_pT_p^*\ge(1-|r_p|)^2I.
\]

Because
\[
\iota_p\varepsilon_p+\varepsilon_p\iota_p=I,
\]
the diagonal part of (1) obeys
\[
\boxed{
A_s
:=
\sum_p
\Big(
T_p^*T_p\otimes\iota_p\varepsilon_p
+
T_pT_p^*\otimes\varepsilon_p\iota_p
\Big)
\ge
g_X(s)I,
}
\]
where
\[
g_X(s)
=
\sum_{p\le X}(1-|r_p(s)|)^2.
\tag{6}
\]

For \(\Re s\ge1/2\),
\[
g_X(s)
\ge
\sum_{p\le X}(1-p^{-1/2})^2.
\tag{7}
\]

## 5. Curvature norm and explicit coercive lower bound

Let
\[
R_s
=
\sum_{p\ne q}
[T_p,T_q^*]\otimes\varepsilon_p\iota_q.
\]

Since \(\|\varepsilon_p\iota_q\|\le1\),
\[
\|R_s\|
\le
\sum_{p\ne q}|r_p(s)r_q(s)|.
\]

At \(\Re s\ge1/2\), define
\[
S_1(X)=\sum_{p\le X}p^{-1/2},
\qquad
S_2(X)=\sum_{p\le X}p^{-1}.
\]

Then
\[
\boxed{
\|R_s\|
\le
S_1(X)^2-S_2(X).
}
\tag{8}
\]

Combining (6)--(8),
\[
\boxed{
D_s^2\ge\kappa(X)I
}
\tag{9}
\]
with
\[
\boxed{
\kappa(X)
=
\pi(X)-2S_1(X)-S_1(X)^2+2S_2(X).
}
\tag{10}
\]

This bound is uniform in \(\Im s\) and valid throughout \(\Re s\ge1/2\).

## 6. Large-cutoff asymptotics

By the prime number theorem and partial summation,
\[
\pi(X)
=
\frac{X}{\log X}
+
O\!\left(\frac{X}{\log^2X}\right),
\]
\[
S_1(X)
=
\frac{2\sqrt X}{\log X}
+
O\!\left(\frac{\sqrt X}{\log^2X}\right),
\]
while
\[
S_2(X)=O(\log\log X).
\]

Therefore
\[
\boxed{
\kappa(X)
=
\frac{X}{\log X}
\left(
1-\frac{4}{\log X}
+o\!\left(\frac1{\log X}\right)
\right).
}
\tag{11}
\]

In particular, \(\kappa(X)>0\) for all sufficiently large \(X\), and
\[
\boxed{
\|D_s^{-1}\|
=
O\!\left(\sqrt{\log X}\,X^{-1/2}\right)
}
\tag{12}
\]
uniformly for \(\Re s\ge1/2\).

Writing \(X=e^L\),
\[
\boxed{
\|D_s^{-1}\|
=
O\!\left(\sqrt L\,e^{-L/2}\right).
}
\tag{13}
\]

The scale predicted in the interrupted handoff therefore survives on the real causal interval even after the missing mixed terms are restored.

The mechanism is now correct:

- diagonal many-prime Hodge energy is of order \(X/\log X\);
- causal boundary curvature is at most order \(X/\log^2X\);
- half-density weighting suppresses the curvature by one full logarithm.

Chebyshev-type upper/lower prime-counting estimates already suffice for eventual positivity; the full PNT is used only for the sharp asymptotic display.

## 7. Degree-zero sector is even cleaner

On fermionic degree zero,
\[
D_s^2|_{\Lambda^0}
=
d_s^*d_s
=
\sum_{p\le X}T_p^*T_p.
\]

All mixed curvature terms vanish identically on the vacuum sector. Hence
\[
\boxed{
D_s^2|_{\Lambda^0}
\ge
\sum_{p\le X}(1-p^{-1/2})^2 I.
}
\tag{14}
\]

Thus the scalar vacuum-to-one-particle Hodge Green operator has an even stronger exact coercive denominator. The global RH difficulty is not bulk invertibility; it is identifying the completed physical scalar boundary response as the correct bounded/Feshbach matrix element of this Green system.

## 8. Interpretation for the RH programme

This repairs Priority 1 of the 2026-09-24 handoff.

The many-prime causal Hodge bulk is not merely positive in an artificial tensor-product model. On the actual common causal interval it has:

1. an exact Hodge diagonal;
2. an explicit boundary curvature;
3. a curvature norm suppressed by half-density;
4. an eventual uniform coercive gap of order \(X/\log X\);
5. inverse Green suppression \(O(\sqrt L e^{-L/2})\).

The omitted commutators are structurally interesting: they are precisely the connected boundary terms that any correct Feshbach completion must retain.

The next load-bearing task is now sharper:

> derive the exact pole--prime--Archimedean scalar boundary functional as a Schur/Feshbach matrix element of the causal Koszul Green system, with the curvature term retained rather than set to zero.

If the physical boundary source has the expected coherent size \(O(e^{L/2}\operatorname{poly}(L))\), (13) reduces the resulting one-propagator response to polynomial size. The exact boundary identity is still missing and remains RH-strength.

No RH claim is made here.
