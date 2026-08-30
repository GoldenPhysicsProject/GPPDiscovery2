# Run 14: strict zeta cumulant bridge and raised-box Fubini frontier

## Prime-gas / zeta Gibbs

On `GPPVerify2` `codex/lean-workbench` the analytic moment layer was extended through order four at commit `3c59c57d37c976e4112731d2f63251ce0e1590cf`.  For every real `beta > 1` the weighted series

- `(n+1)^(-beta) log(n+1)^3`,
- `(n+1)^(-beta) log(n+1)^4`

are formally summable, using the constant-one L-series abscissa and repeated `LSeries.logMul`.

The strict centered two-observable Gibbs geometry is now expressed on the actual zeta Gibbs support.  `ZetaGibbsTwoObservableStrict.lean` proves, for every nonzero `(a,b)`, strict positivity of the normalized mean square of

`a (X-E X) + b (X^2-E X^2)`

with `X=log(n+1)`.  Strictness is already witnessed by the three support states `n=0,1,2` with distinct energies `0, log 2, log 3`.  The resulting centered covariance determinant is strictly positive.  An earlier incomplete raw-moment summary theorem containing a `sorry` was removed rather than retained.

At commit `2fdd8843d9737a56db07a2544a3f0cfa98d758eb`, `ZetaGibbsCenteredMomentBridge.lean` was added to identify the centered covariance entries with the existing raw-moment/cumulant hierarchy.  If CI certifies the file, the final theorem is the strict honest-half-line inequality

`kappa_2 kappa_4 + 2 kappa_2^3 - kappa_3^2 > 0` for `beta > 1`.

This is a thermodynamic/Fisher statement on the absolutely convergent zeta Gibbs half-line only.  It is not analytic continuation and not RH.

CI state at recording time: axiom/scaffold audit green; ordinary Build, full construction, finite-core and Gibbs differential lanes still running/queued.  Do not promote the new cumulant bridge as Lean-certified until terminal CI passes.

## Spectral / Mehler-Fock

The current `MehlerFockGammaCollapsedWeight.lean` has an all-real half-shift Gamma identity and collapsed Wiener-Hopf/Mehler-Fock weight with no puncture/stub.  The ordinary library Build for repair commit `d809a5f5527a9b166f6cce494880cc3eb29a2889` passed.  This remains a spectral-weight identity, not a scalar `SL(2,C)` Plancherel-density identification.

## Raised-box regulator

The raised-box epsilon regulator is still distinct from the already-formalized physical small-m scalar-box convergence wrapper.  `RaisedBoxResidueAssembly.lean` remains conditional on

`simplexMoment S T -> 1/6` as `epsilon -> 0+`.

The exact remaining formal gap is now localized more sharply.  Pointwise convergence of the physical Symanzik kernel is proved, and the one-channel bound

`Q^(-epsilon) <= 1 + (S x1 x3)^(-delta)`

is proved for `0 < delta < 1`, `0 <= epsilon <= delta`.  The Beta layer proves convergent complex-valued inner slices and the reduced outer Beta kernel.  What is still missing is the concrete real-valued Fubini/Tonelli bridge showing that the nested simplex majorant used by `simplexMoment` is integrable and reducing it to those certified Beta slices.  Once that bridge is available, nested/filter dominated convergence can be applied and the residue assembly becomes unconditional.

No scalar-box regulator Lean closure is claimed yet.

## Other frontiers unchanged

The Weil front still lacks identification of the actual prime-plus-Archimedean relative trace/Gram object with the full Weil quadratic form and its positivity.  The scalar transfer-response model alone is insufficient.

The YM/gravity front still requires explicit fixed-loop-momentum nonzero-mu Yang-Mills tree currents/numerators and physical massive-vector polarization sewing before any actual generalized-cut or double-copy claim.
