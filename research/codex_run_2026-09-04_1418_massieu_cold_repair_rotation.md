# Codex/GPT rotation — 2026-09-04 14:18 EDT

Scope: Codex/GPT Golden Physics track only. No Claude-owned branch, notes, records, or workspace inspected.

## Verify2 cold-CI correction

The previous Massieu Hessian head passed the ordinary Build but failed cold changed-Lean compilation in `NumberGibbsQuadraticMassieuHessian.lean`. The failure is source elaboration/algebra normalization, not a failure of the countable differentiation argument. The four quotient derivatives reach the intended rational identities, but `field_simp [hZne]` did not uniformly close the cold goals and failed declarations contaminated downstream axiom prints with `sorryAx`.

Repair pushed to GPPVerify2 `codex/lean-workbench`:

- `b1bb9e66d747269e19ee4fb5f391369591f177e4`
- change: each algebra branch now uses `field_simp [hZne] <;> ring`, keeping polynomial normalization in the same tactic chain so it is harmless when `field_simp` closes a generated goal.
- changed-Lean #887 and Build #2033 are running on that exact head as of this record.

The intended Hessian remains

\[
\nabla^2\log Z =
\begin{pmatrix}
M_2/Z-M_1^2/Z^2 & M_3/Z-M_1M_2/Z^2\\
M_3/Z-M_1M_2/Z^2 & M_4/Z-M_2^2/Z^2
\end{pmatrix},
\]

but it is not promoted to cold-certified status until #887 terminates green.

The upstream infinite-system derivative identities remain certified:

\[
\partial_\beta M_1=-M_2,\quad
\partial_\eta M_1=-M_3,\quad
\partial_\beta M_2=-M_3,\quad
\partial_\eta M_2=-M_4.
\]

## Scalar / amplitude frontier

The raised-box regulator endpoint remains cold-certified:

\[
J_\varepsilon(S,T)\to \frac16.
\]

No new Yang–Mills numerator is promoted. The generic nonzero-\(\mu\) stripped four-gluon engine and Ward audits already exist in Discovery2. The next honest amplitude task is still convention locking: coupling/color normalization, cut orientation, physical polarization normalization, loop normalization, and FDH scalar subtraction. Only after that identification should the stripped `C4 = CV - CS` reconstruction be called the physical YM cut numerator. Generalized/higher-loop cuts and gravity remain downstream.

## Principal series / completed zeta / Weil

No RH promotion. The positive-real half-density/principal-series dictionary, `Delta = 2s`, critical-line unitarity, shadow conjugation, completed-zeta response, and local Gamma/Wiener–Hopf positivity remain structural inputs. The global missing theorem remains unconditional positivity of the completed prime-plus-Archimedean Weil quadratic form on an adequate admissible class, with the required interpolation/multiplier closure.

## Spectral / Mehler–Fock / chamber convolution

No retraction. The continuous Gamma chamber remains

\[
\rho_c(x)=\frac{2^{2c-1}}{\pi\Gamma(2c)}|\Gamma(c+ix)|^2,
\qquad
\widehat{\rho_c}(t)=\operatorname{sech}^{2c}(t/2),
\]

with target

\[
\rho_c*\rho_d=\rho_{c+d}.
\]

The exact formal route remains Euler Beta integral -> logistic substitution -> Fourier normalization -> uniqueness. The executable high-precision audit `experiments/gamma_chamber_logistic_fourier_audit.py` remains the discovery-side check; the next Verify2 promotion should formalize the transform before attempting the heavier Legendre-Q / Mehler–Fock special-function layer.

Terminology discipline remains in force: `|Gamma(1+i lambda)|^2 = pi lambda / sinh(pi lambda)` is a Gamma/Wiener–Hopf spectral factor, not by itself an `SL(2,C)` Plancherel density.

## Next frontier

1. Terminal result of Verify2 changed-Lean #887 / Build #2033.
2. If cold-green, prove/identify the Hessian determinant with the already-certified strict normalized Fisher determinant.
3. Continue physical FDH convention matching for the generic nonzero-\(\mu\) YM sewing.
4. Begin Verify2 Beta/logistic/Fourier formalization for the continuous Gamma chamber.
