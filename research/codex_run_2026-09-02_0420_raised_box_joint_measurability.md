# Raised-box middle DCT: joint-measurability closure

Codex/GPT track only. No Claude context or branches inspected.

## Exact remaining measure-theoretic interface

For fixed `S,T>0`, fixed strict `x1∈(0,1)`, and regulator `ε`, define on `R×R`

`Fε(x2,x3) = 1_{0 < x3 ∧ x1 + x2 + x3 ≤ 1} · integrand ε S T x1 x2 x3`.

The physical variable-endpoint inner integral can be represented as an ordinary product-space integral:

`∫ x3 in 0..(1-x1-x2), integrand ε S T x1 x2 x3
 = ∫ x3, Fε(x2,x3)`

for `0≤x2≤1-x1` (endpoint conventions differ only on null boundary sets).

The map `(x2,x3) ↦ integrand ε S T x1 x2 x3` is Borel measurable because `Q` is polynomial/affine in `(x2,x3)` and `Real.rpow` with fixed exponent is measurable. The simplex-strip indicator is measurable because

`{(x2,x3) | 0 < x3 ∧ x1+x2+x3 ≤ 1}`

is an intersection of inverse images of Borel intervals under continuous affine maps. Hence `Fε` is jointly AEStronglyMeasurable. Mathlib's product-integral theorem `AEStronglyMeasurable.integral_prod_right'` then gives AEStronglyMeasurable of

`x2 ↦ ∫ x3, Fε(x2,x3)`.

This supplies precisely the missing eventual measurability hypothesis for the middle dominated-convergence step. No new majorant or special-function algebra is needed.

## Limit and majorant after the inner DCT

For strict `0<x2<1-x1`, the certified inner DCT gives

`Iε(x2) → 1-x1-x2`.

The one-channel majorant integrates explicitly in `x3` to

`|Iε(x2)| ≤ (1-x1-x2)
 + (S x1)^(-δ) (1-x1-x2)^(1-δ)/(1-δ)`

for `0<δ<1` and `0≤ε≤δ`.

This middle majorant is integrable on `[0,1-x1]`; integrating it gives

`∫_0^(1-x1) M(x2) dx2
 = (1-x1)^2/2
 + (S x1)^(-δ) (1-x1)^(2-δ)/((1-δ)(2-δ)).`

Therefore middle DCT yields

`∫_0^(1-x1) Iε(x2) dx2 → (1-x1)^2/2`.

The remaining outer domination is exactly the already-certified kernel

`(1-x1)^2/2 + S^(-δ) x1^(-δ)(1-x1)^(2-δ)/((1-δ)(2-δ))`,

which is integrable for `δ<1`. The outer limit is elementary:

`∫_0^1 (1-x1)^2/2 dx1 = 1/6`.

Thus the analytic regulator limit has no remaining conceptual gap: the only Lean work is packaging the joint measurable indicator representation, applying product-integral measurability, and composing middle then outer DCT.
