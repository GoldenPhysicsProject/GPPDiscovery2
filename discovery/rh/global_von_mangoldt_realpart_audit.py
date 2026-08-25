#!/usr/bin/env python3
"""Numerical audit for the convergent-axis identity

    Re[-zeta'(a+it)/zeta(a+it)]
      = sum_{n>=2} Lambda(n) n^{-a} cos(t log n),   a > 1.

This is discovery-side evidence only.  The corresponding exact theorem belongs in
GPPVerify2 after formalization.  No critical-strip continuation is tested here.
"""

import math
import mpmath as mp

mp.mp.dps = 60


def von_mangoldt_sieve(N: int):
    lam = [mp.mpf("0")] * (N + 1)
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, N + 1):
        if not is_prime[p]:
            continue
        for q in range(p * 2, N + 1, p):
            is_prime[q] = False
        lp = mp.log(p)
        q = p
        while q <= N:
            lam[q] = lp
            if q > N // p:
                break
            q *= p
    return lam


def cosine_sum(a, t, lam, N):
    return mp.fsum(
        lam[n] * mp.power(n, -a) * mp.cos(t * mp.log(n))
        for n in range(2, N + 1)
        if lam[n]
    )


def target(a, t):
    s = mp.mpc(a, t)
    return mp.re(-mp.diff(mp.zeta, s) / mp.zeta(s))


def main():
    Nmax = 100_000
    lam = von_mangoldt_sieve(Nmax)
    tests = [(1.8, 2.2), (2.0, 0.7), (2.5, 5.0), (3.0, 1.25)]
    cutoffs = [1_000, 10_000, 100_000]

    for a, t in tests:
        z = target(a, t)
        print(f"a={a}, t={t}, target={mp.nstr(z, 30)}")
        last = None
        for N in cutoffs:
            sN = cosine_sum(a, t, lam, N)
            err = abs(sN - z)
            print(f"  N={N:6d}  partial={mp.nstr(sN, 30)}  abs_err={mp.nstr(err, 8)}")
            last = err
        assert last < mp.mpf("2e-4")

    print("PASS: convergent-axis real-part/cosine identity numerically audited.")


if __name__ == "__main__":
    main()
