#!/usr/bin/env python3
"""Audit the exact partial-summation remainder behind the primitive m=1 counterterm.

For
    S1(X) = sum_{p <= X} p^(-1/2)
    C1(X) = li(sqrt(X)) - li(sqrt(2))
and E(x) = pi(x) - li(x), Abel/partial summation gives the exact identity

    S1(X) - C1(X)
      = E(X)/sqrt(X)
        + 1/2 * integral_2^X E(t) t^(-3/2) dt
        + li(2)/sqrt(2).

This script checks the identity numerically without assuming convergence of the
remainder.  The point is diagnostic: subtracting the smooth PNT density leaves
a remainder controlled by the prime-counting error E, so numerical flattening
of S1-C1 at modest X is not evidence for a finite renormalized limit.

No RH claim is made.
"""

from __future__ import annotations

import math
import mpmath as mp

mp.mp.dps = 50


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def li(x: mp.mpf) -> mp.mpf:
    return mp.li(x)


def audit(X: int, primes: list[int]) -> tuple[mp.mpf, ...]:
    ps = [p for p in primes if p <= X]
    piX = len(ps)
    sqrtX = mp.sqrt(X)
    s1 = mp.fsum(1 / mp.sqrt(p) for p in ps)
    c1 = li(sqrtX) - li(mp.sqrt(2))
    residual = s1 - c1

    # E(X)/sqrt(X)
    endpoint = (mp.mpf(piX) - li(mp.mpf(X))) / sqrtX

    # Evaluate (1/2) int_2^X E(t)t^(-3/2)dt by splitting the
    # prime-counting and li pieces analytically.  Partial summation gives
    # int pi(t)t^(-3/2)dt = 2*(S1 - pi(X)/sqrt(X)).
    int_pi = 2 * (s1 - mp.mpf(piX) / sqrtX)

    # Integration by parts for the smooth li piece:
    # int_2^X li(t)t^(-3/2)dt
    # = 2*( C1 - li(X)/sqrt(X) + li(2)/sqrt(2) ).
    int_li = 2 * (c1 - li(mp.mpf(X)) / sqrtX + li(mp.mpf(2)) / mp.sqrt(2))
    error_integral_half = mp.mpf("0.5") * (int_pi - int_li)
    lower_constant = li(mp.mpf(2)) / mp.sqrt(2)
    rhs = endpoint + error_integral_half + lower_constant
    defect = residual - rhs
    return residual, endpoint, error_integral_half, lower_constant, rhs, defect


def main() -> None:
    cutoffs = [10_000, 100_000, 1_000_000, 5_000_000]
    primes = primes_upto(max(cutoffs))
    print("Primitive m=1 li-counterterm exact remainder audit")
    print("Identity: R = E(X)/sqrt(X) + 1/2 int E(t)t^(-3/2)dt + li(2)/sqrt(2)\n")
    for X in cutoffs:
        residual, endpoint, integral, const, rhs, defect = audit(X, primes)
        print(f"X={X:,}")
        print(f"  S1-C1                  = {mp.nstr(residual, 18)}")
        print(f"  E(X)/sqrt(X)           = {mp.nstr(endpoint, 18)}")
        print(f"  1/2 integral remainder = {mp.nstr(integral, 18)}")
        print(f"  lower constant          = {mp.nstr(const, 18)}")
        print(f"  reconstructed RHS       = {mp.nstr(rhs, 18)}")
        print(f"  identity defect         = {mp.nstr(defect, 8)}\n")

    print("Interpretation:")
    print("  A finite limit of S1-C1 requires control of BOTH the endpoint")
    print("  E(X)/sqrt(X) and the weighted integral of E(t)=pi(t)-li(t).")
    print("  The smooth li(sqrt X) subtraction alone does not supply that control.")


if __name__ == "__main__":
    main()
