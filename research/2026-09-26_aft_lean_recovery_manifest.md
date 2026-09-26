# AFT Lean recovery manifest: retired Verify2 -> current GPPVerify

Date: 2026-09-26

Status: repository recovery/audit. No new mathematical claim.

The user's recollection was correct: a substantial Arithmetic Field Theory (AFT) formalization exists in the retired repository GoldenPhysicsProject/GPPVerify2. The current formal repository GoldenPhysicsProject/GPPVerify on branch codex/rh-boundary-closure does not presently contain the main AFT modules. They should be audited and migrated selectively rather than reinvented.

Source snapshot audited:
- repository: GoldenPhysicsProject/GPPVerify2
- commit/tree ref: 45601c8c44cd30f35e6a34ec6827e55467926dfe

## Core AFT / OS files in retired Verify2

CelestialHolography:
- ArithmeticOSReflection.lean
- ArithmeticOSGram.lean
- ArithmeticPrimeLocalOS.lean
- ArithmeticPrimeFactorMap.lean
- ArithmeticOSFactorization.lean
- ArithmeticDefectPositivity.lean
- ArithmeticCompletedDefectCriterion.lean
- ArithmeticEulerLogAnomaly.lean
- ArithmeticNoGhostCoercivity.lean
- ArithmeticNoGhostInertia.lean
- ArithmeticPrimeWaveParticle.lean
- ArithmeticPrincipalSeriesSelection.lean
- ArithmeticSplitConventionBridge.lean
- ArithmeticSplitSignature.lean
- ArithmeticTemperedPrincipalSeries.lean
- ConformalShadowPrincipalSeries.lean

RiemannHypothesis:
- ArithmeticConformalKinematics.lean
- ArithmeticConformalCasimir.lean
- ArithmeticEisensteinUnitarity.lean
- ArithmeticSplitCoordinates.lean
- ArithmeticTimeEvolution.lean
- CausalHeatPrimePowerAnomaly.lean
- CausalPrimeHeatBridge.lean
- CausalPrimeHeatReindex.lean
- CausalPrimeHeatSummability.lean
- CausalPrimeResolventFinite.lean
- PrimeLocalResponseContraction.lean
- PrimeResponseContraction.lean
- PrimeResponseTransferOperator.lean

## p-adic / local-conformal stack in retired Verify2

- PadicConformalScaling.lean
- PadicCrossRatio.lean
- PadicMobiusConformal.lean
- PadicEulerFactorBridge.lean
- PadicFieldHaarMeasure.lean
- PadicFullZetaIntegral.lean
- PadicHaarMeasure.lean
- PadicHaarTransfer.lean
- PadicIndexPn.lean
- PadicMultiplicativeMeasure.lean
- PadicOriginMeasure.lean
- PadicScalingHaar.lean
- PadicShellMeasure.lean
- PadicShellNorm.lean
- PadicZetaIntegral.lean
- PadicZetaIntegralClosedForm.lean

The lower p-adic Haar/Tate stack is already largely present in current GPPVerify; the conformal bridge files PadicConformalScaling and PadicMobiusConformal are missing from the current rh-boundary-closure branch.

## Thermodynamic / prime-field stack in retired Verify2

The retired repository also contains a large verified arithmetic-field layer:
- PrimeGasPartition
- PrimeOccupationBridge
- PrimeGreenAmplitude
- PrimePoisson / finite positive-type modules
- PrimeFisher probability, moment, countable and centered geometry modules
- PrimeHankel Gram / all-order / infinite-lift modules
- ZetaGibbs entropy, Fisher, cumulant, free-energy, KL/Bregman, centered geometry and critical regularization modules
- VonMangoldtPrimePowerTower, Reindex, Fubini, PoissonFiber

Many descendants or older versions of this stack already exist in current GPPVerify, but the exact retired branch should be compared theorem-by-theorem before copying.

## Important historical CI record

The 2026-08-28 continuation audit recorded that at the then-active Verify2 snapshots:
- dedicated spectral/arithmetic-OS/Gibbs/Fisher workflows were green;
- the finite prime factor map had been CI-certified;
- the AFT completed-defect criterion had been added and was being gated;
- no RH proof was claimed.

These are historical CI statements for those exact old commits only. They do not establish that copied files build under the current GPPVerify toolchain.

## Main mathematical content worth recovering

1. Multiplicative Euclidean time:
   x -> 1/x becomes t=log x -> -t, with half-density Mellin reflection
   s -> 1-conj(s), fixed at Re(s)=1/2.

2. Prime-local OS positivity:
   each prime-power kernel has an explicit rank-one Gram factorization.

3. Exact Euler-log anomaly:
   the 1/m Euler-log repetition factor cancels m log p to produce log p, giving the von Mangoldt prime-power coefficient in the causal heat anomaly.

4. Completed defect criterion:
   ||A_prime x|| <= ||A_inf x|| implies positivity of
   ||A_inf x||^2 - ||A_prime x||^2.

5. No-ghost coercivity skeleton:
   a positive lower bound on the odd Hodge Laplacian kills odd harmonic cohomology.

6. No-ghost inertia obstruction:
   positive reweighting alone cannot remove an indefinite ghost direction; a true quotient/exactness mechanism is required.

7. p-adic conformal scaling:
   valuation depth is a discrete radial coordinate and local shell amplitudes scale by p^{-Delta}; PadicMobiusConformal extends this toward PGL(2,Q_p) covariance.

## Current migration status

On current GPPVerify branch codex/rh-boundary-closure, the principal AFT modules listed above are absent. Several of their dependencies are also absent, including:
- PositiveRealPrincipalSeries.lean
- ArithmeticDefectPositivity.lean
- VonMangoldtPrimePowerTower.lean
- CausalPrimeResolventFinite.lean
- PrimeResponseContraction.lean

Other dependencies are already present:
- PadicZetaIntegralClosedForm.lean
- ScaleShadowHalfDensity.lean
- CasimirIdentity.lean
- GlobalEisensteinCoefficient.lean
- CompletedZetaReality.lean

Therefore migration should be dependency-ordered and audit-driven, not a blind bulk copy.

## Recommended migration order

Phase A: low-risk algebraic/conformal core
1. PadicConformalScaling
2. PadicMobiusConformal
3. ArithmeticConformalKinematics
4. ArithmeticConformalCasimir
5. ArithmeticTimeEvolution

Phase B: AFT reflection core
6. PositiveRealPrincipalSeries
7. ArithmeticOSReflection
8. ArithmeticOSGram
9. ArithmeticOSFactorization
10. ArithmeticPrimeLocalOS
11. ArithmeticPrimeFactorMap

Phase C: causal prime-current core
12. VonMangoldtPrimePowerTower
13. ArithmeticEulerLogAnomaly
14. CausalHeatPrimePowerAnomaly
15. CausalPrimeResolventFinite
16. CausalPrimeHeatBridge

Phase D: no-ghost / transfer closure skeleton
17. ArithmeticDefectPositivity
18. ArithmeticCompletedDefectCriterion
19. ArithmeticNoGhostInertia
20. ArithmeticNoGhostCoercivity
21. PrimeResponseContraction
22. PrimeResponseTransferOperator

After each phase, compile under the current Lean/Mathlib version before advancing.

## Connection to the new 2026-09-26 program

The recovered AFT stack is directly relevant to the new finite-place/celestial and dark-sector work:
- PadicConformalScaling supplies the local non-Archimedean CFT leg.
- ArithmeticConformalCasimir supplies the shared Casimir coordinate.
- ArithmeticOSReflection supplies the Euclidean reflection/half-density bridge.
- ArithmeticEulerLogAnomaly supplies the exact von-Mangoldt current that generated the isothermal-halo asymptotic.
- ArithmeticCompletedDefectCriterion and ArithmeticNoGhostCoercivity are exactly the operator/Hodge mechanisms needed for the current RH no-escape theorem.

So the present program should be treated as a continuation of AFT, not a new parallel theory.
