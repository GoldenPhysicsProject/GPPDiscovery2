#!/usr/bin/env python3
"""Audit the explicit three-prime witness for the 3x3 prime-gas Hankel determinant.

For beta>1 let
    kappa_r(beta) = sum_{p,k>=1} k^(r-1) (log p)^r p^(-k beta),  r>=2.
The 3x3 Hankel determinant is
    H3 = det [kappa_{i+j+2}]_{i,j=0}^2.
For the positive moment measure
    dnu_beta = sum_{n>=2} Lambda(n) log(n) n^(-beta) delta_{log n},
Cauchy--Binet gives H3 as a sum over triples of support points of
weight products times squared Vandermonde factors.  Therefore the single
prime triple 2,3,5 gives the rigorous candidate lower bound

 H3 >= L235(beta)
    = (log 2 log 3 log 5)^2 30^(-beta)
      * ((log 3-log 2)(log 5-log 2)(log 5-log 3))^2 > 0.

This script is discovery/audit only.  It increases the prime-power cutoff
independently and prints H3, L235, and their ratio at high precision.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 70


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def cumulants(beta: mp.mpf, cutoff: int, rmax: int = 6) -> list[mp.mpf]:
    out = [mp.mpf("0") for _ in range(rmax + 1)]
    for p in primes_upto(cutoff):
        lp = mp.log(p)
        pk = p
        k = 1
        while pk <= cutoff:
            for r in range(2, rmax + 1):
                out[r] += (mp.mpf(k) ** (r - 1)) * (lp**r) * (mp.mpf(p) ** (-k * beta))
            k += 1
            pk *= p
    return out


def hankel3(beta: mp.mpf, cutoff: int) -> mp.mpf:
    kap = cumulants(beta, cutoff)
    mat = mp.matrix([[kap[i + j + 2] for j in range(3)] for i in range(3)])
    return mp.det(mat)


def witness_235(beta: mp.mpf) -> mp.mpf:
    l2, l3, l5 = mp.log(2), mp.log(3), mp.log(5)
    weights = (l2**2) * (l3**2) * (l5**2) * mp.power(30, -beta)
    vandermonde_sq = ((l3 - l2) * (l5 - l2) * (l5 - l3)) ** 2
    return weights * vandermonde_sq


def main() -> None:
    betas = [mp.mpf(x) for x in ("1.10", "1.50", "2", "3", "5", "10")]
    cutoffs = (20_000, 50_000)
    for beta in betas:
        lower = witness_235(beta)
        vals = [hankel3(beta, c) for c in cutoffs]
        print(f"beta={mp.nstr(beta, 6)}")
        for c, h3 in zip(cutoffs, vals):
            print(f"  cutoff={c:6d} H3={mp.nstr(h3, 28)} ratio={mp.nstr(h3/lower, 18)}")
        print(f"  L235={mp.nstr(lower, 28)}")
        print(f"  cutoff_delta={mp.nstr(abs(vals[-1]-vals[-2]), 12)}")
        assert vals[-1] > lower > 0


if __name__ == "__main__":
    main()
