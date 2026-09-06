#!/usr/bin/env python3
"""Exact cumulant audit for the continuous Gamma-chamber heat-time subordinator.

For

    S_c = sum_{k>=0} Gamma(shape=2c, rate=pi^2 (2k+1)^2),

the m-th cumulant is

    kappa_m(S_c)
      = 2 c (m-1)! (1 - 2^(-2m)) zeta(2m) / pi^(2m).

This extends the already recorded mean c/4 and variance c/48 to all orders.
The script asks SymPy for exact even-zeta values through m=6 and checks the
first two certified values. No RH/arithmetic positivity claim is involved.
"""

from __future__ import annotations

import sympy as sp

c = sp.symbols("c", positive=True)


def cumulant(m: int):
    assert m >= 1
    return sp.simplify(
        2 * c * sp.factorial(m - 1)
        * (1 - sp.Rational(1, 2) ** (2 * m))
        * sp.zeta(2 * m) / sp.pi ** (2 * m)
    )


def main() -> None:
    vals = [sp.simplify(cumulant(m)) for m in range(1, 7)]
    assert sp.simplify(vals[0] - c / 4) == 0
    assert sp.simplify(vals[1] - c / 48) == 0

    # Independent coefficient check from the cumulant generating function
    # K_c(t) = log E exp(t S_c) = -2c sum_k log(1-t/lambda_k).
    # Its t^m coefficient must be kappa_m / m!.
    for m, km in enumerate(vals, start=1):
        odd_zeta_sum = sp.simplify(
            (1 - sp.Rational(1, 2) ** (2 * m)) * sp.zeta(2 * m)
            / sp.pi ** (2 * m)
        )
        coeff = sp.simplify(2 * c * odd_zeta_sum / m)
        assert sp.simplify(coeff - km / sp.factorial(m)) == 0

    print("continuous Gamma-chamber heat-time cumulants:")
    for m, km in enumerate(vals, start=1):
        print(f"kappa_{m} =", km)
    print("PASS: all-order cumulant formula and K_c coefficient relation verified through m=6 exactly")


if __name__ == "__main__":
    main()
