#!/usr/bin/env python3
"""Exact symbolic audit of the scalar-box regulator endpoint/pole geometry.

For S,U,m > 0 define
    R^2 = U/(U+4m),
    kappa^2 = (S(U+4m)-4m^2)/(SU),
    a = (kappa-1)/(kappa+1),
    q = (1-R)/(1+R).

The transformed dispersion integral has a moving pole at x=a and endpoint x=q.
This script derives their small-m series exactly with SymPy and verifies the
coefficients that control the massless logarithms.  It is a discovery audit,
not a proof of the full dilogarithmic remainder estimate.
"""

import sympy as sp

m, S, U = sp.symbols("m S U", positive=True)
R = sp.sqrt(U / (U + 4*m))
kappa = sp.sqrt((S*(U + 4*m) - 4*m**2) / (S*U))
a = sp.simplify((kappa - 1) / (kappa + 1))
q = sp.simplify((1 - R) / (1 + R))
ratio = sp.simplify(q/a - 1)
diff = sp.simplify(q - a)


def coeffs(expr, order=4):
    ser = sp.series(expr, m, 0, order).removeO().expand()
    return [sp.simplify(ser.coeff(m, i)) for i in range(1, order)]

expected_a = [
    1/U,
    -(2*S + U)/(S*U**2),
    (5*S + 4*U)/(S*U**3),
]
expected_q = [1/U, -2/U**2, 5/U**3]
expected_ratio = [
    1/S,
    (U - 2*S)/(S**2*U),
    6/(S*U**2) - 2/(S**2*U) + 1/S**3,
]
expected_diff = [0, 1/(S*U), -4/(S*U**2)]

for name, expr, expected in [
    ("a", a, expected_a),
    ("q", q, expected_q),
    ("q/a - 1", ratio, expected_ratio),
    ("q - a", diff, expected_diff),
]:
    got = coeffs(expr)
    assert all(sp.simplify(g-e) == 0 for g, e in zip(got, expected)), (name, got)
    print(f"{name}: {sp.series(expr, m, 0, 4)}")

print("\nVerified exact coefficients:")
print("a = m/U - (2S+U)m^2/(S U^2) + (5S+4U)m^3/(S U^3) + O(m^4)")
print("q = m/U - 2m^2/U^2 + 5m^3/U^3 + O(m^4)")
print("q-a = m^2/(S U) - 4m^3/(S U^2) + O(m^4)")
print("q/a-1 = m/S + (U-2S)m^2/(S^2 U) + O(m^3)")
