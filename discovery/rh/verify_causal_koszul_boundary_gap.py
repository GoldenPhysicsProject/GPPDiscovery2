#!/usr/bin/env python3
"""Audit the corrected causal Koszul lower bound.

Computes
    g(X)=pi(X)-2 S1(X)+2 S2(X)-S1(X)^2,
with S1=sum_{p<=X} p^(-1/2), S2=sum_{p<=X} p^(-1).

Also verifies on small finite chains the exact operator-valued Hodge-square
decomposition with the prime-prime causal boundary commutator.
"""
from __future__ import annotations

import math
import numpy as np


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0:2] = b"\x00\x00"
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def scalar_bound(X: int) -> tuple[int, float, float, float, float]:
    ps = primes_upto(X)
    s1 = sum(p ** -0.5 for p in ps)
    s2 = sum(1.0 / p for p in ps)
    mass = sum((1.0 - p ** -0.5) ** 2 for p in ps)
    boundary = s1 * s1 - s2
    gap = mass - boundary
    return len(ps), s1, mass, boundary, gap


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


def finite_chain_audit(m: int, shifts: list[int], qs: list[complex]):
    n = len(shifts)
    creates = [jw_create(n, i) for i in range(n)]
    annih = [c.conj().T for c in creates]
    eye_h = np.eye(m, dtype=complex)
    Ts = [eye_h - q * shift_right(m, k) for k, q in zip(shifts, qs)]

    dim = m * (2 ** n)
    d = np.zeros((dim, dim), dtype=complex)
    for T, c in zip(Ts, creates):
        d += np.kron(T, c)
    D = d + d.conj().T

    diag = np.zeros_like(D)
    boundary = np.zeros_like(D)
    for i, T in enumerate(Ts):
        diag += np.kron(T @ T.conj().T, creates[i] @ annih[i])
        diag += np.kron(T.conj().T @ T, annih[i] @ creates[i])

    for i, Ti in enumerate(Ts):
        for j, Tj in enumerate(Ts):
            if i == j:
                continue
            comm = Ti @ Tj.conj().T - Tj.conj().T @ Ti
            boundary += np.kron(comm, creates[i] @ annih[j])

    D2 = D @ D
    identity_error = np.linalg.norm(D2 - diag - boundary)
    comm_max = 0.0
    for i, Ti in enumerate(Ts):
        for j, Tj in enumerate(Ts):
            if i == j:
                continue
            qbound = abs(qs[i] * qs[j])
            comm = Ti @ Tj.conj().T - Tj.conj().T @ Ti
            comm_max = max(comm_max, np.linalg.norm(comm, 2) - qbound)

    eigmin = np.linalg.eigvalsh(D2).min()
    mass_lower = sum((1.0 - abs(q)) ** 2 for q in qs)
    boundary_triangle = sum(
        abs(qs[i] * qs[j])
        for i in range(n) for j in range(n) if i != j
    )
    return identity_error, comm_max, eigmin, mass_lower, boundary_triangle


if __name__ == "__main__":
    print("X pi(X) S1 mass boundary gap")
    for X in [100, 1000, 10_000, 100_000, 1_000_000]:
        n, s1, mass, boundary, gap = scalar_bound(X)
        print(f"{X:>8} {n:>7} {s1:12.6f} {mass:14.6f} {boundary:14.6f} {gap:14.6f}")

    print("\nfinite-chain decomposition audit")
    row = finite_chain_audit(
        24,
        [2, 3, 5],
        [2 ** -0.5, 3 ** -0.5, 5 ** -0.5],
    )
    print("identity_error =", row[0])
    print("max(comm_norm - |q_i q_j|) =", row[1])
    print("lambda_min(D^2) =", row[2])
    print("diagonal mass lower =", row[3])
    print("boundary triangle bound =", row[4])
