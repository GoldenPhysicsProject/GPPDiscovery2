#!/usr/bin/env python3
"""Verify the exact pole-healing identities used in the RH discovery note.

This script does not use zeta zeros and does not prove RH.
"""

from __future__ import annotations
import argparse
import mpmath as mp


def b02(L, s):
    a = L / (4 * mp.pi)
    C = 2 * L * mp.sinh(L / 4) ** 2 / mp.pi**2
    return C * s / (s * s + a * a)


def correction(L, s):
    a = L / (4 * mp.pi)
    return (
        2 * L / mp.pi**2
        * s * mp.sin(mp.pi * s) ** 2
        / (s * s + a * a)
    )


def healed_closed(L, s):
    a = L / (4 * mp.pi)
    return (
        L / mp.pi**2
        * s * (mp.cosh(L / 2) - mp.cos(2 * mp.pi * s))
        / (s * s + a * a)
    )


def healed_integral(L, s):
    a = L / (4 * mp.pi)
    return (
        L / mp.pi**2
        * mp.quad(
            lambda x: mp.cosh(a * (2 * mp.pi - x)) * mp.sin(s * x),
            [0, 2 * mp.pi],
        )
    )


def check(L, N, dps):
    mp.mp.dps = dps
    L = mp.mpf(L)
    tol = mp.mpf(10) ** (-(dps // 2))

    closed_err = mp.mpf("0")
    integral_err = mp.mpf("0")
    hermite_value_err = mp.mpf("0")
    hermite_deriv_err = mp.mpf("0")

    samples = [
        mp.mpf("0.13"),
        mp.mpf("0.47"),
        mp.mpf("1.21"),
        mp.mpc("0.3", "0.4"),
        mp.mpc("1.2", "0.7"),
    ]

    for z in samples:
        p = b02(L, z) + correction(L, z)
        closed_err = max(closed_err, abs(p - healed_closed(L, z)))
        integral_err = max(integral_err, abs(p - healed_integral(L, z)))

    for n in range(-N, N + 1):
        nn = mp.mpf(n)
        hermite_value_err = max(
            hermite_value_err,
            abs(healed_closed(L, nn) - b02(L, nn)),
        )
        hermite_deriv_err = max(
            hermite_deriv_err,
            abs(
                mp.diff(lambda z: healed_closed(L, z), nn)
                - mp.diff(lambda z: b02(L, z), nn)
            ),
        )

    assert closed_err < tol, closed_err
    assert integral_err < mp.sqrt(tol), integral_err
    assert hermite_value_err < tol, hermite_value_err
    assert hermite_deriv_err < mp.sqrt(tol), hermite_deriv_err

    print("Pole-healing verification")
    print("L =", mp.nstr(L, 16), "N =", N, "dps =", dps)
    print("closed-form error        =", mp.nstr(closed_err, 8))
    print("compact-integral error   =", mp.nstr(integral_err, 8))
    print("integer value error      =", mp.nstr(hermite_value_err, 8))
    print("integer derivative error =", mp.nstr(hermite_deriv_err, 8))
    print("status: exact identities numerically verified; not an RH proof")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", default=str(2 * mp.log(3)))
    ap.add_argument("--N", type=int, default=8)
    ap.add_argument("--dps", type=int, default=60)
    args = ap.parse_args()
    check(args.L, args.N, args.dps)
