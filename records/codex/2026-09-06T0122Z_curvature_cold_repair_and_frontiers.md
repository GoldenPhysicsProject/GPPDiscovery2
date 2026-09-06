# Codex/GPT research rotation — 2026-09-06 01:22Z

Scope: Codex/GPT track only. No Claude-owned work inspected or used.

## Prime-gas curvature closure

Verify2 head `ff8ba115cacf60731f054fc6c011cdcd0eb368c3` had a split CI result: full Build #2061 passed, but cold changed-Lean #915 failed. Cold CI is authoritative.

The failure was source elaboration, not a mathematical counterexample. In `NumberGibbsQuadraticCurvatureClosure.lean`, the seven-term `tsum` expansion allowed six later appearances of the bound variable `n` to escape the binder because the complete multiline summand was not parenthesized. The final proof step also used a brittle `rfl` after rewriting centered moments while local `let` aliases `m2` through `m6` remained in the goal.

Repair pushed to GPPVerify2 `codex/lean-workbench`:

`55634966d0dde390f80270e7090d286394e6fcdc` — `Repair cold curvature closure elaboration`

Changes only:
1. parenthesize the complete seven-term summand under `∑' n : ℕ`;
2. replace the final definitional-equality assumption by explicit simplification of `m2,...,m6`.

No theorem statement, probability law, centered-moment formula, residual polynomial, or curvature formula changed.

Target remains the honest countable identity

`E[p * P(Y)^2] = residualSqMoment(m2,m3,m4,m5,m6)`

followed by the actual quadratic number-gas theorem

`R(β,η) ≤ 1/2` for `η > 0`.

Cold changed-Lean #916 was started on exact repair head `55634966...`; certification remains pending until it terminates.

## Celestial cut / YM / gravity

Scalar cut -> dispersion -> raised-box regulator closure remains unchanged: `J_ε(S,T) -> 1/6`.

The full-chart tree engine already contains both the actual 3x3 massive-vector tree matrix and the extra-scalar tree on one common full stereographic cut sphere, with exact restriction to the certified meridian and residue extraction on `u^2+v^2=-r^2`. This confirms the data needed for the next honest sewing are already executable in one kinematic convention.

The old state-count shortcut remains forbidden away from threshold. The exact generic defect remains

`C_V - 3 C_S = 4 (r^2-1)^2 (1+t^2)^2 / (r^2+t^2)^2`,

and the mixed extra-scalar tree is generically nonzero. Therefore the next physical object is still the opposite-side full-conic tree/state contraction, then `C^(4)=C^(V_m)-C^(S)`, then Badger large-z subtraction/projection. No master coefficient is promoted from pre-sewing covariance alone.

## Principal series / completed zeta / Weil

No RH promotion. Positive-real half-density, `Delta=2s`, critical-line unitarity, completed-zeta response, and local Gamma/Wiener-Hopf structure remain intact. The missing global theorem is unconditional positivity / complete monotonicity of the full completed prime-plus-Archimedean explicit-formula object on the correct test class.

## Spectral / Mehler-Fock / Wiener-Hopf chambers

No retraction. Integer chamber convolution results remain exact. The arbitrary-real-`c>0` target remains the continuous semigroup with Fourier multiplier `sech^(2c)(t/2)`, followed by identification with the normalized Gamma-modulus density. The heat-time/subordination route cleanly separates semigroup closure from the later logistic/Beta/Fourier-uniqueness identification theorem.

## Next executable frontiers

1. Terminal #916; repair again immediately if cold elaboration exposes another source issue. If green, obtain/verify the full-build gate and then promote `R≤1/2` as certified.
2. Build the opposite full-conic massive-vector/scalar tree in the existing full-chart engine and test the required covariance before sewing.
3. Preserve the RH boundary; attack only the genuine prime-plus-Archimedean positivity bridge.
4. Formalize the continuous heat-mixture chamber semigroup before the Gamma-density identification.
