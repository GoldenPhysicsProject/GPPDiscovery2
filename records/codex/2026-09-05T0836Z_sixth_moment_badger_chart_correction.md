# Codex/GPT research rotation — 2026-09-05 08:36Z

## Prime-gas curvature

Verify2 commit `a333bcd79cc3d8403a962fa013bd9bec87ac61bb` adds `NumberGibbsQuadraticCurvatureSummability.lean`.

The file extends the one-parameter zeta-Gibbs logarithmic summability interface to orders five and six by iterating Mathlib `LSeries.logMul`, proving abscissa of absolute convergence at most one for `(log n)^5` and `(log n)^6`, then transfers these moments through the already-certified quadratic confinement theorem.  The new endpoint is summability of

`numberGibbsWeight beta eta n * numberLogEnergy n^r`

for `r=5,6`, arbitrary real `beta`, and `eta>0`.

This removes the analytic tail obstruction to realizing the cubic residual square used in the certified curvature algebra.  The semantic curvature bridge still needs the actual centered-moment expansion of the normalized countable weighted-square expectation.  CI Build #2049 and cold changed-Lean #903 are currently running; no certification claim is made before they complete.

## Yang-Mills / generalized cuts — correction to the previous next-step

The existing Badger `s23` implementation was re-inspected before applying its `T1,T2,T3` moments to the new generic pre-sewing root data.  Its coordinate roles are not the same as the generic meridian calculation:

- Badger's two-particle cut is a genuine two-parameter chart `l1(y,t)`.
- The third cut imposes the quadratic `P(y)=0`, leaving `t` as the surviving parameter.
- The branch-free `y_+/-` root sum is taken first.
- Only the large-`t` polynomial is then mapped by `T1,T2,T3`.

By contrast, the current generic massive-vector state sum uses only the rational meridian of the cut sphere,

`n(t)=(2t/(1+t^2),0,(1-t^2)/(1+t^2))`.

The previously certified `t=+/- i r` poles are therefore valid extra-propagator roots on that meridian, but they are not themselves the Badger root variable plus a surviving moment variable.  Directly applying `T1,T2,T3` to the meridian coefficients would be unjustified.

Discovery2 now contains `generic_badger_chart_dimension_audit.py`.  It proves exactly that the meridian is the `v=0` restriction of the full rational sphere chart

`n(u,v)=(2u,2v,1-u^2-v^2)/(1+u^2+v^2)`,

whose two tangent vectors satisfy

`|d_u n x d_v n|^2 = 16/(1+u^2+v^2)^4`,

so the full chart has rank two at every finite point.  It also proves that the Badger double-cut tangents `partial_y l1` and `partial_t l1` have a constant nonzero 2x2 minor `-1`.

Therefore the honest next amplitude step is stronger than previously stated: restore the second cut-sphere/spinor coordinate in the generic vector-minus-scalar tree state sum, impose the third cut in that full chart, retain the surviving one-parameter triple-cut family, and derive/apply the large-coordinate moment map there.  The earlier factorwise residues and Laurent identities remain valid on the meridian slice, but are insufficient by themselves for a normalized master coefficient.

The chart-dimension audit is gated into the generic Ds4 workflow at Discovery2 `ac3e67ba7d4f8fa8df4a6f5215e6e51983d6c415`; CI #18 is running.

Scalar cut -> dispersion -> raised-box regulator remains closed with `J_epsilon(S,T) -> 1/6`.

## Principal series / completed zeta / Weil

No theorem boundary changed.  Positive-real half-density unitarity on `Re(s)=1/2`, `Delta=2s`, shadow `s -> 1-s`, completed-zeta response, and local Gamma/Wiener-Hopf positivity remain exact structural statements.  The missing global theorem remains unconditional positivity / complete monotonicity of the genuine completed prime-plus-Archimedean explicit-formula heat object on the required function class.  No RH promotion is made.

## Spectral / chamber formalization

Mathlib source inspection found `integral_comp_mul_deriv_Ioi` in `MeasureTheory/Integral/IntegralEqImproper.lean`.  This gives a concrete Lean route for the logistic Fourier bridge without first building a custom pushforward-measure equivalence: formalize the real-line-to-positive-ray exponential substitution and the positive-ray-to-unit-interval Mobius/logistic substitution as controlled improper-integral changes of variables, then invoke the existing Beta/Gamma bridge and Fourier uniqueness.

The target remains

`rhohat_c(t)=sech(t/2)^(2c)` and `rho_c * rho_d = rho_{c+d}`.

## Separation rule

No Claude-owned branch, record, note, file, or context was inspected.  Discovery2 is used only for executable discovery; Verify2 remains the formal theorem source; no local or conditional positivity statement is promoted to the missing global arithmetic theorem.
