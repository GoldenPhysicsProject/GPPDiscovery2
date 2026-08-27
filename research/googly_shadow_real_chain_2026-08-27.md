# Googly/shadow real-chain discovery

Codex/GPT track, 2026-08-27.

## Verified representation-theoretic core

For celestial weights `(h, hbar)`, define

- `Delta = h + hbar`,
- `J = h - hbar`,
- shadow `(h,hbar) -> (1-h,1-hbar)`.

Then exactly

`(Delta,J) -> (2-Delta,-J)`.

Thus the celestial shadow exchanges the `+2` and `-2` graviton helicity labels and the `+1` and `-1` gauge-boson labels. On the scalar principal series `Delta = 1+i nu`, the dimension component becomes ordinary complex conjugation.

## Grassmannian core

Model `Gr(2,4)` set-theoretically as the type of two-dimensional complex subspaces of `C^4`. Orthogonal complement is a genuine self-map because the complement again has complex dimension two, and it is an involution.

This yields a concrete geometric Z2 on the actual subspace Grassmannian rather than a dimension-count surrogate.

## Current googly architecture

The strongest presently justified chain is

`Gr(2,4) complement involution`
`-> celestial shadow involution`
`-> (Delta,J) -> (2-Delta,-J)`
`-> exchange of opposite helicity labels`.

The remaining genuinely geometric theorem is to lift this boundary/representation map through the Penrose transform / Penrose-Ward correspondence so that the ASD twistor cohomology sector maps canonically to the SD sector. Full sheaf cohomology and holomorphic bundle infrastructure is not yet present in the pinned Mathlib, so this lift must either be constructed from lower-level definitions or isolated as a precise imported theorem with all hypotheses explicit.

## Verify2 commits

- `9d9e8625c4a2c5bfcc0239e680abf0276a227d57`: exact celestial shadow helicity reversal.
- `d1b55344fde3b653ce5f85365d86858f9c05b41e`: replace `googly_is_shadow : True` with real helicity theorems.
- `08197c9d8dd679564aac03a43c2bf7a02c81fb3d`: discrete P/T helicity algebra.
- `005634e4a370dc411de47fefb031436d16d44e7a`: actual set-level `Gr(2,4)` type and complement involution.
- `871cd5895945e0e34f06525b62e8fc064e302d50`: explicit CI gates for the new modules.
