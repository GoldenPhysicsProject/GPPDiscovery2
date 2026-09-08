#!/usr/bin/env python3
"""Executable audit of continuous Gamma-chamber even moments and cumulants.

Discovery evidence only: the algebraic recurrence is formalized separately in
GPPVerify2.  Here we directly integrate the normalized Gamma density

    rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2

and compare with the recurrence-predicted formulas.  The eighth moment is the
next chamber-step consequence; the first four nonzero cumulants then collapse
to quantities linear in c, as expected for an infinitely divisible chamber
family, but this script by itself is not a proof of infinite divisibility.
"""

import mpmath as mp

mp.mp.dps = 60
pi = mp.pi


def rho(c, x):
    z = mp.gamma(c + 1j * x)
    return (mp.power(2, 2 * c - 1) / (pi * mp.gamma(2 * c))) * abs(z) ** 2


def even_moment(c, order):
    assert order % 2 == 0
    f = lambda x: (x ** order) * rho(c, x)
    return 2 * mp.quad(f, [0, 1, 3, 7, mp.inf])


def m2_exact(c):
    return c / 2


def m4_exact(c):
    return c * (3 * c + 1) / 4


def m6_exact(c):
    return c * (15 * c * c + 15 * c + 4) / 8


def m8_exact(c):
    return c * (105 * c**3 + 210 * c**2 + 147 * c + 34) / 16


def cumulants_from_even_moments(m2, m4, m6, m8):
    k2 = m2
    k4 = m4 - 3 * m2**2
    k6 = m6 - 15 * m4 * m2 + 30 * m2**3
    k8 = m8 - 28 * m6 * m2 - 35 * m4**2 + 420 * m4 * m2**2 - 630 * m2**4
    return k2, k4, k6, k8


for c in [mp.mpf("0.2"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("1.7"), mp.mpf("3.25")]:
    norm = 2 * mp.quad(lambda x: rho(c, x), [0, 1, 3, 7, mp.inf])
    m2 = even_moment(c, 2)
    m4 = even_moment(c, 4)
    m6 = even_moment(c, 6)
    m8 = even_moment(c, 8)

    assert mp.almosteq(norm, 1)
    assert mp.almosteq(m2, m2_exact(c))
    assert mp.almosteq(m4, m4_exact(c))
    assert mp.almosteq(m6, m6_exact(c))
    assert mp.almosteq(m8, m8_exact(c))

    excess = m4 / (m2 * m2) - 3
    assert mp.almosteq(excess, 1 / c)

    k2, k4, k6, k8 = cumulants_from_even_moments(m2, m4, m6, m8)
    assert mp.almosteq(k2, c / 2)
    assert mp.almosteq(k4, c / 4)
    assert mp.almosteq(k6, c / 2)
    assert mp.almosteq(k8, 17 * c / 8)

    print("c =", c)
    print("  normalization error =", abs(norm - 1))
    print("  M2 error =", abs(m2 - m2_exact(c)))
    print("  M4 error =", abs(m4 - m4_exact(c)))
    print("  M6 error =", abs(m6 - m6_exact(c)))
    print("  M8 error =", abs(m8 - m8_exact(c)))
    print("  excess kurtosis =", excess, " target =", 1 / c)
    print("  cumulants k2,k4,k6,k8 =", k2, k4, k6, k8)

# c=1 is the normalized celestial spectral weight rho_1=(2/pi)P.
c = mp.mpf("1")
assert mp.almosteq(m2_exact(c), mp.mpf("0.5"))
assert mp.almosteq(m4_exact(c), mp.mpf("1"))
assert mp.almosteq(m6_exact(c), mp.mpf("4.25"))
assert mp.almosteq(m8_exact(c), mp.mpf("31"))
print("c=1 exact moments: M2=1/2, M4=1, M6=17/4, M8=31")
print("cumulants: k2=1/2, k4=1/4, k6=1/2, k8=17/8")
print("all executable checks passed")
