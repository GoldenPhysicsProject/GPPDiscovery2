# Celestial light / principal-series / ambidextrous intertwiner structure

Date: 2026-09-05
Status: internal exact label algebra + external analytic intertwiner + exact normalization comparison

## Chiral light transforms

For split celestial weights `(h,hbar)`, keep the operations distinct:

`L(h,hbar) = (1-h,hbar)`

`Lbar(h,hbar) = (h,1-hbar)`

`S(h,hbar) = (1-h,1-hbar) = L Lbar(h,hbar)`

`P(h,hbar) = (hbar,h)`

where `P` is chiral factor exchange/parity at the representation-label level.

Exact algebra:

- `L²=Lbar²=S²=P²=1`;
- `L Lbar = Lbar L`;
- `P L P = Lbar` and `P Lbar P = L`;
- `P S = S P`.

Thus full shadow is not parity/orientation. It is the product of the two chiral light reflections.

In `(Δ,J)=(h+hbar,h-hbar)` coordinates:

- `L : (Δ,J) -> (1-J,1-Δ)`;
- `Lbar : (Δ,J) -> (1+J,Δ-1)`;
- `S : (Δ,J) -> (2-Δ,-J)`;
- `P : (Δ,J) -> (Δ,-J)`.

On principal-series weights

`h=1/2+ia`, `hbar=1/2+ib`,

`L` flips only `a`, `Lbar` flips only `b`, shadow flips both, parity swaps the two parameters.

Lean: `CelestialLightWeylIntertwiners.lean`.

## Analytic external theorem

Brown–Gowdy–Spence, *Celestial twistor amplitudes* (2023), identify split-signature twistor half-Fourier transforms with the corresponding celestial light transforms after half-Mellin transformation. Full Fourier corresponds to full celestial shadow.

This gives the correct field-level interpretation of the chiral factorization:

- one half-Fourier ↔ `L`;
- the opposite half-Fourier ↔ `Lbar`;
- full Fourier ↔ `S=L Lbar`.

This is better suited to the googly problem than treating full Fourier as the chirality exchange, because full Fourier is a same-state representation change while the two half transforms retain the chirality tag.

## Exact GPP principal-series normalization match

The GPP paper `Principal-Series Kinematic Blocks for Celestial Two-Particle Cuts` uses

`h=(1+iλ)/2`

and proves

`|c(λ)|² = (2λ/π)coth(πλ/2)`.

For the normalized split light transform, the two real `Z2` principal-series sectors have densities

`ρ_even(λ)=λ/(2π)tanh(πλ/2)`

and

`ρ_odd(λ)=λ/(2π)coth(πλ/2)`.

Therefore exactly

`|c(λ)|² = 4 ρ_odd(λ)`.

Lean: `PrincipalSeriesLightPlancherelMatch.lean` formalizes this final closed-form identity only. The Gamma-function derivations remain external/local-paper inputs.

A stronger complex normalization relation was derived algebraically:

`κ_1(λ) = (i/2) [Γ(1/2-iλ/2)/Γ(1/2+iλ/2)] c(-λ)`.

For real `λ`, the Gamma ratio is a pure phase. This is an exact normalization relation, but it should not yet be promoted to an identification of the full operators until the basis/convention map is written explicitly.

## Current interpretation

The flat infinity-twistor complex produces two projective two-spinor factors, and the normalized Weyl intertwiners act independently on them. Projective ambitwistor space contains both chiral projections simultaneously. This gives the representation-theoretic version of “both halves are here” without identifying shadow with parity or attempting to derive one chirality from the other.

Latest relevant GPPVerify integration commit at time of note: `6958d067d308ba859dd2a5493a9b2d4b05bf9c15`.
