#!/usr/bin/env python3
"""Exact bilateral moment hierarchy for the normalized celestial spectral weight.

This is a Codex/GPT discovery audit only.  It packages a consequence of the already
formalized Mellin bridge for

    P(lam) = pi*lam/sinh(pi*lam)

into the probability density

    rho(lam) = (2/pi) P(lam) = 2*lam/sinh(pi*lam).

Because rho is even, for n >= 0

    M_{2n} = int_R lam^(2n) rho(lam) dlam
           = 4 int_0^infty lam^(2n+1)/sinh(pi*lam) dlam
           = 8 Gamma(2n+2)/pi^(2n+2)
               * (1 - 2^(-(2n+2))) * zeta(2n+2).

The script checks the symbolic reductions at low order and independently verifies
normalization and moments by high-precision quadrature.  It does not assume the
sech^2 Fourier transform, so it is an independent audit of the moment side of the
celestial-spectral-weight/chamber identification.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def exact_moment(n: int) -> sp.Expr:
    s = 2 * n + 2
    return sp.simplify(
        8
        * sp.factorial(2 * n + 1)
        / sp.pi**s
        * (1 - sp.Rational(1, 2) ** s)
        * sp.zeta(s)
    )


def rho(x: mp.mpf) -> mp.mpf:
    if x == 0:
        return mp.mpf(2) / mp.pi
    return 2 * x / mp.sinh(mp.pi * x)


def numerical_moment(n: int) -> mp.mpf:
    # even integrand: double the positive half-line integral
    return 2 * mp.quad(lambda x: x ** (2 * n) * rho(x), [0, mp.inf])


def main() -> None:
    expected = [
        sp.Integer(1),
        sp.Rational(1, 2),
        sp.Integer(1),
        sp.Rational(17, 4),
        sp.Integer(31),
    ]
    got = [exact_moment(n) for n in range(len(expected))]
    assert got == expected, (got, expected)

    mp.mp.dps = 80
    tol = mp.mpf("1e-60")
    for n, ex in enumerate(expected):
        numeric = numerical_moment(n)
        target = mp.mpf(str(sp.N(ex, 80)))
        err = abs(numeric - target)
        assert err < tol, (n, numeric, target, err)
        print(f"M_{2*n} = {ex} ; quadrature error = {mp.nstr(err, 5)}")

    # In particular rho is normalized and has variance 1/2.
    assert expected[0] == 1
    assert expected[1] == sp.Rational(1, 2)

    print("general formula:")
    print("M_{2n} = 8*Gamma(2n+2)/pi^(2n+2)*(1-2^(-(2n+2)))*zeta(2n+2)")
    print("PASS: normalized bilateral celestial spectral-weight moment hierarchy")


if __name__ == "__main__":
    main()
