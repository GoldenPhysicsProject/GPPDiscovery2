#!/usr/bin/env python3
"""Exact symbolic audit of the real-c Gamma-chamber recurrence.

For c>0 define

    rho_c(x) = 2^(2c-1)/(pi*Gamma(2c)) * Gamma(c+i x) Gamma(c-i x).

Euler recurrence implies

    rho_{c+1}(x) / rho_c(x)
      = 2 (c^2+x^2) / (c(2c+1)).

This script checks the normalization-factor reduction, the sharp crossing
threshold 2*x^2=c, and exact compatibility with the integer Lean chamber
factor under c=k+1.
"""

import sympy as sp

c, x, k = sp.symbols("c x k", positive=True, real=True)

# Ratio of normalizations times the conjugate-Gamma recurrence factor.
normalization_ratio = (
    2 ** (2 * (c + 1) - 1)
    / sp.gamma(2 * (c + 1))
    * (c**2 + x**2)
    / (2 ** (2 * c - 1) / sp.gamma(2 * c))
)
continuous_factor = 2 * (c**2 + x**2) / (c * (2 * c + 1))

assert sp.simplify(normalization_ratio - continuous_factor) == 0

# F_c(x)-1 has exactly the sign of 2*x^2-c for c>0.
assert sp.simplify(
    continuous_factor - 1 - (2 * x**2 - c) / (c * (2 * c + 1))
) == 0

# Integer restriction: c=k+1 reproduces rhoStepFactor k x in Verify2.
integer_factor = 2 * (((k + 1) ** 2) + x**2) / ((k + 1) * (2 * k + 3))
assert sp.simplify(continuous_factor.subs(c, k + 1) - integer_factor) == 0

print("continuous Gamma-chamber recurrence: PASS")
print("rho_(c+1)/rho_c =", sp.factor(continuous_factor))
print("factor - 1 =", sp.factor(continuous_factor - 1))
print("crossing: factor = 1 iff 2*x^2 = c (for c>0)")
print("integer restriction c=k+1: PASS")
