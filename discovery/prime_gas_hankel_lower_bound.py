#!/usr/bin/env python3
"""High-precision audit of the strict 2x2 prime-gas Hankel determinant bound.

For beta > 1 define
    kappa_r(beta) = sum_{n>=2} Lambda(n) (log n)^(r-1) n^(-beta).
Then
    H2 = kappa_2*kappa_4 - kappa_3^2
is the 2x2 Hankel determinant of the positive discrete measure
    dnu_beta = sum Lambda(n) log(n) n^(-beta) delta_{log n}.
The pairwise identity gives
    H2 = sum_{m<n} w_m w_n (log m-log n)^2,
where w_n = Lambda(n) log(n) n^(-beta), hence the explicit witness
    H2 >= (log 2)^2 (log 3)^2 (log 3-log 2)^2 6^(-beta) > 0.

This script checks the full determinant from prime powers against that explicit
2,3 witness while independently increasing the prime-power cutoff.
"""

import mpmath as mp

mp.mp.dps = 70


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def cumulant(beta, r, pmax):
    total = mp.mpf("0")
    for p in primes_upto(pmax):
        lp = mp.log(p)
        k = 1
        while True:
            term = (k ** (r - 1)) * (lp ** r) * mp.power(p, -k * beta)
            total += term
            if abs(term) < mp.mpf("1e-68"):
                break
            k += 1
    return total


def witness(beta):
    l2, l3 = mp.log(2), mp.log(3)
    return l2**2 * l3**2 * (l3 - l2)**2 * mp.power(6, -beta)


def audit(beta, pmax):
    k2 = cumulant(beta, 2, pmax)
    k3 = cumulant(beta, 3, pmax)
    k4 = cumulant(beta, 4, pmax)
    det = k2 * k4 - k3**2
    lb = witness(beta)
    return det, lb, det / lb


if __name__ == "__main__":
    for beta in map(mp.mpf, ["1.05", "1.1", "1.5", "2", "3", "5", "10"]):
        print(f"beta={beta}")
        for pmax in [100, 1000, 10000]:
            det, lb, ratio = audit(beta, pmax)
            print(f"  pmax={pmax:5d} det={mp.nstr(det, 24)}")
            print(f"              lb ={mp.nstr(lb, 24)} ratio={mp.nstr(ratio, 18)}")
            assert det > lb > 0
