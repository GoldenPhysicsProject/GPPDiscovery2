#!/usr/bin/env python3
"""Numerical regression audit for the exact arithmetic-QFT phase dictionary.

For an arithmetic level n with Hamiltonian energy E_n = log n,
unitary real-time evolution is exp(i t E_n) = exp(i t log n) = n^(it).
The same E_n gives Euclidean/Gibbs weight exp(-beta E_n) = n^(-beta).
Thus the principal-series Fourier mode on x=log n and the Bost-Connes style
arithmetic time evolution use the same logarithmic Hamiltonian spectrum.

This script is evidence/regression only; the equalities are elementary exact identities.
"""

from __future__ import annotations

import cmath
import math


def phase_from_energy(n: int, t: float) -> complex:
    return cmath.exp(1j * t * math.log(n))


def phase_from_complex_power(n: int, t: float) -> complex:
    return cmath.exp((1j * t) * cmath.log(n))


def gibbs_from_energy(n: int, beta: float) -> float:
    return math.exp(-beta * math.log(n))


def gibbs_power(n: int, beta: float) -> float:
    return n ** (-beta)


def run() -> None:
    ns = [2, 3, 5, 7, 11, 29]
    ts = [-3.25, -1.0, 0.0, 0.75, 4.5]
    betas = [1.1, 1.5, 2.0, 3.0]
    tol = 2e-13

    for n in ns:
        for t in ts:
            a = phase_from_energy(n, t)
            b = phase_from_complex_power(n, t)
            assert abs(a - b) < tol, (n, t, a, b)
            assert abs(abs(a) - 1.0) < tol, (n, t, abs(a))

    for n in ns:
        for beta in betas:
            a = gibbs_from_energy(n, beta)
            b = gibbs_power(n, beta)
            assert abs(a - b) < tol, (n, beta, a, b)

    # Multiplicativity of the sampled principal character.
    for m in ns[:4]:
        for n in ns[2:]:
            for t in ts:
                lhs = phase_from_energy(m * n, t)
                rhs = phase_from_energy(m, t) * phase_from_energy(n, t)
                assert abs(lhs - rhs) < 5e-13, (m, n, t, lhs, rhs)

    print("PASS: logarithmic Hamiltonian / principal-phase / Gibbs dictionary")


if __name__ == "__main__":
    run()
