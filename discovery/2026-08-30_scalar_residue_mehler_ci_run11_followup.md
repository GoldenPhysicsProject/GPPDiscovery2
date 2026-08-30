# Codex follow-up: raised-box residue and Mehler-Fock CI localization

## Verify2 head audited

Starting Verify2 head: `17670875d3b86114c02e1b4ea34ffb37a93ab463` on `codex/lean-workbench`.

Fresh inspection of GitHub Actions localized two independent deterministic failures:

1. `Codex structured scalar-box majorant` passes the physical majorant, structured core/convergence, Gamma residue, raised-box majorant algebra, scaled Beta layer, nested simplex reduction, Beta-to-Gamma closure, and pointwise regulator limit. Its sole failing step is `Raised-box residue assembly`.
2. `Codex fast gates` passes the scalar-box convergence chain, adjacent-MHV algebra, massive-vector scalar reconstruction, real dilogarithm/Landen chain, Gamma phase symmetry, strict weighted variance, zeta-Gibbs thermodynamics, Ward reconstruction, Gr(2,4), twistor and antiunitary exchange. Its independent failing step is `Mehler-Fock Gamma collapsed weight`.

## Raised-box residue repair

The residue assembly was using `tendsto_nhdsWithin_of_tendsto_nhds tendsto_id` to supply a source-filter restriction. That theorem acts on the target neighborhood and is the wrong direction for the obligation

`Tendsto id (nhdsWithin 0 S) (nhds 0)`.

The correct source restriction is monotonicity of `tendsto_id`:

```lean
(tendsto_id.mono_left inf_le_left)
```

This was substituted for both the punctured-real and positive-regulator `mu^4` specializations. Verify2 commit:

`66f45cc2f4ab3159ee88f1dbb3393f8bc6bd9a20` — `Repair raised-box residue source-filter convergence`.

The theorem statements remain unchanged. In particular, once the concrete simplex DCT is supplied, the dimension-shifted rational term still tends to `-1/6`.

## Scalar frontier after repair

The targeted workflow proves that all supporting analytic algebra beneath the DCT is now independently green through:

- concrete/structured scalar-box majorants,
- Gamma residue at zero,
- raised-box pointwise majorant,
- scaled Beta integrals,
- nested simplex Beta product,
- Beta-to-Gamma closure,
- pointwise regulator removal.

Thus the only genuine scalar analytic theorem still absent is the concrete AE/null-face/Fubini-DCT statement

`simplexMoment eps S T -> 1/6` as `eps -> 0+`.

No new Beta/Gamma identity is needed.

## Mehler-Fock CI localization

`MehlerFockGammaCollapsedWeight.lean` is independently red in the fast gate, while its prerequisite `Gamma real-axis phase symmetry` and the rest of the spectral/thermodynamic fast targets are green. The module's intended exact identities remain:

`Gamma(1/2+i lambda) Gamma(1/2-i lambda) = pi/cosh(pi lambda)`

and

`wienerHopfWeight lambda * mehlerFockWeight lambda = lambda^2 Gamma(1/2+i lambda) Gamma(1/2-i lambda)`.

The connector currently exposes the failing step but not the Lean annotation/log body, so no speculative Mehler-Fock source modification was made in this run. The next action is to extract or reproduce the exact elaboration diagnostic and repair only that statement/proof without weakening the all-real identity.

## Other active fronts

- Prime-gas: centered strict infinite Fisher quadratic positivity and cumulant determinant identities remain intact; pending endpoint remains certification/strict covariance determinant packaging and subsequent genuine multi-parameter curvature work.
- Weil/principal series: no RH promotion. Missing global theorem remains the prime-plus-Archimedean relative trace/Gram identification with the genuine Weil form and unconditional positivity.
- YM/gravity: no promotion from state-sum/Ward infrastructure. Missing physics theorem remains explicit fixed-loop-momentum, nonzero-mu Yang-Mills trees sewn over physical massive-vector polarizations before generalized/higher-loop cuts and gravity reconstruction.
- Spectral/chamber: Gamma/Wiener-Hopf/chamber identities remain local/exact; exact Mehler-Fock/Macdonald reconstruction of box dilogarithms remains open.
