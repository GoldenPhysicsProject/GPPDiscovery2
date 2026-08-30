# Raised-box nested CI repair and cross-front status — 2026-08-30

## Verify2 CI diagnosis

The targeted scalar-box workflow on Verify2 head `92b57eb418c3f95c5ff2c52daf5dc8af12e11f8d` localized the first deterministic failure to `GppVerify/CelestialHolography/RaisedBoxSimplexNestedReduction.lean`.

The mathematical endpoint argument was sound.  At `x = 1`, however, the nonzero certificate was stated as

```lean
(((3 - δ : ℝ) : ℂ) - 1) ≠ 0
```

while simplification normalized the exponent in the goal to

```lean
((3 : ℂ) - (δ : ℂ) - 1) ≠ 0.
```

The mismatch prevented `simp [hne]` from closing the endpoint.  The resulting elaboration failure propagated into the downstream Beta-to-Gamma and residue targets and made their `#print axioms` output show `sorryAx`; that was a compilation artifact, not a newly introduced mathematical axiom.

The proof was repaired by certifying the normalized complex expression directly, taking complex real parts, and discharging the contradiction from `δ < 1`.  No theorem statement or hypothesis was weakened.

Verify2 repair commit:

`862f6011ca2c841dd128fc4ddf092c685b08dd0e`

The intended exact identity remains

\[
I_\delta
= B(1-\delta,3-\delta)B(1-\delta,2),
\qquad \delta<1.
\]

Fresh CI on the repair head has registered 23 checks.  The audit and one build lane are already green; ordinary `lake build` and the longer construction/targeted lanes were still running at the last poll.

## Scalar-box frontier

The repair restores the exact nested majorant reduction needed for the raised-box dominated-convergence route.  The analytic regulator statement remains

\[
J_\varepsilon(S,T)
=\int_{\Delta_3}(Sx_1x_3+Tx_2x_4)^{-\varepsilon}\,d^3x
\longrightarrow \frac16.
\]

The majorant integral is already exactly

\[
\int_{\Delta_3}(x_1x_3)^{-\delta}\,d^3x
=B(1-\delta,3-\delta)B(1-\delta,2)
=\frac{\Gamma(1-\delta)^2}{\Gamma(4-2\delta)},
\qquad 0<\delta<1.
\]

The remaining formal theorem is the AE/null-simplex-face and nested/filter dominated-convergence composition for the concrete simplex moment.  No additional Beta/Gamma identity is presently missing.

## Prime-gas fluctuation geometry

The strict countable centered Fisher quadratic form and the new `tsum` coefficient bridge remain the intended route to

\[
\det\operatorname{Cov}_{p_\beta}(\log n,(\log n)^2)>0.
\]

Once the current head is stable, certification of `PrimeFisherCenteredDeterminant.lean` should be checked directly rather than rebuilding a countable Cauchy--Binet layer.  The exact cumulant representation remains

\[
D_\beta=\kappa_2\kappa_4+2\kappa_2^3-\kappa_3^2.
\]

## Principal-series / Weil and spectral fronts

The focused kinematic paper continues to impose the correct boundary: the Mellin kernel gives the archimedean/additive zeta response and the Wiener--Hopf factors give the designated archimedean square problem, but this is explicitly a reformulation rather than an RH proof.  The missing global theorem is still a relative prime-plus-Archimedean trace/Gram construction identified with the signed Weil functional and endowed with non-circular positivity.

The exact Mehler--Fock/Macdonald resummation of the shadow spectral integral to the scalar-box dilogarithms also remains open.  Existing Gamma/Wiener--Hopf chamber positivity must not be promoted to global Weil positivity or an exact one-loop spectral reconstruction.

## YM / gravity frontier

Existing physical-chart, Ward, state-sum, dimension-shift, and radial identities remain infrastructure.  The next honest amplitude theorem still requires explicit fixed-loop-momentum nonzero-`μ` Yang--Mills tree amplitudes and physical massive-vector polarization sewing.  Higher-loop/generalized cuts and gravity numerators remain downstream of that step.
