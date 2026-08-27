#!/usr/bin/env python3
"""Exact symbolic audit of the exponential-family cumulant differential law.

For normalized raw moments mu_r(beta) of E=log n under p_beta(n) propto exp(-beta E),

    mu_r' = -mu_{r+1} + mu_1 mu_r.

This script verifies algebraically that the standard third and fourth cumulants obey

    kappa_3' = -kappa_4.

No zeta-specific analytic input is used here; the zeta/prime-gas task is to formalize
the normalized moment derivative identities from the already-proved summability layer.
"""

import sympy as sp

m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")

dm1 = -m2 + m1**2
dm2 = -m3 + m1*m2
dm3 = -m4 + m1*m3

kappa3 = m3 - 3*m2*m1 + 2*m1**3
kappa4 = m4 - 4*m3*m1 - 3*m2**2 + 12*m2*m1**2 - 6*m1**4

dkappa3 = (
    sp.diff(kappa3, m1)*dm1
    + sp.diff(kappa3, m2)*dm2
    + sp.diff(kappa3, m3)*dm3
)

residual = sp.factor(sp.expand(dkappa3 + kappa4))

print("kappa3 =", kappa3)
print("kappa4 =", kappa4)
print("d(kappa3)/d beta =", sp.expand(dkappa3))
print("d(kappa3)/d beta + kappa4 =", residual)

if residual != 0:
    raise SystemExit("FAIL: cumulant differential identity did not close")

print("PASS: kappa3' = -kappa4 exactly")
