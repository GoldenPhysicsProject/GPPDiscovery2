#!/usr/bin/env python3
"""Exact/high-precision audit for the continuous Gamma-square chamber Levy exponent.

For a>0 define the positive-half-line Levy kernel
    nu_a(y) = a / (y*sinh(pi*y)), y>0.
The symmetric Levy-Khintchine exponent is
    E_a(t) = 2 a integral_0^inf (1-cos(t y))/(y*sinh(pi y)) dy.

The odd-mode decomposition gives lambda_n=(2n+1)pi and the exact mode integral
    2 a integral_0^inf (1-cos(t y)) exp(-lambda_n y)/y dy
      = a log(1+t^2/lambda_n^2).
Hence
    E_a(t) = a sum_{n>=0} log(1+t^2/lambda_n^2)
           = 2a log cosh(t/2).

This file audits:
  * the compensated local limit at y->0;
  * direct quadrature of the full Levy exponent;
  * the exact single-mode Frullani integral;
  * finite odd-mode partial sums;
  * the rigorous tail upper bound
        0 <= tail_N <= a t^2/(4 pi^2) * trigamma(N+1/2),
    from log(1+u)<=u;
  * convergence of the bound on compact frequency windows.

The script is evidence/derivation support only; it is not a formal proof.
"""

import mpmath as mp

mp.mp.dps = 70


def nu(a, y):
    return a / (y * mp.sinh(mp.pi * y))


def compensated(a, t, y):
    if y == 0:
        return a * t * t / (2 * mp.pi)
    return (1 - mp.cos(t * y)) * nu(a, y)


def levy_exponent_integral(a, t):
    f = lambda y: 2 * compensated(a, t, y)
    return mp.quad(f, [0, 1, mp.inf])


def levy_exponent_exact(a, t):
    return 2 * a * mp.log(mp.cosh(t / 2))


def mode_integral(a, t, n):
    lam = (2 * n + 1) * mp.pi
    f = lambda y: 2 * a * (1 - mp.cos(t * y)) * mp.e ** (-lam * y) / y if y else mp.mpf('0')
    return mp.quad(f, [0, 1, mp.inf])


def mode_exact(a, t, n):
    lam = (2 * n + 1) * mp.pi
    return a * mp.log(1 + (t / lam) ** 2)


def partial_exponent(a, t, N):
    return mp.fsum(mode_exact(a, t, n) for n in range(N))


def tail_exact(a, t, N):
    return levy_exponent_exact(a, t) - partial_exponent(a, t, N)


def tail_bound(a, t, N):
    # sum_{n=N}^inf 1/(2n+1)^2 = (1/4) psi_1(N+1/2)
    return a * t * t * mp.polygamma(1, N + mp.mpf('0.5')) / (4 * mp.pi ** 2)


def check_close(label, x, y, tol=mp.mpf('1e-45')):
    err = abs(x - y)
    print(f"{label}: error={mp.nstr(err, 8)}")
    if err > tol:
        raise AssertionError(f"{label} failed: {x} vs {y}")


def main():
    # Local compensated limit: (1-cos(t y))*a/(y sinh(pi y)) -> a t^2/(2 pi).
    for a, t in [(mp.mpf('1'), mp.mpf('1.3')), (mp.mpf('2.3'), mp.mpf('4.1'))]:
        target = a * t * t / (2 * mp.pi)
        y = mp.mpf('1e-20')
        check_close("local compensated limit", compensated(a, t, y), target, mp.mpf('1e-35'))

    # Full exponent and closed form.
    for a, t in [(mp.mpf('1'), mp.mpf('1.3')), (mp.mpf('2.3'), mp.mpf('4.1')), (mp.mpf('0.5'), mp.mpf('0.7'))]:
        check_close("Levy exponent quadrature", levy_exponent_integral(a, t), levy_exponent_exact(a, t), mp.mpf('1e-25'))

    # Single odd-mode Frullani identity.
    for n in [0, 1, 4, 12]:
        check_close(f"mode n={n}", mode_integral(mp.mpf('1.7'), mp.mpf('2.2'), n), mode_exact(mp.mpf('1.7'), mp.mpf('2.2'), n), mp.mpf('1e-45'))

    # Positive tail and explicit trigamma upper bound.
    a = mp.mpf('1.7')
    for t in [mp.mpf('0.4'), mp.mpf('2.0'), mp.mpf('7.0')]:
        for N in [1, 2, 5, 20, 100]:
            tail = tail_exact(a, t, N)
            bound = tail_bound(a, t, N)
            if tail < 0 or tail > bound:
                raise AssertionError((t, N, tail, bound))
            print(f"tail bound t={t}, N={N}: tail={mp.nstr(tail,8)}, bound={mp.nstr(bound,8)}")

    # A compact-window consequence: for |t|<=T the same bound with T controls every tail.
    T = mp.mpf('5')
    N = 50
    compact_bound = tail_bound(mp.mpf('1'), T, N)
    for t in [mp.mpf(k) / 10 for k in range(-50, 51)]:
        if tail_exact(mp.mpf('1'), t, N) > compact_bound:
            raise AssertionError("compact tail bound failed")
    print("compact frequency-window tail bound verified")
    print("PASS")


if __name__ == "__main__":
    main()
