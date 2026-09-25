#!/usr/bin/env python3
"""Finite-matrix audit of the causal Koszul contracting-homotopy gap.

Checks:
  d h + h d = I
for
  d = sum_p T_p tensor epsilon_p,
  h = sum_p c_p T_p^{-1} tensor iota_p,
with c_p proportional to (1-|q_p|)^2.

Also compares the actual ||h|| and smallest singular value of D=d+d^*
against the analytic bounds
  ||h|| <= 1/sqrt(m),
  s_min(D) >= sqrt(m/2),
where m=sum_p (1-|q_p|)^2.
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


def audit(m: int, shifts: list[int], qs: list[complex]):
    n = len(shifts)
    creates = [jw_create(n, i) for i in range(n)]
    annih = [c.conj().T for c in creates]
    eye_h = np.eye(m, dtype=complex)

    Ts = []
    invs = []
    deltas = []
    for k, q in zip(shifts, qs):
        T = eye_h - q * shift_right(m, k)
        Ts.append(T)
        invs.append(np.linalg.inv(T))
        deltas.append(1.0 - abs(q))

    mass = sum(delta * delta for delta in deltas)
    coeffs = [delta * delta / mass for delta in deltas]

    dim = m * 2**n
    d = np.zeros((dim, dim), dtype=complex)
    h = np.zeros((dim, dim), dtype=complex)

    for T, Tinv, c, eps, iota in zip(Ts, invs, coeffs, creates, annih):
        d += np.kron(T, eps)
        h += c * np.kron(Tinv, iota)

    homotopy_error = np.linalg.norm(d @ h + h @ d - np.eye(dim), 2)

    D = d + d.conj().T
    h_norm = np.linalg.norm(h, 2)
    h_bound = 1.0 / math.sqrt(mass)
    d_min = np.linalg.svd(D, compute_uv=False).min()
    d_lower = math.sqrt(mass / 2.0)

    return homotopy_error, h_norm, h_bound, d_min, d_lower, mass


if __name__ == "__main__":
    cases = [
        ([2], [2 ** -0.5]),
        ([2, 3], [2 ** -0.5, 3 ** -0.5]),
        ([2, 3, 5], [2 ** -0.5, 3 ** -0.5, 5 ** -0.5]),
        (
            [2, 3, 5],
            [
                2 ** -0.5 * np.exp(0.8j),
                3 ** -0.5 * np.exp(-1.3j),
                5 ** -0.5 * np.exp(2.0j),
            ],
        ),
    ]

    print("channels homotopy_err ||h|| h_bound smin(D) D_lower")
    for shifts, qs in cases:
        row = audit(18, shifts, qs)
        print(
            len(shifts),
            *(f"{x:.12g}" for x in row[:5]),
        )
        assert row[0] < 1e-10
        assert row[1] <= row[2] * (1 + 1e-10)
        assert row[3] >= row[4] * (1 - 1e-10)

    print("PASS")
