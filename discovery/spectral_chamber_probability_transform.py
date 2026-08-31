#!/usr/bin/env python3
"""Numerical audit of the exact Gamma/Mehler–Fock chamber probability law.

For

    rho_k(x) = 2^(2k+1)/(2k+1)! * x/sinh(pi*x)
               * prod_{j=1}^k (j^2+x^2),

the Gamma product identity rewrites the density as

    rho_k(x) = 2^(2k+1)/(pi*Gamma(2k+2))
               * Gamma(k+1+i*x) Gamma(k+1-i*x).

Barnes' vertical-line Gamma integral (DLMF 5.13.1, with a=b=k+1,
c=0, z=exp(-t)) gives exactly

    integral_R rho_k(x) dx = 1,
    integral_R exp(i*t*x) rho_k(x) dx = sech(t/2)^(2k+2),
    E[X] = 0,
    Var(X) = (k+1)/2.

Hence the chamber family has the exact convolution semigroup law

    rho_k * rho_l = rho_(k+l+1),
    rho_k = rho_0 ^ *(k+1).

This corrects the discarded repeated-sech extrapolation: rho_k is NOT obtained
by convolving a sech density in x-space.  Rather, rho_0(x)=2x/sinh(pi*x) is the
convolution generator, and its characteristic function is sech(t/2)^2.

The script independently checks normalization, the transform, variance, and
representative convolution identities at high precision.
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


def convolution(k: int, ell: int, x: mp.mpf) -> mp.mpf:
    f = lambda y: rho(k, y) * rho(ell, x - y)
    return mp.quad(f, [-mp.inf, -8, -3, 0, 3, 8, mp.inf])


def main() -> None:
    tol = mp.mpf("1e-45")
    conv_tol = mp.mpf("1e-38")
    print("Gamma/Mehler–Fock chamber probability/convolution audit")
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

    for k, ell in ((0, 0), (0, 1), (1, 1), (1, 2)):
        target = k + ell + 1
        for x in map(mp.mpf, ("0", "0.5", "1.3")):
            lhs = convolution(k, ell, x)
            rhs = rho(target, x)
            err = abs(lhs - rhs)
            print(
                f"conv ({k},{ell}) x={x}: lhs={mp.nstr(lhs, 40)} "
                f"rho_{target}={mp.nstr(rhs, 40)} err={mp.nstr(err, 5)}"
            )
            if err > conv_tol:
                raise AssertionError((k, ell, x, lhs, rhs, err))

    print(
        "PASS: normalization, sech-power transform, variance, and chamber "
        "convolution semigroup all agree."
    )


if __name__ == "__main__":
    main()
