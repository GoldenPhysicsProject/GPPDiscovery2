#!/usr/bin/env python3
"""Executable audit for the continuous-sech sine transform.

Target identity
    ∫_0^∞ sin(t x)/sinh(pi x) dx = (1/2) tanh(t/2).

The audit uses the exact odd-mode expansion
    1/sinh(pi x) = 2 sum_{n>=0} exp(-(2n+1) pi x),  x>0,
and the elementary Laplace-sine integral
    ∫_0^∞ exp(-a x) sin(t x) dx = t/(a^2+t^2).
Hence the transform is reduced to
    I(t) = 2 t sum_{n>=0} 1/(((2n+1)pi)^2+t^2).

A simple explicit tail bound is also checked. For N>=1,
    |I(t)-I_N(t)|
      <= 2|t|/pi^2 * [1/(2N+1)^2 + 1/(2(2N+1))],
from monotonicity of x -> (2x+1)^(-2).

The final closed form is independently checked against direct quadrature and
against the odd-mode partial sums. This is discovery/audit code, not a formal
substitute for the Lean proof of termwise integration and the tanh partial
fraction identity.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 80
PI = mp.pi


def direct_integral(t: mp.mpf) -> mp.mpf:
    t = mp.mpf(t)
    if t == 0:
        return mp.mpf("0")
    f = lambda x: mp.sin(t * x) / mp.sinh(PI * x)
    return mp.quad(f, [0, 1, mp.inf])


def odd_mode_partial_sum(t: mp.mpf, n_terms: int) -> mp.mpf:
    t = mp.mpf(t)
    return 2 * t * mp.fsum(
        1 / (((2 * n + 1) * PI) ** 2 + t**2) for n in range(n_terms)
    )


def odd_mode_tail_bound(t: mp.mpf, n_terms: int) -> mp.mpf:
    if n_terms < 1:
        raise ValueError("n_terms must be >= 1")
    t = abs(mp.mpf(t))
    q = mp.mpf(2 * n_terms + 1)
    return 2 * t / PI**2 * (1 / q**2 + 1 / (2 * q))


def closed_form(t: mp.mpf) -> mp.mpf:
    t = mp.mpf(t)
    return mp.mpf("0.5") * mp.tanh(t / 2)


def check_point(t: mp.mpf, n_terms: int = 2000) -> None:
    t = mp.mpf(t)
    q = direct_integral(t)
    s = odd_mode_partial_sum(t, n_terms)
    c = closed_form(t)
    bound = odd_mode_tail_bound(t, n_terms)
    err_series = abs(c - s)
    err_quad = abs(c - q)
    assert err_series <= bound
    assert err_quad < mp.mpf("1e-60")
    print(
        "t=", mp.nstr(t, 8),
        "quad_err=", mp.nstr(err_quad, 8),
        "series_err=", mp.nstr(err_series, 8),
        "tail_bound=", mp.nstr(bound, 8),
    )


def check_odd_mode_expansion() -> None:
    for x in [mp.mpf("0.03"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("3")]:
        lhs = 1 / mp.sinh(PI * x)
        rhs = 2 * mp.nsum(lambda n: mp.exp(-(2 * n + 1) * PI * x), [0, mp.inf])
        assert abs(lhs - rhs) < mp.mpf("1e-70")


def main() -> None:
    check_odd_mode_expansion()
    for t in ["-10", "-5", "-2", "-0.7", "-0.1", "0", "0.1", "0.7", "2", "5", "10"]:
        check_point(mp.mpf(t))
    print("PASS: sine-over-sinh odd-mode transform audit")


if __name__ == "__main__":
    main()
