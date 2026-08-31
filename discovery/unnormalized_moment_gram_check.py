#!/usr/bin/env python3
"""Numerical check of the unnormalized Cauchy--Binet moment-Gram identity.

This is discovery validation, not a proof.  It deliberately uses *unnormalized*
finite prefixes of the two-parameter number Gibbs weights.
"""

from itertools import combinations
from math import exp, log


def gram_det_from_moments(beta: float, eta: float, N: int) -> tuple[float, list[float], list[float]]:
    xs = [log(n) for n in range(1, N + 1)]
    ws = [exp(-beta * x - eta * x * x) for x in xs]
    m = [sum(w * x**k for w, x in zip(ws, xs)) for k in range(5)]
    m0, m1, m2, m3, m4 = m
    det = (
        m0 * (m2 * m4 - m3 * m3)
        - m1 * (m1 * m4 - m2 * m3)
        + m2 * (m1 * m3 - m2 * m2)
    )
    return det, xs, ws


def cauchy_binet_sum(xs: list[float], ws: list[float]) -> float:
    total = 0.0
    for i, j, k in combinations(range(len(xs)), 3):
        xi, xj, xk = xs[i], xs[j], xs[k]
        vand2 = (xi - xj) ** 2 * (xi - xk) ** 2 * (xj - xk) ** 2
        total += ws[i] * ws[j] * ws[k] * vand2
    return total


def first_arithmetic_witness(xs: list[float], ws: list[float]) -> float:
    x1, x2, x3 = xs[:3]
    return ws[0] * ws[1] * ws[2] * (x1 - x2) ** 2 * (x1 - x3) ** 2 * (x2 - x3) ** 2


def main() -> None:
    beta, eta = 0.7, 0.5
    for N in (3, 8, 15, 30):
        det, xs, ws = gram_det_from_moments(beta, eta, N)
        cb = cauchy_binet_sum(xs, ws)
        witness = first_arithmetic_witness(xs, ws)
        print(
            f"N={N:2d}  Gram={det:.16e}  CB={cb:.16e}  "
            f"abs_err={abs(det-cb):.3e}  witness={witness:.16e}  "
            f"margin={det-witness:.16e}"
        )


if __name__ == "__main__":
    main()
