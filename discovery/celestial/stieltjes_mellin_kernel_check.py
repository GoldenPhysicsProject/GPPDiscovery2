#!/usr/bin/env python3
"""Numerical audit of the universal Stieltjes-Mellin kernel.

For 0 < Re(sigma) < 1,
    integral_0^infty t^{-sigma}/(1+t) dt = pi/sin(pi sigma).

This is the universal factor entering the celestial cut -> dispersion Mellin
bridge.  The script is an audit only; the intended promotion target is a Lean
proof with the strip and integrability hypotheses explicit.
"""

import mpmath as mp

mp.mp.dps = 70

TESTS = [
    mp.mpc("0.2", "0.3"),
    mp.mpc("0.5", "0.0"),
    mp.mpc("0.7", "-0.4"),
    mp.mpc("0.35", "1.1"),
]


def kernel_integral(sigma: mp.mpc) -> mp.mpc:
    f = lambda t: mp.power(t, -sigma) / (1 + t)
    return mp.quad(f, [0, 1, mp.inf])


def closed_form(sigma: mp.mpc) -> mp.mpc:
    return mp.pi / mp.sin(mp.pi * sigma)


def main() -> None:
    worst = mp.mpf("0")
    for sigma in TESTS:
        if not (0 < mp.re(sigma) < 1):
            raise ValueError(f"sigma outside Mellin strip: {sigma}")
        lhs = kernel_integral(sigma)
        rhs = closed_form(sigma)
        err = abs(lhs - rhs)
        worst = max(worst, err)
        print(f"sigma={sigma}")
        print(f" integral = {mp.nstr(lhs, 35)}")
        print(f" closed   = {mp.nstr(rhs, 35)}")
        print(f" abs err  = {mp.nstr(err, 8)}\n")
    print(f"worst absolute error: {mp.nstr(worst, 8)}")


if __name__ == "__main__":
    main()
