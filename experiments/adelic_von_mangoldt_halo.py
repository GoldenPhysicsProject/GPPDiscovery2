#!/usr/bin/env python3
"""
Numerical audit of the adelic/von-Mangoldt hidden response

    D(x) = sum_{n>=2} Lambda(n)/sqrt(n) *
           [1 - (1 + 2x/sqrt(n)) exp(-2x/sqrt(n))].

The theorem candidate is D(x) ~ 4 x as x -> infinity.
Finite cutoff N misses a positive tail of order ~4 x^2/sqrt(N).

This is a numerical audit only; the asymptotic itself follows analytically
from the prime number theorem and partial summation.
"""

import math
import argparse


def primes_upto(n: int):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def von_mangoldt_prime_powers(nmax: int):
    ns, ws = [], []
    for p in primes_upto(nmax):
        lp = math.log(p)
        q = p
        while q <= nmax:
            ns.append(q)
            ws.append(lp / math.sqrt(q))
            if q > nmax // p:
                break
            q *= p
    return ns, ws


def F(y: float) -> float:
    return 1.0 - (1.0 + y) * math.exp(-y)


def response(x: float, ns, ws) -> float:
    return sum(w * F(2.0 * x / math.sqrt(n)) for n, w in zip(ns, ws))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=5_000_000)
    ap.add_argument(
        "--x",
        type=float,
        nargs="*",
        default=[2, 5, 10, 20, 50, 100, 200],
    )
    args = ap.parse_args()

    ns, ws = von_mangoldt_prime_powers(args.nmax)
    print(f"nmax={args.nmax:,}; prime-power terms={len(ns):,}")
    print("x          D_N(x)         4x          ratio       tail scale")
    for x in args.x:
        d = response(x, ns, ws)
        lead = 4.0 * x
        # PNT tail estimate from F(y)=y^2/2+O(y^3)
        tail = 4.0 * x * x / math.sqrt(args.nmax)
        print(
            f"{x:7.1f}  {d:13.6f}  {lead:11.6f}  "
            f"{d/lead:10.6f}  {tail:11.6f}"
        )


if __name__ == "__main__":
    main()
