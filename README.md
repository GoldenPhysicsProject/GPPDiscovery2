# weil-decay

Search-and-discovery repo for the ground-state decay of the **truncated Weil
quadratic form**.

## The question

Connes–van Suijlekom (Prop 4.1) and Connes–Consani–Moscovici (Lemma 5.1) build,
for a prime cutoff `c` and band `N`, a finite `(2N+1) x (2N+1)` Galerkin matrix
`Q(c)`. CvS Theorem 6.1: the zeros of its characteristic function lie on the
critical line **for every finite c**. Criticality is a theorem. Connes (2026,
§6) poses **convergence** as the open question.

`lambda_min(c)` is the smallest eigenvalue of `Q(c)` on the even sector.
Weil positivity, hence RH, is `lambda_min >= 0` for every `c`.

We are not testing whether it is positive. We are measuring **how fast it
decays**:

> Is `log lambda_min` linear in `log c`, and if so, what is the constant?

Measured so far (unconverged, N=20, T=100): `3.67e-27` at c=7, `8.09e-18` at
c=5. Nine orders in one step. A two-point natural-log slope of about `-64`,
against `-2*gamma_1 = -28.27` and `-4*gamma_1 = -56.55`.

If the constant is arithmetic, this is a quantity that *sees the zeros*, which
is more than can be said for most reformulations of RH.

## Why N-convergence comes first

The current far-end run at `c=19` has reached `N=36,44,52`.  The absolute
smallest eigenvalues continue to move by roughly five to six decimal orders at
each step, so `lambda_1` is **not N-converged** and no c-slope based on the
absolute values is presently meaningful.

The first diagnostic is now basis conditioning: record the smallest eigenvalue
(or an equivalent condition diagnostic) of the overlap/Gram matrix alongside
`lambda_1`.  If they track, the common decay is a degenerating-basis scale
rather than spectral information.  Precision must also scale with
`-log10(lambda_1)`; a fixed decimal budget will eventually manufacture a sign
artifact.

The dimensionless ratio `lambda_1/lambda_2` moves much less than the two
absolute eigenvalues and is worth tracking, but it is not yet certified as an
N-limit.  Grid-spacing and c-dependence tests come before interpreting any
apparent geometric or golden-ratio convergence.

## Running

`python point.py --c 7 --N 36 --T 300 --dps 90` for one point, or push / use
workflow_dispatch to run the whole matrix in parallel on Actions. Results land
in `results.jsonl` and `RESULTS.md`, committed back automatically.

## Caveat on small c

At `c=3, N=20, T=100` we saw `lambda_min = -0.332`. Almost certainly marginal
basis resolution (41 modes on an interval of length 2.2, archimedean quadrature
truncated at T=100); the reference implementation reports the same at c=23, 29
and attributes it to exactly that. The scan re-runs c=3 at N=36, T=300 to
settle it. If it survives, that is a much bigger deal than the slope.

The much smaller negative value previously recorded at `c=29, N=28, T=300,
dps=60` has now been resolved: it was a working-precision artifact. At 90--150
digits the value is stably positive, approximately `1.59354525025e-62`, with a
120-digit residual of `1.64e-121` and successful high-precision Cholesky.
However, the N and T sweeps are still unconverged, so this is not a certified
positivity result and does not rescue a c-slope fit. See
[`discovery/weil_decay/C29_PRECISION_AUDIT.md`](discovery/weil_decay/C29_PRECISION_AUDIT.md).

## Status

Discovery only. Nothing here is proved. Anything that becomes a theorem goes to
[GPPVerify](https://github.com/GoldenPhysicsProject/GPPVerify) for Lean 4
formalization, and the first thing that should graduate is **certified
enclosures** for `lambda_min > 0` via interval arithmetic, not another
equivalence.
