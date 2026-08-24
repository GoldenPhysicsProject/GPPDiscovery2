#!/usr/bin/env python3
"""High-precision audit of the explicit scalar-box regulator remainder bound.

This script is not a proof.  It checks the exact dilogarithmic primitive against the
explicit analytic constant in REGULATOR_EXPLICIT_REMAINDER.md on deterministic and
randomized points inside 0 < m <= min(S/4,U/16).
"""

from __future__ import annotations

import math
import random
import mpmath as mp

mp.mp.dps = 100


def exact_values(S: mp.mpf, U: mp.mpf, m: mp.mpf):
    R = mp.sqrt(U / (U + 4 * m))
    kappa = mp.sqrt((S * (U + 4 * m) - 4 * m * m) / (S * U))
    q = (1 - R) / (1 + R)
    a = (kappa - 1) / (kappa + 1)

    def F(x):
        return (
            mp.log(a) * mp.log(x / a - 1)
            - mp.polylog(2, 1 - x / a)
            + mp.polylog(2, 1 - a * x)
            + mp.log(a) * mp.log(1 - a * x)
        )

    D = F(q) - F(1)
    J = 2 * D / (S * U * kappa)
    Jas = (
        2 * mp.log(S / m) * mp.log(U / m)
        + mp.log(U / m) ** 2
        - mp.pi**2 / 3
    ) / (S * U)
    return J, Jas


def explicit_constant(S: mp.mpf, U: mp.mpf):
    m0 = min(S / 4, U / 16)
    s = abs(mp.log(S))
    u = abs(mp.log(U))
    cq = mp.log(mp.mpf(289) / 256)

    A1 = mp.mpf(289) / 192 * (1 / S + mp.mpf(33) / (16 * U))
    B1 = mp.mpf(91) / (15 * U) + (mp.mpf(4) / 61 + mp.mpf(4) / 3) / S
    K1 = A1 * (s + u + 1) + B1 * (u + mp.mpf("0.5"))
    K2 = A1 * B1 + mp.mpf("0.5") * A1**2
    CE = (
        mp.mpf(48) / (19 * S)
        + (
            mp.mpf(16) / 255
            + mp.mpf(232) / 105
            + mp.mpf(8) / 225
            + mp.mpf(16) / 255 * (u + cq + mp.mpf("0.5"))
        )
        / U
    )
    K0 = (
        mp.mpf("1.5")
        + (s + 2 * u) / 2
        + s * u
        + u**2 / 2
        + mp.pi**2 / 6
    )
    return 2 / (S * U) * (K1 + m0 * K2 + CE + 2 * K0 / U)


def audit_point(Ss: str, Us: str, ms: str):
    S, U, m = map(mp.mpf, (Ss, Us, ms))
    assert 0 < m <= min(S / 4, U / 16)
    J, Jas = exact_values(S, U, m)
    C = explicit_constant(S, U)
    rhs = C * m * (1 + abs(mp.log(m)) ** 2)
    ratio = abs(J - Jas) / rhs
    return ratio, J, Jas, rhs


def main():
    anchors = [
        ("1", "1", "1e-8"),
        ("1", "2", "1e-6"),
        ("3", "0.7", "1e-7"),
        ("0.4", "5", "1e-8"),
        ("8", "3", "1e-5"),
    ]
    worst = mp.mpf(0)
    for p in anchors:
        ratio, *_ = audit_point(*p)
        worst = max(worst, ratio)
        print("anchor", p, "ratio=", mp.nstr(ratio, 16))

    rng = random.Random(20260824)
    for _ in range(2000):
        S = mp.mpf(str(10 ** rng.uniform(-1, 1)))
        U = mp.mpf(str(10 ** rng.uniform(-1, 1)))
        m0 = min(S / 4, U / 16)
        m = m0 * mp.mpf(str(10 ** rng.uniform(-8, 0)))
        ratio, *_ = audit_point(mp.nstr(S, 40), mp.nstr(U, 40), mp.nstr(m, 40))
        worst = max(worst, ratio)
        if ratio > 1:
            raise AssertionError(f"explicit bound violated numerically: ratio={ratio}")

    print("worst ratio over audit =", mp.nstr(worst, 16))
    print("PASS")


if __name__ == "__main__":
    main()
