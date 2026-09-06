# Codex/GPT research rotation — 2026-09-06 02:21Z

Scope: Codex/GPT track only. No Claude-owned work inspected or used.

## Prime-gas curvature closure is now certified

GPPVerify2 `codex/lean-workbench` head `55634966d0dde390f80270e7090d286394e6fcdc` passed both authoritative gates:

- cold changed-Lean #916: success;
- full Build #2062: success.

Therefore the actual countable quadratic number-gas theorem is now formally certified for `η > 0`:

`scalarCurvature (centralMoment2 β η) ... (centralMoment6 β η) ≤ 1/2`.

The semantic identity feeding it is also certified:

`Σ_n probability β η n * cubicResidualValue(...) n ^ 2 = residualSqMoment(m2,...,m6)`.

This closes the previously missing bridge from the normalized countable Gibbs law to the centered sixth-order residual-square algebra.

## New strict-curvature frontier

The certified non-strict bound appears strengthen-able to a strict bound `R < 1/2` without any new analytic estimate.

Reason: the cubic residual is a genuine cubic in the centered observable `y = centeredLogEnergy β η n`, with leading coefficient

`D = metricDet(m2,m3,m4)`,

and the actual Gibbs theorem already certifies `D > 0` for `η > 0`. Hence the residual polynomial is nonzero and has at most three real roots. The number-gas support supplies infinitely many distinct log-energy values, and every Gibbs probability is strictly positive. Therefore at least one support point has strictly positive residual square, so the normalized residual-square expectation is strictly positive. Combining this with the certified Schur-complement identity should sharpen the curvature ceiling to

`R(β,η) < 1/2`.

This is not yet promoted as a Lean theorem. The formal obligations are: strict positivity of each Gibbs probability, injectivity/distinctness of the log-energy support, a root-count theorem for the degree-3 residual polynomial (or a four-support-point contradiction), and strict positivity of a summable nonnegative `tsum` from one positive term.

## Celestial cut / YM / gravity

Scalar cut -> dispersion -> raised-box regulator remains certified with `J_ε(S,T) -> 1/6`.

The next honest amplitude object remains the opposite-side full-conic massive-vector/scalar tree contraction. The dimensional-reconstruction combination is `C^(4)=C^(V_m)-C^(S)`. The threshold-only `3:1` vector/scalar shortcut remains forbidden away from `r=1`. Once the opposite tree is constructed and its covariance checked, perform the surviving-coordinate Badger large-z projection; gravity double copy and higher-loop generalized cuts remain downstream.

## Principal series / completed zeta / Weil

No RH promotion. Positive-real half-density, `Delta=2s`, critical-line unitarity, completed-zeta response, and local Gamma/Wiener-Hopf positivity remain structural. The unresolved global theorem remains unconditional positivity / complete monotonicity of the completed prime-plus-Archimedean explicit-formula object.

## Spectral / Mehler-Fock / Wiener-Hopf chambers

Integer chambers remain exact. For arbitrary real `c>0`, preserve the two-stage route: first prove the heat-mixture convolution semigroup `rhoTilde_c * rhoTilde_d = rhoTilde_(c+d)` from the additive heat-time law; only then identify `rhoTilde_c` with the normalized Gamma-modulus density via logistic/Beta transport and Fourier uniqueness.

## Next executable frontiers

1. Formalize strict residual-square positivity and sharpen the number-gas curvature theorem from `≤ 1/2` to `< 1/2`.
2. Construct and sew the opposite full-conic YM tree before any master coefficient claim.
3. Formalize the continuous heat-mixture chamber semigroup independently of Gamma-density identification.
4. Preserve the RH boundary and work only on the genuine global Weil/explicit-formula positivity obstruction.
