#!/usr/bin/env python3
"""Finite-chain audit of the averaged causal Koszul contracting homotopy.

Checks, for a discretized causal shift model,

    d h + h d = I,

and compares ||D^{-1}|| with the rigorous abstract bound

    ||D^{-1}|| <= sqrt(2) ||h||.

This is a finite algebra audit, not a proof of the asymptotic prime estimates.
"""
from __future__ import annotations

import math
import numpy as np

I2 = np.eye(2, dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
CREATE = np.array([[0, 0], [1, 0]], dtype=complex)


def kron_all(xs):
    out = np.array([[1.0 + 0.0j]])
    for x in xs:
        out = np.kron(out, x)
    return out


def jw_create(n: int, i: int) -> np.ndarray:
    return kron_all([Z2 if j < i else CREATE if j == i else I2 for j in range(n)])


def shift_right(m: int, k: int) -> np.ndarray:
    V = np.zeros((m, m), dtype=complex)
    for x in range(k, m):
        V[x, x-k] = 1.0
    return V


def audit(m: int, shifts: list[int], qs: list[float]):
    n = len(shifts)
    creates = [jw_create(n, i) for i in range(n)]
    contractions = [c.conj().T for c in creates]
    Ts = [np.eye(m) - q * shift_right(m, k) for k, q in zip(shifts, qs)]

    dim = m * 2**n
    d = np.zeros((dim, dim), dtype=complex)
    h = np.zeros_like(d)

    for T, eps, iota in zip(Ts, creates, contractions):
        d += np.kron(T, eps)
        h += np.kron(np.linalg.inv(T) / n, iota)

    I = np.eye(dim, dtype=complex)
    contraction_error = np.linalg.norm(d @ h + h @ d - I)

    D = d + d.conj().T
    hnorm = np.linalg.norm(h, 2)
    smin = np.linalg.svd(D, compute_uv=False).min()
    dinv = 1.0 / smin

    return contraction_error, hnorm, dinv, math.sqrt(2.0) * hnorm


if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11]
    print("N contraction_error ||h|| ||D^-1|| sqrt(2)||h||")
    for n in range(2, 6):
        qs = [1.0 / math.sqrt(p) for p in primes[:n]]
        shifts = list(range(1, n + 1))
        row = audit(10, shifts, qs)
        print(
            f"{n} {row[0]:.3e} {row[1]:.9f} "
            f"{row[2]:.9f} {row[3]:.9f}"
        )
