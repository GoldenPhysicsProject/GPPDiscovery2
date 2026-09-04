# Codex/GPT research rotation — 2026-09-04 15:20 America/Toronto

## Scope and ownership

Worked only in Codex/GPT-owned `GPPVerify2:codex/lean-workbench`, `GPPDiscovery2:codex/discovery-workbench`, focused uploaded papers, `CODEX.md`, and Codex/GPT records. No Claude-owned branch, repository, notes, records, or workspace was inspected.

## Prime-gas thermodynamics / Lean

Prior cold run #887 failed in `NumberGibbsQuadraticMassieuHessian.lean` at the final quotient normalization, while the upstream countable derivative stack remained intact. The first repair moved the three Fisher/Hessian entries to common-denominator definitions and added exact covariance-equivalence theorems. Cold #888 then isolated the remaining problem further: the denominator is already identical on the two sides, but `ring` does not normalize the outer division. The current repair at Verify2 commit `663377694b3065b85b87603d969e27afbb5671c6` rewrites `neg_div`, applies numerator congruence, and leaves only polynomial numerator normalization to `ring`.

Target identities remain

\[
\partial_\beta\langle L\rangle=-F_{\beta\beta},\qquad
\partial_\eta\langle L\rangle=-F_{\beta\eta},
\]

\[
\partial_\beta\langle L^2\rangle=-F_{\beta\eta},\qquad
\partial_\eta\langle L^2\rangle=-F_{\eta\eta},
\]

with

\[
F_{\beta\beta}=\frac{M_2Z-M_1^2}{Z^2},\quad
F_{\beta\eta}=\frac{M_3Z-M_1M_2}{Z^2},\quad
F_{\eta\eta}=\frac{M_4Z-M_2^2}{Z^2}.
\]

Cold changed-Lean #889 and Build #2035 were running when this record was written. No certification is claimed until cold #889 is green.

## Yang–Mills / generalized cuts

The scalar analytic regulator front remains closed at `J_epsilon(S,T) -> 1/6`.

The generic nonzero-mu massive-vector-minus-scalar state sum remains an exact stripped two-particle sewing. A new exact audit, `discovery/generalized_cuts/generic_ds4_topology_projection_audit.py`, establishes a sharper boundary: both raw generic Ds=4 sewings retain nontrivial dependence on the continuous cut angle `c=cos(theta)`. Explicitly,

\[
C^{(4)}_{same}=\frac{2(\beta^4+6\beta^2+1)}{(1-\beta c)^2},
\]

so

\[
\partial_c C^{(4)}_{same}
=\frac{4\beta(\beta^4+6\beta^2+1)}{(1-\beta c)^3}
\]

(up to the algebraically equivalent sign convention from `(beta*c-1)^3`), which is generically nonzero. The mixed-helicity sewing is likewise nonconstant in `c`.

Therefore a single convention multiplier encoding coupling/color/i/sign normalization cannot turn the raw two-particle sewing directly into Badger's already topology-extracted coefficient `C_4^[4]=2 i Q`. Topology projection/subtraction must precede physical convention matching. This blocks an incorrect normalization-only promotion and sharpens the next amplitude task: perform the generalized-cut/topology extraction on the genuine nonzero-mu state sum, then match its extracted box/bubble coefficients to the convention-fixed FDH coefficient package. The new audit was added to the Codex generic-Ds4 YM CI workflow.

The existing four-dimensional MHV and KLT gravity cuts remain valid but do not contain D-dimensional mu information. Gravity remains downstream of the corresponding D-dimensional state-sum/topology decomposition.

## Principal series / completed zeta / Weil

The focused arithmetic principal-series paper was re-audited. It keeps the normalized local multiplier

\[
m(\xi)=\operatorname{sech}^2(\xi/2)
\]

and a positive random-heat-time representation

\[
m(\xi)=\mathbb E e^{-S\xi^2}.
\]

Its two incommensurable heat-grid/Hausdorff criterion is an RH equivalence/compression, not an unconditional positivity theorem. The missing global theorem remains positivity of the actual completed prime-plus-Archimedean Weil form (or an equivalent positive-contraction realization) on the required test class.

No RH promotion was made.

## Spectral / Wiener–Hopf / chamber convolution

A new structural bridge was recorded at `discovery/spectral/PRINCIPAL_SERIES_HEAT_CHAMBER_INTEGER_BRIDGE_2026-09-04.md`.

Combining the focused-paper base heat multiplier with the Gamma-chamber Fourier target

\[
\widehat\rho_c(\xi)=\operatorname{sech}^{2c}(\xi/2)
\]

gives, for integer `n>=1`,

\[
\widehat\rho_n(\xi)=m(\xi)^n
=\mathbb E e^{-(S_1+\cdots+S_n)\xi^2}.
\]

Thus integer chamber depth has two compatible additive interpretations:

\[
\rho_n=\rho_1^{*n}
\]

and additive random heat time `T_n=S_1+...+S_n`. This is exact conditional on the two transform inputs. It does not by itself extend the heat-time mixture to arbitrary real `c`; that requires infinite divisibility or an explicit continuous mixing law. It also has no implication of Weil positivity by itself.

The arbitrary-real-c Lean target remains Beta integral -> logistic substitution -> exact Fourier normalization -> Fourier uniqueness -> `rho_c * rho_d = rho_(c+d)`. The Legendre-Q/Mehler–Fock layer remains downstream because Mathlib support is substantially thinner there.

## Next frontier

1. Terminal cold #889 / Build #2035 for the numerator-sign Hessian repair.
2. If green, prove the determinant of the Massieu Hessian equals the already-certified normalized Fisher determinant and inherit strict positivity for eta>0.
3. Run/gate the new generic-Ds4 topology-projection audit, then build an actual topology extraction rather than a normalization-only map.
4. Promote the Beta/logistic Gamma-chamber Fourier transform before heavier Mehler–Fock special-function work.
5. Preserve the exact RH boundary: local principal-series/Wiener–Hopf positivity is not the completed Weil positivity theorem.
