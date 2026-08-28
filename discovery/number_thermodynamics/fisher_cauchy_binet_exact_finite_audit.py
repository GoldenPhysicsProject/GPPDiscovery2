"""Exact rational audit of the finite-support Fisher Cauchy--Binet identity.

This is discovery evidence, not a proof of the general theorem.  For normalized
weights p_i and support x_i it checks

  det Cov(X, X^2)
    = sum_{i<j<k} p_i p_j p_k
        ((x_i-x_j)(x_i-x_k)(x_j-x_k))^2

using fractions.Fraction only, with no floating-point tolerance.
"""

from fractions import Fraction
from itertools import combinations


def fisher_det_and_vandermonde_sum(weights_raw, support):
    total = sum(weights_raw)
    if total == 0:
        raise ValueError("weights must have nonzero total")
    if len(weights_raw) != len(support):
        raise ValueError("weights and support must have equal length")

    p = [Fraction(w, total) for w in weights_raw]
    x = [Fraction(v) for v in support]

    m1 = sum(pi * xi for pi, xi in zip(p, x))
    m2 = sum(pi * xi**2 for pi, xi in zip(p, x))
    m3 = sum(pi * xi**3 for pi, xi in zip(p, x))
    m4 = sum(pi * xi**4 for pi, xi in zip(p, x))

    det_cov = (m2 - m1**2) * (m4 - m2**2) - (m3 - m1 * m2) ** 2

    cb = Fraction(0)
    for i, j, k in combinations(range(len(x)), 3):
        delta = (x[i] - x[j]) * (x[i] - x[k]) * (x[j] - x[k])
        cb += p[i] * p[j] * p[k] * delta**2

    return det_cov, cb


CASES = [
    ([1, 2, 3], [-2, 0, 3]),
    ([1, 2, 3, 4], [-2, -1, 2, 5]),
    ([1, 2, 3, 4, 5], [-2, -1, 0, 2, 5]),
    ([1, 1, 2, 3, 5, 8], [-3, -2, -1, 1, 4, 7]),
    ([2, 3, 5, 7, 11, 13, 17], [-4, -3, -1, 0, 2, 5, 9]),
    ([1, 2, 4, 8, 16, 32, 64, 128], [-5, -4, -2, -1, 1, 3, 6, 10]),
]


if __name__ == "__main__":
    for weights, support in CASES:
        lhs, rhs = fisher_det_and_vandermonde_sum(weights, support)
        assert lhs == rhs
        print(f"N={len(weights)} det={lhs} exact_match={lhs == rhs}")
