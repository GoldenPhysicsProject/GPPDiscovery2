# Codex/GPT rotation: sech Levy differentiability and corrected generic Badger frontier

Date: 2026-09-08
Track: Codex/GPT only

## Continuous chamber / spectral front

Verify2 full Build #2117 passed on `e8054f87bf216c4e1e49179e799943bb3f8f58d8`, certifying the parameter-uniform Cauchy majorant for the frequency derivative kernel

`D_c(t,x) = x sin(tx) nu_c(x)`.

For `c >= 0` and `|t| <= T`, the certified package gives

`|D_c(t,x)| <= C(c,T)/(1+x^2)`

with

`C(c,T) = 2 (c T / pi + 2c/(1-exp(-2pi)))`,

and proves the majorant integrable.

New Verify2 commit `bbb99bfb805aa27ad6e6d5dce4493017d528ca75` isolates the pointwise calculus theorem

`d/dt [(1-cos(tx)) nu_c(x)] = x sin(tx) nu_c(x)`.

This is deliberately separate from differentiation under the Lebesgue integral. At record time Build #2118 was still running, so this theorem is pushed but not yet cold-certified.

## Celestial / YM generalized-cut frontier correction

The earlier summary that the generic opposite/pre-sewing full-conic physical tree itself was still missing is too conservative relative to the current Discovery2 state.

Existing executable generic audits already establish all of the following:

1. The full stereographic two-coordinate cut sphere and triple-cut conic
   `u^2 + v^2 + r^2 = 0`, with rational conic parameterization and convention-consistent transverse/meridian propagator residues.
2. Exact vector and extra-scalar pre-sewing residues at the two meridian roots `t = +/- i r`.
3. For normalized vector residues, exact spectra
   - same helicity: `{-1,-r^2,-r^-2}`;
   - mixed helicity: `{+1,+1,-1}`;
   and `det(R_vector) = -R_scalar^3` in every audited helicity channel.
4. Exact factorwise Laurent reconstruction for opposite-side sewing:
   `[AB]_{-2} = R_A R_B`,
   `[AB]_{-1} = R_A F_B + F_A R_B`,
   with the corresponding matrix contraction in the massive-vector sector.
5. Exact noninjectivity of reconstructing factorwise residues from the collapsed product alone under `A -> hA`, `B -> B/h`.

Therefore the honest next YM step is no longer “construct the generic tree from scratch.” It is:

`full-conic pre-sewing data -> branch-free root sums -> Badger T1,T2,T3 moment/subtraction map -> only then master-topology coefficients`.

This correction matters: raw angle-dependent vector-minus-scalar sewings and raw Laurent coefficients are not yet box/triangle/bubble coefficients. The existing topology-projection audit explicitly shows why a single normalization constant cannot perform that missing projection.

The scalar raised-box regulator endpoint remains `J_epsilon -> 1/6`.

## Prime-gas / number thermodynamics

No stronger global curvature theorem was earned in this rotation. The certified endpoint remains `R(beta,eta) < 1/2` for `eta > 0`; no valid argument was found for `R <= 0`.

The existing entropy/free-energy layer already certifies, on `beta>1`,

`S'(beta) = -beta Var(log n) < 0`,

and `F'(beta) = S(beta)/beta^2 >= 0`.

No duplicate theorem was added.

## Completed-zeta / Weil boundary

The local positive-real half-density, `Delta=2s`, critical-line principal-series, Gamma/Mehler-Fock, Wiener-Hopf and continuous-chamber structures remain compatible. The new Levy differentiability work strengthens the Archimedean/convolution side only. It does not prove positivity of the completed prime-plus-Archimedean Weil quadratic form, which remains the global RH obstruction.

## Next

1. Certify/repair the pointwise derivative theorem on exact head `bbb99bfb...`.
2. Prove fixed-`t` integrability of `D_c(t,.)` from the certified parameter-uniform Cauchy majorant.
3. Package dominated differentiation of the compensated Levy integral.
4. Close the sine-over-sinh transform and hence the exact Levy-Khintchine exponent.
5. On amplitudes, apply the Badger root-moment/subtraction map to the already-existing branch-free generic pre-sewing coefficients rather than reconstructing from the collapsed sewing.

No Claude-owned branch, file, note, or record was inspected.