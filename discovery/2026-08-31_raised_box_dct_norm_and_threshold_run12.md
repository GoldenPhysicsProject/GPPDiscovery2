# Codex run: raised-box DCT norm bridge and threshold asymptotic

Date: 2026-08-31
Track: Codex/GPT only

## Lean advance

`GPPVerify2:codex/lean-workbench` advanced from the certified baseline
`9881d7274a7d48237f917808d978d6dddd5c2a47` to
`792d733f78c78ca751bb3ae757ec448e09be53f2`.

`RaisedBoxRealOuterDomination.lean` now proves the DCT-ready norm estimate

    || x^(-delta) (1-x)^(2-delta) || <= x^(-delta)

for `0 <= x <= 1` and `delta < 1`.

This is stronger at the measure-theory interface than the previous scalar inequality because `Integrable.mono'` and dominated-convergence APIs are formulated in norm/absolute-value form. The proof uses the existing nonnegativity theorem and the already-certified pointwise bound, so no new analytic assumption is introduced.

## Exact threshold asymptotic

The one-channel real simplex majorant has exact total mass

    M_delta(S)
      = 1/6 + S^(-delta) Gamma(1-delta)^2 / Gamma(4-2delta),

for `S>0` and `0<delta<1`.

Set `e = 1-delta`. Then

    Gamma(e) ~ 1/e,
    Gamma(2+2e) -> Gamma(2) = 1,
    S^(-delta) = S^(-1+e) -> S^(-1).

Therefore

    (1-delta)^2 M_delta(S) -> S^(-1)

as `delta -> 1-`.

So the chosen physical one-channel majorant has a genuine double-pole divergence at the endpoint `delta=1`; the `delta<1` condition is sharp for this domination strategy, and the divergence rate is exactly quadratic in `1/(1-delta)`.

This does not obstruct the regulator limit because the DCT argument fixes any single `delta` with `0<delta<1` and only sends `epsilon -> 0+`. It does rule out trying to make the same domination uniform all the way to `delta=1`.

## Cross-front audit

Prime-gas: all-order strict polynomial Hankel/Gram positivity remains certified on the baseline. The next genuinely new thermodynamic theorem should concern the open two-parameter `(beta,eta)` Gibbs family or a rigorous asymptotic/curvature statement, not another reformulation of one-dimensional variance positivity.

Principal-series/Weil: `Delta=2s`, critical-line unitary dilation characters, completed-zeta response symmetry, Gamma-one Wiener-Hopf extension, and local positive kernels remain exact. The global missing theorem is still the non-circular prime-plus-Archimedean identification with the genuine Weil quadratic form and unconditional positivity on an adequate test class.

Spectral/chambers: the all-order Gamma/Mehler-Fock chamber hierarchy is exact, but no repeated-sech convolution law is inferred beyond the cases actually proved.

YM/gravity: the scalar regulator is still one measure-theory theorem away from Lean closure. The next honest amplitude object remains the fixed-loop-momentum `D_s=4`, `mu != 0` Yang-Mills tree sewing numerator; state-count/projector algebra is not being substituted for the tree amplitude.

No Claude branch, records, files, or context were inspected.
