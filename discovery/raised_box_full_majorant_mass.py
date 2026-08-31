#!/usr/bin/env python3
"""Numerical cross-check for the raised-box one-channel DCT majorant.

For S>0 and 0<delta<1, the affine-simplex majorant

    M = 1 + (S*x1*x3)^(-delta)

has total mass

    1/6 + S^(-delta) * Gamma(1-delta)^2 / Gamma(4-2*delta).

The numerical path uses x=t^(1/(1-delta)) in the remaining outer integral,
which cancels the x^(-delta) endpoint singularity and stays stable close to
delta=1.
"""

import argparse
import mpmath as mp


def closed_mass(S: mp.mpf, delta: mp.mpf) -> mp.mpf:
    return (
        mp.mpf(1) / 6
        + S ** (-delta)
        * mp.gamma(1 - delta) ** 2
        / mp.gamma(4 - 2 * delta)
    )


def reduced_numeric_mass(S: mp.mpf, delta: mp.mpf) -> mp.mpf:
    inv = 1 / (1 - delta)
    # x = t^(1/(1-delta)) gives x^(-delta) dx = dt/(1-delta).
    outer = inv * mp.quad(
        lambda t: (1 - t ** inv) ** (2 - delta),
        [0, 1],
    )
    singular = S ** (-delta) * outer / ((1 - delta) * (2 - delta))
    return mp.mpf(1) / 6 + singular


def check(S: mp.mpf, delta: mp.mpf, dps: int) -> None:
    if not (S > 0):
        raise ValueError("S must be positive")
    if not (0 < delta < 1):
        raise ValueError("delta must satisfy 0 < delta < 1")

    mp.mp.dps = dps
    numeric = reduced_numeric_mass(S, delta)
    exact = closed_mass(S, delta)
    err = abs(numeric - exact)

    print(f"S={mp.nstr(S, 16)} delta={mp.nstr(delta, 16)} dps={dps}")
    print(f"numeric = {mp.nstr(numeric, dps // 2)}")
    print(f"closed  = {mp.nstr(exact, dps // 2)}")
    print(f"abs_err = {mp.nstr(err, 8)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--S", default="1")
    parser.add_argument("--delta", default="0.99")
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()
    check(mp.mpf(args.S), mp.mpf(args.delta), args.dps)
