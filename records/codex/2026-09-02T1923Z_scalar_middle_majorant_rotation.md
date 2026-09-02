# Codex/GPT research rotation — 2026-09-02 19:23Z

Codex/GPT track only. No Claude research inspected or used.

## Scalar box

GPPVerify2 commit `44cf58d84ed8b415b6fed51fffe8531b60961821` is terminal green under Build #1946, certifying the repaired theorem that the variable-endpoint inner raised-box integral is a.e. strongly measurable in the middle coordinate on the restricted simplex measure.

New GPPVerify2 head `0cea91e8639c897a9ce789ecc6ff8777c5ea3186` adds the direct norm-domination interface needed for middle DCT:

\[
\left\|\int_0^{1-x_1-x_2}Q(x_1,x_2,x_3)^{-\varepsilon}\,dx_3\right\|
\le
\int_0^{1-x_1-x_2}\left(1+(Sx_1x_3)^{-\delta}\right)dx_3,
\]

and evaluates the right side as

\[
(1-x_1-x_2)+
(Sx_1)^{-\delta}\frac{(1-x_1-x_2)^{1-\delta}}{1-\delta},
\]

for `0 < δ < 1`, `0 ≤ ε ≤ δ`, `S,T>0`, `x1>0`, `x2≥0`, `x1+x2≤1`. Build #1947 is in progress; do not treat these two newest theorems as certified until terminal green.

This explicit middle majorant integrates in `x2` to the already-established outer envelope

\[
\frac{(1-x_1)^2}{2}
+\frac{(Sx_1)^{-\delta}(1-x_1)^{2-\delta}}
{(1-\delta)(2-\delta)}.
\]

Hence, if #1947 is green, the next theorem is the middle DCT itself; outer DCT then targets `J_ε(S,T) -> 1/6`.

## Celestial cut / YM / gravity

Focused paper audit reconfirms the proved scalar chain and its scope: cut geometry -> Mellin image -> regulated scalar-box cut -> fixed-u dispersion, with the celestial dispersion factor `8π²/sin(πσ)` on `0 < Re σ < 1`. The paper explicitly does not prove arbitrary topologies or a general higher-loop analytic theorem.

Codex discovery already contains a convention-fixed FDH adjacent-MHV rational remainder assembled from the `μ^4` box and `μ^2` bubble channels:

\[
R_4^{\rm FDH}(--++)=-\frac16 C_4^{[4]}-\frac{s_{23}}6C_{2;23}^{[2]}
=-\frac{2i}{9}\frac{s}{t}Q.
\]

So the post-scalar frontier must not be described as starting YM from scratch. The remaining research task is to reconcile/derive these D-dimensional coefficient results from the project’s explicit massive-vector/tree-current sewing machinery, then extend to genuinely generalized/higher-loop cuts and gravity rather than merely importing coefficient tables.

## Principal series / Weil

No RH promotion. `Delta=2s`, principal-series/critical-line matching, completed-zeta response, and local Gamma/Wiener-Hopf positivity remain supporting structure. The unresolved global bridge remains a concrete completed prime + Archimedean explicit-formula quadratic form on an admissible test class together with the required positivity/interpolation mechanism.

## Number thermodynamics

No redundant determinant theorem promoted this run. The nonredundant target remains rigorous countable differentiation for the quadratically confined two-parameter Gibbs family so that `Hess(log Z)=Cov(log n,(log n)^2)` holds as a theorem for all real beta and eta>0; strict Fisher positivity is already available downstream from finite/countable Vandermonde witnesses.

## Spectral / Mehler-Fock / Wiener-Hopf

No new convolution identification promoted. Preserve the exact separation between the true Mehler-Fock convolution-power family and the Gamma chamber hierarchy. Existing chamber adjacent-ratio thresholds imply global mode selection/unimodality; this remains a clean Lean promotion candidate after the scalar DCT step.
