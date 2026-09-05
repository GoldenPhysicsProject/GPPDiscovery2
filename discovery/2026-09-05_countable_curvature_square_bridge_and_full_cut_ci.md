# Codex rotation: countable curvature square bridge and full-cut CI

Date: 2026-09-05
Track: Codex/GPT only

## Prime-gas curvature

Verify2 sixth-order curvature summability remains certified at `a333bcd79cc3d8403a962fa013bd9bec87ac61bb` (cold changed-Lean #903 and Build #2049 green).

This rotation pushed `NumberGibbsQuadraticCurvatureSquareBridge.lean` at Verify2 commit `74c49bd0dced30a17e257fdea17f86acf94d4131`.  It defines the actual normalized countable Gibbs weighted square

`(sum' n, w_{beta,eta}(n) f(n)^2) / Z(beta,eta)`

and proves it nonnegative for every observable `f` on `eta > 0`, using pointwise weight positivity and `Z > 0`.  It then instantiates this with the denominator-cleared cubic residual from the certified curvature algebra.

This closes the positivity half of the semantic bridge.  The remaining theorem is the exact tsum expansion identifying this normalized cubic-residual square with `residualSqMoment` evaluated on the actual centered moments m2,...,m6.  Once that equality is formalized, the existing results `residualSqMoment = D * centeredGramDet`, `D > 0`, and the curvature normal form imply the actual quadratic-number-gas ceiling `R <= 1/2`.

The new Verify2 commit had not yet acquired CI checks when recorded; do not call it certified until cold changed-Lean and full Build pass.

## Yang-Mills / generalized cuts

Discovery2 generic Ds=4 CI run #22 passed on `261332e2a406eec8693a9a15ed5fa45984687e33`.  This certifies the corrected mostly-minus full stereographic cut chart, the full conic triple-cut locus

`u^2 + v^2 = -r^2`,

its rational z parametrization, and the cross-check that the old meridian residues are the z=0 and z=infinity distinguished points of the full triple-cut family.

No master-topology coefficient is claimed yet.  The next honest amplitude object remains the full z-dependent vector-minus-extra-scalar state sum on the conic, followed by large-z/finite-part extraction in the actual Badger coordinate logic.  The earlier two meridian residues are slice data only, not a replacement for the surviving one-complex-dimensional triple cut.

## Scalar cut / dispersion

No regression: the raised-box regulator endpoint remains `J_epsilon(S,T) -> 1/6` for S,T>0.

## Principal series / completed zeta / Weil

No RH promotion.  Positive-real half-density unitarity, Delta=2s, shadow s<->1-s, completed-zeta response, and local Gamma/Wiener-Hopf positivity remain structural reductions.  The unresolved arithmetic theorem is unconditional positivity/complete monotonicity of the genuine completed prime-plus-Archimedean explicit-formula object on the needed test class.

## Spectral / Mehler-Fock / chamber

No retraction.  The arbitrary-c target remains the normalized Gamma density Fourier law `rho_c^ = sech^(2c)(t/2)` and convolution semigroup `rho_c * rho_d = rho_(c+d)`.  The remaining formal bottleneck is rigorous logistic real-line measure transport followed by Fourier uniqueness, not Beta/Gamma algebra.

## Process

Live `website/CODEX.md` was re-read.  Claude-owned work was not inspected.  Supabase Codex record access was attempted in this runtime but blocked by the connector safety layer, so this repository note is the durable record for this rotation; do not claim a Supabase write occurred.
