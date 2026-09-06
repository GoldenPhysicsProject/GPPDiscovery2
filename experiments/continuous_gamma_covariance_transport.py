#!/usr/bin/env python3
"""Exact audit of the continuous Gamma-chamber covariance transport identity.

Given the normalized chamber recurrence
    rho_{c+1}(x) = F_c(x) rho_c(x),
    F_c(x) = 2(c^2+x^2)/(c(2c+1)),
and M_2(c)=E_c[X^2]=c/2, verify algebraically that for any observable f,

    E_{c+1}[f] - E_c[f]
      = 2/(c(2c+1)) Cov_c(f(X), X^2).

For f=X^(2m) this gives the exact moment transport law already observed.
"""

import sympy as sp

c, Ef, Ex2f = sp.symbols("c Ef Ex2f", nonzero=True)

Ec1f = 2 * (c**2 * Ef + Ex2f) / (c * (2*c + 1))
cov = Ex2f - (c/2) * Ef
rhs = 2 * cov / (c * (2*c + 1))

assert sp.simplify(Ec1f - Ef - rhs) == 0

# Moment specialization: Ef=M_{2m}(c), Ex2f=M_{2m+2}(c).
M, Mnext = sp.symbols("M Mnext")
moment_shift = sp.simplify(
    2 * (c**2 * M + Mnext) / (c * (2*c + 1)) - M
)
moment_cov = sp.simplify(
    2 * (Mnext - c*M/2) / (c * (2*c + 1))
)
assert sp.simplify(moment_shift - moment_cov) == 0

print("continuous Gamma covariance transport: exact")
print("E_{c+1}[f]-E_c[f] =", sp.factor(rhs))
print("moment increment =", sp.factor(moment_shift))
