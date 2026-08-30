# Follow-up CI repairs: raised-box Gamma closure and twistor googly lift — 2026-08-30

This follows `2026-08-30_raised_box_nested_ci_repair_run11.md` and records two further deterministic elaboration failures exposed after the nested-simplex repair passed.

## 1. Nested simplex repair certified in targeted CI

Verify2 commit `862f6011ca2c841dd128fc4ddf092c685b08dd0e` successfully rebuilt

- `RaisedBoxSimplexNestedReduction`,
- `nestedSimplexIntegral_eq_reduced`, and
- `nestedSimplexIntegral_eq_beta_product`

without `sorryAx`.  The exact identity remains

\[
I_\delta=B(1-\delta,3-\delta)B(1-\delta,2),\qquad \delta<1.
\]

## 2. Raised-box Gamma closure repair

Once the nested reduction was green, targeted CI reached `RaisedBoxSimplexGammaClosure` and exposed a pure product-orientation mismatch after `field_simp`:

```text
Gamma c * (B(a,b) * B(a,2))
```

was supplied where Lean expected

```text
(B(a,b) * B(a,2)) * Gamma c.
```

The proof now starts from the exact post-`field_simp` orientation and commutes/reassociates the first product by ring normalization before using the two Beta--Gamma identities.  No theorem statement or analytic hypothesis changed.

Verify2 repair commit:

`17670875d3b86114c02e1b4ea34ffb37a93ab463`

The intended identity is still

\[
B(1-\delta,3-\delta)B(1-\delta,2)
=\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)}.
\]

## 3. Twistor googly lift repair

A separate full-construction lane exposed two elementary normalization failures in `GooglyTwistorLift`: `ring` left goals containing `Complex.I^2`, including

\[
-(i^2 z_j)=z_j,
\]

and the corresponding Pluecker bilinears.  CI itself indicated `ring_nf`; replacing the final normalizer by `ring_nf` in the involution and exterior-square lift proofs resolves exactly the missing `i^2=-1` normalization without changing definitions or statements.

Intermediate Verify2 repair commit:

`21fb6fe22ee061de377906c34e707976248162a7`

The geometric statements remain

\[
G(G(z))=z
\]

for the antiunitary twistor phase-conjugation map, and

\[
\operatorname{Pluecker}(Gv_1,Gv_2)
=\operatorname{googlyExchange}(\operatorname{Pluecker}(v_1,v_2)).
\]

This is Grassmannian/celestial infrastructure only; it is not the missing explicit nonzero-`mu` Yang--Mills tree sewing theorem.

## 4. Current frontiers

The scalar regulator mathematics remains closed analytically:

\[
J_\varepsilon(S,T)\to\frac16,
\]

with exact integrable majorant

\[
\int_{\Delta_3}(x_1x_3)^{-\delta}d^3x
=\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)},\qquad 0<\delta<1.
\]

The remaining scalar formal endpoint is the AE/null-face/nested dominated-convergence theorem for the concrete simplex moment.  After that, the existing residue and dimension-shift assembly can consume the limit.

The prime-gas lane retains the countable centered strict quadratic form plus the `tsum` coefficient bridge as the shortest route to a strict two-observable Fisher covariance determinant.  The exact cumulant identity remains

\[
D_\beta=\kappa_2\kappa_4+2\kappa_2^3-\kappa_3^2.
\]

The global Weil boundary is unchanged: local half-density/principal-series, completed-zeta response, heat/von-Mangoldt anomaly, and Wiener--Hopf/Gamma chamber identities do not replace the missing relative prime-plus-Archimedean trace/Gram identification and non-circular positivity theorem.

The exact Mehler--Fock/Macdonald resummation to the scalar-box dilogarithms remains open.

The YM/gravity boundary remains explicit fixed-loop-momentum nonzero-`mu` Yang--Mills tree amplitudes sewn over physical massive-vector polarizations before any generalized/higher-loop cut claim.

Fresh CI has been triggered on current Verify2 head `17670875d3b86114c02e1b4ea34ffb37a93ab463`; certification is pending.
