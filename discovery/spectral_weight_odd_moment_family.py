"""Exact/numeric audit of the odd moments of the cut spectral weight.

For
    P(lambda) = pi*lambda/sinh(pi*lambda),
use 1/sinh x = 2*sum_{k>=0} exp(-(2k+1)x) to obtain, for r > -1,

    int_0^infty lambda^r P(lambda) d lambda
      = 2*Gamma(r+2)/pi^(r+1) * (1-2^(-(r+2))) * zeta(r+2).

The physically useful odd powers r=2m+1 therefore give odd zeta values.
This is a direct-weight moment identity only; it is not a convolution or
Wiener-Hopf loop-power statement.
"""

import mpmath as mp

mp.mp.dps = 80


def spectral_weight(lam):
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def numerical_moment(r):
    return mp.quad(lambda x: x**r * spectral_weight(x), [0, 1, mp.inf])


def closed_moment(r):
    return (
        2
        * mp.gamma(r + 2)
        / mp.pi ** (r + 1)
        * (1 - mp.power(2, -(r + 2)))
        * mp.zeta(r + 2)
    )


def main():
    print("Odd spectral-weight moment family")
    for r in (1, 3, 5, 7):
        numeric = numerical_moment(r)
        closed = closed_moment(r)
        error = abs(numeric - closed)
        print(f"r={r}")
        print("  numeric =", mp.nstr(numeric, 60))
        print("  closed  =", mp.nstr(closed, 60))
        print("  abs err =", mp.nstr(error, 8))
        assert error < mp.mpf("1e-45")

    # Explicit first two identities used for Lean promotion targets:
    # r=1: 7*zeta(3)/(2*pi^2)
    # r=3: 93*zeta(5)/(2*pi^4)
    target1 = 7 * mp.zeta(3) / (2 * mp.pi**2)
    target3 = 93 * mp.zeta(5) / (2 * mp.pi**4)
    assert abs(closed_moment(1) - target1) < mp.mpf("1e-70")
    assert abs(closed_moment(3) - target3) < mp.mpf("1e-70")
    print("verified r=1: 7*zeta(3)/(2*pi^2)")
    print("verified r=3: 93*zeta(5)/(2*pi^4)")


if __name__ == "__main__":
    main()
