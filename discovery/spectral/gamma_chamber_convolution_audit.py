#!/usr/bin/env python3
"""Executable audit for the normalized Gamma/Mehler--Fock chamber semigroup.

For k >= 0 define

    rho_k(x) = 2^(2k+1)/(pi*Gamma(2k+2)) * |Gamma(k+1+i x)|^2.

With Fourier convention F[f](t)=integral_R f(x) exp(-i t x) dx, Barnes' transform
predicts

    F[rho_k](t) = sech(t/2)^(2k+2).

Hence rho_k * rho_l = rho_{k+l+1}, and rho_k = rho_0^{*(k+1)}.
This script numerically audits the transform and convolution identities at high
precision.  It is discovery support only; formal promotion requires an exact
Barnes/Fourier Gamma transform plus Fourier uniqueness in Lean.
"""

import mpmath as mp

mp.mp.dps = 60


def rho(k, x):
    return (
        mp.power(2, 2 * k + 1)
        / (mp.pi * mp.gamma(2 * k + 2))
        * abs(mp.gamma(k + 1 + 1j * x)) ** 2
    )


def rho_hat_numeric(k, t):
    f = lambda x: rho(k, x) * mp.cos(t * x)
    return 2 * mp.quad(f, [0, 1, 3, 7, mp.inf])


def rho_hat_exact(k, t):
    return mp.sech(t / 2) ** (2 * k + 2)


def conv_numeric(k, ell, x):
    f = lambda y: rho(k, y) * rho(ell, x - y)
    return mp.quad(f, [-mp.inf, -7, -3, 0, 3, 7, mp.inf])


def relerr(a, b):
    return abs(a - b) / max(mp.mpf("1e-50"), abs(b))


def main():
    transform_cases = [(0, 0), (0, 0.7), (1, 1.3), (2, 2.1), (4, 0.4)]
    conv_cases = [(0, 0, 0.0), (0, 1, 0.6), (1, 2, 1.1), (2, 2, -0.8)]

    print("Fourier-transform audit")
    max_tf = mp.mpf("0")
    for k, t in transform_cases:
        num = rho_hat_numeric(k, mp.mpf(t))
        ex = rho_hat_exact(k, mp.mpf(t))
        err = relerr(num, ex)
        max_tf = max(max_tf, err)
        print(f"k={k:2d} t={t:4.1f} relerr={mp.nstr(err, 8)}")

    print("\nConvolution audit")
    max_cv = mp.mpf("0")
    for k, ell, x in conv_cases:
        num = conv_numeric(k, ell, mp.mpf(x))
        ex = rho(k + ell + 1, mp.mpf(x))
        err = relerr(num, ex)
        max_cv = max(max_cv, err)
        print(
            f"k={k:2d} ell={ell:2d} x={x:4.1f} "
            f"relerr={mp.nstr(err, 8)}"
        )

    print("\nmax transform relerr:", mp.nstr(max_tf, 12))
    print("max convolution relerr:", mp.nstr(max_cv, 12))

    if max_tf > mp.mpf("1e-35") or max_cv > mp.mpf("1e-30"):
        raise SystemExit("audit tolerance exceeded")


if __name__ == "__main__":
    main()
