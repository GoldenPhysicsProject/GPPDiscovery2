#!/usr/bin/env python3
"""Verify the exact Pick/Nyquist fold of the finite CCM Weil matrix.

Discovery verification only; this is not an RH proof.

Checks:
  1. q_nm(y) is the Hermite-Loewner matrix of the reflected sine source.
  2. sin(2*pi*s)/(2*pi) produces exactly the identity matrix on integer nodes.
  3. the W02 pole matrix is a Loewner matrix of an explicit rational source.
  4. the regularized Archimedean + prime sources assemble the full CCM matrix.

Only mpmath and the Python standard library are required.
"""

from __future__ import annotations

import argparse
import mpmath as mp


def vm(k: int) -> mp.mpf:
    for p in range(2, k + 1):
        if k % p == 0:
            m = k
            while m % p == 0:
                m //= p
            return mp.log(p) if m == 1 else mp.mpf("0")
    return mp.mpf("0")


def psi(L, y, s):
    return mp.sin(2 * mp.pi * (1 - y / L) * s) / mp.pi


def h_nyquist(s):
    return mp.sin(2 * mp.pi * s) / (2 * mp.pi)


def omega(L, n, m, y):
    if n != m:
        return (
            mp.sin(2 * mp.pi * m * y / L)
            - mp.sin(2 * mp.pi * n * y / L)
        ) / (mp.pi * (n - m))
    return 2 * (1 - y / L) * mp.cos(2 * mp.pi * n * y / L)


def loewner(f, n, m):
    if n != m:
        return (f(n) - f(m)) / (n - m)
    return mp.diff(f, n)


def pole_source(L, s):
    a = L / (4 * mp.pi)
    c = 2 * L * mp.sinh(L / 4) ** 2 / mp.pi**2
    return c * s / (s * s + a * a)


def w02(L, n, m):
    return (
        32
        * L
        * mp.sinh(L / 4) ** 2
        * (L**2 - 16 * mp.pi**2 * m * n)
        / (
            (L**2 + 16 * mp.pi**2 * m**2)
            * (L**2 + 16 * mp.pi**2 * n**2)
        )
    )


def tail(L):
    return mp.log((mp.exp(L) + 1) / (mp.exp(L) - 1)) / 2


def rho(y):
    return mp.exp(y / 2) / (mp.exp(y) - mp.exp(-y))


def rr(y):
    return 1 / (mp.exp(y) - mp.exp(-y))


def arch_source(L, s):
    p0 = mp.sin(2 * mp.pi * s) / mp.pi

    def integrand(y):
        # The combined expression has a removable limit at zero.
        if abs(y) < mp.mpf("1e-30"):
            y = mp.mpf("1e-30")
        return rho(y) * psi(L, y, s) - rr(y) * p0

    c0 = mp.log(4 * mp.pi) + mp.euler
    return mp.quad(integrand, [0, L]) + (c0 - 2 * tail(L)) * h_nyquist(s)


def alpha(L, n):
    return mp.quad(
        lambda x: mp.sin(2 * mp.pi * n * x / L) * rho(x),
        [0, L],
    ) / mp.pi


def diagR(L, n):
    integ = mp.quad(
        lambda y: (
            mp.exp(y / 2)
            * 2
            * (1 - y / L)
            * mp.cos(2 * mp.pi * n * y / L)
            - 2
        )
        / (mp.exp(y) - mp.exp(-y)),
        [0, L],
    )
    return mp.log(4 * mp.pi) + mp.euler + integ - 2 * tail(L)


def prime_terms(lam):
    K = int(mp.floor(lam**2 + mp.mpf("1e-30")))
    return [(k, vm(k)) for k in range(2, K + 1) if vm(k) != 0]


def prime_source(L, lam, s):
    total = mp.mpf("0")
    for k, vk in prime_terms(lam):
        total += vk / mp.sqrt(k) * psi(L, mp.log(k), s)
    return total


def wp(L, lam, n, m):
    return sum(
        vk / mp.sqrt(k) * omega(L, n, m, mp.log(k))
        for k, vk in prime_terms(lam)
    )


def full_source(L, lam, s):
    return pole_source(L, s) - arch_source(L, s) - prime_source(L, lam, s)


def full_matrix_entry(L, lam, n, m):
    wr = diagR(L, n) if n == m else (alpha(L, m) - alpha(L, n)) / (n - m)
    return w02(L, n, m) - wr - wp(L, lam, n, m)


def check(lam=3, N=4, dps=60):
    mp.mp.dps = dps
    lam = mp.mpf(lam)
    L = 2 * mp.log(lam)
    tol = mp.mpf(10) ** (-(dps // 2))

    fold_err = mp.mpf("0")
    for yfrac in [mp.mpf("0.1"), mp.mpf("0.37"), mp.mpf("0.5"), mp.mpf("0.83")]:
        y = yfrac * L
        f = lambda s: psi(L, y, s)
        for n in range(-N, N + 1):
            for m in range(-N, N + 1):
                fold_err = max(fold_err, abs(omega(L, n, m, y) - loewner(f, n, m)))

    nyquist_err = mp.mpf("0")
    for n in range(-N, N + 1):
        for m in range(-N, N + 1):
            target = mp.mpf(1) if n == m else mp.mpf(0)
            nyquist_err = max(
                nyquist_err,
                abs(loewner(h_nyquist, n, m) - target),
            )

    pole_err = mp.mpf("0")
    pf = lambda s: pole_source(L, s)
    for n in range(-N, N + 1):
        for m in range(-N, N + 1):
            pole_err = max(pole_err, abs(w02(L, n, m) - loewner(pf, n, m)))

    source_err = mp.mpf("0")
    bf = lambda s: full_source(L, lam, s)
    for n in range(-N, N + 1):
        for m in range(-N, N + 1):
            source_err = max(
                source_err,
                abs(full_matrix_entry(L, lam, n, m) - loewner(bf, n, m)),
            )

    assert fold_err < tol, fold_err
    assert nyquist_err < tol, nyquist_err
    assert pole_err < tol, pole_err
    # Numerical differentiation/quadrature is the limiting operation here.
    assert source_err < mp.sqrt(tol), source_err

    print("Pick/Nyquist fold verification")
    print("lambda =", mp.nstr(lam, 12), "L =", mp.nstr(L, 12), "N =", N)
    print("fold error          =", mp.nstr(fold_err, 8))
    print("Nyquist I error     =", mp.nstr(nyquist_err, 8))
    print("pole-source error   =", mp.nstr(pole_err, 8))
    print("full-source error   =", mp.nstr(source_err, 8))
    print("status: all checks passed; discovery verification, not RH proof")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lambda-value", type=str, default="3")
    ap.add_argument("--N", type=int, default=4)
    ap.add_argument("--dps", type=int, default=60)
    args = ap.parse_args()
    check(args.lambda_value, args.N, args.dps)
