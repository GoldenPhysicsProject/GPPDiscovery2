#!/usr/bin/env python3
"""Exact multiplicative scale factor for the scalar-box moving endpoint q.

Starting from

    q = (1-R)/(1+R),
    R^2 = U/(U+4m),
    delta = 4m/U,

one gets exactly

    q = (m/U) Q,
    Q = (2R/(1+R))^2.

For the certified physical interval 8/9 <= R <= 1,

    256/289 <= Q <= 1.

A convenient coarse defect bound is

    1-Q <= (162/289) delta,

which implies, via -log Q <= (1-Q)/Q,

    |log Q| <= (81/128) delta.

This is sufficient to control the only non-uniform factor in
`log(q) * log(1-aq)` because the second logarithm is already O((m/U)^2).
"""

from __future__ import annotations

import sympy as sp

R, U, m, delta = sp.symbols("R U m delta", positive=True)
Q = (2 * R / (1 + R)) ** 2

# Pure factor identity after substituting R^2 = U/(U+4m).
q_exact = 4 * m / ((U + 4 * m) * (1 + R) ** 2)
q_scaled = (m / U) * Q
relation = {R**2: U / (U + 4*m)}
# Clear denominators and use the defining quadratic relation explicitly.
cleared = sp.factor((q_exact - q_scaled) * U * (U + 4*m) * (1 + R)**2 / m)
assert sp.factor(cleared.subs(U, R**2 * (U + 4*m))) == 0

# Exact defect factorization.
defect = sp.factor(1 - Q)
defect_target = sp.factor((1 - R) * (1 + 3*R) / (1 + R)**2)
assert sp.factor(defect - defect_target) == 0

print("Q =", sp.factor(Q))
print("1-Q =", defect)
print("PASS: q=(m/U)Q and the Q defect factorization are exact modulo R^2=U/(U+4m)")
