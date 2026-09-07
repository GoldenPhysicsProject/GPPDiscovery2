#!/usr/bin/env python3
"""High-precision audit of the continuous-sech Lévy condition.

For c > 0, the candidate symmetric Lévy density

    nu_c(x) = c / (|x| sinh(pi |x|))

is not locally L^1 at x=0.  The correct Lévy condition is

    int_R min(1,x^2) nu_c(x) dx < infinity.

This script numerically audits the near-zero cancellation, exponential tail,
weighted Lévy integral, and compensated cosine exponent without asserting a
formal proof.  It is intentionally independent of any RH claim.
"""

import mpmath as mp

mp.mp.dps = 70


def nu(c, x):
    ax = abs(mp.mpf(x))
    if ax == 0:
        return mp.inf
    return mp.mpf(c) / (ax * mp.sinh(mp.pi * ax))


def weighted(c, x):
    ax = abs(mp.mpf(x))
    if ax == 0:
        return mp.mpf(c) / mp.pi
    return min(mp.mpf(1), ax * ax) * nu(c, ax)


def compensated(c, t, x):
    ax = abs(mp.mpf(x))
    if ax == 0:
        return mp.mpf(c) * mp.mpf(t) ** 2 / (2 * mp.pi)
    return (1 - mp.cos(mp.mpf(t) * ax)) * nu(c, ax)


def relerr(a, b):
    scale = max(mp.mpf(1), abs(a), abs(b))
    return abs(a - b) / scale


def audit(c, t):
    c = mp.mpf(c)
    t = mp.mpf(t)

    print(f"c={c}, t={t}")
    print("near-zero weighted ratio -> 1")
    for e in (2, 4, 6, 8):
        x = mp.mpf(10) ** (-e)
        ratio = weighted(c, x) / (c / mp.pi)
        print(f"  x=1e-{e}: {mp.nstr(ratio, 30)}")
        assert abs(ratio - 1) < mp.mpf(10) ** (-(2 * e - 1))

    print("near-zero compensated ratio -> 1")
    target0 = c * t * t / (2 * mp.pi)
    for e in (2, 4, 6, 8):
        x = mp.mpf(10) ** (-e)
        ratio = compensated(c, t, x) / target0
        print(f"  x=1e-{e}: {mp.nstr(ratio, 30)}")
        assert abs(ratio - 1) < mp.mpf(10) ** (-(2 * e - 2))

    # Symmetry reduces the whole-line integrals to 2 times (0, infinity).
    levy_condition = 2 * (
        mp.quad(lambda x: x * x * nu(c, x), [0, 1])
        + mp.quad(lambda x: nu(c, x), [1, mp.inf])
    )
    print("weighted Levy integral =", mp.nstr(levy_condition, 45))
    assert mp.isfinite(levy_condition) and levy_condition > 0

    exponent_integral = 2 * mp.quad(
        lambda x: compensated(c, t, x), [0, 1, mp.inf]
    )
    exponent_exact = 2 * c * mp.log(mp.cosh(t / 2))
    transform_exact = mp.sech(t / 2) ** (2 * c)
    print("compensated integral =", mp.nstr(exponent_integral, 45))
    print("2c log cosh(t/2) =", mp.nstr(exponent_exact, 45))
    print("relative error =", mp.nstr(relerr(exponent_integral, exponent_exact), 12))
    assert relerr(exponent_integral, exponent_exact) < mp.mpf("1e-55")
    assert relerr(mp.e ** (-exponent_integral), transform_exact) < mp.mpf("1e-55")

    # Tail diagnostic: sinh(pi x) ~ exp(pi x)/2, so
    # nu_c(x) / [2c exp(-pi x)/x] -> 1.
    print("tail ratio -> 1")
    for x in (3, 5, 8, 12):
        x = mp.mpf(x)
        model = 2 * c * mp.e ** (-mp.pi * x) / x
        ratio = nu(c, x) / model
        print(f"  x={x}: {mp.nstr(ratio, 30)}")
        assert abs(ratio - 1) < 2 * mp.e ** (-2 * mp.pi * x) + mp.mpf("1e-60")


if __name__ == "__main__":
    for c, t in (("0.25", "0.7"), ("0.7", "1.3"), ("1.2", "2.1")):
        audit(c, t)
        print()
