#!/usr/bin/env python3
"""Branch-free quadratic root sums with the residue Jacobian 1/q'(y_i).

For q(y)=A y^2+B y+C with simple roots y_+,y_-, define

    W_n = sum_i y_i^n / q'(y_i),
    R_m = sum_i y_i^{-m} / q'(y_i).

These are the combinations that occur after taking residues at topology poles.
The script verifies exact branch-free recurrences and closed low-order formulas.
"""

import sympy as sp

A, B, C = sp.symbols("A B C", nonzero=True)
y = sp.symbols("y")
Delta = B**2 - 4*A*C
sqrtD = sp.sqrt(Delta)
y_plus = (-B + sqrtD)/(2*A)
y_minus = (-B - sqrtD)/(2*A)

qprime = lambda r: 2*A*r + B


def weighted_power_sum(n: int):
    return sp.simplify(
        y_plus**n/qprime(y_plus) + y_minus**n/qprime(y_minus)
    )


def weighted_inverse_sum(m: int):
    return sp.simplify(
        y_plus**(-m)/qprime(y_plus) + y_minus**(-m)/qprime(y_minus)
    )

# Polynomial-power residue moments.
W = [weighted_power_sum(n) for n in range(8)]
assert sp.simplify(W[0]) == 0
assert sp.simplify(W[1] - 1/A) == 0
for n in range(2, 8):
    assert sp.simplify(W[n] + (B/A)*W[n-1] + (C/A)*W[n-2]) == 0

expected_W = {
    2: -B/A**2,
    3: (B**2 - A*C)/A**3,
    4: B*(2*A*C - B**2)/A**4,
    5: (B**4 - 3*A*B**2*C + A**2*C**2)/A**5,
}
for n, rhs in expected_W.items():
    assert sp.simplify(W[n] - rhs) == 0

# Inverse-power residue moments.
R = {m: weighted_inverse_sum(m) for m in range(1, 8)}
assert sp.simplify(R[1] + 1/C) == 0
assert sp.simplify(R[2] - B/C**2) == 0
# With R_0 = 0, the reciprocal-root recurrence is
# R_m = -(B/C) R_{m-1} -(A/C) R_{m-2}.
R0 = sp.Integer(0)
for m in range(2, 8):
    prev2 = R0 if m == 2 else R[m-2]
    assert sp.simplify(R[m] + (B/C)*R[m-1] + (A/C)*prev2) == 0

expected_R = {
    3: (A*C - B**2)/C**3,
    4: B*(B**2 - 2*A*C)/C**4,
}
for m, rhs in expected_R.items():
    assert sp.simplify(R[m] - rhs) == 0

# Any Laurent numerator through |k| <= 3 therefore has a branch-free
# residue sum after division by q'(root).
a = {k: sp.symbols(f"a{k:+d}".replace("+", "p").replace("-", "m")) for k in range(-3, 4)}
weighted_laurent = sp.Integer(0)
for k in range(-3, 4):
    if k >= 0:
        weighted_laurent += a[k] * W[k]
    else:
        weighted_laurent += a[k] * R[-k]
weighted_laurent = sp.factor(sp.simplify(weighted_laurent))
assert not weighted_laurent.has(sp.sqrt(Delta))

print("PASS: branch-free Jacobian-weighted quadratic residue moments")
print("W0..W5:", [sp.factor(v) for v in W[:6]])
print("R1..R4:", [sp.factor(R[m]) for m in range(1, 5)])
print("Laurent |k|<=3 residue sum:")
print(weighted_laurent)
