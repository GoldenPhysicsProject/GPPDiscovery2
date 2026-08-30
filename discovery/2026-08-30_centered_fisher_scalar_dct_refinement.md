# Centered Fisher and raised-box DCT refinement — 2026-08-30

## Scope and provenance

Codex/GPT track only. This audit uses the current `GPPVerify2:codex/lean-workbench` sources and the focused celestial/principal-series papers. No Claude work was inspected.

## 1. Countable prime-Fisher geometry: strictness is already centered

A previous compressed status report risked understating/overstating different files. The exact source state is:

- `PrimeFisherTwoParameterStrict.lean` proves strict positivity for the **uncentered** polynomial score `a log n + b (log n)^2` under the unnormalized Fisher weight.
- `PrimeFisherCenteredGeometry.lean` separately defines

  `p_{β,a,b}(x) = -(a μ1 + b μ2) + a x + b x^2`

  with `μ1 = Eβ[X]`, `μ2 = Eβ[X^2]`, proves `p != 0` whenever `(a,b) != (0,0)`, and then invokes the all-order strict polynomial Gram theorem to obtain the genuinely centered normalized statement

  `Eβ[(a(X-μ1)+b(X^2-μ2))^2] > 0`.

Thus strict positive definiteness of the centered two-observable quadratic form is already formalized on `β>1`. The remaining endpoint is not strictness itself; it is the exact coefficient expansion identifying this quadratic form with

`A a^2 + 2 B a b + C b^2`,

where

- `A = Varβ(X)`,
- `B = Covβ(X,X^2)`,
- `C = Varβ(X^2)`.

Once this `tsum` expansion is packaged, `StrictQuadraticDeterminant.lean` immediately yields

`A*C - B^2 > 0`.

Equivalently one may identify the same quantity with `PrimeFisherHankelSchurBridge.centeredCovDet`; the Schur identity already proves

`det H3 = m0^3 det Cov(X,X^2)`.

### Retraction/correction

Do not describe `PrimeFisherTwoParameterStrict` itself as centered. The centered theorem is `PrimeFisherCenteredGeometry.normalized_centered_quadratic_pos`. Conversely, do not describe centered strictness as missing: it is already certified in source. The missing theorem is the coefficient-identification bridge to the explicit covariance determinant.

## 2. Raised scalar box: exact DCT boundary

The concrete object is already the physical nested moment

`J_ε(S,T) = ∫_0^1 dx1 ∫_0^(1-x1) dx2 ∫_0^(1-x1-x2) dx3 Q(S,T;x)^(-ε)`

with

`Q = S x1 x3 + T x2 (1-x1-x2-x3)`.

Verified source infrastructure already gives:

1. `Q>0` on the strict Euclidean simplex interior for `S,T>0`.
2. Pointwise `Q^{-ε} -> 1` as `ε -> 0` on that interior.
3. For `0 <= ε <= δ`, `0<δ<1`,

   `Q^{-ε} <= 1 + (S x1 x3)^(-δ)`.

4. The singular one-channel majorant is integrable and its nested simplex integral reduces exactly to

   `S^{-δ} B(1-δ,3-δ) B(1-δ,2)
    = S^{-δ} Γ(1-δ)^2 / Γ(4-2δ)`.

5. `J_0` is exactly the affine simplex volume, already separately reduced to `1/6` in the zero-volume layer.

The sole analytic closure theorem still absent is therefore the actual nested dominated-convergence composition

`Tendsto (fun ε => J_ε(S,T)) (nhdsWithin 0 (Ici 0)) (nhds (1/6))`.

The implementation should treat simplex boundary faces as measure-zero and use AE pointwise convergence; imposing strict positivity on endpoints is unnecessary and makes the Lean proof harder.

## 3. Spectral / principal-series consistency

The focused principal-series paper and current Verify2 modules agree on the dictionary `Δ=2s` and on the critical-line Gamma weight. The continuously extended Wiener–Hopf weight must be used at λ=0. It is distinct from the scalar `SL(2,C)` Plancherel density. The already-formalized all-chamber positivity theorem is a spectral/Gamma statement only; it must not be promoted to global Weil positivity.

## 4. Arithmetic Weil boundary

The focused arithmetic principal-series program isolates the same global obstruction as Verify2: the prime commutator construction recovers the exact von Mangoldt prime-power anomaly, but prime commutators are not absolutely trace-norm summable. The missing global theorem is a relative prime-plus-Archimedean trace/Gram construction with non-circular positivity (or equivalent contractive defect operator). No RH claim follows before that theorem.

## 5. YM/gravity boundary

No change in status: existing state-count, Ward-reconstruction, μ^4 dimension-shift and μ^8 gravity radial modules are algebraically useful, but honest field-theory closure requires explicit nonzero-μ tree amplitudes and polarization sewing at fixed loop momentum before generalized/higher-loop cuts are claimed.

## Next executable formalization targets

1. Prove the centered-score `tsum` coefficient identity and compose it with `StrictQuadraticDeterminant` to obtain the strict countable covariance determinant.
2. Implement the first nested interval DCT layer for the concrete raised-box integrand using AE interior convergence and the certified one-channel majorant.
3. Only after those gates are green, resume explicit massive-vector tree sewing and the global Weil transfer/relative-trace construction.
