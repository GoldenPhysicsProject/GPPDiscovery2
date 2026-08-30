# Codex/GPT continuation — exact physical-chart CI repair

Date: 2026-08-30
Track: Codex/GPT only

## CI diagnosis correction

The previous record said that the terminal finite-core failure on `GPPVerify2:codex/lean-workbench` could not yet be localized because the compiler diagnostic was unavailable. That is now superseded.

The deterministic failing target was `GppVerify/CelestialHolography/MassiveVectorPhysicalChartClosure.lean`, specifically the proof of

`physicalDenominator_eq_zero_iff (r t : ℝ) : 1 - betaCoord r * cosThetaCoord t = 0 ↔ r = 0 ∧ t = 0`.

The physical-coordinate identity is

  1 - beta(r) cos(theta(t))
    = 2 (r^2 + t^2) / ((1+r^2)(1+t^2)).

For real `r,t`, both denominator factors are strictly positive and therefore nonzero. Hence the fraction vanishes iff `r^2+t^2=0`, which by nonnegativity of squares is equivalent to `r=t=0`.

The old Lean proof rewrote through `div_eq_zero_iff`; the elaboration path was brittle against the actual theorem shape in the pinned Mathlib/Lean environment. The replacement proof does not alter the theorem. It proves denominator nonvanishing explicitly, multiplies the equality by the denominator, simplifies to `r^2+t^2=0`, and finishes with square nonnegativity.

The repair was pushed to `GPPVerify2:codex/lean-workbench` as commit

`cd85c5ef0017a40e335463c56ee1b1e51f0a1485` — `Fix physical chart denominator zero locus proof`.

Fresh CI is running on that exact head. Do not advance `main` or call this certified until the targeted massive-vector chart lane and the integrated construction checks pass.

## Cross-front state after repair

### Scalar box

The raised-box regulator limit remains mathematically closed:

  J_eps(S,T) -> 1/6

for positive Euclidean `S,T` as `eps -> 0+`, using interior pointwise convergence and the integrable fixed-delta majorant whose singular channel integrates to

  B(1-delta,3-delta) B(1-delta,2)
  = Gamma(1-delta)^2 / Gamma(4-2delta),

for `0<delta<1`.

The remaining gap is Lean packaging of the null simplex boundary, AE convergence, and the nested/filter dominated-convergence theorem for the concrete simplex moment.

### Prime-gas Fisher geometry

The full countable centered quadratic form is already strictly positive for every nonzero coefficient pair. The normalized covariance determinant module currently packages only nonnegativity. The shortest strict endpoint is still the justified `tsum` coefficient identity

  E[(a X_c + b Y_c)^2] = A a^2 + 2 B a b + C b^2,

followed by the existing abstract strict-quadratic determinant theorem, yielding `A*C-B^2>0`. Moment summability through degree four is already available.

### Principal series / Weil

Positive-real half-density, `Delta=2s`, critical-line unitarity, completed-zeta response, explicit-formula/heat anomaly, and local Wiener-Hopf structure remain exact. They do not yet supply the unresolved global relative prime-plus-Archimedean trace/Gram identification and non-circular positivity/contractivity theorem. No RH claim is made.

### Spectral / Mehler-Fock / chamber hierarchy

The all-real extended Wiener-Hopf/Gamma weight and strict Gamma-chamber positivity remain exact. The Gamma weight is not the scalar `SL(2,C)` Plancherel density. Exact Mehler-Fock/Macdonald resummation to the scalar-box dilogarithmic answer remains open.

### Yang-Mills / gravity

This repair certifies the intended physical-coordinate zero locus and, once CI passes, restores the strict generic mixed-helicity physical-chart baseline away from the degenerate point `(r,t)=(0,0)`. This is still rational/state-sum infrastructure, not the honest fixed-loop-momentum nonzero-mu Yang-Mills tree sewing. The next physics frontier remains explicit massive-vector polarization sewing, then generalized/higher-loop cuts and gravity numerators.
