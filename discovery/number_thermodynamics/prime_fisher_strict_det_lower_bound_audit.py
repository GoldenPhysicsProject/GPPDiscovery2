"""Exact three-state lower bound for the countable prime-Fisher determinant.

Codex/GPT discovery artifact.  This strengthens the currently formalized countable
nonnegativity target by isolating an explicit positive contribution from n=2,4,8.

For a normalized countable law p_n on distinct x_n, the covariance determinant of
(X, X^2) has the Cauchy--Binet expansion

    det g = sum_{i<j<k} p_i p_j p_k
            ((x_i-x_j)(x_i-x_k)(x_j-x_k))^2.

For the arithmetic Fisher weight

    w_beta(n) = Lambda(n) log(n) exp(-beta log n),

on beta>1, write m0=sum_n w_beta(n), p_n=w_beta(n)/m0.  At n=2^j,

    Lambda(2^j)=log 2,
    log(2^j)=j log 2,
    w_beta(2^j)=j (log 2)^2 2^{-j beta}.

The single triple (2,4,8), corresponding to j=1,2,3, therefore yields

    Vandermonde^2 = [(-L)(-2L)(-L)]^2 = 4 L^6,
    w_2 w_4 w_8 = 6 L^6 2^{-6 beta},

hence

    det g >= 24 (log 2)^12 2^{-6 beta} / m0^3 > 0.

No RH implication is asserted.  This is ordinary strict Fisher positivity for the
actual countable von-Mangoldt weight, with an explicit quantitative certificate.
"""

from __future__ import annotations

import sympy as sp


beta, L, m0 = sp.symbols("beta L m0", positive=True, real=True)


def fisher_weight_power_two(j: int):
    return sp.Integer(j) * L**2 * 2 ** (-sp.Integer(j) * beta)


def vandermonde_sq(xs):
    x1, x2, x3 = xs
    return sp.expand(((x1 - x2) * (x1 - x3) * (x2 - x3)) ** 2)


def run() -> None:
    xs = [L, 2 * L, 3 * L]
    vand = sp.factor(vandermonde_sq(xs))
    assert sp.simplify(vand - 4 * L**6) == 0

    ws = [fisher_weight_power_two(j) for j in (1, 2, 3)]
    wprod = sp.factor(sp.prod(ws))
    target_wprod = 6 * L**6 * 2 ** (-6 * beta)
    assert sp.simplify(wprod / target_wprod - 1) == 0

    triple_term = sp.factor(vand * wprod / m0**3)
    target = 24 * L**12 * 2 ** (-6 * beta) / m0**3
    assert sp.simplify(triple_term / target - 1) == 0

    # Independent determinant check for a probability law supported exactly on
    # x=L,2L,3L.  The 3-point covariance determinant must equal the lone
    # Cauchy--Binet term p1*p2*p3*Vandermonde^2.
    p1, p2 = sp.symbols("p1 p2", positive=True, real=True)
    p3 = 1 - p1 - p2
    mu = {
        k: sp.expand(p1 * L**k + p2 * (2 * L) ** k + p3 * (3 * L) ** k)
        for k in range(1, 5)
    }
    detg = sp.expand(
        (mu[2] - mu[1] ** 2) * (mu[4] - mu[2] ** 2)
        - (mu[3] - mu[1] * mu[2]) ** 2
    )
    cb = sp.expand(p1 * p2 * p3 * vand)
    assert sp.simplify(detg - cb) == 0

    print("PASS: three-state covariance determinant equals Cauchy--Binet/Vandermonde term")
    print("PASS: V(ln2,2ln2,3ln2)^2 = 4 (ln2)^6")
    print("PASS: w_beta(2) w_beta(4) w_beta(8) = 6 (ln2)^6 2^(-6 beta)")
    print("PASS: det g >= 24 (ln2)^12 2^(-6 beta) / m0^3 > 0")
    print("FORMAL TARGET: upgrade prime_fisher_normalized_det_nonneg to strict positivity")


if __name__ == "__main__":
    run()
