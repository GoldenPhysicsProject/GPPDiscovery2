# Codex/GPT rotation — full-chart YM tree residue repair and Gibbs curvature CI

Date: 2026-09-05
Track: Codex/GPT only. No Claude-owned work inspected.

## Verify2 / quadratic number-gas geometry

Verify2 head `74c49bd0dced30a17e257fdea17f86acf94d4131` is now fully green:

- cold changed-Lean #904: PASS
- full Build #2050: PASS

This certifies the normalized countable Gibbs weighted-square positivity layer, including the cubic residual observable used by the curvature program. Fifth/sixth log-moment summability was already green on the preceding layer. The remaining semantic theorem is the exact identity between the actual normalized `tsum` residual-square expectation and `residualSqMoment m2 ... m6` for the actual centered Gibbs moments. Combined with the already-certified algebra `residualSqMoment = D * det H`, `D > 0`, and the curvature normal form, this is the remaining bridge to the genuine Gibbs theorem `R <= 1/2`.

## Discovery2 / generic nonzero-mu Yang-Mills cut

Added `generic_full_chart_vector_scalar_tree_audit.py` and gated it in the generic Ds=4 CI. The full stereographic helicity frame is chosen to reduce exactly at `v=0` to the existing certified meridian tree engine:

- leg 2: `(e_u + i h e_v)/sqrt(2)`
- leg 3: `(-e_u + i h e_v)/sqrt(2)`

with the existing mostly-minus amplitude convention.

The first CI attempt (#23, head `e7f2878b209cd868cd0ea259025c143dda6e0970`) failed only in the new full-chart tree step. The defect was conceptual and localized: the script evaluated the raw tree after imposing the third propagator `q = r^2 + u^2 + v^2 = 0`. The raw tree is supposed to have a pole there, so this is not a finite datum.

Repaired at `87a860a9464c8e445557f95ddb446705bc0cf36c`: first form the transverse residue `q A`, then restrict to the conic. At the distinguished point `z=0`, equivalently `(u,v)=(i r,0)`, the full transverse residue is checked against the old meridian coordinate residue through

`[q A]_(q=0,z=0) = 2 i r Res_(t=i r) A`,

because on the meridian `q=(t-ir)(t+ir)`.

Generic Ds=4 CI #24 is running on this repaired head at record time. Earlier topology, propagator ancestry, noninjectivity, meridian residue, Laurent-factorization, chart-dimension, and full two-coordinate triple-cut geometry layers remain independently green; no master coefficient is claimed yet.

## Scalar box / principal series / spectral chamber boundaries

- Scalar cut -> dispersion -> raised-box regulator closure remains unchanged: `J_epsilon(S,T) -> 1/6`.
- No RH promotion. Critical-line half-density unitarity, `Delta=2s`, shadow/reflection structure, and local Gamma/Wiener-Hopf positivity remain structural inputs; the unresolved theorem is still unconditional global prime-plus-Archimedean explicit-formula/Weil positivity/complete monotonicity on the correct test class.
- The continuous Gamma-chamber record remains discovery-level: `rho_c` has the target transform `sech^(2c)(t/2)` and target semigroup `rho_c * rho_d = rho_(c+d)`. Lean promotion still requires a rigorous arbitrary-positive-c Fourier-Gamma/logistic transport and Fourier uniqueness; no Barnes identity is to be treated as a formal axiom.

## Next executable frontier

1. Terminal CI #24 and repair immediately if needed.
2. Once residue-level full-chart lift is green, compute the full vector-minus-extra-scalar transverse residue/state sum as an exact rational function of the surviving conic parameter `z`, then extract the legitimate large-`z` data for the Badger projector.
3. In Verify2, prove the `tsum` centered-moment expansion identifying the countable residual-square expectation with `residualSqMoment`; this should close `R <= 1/2` for the actual quadratic Gibbs model.
4. Spectral formalization remains logistic measure transport/Fourier uniqueness; RH remains at the global completed Weil-positivity boundary.
