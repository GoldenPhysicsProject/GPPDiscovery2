# Connected zeta-gauge metric-flow experiment
Date: 2026-09-25
Status: numerical/structural experiment only. No RH claim.

## Question

The private RH frontier asks whether, after removing the two coherent pole modes and adding the real-place completion, the relative logarithmic zeta-gauge metric derivative

\[
G^{-1/2}\frac{dG}{d\beta}G^{-1/2}
\]

has only subexponential negative numerical range on the connected physical subspace.

The exact causal interval operator is

\[
Z_{L,\beta}=\sum_{n<e^L}n^{-\beta/2}V_{\log n},\qquad
G_{L,\beta}=Z_{L,\beta}^*Z_{L,\beta}.
\]

I tested this directly in the CCM Fourier basis using the exact matrix elements of the unilateral causal shifts.

## Exact discretized shift

For \(e_m(x)=L^{-1/2}e^{2\pi i m x/L}\),

\[
\langle e_n,V_y e_m\rangle
=
\begin{cases}
\frac{L-y}{L}e^{-2\pi i m y/L},&n=m,\\
e^{-2\pi i m y/L}
\frac{1-e^{2\pi i(m-n)y/L}}{2\pi i(m-n)},&n\ne m.
\end{cases}
\]

Numerically \(V_y+V_y^*\) reproduces the CCM box kernel to machine precision.

The two pole vectors are the exact even/odd vectors from
\(W_{02}=\frac12cc^T-\frac12ss^T\).
After conjugating by \(G^{1/2}\), the correct connected constraints are orthogonality to
\(G^{-1/2}c\) and \(G^{-1/2}s\), not to \(c,s\) themselves.

## Result

The pole projection removes a very large part of the negative metric-flow direction, but not all of it.

Representative results (ordinary zeta-gauge metric, beta=1):

- lambda=3, N=30: full minimum about -1.13; connected minimum about -0.91.
- lambda=5, N=60: full minimum about -2.47; connected minimum about -1.39.
- lambda=12, N=60: full minimum about -6.69; connected minimum about -1.23.
- lambda=20, N=80: full minimum about -11.17; connected minimum about -2.10.
- lambda=30, N=60: full minimum about -16.55; connected minimum about -3.55.
- lambda=40, N=70: connected minimum about -4.99.
- lambda=50, N=80: connected minimum about -6.63.

Thus the two-mode removal is a real cancellation, not cosmetic, but the remaining negative edge still appears to grow at large lambda. This agrees with the previously proved finite-rank scalarization no-go: rank-two pole removal alone cannot close RH.

## Naive massive insertion fails

I also replaced the bulk metric by

\[
G=Z^*(D^2+1/4)^pZ
\]

for \(p=\pm 1/2,\pm1\), as the simplest possible insertion of the co-Poisson massive operator. Every such ordinary Hilbert weighting worsened the connected numerical range, often dramatically.

So the live completion cannot be a simple positive diagonal reweighting by \(K_0\) or \(K_0^{-1}\). The co-Poisson operation has to enter as a connected/Feshbach cancellation before scalarization, exactly as the critical-split theorem suggested.

## Interpretation

This experiment narrows the missing mechanism:

1. the zeta-gauge metric flow itself contains a large coherent negative direction;
2. the exact pole plane removes most of it;
3. a residual infinite-dimensional negative channel remains;
4. simple massive weighting does not cure it;
5. therefore the Archimedean/co-Poisson completion must alter the **Schur complement**, not merely the metric weight.

That points directly at a block Feshbach model in which the prime Hodge bulk is eliminated first and only the connected boundary Schur complement is compared with the Riemann seed.

Reproduction: `experiments/rh_connected_metric_flow.py`.
