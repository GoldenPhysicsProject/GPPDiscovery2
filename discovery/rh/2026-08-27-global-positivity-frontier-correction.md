# RH positivity frontier correction — 2026-08-27

The live Verify2 branch is farther along on the arithmetic Bochner side than the working queue previously recorded.

Already formalized in `GlobalPrimePoissonPositiveType.lean`:

- a general closure theorem: a pointwise summable family of real positive-type kernels has positive-type `tsum`;
- for every real `a > 1`, the infinite prime-Poisson response `t ↦ Σ'_p WpA(p,a,t)` is positive type;
- via the exact prime-power regrouping identity, `t ↦ 2 Re(-ζ'/ζ(a+it))` is positive type.

Already formalized downstream:

- `GlobalPrimePoissonBound.lean`: `|Re(-ζ'/ζ(a+it))| ≤ Re(-ζ'/ζ(a))` for `a>1`;
- `GlobalPrimePoissonSecondDifference.lean`: `3R_a(0)-4R_a(t)+R_a(2t) ≥ 0`.

Therefore the next RH target is **not** another positive-type consequence on the absolute-convergence half-plane. `WeilSupportLadder.lean` identifies the sharper frontier. For convolution-square tests supported below the first arithmetic rung `log 2`, the prime side vanishes exactly. The unproved input is positivity of the archimedean Weil functional on that rung. Beyond rung zero, the decisive missing theorem remains the explicit-formula/operator transport that combines the archimedean square and the finite prime perturbation and lands in the already-formalized RH-equivalent zero-pairing PSD criterion.

Important nonclaim: positive type of `Re(-ζ'/ζ)` is not itself Weil positivity and must not be substituted for the zero-pairing criterion.

Same run: Gibbs CI #70 certified `ZetaFisherStrictMonotonicity.lean`; `ZetaGibbsFisherStrict.lean` then failed only on two unopened namespace-owned identifiers. Verify2 commit `4698e841b30efe9dddf8c7bd244debf095890445` exposes the owning namespaces without changing theorem statements. A new `SechConvolutionEndpoints.lean` proves the right-endpoint limit candidate from the quantitative log-cosh remainder bounds; dedicated CI gate added at Verify2 `aba13ce46fcfea01103fda84206b40015b27cc18`, pending kernel verdict at time of this note.
