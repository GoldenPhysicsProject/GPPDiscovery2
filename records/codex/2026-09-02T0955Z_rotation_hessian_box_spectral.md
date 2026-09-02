# Codex rotation checkpoint — 2026-09-02 09:55Z

Scope: Codex/GPT track only. No Claude research inspected.

## 1. Scalar-box regulator lane

Current Verify2 workbench head before this checkpoint: `33aeb6922d0079af2f3b00234c09c0022c4b9931`.
GitHub Actions Build #1936 completed successfully on that exact SHA.

Certified middle singular integral:

`∫_0^L (S*x1)^(-δ) (L-x)^(1-δ) dx
 = (S*x1)^(-δ) L^(2-δ)/(2-δ)` for `δ < 1`.

Combining this with the already-certified inner endpoint integral gives the exact singular contribution to the post-middle envelope

`(S*x1)^(-δ) (1-x1)^(2-δ) / ((1-δ)(2-δ))`.

The regular contribution is `(1-x1)^2/2`; therefore the full analytic outer envelope remains

`(1-x1)^2/2 + (S*x1)^(-δ)(1-x1)^(2-δ)/((1-δ)(2-δ))`.

The remaining formal gap is not the integral algebra. It is the product-space/joint-measurability packaging needed to carry the variable-endpoint inner integral through the middle DCT, followed by outer DCT assembly. Do not claim `simplexMoment -> 1/6` in Lean until that layer is compiled.

## 2. Quadratically confined number gas

For

`Z(β,η)=Σ_{n>=1} exp(-β L_n - η L_n^2)`, `L_n=log n`, `η>0`,

the sufficient statistics are `(L,L^2)`. Finite truncations give the exact Hessian/covariance identities

`∂²_{ββ} log Z = Var(L)`,
`∂²_{βη} log Z = Cov(L,L²)`,
`∂²_{ηη} log Z = Var(L²)`.

Hence

`det Hess(log Z) = Var(L) Var(L²) - Cov(L,L²)^2`.

Because the support contains at least three distinct positive integers, `L²` is not affine in `L` on the support, so the covariance determinant should be strictly positive once the countable differentiation and nondegeneracy argument are formalized. This is the clean next theorem: the confined two-parameter family is a strictly convex exponential family for every real β and every η>0.

Executable discovery check added at `prime_gas/quadratic_confinement_hessian_check.py`. Sample finite truncations at `(β,η)=(0,.2),(1,.1),(-3,.4),(2,.05)` all returned positive determinants.

## 3. Principal-series / Weil lane

No promotion of local spectral positivity to Weil positivity. The current honest bridge remains: construct a concrete test-transform class for which explicit-formula positivity is available and prove arbitrary finite interpolation on the zero set together with its reflected set. The local completed-zeta/principal-series response and shadow/reflection algebra are inputs, not the missing global positivity theorem.

## 4. Spectral / Mehler-Fock / Wiener-Hopf lane

Preserve the corrected distinction between the two Gamma products:

`Γ(1+iλ) Γ(1-iλ) = π λ / sinh(π λ)`,

whereas

`Γ(1/2+iλ) Γ(1/2-iλ) = π / cosh(π λ)`.

The exact shifted-sech self-convolution is already formalized in Verify2; it must not be extrapolated into a repeated-sech/chamber theorem without a separate proof. A useful next structural target is to derive the chamber transition law from the exact Gamma recurrence and then identify precisely which chamber densities admit a Wiener-Hopf convolution representation.

## 5. Physics boundary

The focused scalar-box paper establishes the scalar cut -> Mellin -> dispersion chain, but this does not by itself sew Yang-Mills numerators. After regulator closure, the next honest dynamical object is the fixed-loop-momentum nonzero-μ product of tree amplitudes summed over the three massive-vector polarizations. State counting and dimensional-reconstruction algebra are not a substitute for that numerator.
