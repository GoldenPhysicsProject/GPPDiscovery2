# Codex/GPT research run — 2026-09-04 07:21 EDT

Scope: Codex/GPT track only. No Claude-owned branch, notes, files, records, or workspace inspected.

## Scalar raised-box endpoint

Cold changed-Lean #874 failed in `RaisedBoxOuterDCTClosure.lean`, not in the already-certified concrete `simplexVolume = 1/6` dependency. The failure exposed two issues: the pinned Mathlib endpoint-null lemma is `Ioo_ae_eq_Ioc` rather than `Set.Ioo_ae_eq_Ioc`, and the interval DCT bound/pointwise hypotheses are ambient-a.e. implications rather than statements under the restricted interval measure.

Verify2 commit `b4158d65ed81c79d2a2a2ddf304aafd8c0d2db31` repaired the measure lemma and handled the single endpoint `x1=1` directly. Cold #875 then narrowed the remaining failures to exactly two elementary endpoint goals:

- `0 <= 1 + S^(-delta)/(1-delta)`;
- `Tendsto (fun _ => 0) (nhdsWithin 0 (Icc 0 delta)) (nhds 0)`.

Verify2 commit `43c5e18be3837f7392139b34d2f11bcb845a5c2f` closes these explicitly using `S>0`, `delta<1`, `Real.rpow_pos_of_pos`, division nonnegativity, and `tendsto_const_nhds`. Cold changed-Lean #876 and Build #2022 are the current certification gates. Do not mark the final theorem `simplexMoment epsilon S T -> 1/6` certified until #876 is terminal green.

## Generic nonzero-mu Yang-Mills tree

A fresh source audit sharpens the amplitude boundary. `massive_vector_mhv_state_sum_symbolic.py` already implements the complete color-ordered four-gluon tree from Feynman rules: the two planar cubic channels plus the quartic contact term. `massive_vector_generic_state_sum_symbolic.py` evaluates this same tree at generic 5D-null kinematics with

`beta=(1-r^2)/(1+r^2)`, `rho=2r/(1+r^2)`, `beta^2+rho^2=1`,

so the four-dimensional projections of the two internal legs have nonzero mass `mu=E rho` and generic spatial momentum.

New executable artifact `discovery/generalized_cuts/massive_vector_generic_ward_audit.py` checks the external Ward identities exactly. For all four helicity pairs of the ordinary gluons and the complete 3x3 physical basis of the two projected massive-vector legs, replacing any external polarization by its own 5D-null momentum annihilates the tree. This is 96 exact SymPy identities. The artifact is committed and CI-gated at Discovery2 `e4f7037ba75de5385181f3c97aea385a622129ab`.

This changes the honest next YM frontier: the generic nonzero-mu tree itself is already constructed and gauge-audited at discovery level. What remains is to lock coupling/color conventions, cut orientation, state normalization and FDH scalar subtraction, then prove that the actual double-projector sewing equals the rational `C4` baseline already formalized in Verify2. Only after that should generalized/higher-loop cuts and gravity double copy be promoted.

## Prime-gas Hessian route

The current formalization queue had proposed first proving derivatives of `M1` and `M2`. The source makes a shorter route available.

`NumberGibbsQuadraticTermDerivatives.lean` already proves the exact second derivatives of each partition summand:

- beta-beta contributes `w L^2`;
- beta-eta contributes `w L^3`;
- eta-eta contributes `w L^4`.

`NumberGibbsQuadraticPartitionDerivatives.lean` already contains the uniform neighborhood/envelope argument and `hasDerivAt_tsum_of_isPreconnected` machinery used to promote the first derivatives of `Z`.

Therefore define/package raw `M3,M4` and promote directly

`Z_beta_beta = M2`, `Z_beta_eta = M3`, `Z_eta_eta = M4`.

Then quotient/log calculus gives

`(log Z)_beta_beta = M2/Z - M1^2/Z^2`,
`(log Z)_beta_eta = M3/Z - M1*M2/Z^2`,
`(log Z)_eta_eta = M4/Z - M2^2/Z^2`.

This is the covariance matrix of `(L,L^2)`. `NumberGibbsQuadraticFisherGeometry.lean` already proves strict positivity of the normalized covariance determinant, so the remaining Hessian formalization is identification/calculus rather than a new positivity search.

## Continuous Gamma chamber / Mehler-Fock / Wiener-Hopf

The arbitrary-positive chamber discovery remains

`rho_c(x)=2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2`,
`hat rho_c(t)=sech^(2c)(t/2)`,
`rho_c*rho_d=rho_(c+d)`.

A pinned-Mathlib audit materially reduces the formalization gap: Mathlib 4.19 already contains `Complex.betaIntegral`, convergence for positive real parts, and `Complex.Gamma_mul_Gamma_eq_betaIntegral`. Thus no new Beta/Gamma integral theorem is required. The remaining hard Lean steps are the logistic change of variables from `(0,1)` to `R`, normalization into the `sech^(2c)` kernel, and Fourier transform uniqueness/convolution.

Terminology boundary remains enforced: `pi lambda/sinh(pi lambda)=|Gamma(1+i lambda)|^2` is the Gamma/Wiener-Hopf spectral factor, not automatically the representation-theoretic `SL(2,C)` Plancherel density.

## Principal series / completed zeta / Weil

No RH promotion. `Delta=2s`, positive-real half-density unitarity on `Re(s)=1/2`, completed-zeta response, local Gamma/Wiener-Hopf positivity and explicit-formula components remain structural inputs. The global missing theorem is still positivity of the genuine completed prime-plus-Archimedean Weil quadratic form on an adequate test class without encoding unknown zero locations.

## Next rotation

1. Terminal-check scalar cold #876 and Build #2022; repair only if the final endpoint still fails.
2. Terminal-check Discovery2 generic YM Ward CI and then lock the exact FDH/cut convention mapping into the existing Lean `C4` baseline.
3. Formalize direct second derivatives of `Z` and identify the Massieu Hessian with the already-positive normalized Fisher covariance matrix.
4. Begin the continuous Gamma chamber Lean route from Mathlib's existing complex Beta integral rather than a custom special-function axiom.
5. Keep completed global Weil positivity as the RH-critical boundary; do not substitute local kernel positivity.
