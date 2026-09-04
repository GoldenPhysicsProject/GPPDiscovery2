#!/usr/bin/env python3
"""Exact-structure audit for the continuous positive-real Gamma chamber.

For c > 0 and real x,

    B(c+ix,c-ix)
      = 4^{-c} ∫_R sech(y/2)^{2c} e^{ixy} dy,

hence

    |Γ(c+ix)|²
      = Γ(2c) 4^{-c} ∫_R sech(y/2)^{2c} e^{ixy} dy.

With

    rho_c(x) = 2^{2c-1}/(pi Γ(2c)) |Γ(c+ix)|²,

this becomes the inverse-Fourier representation

    rho_c(x) = (1/(2 pi)) ∫_R sech(y/2)^{2c} e^{ixy} dy,

so under the convention F[f](t)=∫ f(x)e^{-ixt}dx,

    F[rho_c](t) = sech(t/2)^{2c}.

The script checks both the logistic change of variables and the normalized
Fourier identity at high precision for nonintegral positive c.  It is
supporting discovery evidence only; the theorem is intended for Lean via the
Euler Beta integral, change of variables, and Fourier uniqueness.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 70


def sech(z):
    return 1 / mp.cosh(z)


def beta_side(c, x):
    return mp.beta(c + 1j * x, c - 1j * x)


def logistic_side(c, x):
    f = lambda y: mp.power(sech(y / 2), 2 * c) * mp.e ** (1j * x * y)
    return mp.power(4, -c) * mp.quad(f, [-mp.inf, 0, mp.inf])


def rho(c, x):
    return (
        mp.power(2, 2 * c - 1)
        / (mp.pi * mp.gamma(2 * c))
        * abs(mp.gamma(c + 1j * x)) ** 2
    )


def rho_inverse_fourier(c, x):
    f = lambda y: mp.power(sech(y / 2), 2 * c) * mp.e ** (1j * x * y)
    return mp.quad(f, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)


def rho_fourier(c, t):
    # rho_c is even, so use the real cosine transform for numerical stability.
    f = lambda x: 2 * rho(c, x) * mp.cos(t * x)
    return mp.quad(f, [0, mp.inf])


def relerr(a, b):
    scale = max(mp.mpf(1), abs(a), abs(b))
    return abs(a - b) / scale


def main():
    cx_grid = [
        (mp.mpf("0.37"), mp.mpf("0.0")),
        (mp.mpf("0.37"), mp.mpf("1.2")),
        (mp.mpf("0.75"), mp.mpf("2.3")),
        (mp.mpf("1.25"), mp.mpf("0.8")),
        (mp.mpf("2.4"), mp.mpf("3.1")),
    ]
    ct_grid = [
        (mp.mpf("0.37"), mp.mpf("0.4")),
        (mp.mpf("0.75"), mp.mpf("1.1")),
        (mp.mpf("1.25"), mp.mpf("2.0")),
        (mp.mpf("2.4"), mp.mpf("0.7")),
    ]

    tol = mp.mpf("1e-45")
    worst = mp.mpf(0)

    print("Beta/logistic identity:")
    for c, x in cx_grid:
        lhs = beta_side(c, x)
        rhs = logistic_side(c, x)
        err = relerr(lhs, rhs)
        worst = max(worst, err)
        print(f"  c={mp.nstr(c,6)} x={mp.nstr(x,6)} relerr={mp.nstr(err,8)}")
        if err > tol:
            raise SystemExit(f"Beta/logistic audit failed at c={c}, x={x}: {err}")

    print("\nNormalized inverse-Fourier identity:")
    for c, x in cx_grid:
        lhs = rho(c, x)
        rhs = rho_inverse_fourier(c, x)
        err = relerr(lhs, rhs)
        worst = max(worst, err)
        print(f"  c={mp.nstr(c,6)} x={mp.nstr(x,6)} relerr={mp.nstr(err,8)}")
        if err > tol:
            raise SystemExit(f"inverse-Fourier audit failed at c={c}, x={x}: {err}")

    print("\nForward Fourier identity F[rho_c](t)=sech(t/2)^(2c):")
    # Infinite-interval quadrature of oscillatory tails is the numerically
    # hardest check, so use a less aggressive but still high-precision bound.
    fourier_tol = mp.mpf("1e-30")
    for c, t in ct_grid:
        lhs = rho_fourier(c, t)
        rhs = mp.power(sech(t / 2), 2 * c)
        err = relerr(lhs, rhs)
        worst = max(worst, err)
        print(f"  c={mp.nstr(c,6)} t={mp.nstr(t,6)} relerr={mp.nstr(err,8)}")
        if err > fourier_tol:
            raise SystemExit(f"forward-Fourier audit failed at c={c}, t={t}: {err}")

    print(f"\nPASS; worst relative error = {mp.nstr(worst,10)}")
    print("Convolution consequence: rho_c * rho_d = rho_(c+d) by Fourier uniqueness.")


if __name__ == "__main__":
    main()
