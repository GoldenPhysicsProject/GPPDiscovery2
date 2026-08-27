# Codex formalization update — 2026-08-27

## Exact sech convolution

The live Verify2 branch already kernel-proved the scaled whole-line identity

\[
\int_{\mathbb R}\frac{\pi\sinh(\pi\lambda)}{\cosh(\pi x)\cosh(\pi(\lambda-x))}\,dx
=2\pi\lambda.
\]

Codex added `SechConvolutionClosedForm.lean` to extract the fixed nonzero factor. The first proof attempt failed only at the final automated cancellation: Lean had reduced the theorem to `pi*sinh(pi*lambda)*I = 2*pi*lambda`, but `nlinarith` cannot cancel the symbolic nonzero `sinh` factor. The repair explicitly cancels `pi` and then uses `eq_div_iff` with the proved `sinh(pi*lambda) != 0`. Dedicated sech CI #58 is green at Verify2 commit `78b15f4a3a531e61505c00802001a67378c01e0a`, proving

\[
\int_{\mathbb R}\frac{dx}{\cosh(\pi x)\cosh(\pi(\lambda-x))}
=\frac{2\lambda}{\sinh(\pi\lambda)},\qquad \lambda\ne0.
\]

The removable case `lambda=0`, whose target is `2/pi`, remains deliberately separate; no division-through-zero shortcut is used.

## Zeta Gibbs differential cumulants

A new Verify2 candidate `ZetaGibbsCumulantDerivative.lean` (introduced at `5f3784c3f39a94779e1d8aaf4e0d91b6f8b5189d`, gated at `ded0520de2c706e7974e14734093f50d4c3aef8d`) implements the exact route

1. genuine Gibbs variance = real part of the once-log-weighted von Mangoldt L-series;
2. `LSeries_hasDerivAt` inserts one further logarithm and a minus sign on `beta>1`;
3. the existing twice-log von Mangoldt bridge identifies that series with the genuine third Gibbs cumulant.

Target theorem:

\[
\frac{d}{d\beta}\operatorname{Var}_\beta(\log n)=-\kappa_3(\beta),
\]

with strict negativity following from the already-proved `kappa_3(beta)>0`. At the time of this note the dedicated Gibbs CI is still compiling, so this candidate is not yet promoted to certified status.

## Celestial cuts, gravity, and generalized sewing

Two formerly conflated gaps are already closed independently:

- `TreeLoopSewing.lean` proves the exact graph topology: sewing `L` disjoint pairs of a `(4+2L)`-point cubic tree leaves four external legs and produces cycle rank exactly `L`.
- `Mu8GravityRadialIntegral.lean` proves the D-dimensional all-plus gravity radial shell normalization
  `integral_0^infty tanh(r)/cosh(r)^8 dr = 1/8`.

The honest remaining gravity/celestial obstacles are analytic, not combinatorial: (a) reduce or directly control the four-uncut-propagator gravity angular/dispersion integral; (b) derive the explicit celestial pair-sewing identity equating inverse-Mellin double-shadow discontinuity with direct momentum-space pair closure. Neither is implied by the scalar two-denominator regulator theorem.

## Half-density / completed zeta / Weil boundary

The local operator stage is already stronger than the stale queue wording. `CutkoskyWeilBridge.lean` proves on `ell^2(Z,C)` the bounded-operator identity

\[
C_{K_r-1}=P_0 C_{K_r}P_0
\]

and positivity of the compressed operator from its Fourier eigenvalues (`0` at the vacuum mode and `r^{|n|}` otherwise). `ScaleShadowHalfDensity.lean` proves `Delta=2s`, critical-line/principal-series equivalence, and shadow as Hermitian conjugation on the unitary line. `CompletedZetaPrincipalSeriesResponse.lean` proves the completed-zeta logarithmic response is shadow-odd and purely imaginary on `Re Delta=1` away from zeros/poles.

Therefore the RH frontier is now stated more sharply: construct the global Mellin/Fourier/classical explicit-formula assembly that identifies the prime and Archimedean local operators with the genuine Weil quadratic form on an adequate test class, then prove that global form positive unconditionally. No local-kernel or operator result is promoted to RH.
