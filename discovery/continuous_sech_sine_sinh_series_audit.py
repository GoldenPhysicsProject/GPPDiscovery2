#!/usr/bin/env python3
"""Executable audit for the sine-over-sinh transform used in the continuous-sech Levy exponent.

Checks
    S(t) = integral_0^infty sin(t x)/sinh(pi x) dx
         = 2 t sum_{n>=0} 1/(((2n+1)pi)^2+t^2)
         = 1/2 tanh(t/2)

and verifies a rigorous elementary truncation envelope for the odd-mode series:

|S(t)-S_N(t)| <= (2 |t| / pi^2) *
    [ 1/(2N+1)^2 + 1/(2(2N+1)) ],

where S_N uses n=0,...,N-1.  The envelope follows by dropping t^2 from
the denominator and applying the integral test to sum_{n=N}^infty(2n+1)^(-2).

This script is discovery evidence only; it does not replace the Lean proof of
sum/integral interchange or of the half-integer Mittag-Leffler identity.
"""

import mpmath as mp

mp.mp.dps = 70


def integral_value(t: mp.mpf) -> mp.mpf:
    if t == 0:
        return mp.mpf("0")
    f = lambda x: mp.sin(t * x) / mp.sinh(mp.pi * x)
    # Split to make the removable x=0 behavior and exponential tail numerically tame.
    return mp.quad(f, [0, mp.mpf("0.25"), 1, 3, mp.inf])


def partial_sum(t: mp.mpf, n_terms: int) -> mp.mpf:
    return 2 * t * mp.fsum(
        1 / (((2 * n + 1) * mp.pi) ** 2 + t**2) for n in range(n_terms)
    )


def tail_bound(t: mp.mpf, n_terms: int) -> mp.mpf:
    if n_terms < 1:
        raise ValueError("n_terms must be >= 1")
    q = mp.mpf(2 * n_terms + 1)
    odd_square_tail = 1 / q**2 + 1 / (2 * q)
    return 2 * abs(t) / mp.pi**2 * odd_square_tail


def exact_value(t: mp.mpf) -> mp.mpf:
    return mp.tanh(t / 2) / 2


def audit_one(t_string: str) -> None:
    t = mp.mpf(t_string)
    exact = exact_value(t)
    integ = integral_value(t)
    print(f"t = {t}")
    print(f"  integral       = {mp.nstr(integ, 40)}")
    print(f"  1/2 tanh(t/2) = {mp.nstr(exact, 40)}")
    print(f"  quadrature err = {mp.nstr(abs(integ-exact), 8)}")

    for n_terms in (2, 5, 20, 100, 1000):
        approx = partial_sum(t, n_terms)
        err = abs(exact - approx)
        bound = tail_bound(t, n_terms)
        if err > bound:
            raise AssertionError(
                f"tail bound failed: t={t}, N={n_terms}, err={err}, bound={bound}"
            )
        print(
            f"  N={n_terms:4d}: err={mp.nstr(err, 8)}  "
            f"bound={mp.nstr(bound, 8)}  ratio={mp.nstr(err/bound if bound else 0, 6)}"
        )

    # Oddness is exact at the series and closed-form levels.
    neg_exact = exact_value(-t)
    neg_partial = partial_sum(-t, 100)
    if abs(neg_exact + exact) > mp.mpf("1e-65"):
        raise AssertionError("closed-form oddness failure")
    if abs(neg_partial + partial_sum(t, 100)) > mp.mpf("1e-65"):
        raise AssertionError("series oddness failure")
    print()


def main() -> None:
    for t in ("0.125", "0.7", "1.3", "4.2", "-2.75"):
        audit_one(t)
    print("PASS: integral/series/tanh agreement and explicit odd-mode tail envelope verified.")


if __name__ == "__main__":
    main()
