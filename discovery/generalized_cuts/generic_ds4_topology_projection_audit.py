#!/usr/bin/env python3
"""Exact obstruction and propagator-pole decomposition for the raw generic Ds=4 sewing.

The generic massive-vector-minus-scalar sewings retain a continuous cut angle c=cos(theta).
A convention factor (coupling, color, i-sign, normalization) is independent of that angle.
Therefore a nonconstant raw sewing cannot be identified directly with an already-extracted
box/bubble coefficient by multiplying by one convention constant: topology projection or
subtraction must occur first.

For the mixed-helicity channel we additionally change variables to the physical propagator
coordinate x = 1 - beta*c.  The resulting exact Laurent decomposition separates double-pole,
simple-pole, and polynomial pieces.  This is algebraic topology-reduction data only: assigning
those pieces to box/triangle/bubble master coefficients still requires the actual integrand-
reduction/generalized-cut map and its normalization conventions.
"""
from __future__ import annotations
import sympy as sp

beta, c, x = sp.symbols("beta c x", real=True)
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

# Exact propagator coordinate x = 1 - beta*c.  Write r = rho^2 = 1-beta^2.
r = sp.symbols("r", real=True)
c_of_x = (1 - x) / beta
mixed_x = sp.factor(C4_mixed.subs(c, c_of_x))
mixed_x_r = sp.factor(mixed_x.subs(beta**2, 1-r))

mixed_laurent = (
    2*x**2
    - 8*x
    + 4*r + 24
    - (8*r + 32)/x
    + 2*(r**2 + 8*r + 8)/x**2
)

# SymPy does not always replace all even beta powers under a single structural subs,
# so compare after clearing the relation r = 1-beta^2 explicitly.
mixed_laurent_beta = sp.factor(mixed_laurent.subs(r, 1-beta**2))
assert sp.simplify(sp.together(mixed_x - mixed_laurent_beta)) == 0

same_x = sp.factor(C4_same.subs(c, c_of_x))
same_double_pole = 2*(r**2 - 8*r + 8)/x**2
assert sp.simplify(sp.together(same_x - same_double_pole.subs(r, 1-beta**2))) == 0

print("C4_same =", C4_same)
print("d/dc C4_same =", d_same_dc)
print("C4_mixed =", C4_mixed)
print("d/dc C4_mixed =", d_mixed_dc)
print("same channel in x=1-beta*c:", same_double_pole)
print("mixed channel Laurent decomposition in x=1-beta*c:", mixed_laurent)
print("PASS: raw sewings are angle-dependent and their exact propagator-pole decomposition is certified")
