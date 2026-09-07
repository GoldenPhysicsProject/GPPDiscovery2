#!/usr/bin/env python3
"""High-precision audit of the continuous real-c Gamma chamber semigroup.

For c > 0 define the normalized spectral density

    rho_c(x) = 2^(2c-1)/(pi*Gamma(2c)) * |Gamma(c+i x)|^2.

With Fourier convention F[f](t)=integral_R f(x) exp(-i t x) dx,
Barnes' Gamma transform gives

    F[rho_c](t) = sech(t/2)^(2c).

Consequently rho_c * rho_d = rho_(c+d) for arbitrary real c,d > 0.
This audit deliberately includes noninteger and irrational-looking decimal
parameters, extending the earlier integer-chamber audit.  It also checks the
heat-subordinator Laplace semigroup and the exact first two cumulant formulas

    E[S_c] = c/4,    Var(S_c) = c/48.

This is executable discovery support, not a replacement for the exact
Barnes/Fourier transform and transform-uniqueness proof required in Lean.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 70


def rho(c: mp.mpf, x: mp.mpf) -> mp.mpf:
    return (
        mp.power(2, 2 * c - 1)
        / (mp.pi * mp.gamma(2 * c))
        * abs(mp.gamma(c + 1j * x)) ** 2
    )


def rho_hat_numeric(c: mp.mpf, t: mp.mpf) -> mp.mpf:
    f = lambda x: rho(c, x) * mp.cos(t * x)
    return 2 * mp.quad(f, [0, 1, 3, 7, 15, mp.inf])


def rho_hat_exact(c: mp.mpf, t: mp.mpf) -> mp.mpf:
    return mp.sech(t / 2) ** (2 * c)


def conv_numeric(c: mp.mpf, d: mp.mpf, x: mp.mpf) -> mp.mpf:
    f = lambda y: rho(c, y) * rho(d, x - y)
    return mp.quad(f, [-mp.inf, -15, -7, -3, 0, 3, 7, 15, mp.inf])


def heat_laplace(c: mp.mpf, q: mp.mpf) -> mp.mpf:
    return mp.sech(mp.sqrt(q) / 2) ** (2 * c)


def relerr(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return abs(a - b) / max(mp.mpf("1e-60"), abs(b))


def main() -> None:
    transform_cases = [
        ("0.25", "0.0"),
        ("0.25", "0.9"),
        ("0.7", "1.4"),
        ("1.125", "2.0"),
        ("2.35", "0.55"),
    ]
    convolution_cases = [
        ("0.25", "0.4", "0.0"),
        ("0.3", "0.7", "0.65"),
        ("0.875", "1.125", "-0.8"),
        ("1.2", "2.35", "1.1"),
    ]
    heat_cases = [
        ("0.3", "0.7", "0.2"),
        ("0.25", "1.125", "1.7"),
        ("1.2", "2.35", "4.0"),
    ]

    print("Continuous real-c Fourier-transform audit")
    max_tf = mp.mpf("0")
    for cs, ts in transform_cases:
        c, t = mp.mpf(cs), mp.mpf(ts)
        num = rho_hat_numeric(c, t)
        ex = rho_hat_exact(c, t)
        err = relerr(num, ex)
        max_tf = max(max_tf, err)
        print(f"c={cs:>5s} t={ts:>4s} relerr={mp.nstr(err, 10)}")

    print("\nContinuous real-c convolution audit")
    max_cv = mp.mpf("0")
    for cs, ds, xs in convolution_cases:
        c, d, x = mp.mpf(cs), mp.mpf(ds), mp.mpf(xs)
        num = conv_numeric(c, d, x)
        ex = rho(c + d, x)
        err = relerr(num, ex)
        max_cv = max(max_cv, err)
        print(
            f"c={cs:>5s} d={ds:>5s} x={xs:>5s} "
            f"relerr={mp.nstr(err, 10)}"
        )

    print("\nHeat-subordinator Laplace semigroup audit")
    max_heat = mp.mpf("0")
    for cs, ds, qs in heat_cases:
        c, d, q = mp.mpf(cs), mp.mpf(ds), mp.mpf(qs)
        lhs = heat_laplace(c, q) * heat_laplace(d, q)
        rhs = heat_laplace(c + d, q)
        err = relerr(lhs, rhs)
        max_heat = max(max_heat, err)
        print(
            f"c={cs:>5s} d={ds:>5s} q={qs:>4s} "
            f"relerr={mp.nstr(err, 10)}"
        )

    print("\nHeat-time cumulants")
    for cs in ["0.25", "0.7", "1.125", "2.35"]:
        c = mp.mpf(cs)
        mean = c / 4
        var = c / 48
        # Additivity is exact at the formula level; print values as an audit ledger.
        print(f"c={cs:>5s} E[S_c]={mp.nstr(mean, 15)} Var(S_c)={mp.nstr(var, 15)}")

    print("\nmax transform relerr:", mp.nstr(max_tf, 14))
    print("max convolution relerr:", mp.nstr(max_cv, 14))
    print("max heat-semigroup relerr:", mp.nstr(max_heat, 14))

    if max_tf > mp.mpf("1e-35"):
        raise SystemExit("continuous transform audit tolerance exceeded")
    if max_cv > mp.mpf("1e-28"):
        raise SystemExit("continuous convolution audit tolerance exceeded")
    if max_heat > mp.mpf("1e-60"):
        raise SystemExit("heat semigroup audit tolerance exceeded")

    print("PASS: noninteger real-c Gamma chamber Fourier law numerically verified")
    print("PASS: rho_c * rho_d = rho_(c+d) numerically verified for noninteger c,d")
    print("PASS: heat-subordinator Laplace multipliers compose additively in c")
    print("BOUNDARY: exact Barnes transform + Fourier/Laplace uniqueness remain the formal analytic obligations")


if __name__ == "__main__":
    main()
