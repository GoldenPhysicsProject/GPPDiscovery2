#!/usr/bin/env python3
"""Audit the natural logarithmic cancellation between the exceptional m=1 and m=2 channels.

This is discovery work, not an RH proof.

At the critical half-density boundary define

    S1(X) = sum_{p <= X} p^(-1/2),
    S2(X) = (1/2) sum_{p <= X} p^(-1).

The leading continuous prime-density counterterm for S1 is

    C1(X) = li(sqrt(X)) - li(sqrt(2)).

The first smooth Möbius correction to pi(x) is

    -(1/2) li(sqrt(x)).

Its weighted Stieltjes contribution to S1 is EXACTLY

    integral_2^X x^(-1/2) d[-(1/2) li(sqrt(x))]
      = -(1/2) [log log X - log log 2].

Thus the primitive residual S1-C1 naturally contains a negative
(1/2) log log X term.  This is opposite to the positive m=2 divergence
S2(X) ~ (1/2) log log X + M/2.  Consequently the combined exceptional
channel

    (S1(X) - C1(X)) + S2(X)

has its leading logarithmic divergence cancelled.

All smooth Möbius corrections n >= 3 are integrable after the p^(-1/2)
weight because x^(1/n-3/2)/log x has power exponent strictly below -1.
What remains after this cancellation is the genuinely arithmetic oscillatory
prime-counting error / zeros-side content.  No convergence or positivity of
that remainder is asserted here.
"""

from __future__ import annotations

import math
import mpmath as mp


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def primitive_leading_counterterm(x: int) -> float:
    return float(mp.li(mp.sqrt(x)) - mp.li(mp.sqrt(2)))


def prime_square_log_counterterm(x: int) -> float:
    """Magnitude of the positive log-log term; m=1 receives its negative."""
    return 0.5 * (math.log(math.log(x)) - math.log(math.log(2.0)))


def audit(
    cutoffs: tuple[int, ...] = (
        10_000,
        100_000,
        1_000_000,
        5_000_000,
        10_000_000,
        20_000_000,
    )
) -> None:
    max_x = max(cutoffs)
    primes = primes_upto(max_x)

    s1 = 0.0
    s2 = 0.0
    rows: list[tuple[float, ...]] = []
    cutoff_index = 0

    for p in primes:
        while cutoff_index < len(cutoffs) and p > cutoffs[cutoff_index]:
            x = cutoffs[cutoff_index]
            c1 = primitive_leading_counterterm(x)
            logct = prime_square_log_counterterm(x)
            raw_r1 = s1 - c1
            corrected_r1 = raw_r1 + logct
            combined = raw_r1 + s2
            mertens_residual = s2 - logct
            rows.append(
                (x, raw_r1, corrected_r1, s2, combined, mertens_residual)
            )
            cutoff_index += 1
        s1 += p ** -0.5
        s2 += 0.5 / p

    while cutoff_index < len(cutoffs):
        x = cutoffs[cutoff_index]
        c1 = primitive_leading_counterterm(x)
        logct = prime_square_log_counterterm(x)
        raw_r1 = s1 - c1
        corrected_r1 = raw_r1 + logct
        combined = raw_r1 + s2
        mertens_residual = s2 - logct
        rows.append((x, raw_r1, corrected_r1, s2, combined, mertens_residual))
        cutoff_index += 1

    print(
        "X | raw m1 residual | m1 + 1/2 loglog | m2 | combined m1+m2 | m2-log counterterm"
    )
    for x, raw, corr, m2, combo, mertens_res in rows:
        print(
            f"{int(x):>9d} | {raw: .12f} | {corr: .12f} | "
            f"{m2: .12f} | {combo: .12f} | {mertens_res: .12f}"
        )

    # Exact bookkeeping identity at every cutoff:
    # combined - corrected_r1 = m2 - logct.
    for x, raw, corr, m2, combo, mertens_res in rows:
        defect = (combo - corr) - mertens_res
        assert abs(defect) < 5e-13, (x, defect)

    # The n=2 correction is the unique logarithmically divergent smooth
    # Möbius correction after the half-density weight.  For all n>=3,
    # exponent 1/n - 3/2 is strictly below -1.
    for n in range(3, 50):
        assert 1.0 / n - 1.5 < -1.0

    print("\nExact structural conclusion:")
    print("  m=1 prime-square smooth correction = -1/2 (log log X - log log 2)")
    print("  m=2 leading divergence             = +1/2 log log X + constant + o(1)")
    print("  therefore their leading logarithmic divergences cancel in the joint channel.")
    print("No convergence, Schur positivity, or RH conclusion is asserted.")


if __name__ == "__main__":
    mp.mp.dps = 50
    audit()
