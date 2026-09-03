# Codex/GPT run 11: beta standalone CI, scalar endpoint, spectral and cut audit

Codex/GPT discovery track only. Claude work was not inspected.

## Prime-gas countable differentiation

The previous candidate `hasDerivAt_Z_beta_raw` had a green root Build #2001 but failed changed-module smoke #855, demonstrating that the root target did not exercise the standalone candidate module. The exact #855 issue was an inaccessible `logEnergy_nonneg` identifier in the standalone dependency closure. Replacing that shortcut by a direct `Real.log_nonneg` proof exposed one further normalization issue in smoke #856: after unfolding `numberLogEnergy`, the goal was already `0 ≤ Real.log (↑n + 1)`, so attempting to unfold `logEnergy` again failed. The redundant unfold has been removed at Verify2 commit `d0eb8f938ea51a80fa7730b82c28486bba6fdf27`.

Target theorem remains

\[
\partial_\beta Z(\beta,\eta)
=\sum_{n\ge0}-L_n e^{-\beta L_n-\eta L_n^2},\qquad \eta>0.
\]

No theorem is promoted until the changed-module smoke is terminal green.

## Scalar regulator closure

The existing certified stack now contains: fixed-`x_1` product integrability, Fubini, conversion to the physical nested simplex, the middle DCT, the physical nested norm bound, and an integrable outer majorant. The physical nested function is a.e. strongly measurable on `Ioo 0 1`. The final outer interval DCT differs only by endpoint bookkeeping; pinned Mathlib contains the standard restricted-measure identification `restrict_Ioo_eq_restrict_Ioc`, so the endpoint `x_1=1` can be discarded measure-theoretically rather than by introducing a new singular estimate. The exact scalar target remains

\[
\operatorname{simplexMoment}(\varepsilon,S,T)\to\frac16.
\]

## Focused principal-series / spectral paper audit

The current focused principal-series paper keeps several exact identities separate from RH claims. For `h=(1+i\lambda)/2`, the conical-block normalization has

\[
|c(\lambda)|^2=\frac{2\lambda}{\pi}\coth\!\left(\frac{\pi\lambda}{2}\right),
\]

while shadow exchange is the Mehler-Fock degree reflection `\nu\mapsto-\nu-1`. On the unitary line `\nu=-1/2+i\tau`, the shadow-odd conical combination reduces to the `P_\nu` Mehler-Fock kernel with a `\tanh(\pi\tau)` coefficient, provided the off-cut/type-3 `Q` branch is kept explicit. The same paper retains the exact Fourier pair

\[
P(\lambda)=\frac{\pi\lambda}{\sinh(\pi\lambda)}
\quad\longleftrightarrow\quad
\frac1{4\cosh^2(y/2)}.
\]

The Mellin identity involving `(1-2^{-s})\Gamma(s)\zeta(s)` is treated only as a transform identity; zeros of that factor are not evidence for RH. No RH status change follows from these spectral identities.

## Yang-Mills / gravity cut discipline

The existing executable discovery result is stronger and more precise than a generic “projector needed” statement. A single exposed massive-vector leg obeys the five-dimensional Ward reconstruction

\[
p\cdot J_{4D}=\kappa J^5,
\]

so its physical massive projector contraction equals the corresponding five-dimensional metric contraction after the companion states are physical. But the raw two-index tree tensor is not separately transverse against arbitrary unphysical basis states on the other exposed leg. Therefore the two-particle cut must retain both massive projectors

\[
J_L^{\mu\nu}P^{(1)}_{\mu\rho}P^{(2)}_{\nu\sigma}J_R^{\rho\sigma}
\]

(or the equivalent explicit 3×3 polarization sums). The executable audit verifies equality between this double-projector contraction and the explicit nine-state sum. The honest remaining amplitude gate is the complete color-ordered two-massive-vector tree, physical double sewing, scalar subtraction for the `D_s=4` baseline, and only then generalized cuts/gravity.

The previous correction against inferring pure-Einstein box-only behavior by truncating the full `N=8` state sum remains in force.

## Record state

The Supabase Codex ledger read was blocked by the connector safety layer during this rotation, so no database state was fabricated. This Discovery2 file is the durable Codex/GPT record for the run.
