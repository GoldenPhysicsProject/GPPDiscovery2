# Codex/GPT research run — 2026-09-01

## Number thermodynamics

Verify2 head `eb942518f8154d17782d1e4b236b69c1c047fb98` passed changed-Lean smoke. Its theorem `numberGibbs_fisherNumerator_infinite_pos` specializes the fixed three-state countable Fisher witness to

\[
w_{\beta,\eta}(n)=\exp[-\beta\log(n+1)-\eta\log^2(n+1)],\qquad x_n=\log(n+1),
\]

with raw-moment summability through order four as the only analytic hypothesis.

New Verify2 commit `10255ca96c497fecc8c5f5b5cad5a8ee83992b8c` adds `NumberGibbsTwoParameterZetaWedge.lean`. It formalizes the comparison route

\[
0\le \eta \implies
w_{\beta,\eta}(n)\le e^{-\beta\log(n+1)}=(n+1)^{-\beta},
\]

and uses the already-certified zeta-Gibbs log-moment summability theorems to target an unconditional strict infinite Fisher numerator for `β > 1`, `η ≥ 0`. Changed-Lean CI is running; do not promote this result until green.

The stronger frontier remains the genuinely quadratic regime: for every real `β` and `η>0`, prove all fixed log moments summable by eventual comparison with `(n+1)^(-2)`. The discovery inequality is: for fixed `r`, set `A=|β|+r+2`; once `log(n+1) ≥ max(1,A/η)`,

\[
(\log(n+1))^r e^{-\beta\log(n+1)-\eta\log^2(n+1)}\le (n+1)^{-2}.
\]

## Scalar box / celestial amplitudes

Audit confirms there is no missing Beta/Gamma estimate. `RaisedBoxSimplexNestedReduction` already proves the nested singular majorant equals the reduced Beta product and states that the remaining regulator theorem is DCT for the original raised-box integrand. `RaisedBoxSimplexZeroRegulator` already proves the exact endpoint value `1/6`. `RaisedBoxPointwiseLimit` supplies pointwise convergence on the strict simplex interior.

Therefore the honest remaining scalar theorem is exactly:

1. package the simplex boundary faces as a measure-zero exceptional set;
2. obtain AE pointwise convergence of the original integrand to `1`;
3. use the existing fixed integrable majorant and nested interval parameterization in dominated convergence;
4. identify the integral of the limit with simplex volume `1/6`.

Do not add more surrogate endpoint or Gamma lemmas unless DCT exposes a genuinely missing measure lemma.

## Spectral salvage audit

`SpectralRhoMehlerFockBridge` already gives the all-order explicit chamber density, including the removable origin value. `SpectralRhoPositivity` already proves every normalized Gamma/Mehler–Fock chamber weight is real and strictly positive for every real spectral parameter. These are stronger exact salvage results than an away-from-zero formula alone; retain them as certified Archimedean infrastructure. No new global Weil positivity consequence follows from this audit.

## Integrity

No Claude branch, record, prompt, or artifact was inspected. No global RH/Weil claim and no YM/gravity numerator claim was promoted in this run.
