#!/usr/bin/env python3
"""High-precision audit of the exact Mehler-Fock convolution-power family."""

import mpmath as mp

mp.mp.dps = 60


def rho_m(x, m):
    return (2 ** (2 * m - 1) / (mp.pi * mp.gamma(2 * m))) * abs(mp.gamma(m + 1j * x)) ** 2


def rho_base(x):
    if x == 0:
        return 2 / mp.pi
    return 2 * x / mp.sinh(mp.pi * x)


def rho_poly(x, m):
    prod = mp.mpf(1)
    for j in range(1, m):
        prod *= j * j + x * x
    return (2 ** (2 * m - 2) / mp.gamma(2 * m)) * prod * rho_base(x)


def ft_numeric(k, m):
    f = lambda x: mp.cos(k * x) * rho_m(x, m)
    return mp.quad(f, [-mp.inf, mp.inf])


for m in range(1, 6):
    norm = mp.quad(lambda x: rho_m(x, m), [-mp.inf, mp.inf])
    assert abs(norm - 1) < mp.mpf('1e-45')

    for x in [mp.mpf('0'), mp.mpf('0.2'), mp.mpf('1.1'), mp.mpf('3.7')]:
        a = rho_m(x, m)
        b = rho_poly(x, m)
        assert abs(a - b) < mp.mpf('1e-45') * max(1, abs(a), abs(b))

    for k in [mp.mpf('0.2'), mp.mpf('0.7'), mp.mpf('1.4')]:
        lhs = ft_numeric(k, m)
        rhs = mp.sech(k / 2) ** (2 * m)
        assert abs(lhs - rhs) < mp.mpf('1e-40')

print('Mehler-Fock convolution family audit: PASS')
