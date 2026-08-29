# Codex/GPT all-fronts continuation — 2026-08-29 07:26Z

Scope: Codex/GPT track only. No Claude work inspected.

## 1. Celestial cuts / scalar box / generalized cuts

The scalar-box regulator layer remains at the previously formalized automatic-small-regulator theorem. The new exact amplitude-side increment is the physical-region classification of the universal massive spin-1 little-group polynomial

\[
P_V(s,\mu)=s^2-4s\mu^2+3\mu^4=(s-\mu^2)(s-3\mu^2).
\]

At threshold `s=4 mu^2`, `P_V=3 mu^4`. Moreover for the physical two-particle region `s >= 4 mu^2`,

\[
P_V(s,\mu)-3\mu^4=s(s-4\mu^2)\ge0,
\]

so

\[
P_V(s,\mu)\ge3\mu^4\ge0.
\]

This has been pushed to `GppVerify/CelestialHolography/MassiveVectorStateSum.lean`.

Boundary: this is the universal little-group/state-sum factor only. The honest nonzero-mu `D_s=4` MHV cut still requires the two massive-vector tree tensors with both physical projectors retained, followed by subtraction of the real-scalar cut. No generic double-metric Ward shortcut is being used.

## 2. Positive-real half-density / principal series

For `Delta=2s`, the existing exact principal-axis/unitarity equivalence was strengthened off-axis. At every scale `a>1`:

- `Re Delta = 1` gives unit norm of the half-density dilation character;
- `Re Delta > 1` gives strict amplification;
- `Re Delta < 1` gives strict contraction.

The norm is

\[
\|\chi_s(a)\|=\exp(\log a\,(\Re s-1/2)).
\]

This is pushed in `PrincipalSeriesDilationBridge.lean`.

Boundary: this classifies the representation-theoretic unitary axis exactly but does not constrain zeta zeros by itself. The unresolved global step is still identification of the signed completed arithmetic Weil form with the positive prime-Archimedean operator/kernel.

## 3. Prime-gas number thermodynamics / Fisher geometry

The countable nonnegative Fisher determinant theorem is already present after the workbench/main synchronization. This run added the strict local Vandermonde witness:

for `p_i,p_j,p_k>0` and three pairwise distinct support values `x_i,x_j,x_k`,

\[
p_i p_j p_k[(x_i-x_j)(x_i-x_k)(x_j-x_k)]^2>0.
\]

This is the exact finite witness needed to upgrade the countable prime-gas two-parameter Fisher determinant from nonnegative to strictly positive when a fixed three-point support witness is propagated through the countable limit.

Boundary: the final strict countable theorem is not yet formalized; the remaining analytic/formal step is to retain a fixed positive lower bound from one three-point witness through sufficiently large truncations and then through the mass-aware Fisher limit.

## 4. Spectral weights / Mehler-Fock / Wiener-Hopf chambers

The existing chamber recurrence is

\[
\rho_{k+1}(\lambda)=r_k(\lambda)\rho_k(\lambda),
\qquad
r_k(\lambda)=\frac{2((k+1)^2+\lambda^2)}{(k+1)(2k+3)}>0.
\]

Since every chamber real density is already proved strictly positive, the exact threshold

\[
r_k(\lambda)>1\iff k+1<2\lambda^2,
\qquad
r_k(\lambda)<1\iff 2\lambda^2<k+1
\]

implies strict chamber growth above the threshold and strict chamber decrease below it. A Lean patch implementing these two monotonicity theorems has been pushed; CI has not yet certified that newest patch at the time of this record.

## CI

Before the newest sequence of commits, the scaffold/axiom audit and causal-diamond Fisher cancellation gates were green. The current head CI was queued/restarting after the latest spectral proof repair. No mathematical retraction occurred. One incomplete Lean placeholder in the first version of the spectral decrease proof was caught immediately and replaced before this record; the repaired theorem is provisional until CI compiles it.

## Next executable frontier

1. Compile/repair the newest spectral and off-axis dilation proofs if CI exposes API issues.
2. Formalize the fixed-three-support lower bound that upgrades countable Fisher nonnegativity to strict positivity for the prime/log Gibbs support.
3. Complete the double massive-projector MHV tree sewing and subtract the scalar state to obtain the honest nonzero-mu `D_s=4` cut numerator; then double-copy at the projector/state-sum level.
4. Continue the global prime-Archimedean/Weil operator identification without conflating local positive factors with the signed global Weil form.
