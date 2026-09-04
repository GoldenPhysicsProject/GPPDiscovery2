#!/usr/bin/env python3
"""Exact/numerical audit of cumulants for the continuous Gamma chamber law.

For c>0,

    rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2

has characteristic function

    phi_c(t) = sech(t/2)^(2c).

Hence log phi_c(t) = 2c log sech(t/2), so every cumulant is linear in c.
This script expands the exact characteristic exponent and independently checks the
first even moments by numerical integration.  Odd cumulants vanish by symmetry.

Discovery result:
    kappa_2 = c/2
    kappa_4 = c/4
    kappa_6 = c/2
    kappa_8 = 17 c/8

The semigroup rho_c * rho_d = rho_(c+d) therefore has additive cumulants exactly,
which gives a concrete fluctuation-geometry bridge to the prime-gas/Fisher front.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 50


def rho(c, x):
    return (mp.power(2, 2*c - 1) /
            (mp.pi * mp.gamma(2*c)) *
            abs(mp.gamma(c + 1j*x))**2)


def even_moment(c, order):
    f = lambda x: x**order * rho(c, x)
    return 2 * mp.quad(f, [0, mp.inf])


def main():
    t, c = sp.symbols('t c', real=True)
    logphi = 2*c*sp.log(1/sp.cosh(t/2))
    print('log characteristic function series:')
    print(sp.series(logphi, t, 0, 10))

    # log phi(t) = sum_n kappa_n (i t)^n/n!
    kappas = {}
    for n in (2, 4, 6, 8):
        coeff = sp.expand(sp.series(logphi, t, 0, n+1).removeO()).coeff(t, n)
        kappa = sp.simplify(coeff * sp.factorial(n) / (sp.I**n))
        kappas[n] = kappa
        print(f'kappa_{n} = {kappa}')

    expected = {
        2: c/2,
        4: c/4,
        6: c/2,
        8: 17*c/8,
    }
    for n, rhs in expected.items():
        assert sp.simplify(kappas[n] - rhs) == 0

    # Moment-cumulant checks for a few noninteger c values.
    # mu2=k2; mu4=k4+3k2^2; mu6=k6+15k4*k2+15k2^3.
    for cv in [mp.mpf('0.37'), mp.mpf('0.5'), mp.mpf('1.25'), mp.mpf('2.7')]:
        k2 = cv/2
        k4 = cv/4
        k6 = cv/2
        predictions = {
            2: k2,
            4: k4 + 3*k2**2,
            6: k6 + 15*k4*k2 + 15*k2**3,
        }
        for n, pred in predictions.items():
            got = even_moment(cv, n)
            rel = abs(got-pred)/max(mp.mpf(1), abs(got), abs(pred))
            print(f'c={mp.nstr(cv,6)} mu_{n} relerr={mp.nstr(rel,12)}')

    print('\nExact fluctuation identities:')
    print('Var[rho_c] = c/2')
    print('fourth cumulant = c/4')
    print('sixth cumulant = c/2')
    print('eighth cumulant = 17 c/8')
    print('All cumulants are additive under c -> c+d by the convolution semigroup.')


if __name__ == '__main__':
    main()
