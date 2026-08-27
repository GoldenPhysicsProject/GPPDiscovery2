#!/usr/bin/env python3
"""High-precision audit of the shifted sech self-convolution.

Checks
    I(lambda) = int_R dx / (cosh(pi x) cosh(pi(lambda-x)))
against
    2 lambda / sinh(pi lambda), lambda != 0,
and the removable value I(0) = 2/pi.

This is numerical evidence only.  The exact Lean route is FTC for the
log-cosh primitive followed by an improper-limit passage.
"""

import mpmath as mp

mp.mp.dps = 80


def convolution(lam: mp.mpf) -> mp.mpf:
    f = lambda x: 1 / (mp.cosh(mp.pi * x) * mp.cosh(mp.pi * (lam - x)))
    if lam == 0:
        return mp.quad(f, [-mp.inf, 0, mp.inf])
    split = abs(lam)
    return mp.quad(f, [-mp.inf, -split, 0, split, mp.inf])


def closed_form(lam: mp.mpf) -> mp.mpf:
    if lam == 0:
        return 2 / mp.pi
    return 2 * lam / mp.sinh(mp.pi * lam)


def main() -> None:
    samples = [
        mp.mpf("0"), mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.5"),
        mp.mpf("1"), mp.mpf("2"), mp.mpf("-0.5"), mp.mpf("-2")
    ]
    print("dps=", mp.mp.dps)
    print("lambda\tintegral\tclosed_form\tabs_error")
    for lam in samples:
        val = convolution(lam)
        rhs = closed_form(lam)
        err = abs(val - rhs)
        print(
            f"{mp.nstr(lam, 8)}\t{mp.nstr(val, 32)}\t"
            f"{mp.nstr(rhs, 32)}\t{mp.nstr(err, 8)}"
        )


if __name__ == "__main__":
    main()
