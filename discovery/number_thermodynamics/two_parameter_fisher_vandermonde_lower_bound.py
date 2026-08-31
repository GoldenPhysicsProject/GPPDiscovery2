#!/usr/bin/env python3
"""Numerical check for the explicit 3-point lower bound on the two-parameter
zeta-Gibbs Fisher determinant.

For p_n proportional to exp(-beta log n - eta (log n)^2), the covariance
matrix of X=log n and X^2 has determinant

  det g = sum_{i<j<k} p_i p_j p_k prod_{pairs}(x_j-x_i)^2

whenever the countable Cauchy-Binet passage is justified. Keeping only the
triple n=1,2,3 yields the explicit positive lower bound tested here.
"""

import mpmath as mp

mp.mp.dps = 60


def fisher_det(beta, eta, tol=mp.mpf("1e-55"), nmax=200000):
    xs, ws = [], []
    Z = mp.mpf("0")
    for n in range(1, nmax + 1):
        x = mp.log(n)
        w = mp.exp(-beta * x - eta * x * x)
        xs.append(x)
        ws.append(w)
        Z += w
        if eta > 0 and n > 100 and w < tol:
            break
    ps = [w / Z for w in ws]
    m1 = mp.fsum(p * x for p, x in zip(ps, xs))
    m2 = mp.fsum(p * x**2 for p, x in zip(ps, xs))
    m3 = mp.fsum(p * x**3 for p, x in zip(ps, xs))
    m4 = mp.fsum(p * x**4 for p, x in zip(ps, xs))
    a = m2 - m1**2
    b = m3 - m1 * m2
    c = m4 - m2**2
    return a * c - b**2, Z, len(xs)


def three_point_lower_bound(beta, eta, Z):
    l2, l3 = mp.log(2), mp.log(3)
    vandermonde_sq = (l2 * l3 * (l3 - l2)) ** 2
    weight = mp.exp(-beta * mp.log(6) - eta * (l2**2 + l3**2)) / Z**3
    return weight * vandermonde_sq


def main():
    samples = [(0, 1), (1, 2), (-5, 1), (2, mp.mpf("0.2")), (4, 3)]
    for beta, eta in samples:
        detg, Z, terms = fisher_det(mp.mpf(beta), mp.mpf(eta))
        lb = three_point_lower_bound(mp.mpf(beta), mp.mpf(eta), Z)
        print(f"beta={beta}, eta={eta}, terms={terms}")
        print("  det g =", mp.nstr(detg, 30))
        print("  n=1,2,3 lower bound =", mp.nstr(lb, 30))
        print("  ratio =", mp.nstr(detg / lb, 30))
        assert detg > 0
        assert lb > 0
        assert detg >= lb


if __name__ == "__main__":
    main()
