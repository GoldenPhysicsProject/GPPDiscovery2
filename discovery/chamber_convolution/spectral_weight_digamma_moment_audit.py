#!/usr/bin/env python3
"""High-precision audit of the exact P(lambda)-digamma moment.

Source-mined target from the focused principal-series/conical-block manuscript:

    (1/(2*pi)) * int_R P(lambda) Re psi(1/2 + i lambda/2) d lambda
      = 1/8 + (1/4) psi(1/2),

where P(lambda)=pi*lambda/sinh(pi*lambda), with P(0)=1 by continuity.

This is an Archimedean spectral-weight identity only.  It does not identify P
with the genuine SL(2,C) Plancherel density and it supplies no RH implication.
"""

import mpmath as mp

mp.mp.dps = 70


def P(lam):
    if lam == 0:
        return mp.mpf(1)
    return mp.pi * lam / mp.sinh(mp.pi * lam)


def integrand(lam):
    return P(lam) * mp.re(mp.digamma(mp.mpf("0.5") + 0.5j * lam))


def main():
    lhs = mp.quad(integrand, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
    rhs = mp.mpf(1) / 8 + mp.digamma(mp.mpf("0.5")) / 4
    err = abs(lhs - rhs)

    print("lhs =", mp.nstr(lhs, 60))
    print("rhs =", mp.nstr(rhs, 60))
    print("abs error =", mp.nstr(err, 12))

    # Independent closed-form simplification psi(1/2)=-gamma-2 log 2.
    rhs_elementary = mp.mpf(1) / 8 - mp.euler / 4 - mp.log(2) / 2
    err_elementary = abs(rhs - rhs_elementary)
    print("rhs elementary =", mp.nstr(rhs_elementary, 60))
    print("closed-form consistency error =", mp.nstr(err_elementary, 12))

    assert err < mp.mpf("1e-55")
    assert err_elementary < mp.mpf("1e-65")


if __name__ == "__main__":
    main()
