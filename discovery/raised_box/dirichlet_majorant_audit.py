#!/usr/bin/env python3
"""Exact/numerical audit for the raised-box simplex DCT majorant.

For the standard 3-simplex x_i >= 0, sum x_i = 1,

  int_{Delta_3} x1^(-delta) x3^(-delta) d sigma
    = Gamma(1-delta)^2 / Gamma(4-2 delta),   0 < delta < 1.

After integrating x3 and x2 analytically, the remaining check is

  1/((1-d)(2-d)) * int_0^1 x^(-d) (1-x)^(2-d) dx.

SciPy's algebraically weighted quadrature handles both endpoint powers directly,
so this remains stable even close to delta=1.
"""

from __future__ import annotations

import argparse
import math
import sympy as sp
from scipy.integrate import quad


def symbolic_formula():
    delta = sp.symbols("delta", real=True)
    alphas = [1 - delta, 1, 1 - delta, 1]
    rhs = sp.prod(sp.gamma(a) for a in alphas) / sp.gamma(sum(alphas))
    target = sp.gamma(1 - delta) ** 2 / sp.gamma(4 - 2 * delta)
    assert sp.simplify(rhs - target) == 0
    return sp.simplify(target)


def numeric_simplex_integral(delta: float) -> float:
    if not (0.0 < delta < 1.0):
        raise ValueError("delta must satisfy 0 < delta < 1")
    prefactor = 1.0 / ((1.0 - delta) * (2.0 - delta))
    beta_integral, error = quad(
        lambda x: 1.0,
        0.0,
        1.0,
        weight="alg",
        wvar=(-delta, 2.0 - delta),
        epsabs=1e-13,
        epsrel=1e-13,
        limit=200,
    )
    if error > 1e-10:
        raise SystemExit(f"weighted quadrature error estimate too large: {error}")
    return prefactor * beta_integral


def closed_form(delta: float) -> float:
    return math.gamma(1.0 - delta) ** 2 / math.gamma(4.0 - 2.0 * delta)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delta", type=float, nargs="*", default=[0.1, 0.25, 0.5, 0.75, 0.9, 0.99]
    )
    args = parser.parse_args()

    formula = symbolic_formula()
    print("symbolic:", formula)
    print("simplex volume delta=0:", 1.0 / 6.0)

    for delta in args.delta:
        exact = closed_form(delta)
        numeric = numeric_simplex_integral(delta)
        rel = abs(numeric - exact) / abs(exact)
        print(
            f"delta={delta:>5g}  numeric={numeric:.16g}  "
            f"closed={exact:.16g}  relerr={rel:.3e}"
        )
        if rel > 1e-11:
            raise SystemExit(f"quadrature mismatch at delta={delta}: relerr={rel}")

    d = sp.symbols("d", real=True)
    lim = sp.limit(sp.gamma(1 - d) ** 2 / sp.gamma(4 - 2 * d), d, 0, dir="+")
    assert sp.simplify(lim - sp.Rational(1, 6)) == 0
    print("delta -> 0 limit: 1/6 [verified]")


if __name__ == "__main__":
    main()
