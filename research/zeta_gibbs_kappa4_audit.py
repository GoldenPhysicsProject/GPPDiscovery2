#!/usr/bin/env python3
"""Independent numerical audit of the fourth zeta-Gibbs cumulant.

For beta > 1 and E(n)=log n under P_beta(n)=n^{-beta}/zeta(beta),

    kappa_r(beta) = (-1)^r d^r/d beta^r log zeta(beta)
                  = sum_{n>=2} Lambda(n) (log n)^(r-1) n^{-beta},  r>=2.

The second equality follows from the absolutely convergent Euler/von-Mangoldt
series on beta>1.  This script compares a finite von-Mangoldt sum against high-
precision numerical differentiation of log zeta.  It is evidence/audit only; the
Lean proof must identify the convergent global series exactly.
"""

import argparse
import math
import mpmath as mp


def von_mangoldt_table(limit: int):
    lam = [0.0] * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    root = int(math.isqrt(limit))
    for p in range(2, root + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            lp = math.log(p)
            q = p
            while q <= limit:
                lam[q] = lp
                if q > limit // p:
                    break
                q *= p
    return lam


def partial_cumulant(lam, order: int, beta: float):
    return math.fsum(
        lam[n] * (math.log(n) ** (order - 1)) * (n ** (-beta))
        for n in range(2, len(lam))
        if lam[n] != 0.0
    )


def derivative_cumulant(order: int, beta: float):
    f = lambda x: mp.log(mp.zeta(x))
    return (-1) ** order * mp.diff(f, mp.mpf(beta), order)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=200_000)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--betas", type=float, nargs="*", default=[1.5, 2.0, 3.0, 5.0, 10.0])
    args = parser.parse_args()

    mp.mp.dps = args.dps
    lam = von_mangoldt_table(args.limit)

    print(f"limit={args.limit} dps={args.dps}")
    print("beta order partial_vonMangoldt high_precision_derivative abs_error")
    for beta in args.betas:
        for order in (2, 3, 4):
            partial = partial_cumulant(lam, order, beta)
            exact = derivative_cumulant(order, beta)
            err = abs(mp.mpf(partial) - exact)
            print(
                f"{beta:5.2f} {order:d} "
                f"{partial:.16e} {mp.nstr(exact, 20):>22s} {mp.nstr(err, 8)}"
            )
        k4 = derivative_cumulant(4, beta)
        if not (k4 > 0):
            raise SystemExit(f"unexpected nonpositive kappa_4 at beta={beta}: {k4}")

    print("AUDIT: kappa_4 positive at every sampled beta; no sign-change evidence.")
    print("FORMAL BOUNDARY: exact global kappa_4 = positive von-Mangoldt series still requires proof.")


if __name__ == "__main__":
    main()
