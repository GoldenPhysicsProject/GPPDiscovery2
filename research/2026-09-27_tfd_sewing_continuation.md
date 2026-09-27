# TFD sewing continuation checkpoint

Date: 2026-09-27. Research process: Codex/GPT, without subagents.
Baseline recovered from GPPDiscovery2 branch codex/discovery-workbench, commit 32ed875ee77778774a09763d1c9b737b2fc5bc69.
Status: exact mathematical results and floating-point controls; RH is not proved; no new Lean certification.

## Continuity recovered

- The user handoff ended at b730760cfa51b0efba70f74716c80e323af4eb62. The live branch was newer and included 39 September 27 research notes, including the explicit SU(1,1) Jacobi intertwiner, local cross-mode obstruction, prime-edge DtN construction, and real-place pole/trivial-zero ladder.
- Personal conversation retrieval recovered relevant excerpts, not the full preceding transcript. The exact formulas were checked against repository text and the attached v34 manuscript.
- The real-place contact normalization and subtraction were retained. The older Haar-alone argument remains invalid.
- Supabase preserved the September 24 signed spectral criterion, omitted from the handoff. Its provenance is retained in the new distribution-domain reduction.
- The discovery Lean run attached to b730760 completed with failure: GitHub Actions run 36291785011. No build success is claimed. This continuation did not repair the sandbox or Claude's GPPVerify migration.
- GPP-bridge/CODEX.md confirms full Codex-owned bridge narrative plus Supabase mirror. Existing Codex records are used; Claude's files and branches are not changed.

## New derivations

1. [Boundary Cayley and parity sewing](2026-09-27_tfd_boundary_cayley_parity_sewing.md).
   The normalized interval precision has Cayley transfer \(p^{-s}S\). The full paired determinant yields \(\zeta(2s)\); the symmetric restriction yields \(\zeta(s)\). The actual endpoint Schur covariance is an explicitly positive mixed-boundary Stieltjes sum, but differs from the vacuum-subtracted arithmetic current. The entire even Euler sector can be isolated as \(\tfrac12\log\zeta(2s)\), leaving the primitive channel and a convergent odd tail.

2. [Positive Lévy parent](2026-09-27_completed_current_levy_parent.md).
   Pole-subtracted increments of \(\xi'/\xi\) have a positive Lévy measure with continuous density \(e^{-(q+2)x}/(1-e^{-2x})\) and prime-power atoms \(\Lambda(n)n^{-q}\). An explicit independent-jump construction is supplied. The function is Bernstein but not complete Bernstein: its inverse Laplace tail has prime-power jumps. This distinguishes a valid probabilistic positivity theorem from the required Stieltjes theorem.

3. [Coherent synthesis correction](2026-09-27_coherent_synthesis_domain_correction.md).
   The common-module second-tail synthesis \(V_2\) is trace class by a summable row expansion. The first-tail map \(V_1\) is unbounded on \(\ell^2\). The sharp extension threshold is \(kq'/2>1\); \(k=3\) is needed for bounded all-ones coefficients. The Euler diagonal Schatten threshold remains unchanged. The earlier note now carries a correction.

4. [Prime-edge and finite-cutoff obstructions](2026-09-27_prime_edge_escape_and_cutoff_obstructions.md).
   Endpoint-only gluing of unbounded prime edges retains essential spectrum \([1,\infty)\); an explicit weakly null sequence proves it. A naive finite-prime replacement of the exact shifted current has an unwanted pole at \(u=-3/4\) and negative cut density near \(u=-1\). Neither construction can be promoted to the desired ordinary positive trace without the missing quotient/cancellation.

5. [Primitive tempered sewing](2026-09-27_primitive_tempered_sewing_reduction.md).
   All \(m\ge2\) prime repetitions have at most \(O(X^2)\) mass up to logarithmic length \(X\), and \(m\ge3\) has finite mass. The excited real-place ladder is tempered. The only unknown domain obstruction is the primitive-prime current minus \(e^{x/2}dx\). If that exact compensated distribution is tempered, Gaussian smoothing gives an analytic resolvent off the negative real cut and forces RH. No primitive cancellation bound is proved here.

## Reproducibility and limits

Run:

    python discovery/verify_tfd_sewing_continuation.py

Outputs: [numerical controls](2026-09-27_tfd_sewing_numerical_controls.json).

The script uses NumPy/SciPy double precision, primes through \(10^6\), and no zero data. It checks the Cayley/parity algebra, the genuine positive endpoint spectral sum with an analytic tail bound, Lévy quadrature against the digamma formula, coherent-row bounds, and robust negative densities of naive finite cutoffs. It does not certify small eigenvalue signs, infinite RH positivity, or a numerical zero-location theorem.

Recorded maximum local identity discrepancies: approximately \(4.8\times10^{-16}\) for the Cayley matrices and \(8.9\times10^{-16}\) for the Lévy checks. The analytic proofs are independent of these numerical controls.

## Exact remaining boundary

The useful next target is a zero-independent global prime–Archimedean map which:

- preserves the symmetric arithmetic observable, including its primitive odd traversals;
- cancels or quotients the unwanted interior/continuum channels before taking an infinite trace;
- sends the exact primitive discrepancy into a controlled distribution space, with all subtraction/contact terms fixed.

The new tempered-distribution theorem makes this a precise sufficient endpoint. It is still RH-strength. The proved positive local Schur complement and positive Lévy process do not supply this final map.
