# Codex zeta-Gibbs fourth-cumulant checkpoint — 2026-08-27

Codex/GPT work only. No Claude-side material was inspected.

## Correction to the previous checkpoint

The previous all-fronts note correctly warned that a generic fourth cumulant has no fixed sign, but that warning is too weak for the arithmetic zeta-Gibbs family.  For

\[
P_\beta(n)=\frac{n^{-\beta}}{\zeta(\beta)},\qquad E(n)=\log n,\qquad \beta>1,
\]

one has formally, and on this half-line absolutely convergently,

\[
\kappa_r(\beta)=(-1)^r\frac{d^r}{d\beta^r}\log\zeta(\beta)
=\sum_{n\ge2}\Lambda(n)(\log n)^{r-1}n^{-\beta},\qquad r\ge2.
\]

Thus every term in the von-Mangoldt expansion of \(\kappa_4\) is positive.  GPPVerify2 already contains the finite-mode positivity theorem for every positive cumulant order (`PrimePowerCumulantPositivity.lean`) and absolute summability for every finite logarithmic insertion (`VonMangoldtCumulantSummability.lean`).  What is still missing is the exact global identification of the fourth central cumulant with the three-log-inserted von-Mangoldt L-series and then the derivative law

\[
\kappa_3'(\beta)=-\kappa_4(\beta).
\]

## Independent numerical audit

`zeta_gibbs_kappa4_audit.py` compares

\[
\sum_{n\le N}\Lambda(n)(\log n)^3 n^{-\beta}
\]

against high-precision fourth differentiation of `log(zeta(beta))`.  With `N=200000`, 50 decimal digits, representative values are:

| beta | kappa_4 from d^4 log zeta | truncated von-Mangoldt sum | absolute tail/error |
|---:|---:|---:|---:|
| 1.5 | 95.9495491061723 | 82.2946994361981 | 13.6548496699742 |
| 2.0 | 5.96872026946544 | 5.95699759934748 | 0.01172267011796 |
| 3.0 | 0.360657811201248 | 0.360657785442721 | 2.5758527e-8 |
| 5.0 | 0.0188558720446880 | 0.0188558720446880 | 2.2e-18 |

The slow convergence near beta=1 is expected and is not evidence against the identity.  No sign-change evidence was found; direct high-precision values of kappa_4 were positive at beta = 1.01, 1.05, 1.1, 1.2, 1.5, 2, 3, 5, 10, 20.

## Honest claim boundary

This numerical audit is not the proof of global positivity.  The next Lean target is a fourth-cumulant bridge: define/identify the genuine Gibbs fourth central cumulant, prove it equals the real part of the three-log-weighted von-Mangoldt L-series for beta>1, deduce strict positivity from its positive prime-power expansion, and differentiate kappa_3 to obtain `kappa_3' = -kappa_4`.
