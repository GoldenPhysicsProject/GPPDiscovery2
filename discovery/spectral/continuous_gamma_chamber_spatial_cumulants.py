#!/usr/bin/env python3
"""Exact audit of all-order spatial cumulants for the continuous Gamma chamber.

For c>0 the normalized chamber density has characteristic function
    phi_c(t) = sech(t/2)^(2c).
Hence
    log phi_c(t) = sum_m (-1)^m kappa_{2m} t^(2m)/(2m)!
with odd cumulants zero.  The exact Bernoulli formula audited here is
    kappa_{2m} = c * (2^(2m)-1) * |B_{2m}| / m.

This is discovery/executable evidence, not a substitute for the Fourier/Gamma
identification theorem in Lean.
"""
from __future__ import annotations

import sympy as sp


t, c = sp.symbols("t c", positive=True)


def predicted_even_cumulant(m: int) -> sp.Expr:
    B = sp.bernoulli(2 * m)
    return sp.simplify(c * (2 ** (2 * m) - 1) * abs(B) / m)


def extracted_even_cumulant(m: int, max_m: int) -> sp.Expr:
    # log(sech(t/2)^(2c)) = -2c log(cosh(t/2)).
    series = sp.series(-2 * c * sp.log(sp.cosh(t / 2)), t, 0, 2 * max_m + 2).removeO()
    coeff = sp.expand(series).coeff(t, 2 * m)
    # log characteristic function coefficient is (-1)^m kappa_{2m}/(2m)!.
    return sp.simplify((-1) ** m * sp.factorial(2 * m) * coeff)


def main() -> None:
    max_m = 8
    rows = []
    for m in range(1, max_m + 1):
        got = extracted_even_cumulant(m, max_m)
        want = predicted_even_cumulant(m)
        delta = sp.simplify(got - want)
        assert delta == 0, (m, got, want, delta)
        rows.append((2 * m, got))

    # First values reproduce and extend the previously audited integer hierarchy.
    expected = {
        2: c / 2,
        4: c / 4,
        6: c / 2,
        8: 17 * c / 8,
        10: 31 * c / 2,
        12: 691 * c / 4,
    }
    for order, want in expected.items():
        m = order // 2
        got = extracted_even_cumulant(m, max_m)
        assert sp.simplify(got - want) == 0, (order, got, want)

    print("continuous Gamma chamber spatial cumulants: exact audit PASS")
    for order, value in rows:
        print(f"kappa_{order} = {sp.sstr(value)}")
    print("odd cumulants = 0 by evenness of log phi_c")
    print("formula: kappa_{2m}=c*(2^(2m)-1)*|B_{2m}|/m")


if __name__ == "__main__":
    main()
