"""Natural x -> p*x prime action in the *golden* cross-ratio coordinate.

This tests a more faithful prime model than translations by log(p) in u.
Every identity is algebraic; quadratures are independent numerical checks.
"""

import numpy as np
from scipy.integrate import quad


PHI = (1 + np.sqrt(5.0)) / 2
QGOLD = PHI ** -2


def coefficients(p):
    a = PHI * (p - 1)
    b = PHI + p / PHI
    c = p * PHI + 1 / PHI
    d = (p - 1) / PHI
    return a, b, c, d


def q_prime(y, p):
    a, b, c, d = coefficients(p)
    return (a + b * y) / (c + d * y)


def derivative_q_prime(y, p):
    _, _, c, d = coefficients(p)
    return 5 * p / (c + d * y) ** 2


def weighted_prime(y, p, profile):
    z = q_prime(y, p)
    jac = abs(y * derivative_q_prime(y, p) / z)
    return np.sqrt(jac) * profile(z)


def profile(y):
    u = np.log(abs(y))
    if y > 0:
        return np.exp(-u * u) * (1 + 0.2 * np.cos(1.3 * u))
    return np.exp(-0.5 * (u - 1) ** 2) * np.exp(0.4j * u)


def norm_sq(p=None):
    def density(u, sheet):
        y = sheet * np.exp(u)
        f = profile(y) if p is None else weighted_prime(y, p, profile)
        return abs(f) ** 2

    total = 0.0
    for sheet in (+1, -1):
        points = []
        if sheet == -1 and p is not None:
            a, b, c, d = coefficients(p)
            points = sorted([np.log(a / b), np.log(c / d)])
        val = quad(density, -35, 35, args=(sheet,), points=points,
                   epsabs=4e-10, epsrel=4e-10, limit=250)[0]
        total += val
    return total


def main():
    print("Natural prime conjugate P_p = C o (x -> p*x) o C^{-1}:")
    baseline = norm_sq()
    print(f"Original two-sheet squared norm: {baseline:.12f}")
    for p in (2, 3, 5, 7):
        a, b, c, d = coefficients(p)
        det = b*c - a*d
        assert abs(det - 5*p) < 1e-12
        for y in (-4.0, -0.3, 0.2, 1.1, 3.0):
            x = (PHI + y/PHI)/(1-y)
            actual = (p*x-PHI)/(p*x+1/PHI)
            assert abs(q_prime(y, p) - actual) < 3e-14

        shifted = norm_sq(p)
        assert abs(shifted - baseline) < 2e-8
        print(f"p={p} determinant={det:.10f}; weighted norm="
              f"{shifted:.12f}; deviation={shifted-baseline:+.2e}")

        # Comparison of the two projective compositions, prior to weights.
        y = 0.2
        prime_after_gold = q_prime(-QGOLD*y, p)
        gold_after_prime = -QGOLD*q_prime(y, p)
        assert abs(prime_after_gold-gold_after_prime) > 1e-3

        # The weighted L2 actions also do not commute on generic states.
        up = weighted_prime(-QGOLD*y, p, profile)
        pu = weighted_prime(y, p, lambda z: profile(-QGOLD*z))
        assert abs(up-pu) > 1e-3
        print(f"    noncommutation at y=.2: projective gap="
              f"{abs(prime_after_gold-gold_after_prime):.6f}; "
              f"unitary operator gap={abs(up-pu):.6f}")

    print("The golden and natural prime x-dilation lifts are both unitary "
          "but do NOT commute. No discrete spectrum or RH follows.")


if __name__ == "__main__":
    main()
