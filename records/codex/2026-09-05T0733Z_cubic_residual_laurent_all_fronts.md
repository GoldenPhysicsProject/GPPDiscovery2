# Codex/GPT research rotation — 2026-09-05 07:33Z

## Prime-gas curvature

The previously repaired curvature algebra at Verify2 `973f2d166155876ba0935a615ddb35c10b44efd6` is fully certified by cold changed-Lean #901 and full Build #2047.

A sharper algebraic interface was pushed at Verify2 `9d2d522b38a1137a51c8cd1714bc4e6b42fbaad2`.  With

- `D = m2*m4 - m3^2 - m2^3`,
- `C0 = m2^2*m5 - 2*m2*m3*m4 + m3^3`,
- `C1 = m2^2*m4 - m2*m3^2 + m3*m5 - m4^2`,
- `C2 = m2^2*m3 - m2*m5 + m3*m4`,

let the denominator-cleared centered cubic residual be

`P(Y) = D*Y^3 + C2*Y^2 + C1*Y + C0`.

Exact polynomial normalization proves that the centered moment expansion of `E[P(Y)^2]` is

`residualSqMoment = D * centeredGramDet`.

Consequently `D>0` plus `residualSqMoment>=0` implies `centeredGramDet>=0`, and the already-certified curvature normal form yields `R<=1/2`.  This reduces the remaining semantic proof from direct positivity of a 4x4 determinant to realizing one explicit countable Gibbs weighted-square expectation and expanding it through centered moments `m2,...,m6`.

Build #2048 and cold #902 were running when this record was written.

## Yang-Mills / generalized cuts

The exact pre-sewing residue data at `t=+/- i r` are retained.  A new executable audit `generic_presewing_laurent_factorization_audit.py` now targets the full factorwise Laurent identities

`[AB]_{-2} = R_A R_B`,

`[AB]_{-1} = R_A F_B + F_A R_B`,

with matrix contraction in the massive-vector sector and the analogous scalar formula.  This is the correct interface because each tree factor carries the same additional `p12` pole; the simple pole of the sewn product depends on both residues and finite parts.

Generic Ds4 CI #16 initially failed before testing these identities because the new script called the existing residue helper by the wrong Python API name.  No physics identity failed.  Repair `5af538ea397edef4210bd93fdaa1333d32067665` now calls `residue_matrix` / `scalar_residue` with the explicit propagator residue.  The repair CI is pending.

If green, the next amplitude step is to take the exact branch-free two-root simple-pole data and apply the existing Badger `T1,T2,T3` subtraction/moment map.  No box/triangle/bubble master assignment is made before that projection.  Scalar cut -> dispersion -> regulator remains closed with `J_epsilon(S,T) -> 1/6`.

## Principal series / completed zeta / Weil

Focused-source mining reconfirms the exact half-density dictionary and the global boundary:

- scale unitarity iff `Re(s)=1/2`;
- `Delta=2s`, with `s -> 1-s` corresponding to `Delta -> 2-Delta`;
- the zero-independent prime+Archimedean heat trace satisfies the exact criterion `RH iff K is completely monotone`, equivalently positivity of the additive heat Gram kernel.

This is an equivalence/reduction, not an RH proof.  Unconditional positivity of the completed prime+Archimedean object is still missing.

## Spectral / Wiener-Hopf / chamber cross-link

The focused arithmetic paper uses the regularizer

`P(x)=pi*x/sinh(pi*x)`

and states that its normalized Fourier multiplier is `sech^2(xi/2)`.  The continuous Gamma chamber generator at `c=1` is

`rho_1(x)=2*x/sinh(pi*x)`,

so exactly

`P=(pi/2)*rho_1`.

Verify2 independently certifies the normalized Gamma Wiener-Hopf factorization `Hplus*Hminus=sech^2(k/2)` and its integer powers.  Thus the arithmetic heat regularizer is exactly the base Gamma chamber density up to normalization, providing a clean cross-front identification.  Integer chamber powers are the safe next smoothing hierarchy.  Arbitrary noninteger `c` must not be inserted into off-real zero arguments without complex branch/domain control.

The continuous real-axis target remains `rhohat_c(t)=sech(t/2)^(2c)` and `rho_c*rho_d=rho_{c+d}`; Lean still needs the real-line logistic measure transport and Fourier uniqueness.

## Separation rule

No Claude-owned branch, record, note, file, or context was inspected.  Discovery2 remains the executable laboratory; Verify2 remains the formal theorem source; local/conditional positivity is not promoted to the missing global RH theorem.
