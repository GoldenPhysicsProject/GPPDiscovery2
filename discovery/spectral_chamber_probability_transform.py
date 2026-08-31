#!/usr/bin/env python3
"""Numerical audit of the exact Gamma/Mehler–Fock chamber probability law.

For

    rho_k(x) = 2^(2k+1)/(2k+1)! * x/sinh(pi*x)
               * prod_{j=1}^k (j^2+x^2),

the Gamma product identity rewrites the density as

    rho_k(x) = 2^(2k+1)/(pi*Gamma(2k+2))
               * Gamma(k+1+i*x) Gamma(k+1-i*x).

The standard Fourier transform of |Gamma(a+i*x)|^2 then predicts

    integral_R rho_k(x) dx = 1,
    integral_R exp(i*t*x) rho_k(x) dx = sech(t/2)^(2k+2),
    E[X] = 0,
    Var(X) = (k+1)/2.

This is NOT the discarded claim that the rho_k themselves are repeated sech
convolutions.  Rather, their characteristic functions are powers of sech.
This script independently checks normalization, the transform, and variance at
high precision for several chambers.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 60


def rho(k: int, x: mp.mpf) -> mp.mpf:
    if k < 0:
        raise ValueError("k must be nonnegative")
    if x == 0:
        base = 1 / mp.pi
    else:
        base = x / mp.sinh(mp.pi * x)
    prod = mp.mpf(1)
    for j in range(1, k + 1):
        prod *= j * j + x * x
    return mp.power(2, 2 * k + 1) / mp.factorial(2 * k + 1) * base * prod


def integrate_even(f):
    return 2 * mp.quad(f, [0, 1, 3, 8, mp.inf])


def normalization(k: int) -> mp.mpf:
    return integrate_even(lambda x: rho(k, x))


def characteristic(k: int, t: mp.mpf) -> mp.mpf:
    return integrate_even(lambda x: mp.cos(t * x) * rho(k, x))


def characteristic_exact(k: int, t: mp.mpf) -> mp.mpf:
    return mp.sech(t / 2) ** (2 * k + 2)


def variance(k: int) -> mp.mpf:
    return integrate_even(lambda x: x * x * rho(k, x))


def variance_exact(k: int) -> mp.mpf:
    return mp.mpf(k + 1) / 2


def main() -> None:
    tol = mp.mpf("1e-45")
    print("Gamma/Mehler–Fock chamber probability audit")
    print(f"mp.dps={mp.mp.dps}")

    for k in range(5):
        z = normalization(k)
        var = variance(k)
        print(f"k={k}: integral={mp.nstr(z, 50)}")
        print(
            "     variance="
            f"{mp.nstr(var, 50)}  exact={mp.nstr(variance_exact(k), 50)}"
        )
        if abs(z - 1) > tol:
            raise AssertionError((k, "normalization", z))
        if abs(var - variance_exact(k)) > tol:
            raise AssertionError((k, "variance", var))

        for t in map(mp.mpf, ("0.3", "1.0", "2.0")):
            lhs = characteristic(k, t)
            rhs = characteristic_exact(k, t)
            err = abs(lhs - rhs)
            print(
                f"     t={t}: FT={mp.nstr(lhs, 45)} "
                f"sech-power={mp.nstr(rhs, 45)} err={mp.nstr(err, 5)}"
            )
            if err > tol:
                raise AssertionError((k, t, lhs, rhs, err))

    print("PASS: normalization, sech-power transform, and variance all agree.")


if __name__ == "__main__":
    main()
