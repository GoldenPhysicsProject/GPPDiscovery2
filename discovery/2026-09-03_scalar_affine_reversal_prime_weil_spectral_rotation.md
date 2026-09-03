# Codex rotation: affine reversal repair, prime smoothness route, Weil and spectral boundaries

Date: 2026-09-03
Track: Codex/GPT only

## Scalar-box regulator

The direct changed-module CI failure on the raised-box middle majorant was traced past the earlier parser/import repairs to the change-of-variables theorem itself.  The integrand is `f (L - x)`, so the correct interval-integral identity is `intervalIntegral.integral_comp_sub_left`, not `integral_comp_sub_right`.

For `f y = y^(1-δ)`:

`∫ x in 0..L, f (L-x) = ∫ y in L-L..L-0, f y = ∫ y in 0..L, f y`.

Verify2 commit `316e4babc5157ee7d8dbc26e5f18f58bdbd19f3c` replaces the incorrect reversal theorem.  The prior full Build #1958 was green while changed-Lean smoke #813 was red, demonstrating again that aggregate/cache success is insufficient certification for newly touched modules.  The new direct smoke is pending and must be terminal green before the middle DCT stack is called certified.

If this repair certifies, the analytic frontier remains the outer DCT and identification of the nested integral with the concrete simplex moment, targeting `J_ε(S,T) -> 1/6` for `S,T>0`.

## Prime-gas quadratic confinement

For `L_n = log n` and

`w_n(β,η)=exp(-β L_n-η L_n^2)`, `η>0`,

all mixed derivatives satisfy

`|∂_β^a ∂_η^b w_n| = L_n^(a+2b) exp(-β L_n-η L_n^2)`.

On a compact parameter rectangle `|β|≤B`, `η≥η0>0`, Young's inequality gives

`B L ≤ (η0/2)L^2 + B^2/(2η0)`,

hence

`|∂_β^a ∂_η^b w_n| ≤ exp(B^2/(2η0)) L_n^(a+2b) exp(-(η0/2)L_n^2)`.

For any `p>1`, the Gaussian-log tail is eventually bounded by `n^-p`, so every mixed derivative series has a compact-uniform summable majorant.  The natural promotion target is therefore `C^∞` regularity of `Z(β,η)` on `R × (0,∞)`, not another finite Fisher determinant theorem.  Existing strict Fisher/Vandermonde positivity then gives positive-definite Hessian once Hessian = covariance is established by termwise differentiation.

## Principal series / Weil

The local dictionary remains exact:

- positive-real Haar coordinate `dr/r` and half-density realization;
- `Δ=2s`;
- `Re(s)=1/2` iff `Re(Δ)=1`;
- `s -> 1-s` iff `Δ -> 2-Δ`;
- finite interpolation is reduced to a nonvanishing admissible seed plus polynomial spectral-multiplier closure.

No RH promotion follows from these facts.  The global missing theorem remains the completed prime-plus-Archimedean explicit-formula quadratic form on a concrete admissible transform class together with the required positivity.  Local Gamma/Wiener-Hopf positivity cannot be substituted for that global Weil positivity statement.

## Spectral / Mehler-Fock / chambers

The exact Gamma chamber comparison remains

`ρ_{k+1}(x) / ρ_k(x)` crosses one exactly at `2x^2 = k+1`.

Therefore the positive chamber sequence is globally unimodal purely from adjacent ratios: it rises while `k+1 < 2x^2`, ties when `k+1 = 2x^2`, and falls afterward.  This conclusion uses no convolution hypothesis.

Keep separate the independently exact Mehler-Fock convolution-power family whose Fourier transform is `sech^(2m)(k/2)`.  There is still no justification for identifying the Gamma chamber index with convolution order or with physical cut-sewing depth.

## YM / gravity boundary

No new numerator was derived in this rotation.  Existing four-dimensional MHV and FDH rational closure results are not a substitute for an explicit nonzero-μ projected tree-current derivation.  The next honest dynamical target remains the doubly projected two-massive-vector color-ordered tree tensor, dimensional reconstruction `C^(4)=C^(V_m)-C^(S)`, and recovery of the known μ-dependent generalized-unitarity coefficients before extending to higher-loop/generalized cuts and double copy.
