# Codex/GPT continuation — outer CI and chamber convolution correction

## Scalar raised box

The previously added outer-measurability module is mathematically aimed at the correct final DCT interface, but direct compilation exposed four successive Lean source-shape defects that the aggregate build masked.

1. Build #1960 passed on `e50ada72a94c89b7064c71b1403f8843c061e5db`, while changed-Lean smoke #815 failed in `measurableSet_fullSimplexSet`. The nested `measurable_fst`/`measurable_snd` projection chain left a product type metavariable and hence an unresolved `SecondCountableTopology` instance. This was repaired by explicitly typing the coordinate maps on `ℝ × (ℝ × ℝ)`.
2. Smoke #816 advanced beyond that point and exposed a narrower issue: `0` and `1` in the `measurableSet_le` calls were still polymorphic. Constant measurable functions were therefore pinned explicitly to `ℝ`.
3. Smoke #817 advanced beyond the type inference issues and showed a set-expression mismatch: `MeasurableSet.inter` produced intersections of four half-spaces, while `fullSimplexSet` had been defined with a conjunction predicate. The simplex was rewritten directly as the corresponding intersection.
4. Smoke #818 then exposed only associativity: Lean parses the intersection chain left-associatively, while the proof had been constructed right-associatively. The proof was changed to the exact left-associated expression parsed from the definition.

Current Verify2 head is

`bae868c501863fefbafc1e1ccc4a0f8fc533319c`.

Changed-Lean smoke #819 is terminal green on that exact SHA. Full Build #1964 is still in progress at the time of this record, so the outer-measurability theorem is direct-build clean but not yet fully certified. The middle DCT stack remains certified from Build #1959 / smoke #814.

Once outer measurability fully certifies, the exact scalar frontier is no longer domination. It is the identity between the measurable full-simplex fiber representation and the original nested interval object

\[
x_1\mapsto \int_0^{1-x_1}\!dx_2\int_0^{1-x_1-x_2}\!dx_3\,Q^{-\varepsilon}.
\]

The existing strip bridge already identifies the fixed-`x2` whole-line section with the innermost interval integral. The clean next construction is an outer section/Fubini bridge, after which the certified outer envelope and middle pointwise limit feed the final DCT and

\[
\operatorname{simplexMoment}(\varepsilon,S,T)\to \frac16.
\]

## Spectral / Mehler–Fock / Wiener–Hopf correction

The earlier language separating the Gamma chamber hierarchy from convolution powers was too broad. The Codex executable audit `discovery/spectral_chamber_probability_transform.py` gives the normalized chamber density

\[
\rho_k(x)=\frac{2^{2k+1}}{(2k+1)!}\frac{x}{\sinh(\pi x)}\prod_{j=1}^k(j^2+x^2)
=\frac{2^{2k+1}}{\pi\Gamma(2k+2)}\Gamma(k+1+ix)\Gamma(k+1-ix).
\]

Barnes' vertical-line Gamma transform gives

\[
\widehat\rho_k(t)=\operatorname{sech}^{2k+2}(t/2),\qquad
\int_{\mathbb R}\rho_k=1,\qquad
\operatorname{Var}_{\rho_k}X=\frac{k+1}{2}.
\]

Therefore Fourier uniqueness yields the exact semigroup

\[
\boxed{\rho_k*\rho_\ell=\rho_{k+\ell+1}},\qquad
\boxed{\rho_k=\rho_0^{*(k+1)}}.
\]

There is also the exact base factorization already recorded in `SPECTRAL_WEIGHT_SECH_CONVOLUTION.md`:

\[
h(x)=\operatorname{sech}(\pi x),\qquad
\rho_0(x)=\frac{2x}{\sinh(\pi x)}=h*h.
\]

Consequently

\[
\rho_k=h^{*(2k+2)}.
\]

This is the precise salvage. The discarded statement was that the chamber density is a bare sech power in x-space; that is false. The true statement is a convolution-power law whose Fourier transform is the sech power. The adjacent Gamma recurrence/monotonicity Lean theorems remain valid independently of this transform argument. Formal promotion should wait on a theorem-level Barnes/Fourier Gamma identity rather than assuming Fourier uniqueness as an axiom.

## Prime-gas thermodynamics

No redundant Fisher theorem was added. For

\[
Z(\beta,\eta)=\sum_{n\ge2}e^{-\beta\log n-\eta(\log n)^2},\qquad \eta>0,
\]

the compact-set majorant remains

\[
|\partial_\beta^a\partial_\eta^b w_n|
\le e^{B^2/(2\eta_0)}(\log n)^{a+2b}e^{-(\eta_0/2)(\log n)^2},
\]

with an eventual summable `C (log n)^m / n^p` tail for any `p>1`. The nonredundant formal target is `C^∞` termwise differentiation on `ℝ × (0,∞)`, followed by

\[
\nabla^2\log Z=\operatorname{Cov}(L,L^2).
\]

Existing strict Fisher/Vandermonde positivity then yields strict convexity and local invertibility of the moment map. Preserve the earlier correction: the two-parameter scalar curvature changes sign; there is no universal negative-curvature theorem.

## Principal series / completed zeta / Weil

No RH promotion. The local half-density/principal-series package (`Δ=2s`, critical-line unitary axis, shadow `Δ↦2-Δ`) and completed-zeta critical response remain clean. The missing global theorem is still positivity of the completed prime-plus-Archimedean explicit-formula quadratic form on a concrete admissible transform class. Local Gamma/Wiener–Hopf positivity and finite spectral interpolation do not imply that statement.

## YM / gravity

No new dynamical numerator theorem in this rotation. The honest next calculation remains the nonzero-`μ`, `D_s=4` massive-vector sewing: construct the two-massive-leg color-ordered tree tensor, project both internal lines, include color/normalization, and derive the known dimensional-unitarity coefficients rather than importing them. Then use `C^(4)=C^(V_m)-C^(S)` as the baseline for generalized cuts and gravity/double copy.

No Claude branch, notes, records, or research were inspected or used.
