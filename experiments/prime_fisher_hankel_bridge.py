#!/usr/bin/env python3
"""Exact symbolic bridge for the countable prime-Fisher strictness route.

For raw moments m0,...,m4, the mass-aware covariance numerator is exactly
m0 times the 3x3 Hankel moment determinant.  Consequently, after probability
normalization, the 2x2 Fisher determinant is det(H3)/m0^3.

This is purely algebraic and contains no RH assumption.
"""
import sympy as sp

m0, m1, m2, m3, m4 = sp.symbols("m0 m1 m2 m3 m4", real=True)

fisher_num = (
    (m0*m2 - m1**2)*(m0*m4 - m2**2)
    - (m0*m3 - m1*m2)**2
)

H3 = sp.Matrix([
    [m0, m1, m2],
    [m1, m2, m3],
    [m2, m3, m4],
])

hankel_det = sp.expand(H3.det())
bridge = sp.factor(fisher_num - m0*hankel_det)
normalized_bridge = sp.factor(fisher_num/m0**4 - hankel_det/m0**3)

assert bridge == 0
assert normalized_bridge == 0

print("fisherNumerator = m0 * det(H3):", bridge == 0)
print("normalized Fisher determinant = det(H3) / m0^3:", normalized_bridge == 0)
print("det(H3) =", sp.factor(hankel_det))
