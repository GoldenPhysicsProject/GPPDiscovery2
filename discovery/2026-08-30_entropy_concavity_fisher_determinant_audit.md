# Codex continuation: entropy concavity and Fisher determinant audit

Date: 2026-08-30

## Verify2 repair

The root-build failure in `CausalPrimeHeatBridge.lean` was a normalization/rewrite mismatch, not a mathematical failure.  The exact local bridge remains

\[
\frac{\log p}{\sqrt{p^{m+1}}}\,g_t((m+1)\log p)
=
\frac{\Lambda(p^{m+1})}{\sqrt{p^{m+1}}}\,g_t(\log p^{m+1}).
\]

The repair rewrites `repetition m = m+1` at the interface to the already-proved von-Mangoldt prime-power theorem and uses the exact logarithmic prime-power identity.

## Zeta Gibbs entropy/free energy

The entropy-sign hypothesis previously carried by the free-energy curvature theorem has now been discharged on the honest Gibbs half-line `beta > 1`.

The formalized route is

\[
Z(\beta)\ge 1,
\qquad
\log Z(\beta)\ge 0,
\qquad
U(\beta)\ge 0,
\]

hence

\[
S(\beta)=\log Z(\beta)+\beta U(\beta)\ge0.
\]

Together with strict Gibbs variance `kappa_2(beta)>0`, the exact curvature law

\[
F''(\beta)
=-\frac{\kappa_2(\beta)}{\beta}
-\frac{2S(\beta)}{\beta^3}
\]

therefore gives the unconditional theorem

\[
\boxed{F''(\beta)<0\qquad(\beta>1).}
\]

This is a genuine strengthening: entropy nonnegativity is no longer a hypothesis.

## Prime Fisher determinant audit

The all-order strict Gram theorem already gives

\[
\sum_n w_\beta(n)[p(\log n)]^2>0
\]

for every nonzero real polynomial `p` and `beta > 1`.  The two-statistic specialization `p(x)=a x+b x^2` is already formalized.

The Schur bridge is also already formalized:

\[
\det H_3=m_0^3\det\operatorname{Cov}(X,X^2),
\]

with positive mass transferring strict raw-Hankel determinant positivity to strict centered covariance determinant positivity.

What is *not yet packaged as a single unconditional theorem* is the final infinite-support determinant statement.  The clean route is to combine strict positivity for every centered nonzero quadratic score with the elementary `2x2` positive-definite determinant lemma, or equivalently establish the general Cauchy--Binet/Vandermonde lift for the countable moment matrix.  Do not claim the determinant theorem closed until that final bridge is formalized.

## Scalar-box frontier

No change in the honest blocker.  Pointwise convergence, one-channel domination, Beta integrability, nested Beta reduction, and zero-regulator volume `1/6` are already certified.  The remaining step is the measure-theoretic nested dominated-convergence bridge

\[
J_\varepsilon(S,T)\to\frac16.
\]

Once this is formalized, the existing Gamma residue/dimension-shift assembly gives the finite `mu^4` term `-1/6`.

## Spectral / principal-series / YM status

No new spectral or YM claim is introduced here.  Preserve the direct-convolution versus Wiener--Hopf chamber separation; the Mehler--Fock-to-dilog analytic reconstruction remains open.  The YM frontier remains convention-complete numerator sewing and generalized cuts after scalar regulator closure.
