#!/usr/bin/env python3
"""Executable audit of the corrected continuous-sech Lévy integrability target.

For c > 0,
    nu_c(x) = c / (|x| sinh(pi |x|))
has the origin asymptotic
    nu_c(x) ~ c / (pi x^2),
so nu_c itself is NOT locally integrable at x=0.

The correct Lévy condition is
    integral_R min(1,x^2) nu_c(x) dx < infinity,
and the exponent integrand
    (1-cos(t x)) nu_c(x)
is locally integrable because the quadratic zero of 1-cos(t x) cancels the
x^-2 singularity.

This script verifies the asymptotic ratios and numerically checks convergence of
both the Lévy-weighted integral and the Lévy-Khintchine exponent integral.
"""

from mpmath import mp

mp.dps = 60


def nu(c, x):
    x = mp.mpf(x)
    return mp.mpf(c) / (abs(x) * mp.sinh(mp.pi * abs(x)))


def origin_ratio(c, x):
    """Ratio nu_c(x) / (c/(pi x^2)); tends to 1 as x -> 0."""
    x = mp.mpf(x)
    return nu(c, x) * mp.pi * x * x / mp.mpf(c)


def compensated_origin_ratio(c, t, x):
    """Ratio (1-cos(tx))*nu_c(x) / (c*t^2/(2*pi)); tends to 1."""
    x = mp.mpf(x)
    target = mp.mpf(c) * mp.mpf(t) ** 2 / (2 * mp.pi)
    return (1 - mp.cos(mp.mpf(t) * x)) * nu(c, x) / target


def levy_weighted_integral(c, eps):
    """2*int_eps^infty min(1,x^2) nu_c(x) dx."""
    c = mp.mpf(c)
    eps = mp.mpf(eps)
    near = mp.quad(lambda x: x * x * nu(c, x), [eps, 1])
    tail = mp.quad(lambda x: nu(c, x), [1, mp.inf])
    return 2 * (near + tail)


def exponent_integral(c, t, eps):
    """2*int_eps^infty (1-cos(tx)) nu_c(x) dx."""
    c = mp.mpf(c)
    t = mp.mpf(t)
    eps = mp.mpf(eps)
    f = lambda x: (1 - mp.cos(t * x)) * nu(c, x)
    return 2 * mp.quad(f, [eps, 1, mp.inf])


def expected_exponent(c, t):
    """-log Phi_c(t) = 2 c log cosh(t/2)."""
    return 2 * mp.mpf(c) * mp.log(mp.cosh(mp.mpf(t) / 2))


def main():
    c = mp.mpf("0.7")
    t = mp.mpf("1.3")

    print("origin asymptotic nu_c(x) ~ c/(pi*x^2)")
    for x in ["1e-2", "1e-4", "1e-6", "1e-8"]:
        print(x, mp.nstr(origin_ratio(c, x), 30))

    print("\ncompensated integrand tends to c*t^2/(2*pi)")
    for x in ["1e-2", "1e-4", "1e-6", "1e-8"]:
        print(x, mp.nstr(compensated_origin_ratio(c, t, x), 30))

    print("\nLevy-weighted integral convergence")
    vals = []
    for eps in ["1e-2", "1e-3", "1e-4", "1e-5"]:
        val = levy_weighted_integral(c, eps)
        vals.append(val)
        print(eps, mp.nstr(val, 30))
    assert abs(vals[-1] - vals[-2]) < mp.mpf("1e-4")

    print("\nExponent integral convergence and exact target")
    target = expected_exponent(c, t)
    vals = []
    for eps in ["1e-2", "1e-3", "1e-4", "1e-5"]:
        val = exponent_integral(c, t, eps)
        vals.append(val)
        print(eps, mp.nstr(val, 30), "err", mp.nstr(abs(val - target), 8))
    print("target", mp.nstr(target, 30))
    assert abs(vals[-1] - target) < mp.mpf("1e-5")

    print("\nPASS: nu itself is singular/non-L1 at zero, but the Levy-weighted and")
    print("quadratically compensated integrands converge as required.")


if __name__ == "__main__":
    main()
