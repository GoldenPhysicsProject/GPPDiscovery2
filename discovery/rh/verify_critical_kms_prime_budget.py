#!/usr/bin/env python3
"""Verify the critical-KMS prime dual-norm identity and polynomial envelope.

No zero data are used. This is a discovery check, not an RH proof.
"""

from __future__ import annotations
import argparse
import math


def primes_upto(n: int):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0: sieve[0] = 0
    if n >= 1: sieve[1] = 0
    p = 2
    while p * p <= n:
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n-p*p)//p)+1)
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def budget(L: float):
    X = int(math.exp(L))
    total = 0.0
    for p in primes_upto(X):
        pk = p
        k = 1
        lp = math.log(p)
        while pk <= X:
            d = (1.0 - 1.0/pk) / (k * lp)
            c = lp / math.sqrt(pk)
            direct = c*c/d
            closed = k * lp**3 / (pk - 1.0)
            if abs(direct-closed) > 1e-12 * max(1.0, abs(closed)):
                raise RuntimeError("identity failure")
            total += closed
            if pk > X // p:
                break
            pk *= p
            k += 1
    crude = 2.0 * sum((math.log(n)**3)/n for n in range(2, X + 1))
    return X, total, crude


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", nargs="*", type=float, default=[2,3,4,5,6,7,8,9,10])
    args = ap.parse_args()
    print("L  exp(L)  KMS_dual_sq  /L^4  crude_integer_envelope")
    for L in args.L:
        X, val, crude = budget(L)
        print(f"{L:4.1f} {X:8d} {val:15.8g} {val/L**4:10.4g} {crude:18.8g}")
        if val > crude * (1 + 1e-12):
            raise RuntimeError("crude envelope failure")
    print("PASS")


if __name__ == "__main__":
    main()
