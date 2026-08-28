#!/usr/bin/env python3
"""Exact/numerical audit for the raised-box simplex DCT majorant.

For the standard 3-simplex
    x_i >= 0, x1+x2+x3+x4 = 1,
the one-channel majorant reduces to (A*x1*x3)^(-delta).
The Dirichlet integral is

    int_{Delta_3} x1^(-delta) x3^(-delta) d sigma
      = Gamma(1-delta)^2 / Gamma(4-2 delta),   0 < delta < 1.

The exact reduction is symbolic.  For the independent numerical check we integrate
x3 and x2 analytically first:

  int_0^(1-x1-x2) x3^(-d) dx3
      = (1-x1-x2)^(1-d)/(1-d),

  int_0^(1-x1) (...) dx2
      = (1-x1)^(2-d)/((1-d)(2-d)),

leaving only the stable one-dimensional Beta integral

  1/((1-d)(2-d)) * int_0^1 x^(-d) (1-x)^(2-d) dx.
"""

from __future__ import annotations

import argparse
import mpmath as mp
import sympy as sp


def symbolic_formula():
    delta = sp.symbols("delta", real=True)
    alphas = [1 - delta, 1, 1 - delta, 1]
    rhs = sp.prod(sp.gamma(a) for a in alphas) / sp.gamma(sum(alphas))
    target = sp.gamma(1 - delta) ** 2 / sp.gamma(4 - 2 * delta)
    assert sp.simplify(rhs - target) == 0
    return sp.simplify(target)


def numeric_simplex_integral(delta: mp.mpf) -> mp.mpf:
    if not (0 < delta < 1):
        raise ValueError("delta must satisfy 0 < delta < 1")

    prefactor = 1 / ((1 - delta) * (2 - delta))
    beta_integral = mp.quad(
        lambda x: x ** (-delta) * (1 - x) ** (2 - delta), [0, 1]
    )
    return prefactor * beta_integral


def closed_form(delta: mp.mpf) -> mp.mpf:
    return mp.gamma(1 - delta) ** 2 / mp.gamma(4 - 2 * delta)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=35)
    parser.add_argument(
        "--delta", type=str, nargs="*", default=["0.1", "0.25", "0.5", "0.75", "0.9"]
    )
    args = parser.parse_args()
    mp.mp.dps = args.dps

    formula = symbolic_formula()
    print("symbolic:", formula)
    print("simplex volume delta=0:", mp.mpf(1) / 6)

    for raw in args.delta:
        delta = mp.mpf(raw)
        exact = closed_form(delta)
        numeric = numeric_simplex_integral(delta)
        err = abs(numeric - exact)
        rel = err / abs(exact)
        print(
            f"delta={raw:>5}  numeric={mp.nstr(numeric, 18)}  "
            f"closed={mp.nstr(exact, 18)}  relerr={mp.nstr(rel, 5)}"
        )
        if rel > mp.mpf("1e-18"):
            raise SystemExit(f"quadrature mismatch at delta={raw}: relerr={rel}")

    d = sp.symbols("d", real=True)
    lim = sp.limit(sp.gamma(1 - d) ** 2 / sp.gamma(4 - 2 * d), d, 0, dir="+")
    assert sp.simplify(lim - sp.Rational(1, 6)) == 0
    print("delta -> 0 limit: 1/6 [verified]")


if __name__ == "__main__":
    main()
