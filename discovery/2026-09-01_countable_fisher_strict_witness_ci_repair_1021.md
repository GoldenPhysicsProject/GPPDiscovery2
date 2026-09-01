# Countable Fisher strict-witness CI repair

Codex/GPT track only. No Claude material inspected.

## CI diagnosis

Verify2 head `8ef243c8fcb9e8f2a7e831d6763506deabeb8fab` failed changed-Lean smoke run `33513917432` only in `CountableFisherStrictWitness.lean`.

The rebuilt dependency chain through `CountableFisherMomentLimit.lean` compiled without `sorryAx`. The remaining failures were:

1. `fisherNumerator` and `fisherDet` were unresolved because opening `GppCountableFisherMomentLimit` does not re-export its opened `GppFiniteFisherMomentBridge` namespace.
2. The eventual fixed-three-state prefix proof used `omega` on nested `max` bounds with metavariables from the failed namespace resolution, leaving three index inequalities unproved.

## Repair

Verify2 commit `7f3192b487beb85fccb4f21a0efc40e7a71c569f`:

- explicitly opens `GppFiniteFisherMomentBridge`;
- replaces the three `omega` calls with explicit `Nat.le_max_left`, `Nat.le_max_right`, `Nat.lt_succ_of_le`, and transitivity proofs.

The theorem target is unchanged. For fixed natural states `i,j,k`, every sufficiently large prefix retains the constant lower witness

`c = w_i^2 w_j w_k ((x_i-x_j)(x_i-x_k)(x_j-x_k))^2 / 6`,

and, once moments through order four are summable, convergence of the mass-aware Fisher numerator transfers `c>0` to the countable limit.

CI run `33519125811` was queued at recording time; do not call this head certified until it completes successfully.

## Scalar front

No new scalar theorem in this run. The exact remaining scalar-box blocker remains almost-everywhere simplex-boundary removal plus nested interval dominated convergence for the already-established majorant, to prove `J_ε(S,T) -> 1/6`.

## Weil / spectral / amplitude fronts

No new global Weil positivity, RH, Mehler-Fock/chamber, YM, or gravity theorem was promoted. Existing Archimedean principal-series/Gamma/Wiener-Hopf infrastructure remains valid; honest YM sewing remains downstream of scalar regulator closure.
