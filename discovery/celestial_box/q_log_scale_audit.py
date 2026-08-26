#!/usr/bin/env python3
"""Exact symbolic audit for the scalar-box moving endpoint q=rho*Q.

This is discovery-side executable evidence only.  The corresponding Lean target is
|log q| <= |log rho| + (81/32) rho on 0 < rho <= 1/16.
"""

import sympy as sp

R, rho = sp.symbols("R rho", positive=True)

q = (1 - R) / (1 + R)
Q = (2 * R / (1 + R)) ** 2
rho_from_R = (1 - R**2) / (4 * R**2)

factorization = sp.factor(q - rho_from_R * Q)
print("q - rho(R)*Q =", factorization)
assert factorization == 0

# The certified physical chamber gives q <= (324/289) rho and Q >= 256/289.
# Since 0 < Q <= 1, -log Q <= (1-Q)/(256/289), while
# 1-Q = ((1-R)(1+3R))/(1+R)^2 <= 2q on R in [8/9,1].
# Combining those rational constants gives the exact coarse coefficient 81/32.
coefficient = sp.factor(sp.Rational(289, 256) * 2 * sp.Rational(324, 289))
print("log-Q coefficient =", coefficient)
assert coefficient == sp.Rational(81, 32)

one_minus_Q = sp.factor(1 - Q)
expected = sp.factor((1 - R) * (1 + 3 * R) / (1 + R) ** 2)
print("1-Q =", one_minus_Q)
assert sp.factor(one_minus_Q - expected) == 0

ratio_to_q = sp.factor((1 - Q) / q)
print("(1-Q)/q =", ratio_to_q)
# ratio = (1+3R)/(1+R), monotone and <=2 for 0<R<=1.
assert sp.factor(ratio_to_q - (1 + 3 * R) / (1 + R)) == 0

print("PASS: q=rho*Q and the 81/32 logarithmic-scale constant are exact.")
