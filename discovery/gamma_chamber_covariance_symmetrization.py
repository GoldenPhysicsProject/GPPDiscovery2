#!/usr/bin/env python3
"""Exact finite-measure covariance symmetrization audit.

For positive weights w_i, observables g_i and radial variables y_i,

  2 W^2 Cov_w(g,y)
    = sum_{i,j} w_i w_j (g_i-g_j)(y_i-y_j),

where W=sum_i w_i and Cov_w uses the normalized weighted expectation.
If g is nondecreasing in y, every summand on the right is nonnegative.

This is the discrete algebraic spine for the measure-theoretic iid-copy
identity needed in continuous Gamma-chamber ordering.  It does not assume
a Gamma density and does not claim the continuum Fubini step.
"""
from fractions import Fraction
from itertools import product


def check(weights, ys, gs):
    w = list(map(Fraction, weights))
    y = list(map(Fraction, ys))
    g = list(map(Fraction, gs))
    assert len(w) == len(y) == len(g) and w
    W = sum(w)
    assert W != 0

    s_g = sum(wi * gi for wi, gi in zip(w, g))
    s_y = sum(wi * yi for wi, yi in zip(w, y))
    s_gy = sum(wi * gi * yi for wi, gi, yi in zip(w, g, y))

    lhs = 2 * (W * s_gy - s_g * s_y)
    rhs = sum(
        w[i] * w[j] * (g[i] - g[j]) * (y[i] - y[j])
        for i, j in product(range(len(w)), repeat=2)
    )
    assert lhs == rhs
    return lhs, rhs


def monotone_pairwise_nonnegative(weights, ys, gs):
    w = list(map(Fraction, weights))
    y = list(map(Fraction, ys))
    g = list(map(Fraction, gs))
    for wi in w:
        assert wi >= 0
    for i, j in product(range(len(w)), repeat=2):
        assert (g[i] - g[j]) * (y[i] - y[j]) >= 0
    lhs, rhs = check(w, y, g)
    assert rhs >= 0
    assert lhs >= 0
    return lhs


if __name__ == "__main__":
    # Nonuniform exact-rational audit with strictly increasing radial observable.
    weights = [1, 2, 5, 7]
    ys = [0, Fraction(1, 3), 2, 5]
    gs = [1, Fraction(7, 6), 4, 26]  # increasing in y
    lhs, rhs = check(weights, ys, gs)
    assert lhs == rhs
    assert monotone_pairwise_nonnegative(weights, ys, gs) > 0

    # Constant observable: covariance vanishes identically.
    zero_lhs, zero_rhs = check([1, 3, 4], [0, 1, 9], [2, 2, 2])
    assert zero_lhs == zero_rhs == 0

    print("finite covariance symmetrization: PASS")
    print(f"strict monotone audit numerator = {lhs}")
