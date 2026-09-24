# RH discovery: half-density zeta gauge is subexponentially conditioned
## Exact von Mangoldt connection and finite divisor-space bounds

**Date:** 2026-09-24  
**Status:** exact finite arithmetic theorem plus elementary norm bounds. This does not by itself control the completed scalar Weil pullback and is not an RH proof.

## 1. Finite divisor Hilbert space

Let \(S\subset\mathbb N\) be finite and divisor-closed, with
\[
X=\max S,\qquad L=\log X.
\]
Work on \(\ell^2(S)\).

Define half-density zeta synthesis
\[
\boxed{
(Zf)(n)=\sum_{\substack{d\mid n\\ d\in S}}
\sqrt{\frac dn}\,f(d).
}
\tag{1}
\]

Define the half-density Möbius operator
\[
\boxed{
(Mf)(n)=\sum_{\substack{d\mid n\\ d\in S}}
\mu(n/d)\sqrt{\frac dn}\,f(d).
}
\tag{2}
\]

Because the arithmetic kernels
\[
a(m)=m^{-1/2},
\qquad
b(m)=\mu(m)m^{-1/2}
\]
satisfy
\[
(a*b)(m)
=
m^{-1/2}\sum_{d\mid m}\mu(d)
=
\delta_{m1},
\]
one has exactly
\[
\boxed{MZ=ZM=I.}
\tag{3}
\]

Thus \(M=Z^{-1}\).

## 2. Exact half-density logarithmic gauge identity

Let
\[
(Df)(n)=\log n\,f(n).
\]

A direct calculation gives
\[
DZ-ZD=L_{\Lambda}Z,
\]
or equivalently
\[
\boxed{
MDZ-D=L_{\Lambda},
}
\tag{4}
\]
where
\[
\boxed{
(L_{\Lambda}f)(n)
=
\sum_{d\mid n}
\Lambda(n/d)
\sqrt{\frac dn}\,f(d).
}
\tag{5}
\]

Indeed,
\[
(DZ-ZD)_{n,d}
=
(\log n-\log d)\sqrt{\frac dn}\,1_{d\mid n}
=
\log(n/d)\sqrt{\frac dn}\,1_{d\mid n},
\]
and Möbius inversion changes \(\log\) into the von Mangoldt function.

Equation (4) is the half-density matrix realization of the already formalized
Dirichlet logarithmic gauge identity
\[
\mu*D(\zeta*f)-Df=\Lambda*f.
\]

The critical \(n^{-1/2}\) weight is built into the synthesis itself.

## 3. Schur bound for zeta and Möbius synthesis

Use Schur weights
\[
p_n=n^{-1/2}.
\]

For \(Z\), the weighted row sum is
\[
\frac1{p_n}
\sum_d |Z_{n,d}|p_d
=
\sqrt n
\sum_{d\mid n}
\sqrt{\frac dn}\,\frac1{\sqrt d}
=
\tau(n).
\]

Therefore
\[
A_S
:=
\sup_n
\frac1{p_n}
\sum_d|Z_{n,d}|p_d
\le
\tau_{\max}(X),
\]
where
\[
\tau_{\max}(X)=\max_{n\le X}\tau(n).
\]

For a fixed column \(d\), write \(n=dm\). Then
\[
\frac1{p_d}
\sum_n |Z_{n,d}|p_n
=
\sum_{\substack{m\ge1\\dm\in S}}\frac1m
\le
H_{\lfloor X/d\rfloor}
\le
1+\log X.
\]

Schur's test therefore gives
\[
\boxed{
\|Z\|_{2\to2}
\le
\sqrt{
\tau_{\max}(X)(1+L)
}.
}
\tag{6}
\]

The same estimate holds for \(M\), because
\[
|\mu(n/d)|\le1:
\]
\[
\boxed{
\|M\|_{2\to2}
\le
\sqrt{
\tau_{\max}(X)(1+L)
}.
}
\tag{7}
\]

## 4. Subexponential conditioning

The elementary divisor estimate
\[
\forall\varepsilon>0\quad
\tau(n)\le C_\varepsilon n^\varepsilon
\]
implies
\[
\tau_{\max}(e^L)=e^{o(L)}.
\]

For completeness, this estimate needs no prime number theorem. Choose \(P\) so
large that \(p^\varepsilon\ge2\) for every prime \(p>P\). For those primes,
\[
a+1\le2^a\le p^{\varepsilon a}.
\]
The finitely many primes \(p\le P\) contribute only a finite constant after
maximizing
\[
(a+1)p^{-\varepsilon a}
\]
over \(a\ge0\). Multiplication over the prime factorization gives the claim.

Hence
\[
\boxed{
\|Z\|,\|M\|=e^{o(L)}.
}
\tag{8}
\]

The half-density arithmetic synthesis and its Möbius inverse are therefore
subexponentially conditioned in logarithmic support.

## 5. Subexponential von Mangoldt connection

Since
\[
\|D\|\le L,
\]
equations (4), (6), and (7) yield
\[
\|L_\Lambda\|
=
\|MDZ-D\|
\le
\|M\|\,\|D\|\,\|Z\|+\|D\|.
\]

Therefore
\[
\boxed{
\|L_\Lambda\|
\le
L\left[
1+
(1+L)\tau_{\max}(e^L)
\right]
=
e^{o(L)}.
}
\tag{9}
\]

This is a zero-independent operator-norm bound for the critical half-density
von Mangoldt connection.

## 6. Relation to the vacuum-instability criterion

The new RH stability theorem only asks for a subexponential lower floor:
\[
e(R)\ge-\exp(o(R)).
\]

Equation (9) shows that the prime connection itself already has exactly the
required growth scale in the natural divisor/zeta-gauge Hilbert geometry.

So the exponential instability associated with an off-critical zero cannot be
blamed on the intrinsic size of the half-density von Mangoldt connection.

It can only enter when the arithmetic parent is pulled back to the completed
one-dimensional scalar boundary.

This localizes the remaining problem sharply:

\[
\boxed{
\text{control the norm of the completed scalarization / boundary map}.
}
\]

## 7. Relation to the formalized zeta-gauge Gram square

The existing finite zeta-gauge positivity theorem has
\[
G=Z^TZ,
\qquad
H=Z^T\operatorname{diag}(d)Z,
\]
with
\[
x^THx
=
\|D^{1/2}Zx\|^2\ge0.
\]

The present theorem adds quantitative conditioning:
\[
Z,\ Z^{-1},\ L_\Lambda
\]
all have only subexponential norm in logarithmic cutoff.

This is exactly the scale required by the newly derived RH vacuum-stability
criterion.

The missing step is not finite positivity or arithmetic conditioning. It is
the completed Poisson/Archimedean scalar trace.

## 8. Warning: this does not revive the old periodization argument

Earlier work proved that raw periodization is not closable in the Gamma
Sobolev topology: it samples point values of a Fourier transform while the
Gamma norm controls only weighted \(L^2\) data.

The theorem above lives in a different space: the finite divisor/zeta-gauge
Hilbert geometry.

Therefore one may not simply compose (9) with raw periodization and claim a
scalar bound.

A genuine completion must include the Archimedean smoothing/shadow boundary.
The next discovery note attacks exactly that map using the fixed Riemann seed
\(\phi\).
