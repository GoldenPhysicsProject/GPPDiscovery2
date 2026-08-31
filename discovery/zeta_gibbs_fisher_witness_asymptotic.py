#!/usr/bin/env python3
"""Large-eta asymptotic audit for the two-parameter number-Gibbs Fisher determinant.

Family:
    Z(beta, eta) = sum_{n>=1} exp(-beta log n - eta (log n)^2), eta > 0.

The Fisher metric for observables X=log n and X^2 has determinant
    det g = Cov(X,X) Cov(X^2,X^2) - Cov(X,X^2)^2.

For the normalized Gibbs weights, finite Cauchy-Binet gives a sum over triples.
The fixed triple n=(1,2,3) contributes
    W123/Z^3,
where
    W123 = exp(-beta log 6 - eta[(log 2)^2+(log 3)^2])
           * [log 2 log 3 log(3/2)]^2.

This script checks that for fixed beta the ratio det(g)/(W123/Z^3) tends to 1
as eta -> +infinity, i.e. the explicit strict lower witness is asymptotically
sharp in the low-temperature/strong-quadratic-confinement regime.
"""

from __future__ import annotations

import argparse
import mpmath as mp


def moments(beta: mp.mpf, eta: mp.mpf, nmax: int):
    raw = [mp.mpf("0") for _ in range(5)]
    for n in range(1, nmax + 1):
        x = mp.log(n)
        w = mp.e ** (-beta * x - eta * x * x)
        for k in range(5):
            raw[k] += w * x**k
    z = raw[0]
    return z, [r / z for r in raw]


def fisher_det(beta: mp.mpf, eta: mp.mpf, nmax: int):
    z, m = moments(beta, eta, nmax)
    g11 = m[2] - m[1] ** 2
    g12 = m[3] - m[1] * m[2]
    g22 = m[4] - m[2] ** 2
    return g11 * g22 - g12**2, z


def witness_123(beta: mp.mpf, eta: mp.mpf, z: mp.mpf):
    a = mp.log(2)
    b = mp.log(3)
    vandermonde_sq = (a * b * (b - a)) ** 2
    unnormalized = mp.e ** (-beta * mp.log(6) - eta * (a * a + b * b)) * vandermonde_sq
    return unnormalized / z**3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--nmax", type=int, default=5000)
    parser.add_argument("--betas", nargs="*", default=["0", "1", "2"])
    parser.add_argument("--etas", nargs="*", default=["2", "3", "4", "5", "7", "10", "15", "20"])
    args = parser.parse_args()

    mp.mp.dps = args.dps
    for beta_text in args.betas:
        beta = mp.mpf(beta_text)
        print(f"beta={beta_text}")
        for eta_text in args.etas:
            eta = mp.mpf(eta_text)
            detg, z = fisher_det(beta, eta, args.nmax)
            w123 = witness_123(beta, eta, z)
            ratio = detg / w123
            print(
                f"eta={eta_text:>5}  Z={mp.nstr(z, 20)}  "
                f"det/w123={mp.nstr(ratio, 30)}"
            )
        print()


if __name__ == "__main__":
    main()
