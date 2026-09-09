#!/usr/bin/env python3
"""Odd-mode Gamma-difference random-series realization of the Gamma-square chamber law.

Codex/GPT Golden Physics discovery track.

For a>0 the normalized Gamma-square/chamber characteristic function is

    phi_a(t) = sech(t/2)^(2a).

Euler's odd cosh product gives

    phi_a(t)
      = product_{n>=0} (1 + t^2 / ((2n+1)^2 pi^2))^(-2a).

Each factor is the characteristic function of a difference of two independent
Gamma(shape=2a, rate=(2n+1)pi) random variables. Hence the chamber law is the
L2-convergent sum of independent odd-mode Gamma differences.

This script audits the product numerically and verifies that summing the exact
mode cumulants reproduces the Bernoulli chamber cumulants. It is a discovery
artifact, not a Lean proof.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 70


def chamber_cf(t, a):
    return mp.sech(t / 2) ** (2 * a)


def finite_mode_cf(t, a, N):
    out = mp.mpf(1)
    for n in range(N):
        rate = (2 * n + 1) * mp.pi
        out *= (1 + (t / rate) ** 2) ** (-2 * a)
    return out


def finite_variance(a, N):
    # Difference of two Gamma(2a, rate) variables has variance 4a/rate^2.
    return mp.fsum(4 * a / (((2 * n + 1) * mp.pi) ** 2) for n in range(N))


def symbolic_cumulant_check(max_m=8):
    a = sp.symbols("a", positive=True)
    for m in range(1, max_m + 1):
        # Even cumulant of Gamma(alpha,rate)-Gamma(alpha,rate), alpha=2a:
        # 2 alpha (2m-1)! / rate^(2m) = 4a(2m-1)!/rate^(2m).
        mode_sum = sp.simplify(
            4 * a * sp.factorial(2 * m - 1) / sp.pi ** (2 * m)
            * (1 - sp.Rational(1, 2) ** (2 * m)) * sp.zeta(2 * m)
        )
        chamber = sp.simplify(
            a * (2 ** (2 * m) - 1) * abs(sp.bernoulli(2 * m)) / m
        )
        assert sp.simplify(mode_sum - chamber) == 0, (m, mode_sum, chamber)


def main():
    symbolic_cumulant_check(10)

    for a in (mp.mpf("0.5"), mp.mpf("1"), mp.mpf("1.7")):
        for t in (mp.mpf("0.3"), mp.mpf("1"), mp.mpf("3")):
            target = chamber_cf(t, a)
            # Product convergence is O(1/N); use two increasing truncations and
            # demand monotone approach from above, as every omitted factor < 1.
            p1 = finite_mode_cf(t, a, 2000)
            p2 = finite_mode_cf(t, a, 10000)
            assert p1 >= p2 >= target
            assert abs(p2 - target) < mp.mpf("2e-5")

        v = finite_variance(a, 100000)
        assert abs(v - a / 2) < mp.mpf("2e-6")

    print("Exact product law:")
    print("  sech(t/2)^(2a) = PROD_{n>=0} (1+t^2/((2n+1)^2*pi^2))^(-2a)")
    print("Random-series interpretation:")
    print("  X_a = SUM_{n>=0} (G_{n,+}-G_{n,-}),")
    print("  G_{n,+/-} iid Gamma(shape=2a, rate=(2n+1)pi), independent over n")
    print("  convergence holds in L2 because SUM Var(mode_n)=a/2 < infinity")
    print("Cumulants:")
    print("  kappa_{2m}=a(2^(2m)-1)|B_{2m}|/m, kappa_{2m+1}=0")
    print("PASS: odd-mode Gamma-difference factorization reproduces the chamber law and all audited cumulants")


if __name__ == "__main__":
    main()
