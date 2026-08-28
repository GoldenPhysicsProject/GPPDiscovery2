#!/usr/bin/env python3
"""Numerical/symbolic audit for the two-parameter prime-gas Fisher determinant.

Checks, on finite support n=1..N, that
  det Cov(X,X^2)
= det E[(1,X,X^2)^T(1,X,X^2)]
= sum_{i<j<k} p_i p_j p_k Vandermonde(x_i,x_j,x_k)^2.

This is discovery code only; the theorem target belongs in GPPVerify2.
"""

from itertools import combinations
import math


def audit(beta: float = 2.0, eta: float = 0.15, N: int = 40) -> None:
    ns = list(range(1, N + 1))
    xs = [math.log(n) for n in ns]
    ws = [math.exp(-beta * x - eta * x * x) for x in xs]
    Z = sum(ws)
    ps = [w / Z for w in ws]

    mu = {k: sum(p * (x ** k) for p, x in zip(ps, xs)) for k in range(1, 5)}
    var_x = mu[2] - mu[1] ** 2
    cov_x_x2 = mu[3] - mu[1] * mu[2]
    var_x2 = mu[4] - mu[2] ** 2
    det_cov = var_x * var_x2 - cov_x_x2 ** 2

    # det of [[1,m1,m2],[m1,m2,m3],[m2,m3,m4]]
    a, b, c, d = mu[1], mu[2], mu[3], mu[4]
    det_moment = (b * d - c * c) - a * (a * d - b * c) + b * (a * c - b * b)

    vandermonde_sum = 0.0
    for i, j, k in combinations(range(len(xs)), 3):
        xi, xj, xk = xs[i], xs[j], xs[k]
        v = (xi - xj) * (xi - xk) * (xj - xk)
        vandermonde_sum += ps[i] * ps[j] * ps[k] * v * v

    print(f"beta={beta} eta={eta} N={N}")
    print(f"Z={Z:.17g}")
    print(f"Var(X)={var_x:.17g}")
    print(f"Cov(X,X^2)={cov_x_x2:.17g}")
    print(f"Var(X^2)={var_x2:.17g}")
    print(f"det covariance={det_cov:.17g}")
    print(f"det moment Gram={det_moment:.17g}")
    print(f"Vandermonde sum={vandermonde_sum:.17g}")
    print(f"|cov-moment|={abs(det_cov-det_moment):.3e}")
    print(f"|cov-vander|={abs(det_cov-vandermonde_sum):.3e}")
    assert det_cov > 0.0
    assert abs(det_cov - det_moment) < 1e-12
    assert abs(det_cov - vandermonde_sum) < 1e-12


if __name__ == "__main__":
    audit()
