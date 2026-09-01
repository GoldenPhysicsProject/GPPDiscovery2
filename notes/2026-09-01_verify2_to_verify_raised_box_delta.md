# Raised-box Verify2 → canonical Verify delta audit

Date: 2026-09-01
Status: source audit only; not yet a 4.33 build certificate

## Canonical topology

`GoldenPhysicsProject/GPPVerify/main` is the shared canonical formal record. Codex prepares formal changes on `GPPVerify:codex/lean-workbench`. `GPPVerify2` is now a source tree whose unique mathematics must be audited and migrated, not a competing canonical verification repository.

## Verified source delta inspected this turn

The current Verify2 raised-box chain contains at least the following concrete modules absent by exact-name search from canonical Verify's CelestialHolography tree:

- `RaisedBoxConcreteMoment.lean`
- `RaisedBoxRealMajorantIntegrability.lean`
- `RaisedBoxRealOuterDomination.lean`
- `RaisedBoxRealOuterIntegrability.lean`

The endpoint of this inspected chain proves interval integrability of

`x ^ (-δ) * (1 - x) ^ (2 - δ)` on `[0,1]` for `δ < 1`, by domination with `x ^ (-δ)`.

The dependency chain is substantive rather than a standalone leaf:

`RaisedBoxPointwiseLimit` + `RaisedBoxSimplexMajorantAlgebra`
→ `RaisedBoxConcreteMoment`
→ `RaisedBoxRealMajorantIntegrability`
→ `RaisedBoxRealOuterDomination`
→ `RaisedBoxRealOuterIntegrability`.

Before migration, continue walking dependencies backward and match theorem substance / formalization-queue identity against canonical Verify. Do not classify a file as unique merely because the filename is absent. Claude's 2026-09-01 warning about `ShiftedLogDerivDivisor` vs stronger canonical `ShiftedLogDerivativeTransfer` is the model counterexample.

## Mathematical boundary

This chain certifies the outer majorant needed for the raised-box DCT route, but it does **not** by itself prove the final nested Fubini/Tonelli/DCT statement `J_ε(S,T) → 1/6`. Do not report scalar-box closure until that convergence theorem is actually built and certified on the canonical 4.33.1 tree.

## Next migration action

1. inventory the full raised-box dependency closure in Verify2;
2. match each endpoint against canonical Verify by theorem substance and queue ID, not path;
3. port only genuinely missing mathematics to `GPPVerify:codex/lean-workbench`;
4. repair imports/API against Mathlib 4.33.1 using current upstream paths;
5. run targeted build, full build, sorry/axiom/scaffold gates before proposing integration into `main`.
