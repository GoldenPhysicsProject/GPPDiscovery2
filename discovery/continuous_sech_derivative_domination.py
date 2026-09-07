"""Executable audit for the continuous-sech Levy derivative kernel.

This is discovery evidence, not a substitute for the Lean/analytic proof.

For c >= 0 define
    nu_c(x) = c / (|x| sinh(pi |x|)),
    D_c(t,x) = x sin(t x) nu_c(x),  D_c(t,0) = 0.

The exact analytic bounds checked here are
    |D_c(t,x)| <= c |t| / pi                       (all x),
    |D_c(t,x)| <= 4 c exp(-pi |x|)                (|x| >= 1),
so for |t| <= T a valid L1 majorant has mass
    2 c T / pi + 8 c exp(-pi) / pi.

The final signed-integral comparison
    integral_R D_c(t,x) dx = c tanh(t/2)
is only a high-precision audit here; its analytic/Lean proof still requires the
sine-over-sinh transform and differentiation-under-the-integral machinery.
"""

import mpmath as mp

mp.mp.dps = 70


def levy_density(c, x):
    x = mp.mpf(x)
    if x == 0:
        return mp.inf
    return c / (abs(x) * mp.sinh(mp.pi * abs(x)))


def derivative_kernel(c, t, x):
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf("0")
    return x * mp.sin(t * x) * levy_density(c, x)


def global_bound(c, t):
    return c * abs(t) / mp.pi


def tail_bound(c, x):
    return 4 * c * mp.exp(-mp.pi * abs(x))


def compact_majorant_mass(c, T):
    return 2 * c * T / mp.pi + 8 * c * mp.exp(-mp.pi) / mp.pi


def signed_integral(c, t):
    f = lambda x: derivative_kernel(c, t, x)
    return mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])


def absolute_integral(c, t):
    f = lambda x: abs(derivative_kernel(c, t, x))
    return mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])


def audit_case(c, t):
    c = mp.mpf(c)
    t = mp.mpf(t)
    assert c >= 0

    # Dense deterministic two-sided grid, including the origin and tail split.
    for k in range(-1200, 1201):
        x = mp.mpf(k) / 80
        value = abs(derivative_kernel(c, t, x))
        assert value <= global_bound(c, t) + mp.mpf("1e-60")
        if abs(x) >= 1:
            assert value <= tail_bound(c, x) + mp.mpf("1e-60")

    abs_int = absolute_integral(c, t)
    majorant_mass = compact_majorant_mass(c, abs(t))
    assert abs_int <= majorant_mass + mp.mpf("1e-55")

    integral = signed_integral(c, t)
    target = c * mp.tanh(t / 2)
    error = abs(integral - target)
    assert error < mp.mpf("1e-55")

    return {
        "c": c,
        "t": t,
        "absolute_integral": abs_int,
        "majorant_mass": majorant_mass,
        "signed_integral": integral,
        "target": target,
        "error": error,
    }


def main():
    cases = [
        ("0.25", "-3.7"),
        ("0.7", "0.4"),
        ("1.2", "2.3"),
        ("2.4", "5.1"),
    ]
    for case in cases:
        result = audit_case(*case)
        print("case", mp.nstr(result["c"], 8), mp.nstr(result["t"], 8))
        print("  integral |D|    =", mp.nstr(result["absolute_integral"], 40))
        print("  L1 majorant mass=", mp.nstr(result["majorant_mass"], 40))
        print("  integral D      =", mp.nstr(result["signed_integral"], 40))
        print("  c*tanh(t/2)     =", mp.nstr(result["target"], 40))
        print("  signed error    =", mp.nstr(result["error"], 8))


if __name__ == "__main__":
    main()
