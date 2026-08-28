# Codex continuation — AFT/spectral/shadow audit — 2026-08-28

Codex/GPT track only. No Claude work inspected.

## CI checkpoint

At Verify2 `571553fe567d497b054bbba68d292b979184a6d0`, the dedicated spectral, arithmetic-OS, Gibbs, and Fisher workflows are green. The full Wiener–Hopf/Gamma chamber hierarchy and the pinned-Mathlib `Aᴴ A` arithmetic OS factorization criterion are CI-certified.

The certified spectral chain includes

`extendedWienerHopfWeight x = (pi/2) * Re(rhoGamma 0 x)`,

its inverse, the all-real Mehler–Fock chamber family, and

`rhoGamma k x = (prod_{j<k} rhoStepFactor j x) * rhoGamma 0 x`,

with positive chamber multipliers. Every formal Gamma chamber therefore sits over the same positive Wiener–Hopf base spectral weight.

## AFT / arithmetic OS

The explicit finite prime-local factor map introduced at `63d7eca...` initially failed only because pinned Mathlib spells the square-root identity `Real.sq_sqrt`. Verify2 `66874521e4b7f65a403b340f28b8ecb17e8a07c1` repairs that proof. Its dedicated arithmetic-OS workflow is green, so the finite prime factor map is now CI-certified.

For cutoff `M`, positive-time samples `t_i`, and prime scale `p`,

`A_p(m,i)=sqrt(modeWeight p (m+1)) * modeValue p (m+1) (t_i)`,

and definitionally

`K_p=A_pᴴ A_p`.

Thus prime-local factorization is no longer hypothetical. The global obstruction is the opposite sign of the prime term in the completed explicit formula: the positive local factors cannot simply be direct-summed into the completed kernel.

To isolate the exact no-ghost theorem needed next, Verify2 `028b429d7def5b2ac8c6ded53acbb89b1ff8b766` adds `ArithmeticCompletedDefectCriterion.lean`. For ambient/Archimedean amplitude `Ainf` and assembled prime amplitude `Aprime`, define

`D(x)=||Ainf x||^2-||Aprime x||^2`.

The file proves that pointwise contractive domination

`||Aprime x|| <= ||Ainf x||`

implies `D(x)>=0`, and also that an exact physical factorization

`D(x)=||Aphys x||^2`

makes positivity automatic. This is deliberately only a sufficient criterion; it does not construct `Ainf`, prove the contraction, identify `D` with the Weil form, or prove RH. Workflow gate is cumulative Verify2 `f3bc26cc89fa4049c1d2527bb64cb855a3838ec5`; CI was running at record time.

The AFT target is now sharply decomposed:

1. construct the Archimedean/ambient factor from zero-independent completed data;
2. assemble the already-explicit prime factors;
3. prove a no-ghost contraction or exact norm-square defect identity;
4. identify the resulting completed OS form with the genuine Weil quadratic form on an adequate test class.

## Shadow / discrete symmetries / Grassmannian

Verify2 `355a4c072b34df06ca671953203967157600580a` adds `ShadowDiscreteSymmetrySeparation.lean`. It proves at the helicity-label level

`shadow(h)=-h`, `T(h)=h`, `P(h)=-h`,

so shadow has the same necessary helicity-sign action as parity and differs from pure time reversal on every nonzero-helicity sector, including spin 1 and spin 2. This is not a full identification of shadow with parity/PT/CPT. The theorem is gated into the Grassmannian workflow at `cee8ffee884a0e46c91d098d946275a1d9dc1741`; dedicated push-workflow certification was not yet visible through the available run-query endpoint, so it remains source-level pending an observable CI result.

The deeper Gr(2,4) target remains descent of the antiunitary twistor googly lift to the actual complex 2-plane type and comparison, under proved hypotheses, with orthogonal-complement shadow.

## Corpus corrections recorded in Supabase Codex notes

The Codex record now explicitly retires or flags the following rather than allowing them to reappear silently:

- the continuous-spectrum/multiplicity-one RH shortcut;
- the claim that plain unitarity alone proves RH;
- legacy `True` wrappers in `WightmanAxioms.lean`, `HaarPositivityWeil.lean`, `HaarMeasure.lean`, `FunctionalEquation.lean`, and `L2Constraint.lean` as scaffolding rather than proofs;
- the old celestial ladder all-loop rationality theorem: its proof mechanism is valid only through L=2 and fails at weight 6; the focused M3 investigation gives `M3 = 0.0010280204768206811181554290742928570866263084` and no rational relation with denominator <= 10^20;
- the ONON claim that generic bipartite entanglement is measured by `dim(Lambda_A intersect Lambda_B)` and entropy by `log dim(intersection)`: as written it lacks a canonical state-to-plane map and is internally inconsistent (`log 0` for separable states, `log 1=0` for the same text's maximally entangled case);
- the claimed universal celestial Kac–Moody quantization `k=4pi/g_eff^2` of a physical running gauge coupling and the exact corollary `alpha_s(Lambda_QCD)=1`: these require a genuine current-normalization/anomaly derivation and are not formal infrastructure.

## Spectral / loop correction and opportunity

The focused loop paper's exact Wiener–Hopf statement survives audit:

`P(lambda)=pi*lambda/sinh(pi*lambda)` has Fourier transform

`P_hat(k)=pi/(2 cosh(k/2)^2)`,

with factors

`P_hat_±(k)=(1/sqrt(2pi))*Gamma(1/2 ∓ i k/(2pi))^2`.

Their product has the correct normalization by the Gamma half-shift modulus identity. The paper's Parseval route gives the exact L=2 moment `M2=1/90`. What fails is the extrapolation to all-loop rationality, not the base Wiener–Hopf structure. For L=3 the natural decomposition uses one-sided convolution `h`, one-sided correlation `K`, and distinct chamber orbits rather than a universal octant fraction.

This gives a better spectral-convolution frontier: formalize the exact L=2 convolution/Parseval identity and then the honest L=3 chamber decomposition without imposing rationality.

## Gibbs / number thermodynamics

Critical pole removal and the exact cumulant/entropy/free-energy/fluctuation differential layer remain CI-green on `beta>1`:

`H(beta)=(beta-1)Z(beta)>0`,

`log Z(beta)=log H(beta)-log(beta-1)`,

`F(beta)=-log H(beta)/beta + log(beta-1)/beta`.

The next honest analytic input remains regularity/derivative control of `H` as `beta -> 1+`.

## Scalar box

Inner affine simplex Beta reduction and outer Beta product remain established. The exact blocker remains the nested interval/Fubini endpoint passage and then dominated convergence for the regulator. Beta-to-Gamma simplification is downstream algebra, not a substitute for this missing step.

## Yang–Mills / gravity / higher cuts

No trustworthy focused formula has yet supplied the explicit `D_s=4`, `mu != 0` two-massive-vector/two-positive-helicity-gluon tree current. Existing Ward/projector reconstruction is exact; the sewn numerator and generalized cuts remain downstream. No numerator has been guessed.

## Next rotating frontiers

1. Check `f3bc26c...` AFT defect-criterion CI and repair/build immediately.
2. Construct an actual finite completed prime–Archimedean toy model using the explicit prime factor and existing contraction/no-ghost primitives, while keeping existence assumptions visible.
3. Formalize the exact L=2 Wiener–Hopf/Parseval convolution identity and rescope the old all-loop theorem to the certified L<=2 statement.
4. Push raised-box nested Fubini/endpoint/DCT closure.
5. Continue the Gr(2,4) antiunitary descent and shadow-vs-discrete-symmetry audit.
6. Replace legacy theorem wrappers progressively with real interfaces.
7. Continue honest YM current search/derivation before any sewing claim.
