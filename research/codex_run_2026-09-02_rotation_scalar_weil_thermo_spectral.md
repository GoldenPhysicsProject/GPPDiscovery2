# Codex/GPT rotation checkpoint — scalar box, principal series/Weil, thermodynamics, spectral chambers

Codex/GPT track only. Claude branches, notes, and research were not inspected.

## Scalar-box formal advance

The exact singular part of the nested raised-box DCT envelope has now been packaged in Lean on `GPPVerify2:codex/lean-workbench` at commit `33aeb6922d0079af2f3b00234c09c0022c4b9931`:

`∫_0^L (S x1)^(-δ) (L-x)^(1-δ) dx = (S x1)^(-δ) L^(2-δ)/(2-δ)` for `δ<1`.

This composes the already-formalized affine middle integral with constant-factor interval-integral linearity. It is exactly the singular contribution appearing after the certified `x3` majorant integration. The full middle envelope is therefore

`L^2/2 + (S x1)^(-δ) L^(2-δ)/((1-δ)(2-δ))`, with `L=1-x1`.

The new exact head did not yet have a workflow run attached when checked, so this checkpoint does not call the theorem CI-certified. The prior `GPPVerify2` head `ec6ac9cafaab1145c5dfc767f461a00dbefc3847` is certified by Build #1935.

Remaining scalar-box Lean boundary: package the measurable simplex-strip indicator on `(x2,x3)`, obtain middle-integral AEStronglyMeasurable via `AEStronglyMeasurable.integral_prod_right'`, apply middle DCT, then the already-proved outer-kernel integrability to obtain the unconditional concrete regulator limit `simplexMoment ε S T -> 1/6`.

## Positive-real principal series and completed-zeta response

Current Lean already proves the exact dictionary needed here:

- `Δ=2s` sends the celestial principal axis `Re Δ=1` to `Re s=1/2`.
- The completed-zeta logarithmic response `Λ'(Δ/2)/Λ(Δ/2)` has zero real part on that axis away from zeros.
- Multiplying by `-i` gives a real phase response there.
- Functional-equation reflection becomes scalar-shadow oddness `Δ -> 2-Δ`; on `Re Δ=1`, shadow equals complex conjugation.

This is a response/representation theorem, not RH.

The current Weil reduction is also sharper than a vague global-surjectivity target. `WeilInterpolationBridge.lean` proves that it is enough for the candidate test-transform class to interpolate arbitrary coefficient data on each finite pair-support

`S ∪ zetaInvolution(S)`.

Thus the genuine analytic frontier is: construct a concrete Mellin/Paley-Wiener/Wiener-Hopf test class whose explicit-formula quadratic form is positive and whose transform has this finite pair-support interpolation property. No local Gamma/chamber positivity result substitutes for that requirement.

## Quadratically confined number thermodynamics

The existing two-parameter family

`w_{β,η}(n)=exp(-β log(n+1)-η log(n+1)^2)`, `η>0`,

already has formalized convergence for every real `β`, positive partition function, generalized Legendre identities, and strict positivity of the normalized covariance/Fisher determinant for the observables `(L,L^2)`.

The next nonredundant theorem is differential rather than algebraic: prove differentiability of `log Z(β,η)` and identify its Hessian with the covariance matrix of `(L,L^2)` (with the expected sign convention in the mixed/parameter derivatives). This upgrades the currently algebraic Fisher determinant to the actual thermodynamic information geometry of the partition function.

## Spectral Gamma / Wiener-Hopf chamber lane

The chamber recurrence is already exact and stronger than a qualitative positivity statement. If `ρ_k(x)` denotes the real Gamma spectral density, adjacent chambers satisfy comparison thresholds at

`2 x^2 = k+1`.

Lean proves:

- `ρ_k(x) < ρ_{k+1}(x) <-> k+1 < 2x^2`,
- `ρ_{k+1}(x) < ρ_k(x) <-> 2x^2 < k+1`,
- equality exactly at the threshold,
- for `k>0`, chamber `k` is a strict local maximum exactly when `k < 2x^2 < k+1`.

No convolution assumption enters these theorems. Therefore the next salvage target should not be another recurrence corollary; it should connect the exact chamber density to the already-formalized sech-convolution/Wiener-Hopf kernels and determine which convolution identities genuinely survive. Repeated-sech folklore remains unproved and must not be inferred from chamber positivity.

## Honest Yang-Mills boundary

The dimensional-reconstruction files themselves explicitly state the missing physics: they prove state-count algebra only and do not compute the fixed-loop-momentum `D_s=4`, `μ≠0` gluon sewing numerator. That dynamical numerator remains the next YM target after scalar-box closure; state counting, polarization bookkeeping, or the relation `C^(D_s)=C^(4)+(D_s-4)C_scalar` does not replace the actual sewn tree amplitudes.
