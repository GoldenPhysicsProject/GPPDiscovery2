"""Executable check for the two-parameter confined number-gas Fisher geometry.

Weights:
    w_n(beta, eta) = exp(-beta L_n - eta L_n^2),  L_n = log n.

For eta > 0 the infinite partition sum converges for every real beta.  The
log-partition Hessian is expected to be the covariance matrix of the sufficient
statistics (L, L^2):

    d_bb log Z = Var(L)
    d_be log Z = Cov(L, L^2)
    d_ee log Z = Var(L^2).

This script checks the moment formulas numerically on finite truncations and
reports the determinant Var(L) Var(L^2) - Cov(L,L^2)^2.  It is discovery code,
not a proof; the finite-truncation identities themselves are algebraic and the
countable theorem requires justified differentiation under the convergent sum.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Geometry:
    Z: float
    mean_L: float
    mean_L2: float
    var_L: float
    cov_L_L2: float
    var_L2: float
    det: float


def confined_geometry(beta: float, eta: float, N: int = 20_000) -> Geometry:
    if eta <= 0:
        raise ValueError("eta must be positive for the all-beta confined ensemble")

    rows: list[tuple[float, float]] = []
    for n in range(1, N + 1):
        L = math.log(n)
        w = math.exp(-beta * L - eta * L * L)
        rows.append((L, w))

    Z = sum(w for _, w in rows)
    m1 = sum(L * w for L, w in rows) / Z
    m2 = sum(L**2 * w for L, w in rows) / Z
    m3 = sum(L**3 * w for L, w in rows) / Z
    m4 = sum(L**4 * w for L, w in rows) / Z

    var_L = m2 - m1 * m1
    cov = m3 - m1 * m2
    var_L2 = m4 - m2 * m2
    det = var_L * var_L2 - cov * cov
    return Geometry(Z, m1, m2, var_L, cov, var_L2, det)


def main() -> None:
    samples = [
        (0.0, 0.2),
        (1.0, 0.1),
        (-3.0, 0.4),
        (2.0, 0.05),
    ]
    for beta, eta in samples:
        g = confined_geometry(beta, eta, N=5000)
        print(
            f"beta={beta: .3f} eta={eta: .3f} "
            f"Z={g.Z:.12g} varL={g.var_L:.12g} "
            f"cov={g.cov_L_L2:.12g} varL2={g.var_L2:.12g} "
            f"det={g.det:.12g}"
        )
        if not (g.det > 0.0):
            raise AssertionError("finite-truncation Fisher determinant is not positive")


if __name__ == "__main__":
    main()
