# Codex/GPT rotation: scalar strip measurability and number-gas Hankel curvature

Scope: Codex/GPT only. No Claude research, branches, notes, or artifacts inspected.

## Scalar box

GPPVerify2 `codex/lean-workbench` advanced from certified head `0ff44e9d1fdc7a6413b8995c0d8d025f8b5388f2` (Build #1937 green) to `a56050c71f75e809aeb23d8a02da3bdd2f0a7413`.

The new Lean layer defines, for fixed outer coordinate x1,

`innerSimplexStrip x1 = {(x2,x3) | 0 <= x3 and x2+x3 <= 1-x1}`

and proves the strip Borel measurable, then proves the raised-box integrand extended by zero off this strip is measurable. This is the precise product-measure packaging needed before applying `integral_prod_right'`/Fubini to the variable-endpoint inner integral.

Build #1938 was in progress at recording time; do not call the new theorem certified until terminal success.

Next scalar step: use the measurable strip function to obtain measurability of the x2-parameterized x3 integral, then compose the already-certified inner DCT with the exact middle majorant integral and outer DCT to prove the unconditional regulator limit `simplexMoment epsilon S T -> 1/6` for positive Euclidean S,T.

## Prime-gas information geometry

For the quadratically confined number gas with sufficient statistics `(X,X^2)`, put `Z=X-E[X]` and `m_k=E[Z^k]`. The Fisher determinant simplifies exactly to

`D = m2*m4 - m3^2 - m2^3`.

Let the centered Hankel moment matrix be

```
H = [[1,  0, m2, m3],
     [0, m2, m3, m4],
     [m2,m3, m4, m5],
     [m3,m4, m5, m6]].
```

Direct symbolic elimination gives the exact identity

`det(curvature_numerator_matrix) = det(H) - D^2`.

Therefore the two-dimensional Hessian scalar curvature is

`R = (D^2 - det(H))/(2 D^2) = 1/2*(1-det(H)/D^2)`.

The mean cancels identically, so this curvature expression is translation invariant in X. Since H is a moment Gram matrix, `det(H) >= 0`; hence every nondegenerate finite truncation satisfies the structural upper bound `R <= 1/2`. This does NOT prove `R < 0`: negativity is equivalent to the stronger inequality `det(H) > D^2`.

The executable audit `prime_gas/quadratic_confinement_scalar_curvature.py` now checks this Hankel reduction numerically in addition to the independent finite-difference Ricci audit.

Next number-gas step: formalize the finite moment/Hankel identity, then prove countable differentiation under the quadratically confined partition sum so the identity applies to the full infinite Gibbs family.

## Other fronts and boundaries

Principal-series/Weil boundary unchanged: local half-density/unitarity, Delta=2s, completed-zeta response, Gamma/Wiener-Hopf kernels and chamber positivity do not imply the global Weil quadratic-form positivity. The unresolved bridge remains an explicit-formula test algebra plus the required interpolation/global positivity argument.

Spectral/chamber boundary unchanged: keep exact Gamma recurrences and chamber threshold/unimodality results; do not infer repeated-sech convolution identities without proof.

YM/gravity boundary unchanged: state counting and scalar-box closure are not amplitude sewing. After regulator closure the next physical object remains the fixed-loop-momentum nonzero-mu YM tree-current product sewn over the three massive-vector polarizations, followed by generalized/higher-loop cuts and double copy.
