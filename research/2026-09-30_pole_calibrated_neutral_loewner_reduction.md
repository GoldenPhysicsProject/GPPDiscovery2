# Pole-calibrated neutral reduction and exact Loewner interpolant for the CCM form

Date: 2026-09-30
Status: exact algebraic reduction + exact interpolation identity extracted from the CCM matrix formulas. No RH claim.

This note sharpens the 2026-09-29 Riemann-vacuum pole-threshold observation and audits the suggested Herglotz/inertia route.

## 1. Setup

Write the completed finite/semilocal Weil form in parity blocks as

\[
Q=A+\frac12|c\rangle\langle c|-\frac12|s\rangle\langle s|,
\]

with
- \(A=-W_{\mathbb R}-W_P\) the pole-removed prime--Archimedean part,
- \(c\) even,
- \(s\) odd.

Assume the parity restrictions \(A_+\), \(A_-\) are invertible.

The exact global Riemann-kernel radical calibration gives, whenever the corresponding
radical vectors belong to the admitted completion,

\[
\langle c,A_+^{-1}c\rangle=-2,\qquad
\langle s,A_-^{-1}s\rangle=2.
\]

The important point below is that ONCE these two scalar identities are known, there is no
need to prove the full inertia statement first.

## 2. Exact pole-calibrated neutral decomposition

Define the neutral subspace

\[
\mathcal N
=
\{x:\langle c,x\rangle=\langle s,x\rangle=0\}.
\]

For every vector \(x=x_++x_-\) there is a unique decomposition

\[
x
=
y
+\alpha A_+^{-1}c
+\beta A_-^{-1}s,
\qquad
y\in\mathcal N.
\]

Indeed the two calibration scalars are nonzero, so the coefficients are fixed by the two
boundary charges.

Because \(y\) is neutral,

\[
\langle y,A A_+^{-1}c\rangle=\langle y,c\rangle=0,
\qquad
\langle y,A A_-^{-1}s\rangle=\langle y,s\rangle=0.
\]

For the even boundary direction,

\[
\langle A_+^{-1}c,A A_+^{-1}c\rangle
=
\langle c,A_+^{-1}c\rangle=-2,
\]
while
\[
\frac12|\langle c,A_+^{-1}c\rangle|^2
=
\frac12|-2|^2=2.
\]
They cancel exactly.

For the odd boundary direction,

\[
\langle A_-^{-1}s,A A_-^{-1}s\rangle
=
\langle s,A_-^{-1}s\rangle=2,
\]
while
\[
-\frac12|\langle s,A_-^{-1}s\rangle|^2
=
-\frac12|2|^2=-2.
\]
They cancel exactly.

Therefore

\[
\boxed{
\langle x,Qx\rangle
=
\langle y,Ay\rangle.
}
\]

This is an exact congruence, not an asymptotic statement.

Consequences:

\[
\boxed{
Q\succeq0
\iff
A|_{\mathcal N}\succeq0.
}
\]

Moreover, if \(A|_{\mathcal N}>0\), then automatically

\[
n_-(A_+)=1,\qquad n_-(A_-)=0,
\]

because the one-dimensional \(A\)-orthogonal complements have signs \(-2\) and \(+2\),
respectively.

So the most economical route is NOT

1. prove the two inertia statements;
2. then use the pole thresholds.

It is

1. calibrate the pole directions exactly using the Riemann radical;
2. prove positivity only on the codimension-two neutral space.

The inertia theorem then follows as a corollary.

This is the precise no-ghost/gauge-fixed form of the problem.

## 3. Neutrality is exactly annihilation of the two pole modes

In logarithmic coordinate \(u\), the two boundary modes are

\[
e_+(u)=e^{u/2},\qquad e_-(u)=e^{-u/2},
\]

with

\[
c=e_++e_-,
\qquad
s=e_+-e_-.
\]

Thus

\[
\langle c,f\rangle=\langle s,f\rangle=0
\iff
\langle e_+,f\rangle=\langle e_-,f\rangle=0.
\]

Equivalently the Mellin/Fourier transform of \(f\) vanishes at the two elementary pole
points \(z=\pm i/2\), i.e. at \(s=0,1\).

## 4. Exact differential-range realization of the neutral space

Let

\[
L_0=\frac{d^2}{du^2}-\frac14.
\]

Then

\[
L_0 e^{\pm u/2}=0.
\]

Hence for every \(g\in C_c^\infty(\mathbb R)\),

\[
f=L_0g
\]

is neutral by integration by parts.

Conversely, let \(f\in C_c^\infty(\mathbb R)\) satisfy

\[
\int e^{u/2}f(u)\,du=0,
\qquad
\int e^{-u/2}f(u)\,du=0.
\]

A fundamental solution of \(L_0\) is

\[
G(u)=-e^{-|u|/2}.
\]

Put \(g=G*f\). Outside the support of \(f\), the two tails of \(g\) are proportional to

\[
e^{-u/2}\int e^{v/2}f(v)\,dv
\]

on the right and

\[
e^{u/2}\int e^{-v/2}f(v)\,dv
\]

on the left. The two neutral moments kill these tails exactly. Thus \(g\) is compactly
supported and \(L_0g=f\).

Therefore

\[
\boxed{
\mathcal N\cap C_c^\infty
=
L_0(C_c^\infty).
}
\]

This gives a second exact formulation of the hard sign:

\[
A|_{\mathcal N}\succeq0
\iff
\langle L_0g,A L_0g\rangle\ge0
\quad\forall g\in C_c^\infty.
\]

The operator \(L_0\) is not an arbitrary trick: it is the unique constant-coefficient
second-order operator annihilating the two completed pole modes \(e^{\pm u/2}\).

This is the correct place to test any proposed Ward/Hodge square identity.

## 5. Exact Loewner structure of the finite CCM pole-removed matrix

The CCM builder uses \(L=2\log\lambda\), Fourier indices \(n=-N,\dots,N\), and

\[
\rho(y)=\frac{e^{y/2}}{e^y-e^{-y}}.
\]

For a prime power \(k\le e^L\), write

\[
y_k=\log k,\qquad
w_k=\frac{\Lambda(k)}{\sqrt{k}}.
\]

Define the REGULARIZED real analytic interpolant

\[
\begin{aligned}
b_L(x)
={}&
\frac1\pi\int_0^L
\frac{
e^{y/2}\sin\!\bigl(2\pi x(1-y/L)\bigr)-\sin(2\pi x)
}{
e^y-e^{-y}
}\,dy\\
&+
\frac{\log(4\pi)+\gamma-2\,\mathrm{tail}(L)}{2\pi}
\sin(2\pi x)\\
&+
\frac1\pi
\sum_{k\le e^L}
\frac{\Lambda(k)}{\sqrt{k}}
\sin\!\bigl(2\pi x(1-y_k/L)\bigr),
\end{aligned}
\]

where

\[
\mathrm{tail}(L)
=
\frac12\log\frac{e^L+1}{e^L-1}.
\]

The subtraction by \(\sin(2\pi x)\) inside the integral is essential: it cancels the
\(1/y\) singularity at \(y=0\). It vanishes at integer nodes, so it does not change the
off-diagonal sampled values.

At an integer \(n\),

\[
\sin(2\pi n(1-y/L))
=
-\sin(2\pi n y/L),
\]

and

\[
\cos(2\pi n(1-y/L))
=
\cos(2\pi n y/L).
\]

Direct differentiation therefore gives exactly the CCM formulas:

\[
(W_{\mathbb R}+W_P)_{nm}
=
\begin{cases}
\dfrac{b_L(n)-b_L(m)}{n-m},&n\ne m,\\[1.2ex]
b_L'(n),&n=m.
\end{cases}
\]

Thus

\[
\boxed{
W_{\mathbb R}+W_P
=
\operatorname{Loewner}_{\{-N,\dots,N\}}(b_L),
}
\]

and

\[
\boxed{
A
=
\operatorname{Loewner}_{\{-N,\dots,N\}}(-b_L).
}
\]

This is exact, zero-free, and follows only from the displayed CCM prime and
Archimedean formulas.

## 6. Important correction to the proposed Herglotz shortcut

It is legitimate to say that \(A\) is an exact Loewner matrix of the explicit function
\(-b_L\).

It is NOT yet legitimate to say that \(-b_L\) is Herglotz/Pick.

Ordinary Pick/Herglotz would make every Loewner matrix positive semidefinite, whereas
the observed \(A_+\) has one substantial negative direction. The correct possible target
is a generalized Nevanlinna/Pick statement with a controlled number of negative squares,
or a Pick statement AFTER the two pole/neutral degrees of freedom have been removed.

In other words:

\[
\text{Loewner structure = proved},
\]

but

\[
\text{the required Pick / generalized-Pick sign = the open theorem}.
\]

Assuming Herglotz here would simply assume the missing positivity in another language.

## 7. A cleaner analytic target

Combining Sections 2 and 5, the finite problem can be stated as:

> Prove that the Loewner form of \(-b_L\) is nonnegative on the two-moment neutral
> subspace
> \[
> \sum_n \bar c_n\,\widehat e_+(n)=
> \sum_n \bar c_n\,\widehat e_-(n)=0.
> \]

Equivalently, prove positivity of the pulled-back kernel

\[
L_0^*\,A\,L_0
\]

on compactly supported smooth functions.

If this is established in the completed window/exhaustion with the exact \(\Phi,\Phi'\)
calibration, the full Weil form is positive by the congruence of Section 2.

This is sharper than a brute eigenvalue sweep and sharper than proving the two inertia
statements separately.

## 8. Numerical falsifier retained, not promoted to proof

A fast independent double-precision sweep of the exact CCM formulas at \(N=12\) over

\[
\lambda=1.2,1.5,2,2.5,3,3.5,4,5
\]

found one substantial negative eigenvalue in the even block of \(A\) and no substantial
negative eigenvalue in the odd block. Near-zero eigenvalues rapidly reach floating-point
scale as \(\lambda\) grows, so this sweep is useful only as a falsifier.

It supports the target but cannot certify the vanishing margins.

## 9. Current preferred route

1. Land the finite-Haar principal-series norm law.
2. Formalize the abstract pole-calibrated neutral congruence in Lean.
3. Treat the explicit \(b_L\) above as the exact finite analytic object.
4. Attack neutral Loewner positivity / generalized Nevanlinna index, NOT a presumed
   Herglotz property.
5. In parallel, test whether the differential pullback \(L_0^* A L_0\) admits the missing
   nonlocal Poisson/Archimedean Gram factorization.
6. Keep the Hardy-strip quotient as an independent closure route: if the physical
   Poisson-sewn quotient has subexponential two-sided scale growth, zero retention already
   forces the principal series.

The hard joint is now isolated very narrowly:
a two-pole-neutralized, explicitly sampled Loewner form.
