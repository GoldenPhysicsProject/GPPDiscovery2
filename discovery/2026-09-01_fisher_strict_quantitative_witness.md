# Codex run: strict quantitative Fisher witness

Date: 2026-09-01
Track: Codex/GPT only

## Verified base

The pinned-Lean repair head `f2a3e545a4fd5a79de880c82411d059c245aa5a5` on `GPPVerify2/codex/lean-workbench` passed the `Codex changed Lean smoke` workflow. This certifies the scalar-aware Vandermonde channel factorization and the repaired finite Fisher/Vandermonde dependency chain under the current toolchain.

## New formal theorem staged

Verify2 commit `29f17d38863b4a672a33800e3edd329f7a25d51b` adds
`GppFiniteFisherQuantitativeWitness.fisherNumerator_pos_of_positive_distinct_witness`.

For finite nonnegative weights `p` and observables `x`, if a chosen triple `i,j,k` has strictly positive weights and pairwise distinct observable values, then the full mass-aware finite Fisher numerator is strictly positive.

The proof deliberately factors through the stronger quantitative estimate

\[
\frac{p_i^2 p_j p_k}{6}
\left[(x_i-x_j)(x_i-x_k)(x_j-x_k)\right]^2
\le N_F.
\]

Thus the theorem is not merely qualitative: the selected witness is compatible with a fixed-prefix lower bound for the countable limit bridge.

The new head triggered `Codex changed Lean smoke` run `33507517701`; it was queued at the time of this record and must not be called CI-certified until the run completes successfully.

## Number-Gibbs next closure

For the two-parameter number-Gibbs weights

\[
w_n(\beta,\eta)=n^{-\beta}e^{-\eta(\log n)^2},\qquad \eta>0,
\]

the previous discovery result gives summability of every fixed logarithmic moment for all real `β`. The fixed support points `1,2,3` have positive weights and distinct energies `0, log 2, log 3`. The remaining formal task is to connect their quantitative finite witness uniformly to `partialMoment` truncations (for all sufficiently large `N`) and invoke `CountableFisherStrictWitness.fisherNumerator_infinite_pos_of_eventually_partial_ge`.

## Other fronts

Scalar box: no new analytic estimate is missing. The concrete moment, interior pointwise regulator limit, one-channel domination, slice integrability, and outer reduced majorant integrability are already present. The formal blocker remains the almost-everywhere boundary-face bookkeeping plus nested interval dominated-convergence assembly required for `J_ε(S,T) → 1/6`.

Yang-Mills/gravity: no numerator claim promoted before scalar regulator closure. The next honest amplitude target remains fixed-loop `D_s=4`, nonzero-`μ` tree sewing over the massive-vector state sum, followed by generalized/higher-loop cuts and only then double copy.

Principal-series/Weil: local positive-real half-density, `Δ=2s`, critical-line unitarity and the Archimedean Gamma/Mehler-Fock/Wiener-Hopf structures remain valid. No non-circular global prime-plus-Archimedean Weil positivity theorem was obtained.

Spectral/chambers: no new theorem this run; existing exact recurrence, positivity, convolution, and chamber-crossing results remain unchanged.

No Claude material was inspected or used.