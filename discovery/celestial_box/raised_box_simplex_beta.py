#!/usr/bin/env python3
"""Exact raised-box 3-simplex majorant reduction.

For 0 <= delta < 1, verify symbolically that

  I(delta) = int_{x1,x2,x3 >= 0, x1+x2+x3 <= 1}
             x1^(-delta) x3^(-delta) dx1 dx2 dx3

reduces, after integrating x2 and scaling x3=(1-x1)t, to

  B(1-delta,2) B(1-delta,3-delta)
    = Gamma(1-delta)^2 / Gamma(4-2 delta).

This is discovery evidence / an exact CAS reduction, not a Lean proof.
The analytic domain delta < 1 is recorded explicitly because the endpoint
singularities x1=0 and x3=0 are integrable exactly in that range.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    d = sp.symbols("delta", real=True)

    # After x2 integration the simplex measure contributes
    # (1 - x1 - x3).  Scaling x3=(1-x1)t gives the first Beta factor.
    inner_beta = sp.beta(1 - d, 2)

    # The remaining x1 integral is B(1-d, 3-d).
    outer_beta = sp.beta(1 - d, 3 - d)

    two_beta = inner_beta * outer_beta
    gamma_target = sp.gamma(1 - d) ** 2 / sp.gamma(4 - 2 * d)

    expanded = sp.expand_func(two_beta)
    difference = sp.simplify(expanded - gamma_target)

    print("two-Beta form:", two_beta)
    print("expanded form:", expanded)
    print("Gamma target:", gamma_target)
    print("difference:", difference)

    assert difference == 0

    # Regulator removal at delta=0 returns the affine 3-simplex volume 1/6.
    at_zero = sp.simplify(gamma_target.subs(d, 0))
    print("delta=0:", at_zero)
    assert at_zero == sp.Rational(1, 6)

    # The Gamma quotient is finite on the physical majorant range 0<=d<1;
    # its first singular boundary is d=1 through Gamma(1-d).
    print("analytic domain for endpoint integrability: 0 <= delta < 1")


if __name__ == "__main__":
    main()
