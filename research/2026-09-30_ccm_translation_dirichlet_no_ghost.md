# CCM pole-removed form as an exact translation Dirichlet energy minus a mass

Date: 2026-09-30  
Status: exact finite-window algebra derived directly from the CCM matrix formulas already reproduced in the project. No RH claim.

This note continues the pole-calibrated neutral reduction. The key point is that the
pole-removed operator
\[
A=-W_{\mathbb R}-W_P
\]
is not an opaque dense matrix: it is exactly a positive weighted translation-difference
Dirichlet form minus one scalar mass term.

That turns the remaining no-ghost statement into one sharp Poincaré inequality.

## 1. Fourier window and the CCM overlap kernel

Fix \(L>0\) and the normalized Fourier basis on \([0,L]\),
\[
U_n(x)=L^{-1/2}e^{2\pi i n x/L},\qquad n\in\mathbb Z.
\]

Let
\[
f(x)=\sum_{|n|\le N} c_n U_n(x)
\]
on \([0,L]\), extended by zero to the full real line.

For \(0\le y\le L\), define the one-sided overlap
\[
C_f(y)=\int_0^{L-y} f(x+y)\overline{f(x)}\,dx.
\]

A direct basis calculation gives
\[
2\Re C_f(y)
=
\sum_{n,m}\overline{c_n}c_m\,q_{nm}(y),
\]
where
\[
q_{nm}(y)=
\begin{cases}
\dfrac{\sin(2\pi m y/L)-\sin(2\pi n y/L)}
{\pi(n-m)},&n\ne m,\\[1.2ex]
2(1-y/L)\cos(2\pi n y/L),&n=m.
\end{cases}
\]

This is exactly the CCM kernel called \(q(U_n,U_m)(y)\).

Therefore
\[
\boxed{q(f,f)(y)=2\Re C_f(y).}
\]

## 2. Translation-difference identity

Let \(T_y\) denote full-line translation of the zero extension,
\[
(T_yf)(x)=f(x-y).
\]

Since translation is unitary on \(L^2(\mathbb R)\),
\[
\|f-T_yf\|_2^2
=
2\|f\|_2^2
-
2\Re\langle T_yf,f\rangle.
\]

For \(0\le y\le L\), the overlap of the supports is exactly the integral defining
\(C_f(y)\). Hence
\[
\boxed{
q(f,f)(y)
=
2\|f\|_2^2-\|f-T_yf\|_2^2.
}
\]

Put
\[
E_y(f):=\|f-T_yf\|_2^2\ge0.
\]

The CCM \(q\)-kernel is therefore a correlation kernel, and its complement is a genuine
Dirichlet translation energy.

## 3. Archimedean form

The reproduced CCM formulas use
\[
\rho(y)=\frac{e^{y/2}}{e^y-e^{-y}},
\qquad
\operatorname{tail}(L)
=
\frac12\log\frac{e^L+1}{e^L-1}.
\]

The diagonal formula contains the local subtraction
\[
\frac{2}{e^y-e^{-y}}
=
\frac1{\sinh y}.
\]

Substituting
\[
q(f,f)(y)=2\|f\|^2-E_y(f)
\]
into the exact archimedean matrix formula and collecting the scalar terms yields
\[
\boxed{
W_{\mathbb R}(f)
=
\kappa_R(L)\|f\|_2^2
-
\int_0^L\rho(y)E_y(f)\,dy,
}
\]
with the finite real scalar
\[
\boxed{
\kappa_R(L)
=
\log(4\pi)+\gamma_E
+
\int_0^L
\frac{e^{y/2}-1}{\sinh y}\,dy
-
\log\coth(L/2).
}
\]

The apparent \(y=0\) singularities cancel in the displayed integrand.

## 4. Prime-power form

Let
\[
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
P_L=\sum_{2\le n\le e^L} w_n.
\]

The finite CCM prime form is
\[
W_P(f)
=
\sum_{2\le n\le e^L}
w_n\,q(f,f)(\log n).
\]

Using the translation identity,
\[
\boxed{
W_P(f)
=
2P_L\|f\|_2^2
-
\sum_{2\le n\le e^L}
\frac{\Lambda(n)}{\sqrt n}
E_{\log n}(f).
}
\]

Thus every prime-power contribution supplies a positive translation-difference energy
to \(-W_P\), together with a scalar mass subtraction.

## 5. Exact Dirichlet-minus-mass decomposition of the pole-removed form

Recall
\[
A=-W_{\mathbb R}-W_P.
\]

Define
\[
\mathcal D_L(f)
=
\int_0^L\rho(y)\|f-T_yf\|_2^2\,dy
+
\sum_{2\le n\le e^L}
\frac{\Lambda(n)}{\sqrt n}
\|f-T_{\log n}f\|_2^2.
\]

Every coefficient is nonnegative, so
\[
\mathcal D_L(f)\ge0.
\]

Define the scalar
\[
\mu_L=\kappa_R(L)+2P_L.
\]

Then the exact identity is
\[
\boxed{
\langle f,Af\rangle
=
\mathcal D_L(f)-\mu_L\|f\|_2^2.
}
\]

This is the main result of the note.

The pole-removed prime--Archimedean operator is therefore a nonlocal symmetric Markov /
Dirichlet generator shifted by a scalar mass.

## 6. Fourier symbol on the full line

For a full-line test function for which the translation representation is literal,
Plancherel gives
\[
\|f-T_yf\|_2^2
=
\int_{\mathbb R}
2(1-\cos(\xi y))|\widehat f(\xi)|^2\,d\xi.
\]

Formally, and exactly on the zero-extended finite-window domain after the corresponding
compression, the positive part has symbol
\[
\boxed{
\Psi_L(\xi)
=
2\int_0^L\rho(y)(1-\cos(\xi y))\,dy
+
2\sum_{2\le n\le e^L}
\frac{\Lambda(n)}{\sqrt n}
(1-\cos(\xi\log n)).
}
\]

Hence \(A\) is a compressed Lévy/translation-difference generator minus \(\mu_L\).

This does NOT prove positivity, because the hard question is precisely whether the
relevant constrained spectral gap reaches the sharp value \(\mu_L\).

## 7. Insert the exact pole-neutral reduction

From the previous note, with
\[
Q=A+\frac12|c\rangle\langle c|-\frac12|s\rangle\langle s|
\]
and the exact pole calibration
\[
\langle c,A_+^{-1}c\rangle=-2,
\qquad
\langle s,A_-^{-1}s\rangle=2,
\]
the full completed form satisfies
\[
Q\succeq0
\iff
A|_{\mathcal N}\succeq0,
\]
where
\[
\mathcal N
=
\{f:\langle c,f\rangle=\langle s,f\rangle=0\}.
\]

Equivalently, in logarithmic coordinates,
\[
\mathcal N\cap C_c^\infty
=
\left(\partial_u^2-\frac14\right)C_c^\infty.
\]

Combining this with the Dirichlet decomposition gives the sharp current target:
\[
\boxed{
\mathcal D_L(f)\ge\mu_L\|f\|_2^2
\qquad
(f\in\mathcal N).
}
\]

Thus RH/no-ghost has been compressed to a two-moment constrained Poincaré inequality
for an explicit positive jump/translation form.

## 8. Boundary-source identities from the Riemann radical

Let
\[
C=\langle c,\Phi\rangle.
\]
The exact even calibration gives
\[
A\Phi=-\frac C2\,c.
\]

Since
\[
\langle s,\Phi'\rangle=-\frac C2,
\]
the odd calibration gives
\[
A\Phi'=-\frac C4\,s.
\]

Writing
\[
e_+=e^{u/2},\qquad e_-=e^{-u/2},
\qquad
c=e_++e_-,
\qquad
s=e_+-e_-,
\]
one obtains
\[
\boxed{
A(\Phi+2\Phi')=-C\,e_+,
\qquad
A(\Phi-2\Phi')=-C\,e_-.
}
\]

These two vectors are exact Green/Poisson boundary-source solutions for the two pole
channels. They are \(A\)-orthogonal to every neutral test vector.

This strongly suggests that the correct square, if it exists, is a two-boundary
ground-state/Doob transform rather than an ordinary one-ground-state transform.

No positivity conclusion is drawn from this identity alone.

## 9. Relation to previous no-go results

This factorization does not contradict the earlier small-divisor obstructions.

A finite collection of prime shifts alone has irrational-rotation approximate invariants and no
coercive Hodge gap. The present \(\mathcal D_L\) is different:
- it contains the full Archimedean continuum of translation differences;
- it includes all prime powers up to the window scale;
- the two pole channels are removed before asking for the sharp lower bound.

Likewise, the completed logarithmic-derivative Krein square at fixed \(q>1\) was shown to
remain indefinite because the two negative pole sectors are not locally dominated.
Here those two sectors have been separated and exactly calibrated first.

## 10. What would finish the route

A proof of
\[
\mathcal D_L(f)\ge\mu_L\|f\|_2^2
\]
on the two-pole-neutral subspace, uniformly in the completed window/exhaustion, would give:
\[
A|_{\mathcal N}\succeq0
\Longrightarrow
Q\succeq0
\Longrightarrow
\text{Weil positivity}
\Longrightarrow
\mathrm{RH}.
\]

The statement is sharp. A coarse Poincaré estimate is not enough; the constant has to be the exact
\(\mu_L\).

The most promising analytic languages for this exact inequality are now:
- a two-boundary ground-state transform using the exact \(\Phi\pm2\Phi'\) source solutions;
- generalized Nevanlinna/Loewner theory after the two moment constraints;
- a nonlocal Sturm/Courant oscillation theorem for the compressed translation generator;
- an arithmetic Cheeger/Poincaré inequality in which the Archimedean continuum and prime jumps
  are treated before any estimate.

The advantage is that the hard object is now a positive Dirichlet form with an explicit sharp
spectral threshold, rather than the original dense Weil matrix.
