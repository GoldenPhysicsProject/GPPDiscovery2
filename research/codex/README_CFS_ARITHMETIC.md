# Arithmetic causal-fermion spin-two prototype

This is an exact new **operator realization**, not an RH proof. The paired CAR and CFS context is in GPP-bridge PR #11; full derivation is kept private at
`work/codex/2026-10-16_mirrored_CFS_spin_two_full_squarefree_prime_curvature_theorem.md`.

Run `python research/codex/cfs_prime_squarefree_spin_two.py`
(requires SymPy and mpmath).

Key facts:
- A single mirrored spin-one CFS block `|v><v|-|Cv><Cv|` has **identical** two closed-chain eigenvalues for every pair, and a trivially zero CFS Lagrangian. A perfect mirror alone is insufficient.
- Two independent mirrored sectors, in spin dimension two, have Lagrangian `(|c_full|-|c_squarefree|)^2`.
- Let `Z_full(s)=zeta(s)`, `Z_sf(s)=zeta(s)/zeta(2s)`, and use normalized full-integer versus squarefree thermal wave vectors. The difference in the variance of log(n) is **exactly** `4(log(zeta))''(2sigma)>0`. Consequently their spin-two CFS **self-action is strictly positive** for small nonzero t, with leading coefficient `256[(log(zeta))''(2sigma)]^2 t^4`.
- Near sigma=1, a nontrivial off-diagonal renormalized CFS action survives after multiplying by `(sigma-1)^-4`. It uses boundary values of zeta on Re(s)=1 and the squarefree factor on Re(s)=2. It is not the completed signed Weil operator.
- The critical prime-only evaluation `(p^-1/2)` is not in ell²(primes), requiring genuine regularization/renormalization to have a bounded CFS local correlation operator.

**Open:** A zero-independent arithmetic variation principle that includes gamma, both signed pole channels, and every von Mangoldt contribution and implies the all-window signed Weil positivity. Generic CFS action positivity holds for false analogues too.

Earlier spin-one CFS "encoding" of a precomputed cone energy remains a diagnostic, not an independent variational argument. Do not claim RH/GRH, a finite-spin all-prime CFS continuum limit, or Lean verification from this code.
