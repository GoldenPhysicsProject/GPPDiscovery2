#!/usr/bin/env python3
"""High-precision audit for the previously-open fourth principal-series moment A4.

The focused paper `principal_series_blocks.pdf` records

    A_k = (1/(2*pi)) int_R P(lam) D(lam)^k dlam,
    P(lam) = pi*lam/sinh(pi*lam),
    D(lam) = Re psi(1/2 + i lam/2) - psi(1/2),

with A4 = 0.2315253305644009308... and no closed form found.

This script gives strong discovery evidence for

    A4 = 3/8 - log(2) + 2 log(2)^2 - pi^2/24.

It computes A4 independently by high-precision quadrature, verifies the candidate to
well beyond 100 digits, and asks PSLQ to recover the same relation from the basis
[1, log(2), log(2)^2, log(2)^3, pi^2, pi^2 log(2), zeta(3)].

This is NOT yet a proof.  The purpose of the artifact is to promote the old
"no closed form found" endpoint to a sharply testable exact conjecture and provide the
next analytic/formal target.
"""
from __future__ import annotations

import mpmath as mp


def spectral_weight(lam: mp.mpf) -> mp.mpf:
    if lam == 0:
        return mp.mpf(1)
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def D(lam: mp.mpf) -> mp.mpf:
    return mp.re(mp.digamma(mp.mpf("0.5") + mp.mpf("0.5")j * lam)) - mp.digamma(mp.mpf("0.5"))


def A4_quadrature() -> mp.mpf:
    # P and D are even, so (1/(2*pi))*int_R = (1/pi)*int_0^infty.
    return (1 / mp.pi) * mp.quad(
        lambda x: spectral_weight(x) * D(x) ** 4,
        [0, 1, 3, 8, mp.inf],
    )


def candidate() -> mp.mpf:
    return mp.mpf(3) / 8 - mp.log(2) + 2 * mp.log(2) ** 2 - mp.pi**2 / 24


def main() -> None:
    mp.mp.dps = 130
    a4 = A4_quadrature()
    target = candidate()
    err = abs(a4 - target)

    # Independent integer-relation recovery.  The vector is
    # [A4, 1, log2, log2^2, log2^3, pi^2, pi^2 log2, zeta(3)].
    basis = [
        a4,
        mp.mpf(1),
        mp.log(2),
        mp.log(2) ** 2,
        mp.log(2) ** 3,
        mp.pi**2,
        mp.pi**2 * mp.log(2),
        mp.zeta(3),
    ]
    relation = mp.pslq(mp.matrix(basis), tol=mp.mpf("1e-100"), maxcoeff=10_000, maxsteps=20_000)
    expected_relation = [24, -9, 24, -48, 0, 1, 0, 0]

    assert relation == expected_relation, relation
    assert err < mp.mpf("1e-110"), err

    residual = (
        24 * a4
        - 9
        + 24 * mp.log(2)
        - 48 * mp.log(2) ** 2
        + mp.pi**2
    )
    assert abs(residual) < mp.mpf("1e-110"), residual

    print("A4 quadrature =", mp.nstr(a4, 120))
    print("candidate     =", mp.nstr(target, 120))
    print("absolute error=", mp.nstr(err, 12))
    print("PSLQ relation =", relation)
    print("candidate exact form: 3/8 - log(2) + 2*log(2)^2 - pi^2/24")
    print("PASS: >110-digit independent evidence for the A4 closed-form conjecture")


if __name__ == "__main__":
    main()
