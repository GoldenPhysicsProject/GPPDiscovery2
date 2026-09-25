#!/usr/bin/env python3
"""Finite-matrix audit of the causal Koszul curvature identity.

Uses powers of one nilpotent unilateral shift as exact discrete causal shifts.
These shifts commute, while their adjoints do not doubly commute.  The script
checks

D^2 = diagonal Hodge block + sum_{p!=q}[T_p,T_q^*] tensor eps_p iota_q

and compares the true smallest eigenvalue with the analytic lower bound

sum_p (1-|r_p|)^2 - sum_{p!=q}|r_p r_q|.

This is an algebra audit only; it does not use zeta zeros.
"""

from __future__ import annotations
import numpy as np

I2 = np.eye(2, dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
CREATE = np.array([[0, 0], [1, 0]], dtype=complex)
ANNIHILATE = CREATE.conj().T


def kron_all(xs):
    out = np.array([[1.0 + 0.0j]])
    for x in xs:
        out = np.kron(out, x)
    return out


def jw_create(n: int, i: int) -> np.ndarray:
    return kron_all([Z2 if j < i else CREATE if j == i else I2 for j in range(n)])


def jw_annihilate(n: int, i: int) -> np.ndarray:
    return jw_create(n, i).conj().T


def right_shift(dim: int, lag: int) -> np.ndarray:
    v = np.zeros((dim, dim), dtype=complex)
    if lag < dim:
        for j in range(dim - lag):
            v[j + lag, j] = 1.0
    return v


def audit(
    primes=(2, 3, 5, 7),
    lags=(1, 2, 3, 4),
    dim_h=18,
    t=1.371,
):
    n = len(primes)
    assert len(lags) == n
    hs = [right_shift(dim_h, lag) for lag in lags]
    eps = [jw_create(n, i) for i in range(n)]
    iota = [jw_annihilate(n, i) for i in range(n)]

    ih = np.eye(dim_h, dtype=complex)
    iferm = np.eye(2**n, dtype=complex)

    r = np.array([p ** (-0.5 - 1j * t) for p in primes], dtype=complex)
    T = [ih - r[i] * hs[i] for i in range(n)]

    d = np.zeros((dim_h * 2**n, dim_h * 2**n), dtype=complex)
    for i in range(n):
        d += np.kron(T[i], eps[i])
    D = d + d.conj().T
    D2 = D @ D

    diag = np.zeros_like(D2)
    for i in range(n):
        diag += np.kron(T[i].conj().T @ T[i], iota[i] @ eps[i])
        diag += np.kron(T[i] @ T[i].conj().T, eps[i] @ iota[i])

    curvature = np.zeros_like(D2)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            comm = T[i] @ T[j].conj().T - T[j].conj().T @ T[i]
            curvature += np.kron(comm, eps[i] @ iota[j])

    identity_error = np.linalg.norm(D2 - diag - curvature)
    shift_comm_max = 0.0
    mixed_comm_max = 0.0
    for i in range(n):
        for j in range(n):
            shift_comm_max = max(
                shift_comm_max,
                np.linalg.norm(hs[i] @ hs[j] - hs[j] @ hs[i]),
            )
            mixed_comm_max = max(
                mixed_comm_max,
                np.linalg.norm(
                    hs[i] @ hs[j].conj().T - hs[j].conj().T @ hs[i]
                ),
            )

    diag_floor = float(np.sum((1.0 - np.abs(r)) ** 2))
    curvature_bound = float(
        np.sum(
            [abs(r[i] * r[j]) for i in range(n) for j in range(n) if i != j]
        )
    )
    analytic_floor = diag_floor - curvature_bound

    eig = np.linalg.eigvalsh((D2 + D2.conj().T) / 2)
    true_floor = float(np.min(eig).real)

    print("primes:", primes)
    print("lags:", lags)
    print("causal shift commutator max ||[V_i,V_j]|| =", shift_comm_max)
    print("mixed adjoint commutator max ||[V_i,V_j^*]|| =", mixed_comm_max)
    print("Hodge identity residual ||D^2-diag-curvature|| =", identity_error)
    print("diagonal lower bound =", diag_floor)
    print("curvature triangle bound =", curvature_bound)
    print("analytic D^2 floor =", analytic_floor)
    print("true min eigenvalue(D^2) =", true_floor)


if __name__ == "__main__":
    audit()
