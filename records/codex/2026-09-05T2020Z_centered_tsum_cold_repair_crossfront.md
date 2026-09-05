# Codex/GPT all-front continuation — centered `tsum` cold repair and cross-front boundary audit

## Verify2 / number thermodynamics

Cold changed-Lean run #910 on `a34c90457736ad78c85678bc79602dd23d710819` failed although full Build #2056 passed. The failure is source elaboration in `NumberGibbsQuadraticCenteredMoments.lean`: RHS `∑' n : ℕ, ...` expressions with multiline additive summands allowed later occurrences of `n` to escape the binder in the cold build, producing `unknown identifier n` and downstream `tsum` rewrite failures.

Repair pushed to GPPVerify2 `codex/lean-workbench`:

- `60355d3220ee5c767c25f19b84c91141e056cff1` (`Fix centered tsum binder scope`)
- parenthesizes the full bound summands in the first- and second-centered-moment `tsum` calculations;
- theorem statements, normalized probability model, centered-moment definitions, determinant algebra, and positivity claims are unchanged.

Cold #911 and full Build #2057 were triggered and were still running when this record was written. Do not promote the repaired centered-expectation theorems until cold #911 is green.

The target remains

\[
\langle P(Y)^2\rangle=\operatorname{residualSqMoment}(m_2,\ldots,m_6)=D\det H,
\]

then the already-certified square positivity and `D>0` yield `R <= 1/2`.

## YM / generalized-cut boundary

The full-conic massive-vector covariance theorem remains the certified pre-sewing frontier. Reinspection of the generic state-sum engine confirms an important restriction that must survive the next sewing step: the old same-helicity `vector = 3 scalar` relation is threshold-only. At generic massive kinematics its exact defect is

\[
C_V-3C_S=
\frac{4(r^2-1)^2(1+t^2)^2}{(r^2+t^2)^2}.
\]

Likewise the mixed-helicity extra-scalar tree is generically nonzero,

\[
S_{+-}=-\frac{2t^2(r^2-1)^2}{(r^2+1)(r^2+t^2)(1+t^2)},
\]

and vanishes on the old threshold slice `r=1`. Therefore the next full-conic opposite-tree sewing must use the actual vector and scalar residues/tree data, not state-count multiplication inherited from threshold.

No triangle/bubble/box master coefficient is promoted here.

## Principal series / completed zeta

The current Codex principal-series record gives an exact chiral-light algebra on `(h,hbar)` and the split-principal-series normalization match

\[
|c(\lambda)|^2=4\rho_{\mathrm{odd}}(\lambda),
\qquad
\rho_{\mathrm{odd}}(\lambda)=\frac{\lambda}{2\pi}\coth\frac{\pi\lambda}{2}.
\]

This strengthens the local intertwiner/Plancherel normalization interface but does not prove global prime-plus-Archimedean Weil positivity. RH remains unpromoted.

## Spectral / Mehler-Fock / Wiener-Hopf

The exact integer chamber family remains

\[
\rho_m(x)=\frac{2^{2m-1}}{\pi\Gamma(2m)}|\Gamma(m+ix)|^2,
\qquad
\widehat{\rho_m}(k)=\operatorname{sech}^{2m}(k/2),
\qquad
\rho_m=\rho^{*m}.
\]

Equivalently

\[
\rho_m(x)=\frac{2^{2m-2}}{\Gamma(2m)}
\Bigl(\prod_{j=1}^{m-1}(j^2+x^2)\Bigr)\rho(x).
\]

This is exact for integer `m>=1`. The arbitrary real `c>0` semigroup remains an analytic-formalization frontier: rigorous logit/logistic transport plus Fourier uniqueness are still required before promotion.

## Scalar box

No regression: the scalar cut -> dispersion -> raised-box regulator endpoint remains closed with

\[
J_\varepsilon(S,T)\to 1/6.
\]

## Next

1. Terminal cold #911 / Build #2057; repair if cold fails.
2. If green, extend honest centered Gibbs `tsum` identities through orders 3–6 and close the cubic-square expectation bridge.
3. Build the genuinely sewn full-conic `D_s=4` vector-minus-extra-scalar state sum using generic, not threshold, state data; only then apply the Badger projector.
4. Keep the global Weil positivity and arbitrary-real chamber semigroup boundaries explicit.
