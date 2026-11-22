"""Exact checks for the conditional transverse-spin mass bound (SymPy >= 1.12).

The proof is the Lagrange identity plus Cauchy--Schwarz. The checks verify
the algebra and saturating/vanishing-mass witnesses symbolically.
"""
import sympy as s

y1, y2, k1, k2 = s.symbols("y1 y2 k1 k2", real=True)
r2 = y1**2 + y2**2
k2_norm = k1**2 + k2**2
J = y1*k2 - y2*k1
dot = y1*k1 + y2*k2
assert s.expand(r2*k2_norm - J**2 - dot**2) == 0

hbar, radius, c = s.symbols("hbar radius c", positive=True)
saturating = {y1: radius, y2: 0, k1: 0, k2: hbar/(2*radius)}
assert s.simplify(J.subs(saturating) - hbar/2) == 0
assert s.simplify(k2_norm.subs(saturating) - (hbar/(2*radius))**2) == 0

massless = {y1: radius, y2: 0, k1: 0, k2: 0}
assert s.simplify(J.subs(massless)) == 0
assert s.simplify(k2_norm.subs(massless)) == 0

r = s.symbols("r", positive=True)
kr = hbar/(2*r)
assert s.limit(kr/c, r, s.oo) == 0

print("PASS: Lagrange identity; sharp gap; massless witness; no-gap limit.")
