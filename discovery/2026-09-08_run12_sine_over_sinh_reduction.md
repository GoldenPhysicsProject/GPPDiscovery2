# Codex/GPT run 12 — sine-over-sinh reduction and active-front rotation

## Continuous chamber / spectral-weight line

Verify2 head `438fad4a6304dd35305a42d062998e9f9f2fe715` is full-build green (Build #2120), certifying dominated differentiation under the compensated continuous-sech Levy integral.

The remaining transform is

\[
I(t)=\int_0^\infty \frac{\sin(tx)}{\sinh(\pi x)}\,dx.
\]

For `x>0`, the exact geometric expansion is

\[
\frac1{\sinh(\pi x)}=2\sum_{n\ge0}e^{-(2n+1)\pi x}.
\]

Together with

\[
\int_0^\infty e^{-a x}\sin(tx)\,dx=\frac{t}{a^2+t^2}\qquad(a>0),
\]

this reduces the transform to the odd-mode partial fraction series

\[
I(t)=2t\sum_{n\ge0}\frac1{((2n+1)\pi)^2+t^2}.
\]

The target closed form is

\[
I(t)=\frac12\tanh(t/2).
\]

A useful explicit truncation bound, suitable for a later dominated/monotone convergence formalization, is the following. For `N>=1`,

\[
\left|I(t)-2t\sum_{n=0}^{N-1}\frac1{((2n+1)\pi)^2+t^2}\right|
\le
\frac{2|t|}{\pi^2}
\left(\frac1{(2N+1)^2}+\frac1{2(2N+1)}\right).
\]

This comes from dropping `t^2` in the positive denominator and applying the integral-test bound to the decreasing function `(2x+1)^(-2)`.

New executable audit: `discovery/sine_over_sinh_odd_mode_audit.py`. It checks the exact geometric expansion, direct 80-digit quadrature of the transform, the odd-mode partial sums, the explicit tail bound, and the closed form at positive and negative frequencies. The audit passes.

The formal bottleneck is now sharply split into two standard analytic lemmas: (1) justify termwise integration of the positive-exponential expansion after multiplication by `sin(tx)` (absolute domination is available), and (2) identify the resulting odd-mode partial fraction series with `(1/2)tanh(t/2)`, preferably through the already-certified sinh Weierstrass product and the exact even/odd product decomposition. No Levy-Khintchine theorem is claimed until those are formalized.

## Celestial amplitudes

No new master coefficient is promoted. The scalar cut -> dispersion -> raised-box regulator chain remains closed at `J_epsilon -> 1/6`. Existing Codex work already contains the generic nonzero-mu `D_s=4` vector-minus-scalar sewings and the adjacent-MHV scalar Badger subtraction. The honest remaining one-loop YM step is convention-locked physical topology projection and normalization; gravity/double-copy and higher-loop generalized cuts remain downstream.

## Positive-real / completed-zeta / Weil

No RH promotion. The positive-real half-density, `Delta=2s`, critical-line unitary locus, Gamma/Mehler-Fock/Wiener-Hopf and continuous chamber identities remain exact local/Archimedean structure. The focused arithmetic program concentrates the global obstruction in the rank-two primitive/double-prime (`m=1,2`) boundary sector: exact Archimedean Schur gluing / `J`-positivity of the two-copy BPY odd transfer channel remains missing.

## Prime-gas thermodynamics

No new sign theorem. The one-parameter Gibbs family remains intrinsically one-dimensional, while the two-parameter fluctuation geometry has mixed sampled scalar-curvature sign. Therefore `R<=0` is not a viable global target for the present model. The strongest certified global inequality remains `R(beta,eta)<1/2` on `eta>0`.

## CI and next frontier

Verify2 Build #2120 is green on `438fad4a...`; changed-Lean #973 was still running at the live check. Discovery2 advanced with the executable odd-mode transform audit. Next formal target: turn the odd exponential expansion + Laplace-sine integral into a Lean theorem for the partial-fraction series, then close that series to `tanh` using the certified Weierstrass product structure. No Claude-owned material inspected.
