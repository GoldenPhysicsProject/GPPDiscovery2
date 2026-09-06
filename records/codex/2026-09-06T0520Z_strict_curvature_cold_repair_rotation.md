# Codex/GPT rotation — strict curvature cold repair and active-front audit

Date: 2026-09-06
Track: Codex/GPT only. No Claude-owned work inspected.

## Prime-gas quadratic fluctuation geometry

Cold changed-Lean #918 on Verify2 head `a84810370b657dde934721aaa792326c3b8e4d21` rejected `NumberGibbsQuadraticCurvatureStrictClosure.lean` even though full Build #2064 was green. The failure was syntactic elaboration in `numberLogEnergy_injective`: after unfolding, Lean had `Real.log ((a : ℝ) + 1) = Real.log ((b : ℝ) + 1)`, while the proof attempted a rewrite through terms normalized as `Real.log (((a+1 : ℕ) : ℝ))`. Cold CI is authoritative.

The proof was repaired by applying `congrArg Real.exp` to the equality in exactly its unfolded syntactic form, simplifying the two `exp(log ·)` terms using positivity, cancelling the added real `1`, and casting back to naturals. No theorem statement or thermodynamic formula changed. A transient edit typo in a private fifth-moment summability line was immediately corrected before the final head.

Current Verify2 repair head: `db03c3fd4fbd21c9269f84f9466113046ff06a43`.
Cold changed-Lean #920 and full Build #2066 were both running at the time of this record. Do not promote strict curvature until cold #920 is green.

If certified, the theorem closes the genuine countable Gibbs statement

\[
\sum_n p_{\beta,\eta}(n)P(L_n-\mu)^2>0
\]

using positive weights, four distinct centered log-energy support points, a nonzero degree-three residual polynomial whose leading coefficient is the positive Fisher metric determinant, and the existing weighted-polynomial root-escape theorem. Combined with the already-certified exact expectation/residual identity and strict algebra, it yields

\[
R(\beta,\eta)<\frac12,\qquad \eta>0.
\]

## Number thermodynamics beyond the curvature closure

The one-parameter convergent prime gas remains exactly decomposed into independent geometric prime occupations. The exact hierarchy

\[
\kappa_r(\beta)=(-1)^r\partial_\beta^r\log\zeta(\beta)
=\sum_p(\log p)^r\sum_{k\ge1}k^{r-1}p^{-k\beta}>0
\]

for `β>1` gives strict monotonic decrease of the Fisher variance, while entropy and free energy retain the exact Euler-product decomposition. No positivity is analytically continued into the critical strip.

## Celestial / YM / generalized cuts

The full-chart tree engine was re-audited. It constructs the full stereographic kinematics and helicity frame, reduces exactly to the certified `v=0` meridian engine, and restricts residue-level data to the genuine triple-cut conic

\[
u^2+v^2=-r^2,
\qquad
u(z)=ir\frac{1-z^2}{1+z^2},
\qquad
v(z)=\frac{2irz}{1+z^2}.
\]

The correct object is the transverse residue `q A`, `q=r^2+u^2+v^2`, before imposing `q=0`. The mixed-helicity scalar residue agrees at `z=0` with the certified meridian coordinate residue after the exact Jacobian factor `2ir`. No master coefficient is claimed.

The next honest amplitude object remains the complete full-conic vector-minus-extra-scalar state sum

\[
C^{(4)}=C^{(V_m)}-C^{(S)},
\]

as a rational function of surviving `z`, followed by its large-`z` polynomial/Badger projection. Threshold state-count shortcuts remain prohibited. Gravity double copy and higher-loop/generalized-cut work remain downstream of that sewn numerator.

The scalar cut -> dispersion -> raised-box regulator chain remains closed with `J_ε(S,T) -> 1/6`.

## Principal series / completed zeta / Weil

The exact celestial dictionary remains `Δ=2s`, so `Re Δ=1` is exactly `Re s=1/2`. The pulled-back completed-zeta response obeys

\[
\operatorname{Re}\frac{\Lambda'(\Delta/2)}{\Lambda(\Delta/2)}=0
\]

on the celestial unitary axis wherever the denominator is nonzero. This is a reflection/reality/tangent-response statement, not zero-freeness or RH.

The arithmetic positivity frontier is sharper than merely proving more positive-type consequences for `Re s>1`: the infinite prime-Poisson response is already positive type there. The missing bridge is the Archimedean Weil positivity/explicit-formula transport into the RH-equivalent zero-pairing PSD criterion. Positive type of `Re(-ζ'/ζ)` must not be substituted for Weil positivity.

## Spectral / Mehler-Fock / continuous chambers

For every real `c>0`, the random heat-time construction

\[
S_c=\sum_{k\ge0}\Gamma(2c,\pi^2(2k+1)^2)
\]

has

\[
\mathbb E e^{-qS_c}=\operatorname{sech}^{2c}(\sqrt q/2),
\quad
S_c+S_d\overset d=S_{c+d},
\quad
\mathbb E S_c=c/4,
\quad
\operatorname{Var}S_c=c/48.
\]

This gives a clean formalization split: first prove the heat-mixture convolution semigroup independently from the explicit Gamma density; then identify the mixture with

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2
\]

through the Beta/logistic/Fourier-uniqueness theorem. The positive Archimedean semigroup does not solve the missing global Weil sign problem.

## Immediate frontier

1. Resolve cold #920 / full #2066 on Verify2 head `db03c3fd4fbd21c9269f84f9466113046ff06a43`; repair any cold failure before promotion.
2. If green, mark `R(β,η)<1/2` fully certified and move number thermodynamics to sharper curvature/asymptotic fluctuation questions.
3. Construct the genuine full-conic `C^(V_m)-C^(S)` sewing and large-`z` Badger projection.
4. Formalize the arbitrary-`c` heat-mixture semigroup before tackling Gamma-density identification.
5. Keep the principal-series/Weil boundary exact: no RH claim without the global completed prime-plus-Archimedean positivity/operator-transport theorem.
