#!/usr/bin/env python3
"""Numerical audit of the continuous Gamma/Wiener--Hopf chamber law.

For c>0 define

    rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2.

The beta-integral substitution u=e^y/(1+e^y) gives the exact transform pair

    int_R exp(i t x) rho_c(x) dx = sech(t/2)^(2c).

Consequently Fourier uniqueness predicts rho_c * rho_d = rho_(c+d).
This script checks both identities for noninteger and integer parameters.
It is discovery/audit code, not a formal proof.
"""

import mpmath as mp

mp.mp.dps = 50


def rho(c, x):
    return (mp.power(2, 2*c - 1) /
            (mp.pi * mp.gamma(2*c)) *
            abs(mp.gamma(c + 1j*x))**2)


def sech(z):
    return 1 / mp.cosh(z)


def fourier_rho(c, t):
    f = lambda x: mp.cos(t*x) * rho(c, x)  # rho_c is even
    return 2 * mp.quad(f, [0, mp.inf])


def convolution(c, d, x):
    f = lambda y: rho(c, y) * rho(d, x-y)
    return mp.quad(f, [-mp.inf, 0, mp.inf])


def relerr(a, b):
    return abs(a-b) / max(mp.mpf(1), abs(a), abs(b))


def main():
    cs = [mp.mpf('0.37'), mp.mpf('0.5'), mp.mpf('1.25'), mp.mpf('2.7')]
    ts = [mp.mpf('0'), mp.mpf('0.4'), mp.mpf('1.3'), mp.mpf('3.0')]

    print('Fourier transform checks')
    worst = mp.mpf('0')
    for c in cs:
        for t in ts:
            lhs = fourier_rho(c, t)
            rhs = sech(t/2)**(2*c)
            e = relerr(lhs, rhs)
            worst = max(worst, e)
            print(f'c={mp.nstr(c,6)} t={mp.nstr(t,6)} relerr={mp.nstr(e,8)}')
    print('worst Fourier relative error:', mp.nstr(worst, 12))

    print('\nConvolution-semigroup checks')
    pairs = [(mp.mpf('0.37'), mp.mpf('0.83')),
             (mp.mpf('0.5'), mp.mpf('1.25')),
             (mp.mpf('1.1'), mp.mpf('2.3'))]
    xs = [mp.mpf('0'), mp.mpf('0.7'), mp.mpf('2.0')]
    worst = mp.mpf('0')
    for c, d in pairs:
        for x in xs:
            lhs = convolution(c, d, x)
            rhs = rho(c+d, x)
            e = relerr(lhs, rhs)
            worst = max(worst, e)
            print(f'c={mp.nstr(c,6)} d={mp.nstr(d,6)} x={mp.nstr(x,6)} relerr={mp.nstr(e,8)}')
    print('worst convolution relative error:', mp.nstr(worst, 12))

    # Exact derivation checkpoint printed for reproducibility.
    print('\nExact beta-substitution identity used:')
    print('|Gamma(c+i x)|^2 = Gamma(2c) 4^(-c) '
          '* integral_R sech(y/2)^(2c) exp(i x y) dy, c>0.')


if __name__ == '__main__':
    main()
