#!/usr/bin/env python3
"""Exact symbolic audit for the continuous Gamma-chamber moment recursion.

For c>0 define the normalized chamber density

    rho_c(x) = 2^(2c-1)/(pi Gamma(2c)) |Gamma(c+i x)|^2,

with characteristic function phi_c(t)=sech(t/2)^(2c).  Gamma recurrence gives

    rho_{c+1}(x) = F_c(x) rho_c(x),
    F_c(x) = 2(c^2+x^2)/(c(2c+1)).

Hence, whenever the required even moments exist,

    M_{2m}(c+1)
      = 2 [c^2 M_{2m}(c) + M_{2m+2}(c)] / [c(2c+1)],

or equivalently

    M_{2m+2}(c)
      = c(2c+1) M_{2m}(c+1)/2 - c^2 M_{2m}(c).

This script derives raw even moments from phi_c and verifies the recurrence
symbolically through M_10.  It is discovery support only; analytic normalization
and the Gamma-density identification remain separate theorem obligations in Lean.
"""

import sympy as sp

c, t = sp.symbols("c t", positive=True, real=True)
phi = sp.sech(t / 2) ** (2 * c)


def even_moment(order: int):
    assert order % 2 == 0
    j = order // 2
    deriv = sp.diff(phi, t, order).subs(t, 0)
    return sp.factor((-1) ** j * deriv)


moments = {order: even_moment(order) for order in range(0, 12, 2)}

expected = {
    0: sp.Integer(1),
    2: c / 2,
    4: c * (3 * c + 1) / 4,
    6: c * (15 * c**2 + 15 * c + 4) / 8,
    8: c * (105 * c**3 + 210 * c**2 + 147 * c + 34) / 16,
    10: c
    * (945 * c**4 + 3150 * c**3 + 4095 * c**2 + 2370 * c + 496)
    / 32,
}

for order, formula in expected.items():
    assert sp.simplify(moments[order] - formula) == 0, (order, moments[order])

for order in range(0, 10, 2):
    lhs = moments[order].subs(c, c + 1)
    rhs = 2 * (c**2 * moments[order] + moments[order + 2]) / (c * (2 * c + 1))
    assert sp.simplify(lhs - rhs) == 0, order

# Normalization plus the c->c+1 density recurrence alone forces the variance.
variance_from_normalization = sp.solve(
    sp.Eq(1, 2 * (c**2 + sp.Symbol("M2")) / (c * (2 * c + 1))),
    sp.Symbol("M2"),
)[0]
assert sp.simplify(variance_from_normalization - c / 2) == 0

print("continuous Gamma-chamber moment recurrence: exact")
for order in sorted(moments):
    print(f"M_{order}(c) = {sp.factor(moments[order])}")
print("normalization + recurrence => M_2(c) = c/2")
