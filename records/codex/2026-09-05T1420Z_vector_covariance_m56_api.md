# Codex/GPT all-fronts rotation — 2026-09-05 14:20Z

## Scope
Codex/GPT track only. No Claude-owned work was inspected.

## Yang–Mills generalized-cut front

Pushed `discovery/generalized_cuts/generic_full_chart_vector_covariance_audit.py` and gated it in `.github/workflows/codex-generic-ym-baseline.yml`.

Target exact covariance on the genuine one-complex-dimensional triple-cut conic:

- `u^2 + v^2 = -r^2`
- `u(z)=i r (1-z^2)/(1+z^2)`
- `v(z)=2 i r z/(1+z^2)`
- `Q(z)=[[c,-s,0],[s,c,0],[0,0,1]]`, `c=(1-z^2)/(1+z^2)`, `s=2z/(1+z^2)`.

For helicities `(h2,h3)`, with already-certified external little-group phase `p=p2*h p3`, the audit checks directly from the transverse residue `q A|_{q=0}`:

`R_V(z) = p(z) Q(z) R_V(0) Q(z)^T`.

After normalization by the scalar residue this becomes similarity covariance

`R_V(z)/S(z) = Q(z) [R_V(0)/S(0)] Q(z)^(-1)`.

Consequences checked by the script if the matrix identity completes:

- same-helicity characteristic polynomial `(λ+1)(λ+r^2)(λ r^2+1)/r^2`;
- mixed-helicity characteristic polynomial `(λ-1)^2(λ+1)`;
- `det R_V(z) = -S(z)^3` on the full conic.

At record time generic Ds=4 CI #26 has every prior audit green and is still executing the new exact matrix-covariance step. Therefore the full-conic similarity law and z-independent spectra are NOT yet promoted as certified results in this record.

## Quadratic number-Gibbs thermodynamics

Verify2 `codex/lean-workbench` now extends `NumberGibbsQuadraticThermodynamics.lean` with raw moments

`M5 = tsum (w L^5)`, `M6 = tsum (w L^6)`

and explicit summability theorems imported from the already-certified sixth-order confinement layer.

Exact Verify2 head at record time: `1fd5058b5163ae00bf8ddde21b426355826e2f8c` (`Extend quadratic Gibbs raw moments through order six`). Cold changed-Lean #905 and full Build #2051 are running; this M5/M6 API extension is therefore not yet called cold-certified here.

Once green, the remaining curvature closure is the sixth-order countable `tsum` expansion identifying the normalized Gibbs expectation of the denominator-cleared cubic residual with the already-certified algebraic `residualSqMoment(m2,...,m6)`. Positivity plus `D>0` then gives the actual quadratic-number-Gibbs scalar-curvature ceiling `R <= 1/2`.

## Scalar cut / regulator

No regression. The scalar celestial cut -> dispersion -> raised-box regulator endpoint remains closed at `J_epsilon(S,T) -> 1/6`.

## Principal-series / arithmetic boundary

No RH promotion. Positive-real half-density/principal-series unitarity, `Delta=2s`, shadow `s <-> 1-s`, completed-zeta response and local Gamma/Wiener-Hopf positivity remain exact structural layers. The unresolved theorem is still unconditional positivity/complete monotonicity of the genuinely completed prime-plus-Archimedean explicit-formula/Weil object on the correct test class.

## Spectral / Mehler–Fock / chamber boundary

No retraction. The continuous target remains `rho_c^(hat)(t)=sech^(2c)(t/2)` and `rho_c * rho_d = rho_{c+d}`. Existing integer chamber/Wiener-Hopf structures remain usable. The formal arbitrary-c blocker is still the rigorous logistic/logit change-of-variables on the real-line integral followed by Fourier uniqueness; no Barnes or unsupported Plancherel axiom is introduced.

## Next frontier

1. Terminal CI #26 and either promote or repair the exact vector-residue covariance law.
2. Terminal Verify2 #905/#2051; then implement the sixth-order centered-moment `tsum` expansion and close `R <= 1/2`.
3. With full-conic vector covariance in hand, construct the actual opposite-tree contraction / Ds=4 vector-minus-extra-scalar state sum and perform the legitimate surviving-coordinate large-z Badger projection before claiming master coefficients.
