#!/usr/bin/env python3
"""High-precision audit of the continuous Gamma-chamber Levy exponent.

Conditional input from the Barnes/Fourier identity:
    rho_c^(t) = sech(t/2)^(2c), c>0.

The corresponding symmetric characteristic exponent is
    Psi_c(t) = -log rho_c^(t) = 2c log cosh(t/2).
This script verifies numerically the Levy-Khintchine representation
    Psi_c(t) = integral_R (1-cos(tx)) c/(|x| sinh(pi|x|)) dx.

It also prints the small-jump asymptotic x^2 nu_c(x) -> c/pi,
which implies infinite Levy activity and infinite variation, while the
quadratic jump moment is finite.  The script is an audit artifact only;
the exact mathematics remains conditional on formalizing the Barnes transform.
"""

import mpmath as mp

mp.mp.dps = 60


def levy_density(c, x):
    x = mp.mpf(x)
    return c / (abs(x) * mp.sinh(mp.pi * abs(x)))


def psi_integral(c, t):
    c, t = mp.mpf(c), mp.mpf(t)
    f = lambda x: (1 - mp.cos(t * x)) * c / (x * mp.sinh(mp.pi * x))
    return 2 * mp.quad(f, [0, 1, mp.inf])


def psi_closed(c, t):
    return 2 * mp.mpf(c) * mp.log(mp.cosh(mp.mpf(t) / 2))


def quadratic_jump_moment(c):
    c = mp.mpf(c)
    f = lambda x: x * c / mp.sinh(mp.pi * x)
    return 2 * mp.quad(f, [0, 1, mp.inf])


if __name__ == "__main__":
    tests = [(mp.mpf("0.5"), mp.mpf("0.2")),
             (mp.mpf("0.5"), mp.mpf("1")),
             (mp.mpf("1"), mp.mpf("1")),
             (mp.mpf("1"), mp.mpf("3")),
             (mp.mpf("2.5"), mp.mpf("3"))]

    print("Levy-Khintchine audit")
    for c, t in tests:
        lhs = psi_integral(c, t)
        rhs = psi_closed(c, t)
        print(f"c={c}, t={t}")
        print("  integral =", mp.nstr(lhs, 40))
        print("  closed   =", mp.nstr(rhs, 40))
        print("  abs err  =", mp.nstr(abs(lhs - rhs), 8))

    print("\nSmall-jump asymptotic x^2 nu_c(x) -> c/pi")
    for c in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2.5")]:
        target = c / mp.pi
        x = mp.mpf("1e-8")
        observed = x * x * levy_density(c, x)
        print(f"c={c}: observed={mp.nstr(observed,30)}, target={mp.nstr(target,30)}")

    print("\nQuadratic jump moment")
    for c in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2.5")]:
        q2 = quadratic_jump_moment(c)
        # Since Psi''(0)=c/2, the symmetric Levy representation requires
        # integral_R x^2 nu_c(dx)=c/2.
        print(f"c={c}: integral x^2 nu(dx)={mp.nstr(q2,30)}, c/2={mp.nstr(c/2,30)}")
