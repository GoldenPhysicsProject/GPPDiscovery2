#!/usr/bin/env python3
"""Audit the natural PNT counterterms for the exceptional m=1 and m=2 prime channels.

This is a discovery diagnostic, not an RH claim and not a claim that the
renormalized residuals converge.  The continuous prime-density model gives

    sum_{p<=X} p^{-1/2}  ~  integral_2^X dt/(sqrt(t) log t)
                         = li(sqrt(X)) - li(sqrt(2)),

while the m=2 channel has the Mertens counterterm (1/2) log log X.

The script compares the full li(sqrt X) counterterm with the cruder leading
term 2 sqrt(X)/log X and reports the m=2 residual at increasing cutoffs.
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


def li_counterterm(x: int) -> float:
    # Match the continuous model integral from 2 to X exactly.
    return float(mp.li(mp.sqrt(x)) - mp.li(mp.sqrt(2)))


def audit(cutoffs: tuple[int, ...] = (10_000, 100_000, 1_000_000, 5_000_000)) -> None:
    max_x = max(cutoffs)
    primes = primes_upto(max_x)
    wanted = set(cutoffs)
    s1 = 0.0
    s2 = 0.0
    rows: list[tuple[float, ...]] = []

    cutoff_iter = iter(cutoffs)
    current = next(cutoff_iter)
    for p in primes:
        while p > current:
            lead = 2.0 * math.sqrt(current) / math.log(current)
            li_ct = li_counterterm(current)
            rows.append((current, s1, lead, s1 - lead, li_ct, s1 - li_ct,
                         s2, s2 - 0.5 * math.log(math.log(current))))
            try:
                current = next(cutoff_iter)
            except StopIteration:
                current = max_x + 1
                break
        if p > max_x:
            break
        s1 += p ** -0.5
        s2 += 0.5 / p

    if current <= max_x:
        lead = 2.0 * math.sqrt(current) / math.log(current)
        li_ct = li_counterterm(current)
        rows.append((current, s1, lead, s1 - lead, li_ct, s1 - li_ct,
                     s2, s2 - 0.5 * math.log(math.log(current))))

    print("X | S1 | leading residual | li(sqrt X) residual | m2 residual")
    for x, s1v, lead, lead_res, li_ct, li_res, s2v, m2_res in rows:
        print(f"{int(x):>8d} | {s1v: .12f} | {lead_res: .12f} | {li_res: .12f} | {m2_res: .12f}")

    # Diagnostic assertions: over this audit range, the full PNT-density
    # counterterm is dramatically sharper than the first asymptotic term.
    for _, _, _, lead_res, _, li_res, _, _ in rows:
        assert abs(li_res) < abs(lead_res)

    # Do not assert convergence of either residual.  That requires control of
    # the prime-counting error beyond this numerical experiment.
    print("\nInterpretation: li(sqrt X) is the natural continuous-density counterterm;")
    print("the residual is diagnostic only and is NOT asserted to converge.")


if __name__ == "__main__":
    mp.mp.dps = 50
    audit()
