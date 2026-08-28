"""Exact rational audit of the finite-support Fisher Cauchy--Binet identity.

For normalized weights p_i and support x_i this checks

  det Cov(X, X^2)
    = sum_{i<j<k} p_i p_j p_k Delta(i,j,k)^2
    = (1/6) sum_{i,j,k} p_i p_j p_k Delta(i,j,k)^2,

where Delta(i,j,k)=(x_i-x_j)(x_i-x_k)(x_j-x_k).

The second equality is the exact bridge to the general ordered-energy object now
formalized in Verify2: repeated indices vanish and each unordered distinct triple
occurs in all six permutations.  All arithmetic here uses fractions.Fraction;
there is no floating-point tolerance.  This remains executable discovery evidence,
not a replacement for the arbitrary-finite Lean Cauchy--Binet proof.
"""

from fractions import Fraction
from itertools import combinations, product


def delta(x, i, j, k):
    return (x[i] - x[j]) * (x[i] - x[k]) * (x[j] - x[k])


def fisher_quantities(weights_raw, support):
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

    unordered = Fraction(0)
    for i, j, k in combinations(range(len(x)), 3):
        unordered += p[i] * p[j] * p[k] * delta(x, i, j, k) ** 2

    ordered = Fraction(0)
    for i, j, k in product(range(len(x)), repeat=3):
        ordered += p[i] * p[j] * p[k] * delta(x, i, j, k) ** 2

    return det_cov, unordered, ordered


CASES = [
    ([1, 2, 3], [-2, 0, 3]),
    ([1, 2, 3, 4], [-2, -1, 2, 5]),
    ([1, 2, 3, 4, 5], [-2, -1, 0, 2, 5]),
    ([1, 1, 2, 3, 5, 8], [-3, -2, -1, 1, 4, 7]),
    ([2, 3, 5, 7, 11, 13, 17], [-4, -3, -1, 0, 2, 5, 9]),
    ([1, 2, 4, 8, 16, 32, 64, 128], [-5, -4, -2, -1, 1, 3, 6, 10]),
    # Degenerate support: determinant and all Vandermonde energies vanish.
    ([1, 2, 3, 4], [7, 7, 7, 7]),
    # Zero-weight points do not affect the identity.
    ([1, 0, 3, 0, 5], [-9, -2, 0, 4, 8]),
]


if __name__ == "__main__":
    for weights, support in CASES:
        det_cov, unordered, ordered = fisher_quantities(weights, support)
        assert det_cov == unordered
        assert ordered == 6 * unordered
        assert ordered == 6 * det_cov
        assert det_cov >= 0
        print(
            f"N={len(weights)} det={det_cov} "
            f"unordered_match={det_cov == unordered} "
            f"ordered_sixfold={ordered == 6 * det_cov}"
        )
