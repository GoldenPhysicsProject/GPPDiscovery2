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

## Focused-paper AFT field realization recovered

The focused arithmetic principal-series paper contains a much stronger field-theory candidate than the prime-gas analogy alone.  It defines four independent Gaussian/Brownian-bridge components and the radial observable

`Q = (1/(2*pi)) * sum_{n>=1} sum_{a=1}^4 G_{n,a}^2 / n^2`

and states the BPY Mellin identity

`E[Q^(s/2)] = 2 xi(s)`.

After the positive critical tilt

`dP_{1/2} = Q^(1/4)/(2 xi(1/2)) dP_G`

and `X = (1/2) log Q`, the paper obtains

`E_{1/2}[exp(z X)] = xi(1/2+z)/xi(1/2)`.

This is therefore an explicit Euclidean Gaussian-field realization of the completed xi response as a nonlinear radial observable, not merely a thermodynamic metaphor.  Equally important, the same paper records the exact obstruction: ordinary free-field/Lee–Yang positivity does not prove RH because the source couples to `log Q`, while the centered measure contains the fractional global weight `Q^(1/4)`; the direct OS route lacks the required positive Hankel gluing.  This is a sharper target than generic "prove reflection positivity": construct or refute the missing positive gluing kernel for the critical tilt and identify it with the completed Weil form.

## Important audit correction

`GppVerify/QuantumGravity/WightmanAxioms.lean` is currently mostly scaffolding: W1–W6, OS reconstruction, CPT, spin-statistics, and the claimed RH/Wightman unification are represented by `True` theorems. The dimension checks are genuine, but this file must not be cited as a formal derivation of QFT axioms.

Likewise, `HaarPositivityWeil.lean` still contains legacy `True` wrappers for the GNS construction, adelic Haar-square positivity, Weil criterion, OS reconstruction, shadow reflection positivity, and universal positivity construction, even though some lower-level ingredients (for example the real convolution-square positive-type theorem in its later dedicated module) have since been genuinely formalized.  The AFT program should retire these wrappers by replacing them with explicit interfaces/dependencies rather than treating their names as results.

This makes the next AFT target precise: replace labels/placeholders by actual field-theoretic interfaces (Hilbert space, reflection operator, positive OS form, semigroup/spectral measure, and correlator/test-function map) and then identify that completed OS form with the genuine Weil quadratic form. The local prime-positive pieces alone are insufficient because the finite-prime term enters the standard explicit formula with the opposite overall sign.

## New theorem candidates pushed this run

1. Verify2 `2233ec76d34d016f63044be417e2500fdabfc972`: `ConformalShadowPrincipalSeries.lean`, proving for arbitrary real boundary dimension `d` that `Delta -> d-Delta` is involutive and equals complex conjugation iff `Re Delta=d/2`, with exact `d=1` arithmetic and `d=2`, `Delta=2s` celestial specializations. Workflow gate added at `1ca1646661669bb1ac1bee0a6bdbf821142b8e8e`.
2. Verify2 `6b5903c4cac6040e3152c8c62bbb159f5549c7d2`: raised-box reduced outer integral now explicitly equals `B(1-delta,3-delta) B(1-delta,2)` after the inner slice has been inserted. This does not fake the still-missing nested Fubini/endpoint passage.
3. Verify2 `e7d49114cabc1cc84910094348e1990eb10677b4`: `ZetaGibbsCriticalRegularization.lean`, defining `H(beta)=(beta-1)Z(beta)` and proving exactly on `beta>1`
   `log Z(beta)=log H(beta)-log(beta-1)`
   together with the corresponding Helmholtz free-energy split.  No `beta->1+` regularity or limit of `H` is asserted. Workflow gate added at `15199f2bb4dbf4e4302f6345a8bc09b9360e4034`.

## Connected active frontiers

1. **AFT / RH:** direct 1d shadow is `s <-> 1-s` with principal line `Re s = 1/2`; under celestial normalization `Delta=2s` this is `Delta <-> 2-Delta`, `Re Delta=1`. The focused Gaussian/BPY construction supplies a concrete Euclidean field candidate, but its critical `Q^(1/4)` tilt lacks the needed OS/Hankel gluing. The decisive missing theorem is completed AFT OS positivity plus exact transport to the genuine Weil form on an adequate test class. No RH claim.
2. **Scalar box:** exact inner affine simplex Beta slice and reduced outer Beta product are now source-level. Remaining raised-box step is the actual nested interval/Fubini endpoint handling, then dominated convergence. The structured physical scalar regulator limit is a separate already-developed layer.
3. **YM/gravity:** projector bookkeeping is already exact; missing object is the explicit `D_s=4`, `mu != 0` two-massive-vector/two-positive-helicity-gluon tree current and its sewn numerator. Higher-loop generalized cuts remain downstream.
4. **Prime thermodynamics:** exact cumulant/entropy/free-energy/fluctuation differential geometry on `beta>1` remains previously certified. The universal critical pole has now been split exactly at source level; next is derivative/limit control of the regularized factor without assuming zeta-specific regularity.
5. **Spectral:** all-order chamber weights are algebraically established; full iterated/convolution interpretation remains open even if the repaired Wiener–Hopf/Gamma normalization becomes CI-green.
