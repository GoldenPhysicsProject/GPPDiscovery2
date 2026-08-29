#!/usr/bin/env python3
"""Exact/numerical audit of the first odd moment of the spectral weight.

For P(lambda) = pi*lambda/sinh(pi*lambda),

    integral_0^infty lambda P(lambda) dlambda
      = 7*zeta(3)/(2*pi^2).

The derivation uses 1/sinh(x) = 2 sum_{k>=0} exp(-(2k+1)x) and
integral_0^infty x^2 exp(-a x) dx = 2/a^3, hence

    integral_0^infty x^2/sinh(x) dx
      = 4 sum_{k>=0} 1/(2k+1)^3
      = 4(1-2^-3) zeta(3)
      = 7 zeta(3)/2.

This is the direct spectral-weight moment.  It is deliberately kept separate
from factorized Wiener-Hopf chamber products and from repeated convolution.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 80


def P(lam):
    if lam == 0:
        return mp.mpf(1)
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def main():
    numeric = mp.quad(lambda x: x * P(x), [0, 1, mp.inf])
    target = 7 * mp.zeta(3) / (2 * mp.pi**2)
    err = abs(numeric - target)

    k = sp.symbols("k", integer=True, nonnegative=True)
    odd_sum = sp.summation(1 / (2 * k + 1) ** 3, (k, 0, sp.oo))
    symbolic = sp.simplify(4 * odd_sum / sp.pi**2)
    expected = 7 * sp.zeta(3) / (2 * sp.pi**2)

    print("spectral weight: P(lambda) = pi*lambda/sinh(pi*lambda)")
    print("numeric integral =", mp.nstr(numeric, 70))
    print("closed form      =", mp.nstr(target, 70))
    print("abs error        =", mp.nstr(err, 8))
    print("symbolic result  =", symbolic)
    print("symbolic check   =", sp.simplify(symbolic - expected))

    assert err < mp.mpf("1e-65")
    assert sp.simplify(symbolic - expected) == 0


if __name__ == "__main__":
    main()
