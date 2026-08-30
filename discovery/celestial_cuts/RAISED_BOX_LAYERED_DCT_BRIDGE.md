# Raised-box layered dominated-convergence bridge

## Exact target

For Euclidean invariants `S,T>0`, let

`Q = S x1 x3 + T x2 x4`, `x4 = 1-x1-x2-x3`,

on the affine simplex `x_i >= 0`, `x1+x2+x3 <= 1`.  For a fixed `0 < delta < 1` and `0 <= epsilon <= delta`, the already-formalized one-channel estimate gives

`Q^(-epsilon) <= 1 + (S x1 x3)^(-delta)`

at interior points.

The right-hand side can be integrated *layer by layer* in the same nested interval coordinates already used by `RaisedBoxConcreteMoment`, avoiding the need to introduce a new abstract 3-dimensional simplex measure before closing the physical limit.

## Exact layered majorant

Write

`M_delta = 1 + S^(-delta) x1^(-delta) x3^(-delta)`.

For fixed `x1,x2` in the nondegenerate slice and `a = 1-x1-x2`,

`integral_0^a M_delta dx3`

is bounded/evaluated by

`a + S^(-delta) x1^(-delta) a^(1-delta)/(1-delta)`.

Integrating the resulting expression in `x2` from `0` to `1-x1` yields

`(1-x1)^2/2 + S^(-delta) x1^(-delta) (1-x1)^(2-delta)/((1-delta)(2-delta))`.

The final `x1` integral is finite exactly for `delta<1`, and equals

`1/6 + S^(-delta) * Gamma(1-delta)^2 / Gamma(4-2 delta)`.

Equivalently, the singular part is the Dirichlet integral

`integral_{Delta_3} (S x1 x3)^(-delta) dx = S^(-delta) Gamma(1-delta)^2/Gamma(4-2 delta)`.

This agrees exactly with the already-formalized unscaled `nestedSimplexIntegral` Gamma closure.

## Formalization consequence

The shortest Lean closure route is therefore not necessarily a product-measure/Fubini rebuild.  It can proceed by nested one-dimensional dominated convergence in the same coordinates as `simplexMoment`:

1. inner `x3` DCT on `[0,1-x1-x2]`, dominated by `1 + S^(-delta)x1^(-delta)x3^(-delta)`;
2. package the resulting inner-integral bound as the explicit `x2` majorant above;
3. apply `x2` DCT on `[0,1-x1]`;
4. package the explicit outer Beta majorant;
5. apply the final `x1` DCT on `[0,1]`;
6. use `simplexMoment_zero` plus `simplexVolume=1/6`.

Existing `RaisedBoxSimplexBetaLayer.scaled_beta_convergent`, `inner_simplex_slice_convergent`, `RaisedBoxSimplexMeasureBridge.outer_reduced_beta_convergent`, and `RaisedBoxSimplexGammaClosure` provide almost all endpoint/integrability data required.  What still has to be proved in Lean is the real-valued nested DCT packaging and the explicit domination of the successive integrated slices.

## Boundary discipline

The boundary sets `x1=0`, `x3=0`, and degenerate slice endpoints are measure zero.  Do not require pointwise positivity there; use the existing interval-integrability/congruence machinery.  Do not replace the singular integrand by a falsely bounded function at the boundary.

## Source-mining correction

The old GDrive `loop_measure_derivation.pdf` should not be used to identify generic off-shell `d^4 ell` with a null celestial `(omega,z,zbar)` measure: `ell=omega q(z,zbar)` with `q^2=0` parametrizes only the null cone, and one complex celestial coordinate parametrizes `S^2`, not the full angular data of generic Euclidean/Riemannian four-momentum.  Its Mellin/Gamma reflection identities remain useful on on-shell cuts.  The current cut-first program is therefore the correct setting for the celestial measure bridge.
