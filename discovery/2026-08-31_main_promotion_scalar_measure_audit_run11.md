# Codex run: certified-head promotion and scalar measure audit

Date: 2026-08-31
Track: Codex/GPT only

## Verify2 publication state

The `codex/lean-workbench` head `9881d7274a7d48237f917808d978d6dddd5c2a47` had a settled 24-workflow CI set with no failed, cancelled, queued, or in-progress runs. Under the operating rule in `CODEX.md` that green formalization should not remain hidden on the research branch, `GPPVerify2/main` was fast-forwarded (non-force) from `4025286936321e43d11f8fa7f9454b69cbe38f68` to `9881d7274a7d48237f917808d978d6dddd5c2a47`.

The promotion triggered fresh main-branch workflows. At the time of this record, the main `Build` and `Codex full construction` runs were in progress; therefore the earlier branch CI is certified, while the post-promotion main rerun is still settling.

## Scalar-box measure audit

A source-level audit clarified an important interface issue.

`RaisedBoxSimplexMeasureBridge.lean` does **not** yet provide the real nested L1/Tonelli bridge for the concrete raised-box moment. Its two theorems are complex-valued `IntervalIntegrable` certificates for the reduced outer Beta integrand and a nondegenerate inner affine Beta slice. They are useful exact special-function certificates, but they are not the concrete real dominated-convergence theorem.

`RaisedBoxConcreteMoment.lean` remains the physical object. It defines

    J_epsilon(S,T) = ∫_0^1 dx1 ∫_0^(1-x1) dx2 ∫_0^(1-x1-x2) dx3 Q(S,T,x)^(-epsilon),

with

    Q = S x1 x3 + T x2 x4,   x4 = 1-x1-x2-x3.

The file formally proves:

1. `J_0` is the affine simplex volume;
2. strict-interior pointwise convergence `Q^(-epsilon) -> 1` as `epsilon -> 0`;
3. for `0 <= epsilon <= delta`, the physical integrand is bounded by

       1 + (S x1 x3)^(-delta).

The real-majorant modules integrated into `FullConstruction` separately prove endpoint integrability, the exact inner singular slice, the exact middle affine integral, and outer domination. The remaining theorem is therefore genuinely measure-theoretic assembly: turn those nested real interval certificates into the integrable dominating function for the concrete iterated integral, discard boundary faces almost everywhere, and apply one-sided dominated convergence.

This confirms the previous frontier rather than retracting it. The exact finite majorant mass derived in discovery remains

    M_delta(S) = 1/6 + S^(-delta) Gamma(1-delta)^2 / Gamma(4-2delta),

for `S>0` and `0<delta<1`; what is missing in Lean is the concrete real `L1`/AE/DCT packaging, not special-function evaluation.

## Cross-front status

The promoted `FullConstruction` now visibly carries, in one import graph, the principal-series/completed-zeta bridge, all-order strict prime Hankel positivity, Gamma/Mehler-Fock spectral chamber results, the raised-box real-majorant slices, scalar-box regulator algebra, and the current massive-cut infrastructure.

No stronger RH claim follows: the global prime-plus-Archimedean identification with the Weil quadratic form and its required positivity remain open. No repeated-sech convolution claim is inferred from the exact Gamma chamber hierarchy. YM/gravity remains downstream of an honest fixed-loop-momentum nonzero-mu Yang-Mills tree sewing numerator; existing projector/state-sum modules are infrastructure, not a substitute for that numerator.

## Persistence note

The Supabase `codex.research_notes` SQL read was blocked by the connector's safety layer in this run. No database write is claimed. This GitHub record is the durable run record.

No Claude branch, records, files, or context were inspected.
