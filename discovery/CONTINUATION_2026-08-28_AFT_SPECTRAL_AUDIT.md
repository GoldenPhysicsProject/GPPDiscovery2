# Codex continuation — AFT/spectral audit — 2026-08-28

Codex/GPT track only. No Claude work inspected.

## Verify2 CI and spectral repair

At Verify2 commit `49d09708cf3c80fee8e07a9799094388512e01e3`, aggregate Build, Gibbs differential thermodynamics, arithmetic OS reflection, and causal-diamond Fisher cancellation were green. The dedicated sech/spectral workflow failed only downstream in `GppVerify/CelestialHolography/WienerHopfGammaBridge.lean`.

Importantly, the full `SpectralRhoMehlerFockBridge.lean` theorem family compiled successfully, including

- `rhoGamma_zero_eq_mehlerFock`,
- `rhoGamma_zero_zero`,
- `chamberPoly_at_zero`,
- `rhoGamma_at_zero`,
- `rhoGamma_eq_mehlerFock_chamber`,
- `rhoGamma_eq_mehlerFock_chamber_all`.

The remaining failure was a Lean coercion normalization: after taking `Complex.re`, simplification rewrote an explicitly real-cast quotient through `Complex.sinh`, while the target used `Real.sinh`. This is a proof-engineering mismatch, not a mathematical counterexample.

Verify2 commit `240f00c7d14ca99454d775c76a4c8bac9e1b3b37` repairs the bridge by rewriting directly with the already-proved theorem

`rhoGamma 0 x = ((2*x / Real.sinh (Real.pi*x) : R) : C)`

and simplifying the real part only after that rewrite. Fresh CI is running; do not call the downstream Wiener–Hopf/Gamma chamber hierarchy certified until it finishes.

## AFT / field-theory inventory recovered from Verify2

The repository already contains substantially more of the prospective arithmetic-field-theory skeleton than a bare zeta/principal-series dictionary:

- multiplicative Haar / half-density / principal-series layer;
- `AdelicL2.lean`;
- a substantial p-adic Haar/zeta-integral suite (`PadicFieldHaarMeasure`, `PadicMultiplicativeMeasure`, `PadicScalingHaar`, `PadicZetaIntegral`, `PadicZetaIntegralClosedForm`, `PadicEulerFactorBridge`, etc.);
- Archimedean zeta-integral and completed-factor modules;
- exact prime occupation response `PrimeOccupationBridge.lean`;
- prime gas, prime Green-amplitude and Dirac/Fock-related modules;
- arithmetic OS reflection, OS Gram positivity, and prime-local OS positivity;
- completed-zeta principal-series response;
- global von-Mangoldt / prime Poisson layers;
- Weil criterion/interpolation/support and `CutkoskyWeilBridge` infrastructure;
- Gamma/Mehler–Fock/Wiener–Hopf spectral factors;
- a separate `HolographicChain.lean` and Gr(2,4)/shadow geometry program.

The exact local occupation identity is already theorem-level:

`-zeta_p'(s)/zeta_p(s) = log(p)/(exp(s log p)-1)`

away from the Bose denominator pole. Hence `E_p = log p` and prime-power repetitions are exact bosonic occupation algebra, while their physical interpretation remains separate.

## Important audit correction

`GppVerify/QuantumGravity/WightmanAxioms.lean` is currently mostly scaffolding: W1–W6, OS reconstruction, CPT, spin-statistics, and the claimed RH/Wightman unification are represented by `True` theorems. The dimension checks are genuine, but this file must not be cited as a formal derivation of QFT axioms.

This makes the next AFT target precise: replace labels/placeholders by actual field-theoretic interfaces (Hilbert space, reflection operator, positive OS form, semigroup/spectral measure, and correlator/test-function map) and then identify that completed OS form with the genuine Weil quadratic form. The local prime-positive pieces alone are insufficient because the finite-prime term enters the standard explicit formula with the opposite overall sign.

## Connected active frontiers

1. **AFT / RH:** direct 1d shadow is `s <-> 1-s` with principal line `Re s = 1/2`; under celestial normalization `Delta=2s` this is `Delta <-> 2-Delta`, `Re Delta=1`. The decisive missing theorem is completed AFT OS positivity plus exact transport to the genuine Weil form on an adequate test class. No RH claim.
2. **Scalar box:** exact inner affine simplex Beta slice is proved. Remaining raised-box step is nested interval/Fubini endpoint handling yielding the second factor `B(1-delta,3-delta)`, then dominated convergence. The structured physical scalar regulator limit is a separate already-developed layer.
3. **YM/gravity:** projector bookkeeping is already exact; missing object is the explicit `D_s=4`, `mu != 0` two-massive-vector/two-positive-helicity-gluon tree current and its sewn numerator. Higher-loop generalized cuts remain downstream.
4. **Prime thermodynamics:** exact cumulant/entropy/free-energy/fluctuation differential geometry on `beta>1` remains green at the previous certified head. The beta->1+ singular/regular decomposition should be formalized generically before asserting zeta-specific regularity.
5. **Spectral:** all-order chamber weights are algebraically established; full iterated/convolution interpretation remains open even if the repaired Wiener–Hopf/Gamma normalization becomes CI-green.
