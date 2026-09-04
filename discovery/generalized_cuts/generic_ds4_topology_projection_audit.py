#!/usr/bin/env python3
"""Exact obstruction to treating the raw generic Ds=4 sewing as a topology coefficient.

The generic massive-vector-minus-scalar sewings retain a continuous cut angle c=cos(theta).
A convention factor (coupling, color, i-sign, normalization) is independent of that angle.
Therefore a nonconstant raw sewing cannot be identified directly with an already-extracted
box/bubble coefficient by multiplying by one convention constant: topology projection or
subtraction must occur first.
"""
from __future__ import annotations
import sympy as sp

beta, c = sp.symbols("beta c", real=True)
rho2 = 1 - beta**2
u = beta**2 * (1 - c**2)
denom = (1 - beta*c)**2

C4_same = sp.factor((2*rho2**2 + 16*beta**2) / denom)
C4_mixed = sp.factor(2*(u**2 - 8*u + 8) / denom)

d_same_dc = sp.factor(sp.diff(C4_same, c))
d_mixed_dc = sp.factor(sp.diff(C4_mixed, c))

# Nonzero polynomial witnesses after clearing denominators.
num_same = sp.factor(sp.together(d_same_dc).as_numer_denom()[0])
num_mixed = sp.factor(sp.together(d_mixed_dc).as_numer_denom()[0])
assert num_same != 0
assert num_mixed != 0

# Concrete exact witnesses exclude accidental symbolic non-simplification.
assert sp.simplify(d_same_dc.subs({beta: sp.Rational(1, 2), c: 0})) != 0
assert sp.simplify(d_mixed_dc.subs({beta: sp.Rational(1, 2), c: 0})) != 0

print("C4_same =", C4_same)
print("d/dc C4_same =", d_same_dc)
print("C4_mixed =", C4_mixed)
print("d/dc C4_mixed =", d_mixed_dc)
print("PASS: raw generic sewings retain cut-angle dependence; topology projection precedes convention matching")
