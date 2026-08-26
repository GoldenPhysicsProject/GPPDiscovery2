#!/usr/bin/env python3
"""Exact algebraic skeleton of the regulated scalar-box remainder theorem.

This audit contains no asymptotic approximation.  It isolates the two algebraic
identities needed after the endpoint/pole logarithmic scale estimates and the small
Spence/dilog remainder bounds have been established.

Write

    la = log(a),       lU = log(m/U),
    lt = log(t),       lS = log(m/S),
    da = la-lU,        dt = lt-lS.

The primitive core before the kappa prefactor is

    D  = la*lt + 1/2*la^2 - pi^2/6 + E,

while the desired asymptotic core is

    D0 = lU*lS + 1/2*lU^2 - pi^2/6.

Then exactly

    D-D0
      = da*(lS+lU) + lU*dt + da*dt + 1/2*da^2 + E.

The prefactor error also splits exactly as

    D/kappa - D0
      = (D-D0)/kappa + (1/kappa-1)*D0.

Thus no further analytic mechanism is hidden in the final assembly: every term is
controlled by one of the already-identified scale/remainder/prefactor estimates.
"""

from __future__ import annotations

import sympy as sp

la, lU, lt, lS, E, kappa, pi2 = sp.symbols(
    "la lU lt lS E kappa pi2", nonzero=True
)

da = la - lU
dt = lt - lS

D = la * lt + sp.Rational(1, 2) * la**2 - pi2 / 6 + E
D0 = lU * lS + sp.Rational(1, 2) * lU**2 - pi2 / 6

scale_rhs = (
    da * (lS + lU)
    + lU * dt
    + da * dt
    + sp.Rational(1, 2) * da**2
    + E
)

prefactor_rhs = (D - D0) / kappa + (1 / kappa - 1) * D0

assert sp.expand((D - D0) - scale_rhs) == 0
assert sp.factor(D / kappa - D0 - prefactor_rhs) == 0

print("D-D0 =", sp.expand(scale_rhs))
print("D/kappa-D0 split =", sp.factor(prefactor_rhs))
print("PASS: scalar-box final remainder assembly is exact")
