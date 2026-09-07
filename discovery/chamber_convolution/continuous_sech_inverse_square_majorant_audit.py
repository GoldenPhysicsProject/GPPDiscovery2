#!/usr/bin/env python3
"""Executable audit for the continuous-sech compensated Levy majorants.

Codex/GPT workbench only.

The certified pointwise bounds suggest a simpler integrability route than an
exponential tail estimate:

    nu_c(x) <= c / (pi |x|^2),               x != 0,
    K_c(t,x) <= 2 c / (pi |x|^2),            x != 0,
    K_c(t,x) <= t^2 c / (2 pi),              all x,

where

    nu_c(x) = c / (|x| sinh(pi |x|)),
    K_c(t,x) = (1-cos(tx)) nu_c(x).

Splitting at |x|=1 gives the explicit integrable majorant mass

    integral_R K_c(t,x) dx <= c (t^2 + 4) / pi.

The exact Levy-Khintchine target, independently known numerically, is

    integral_R K_c(t,x) dx = 2 c log cosh(t/2).

This script checks the inequalities and numerical quadrature for several
noninteger chambers. It is an audit, not a substitute for the analytic proof.
"""

import mpmath as mp

mp.mp.dps = 60


def nu(c, x):
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf("0")
    return c / (abs(x) * mp.sinh(mp.pi * abs(x)))


def K(c, t, x):
    x = mp.mpf(x)
    if x == 0:
        # Totalized point value used in Lean; the punctured limit is finite.
        return mp.mpf("0")
    return (1 - mp.cos(t * x)) * nu(c, x)


def check_pointwise(c, t, xs):
    uniform = t * t * c / (2 * mp.pi)
    for x in xs:
        x = mp.mpf(x)
        if x == 0:
            assert K(c, t, x) <= uniform
            continue
        inv_nu = c / (mp.pi * abs(x) ** 2)
        inv_K = 2 * c / (mp.pi * abs(x) ** 2)
        assert nu(c, x) <= inv_nu * (1 + mp.mpf("1e-50"))
        assert K(c, t, x) <= inv_K * (1 + mp.mpf("1e-50"))
        assert K(c, t, x) <= uniform * (1 + mp.mpf("1e-50"))


def quad_K(c, t):
    f = lambda x: (1 - mp.cos(t * x)) * c / (x * mp.sinh(mp.pi * x))
    # Even integrand; the x=0 singularity is removable after compensation.
    return 2 * mp.quad(f, [0, mp.mpf("0.1"), 1, mp.inf])


def run_case(c, t):
    c = mp.mpf(c)
    t = mp.mpf(t)
    xs = ["1e-12", "1e-8", "1e-4", "0.05", "0.3", "1", "2", "5", "20"]
    check_pointwise(c, t, xs)
    integral = quad_K(c, t)
    target = 2 * c * mp.log(mp.cosh(t / 2))
    piecewise_mass = c * (t * t + 4) / mp.pi
    err = abs(integral - target)
    assert err < mp.mpf("1e-40")
    assert integral <= piecewise_mass
    print(f"c={mp.nstr(c,12)} t={mp.nstr(t,12)}")
    print("  integral       =", mp.nstr(integral, 45))
    print("  exact target   =", mp.nstr(target, 45))
    print("  abs error      =", mp.nstr(err, 8))
    print("  majorant mass  =", mp.nstr(piecewise_mass, 30))


if __name__ == "__main__":
    for c, t in [("0.25", "0.4"), ("0.7", "1.3"), ("1.2", "3.1"), ("2.75", "7.0")]:
        run_case(c, t)
