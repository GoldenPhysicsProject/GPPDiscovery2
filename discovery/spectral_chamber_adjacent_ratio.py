#!/usr/bin/env python3
"""Numerical audit of the exact adjacent spectral-chamber ratio.

For
    rho_k(x) = 2^(2k+1)/(2k+1)! * x/sinh(pi x) * prod_{j=1}^k (j^2+x^2),
verify
    rho_{k+1}(x)/rho_k(x)
      = 2*((k+1)^2+x^2)/((k+1)*(2k+3)).

The equality is algebraic; this script is a floating-point regression check only.
"""

from math import factorial, pi, sinh


def rho(k: int, x: float) -> float:
    base = 1.0 / pi if x == 0.0 else x / sinh(pi * x)
    prod = 1.0
    for j in range(1, k + 1):
        prod *= j * j + x * x
    return (2.0 ** (2 * k + 1) / factorial(2 * k + 1)) * base * prod


def ratio_formula(k: int, x: float) -> float:
    kp1 = k + 1.0
    return 2.0 * (kp1 * kp1 + x * x) / (kp1 * (2.0 * k + 3.0))


if __name__ == "__main__":
    max_err = 0.0
    for k in range(8):
        threshold_sq = (k + 1.0) / 2.0
        for x in (0.0, 0.4, 1.0, 2.5, 5.0):
            lhs = rho(k + 1, x) / rho(k, x)
            rhs = ratio_formula(k, x)
            err = abs(lhs - rhs)
            max_err = max(max_err, err)
            relation = "above" if x * x > threshold_sq else "below" if x * x < threshold_sq else "at"
            print(f"k={k:2d} x={x:4.1f} ratio={lhs:.15g} formula={rhs:.15g} {relation}-crossing")
    print(f"max_abs_error={max_err:.3e}")
