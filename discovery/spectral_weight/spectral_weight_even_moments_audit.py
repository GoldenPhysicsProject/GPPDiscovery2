#!/usr/bin/env python3
"""High-precision audit of exact even moments of P(lambda)=pi*lambda/sinh(pi*lambda)."""

import mpmath as mp

mp.mp.dps = 80


def P(lam):
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def moment_numeric(n):
    f = lambda x: (x ** (2 * n)) * P(x)
    return mp.quad(f, [0, 1, mp.inf])


def moment_zeta(n):
    return (
        2
        * mp.factorial(2 * n + 1)
        / (mp.pi ** (2 * n + 1))
        * (1 - mp.power(2, -(2 * n + 2)))
        * mp.zeta(2 * n + 2)
    )


def moment_bernoulli(n):
    return (
        ((-1) ** n)
        * (2 ** (2 * n + 2) - 1)
        * mp.bernpoly(2 * n + 2, 0)
        / (2 * n + 2)
        * mp.pi
    )


for n in range(8):
    num = moment_numeric(n)
    zeta = moment_zeta(n)
    bern = moment_bernoulli(n)
    print(f"n={n}")
    print(" numeric   =", mp.nstr(num, 60))
    print(" zeta      =", mp.nstr(zeta, 60))
    print(" bernoulli =", mp.nstr(bern, 60))
    print(" |num-zeta|=", mp.nstr(abs(num - zeta), 8))
    print(" |zeta-bern|=", mp.nstr(abs(zeta - bern), 8))
    print()

print("normalized E[lambda^2] =", mp.nstr((4 / mp.pi) * moment_zeta(1), 40))
print("normalized E[lambda^4] =", mp.nstr((4 / mp.pi) * moment_zeta(2), 40))
