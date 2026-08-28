# AFT minimal interval-state positivity target

Date: 2026-08-28

## Exact reduction

The arithmetic principal-series program already identifies the scalar box functional

\[
\Psi(L)=\langle \mathcal W,(L-a)_+\rangle
\]

with Suzuki's screw function and proves the exact criterion

\[
\mathrm{RH}\iff \Psi(L)\ge 0\quad\text{for every }L\ge0.
\]

The triangular kernel is the autocorrelation/translation overlap of the causal interval state

\[
f_L=\mathbf 1_{[0,L]},\qquad
(L-a)_+=\langle f_L,V_a f_L\rangle\quad(a\ge0).
\]

Therefore a full arithmetic Osterwalder--Schrader theorem on every admissible test function is stronger than is necessary for RH.  It is enough to construct a zero-independent positive physical realization of this one cyclic family of interval states.

The sharp target is

\[
\boxed{\Psi(L)=\|J_L f_L\|_{\mathcal H_{\rm phys}}^2}
\qquad(L\ge0),}
\]

where the map/quotient \(J_L\) is built solely from prime--Archimedean/Tate data.  This immediately gives Suzuki positivity and hence RH.

## Defect formulation

A weaker but still sufficient architecture is a pair of zero-independent channels

\[
A_L f_L\in\mathcal H_+,
\qquad
B_L f_L\in\mathcal H_-
\]

such that

\[
\Psi(L)=\|A_Lf_L\|^2-\|B_Lf_L\|^2
\]

and

\[
\|B_Lf_L\|\le \|A_Lf_L\|.
\]

Equivalently, after identifying the two sectors through an ambient positive space, one seeks a contraction \(B\) with

\[
\boxed{I-B^*B\succeq0}
\]

on the interval-state cyclic subspace, not necessarily on the entire arithmetic test-function space.

This is materially weaker than proving global Weil positivity ab initio.

## Exact arithmetic box formula

Using the completed boundary distribution

\[
\mathcal W=\nu_\infty-\nu_p,
\]

with

\[
w_\infty(a)=e^{-a/2}+e^{a/2}-\frac{e^{-a/2}}{1-e^{-2a}},
\]

and

\[
A_\infty(1)
=\frac83-\frac12(\log\pi+\gamma)+\frac\pi4-\frac32\log2,
\]

the interval pairing is explicitly

\[
\Psi(L)
=A_\infty(1)L
+\int_0^L w_\infty(a)\bigl[(L-a)-Le^{-a}\bigr]\,da
-\sum_{\log n\le L}\frac{\Lambda(n)}{\sqrt n}(L-\log n).
\]

This contains no zero data.  Any proposed factorization must reproduce this signed linear quantity exactly.

## Important no-go

Taking a Hilbert--Schmidt norm of the already-constructed coupled commutator cannot solve the problem: that norm is quadratic in the prime/Archimedean coefficients, whereas \(\Psi\) is linear in the completed distribution \(\mathcal W\).  The positive realization must therefore arise from a quotient/GNS/cohomological pairing or a genuine defect operator, not by squaring the coupled relative-trace operator itself.

## Physics interpretation

The interval state is a finite Euclidean-time slab.  Its autocorrelation is the triangular kernel.  Thus the minimal AFT theorem can be phrased as:

> the completed arithmetic boundary state assigns nonnegative physical norm to every finite causal slab.

This is a much smaller reconstruction problem than proving positivity for the full Schwinger hierarchy.

## Formalization

Added `GppVerify/CelestialHolography/ArithmeticDefectPositivity.lean`, proving abstractly:

\[
\|y\|\le\|x\|
\Longrightarrow
\|x\|^2-\|y\|^2\ge0,
\]

and the corresponding exact defect/square representation implications.

## Current blocker

Construct the actual zero-independent interval-state maps/channels from Tate--Poisson plus the causal Dirichlet prime anomaly, and identify their defect exactly with the arithmetic formula above.  No such construction is presently proved, so RH is not yet proved.
