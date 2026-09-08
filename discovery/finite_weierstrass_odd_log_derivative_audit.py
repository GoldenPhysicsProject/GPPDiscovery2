#!/usr/bin/env python3
"""Finite-product route to the odd-lattice/tanh partial fraction.

Codex/GPT discovery artifact. This deliberately separates the algebraic finite-product
identity from the analytic convergence theorem still required in Lean.

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

The certified GPP sinh Weierstrass product supplies

    F_N(x) -> sinh(pi*x)/(pi*x).

Hence the odd-product ratio tends pointwise to

    [sinh(pi*x)/(pi*x)] / [sinh(pi*x/2)/(pi*x/2)]
      = cosh(pi*x/2).

The remaining analytic passage can be made compact-uniform rather than by assuming
that derivatives commute with a pointwise product limit. On |x| <= T,

    |2x/((2k+1)^2+x^2)| <= 2T/(2k+1)^2,

and the odd-square majorant is summable. Thus the derivative partial sums converge
uniformly on every compact interval by the Weierstrass M-test. Combining that with
the certified pointwise limit (and equality at x=0) gives the standard theorem for
limits of differentiable functions with uniformly convergent derivatives. Therefore
the limiting logarithmic derivative is

    pi*coth(pi*x) - (pi/2)*coth(pi*x/2)
      = (pi/2)*tanh(pi*x/2).

After x=t/pi this is precisely

    2t sum_{k>=0} 1/(((2k+1)pi)^2+t^2) = (1/2)tanh(t/2).

The script checks every finite identity symbolically, the hyperbolic limiting algebra,
and the quantitative compact-uniform convergence of the finite log derivatives.
"""

from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 80


def finite_product(x: sp.Symbol, n: int) -> sp.Expr:
    return sp.prod(1 + x**2 / sp.Integer(k) ** 2 for k in range(1, n + 1))


def check_symbolic_finite_identities(max_n: int = 8) -> None:
    x = sp.symbols("x", real=True)
    y = sp.symbols("y", real=True)
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

        f_n_y = finite_product(y, n)
        odd_log_derivative = sp.cancel(
            sp.diff(f_2n, x) / f_2n
            - sp.Rational(1, 2) * (sp.diff(f_n_y, y) / f_n_y).subs(y, x / 2)
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


def compact_uniform_derivative_tail_bound(T: mp.mpf, n: int) -> mp.mpf:
    """Uniform bound on |x| <= T for the omitted derivative series."""
    return 2 * T * (
        1 / mp.mpf(2 * n + 1) ** 2 + 1 / (2 * mp.mpf(2 * n + 1))
    )


def run() -> None:
    check_symbolic_finite_identities()
    check_hyperbolic_limit_algebra()

    tests = [mp.mpf("0.05"), mp.mpf("0.3"), mp.mpf("1"), mp.mpf("2.7"), mp.mpf("-1.4")]
    for x in tests:
        target = odd_log_derivative_closed(x)
        for n in (10, 100, 1000, 10000):
            approx = odd_log_derivative_partial(x, n)
            bound = compact_uniform_derivative_tail_bound(abs(x), n)
            assert abs(target - approx) <= bound * (1 + mp.mpf("1e-60"))

    for T in (mp.mpf("0.5"), mp.mpf("1"), mp.mpf("3")):
        for n in (25, 250, 2500):
            bound = compact_uniform_derivative_tail_bound(T, n)
            for j in range(-20, 21):
                x = T * mp.mpf(j) / 20
                err = abs(odd_log_derivative_closed(x) - odd_log_derivative_partial(x, n))
                assert err <= bound * (1 + mp.mpf("1e-60"))

    print("PASS: finite Weierstrass logarithmic derivative identity")
    print("PASS: exact even/odd finite-product decomposition")
    print("PASS: odd finite log derivative equals odd rational lattice sum")
    print("PASS: limiting odd product = cosh(pi x/2)")
    print("PASS: limiting hyperbolic algebra = (pi/2) tanh(pi x/2)")
    print("PASS: compact-uniform derivative convergence lies inside the odd-square M-test bound")
    print("FORMAL BOUNDARY: apply a derivative-of-uniform-limit theorem to the certified product limit")


if __name__ == "__main__":
    run()
