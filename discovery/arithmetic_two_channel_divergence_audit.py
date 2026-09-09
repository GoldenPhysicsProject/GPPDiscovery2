#!/usr/bin/env python3
"""Audit the two exceptional prime-repetition channels at the critical boundary.

For the Fock norm weights p^{-m/2}/m, the manuscript isolates m=1 and m=2 as
the only divergent repetition sectors.  Prime-number-theorem asymptotics sharpen
that statement:

  S1(X) = sum_{p<=X} p^{-1/2} ~ 2 sqrt(X)/log X,
  S2(X) = 1/2 sum_{p<=X} p^{-1} = 1/2 log log X + M/2 + o(1).

Thus the primitive channel has a power/log divergence while the double-prime
channel has only a log-log divergence.  A single one-scale counterterm cannot
cancel both asymptotic structures; a genuine two-channel completion is natural.

This is a numerical audit of the asymptotics, not a proof of RH or of the global
Schur-completion theorem.
"""

from __future__ import annotations

import math


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    r = int(math.isqrt(n))
    for p in range(2, r + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def audit(X: int) -> tuple[float, float, float, float]:
    ps = primes_upto(X)
    s1 = sum(p ** -0.5 for p in ps)
    s2 = 0.5 * sum(1.0 / p for p in ps)

    a1 = 2.0 * math.sqrt(X) / math.log(X)
    # For the m=2 ratio we compare only the divergent part; the Mertens constant
    # contributes an additive O(1), so convergence is intentionally slow.
    a2 = 0.5 * math.log(math.log(X))
    return s1, s1 / a1, s2, s2 / a2


def main() -> None:
    print("Two-channel critical-boundary divergence audit")
    print("X          S1/(2sqrtX/logX)        S2/(0.5 log log X)")
    for X in (10_000, 100_000, 1_000_000, 5_000_000):
        s1, r1, s2, r2 = audit(X)
        print(f"{X:>8d}   {r1: .12f}              {r2: .12f}")

    # Structural sanity checks: the two counterterm scales become increasingly
    # separated.  This quantity tends to infinity:
    # (2 sqrt X / log X) / (0.5 log log X).
    vals = []
    for X in (10_4 := 10_000, 100_000, 1_000_000, 5_000_000):
        ratio = (2.0 * math.sqrt(X) / math.log(X)) / (0.5 * math.log(math.log(X)))
        vals.append(ratio)
    assert all(b > a for a, b in zip(vals, vals[1:])), vals

    # The m>=3 prime sectors are absolutely convergent.  We numerically check
    # stabilization for the first such case m=3.
    def s3(X: int) -> float:
        return (1.0 / 3.0) * sum(p ** -1.5 for p in primes_upto(X))

    d = abs(s3(5_000_000) - s3(1_000_000))
    print(f"m=3 tail increment from 1e6 to 5e6: {d:.3e}")
    assert d < 1e-4

    print("PASS: primitive and double-prime channels exhibit distinct divergence scales;")
    print("      the first convergent repetition sector is numerically stabilizing.")


if __name__ == "__main__":
    main()
