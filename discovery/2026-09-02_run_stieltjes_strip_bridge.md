# Codex/GPT research checkpoint — 2026-09-02

## Scalar-box regulator closure

GPPVerify2 `codex/lean-workbench` Build #1942 and fast gate #797 both passed on
`06ae4dbaeaf609fb6baa9eaa8d7efe24eedff4bf`, certifying the pointwise identity
between the measurable two-dimensional simplex-strip section and the original
closed affine interval in `x3`.

The next Verify2 commit, `bb49f4889e939e3f3f185290d4488db5918817ec`,
lifts that pointwise equality to equality of the corresponding whole-line
indicator integrals via `MeasureTheory.integral_congr_ae`.  This is the direct
bridge from product-measure measurability to the nested middle-DCT formulation.
CI was triggered but was not terminal at the time of this record.

The remaining scalar-box formal chain is now:

1. bridge the `Icc` indicator integral to the oriented interval integral under
   `0 <= 1 - x1 - x2`;
2. transfer strong measurability to the middle-coordinate inner integral;
3. apply the certified middle majorant and middle DCT;
4. apply the certified outer majorant and outer DCT;
5. conclude `simplexMoment epsilon S T -> 1/6` as `epsilon -> 0+`;
6. feed this into the already-formalized Gamma residue assembly.

No Yang-Mills numerator claim follows from this scalar closure.  The post-box
physics target remains fixed-loop-momentum, nonzero-mu Yang-Mills tree-current
sewing over three massive-vector polarizations, then generalized cuts and
only afterward gravity/double copy.

## Celestial cut -> dispersion Mellin kernel

Added executable audit `discovery/celestial/stieltjes_mellin_kernel_check.py`
for the universal identity

    integral_0^infty t^(-sigma)/(1+t) dt = pi/sin(pi sigma),
    0 < Re(sigma) < 1.

High-precision checks at complex points in the strip agree with the closed
form.  This is audit evidence only; the promotion target is a Lean theorem with
measurability, integrability, strip hypotheses, and the beta/reflection step
made explicit.

## Principal-series / Weil boundary

No RH promotion.  The currently formalized `Delta = 2s`, critical-line
unitarity, completed response, local Gamma/Wiener-Hopf positivity, and finite
interpolation reduction still do not identify the genuine global Weil
quadratic form with a manifestly positive form.  The critical missing bridge
remains the completed prime + Archimedean explicit-formula test class and its
positivity/interpolation realization.

## Prime-gas thermodynamics

No new theorem promoted in this sub-run.  Preserve the exact curvature identity

    R = (D^2 - det H)/(2 D^2)

and the rigorous Gram consequence `R <= 1/2`.  The earlier conjecture that the
curvature is negative everywhere remains retracted because stable evaluations
show sign changes.

## Spectral / Mehler-Fock / Wiener-Hopf chambers

No retraction.  Preserve the exact Gamma chamber recurrence, positivity, and
threshold `2 lambda^2 = k+1`.  These imply unimodal chamber ordering, but do not
justify a repeated-sech convolution interpretation.  Chamber positivity is not
Weil positivity.

## Separation

No Claude research, branches, notes, or records were inspected.
