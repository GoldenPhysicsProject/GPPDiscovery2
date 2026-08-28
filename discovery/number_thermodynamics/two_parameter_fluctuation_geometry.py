#!/usr/bin/env python3
"""Numerical and exact audits for the two-parameter prime-gas Fisher determinant.

Checks on finite support that
  det Cov(X,X^2)
= det E[(1,X,X^2)^T(1,X,X^2)]
= sum_{i<j<k} p_i p_j p_k Vandermonde(x_i,x_j,x_k)^2.

The floating Gibbs audit probes the intended log-energy family.  The rational
five-point audit is exact and specifically checks the first support size beyond
the four-point Lean theorem without any floating-point tolerance.

This is discovery code only; the general finite theorem target belongs in
GPPVerify2.
"""

from fractions import Fraction
from itertools import combinations
import math


def covariance_det(ps, xs):
    mu = {k: sum(p * (x ** k) for p, x in zip(ps, xs)) for k in range(1, 5)}
    return (
        (mu[2] - mu[1] ** 2) * (mu[4] - mu[2] ** 2)
        - (mu[3] - mu[1] * mu[2]) ** 2
    ), mu


def vandermonde_sum(ps, xs):
    total = 0
    for i, j, k in combinations(range(len(xs)), 3):
        xi, xj, xk = xs[i], xs[j], xs[k]
        v = (xi - xj) * (xi - xk) * (xj - xk)
        total += ps[i] * ps[j] * ps[k] * v * v
    return total


def audit_exact_five_point() -> None:
    """Exact Q-arithmetic check at five support points."""
    xs = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(2), Fraction(5)]
    ps = [
        Fraction(1, 15),
        Fraction(2, 15),
        Fraction(3, 15),
        Fraction(4, 15),
        Fraction(5, 15),
    ]
    assert sum(ps) == 1

    det_cov, mu = covariance_det(ps, xs)
    det_moment = (
        (mu[2] * mu[4] - mu[3] ** 2)
        - mu[1] * (mu[1] * mu[4] - mu[2] * mu[3])
        + mu[2] * (mu[1] * mu[3] - mu[2] ** 2)
    )
    v_sum = vandermonde_sum(ps, xs)

    target = Fraction(145004, 1125)
    print("exact five-point audit")
    print(f"det covariance = {det_cov}")
    print(f"det moment Gram = {det_moment}")
    print(f"Vandermonde sum = {v_sum}")
    assert det_cov == target
    assert det_cov == det_moment
    assert det_cov == v_sum
    assert det_cov > 0


def audit(beta: float = 2.0, eta: float = 0.15, N: int = 40) -> None:
    ns = list(range(1, N + 1))
    xs = [math.log(n) for n in ns]
    ws = [math.exp(-beta * x - eta * x * x) for x in xs]
    Z = sum(ws)
    ps = [w / Z for w in ws]

    det_cov, mu = covariance_det(ps, xs)
    var_x = mu[2] - mu[1] ** 2
    cov_x_x2 = mu[3] - mu[1] * mu[2]
    var_x2 = mu[4] - mu[2] ** 2

    # det of [[1,m1,m2],[m1,m2,m3],[m2,m3,m4]]
    a, b, c, d = mu[1], mu[2], mu[3], mu[4]
    det_moment = (b * d - c * c) - a * (a * d - b * c) + b * (a * c - b * b)
    v_sum = vandermonde_sum(ps, xs)

    print(f"beta={beta} eta={eta} N={N}")
    print(f"Z={Z:.17g}")
    print(f"Var(X)={var_x:.17g}")
    print(f"Cov(X,X^2)={cov_x_x2:.17g}")
    print(f"Var(X^2)={var_x2:.17g}")
    print(f"det covariance={det_cov:.17g}")
    print(f"det moment Gram={det_moment:.17g}")
    print(f"Vandermonde sum={v_sum:.17g}")
    print(f"|cov-moment|={abs(det_cov-det_moment):.3e}")
    print(f"|cov-vander|={abs(det_cov-v_sum):.3e}")
    assert det_cov > 0.0
    assert abs(det_cov - det_moment) < 1e-12
    assert abs(det_cov - v_sum) < 1e-12


if __name__ == "__main__":
    audit_exact_five_point()
    audit()
