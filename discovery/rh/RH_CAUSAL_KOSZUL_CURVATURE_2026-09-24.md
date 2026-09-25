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


## 9. Degree-zero Hodge Ward current and beta-flatness

The degree-zero sector gives a second exact structure which is closer to the desired connected response.

Set
\[
A_s=d_s^*d_s=\sum_{p\le X}T_p(s)^*T_p(s).
\]
Whenever the coercive bound above is positive, define the Hodge contraction from one-forms to the vacuum sector by
\[
h_s=A_s^{-1}d_s^*.
\]
Then, on degree zero,
\[
\boxed{h_s d_s=I.}
\tag{15}
\]

Let \(X_0\) denote multiplication by the causal coordinate on \(H_L\), extended trivially to fermion degree. Define the differentiated Hodge current
\[
\Gamma_s
=
h_s[X_0,d_s]
=
A_s^{-1}
\sum_{p\le X}T_p(s)^*[X_0,T_p(s)].
\tag{16}
\]

Commuting the exact contraction identity (15) with \(X_0\) gives the Ward relation
\[
\boxed{
[X_0,h_s]d_s+h_s[X_0,d_s]=0,
}
\qquad
\boxed{
\Gamma_s=-[X_0,h_s]d_s.
}
\tag{17}
\]

Thus the connected prime current in the Hodge parent is a pure commutator of the Green contraction with the causal coordinate.

For one prime,
\[
(T^*T)^{-1}T^*=T^{-1},
\]
so
\[
\Gamma=T^{-1}[X_0,T].
\]
For many primes, with
\[
W_p=A_s^{-1}T_p^*T_p,
\qquad
\sum_pW_p=I,
\]
and
\[
J_p=T_p^{-1}[X_0,T_p],
\]
one has the exact weighted-current identity
\[
\boxed{
\Gamma_s=\sum_{p\le X}W_pJ_p.
}
\tag{18}
\]
The raw causal logarithmic zeta connection is the unweighted sum of these local currents (up to the fixed sign convention). Equation (18) therefore identifies the Hodge response as the normalized/connected parent current rather than the coherent raw scalar sum.

Now write
\[
s=\beta/2+it.
\]
Since
\[
\partial_\beta T_p=-\frac12[X_0,T_p],
\]
we obtain
\[
\partial_\beta A_s
=
-\frac12(B_s+B_s^*),
\qquad
B_s=\sum_pT_p^*[X_0,T_p].
\tag{19}
\]
Since \(\Gamma_s=A_s^{-1}B_s\),
\[
\boxed{
\frac12
\left(
A_s^{1/2}\Gamma_sA_s^{-1/2}
+
A_s^{-1/2}\Gamma_s^*A_s^{1/2}
\right)
=
- A_s^{-1/2}(\partial_\beta A_s)A_s^{-1/2}.
}
\tag{20}
\]

So the Hermitian part of the Hodge current is exactly the negative relative beta derivative of the positive degree-zero Hodge metric. This is the same thermodynamic geometry seen earlier for the positive zeta-gauge metric, but now with the many-prime Hodge denominator already built in.

At \(\beta\ge1\),
\[
\|B_s\|
\le
\sum_{p\le X}
(1+p^{-1/2})\frac{\log p}{\sqrt p}.
\tag{21}
\]
Standard Chebyshev bounds and partial summation give
\[
\sum_{p\le X}\frac{\log p}{\sqrt p}
=
O(\sqrt X),
\qquad
A_s\ge c\frac{X}{\log X}I
\]
for all sufficiently large \(X\). Therefore
\[
\boxed{
\|\Gamma_s\|
=
O\!\left(\frac{\log X}{\sqrt X}\right)
=
O(Le^{-L/2}),
}
\tag{22}
\]
uniformly in \(t\), and likewise
\[
\boxed{
\left\|
A_s^{-1/2}(\partial_\beta A_s)A_s^{-1/2}
\right\|
=
O(Le^{-L/2}).
}
\tag{23}
\]

This is stronger than mere bulk invertibility: the normalized degree-zero Hodge metric becomes beta-flat exponentially fast with the arithmetic cutoff.

What remains open is the exact scalar extraction. A proof of RH would require showing that the completed pole--prime--Archimedean Weil boundary observable is a bounded/Feshbach functional of this connected Hodge response (plus a subexponential defect). Equations (17)--(23) do not assert that identification; they sharpen the parent-space object that a correct completion must couple to.


## 10. Exact coherent/connected decomposition of the causal prime connection

The Hodge structure gives an exact infinite-dimensional connected subtraction, not a finite-rank removal.

Let the one-form space be
\[
\mathcal H_1=\bigoplus_{p\le X}H_L,
\]
and write
\[
(df)_p=T_pf,
\qquad
d^*(g_p)=\sum_pT_p^*g_p,
\qquad
A=d^*d.
\]
Since \(A\) is invertible in the coercive regime, define
\[
h=A^{-1}d^*,
\qquad
\Pi=dh=dA^{-1}d^*.
\]
Then \(\Pi\) is the orthogonal projection onto \(\operatorname{ran}d\), and
\[
I-\Pi
\]
projects onto
\[
\ker d^*.
\]

Define the local-resolvent row
\[
\mathcal R(g_p)
=
\sum_{p\le X}T_p^{-1}g_p.
\tag{24}
\]
Since \(T_p^{-1}T_p=I\),
\[
\boxed{
\mathcal R d=\pi(X)I.
}
\tag{25}
\]
Consequently
\[
\boxed{
\mathcal R\Pi
=
\pi(X)h.
}
\tag{26}
\]

Let
\[
J=[X_0,d],
\qquad
\Gamma=hJ.
\]
The causal zeta connection is
\[
P_L
=
Z_L^{-1}[X_0,Z_L]
=
-\sum_{p\le X}T_p^{-1}[X_0,T_p]
=
-\mathcal RJ.
\tag{27}
\]
Using \(I=\Pi+(I-\Pi)\),
\[
\boxed{
P_L
=
-\pi(X)\Gamma
-
\mathcal R(I-\Pi)J.
}
\tag{28}
\]

Thus the raw prime connection splits exactly into

1. the coherent Hodge-exact current \(-\pi(X)\Gamma\);
2. the transverse connected current
\[
\boxed{
P_L^{\rm conn}
:=
-\mathcal R(I-\Pi)J.
}
\tag{29}
\]

This is the required infinite-dimensional subtraction mechanism that the finite-rank scalarization no-go left open.

### Polynomial bound for the connected row

Let \(g=(g_p)\in\ker d^*\). Then
\[
0=d^*g
=
\sum_p(I-\overline{r_p}V_p^*)g_p,
\]
so
\[
\sum_pg_p
=
\sum_p\overline{r_p}V_p^*g_p.
\tag{30}
\]
Also
\[
T_p^{-1}-I=r_pV_pT_p^{-1}.
\tag{31}
\]
Therefore
\[
\mathcal Rg
=
\sum_p
\left(
\overline{r_p}V_p^*
+
r_pV_pT_p^{-1}
\right)g_p.
\tag{32}
\]

For \(\Re s\ge1/2\),
\[
|r_p|\le p^{-1/2},
\qquad
\|T_p^{-1}\|
\le
\frac1{1-p^{-1/2}}.
\]
Hence
\[
\|\mathcal R|_{\ker d^*}\|
\le
C_0
\left(\sum_{p\le X}\frac1p\right)^{1/2},
\tag{33}
\]
where one may take the absolute constant
\[
C_0=1+\frac1{1-2^{-1/2}}.
\]
Using only the trivial comparison with the harmonic series,
\[
\sum_{p\le X}\frac1p
\le
\sum_{2\le n\le X}\frac1n
\le
1+\log X,
\]
so
\[
\boxed{
\|\mathcal R(I-\Pi)\|
=
O(\sqrt L).
}
\tag{34}
\]

The differentiated column obeys
\[
([X_0,T_p]f)
=
-(\log p)r_pV_pf.
\]
Thus
\[
\|J\|^2
\le
\sum_{p\le X}\frac{(\log p)^2}{p}
\le
\sum_{2\le n\le X}\frac{(\log n)^2}{n}
=
O(L^3),
\]
and therefore
\[
\boxed{
\|J\|=O(L^{3/2}).
}
\tag{35}
\]

Combining (29), (34), and (35),
\[
\boxed{
\|P_L^{\rm conn}\|
=
O(L^2).
}
\tag{36}
\]

This bound is uniform in the vertical spectral parameter and uses no zeta-zero information and no prime number theorem.

With Mertens' theorem for primes, (34) sharpens to \(O(\sqrt{\log\log X})\), but that improvement is unnecessary for RH stability.

### Meaning of the result

Equation (28) isolates the entire exponential scalar-prime conditioning into the coherent Hodge-exact piece \(-\pi(X)\Gamma\). Once that exact range component is removed, the surviving connected prime connection is polynomially bounded.

This does **not** authorize dropping the coherent term by hand. The remaining RH-strength theorem is now extremely specific:

> prove that the completed co-Poisson/pole/Archimedean scalar boundary construction implements the Hodge quotient (or an equivalent Feshbach subtraction) so that the physical Weil observable sees the connected current (29), while the coherent exact component is accounted for by the completion channels, with at most subexponential defect.

If that identification is established, the prime-side norm estimate needed by the vacuum-instability theorem is already closed by (36).


## 11. Independent finite-matrix audit in the live continuation

Because the local Python/container runtime was unavailable during this chat, the core identities were independently evaluated in a small real-matrix model directly in the execution runtime.

Parameters:
- causal Hilbert dimension (8);
- prime channels (p=2,3,5);
- causal lags (1,2,3);
- critical real weights (r_p=p^{-1/2});
- Jordan--Wigner fermionic creation/contraction matrices.

Observed residuals:
[
max_{p,q}|V_pV_q-V_qV_p|_F=0,
]
while
[
max_{p,q}|V_pV_q^*-V_q^*V_p|_F
=2.449489742783178,
]
confirming that the missing mixed adjoint commutators are genuinely present.

The corrected Hodge identity had Frobenius residual
[
|D^2-A_{m diag}-R_{m curv}|_F
=
1.1749496091904413	imes10^{-15}.
]

For the degree-zero Hodge projector and connected decomposition:
[
|Pi^2-Pi|_F, |Pi^*-Pi|_F
le
6.150930332726244	imes10^{-16},
]
[
|mathcal Rd-pi(X)I|_F=0,
]
and
[
|P+pi(X)Gamma-P^{m conn}|_F
=
8.632093056965055	imes10^{-16}.
]

Thus the two new operator identities are numerically reproduced to floating-point precision in a concrete common-causal-space model. This is a discovery-layer audit, not a substitute for Lean formalization.


## 12. Exact co-Poisson covariant anticommutation and the surviving shadow-odd joint

The classical co-Poisson identity in the v34 programme can be combined directly with the causal zeta gauge.

Let
[
mathscr R
]
be logarithmic reflection, let (mathcal C) be the half-density cosine/shadow involution, and let (mathcal Z) be the arithmetic half-density periodization operator. On the common co-Poisson test domain,
[
oxed{
mathscr Rmathcal Z=mathcal Zmathcal C.
}
	ag{37}
]
Formally, or on any finite/invertible regularization where the products are bounded,
[
mathcal C=mathcal Z^{-1}mathscr Rmathcal Z.
	ag{38}
]

Let (X_0) be logarithmic coordinate multiplication. Since
[
mathscr R X_0=-X_0mathscr R,
]
define the zeta-gauged coordinate
[
Y
=
mathcal Z^{-1}X_0mathcal Z
=
X_0+mathcal A,
qquad
mathcal A
=
mathcal Z^{-1}[X_0,mathcal Z].
	ag{39}
]
Then
[
oxed{
Ymathcal C+mathcal C Y=0.
}
	ag{40}
]
Indeed,
[
{Y,mathcal C}
=
mathcal Z^{-1}{X_0,mathscr R}mathcal Z
=
0.
]

Equivalently, the prime logarithmic connection satisfies the exact Ward identity
[
oxed{
mathcal Amathcal C+mathcal Cmathcal A
=
-left(X_0mathcal C+mathcal C X_0ight).
}
	ag{41}
]

In Mellin representation this is exactly the logarithmic derivative of the zeta functional equation, but (40)--(41) exhibit its operator meaning: the prime connection is the gauge field which makes the covariant coordinate odd under the Archimedean shadow involution.

The same similarity also gives, with
[
G=mathcal Z^*mathcal Z,
]
the formal positive-metric identities
[
Y^*G=GY,
qquad
mathcal C^*Gmathcal C=G.
	ag{42}
]
As already emphasized in v34, boundary self-adjointness alone is blind to off-axis zeros; the issue is the causal/Hardy realization and the conditioning/domain of the similarity at the critical boundary.

### Combination with the new Hodge split

From (28),
[
mathcal A
=
-pi(X)Gamma
+
P_L^{m conn},
qquad
|P_L^{m conn}|=O(L^2).
]
Insert this into (41):
[
oxed{
pi(X){Gamma,mathcal C}
=
{X_0,mathcal C}
+
{P_L^{m conn},mathcal C}.
}
	ag{43}
]
Since (mathcal C) is unitary on the half-density boundary,
[
|{P_L^{m conn},mathcal C}|
le
2|P_L^{m conn}|
=
O(L^2).
	ag{44}
]

Thus the shadow-even component of the exponentially scaled coherent Hodge current is already fixed by the explicit Archimedean operator modulo a polynomial term.

Writing
[
B_{m even}
=
rac12(B+mathcal C Bmathcal C),
qquad
B_{m odd}
=
rac12(B-mathcal C Bmathcal C),
]
equation (41) determines (mathcal A_{m even}) exactly:
[
oxed{
mathcal A_{m even}
=
-rac12
left(
X_0+mathcal C X_0mathcal C
ight).
}
	ag{45}
]
The unresolved information is therefore entirely in
[
oxed{
mathcal A_{m odd}
=
rac12
left(
mathcal A-mathcal Cmathcal Amathcal C
ight),
}
	ag{46}
]
equivalently in the shadow-odd part of (pi(X)Gamma) up to the polynomial connected error.

This matches the v34 no-go/Hardy analysis: functional-equation symmetry fixes the unitary boundary relation, while RH is exactly the extra one-sided causal/inner condition. Off-critical zeros can only survive in the shadow-odd causal sector.

### New minimal joint

The previous generic completion problem can therefore be reduced further:

> control the shadow-odd component of the coherent Hodge current after the co-Poisson completion.

Everything else is now either exact or polynomial:
- transverse connected prime current: (O(L^2));
- shadow-even coherent component: fixed by the Archimedean Ward identity modulo (O(L^2));
- elementary pole modes: exactly killed by the massive/theta boundary Ward operator;
- Archimedean semibounded channel: already controlled.

A subexponential bound on the physical scalarization of
[
pi(X)Gamma_{m odd}
]
would therefore be sufficient for the existing vacuum-instability criterion. This is the same causal content as the Hardy innerness problem, but now isolated inside one canonical Hodge-current component rather than the full prime--Archimedean distribution.
