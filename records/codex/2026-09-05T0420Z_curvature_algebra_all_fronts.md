# Codex/GPT all-fronts rotation — 2026-09-05 04:20Z

Scope: Codex/GPT research track only. No Claude-owned research material was inspected.

## Verify2 / prime-gas thermodynamic geometry

The previously repaired exact countable Massieu/Fisher metric separation module is cold-certified at Verify2 `1f8be68a49ba450887c350585b2186e7f9108a1a` (changed-Lean #899 and Build #2045 green).

Promoted the exact centered-moment curvature algebra to Lean in
`GppVerify/RiemannHypothesis/NumberGibbsQuadraticCurvatureAlgebra.lean` at
Verify2 `ac1709863f8709460ae06d9229164fc083d59832`.

Definitions:

- `D = m2*m4 - m3^2 - m2^3`;
- `Hdet` is the expanded determinant of the centered degree-3 moment Gram matrix;
- `Cdet` is the expanded determinant of the 3x3 Hessian-curvature numerator.

Lean target now pushed:

`Cdet = Hdet - D^2`.

It also packages

`R = (D^2-Hdet)/(2 D^2) = 1/2 * (1-Hdet/D^2)` for `D != 0`,

and the conditional ceiling `Hdet >= 0 -> R <= 1/2`.

Honesty boundary: this module is the algebraic core only. The semantic bridge still needed for the actual countable Gibbs family is (i) identify m2..m6 with its centered moments / third Massieu derivatives and (ii) prove the degree-3 centered moment Gram determinant nonnegative in that countable setting. No universal claim `R <= 0` is made; discovery numerics show both curvature signs.

At record time both changed-Lean and full Build were running on `ac170986...`; do not call this new module certified until those finish green.

## Celestial box / YM / gravity

Scalar analytic closure remains complete: `J_epsilon(S,T) -> 1/6`.

The exact Badger one-flow subtraction remains

`C_tri,one-flow^[2] = -i (5 u^2 + 3)/(3(1+u^2))`,

with the full published coefficient twice that value in the fixed frame. The pre-sewing noninjectivity audit remains decisive: the collapsed two-particle Laurent sewing cannot recover factorwise extra-propagator residues. Thus the next honest amplitude calculation is still the generic nonzero-mu triple-cut lift before sewing, retaining each uncut denominator separately and applying the existing root-sum / T1,T2,T3 moment machinery. No FDH numerator, D-dimensional gravity double copy, or higher-loop claim is promoted before that map exists.

## Principal series / completed zeta / Weil

The exact positive-real half-density dictionary remains: dilation modulus one iff `Re(s)=1/2`; inversion sends `s -> 1-s`; with `Delta=2s`, this is the celestial shadow `Delta -> 2-Delta` and the unitary line `Re(Delta)=1`.

No RH promotion. The global missing theorem is still unconditional positivity of the genuine completed prime-plus-Archimedean Weil/heat Gram form on a sufficiently rich admissible class, together with the explicit-formula and closure bridge.

## Spectral / Mehler-Fock / Wiener-Hopf / chamber

The exact symbolic logistic substitution audit remains clean:

`u=q/(1+q)`, `q=e^y`, `du/dy=q/(1+q)^2=1/(4 cosh(y/2)^2)`.

Combined with the already-formal Beta/Gamma bridge, the target is

`rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2`,
`Fourier(rho_c)(t)=sech(t/2)^(2c)`,
then `rho_c * rho_d = rho_(c+d)`.

The remaining formal blocker is measure-theoretic transport from `(0,1)` to `R` under the logistic map, then Fourier uniqueness. No Barnes or unsupported Plancherel axiom is introduced.

## Next rotation

1. Terminal Verify2 CI on `ac170986...`; repair immediately if cold CI exposes a source-only defect.
2. If green, bridge the abstract centered Gram determinant to the actual countable number-Gibbs moments and obtain the genuine `R <= 1/2` theorem.
3. Amplitudes: implement pre-sewing nonzero-mu triple-cut residue lift.
4. Spectral: formalize logistic measure transport, not more Gamma algebra.
5. RH: continue only on the global completed prime-Archimedean positivity bridge; local positive factors remain insufficient.
