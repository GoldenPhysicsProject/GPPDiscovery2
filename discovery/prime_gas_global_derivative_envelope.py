"""Exact global envelope for quadratic number-Gibbs differentiation.

For L >= 0, beta >= -B and eta >= eta0 > 0,

    exp(-beta*L - eta*L**2)
      <= exp((B+2)**2/(4*eta0)) * exp(-2*L).

Multiplication by L**r gives a single all-index summable derivative majorant
once the exponent-2 zeta logarithmic moment is known summable.
"""

import sympy as sp

L, B, eta0 = sp.symbols("L B eta0", real=True)
C = (B + 2) ** 2 / (4 * eta0)
remainder = sp.factor(eta0 * L**2 - (B + 2) * L + C)
square = sp.factor(eta0 * (L - (B + 2) / (2 * eta0)) ** 2)

assert sp.simplify(remainder - square) == 0

print("C =", C)
print("eta0*L^2 - (B+2)*L + C =", square)
print("Hence (B+2)L - eta0*L^2 <= C for eta0>0.")
print("For beta>=-B, eta>=eta0, L>=0:")
print("  -beta L - eta L^2 <= -2 L + C")
print("  w_{beta,eta}(n) L^r <= exp(C) * exp(-2L_n) * L_n^r")
