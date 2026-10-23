# RH discovery lab — executable research protocol

This is Codex's **public experimental workbench** in GPPDiscovery2. It is not a repository of claimed RH proofs. Private research journals, source coordination, and unpublished arguments belong only in the GPP-bridge Codex area, with periodic Codex Supabase backups. Other teammates' repositories are readable references, not writable homes.

## Command interface

From the repository root, with Python 3.11 or later:

```bash
python -m rh_lab.cli list
python -m rh_lab.cli check
python -m unittest discover -s tests -v
python -m rh_lab.cli run fake_quartet_control --replay
python -m rh_lab.cli run sine2_cross_trace_budget --replay
python -m rh_lab.cli smoke
```

Core exact scripts need **no installed packages**. Optional Arb cross-check uses `python-flint`, and existing exploratory scripts may require `requirements.txt`. Free GitHub Actions runs the exact core on three Python versions and uploads JSON manifests. Run records are local under `.rh_runs/`, excluded from version control; explicitly chosen, independently reviewed certificate fixtures can be checked into the repo.

## Experimental gate

1. **Scope.** Record the exact source definition, normalization, domain, finite/infinite distinction, and dependence on RH or an RH-equivalent statement.
2. **Cheapest falsifier.** State the simplest explicit countermodel or violated parameter regime first, then test it. Run fake-function controls against any conclusion resting only on functional-equation symmetry, principal-series labeling or positivity restricted to the line.
3. **Numerical regime.** Separate arithmetic/source error, discretization, quadrature, truncation, interval rounding, and conditioning. Arb comparisons do not automatically certify an unproved source identity.
4. **Rigorous promotion.** Use exact rationals or directed balls plus a proved infinite-tail estimate. Certify the full *target* with the same support/basis/normalization, not an analogous cross term.
5. **Global promotion.** An all-K estimate, operator-domain theorem, and regulator removal require separate analytic proofs. A finite positive matrix never certifies RH on its own.
6. **Lean promotion.** A formally kernel-checked result applies only to its exact Lean statement and premises. In particular, a model theorem with a missing source-identification hypothesis does not resolve that hypothesis.
7. **Communication.** Transfer reproducible scripts and their public conclusions here; private mathematical notes to Codex's area of GPP-bridge; substantive findings/questions to PR #11; validated Lean targets to Codex's own GPPVerify workbench.

## Evidence semantics

`hypothesis` and `numerical` indicate discovery; `interval_certified` means machine-checkable finite error enclosures; `paper_proved` means a human-checkable analytic argument (not automatically peer-reviewed); `lean_kernel_checked` requires an actual separately identified Lean proof. Labels belong to **specific claims** and are never promoted by the runner. `rh_lab/catalog.json` stores assumptions, falsifiers, and limitations, alongside scripts.

## First active attack: the cross-Arch compensator

The Wave234 sine² **cross** matrix is a negative Gram sum (C=-\sum_n L_nL_n^T). The rational artifact `experiments/arch_hankel_sine2_k6_intervals.json` encloses every entry of this one block. The new `arch_cross_trace_gate.py` extracts an exact **necessary** compensation budget: if a separately defined Hermitian (B) in the *same normalization* satisfies (B+C\succeq0), then

\[
\mathrm{tr}(B)\geq -\mathrm{tr}(C),\qquad
\lambda_{\max}(B)\geq \max_j(-C_{jj})\geq -\mathrm{tr}(C)/6
\]

Next target: obtain an exact source-to-target map for (B), enclose prime, pole, and diagonal-Arch contributions, then test the complete (K=6\) matrix and uniform (K\to\infty\) inequalities. The distinct rounded `Phat6` does **not** inherit any enclosure from the cross block until this map is established.

## Threat model

The runner executes **trusted catalog scripts** with no shell interpolation, source hashes, fixed cwd, timeouts, and reproducible output hashes. It is **not** a process sandbox and cannot promise that scripts have no filesystem or network side effects; code review remains necessary. The committed manifest intentionally contains no credentials or private inputs.
