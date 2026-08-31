#!/usr/bin/env python3
"""Numerical probe for the genuine two-parameter zeta Gibbs family.

Family:
    Z(beta, eta) = sum_{n>=1} exp(-beta log n - eta (log n)^2).

Exact analytic domain (proved in the companion discovery note):
  * eta > 0: convergent for every real beta;
  * eta = 0: convergent iff beta > 1;
  * eta < 0: divergent because the summand does not tend to zero.

On the open domain eta > 0, Hess(log Z) is the covariance matrix of
X=log n and X^2. This script checks the moment formulas and positivity of its
determinant on representative points. It is evidence/reproducibility support,
not the proof of positivity.
"""

from __future__ import annotations

import math


def truncated_geometry(beta: float, eta: float, nmax: int = 20000):
    z = 0.0
    raw = [0.0] * 5
    for n in range(1, nmax + 1):
        x = math.log(n)
        w = math.exp(-beta * x - eta * x * x)
        z += w
        for k in range(1, 5):
            raw[k] += w * x**k
    moments = [v / z for v in raw]
    m1, m2, m3, m4 = moments[1:5]
    g11 = m2 - m1 * m1
    g12 = m3 - m1 * m2
    g22 = m4 - m2 * m2
    det = g11 * g22 - g12 * g12
    return z, g11, g12, g22, det


def main() -> None:
    samples = [(2.0, 0.0), (0.0, 0.2), (-4.0, 0.5), (2.0, 0.1)]
    for beta, eta in samples:
        z, g11, g12, g22, det = truncated_geometry(beta, eta)
        print(
            f"beta={beta: .3f} eta={eta: .3f} Z_N={z:.12g} "
            f"g11={g11:.12g} g12={g12:.12g} g22={g22:.12g} det={det:.12g}"
        )
        if det <= 0.0:
            raise RuntimeError("unexpected non-positive truncated Fisher determinant")


if __name__ == "__main__":
    main()
