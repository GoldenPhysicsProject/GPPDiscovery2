# The RH two-channel obstruction as exact Gaussian cumulant renormalization

Date: 2026-09-27  
Status: exact finite-cutoff identity and critical-limit interpretation. No RH proof.

## 1. Start from the Schatten-3 Euler determinant

On the prime one-particle space let
\[
D(s)e_p=p^{-s}e_p.
\]

For \(\Re s>1\),
\[
\log\zeta(s)
=
P(s)+\frac12P(2s)-\log\det_3(I-D(s)),
\]
where
\[
P(s)=\sum_p p^{-s}.
\]

Equivalently,
\[
\boxed{
\zeta(s)
=
\frac{\exp(P(s)+\frac12P(2s))}
{\det_3(I-D(s))}.
}
\]

The determinant term contains exactly the repetition sectors \(m\ge3\).

## 2. The missing \(m=1,2\) factor is a Gaussian moment-generating function

For one complex number \(x\),
\[
e^{x+x^2/2}
\]
is the analytic continuation of the moment-generating function of a real Gaussian random variable
\[
G\sim N(1,1):
\qquad
\mathbb E[e^{xG}]
=
e^{x+x^2/2}.
\]

For a finite prime set \(\mathcal P\), let \(G_p\) be independent \(N(1,1)\) variables and put
\[
x_p=p^{-s}.
\]

Then
\[
\boxed{
\exp\left(
\sum_{p\in\mathcal P}x_p
+\frac12\sum_{p\in\mathcal P}x_p^2
\right)
=
\mathbb E
\exp\left(
\sum_{p\in\mathcal P}x_pG_p
\right).
}
\]

Therefore the entire primitive-plus-double-prime boundary factor has an exact finite-cutoff Gaussian realization.

The \(m=1\) term is the Gaussian mean and the \(m=2\) term is its variance/covariance term.

## 3. Why exactly two channels fail at the critical boundary

At
\[
s=\frac12+it,
\]
\[
|x_p|=p^{-1/2}.
\]

Hence
\[
\sum_p|x_p|^2
=
\sum_p\frac1p
=
\infty.
\]

So the Gaussian series associated with the two-channel factor does not define an ordinary square-integrable random variable on the prime Hilbert space.

But
\[
\sum_p|x_p|^q<\infty
\qquad(q>2).
\]

This is exactly the operator statement
\[
D(1/2+it)\in\mathfrak S_q
\quad(q>2),
\]
in particular
\[
D\in\mathfrak S_3
\quad\text{but}\quad
D\notin\mathfrak S_2.
\]

Thus the previously isolated analytic fact

\[
\boxed{
\text{only }m=1,2\text{ require boundary completion}
}
\]

has an exact probabilistic meaning:

\[
\boxed{
\text{only the first two cumulants fail to be globally finite.}
}
\]

All cumulants of order \(m\ge3\) are already trace-controlled by the Schatten-3 determinant.

## 4. Relation to the TFD covariance

At real critical half-density, the prime TFD normal covariance is
\[
C_p=\frac1{p-1}
=
\frac{p^{-1}}{1-p^{-1}}.
\]

Its leading ultraviolet behavior is
\[
C_p\sim p^{-1}=|x_p|^2.
\]

Hence the same harmonic-prime divergence that destroys the ordinary Gaussian variance is the divergence of total critical TFD occupation:
\[
\sum_p C_p=\infty.
\]

Meanwhile
\[
\sum_pC_p^2<\infty.
\]

So the following are the same critical threshold seen in three languages:

1. \(D\notin\mathfrak S_2\) but \(D\in\mathfrak S_3\);
2. the first two Euler cumulants need renormalization;
3. the critical prime TFD covariance is not trace class but is Hilbert--Schmidt.

## 5. QFT-style reading

For finite prime cutoff, the boundary factor is an ordinary Gaussian expectation.

At the critical infinite-prime boundary, the covariance ceases to be trace class, so the natural object is no longer an ordinary Gaussian vector in the base Hilbert space. It must be treated as a generalized/rigged Gaussian field with a renormalized exponential.

This is exactly the kind of situation in which vacuum subtraction/Wick ordering becomes structural rather than optional.

The earlier TFD calculation already showed:
- full covariance + vacuum half-quantum is positive;
- normal ordering removes the vacuum term and creates an indefinite relative form.

The determinant calculation now says the same thing globally:
- the finite Euler system has a positive Gaussian first-two-cumulant realization;
- the critical infinite system requires a nontrivial renormalization of mean and covariance;
- the higher non-Gaussian remainder is already under operator control.

## 6. New formulation of the Archimedean task

The real place should not be viewed as an arbitrary extra correction.

It must provide the canonical renormalization of the divergent Gaussian mean/covariance of the prime boundary field while preserving the already well-defined \(\det_3\) bulk.

In other words, the two-channel Archimedean completion problem can be sharpened to:

\[
\boxed{
\text{construct the real-place counterterm/covariance completion that turns the cylindrical prime Gaussian boundary into a positive global Gaussian standard form.}
}
\]

If that completed covariance is the Weyl/Gram covariance whose Schur complement is \(m_*(u)\), its positivity is exactly the missing no-ghost theorem and hence would prove RH.

Nothing here supplies that final positivity. The gain is that the unresolved two-channel problem is now identified as an exact second-order cumulant renormalization problem rather than an unspecified prime divergence.
