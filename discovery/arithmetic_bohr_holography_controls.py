#!/usr/bin/env python3
"""Numerical controls for the arithmetic Hardy/Bohr/TFD synthesis.

No zeta-zero data are used. The exact proofs live in
research/2026-09-27_arithmetic_hardy_ads2_bohr_tfd_vacuum.md.
These controls only illustrate:
  * long-time mean orthogonality of n^{-it};
  * approach of the finite Gram matrix to the identity;
  * weak escape of the normalized critical Gibbs/TFD vector.
"""

from __future__ import annotations

import json
import math
import numpy as np
import mpmath as mp


def mean_gram(N: int, T: float) -> np.ndarray:
    n = np.arange(1, N + 1, dtype=float)
    w = np.log(n[:, None] / n[None, :])
    G = np.ones_like(w)
    mask = np.abs(w) > 1e-15
    G[mask] = np.sin(T * w[mask]) / (T * w[mask])
    return G


def fixed_prefix_probability(beta: float, K: int) -> float:
    """Mass on n<=K under P_beta(n)=n^{-beta}/zeta(beta)."""
    num = mp.fsum(mp.power(n, -beta) for n in range(1, K + 1))
    return float(num / mp.zeta(beta))


def main() -> None:
    mp.mp.dps = 50
    gram = []
    for T in (10.0, 100.0, 1000.0, 10000.0):
        G = mean_gram(20, T)
        off = G - np.eye(20)
        ev = np.linalg.eigvalsh(G)
        gram.append(
            {
                "T": T,
                "max_abs_offdiag": float(np.max(np.abs(off))),
                "min_eigenvalue": float(ev[0]),
                "max_eigenvalue": float(ev[-1]),
            }
        )

    escape = []
    for beta in (1.5, 1.2, 1.1, 1.05, 1.02, 1.01):
        escape.append(
            {
                "beta": beta,
                "mass_n_le_10": fixed_prefix_probability(beta, 10),
                "mass_n_le_100": fixed_prefix_probability(beta, 100),
            }
        )

    out = {
        "uses_zero_data": False,
        "gram_N": 20,
        "mean_orthogonality": gram,
        "critical_weak_escape": escape,
        "exact_identity": (
            "(2T)^-1 int_-T^T n^(-it)m^(it)dt = "
            "sin(T log(m/n))/(T log(m/n)) for m!=n"
        ),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
