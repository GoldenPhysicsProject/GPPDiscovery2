"""Audit the exact odd-mode Gamma-difference -> chamber Levy closure.

For a > 0, the Gamma-square chamber law has characteristic function
    phi_a(t) = sech(t/2)^(2a)
and Euler's odd product gives
    phi_a(t) = prod_{n>=0} (1 + t^2 / lambda_n^2)^(-2a),
    lambda_n = (2n+1) pi.

Each factor is the characteristic function of a difference of two
independent Gamma(shape=2a, rate=lambda_n) variables.  Its symmetric
Levy density is 2a exp(-lambda_n |x|)/|x|.  Summing the odd lattice:

    2 a / |x| * sum_{n>=0} exp(-(2n+1) pi |x|)
      = a / (|x| sinh(pi |x|)).

Hence
    log phi_a(t)
      = integral_R (cos(tx)-1) a/(|x| sinh(pi|x|)) dx
      = -2a log cosh(t/2).

This script verifies the odd-mode sum, the Levy exponent, the product
representation and the variance/cumulant constants independently at
high precision.  It is an audit artifact, not a substitute for proof.
"""

import mpmath as mp

mp.mp.dps = 70


def odd_rate(n):
    return (2 * n + 1) * mp.pi


def mode_levy_sum(x, a, n_terms=2000):
    ax = abs(x)
    return (2 * a / ax) * mp.fsum(
        mp.e ** (-odd_rate(n) * ax) for n in range(n_terms)
    )


def closed_levy_density(x, a):
    ax = abs(x)
    return a / (ax * mp.sinh(mp.pi * ax))


def product_cf(t, a, n_terms=2000):
    return mp.e ** mp.fsum(
        -2 * a * mp.log(1 + (t / odd_rate(n)) ** 2)
        for n in range(n_terms)
    )


def closed_cf(t, a):
    return mp.sech(t / 2) ** (2 * a)


def levy_log_cf(t, a):
    integrand = lambda x: (mp.cos(t * x) - 1) * a / (x * mp.sinh(mp.pi * x))
    return 2 * mp.quad(integrand, [0, 1, mp.inf])


def closed_log_cf(t, a):
    return -2 * a * mp.log(mp.cosh(t / 2))


def mode_variance_sum(a, n_terms=50000):
    # Gamma(shape=2a, rate=lambda) difference has variance 4a/lambda^2.
    return mp.fsum(4 * a / odd_rate(n) ** 2 for n in range(n_terms))


def closed_variance(a):
    return a / 2


def mode_even_cumulant(a, m, n_terms=50000):
    # Difference of two Gamma(2a, lambda) variables:
    # kappa_{2m} = 4 a (2m-1)! / lambda^(2m) per mode.
    return mp.fsum(
        4 * a * mp.factorial(2 * m - 1) / odd_rate(n) ** (2 * m)
        for n in range(n_terms)
    )


def bernoulli_cumulant(a, m):
    return (a / m) * (2 ** (2 * m) - 1) * abs(mp.bernpoly(2 * m, 0))


def relerr(x, y):
    return abs(x - y) / max(mp.mpf(1), abs(y))


def main():
    tol = mp.mpf("1e-45")

    for a in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("1.5"), mp.mpf("2.3")]:
        for x in [mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2.0")]:
            lhs = mode_levy_sum(x, a)
            rhs = closed_levy_density(x, a)
            print("levy-density", a, x, mp.nstr(lhs - rhs, 12))
            assert relerr(lhs, rhs) < tol

        for t in [mp.mpf("0.3"), mp.mpf("1.2"), mp.mpf("2.5")]:
            lhs = product_cf(t, a)
            rhs = closed_cf(t, a)
            print("cf-product", a, t, mp.nstr(lhs - rhs, 12))
            assert relerr(lhs, rhs) < mp.mpf("1e-8")

            lhs_log = levy_log_cf(t, a)
            rhs_log = closed_log_cf(t, a)
            print("levy-exponent", a, t, mp.nstr(lhs_log - rhs_log, 12))
            assert relerr(lhs_log, rhs_log) < mp.mpf("1e-28")

        var_num = mode_variance_sum(a)
        var_exact = closed_variance(a)
        print("variance", a, mp.nstr(var_num - var_exact, 12))
        assert relerr(var_num, var_exact) < mp.mpf("1e-5")

        for m in range(1, 6):
            k_num = mode_even_cumulant(a, m)
            k_exact = bernoulli_cumulant(a, m)
            print("cumulant", a, 2 * m, mp.nstr(k_num - k_exact, 12))
            assert relerr(k_num, k_exact) < mp.mpf("1e-5")

    print("PASS: odd-mode Gamma differences sum exactly to the chamber Levy density")
    print("nu_a(x) = a / (|x| sinh(pi |x|))")
    print("log phi_a(t) = -2 a log cosh(t/2)")
    print("phi_a(t) = sech(t/2)^(2a)")


if __name__ == "__main__":
    main()
