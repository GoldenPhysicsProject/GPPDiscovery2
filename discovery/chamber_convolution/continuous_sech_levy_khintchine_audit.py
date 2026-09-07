#!/usr/bin/env python3
"""High-precision audit of the Levy-Khintchine exponent for continuous sech chambers.

For c>0 define
    Phi_c(t) = sech(t/2)^(2c).

Euler's product for cosh gives
    cosh(t/2) = prod_{n>=1} (1 + t^2/[pi^2 (2n-1)^2]).
Using
    log(1+t^2/a^2) = 2 int_0^infty (1-cos(tx)) e^{-a x} dx/x
and summing the odd exponential progression yields

    log Phi_c(t)
      = -2c int_0^infty (1-cos(tx)) / (x sinh(pi x)) dx.

Equivalently Phi_c is the characteristic exponent associated with the symmetric
Levy measure
    nu_c(dx) = c / (|x| sinh(pi |x|)) dx,  x != 0,
in the convention
    log Phi_c(t) = int_R (cos(tx)-1) nu_c(dx).

This script numerically audits the integral identity and the additive c-semigroup.
It is discovery evidence, not a substitute for the analytic proof or Lean formalization.
"""

import mpmath as mp

mp.mp.dps = 80


def phi(c, t):
    return mp.sech(t / 2) ** (2 * c)


def levy_log_phi(c, t):
    if t == 0:
        return mp.mpf("0")

    def integrand(x):
        if x == 0:
            # (1-cos(tx))/(x*sinh(pi x)) -> t^2/(2*pi)
            return t * t / (2 * mp.pi)
        return (1 - mp.cos(t * x)) / (x * mp.sinh(mp.pi * x))

    # Split near zero and through the exponentially decaying tail.
    val = mp.quad(integrand, [0, mp.mpf("0.05"), mp.mpf("0.5"), 2, 8, mp.inf])
    return -2 * c * val


def relerr(a, b):
    return abs(a - b) / max(mp.mpf("1"), abs(a), abs(b))


def main():
    cases = [
        (mp.mpf("0.125"), mp.mpf("0.3")),
        (mp.mpf("0.4"), mp.mpf("1.25")),
        (mp.mpf("0.875"), mp.mpf("2.75")),
        (mp.mpf("1.2"), mp.mpf("5.0")),
        (mp.mpf("2.35"), mp.mpf("8.5")),
    ]

    tol = mp.mpf("1e-55")
    print("continuous sech Levy-Khintchine audit")
    print("mp.dps =", mp.mp.dps)

    for c, t in cases:
        lhs = mp.log(phi(c, t))
        rhs = levy_log_phi(c, t)
        err = relerr(lhs, rhs)
        print(f"c={c}, t={t}")
        print("  log Phi       =", mp.nstr(lhs, 35))
        print("  Levy integral =", mp.nstr(rhs, 35))
        print("  relative err  =", mp.nstr(err, 8))
        assert err < tol

    semigroup_cases = [
        (mp.mpf("0.25"), mp.mpf("0.4"), mp.mpf("1.7")),
        (mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("4.2")),
        (mp.mpf("1.2"), mp.mpf("2.35"), mp.mpf("6.1")),
    ]
    for c, d, t in semigroup_cases:
        direct = levy_log_phi(c + d, t)
        split = levy_log_phi(c, t) + levy_log_phi(d, t)
        err = relerr(direct, split)
        print(f"semigroup c={c}, d={d}, t={t}, err={mp.nstr(err, 8)}")
        assert err < tol

    # Near-zero variance check. log Phi_c(t) = -c t^2/4 + O(t^4),
    # hence the associated symmetric law has variance c/2.
    for c in [mp.mpf("0.25"), mp.mpf("1"), mp.mpf("2.5")]:
        h = mp.mpf("1e-8")
        variance_est = -2 * mp.log(phi(c, h)) / (h * h)
        target = c / 2
        err = relerr(variance_est, target)
        print(f"variance c={c}: est={mp.nstr(variance_est, 25)}, target={target}, err={mp.nstr(err, 8)}")
        assert err < mp.mpf("1e-16")

    print("PASS")


if __name__ == "__main__":
    main()
