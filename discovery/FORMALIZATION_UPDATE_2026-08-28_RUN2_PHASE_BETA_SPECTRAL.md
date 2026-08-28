# Codex/GPT cross-front continuation — 2026-08-28 run 2

Codex/GPT work only. No Claude work was inspected.

## Spectral Gamma / Wiener-Hopf

The dedicated sech/Wiener-Hopf lane showed that the prior all-order chamber-product repair was not terminally green. The recurrence module itself compiled, but `SpectralRhoChamberProduct.lean` still left one giant real-coercion/factorial normalization goal after `field_simp`.

The proof has now been refactored around the scalar coefficient

\[
c_k=\frac{2^{2k}}{(2k+1)!},
\]

with the exact recurrence

\[
c_{k+1}=\frac{2}{(k+1)(2k+3)}c_k.
\]

This is separated from the chamber polynomial recurrence

\[
P_{k+1}(x)=P_k(x)((k+1)^2+x^2).
\]

The complex induction then becomes a ring identity after applying the already-certified `rhoGamma_succ`. Candidate Verify2 commit: `b44194e66384edda1e9a12eb2390a8878bef94e0`. The expanded target remains

\[
\rho_k(x)=\frac{2^{2k}}{(2k+1)!}
\prod_{j=1}^{k}(j^2+x^2)\rho_0(x).
\]

No iterated-convolution interpretation is asserted from this algebraic product alone.

## Prime-gas thermodynamics

The exact Legendre law already gives

\[
F'(\beta)=\frac{S(\beta)}{\beta^2},
\qquad S'(\beta)=-\beta\kappa_2(\beta),
\qquad \beta>1.
\]

Differentiation yields the exact free-energy curvature response

\[
\boxed{
F''(\beta)=-\frac{\kappa_2(\beta)}{\beta}
-\frac{2S(\beta)}{\beta^3}.}
\]

This has been promoted as `ZetaGibbsFreeEnergyCurvature.lean`, candidate Verify2 commit `97b8be521c6e30400881069bb66bd98ac99a2a39`, and added to the dedicated Gibbs gate in commit `742882fbc8d1b7a6e9fc21209e6f937cf28a51f7`.

No sign of `F''` is claimed because the sign of the entropy potential itself was not used as an established theorem. This is deliberately distinct from the already-certified strict signs `κ₂>0`, `C>0`, and `S'<0`.

## Positive-real principal series / completed zeta

The completed-zeta logarithmic response `R(Δ)` is already purely imaginary on `Re Δ=1` away from its zeros. Define the phase-generator normalization

\[
\mathcal P(\Delta)=-iR(\Delta).
\]

Then on the celestial principal-series axis

\[
\Im \mathcal P(\Delta)=0,
\]

so the normalized response is real. It also remains shadow-odd because `R(Δ)=-R(2-Δ)`.

This packages the functional-equation response in the operator convention expected of an anti-Hermitian logarithmic generator / real phase response. Candidate Verify2 commit: `e29f9e426d2663027fcef84b10c839a0379c55b3`.

This does not locate zeros and does not establish Weil positivity.

## Raised-box regulator layer

The pointwise majorant was already formal. The exact analytic reduction is

\[
I_\delta
=B(1-\delta,2)B(1-\delta,3-\delta)
=\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)},
\qquad 0<\delta<1.
\]

The first Lean promotion now isolates the actual Mathlib Beta layer rather than pretending the whole simplex integral is done. `RaisedBoxSimplexBetaLayer.lean` formalizes:

1. positivity of the Beta real parts `1-δ` and `3-δ` for `δ<1`;
2. the scaled inner identity
\[
\int_0^a x^{-\delta}(a-x)\,dx
=a^{2-\delta}B(1-\delta,2)
\]
in Mathlib's complex-power representation;
3. convergence of the inner and outer unit-interval Beta integrals.

Candidate Verify2 commit: `7c65a82f083baa14ae4378d421dc3db97f338e0e`, gated by structured-majorant workflow commit `ac2fe6b9f9a193464453e77d5d056cadb6a8936a`.

The still-open theorem is the nested affine-simplex integral itself, including the `x2` integration/Fubini layer and real-to-complex power coercions, followed by DCT. The already-assembled structured massive scalar-box regulator theorem remains separate and should not be regressed to this open status.

## Honest YM / gravity boundary

No honest `D_s=4, μ≠0` gluon sewing numerator has yet been derived. `MassiveVectorStateSumReconstruction.lean` remains bookkeeping only. The next noncircular construction is to build the actual tree currents and their massive-vector polarization contraction, with the longitudinal projector term removed only after a proved Ward/transversality identity. Only after that numerator is fixed should double-copy/gravity and generalized/higher-loop cuts be promoted.

No claim was weakened to manufacture progress on this front.
