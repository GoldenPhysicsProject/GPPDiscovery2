#!/usr/bin/env python3
"""Finite-product route to the odd-lattice/tanh partial fraction.

Codex/GPT discovery artifact. This deliberately separates the algebraic finite-product
identity from the analytic limit/derivative interchange still required in Lean.

Let

    F_N(x) = prod_{n=1}^N (1 + x^2/n^2).

Then exactly

    d/dx log F_N(x) = sum_{n=1}^N 2x/(n^2+x^2).

Splitting F_{2N} into its odd and even factors gives

    F_{2N}(x) / F_N(x/2)
      = prod_{k=0}^{N-1} (1 + x^2/(2k+1)^2),

and differentiating this finite identity gives the odd-lattice sum without any
Mittag-Leffler input:

    d/dx log(F_{2N}(x)/F_N(x/2))
      = sum_{k=0}^{N-1} 2x/((2k+1)^2+x^2).

The certified GPP sinh Weierstrass product supplies F_N(x) -> sinh(pi x)/(pi x).
If one additionally justifies passage of the logarithmic derivative to the limit
away from x=0, the limiting odd product is

    2 cosh(pi x/2) /?  More directly the log derivative becomes
    pi*coth(pi*x) - (pi/2)*coth(pi*x/2)
      = (pi/2)*tanh(pi*x/2).

After x=t/pi this is precisely

    2t sum_{k>=0} 1/(((2k+1)pi)^2+t^2) = (1/2)tanh(t/2).

The script checks every finite identity symbolically, the hyperbolic limiting algebra,
and the quantitative convergence of the finite log derivatives.
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 80


def finite_product(x: sp.Symbol, n: int) -> sp.Expr:
    return sp.prod(1 + x**2 / sp.Integer(k) ** 2 for k in range(1, n + 1))


def check_symbolic_finite_identities(max_n: int = 8) -> None:
    x = sp.symbols("x", real=True)
    for n in range(1, max_n + 1):
        f_n = finite_product(x, n)
        log_derivative = sp.cancel(sp.diff(f_n, x) / f_n)
        rational_sum = sp.cancel(
            sum(2 * x / (sp.Integer(k) ** 2 + x**2) for k in range(1, n + 1))
        )
        assert sp.cancel(log_derivative - rational_sum) == 0

        f_2n = finite_product(x, 2 * n)
        f_scaled = finite_product(x / 2, n)
        odd_product = sp.prod(
            1 + x**2 / sp.Integer(2 * k + 1) ** 2 for k in range(n)
        )
        assert sp.cancel(f_2n / f_scaled - odd_product) == 0

        odd_log_derivative = sp.cancel(
            sp.diff(f_2n, x) / f_2n
            - sp.Rational(1, 2)
            * (sp.diff(finite_product(sp.Symbol("y"), n), sp.Symbol("y")) /
               finite_product(sp.Symbol("y"), n)).subs(sp.Symbol("y"), x / 2)
        )
        odd_sum = sp.cancel(
            sum(2 * x / (sp.Integer(2 * k + 1) ** 2 + x**2) for k in range(n))
        )
        assert sp.cancel(odd_log_derivative - odd_sum) == 0


def check_hyperbolic_limit_algebra() -> None:
    x = sp.symbols("x", real=True, nonzero=True)
    lhs = sp.pi * sp.coth(sp.pi * x) - sp.pi / 2 * sp.coth(sp.pi * x / 2)
    rhs = sp.pi / 2 * sp.tanh(sp.pi * x / 2)
    residual = sp.factor(sp.together((lhs - rhs).rewrite(sp.exp)))
    assert residual == 0


def odd_log_derivative_partial(x: mp.mpf, n: int) -> mp.mpf:
    return mp.fsum(
        2 * x / ((2 * k + 1) ** 2 + x**2)
        for k in range(n)
    )


def odd_log_derivative_closed(x: mp.mpf) -> mp.mpf:
    return (mp.pi / 2) * mp.tanh(mp.pi * x / 2)


def run() -> None:
    check_symbolic_finite_identities()
    check_hyperbolic_limit_algebra()

    tests = [mp.mpf("0.05"), mp.mpf("0.3"), mp.mpf("1"), mp.mpf("2.7"), mp.mpf("-1.4")]
    for x in tests:
        target = odd_log_derivative_closed(x)
        for n in (10, 100, 1000, 10000):
            approx = odd_log_derivative_partial(x, n)
            # Absolute tail: sum_{k>=N} 2|x|/(2k+1)^2
            # <= 2|x| [1/(2N+1)^2 + 1/(2(2N+1))].
            bound = 2 * abs(x) * (
                1 / mp.mpf(2 * n + 1) ** 2 + 1 / (2 * mp.mpf(2 * n + 1))
            )
            assert abs(target - approx) <= bound * (1 + mp.mpf("1e-60"))

    print("PASS: finite Weierstrass logarithmic derivative identity")
    print("PASS: exact even/odd finite-product decomposition")
    print("PASS: odd finite log derivative equals odd rational lattice sum")
    print("PASS: limiting hyperbolic algebra = (pi/2) tanh(pi x/2)")
    print("PASS: quantitative convergence lies inside explicit odd-tail bound")
    print("FORMAL BOUNDARY: justify logarithmic-derivative passage through the certified Weierstrass limit")


if __name__ == "__main__":
    run()
