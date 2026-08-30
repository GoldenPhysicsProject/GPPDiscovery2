# Codex/GPT continuation — current-branch frontier audit

## Verify2 head and CI

Audited Verify2 head `d809a5f5527a9b166f6cce494880cc3eb29a2889` on `codex/lean-workbench` while the full CI remained in progress.

The main Build lane has already passed the targeted scalar-box regulator endpoint, logarithm-series kernel, Spence endpoint/derivative/constancy/identity, real inversion kernel, prime Hankel and all-order strict Fisher checks, strict zeta Gibbs thermodynamics, massive-vector 5D Ward reconstruction, half-density Hermitian shadow, Gamma Wiener–Hopf real-axis, Gamma phase symmetry, and finite/radial prime-Poisson positive-type checks. The final repository build/sorry/axiom stages were still running, so the head is not yet declared fully certified.

## Scalar box: correction of stale frontier language

`ScalarBoxAutomaticRegulatorConvergence.lean` does **not** prove the raised-box Feynman-simplex DCT `simplexMoment eps S T -> 1/6`. It removes only the auxiliary eventual inequalities `m <= S/4` and `m <= U/16` from the separate structured physical scalar-box core theorem. Its endpoint is

`structuredScalarBoxCore(...) / kappa(m) - scalarBoxD0(S,U,m) -> 0`

under the remaining physical chamber/defining-relation hypotheses.

The raised-box residue file still states the concrete remaining analytic input honestly:

`simplexMoment eps S T -> 1/6` as `eps -> 0+`.

Once supplied, the existing algebra gives

`eps * I8(eps) -> 1/6`

and the dimension-shifted `mu^4` contribution tends to `-1/6`.

The concrete moment layer already has the exact Symanzik polynomial

`Q = S*x1*x3 + T*x2*(1-x1-x2-x3)`,

strict interior positivity, pointwise `Q^(-eps) -> 1`, and the one-channel majorant

`Q^(-eps) <= 1 + (S*x1*x3)^(-delta)`

for `0 <= eps <= delta`, `0 < delta`. The measure/Beta bridge certifies the relevant singular slice integrability. Therefore the remaining formal task is genuinely the AE/Fubini/DCT packaging on the nested affine simplex, not a missing special-function identity.

Separately, the real special-function branch is stronger than older status summaries: Verify2 proves on `0<x<1`

`Li2(x) + Li2(1-x) = pi^2/6 - log(x) log(1-x)`

and

`Li2(x/(1+x)) + Li2(-x) = -(1/2) log(1+x)^2`,

for the project `li2Series`, with branch-free real endpoint control. These identities are CI-targeted and the corresponding targeted checks passed on this head.

## Prime-gas / fluctuation geometry: corrected status

The strict centered prime-Fisher determinant is already a real theorem on the current branch, not a pending bridge. For every `beta > 1`,

`centeredFisherDet(beta) > 0`,

where the determinant is the covariance determinant of centered `log n` and `(log n)^2` under the normalized prime-Fisher probability. The theorem proceeds through exact countable `tsum` coefficient identification and the abstract strict-quadratic determinant theorem, not a finite truncation.

The zeta Gibbs branch also already contains nontrivial thermodynamic geometry. In particular the Helmholtz free-energy response obeys

`F''(beta) = -kappa_2(beta)/beta - 2 S(beta)/beta^3 < 0`

for every `beta>1`, using strict variance positivity and nonnegative Gibbs entropy.

The exact two-observable zeta-Gibbs covariance determinant is already reduced algebraically to

`D = kappa_2*kappa_4 + 2*kappa_2^3 - kappa_3^2`.

What is not yet identified in the audited files is an unconditional theorem `D>0` for this zeta-Gibbs two-observable determinant. This is now a sharper candidate for the next fluctuation-geometry theorem. Genuine intrinsic curvature still requires a multi-parameter family; the one-parameter free-energy curvature is not to be mislabeled as intrinsic Fisher curvature.

## Weil / transfer operator

The current branch does contain an actual `transferOp`, but it is deliberately only the normalized scalar prime-response multiplier lifted to real amplitudes. It proves norm contraction and strict completed-defect positivity away from zero. The source explicitly states that the true Archimedean/prime amplitude spaces and identification with the genuine Weil quadratic form remain separate.

Thus the old phrase “transfer operator missing” is too coarse. Correct frontier:

- scalar response transfer operator: formalized and contractive;
- genuine arithmetic transfer on the completed test/amplitude space: missing;
- equality of its completed defect with the Weil explicit-formula quadratic form: missing;
- unconditional global positivity on the adequate Weil test class: missing.

No RH claim.

## Celestial sewing / higher loops / YM

`TreeLoopSewing.lean` proves the graph-theoretic all-loop count unconditionally:

`(4+2L)`-point connected cubic tree + `L` pair sewings -> four-point graph of cycle rank `L`.

For `L=1`, six-point cubic tree + one pair sewing gives the four-point one-loop topology. The open-chain denominator plus the closure edge is also exact.

The analytic celestial statement is still represented locally by `ShadowPairSewing.sewing_identity`; the file explicitly does not claim that an explicit six-point celestial amplitude has yet been shown to satisfy it. Therefore the next honest amplitude theorem is the explicit six-point inverse-Mellin/shadow-pair sewing identity with correct normalization/sign/prescription. Independently, the Yang–Mills cut numerator still needs explicit fixed-loop-momentum, nonzero-`mu` tree currents sewn over the three physical massive-vector polarizations before state-count algebra may be called an actual YM cut.

## Spectral / Mehler–Fock

The repaired Gamma/Wiener–Hopf real-axis target is passing the main Build targeted Gamma Wiener–Hopf check on `d809a5f...`; full-head certification remains pending until all terminal CI gates finish. The corrected Gamma spectral weight remains distinct from scalar `SL(2,C)` Plancherel density, and chamber positivity is not global Weil positivity.

## Next frontiers

1. Complete the concrete nested-simplex AE/Fubini/DCT theorem `simplexMoment eps S T -> 1/6` for `S,T>0`, `eps->0+`, then discharge the already-assembled `1/6` and `-1/6` raised-box residues.
2. Prove strict positivity of the zeta-Gibbs two-observable determinant if the countable support/summability layer permits a clean three-support-point or polynomial-Gram argument; then package the exact cumulant inequality `kappa_3^2 < kappa_2*kappa_4 + 2*kappa_2^3`.
3. Replace the scalar-model arithmetic transfer by the true completed prime/Archimedean operator and prove identification with the Weil quadratic form; no RH promotion before that bridge and positivity are real.
4. Derive the explicit six-point celestial pair-sewing identity and the honest nonzero-`mu` Yang–Mills tree sewing numerator; only then promote generalized-cut/higher-loop amplitude claims.
5. Re-poll terminal CI for `d809a5f...` and repair any deterministic failure before advancing Verify2 `main`.

Claude work was not inspected.
