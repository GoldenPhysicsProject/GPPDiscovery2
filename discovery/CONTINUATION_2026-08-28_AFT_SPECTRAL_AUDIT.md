# Codex continuation — AFT/spectral audit — 2026-08-28

Codex/GPT track only. No Claude work inspected.

## Current CI checkpoint and repairs

At cumulative Verify2 head `885ccaf6d5dca5059e80fa5c297fa2e273022300`, aggregate Build, Gibbs differential thermodynamics, and causal-diamond Fisher cancellation are green. Two dedicated workflows exposed implementation failures rather than mathematical counterexamples.

### Spectral

The important advance is that `WienerHopfGammaBridge.lean` is now CI-green. Thus the exact global base normalization

`extendedWienerHopfWeight x = (pi/2) * Re(rhoGamma 0 x)`

and inverse

`Re(rhoGamma 0 x) = (2/pi) * extendedWienerHopfWeight x`

are certified, including the removable origin. The same run also reconfirmed the sech endpoint/closed-form/Wiener–Hopf layers and the complete `SpectralRhoMehlerFockBridge` family through the all-real chamber formulas.

The next failure moved one step downstream into `WienerHopfGammaChamberHierarchy.lean`. It was an induction rewrite mismatch: the successor goal is already written as `rhoGamma (k+1)`, while the proof first attempted `rw [Nat.succ_eq_add_one]`, which searches for a `Nat.succ` pattern that is no longer present. Verify2 `571553fe567d497b054bbba68d292b979184a6d0` removes that spurious rewrite and proceeds directly with `rhoGamma_succ`, the induction hypothesis, and `Finset.prod_range_succ`, followed by unfolding `rhoStepFactor` and ring normalization. Fresh CI is required before the full chamber hierarchy is called certified.

The intended exact hierarchy is

`rhoGamma k x = (prod_{j<k} rhoStepFactor j x) * rhoGamma 0 x`,

hence

`Re rhoGamma(k,x) = (prod_{j<k} rhoStepFactor(j,x)) * (2/pi) W_ext(x)`,

with every multiplier strictly positive.

### AFT / arithmetic OS

The first `ArithmeticOSFactorization.lean` used `Mathlib.Analysis.InnerProductSpace.GramMatrix`, but the repository is pinned to Mathlib v4.19.0 (`c44e0c8e...`), predating that file. Therefore the arithmetic-OS workflow failed at import resolution, not at positivity.

Verify2 `a84ce5524be883e214ed4fa76dc0ade2563c22f3` replaces the post-v4.19 Hilbert-Gram dependency by the finite matrix factorization available in the pinned Mathlib. The criterion is now formulated in the exact `A^*A` form:

`K = Aᴴ * A  ==>  K.PosSemidef`.

The proof uses positivity of the identity matrix and the pinned `PosSemidef.conjTranspose_mul_mul_same` theorem. This is also structurally better aligned with the loop transfer factorization `T=A^*A` than the previous abstract Gram API. Fresh arithmetic-OS CI is required.

Strategically, this isolates the real AFT theorem exactly: construct a zero-independent prime–Archimedean factor `A` (or reflection-preserving `mathfrak L`) such that the arithmetic Hankel/reflected kernel equals `Aᴴ A`; positivity then follows automatically. No RH claim is made.

## Gibbs / number thermodynamics

The critical pole removal is CI-certified on `beta>1`:

`H(beta)=(beta-1)Z(beta)>0`,

`log Z(beta)=log H(beta)-log(beta-1)`,

and

`F(beta)=-log H(beta)/beta + log(beta-1)/beta`.

The exact cumulant/entropy/free-energy/fluctuation differential layer remains green. The honest next analytic input is regularity/derivative control of `H` as `beta -> 1+`; no such limit is currently asserted.

## Principal series / completed arithmetic response

The exact conformal-shadow theorem remains source-level and previously workflow-tested: for real boundary dimension `d`, `Delta -> d-Delta` is involutive and equals conjugation iff `Re Delta=d/2`. At `d=1` this is the arithmetic shadow `s -> 1-s` with principal line `Re s=1/2`; under `Delta=2s`, it is the celestial `d=2` shadow with `Re Delta=1`.

The AFT field candidate remains the focused Gaussian/Brownian-bridge radial observable

`Q = (1/(2*pi)) sum_{n>=1} sum_{a=1}^4 G_{n,a}^2/n^2`,

with `E[Q^(s/2)] = 2 xi(s)` and critical tilt `Q^(1/4)`. The unresolved theorem is not ordinary unitarity but a positive reflection-preserving gluing/factorization of the completed prime–Archimedean kernel, followed by exact identification with the genuine Weil quadratic form on an adequate test class.

## Scalar box

The exact inner affine simplex Beta slice and reduced outer Beta product are in source. The remaining analytic closure is still the real nested interval/Fubini endpoint passage from the original simplex integral to that reduced Beta integral, followed by dominated convergence for the regulator. No new theorem was claimed here this run.

## Yang–Mills / gravity / higher cuts

No explicit trustworthy `D_s=4`, `mu != 0` two-massive-vector/two-positive-helicity-gluon tree current has yet been recovered from the focused material. Existing Ward/projector reconstruction is exact, but an honest sewn numerator still requires that tree current. Higher-loop/generalized-cut claims remain downstream; no numerator has been guessed.

## Active next frontiers

1. Certify Verify2 `a84ce552...` AFT `AᴴA` positivity on the pinned Mathlib and `571553fe...` full Wiener–Hopf/Gamma chamber induction.
2. Construct the actual arithmetic factor map for the completed reflected kernel, not merely more local positivity identities.
3. Close the raised-box nested Fubini/endpoint/DCT layer.
4. Obtain the honest massive-vector `++` tree current before YM/gravity sewing.
5. Add zeta-specific regularity of the pole-removed Gibbs factor only when it can be proved without assumptions.
