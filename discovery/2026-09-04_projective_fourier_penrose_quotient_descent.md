# Projective Fourier/Penrose quotient descent — 2026-09-04

## Status

Exact abstract consequence formalized in `GPPVerify` on `codex/orientation-mass-time-formalization`; the analytic projective Fourier/Penrose commuting square itself remains open.

## New structural point

Suppose there is a representative-level projective Fourier transform

\[
\mathcal F: \mathcal T \to \widetilde{\mathcal T}
\]

with source and dual Penrose maps

\[
P_+:\mathcal T\to\mathcal B,\qquad P_-:\widetilde{\mathcal T}\to\mathcal B,
\]

and bulk orientation reversal `R` satisfying

\[
P_-\,\mathcal F = R\,P_+.
\]

Then no representative-level injectivity assumption is needed for the Fourier transform to descend to physical/Penrose classes. If

\[
P_+(f)=P_+(g),
\]

then automatically

\[
P_-(\mathcal Ff)=P_-(\mathcal Fg).
\]

Equivalently, the source Penrose kernel is mapped into the dual Penrose kernel.

This is exactly the quotient statement needed when homogeneous/distributional projective Fourier representatives are only defined modulo Penrose-null regularization terms.

If both forward and backward transforms satisfy the corresponding commuting squares and `R^2=1`, then literal representative equality is unnecessary: two transforms close on physical classes,

\[
P_+\bigl(\mathcal F^{-}\mathcal F f\bigr)=P_+(f),
\]

and similarly on the dual side.

## Formalization

New module:

`GppVerify/CelestialHolography/ProjectiveFourierIntertwinerCriterion.lean`

Commit at creation:

`98d5c08c106f9225b67535bca5b344682f5a1f0c`

The module explicitly marks the commuting square as a hypothesis rather than pretending the distributional projective Fourier theorem has been constructed.

## Why this matters for the googly problem

The natural mathematical target is therefore not a pointwise involution on twistor representatives. The strongest needed statement is a well-defined involution on the quotient by the Penrose kernel. This matches the current geometry:

- annihilator duality is correspondence-valued rather than point-valued;
- split metric polarity, Grassmannian complement, and split Hodge coincide on the big cell;
- Fourier support lands on the annihilator plane;
- projective Fourier homogeneity gives `k -> -k-4`;
- regularization ambiguities can live upstairs while disappearing after Penrose reconstruction.

The remaining hard theorem is still the analytic/distributional identity

\[
P_-\circ D_\varepsilon = R_{\mathfrak o}\circ P_+
\]

for the genuine homogeneous projective Fourier/Radon/Penrose transform.
