#!/usr/bin/env python3
"""Exact symbolic Hessian-curvature reduction for the quadratic number gas.

For X with mean mu and centered moments m_k = E[(X-mu)^k], consider the
exponential-family sufficient statistics (X, X^2).  The Fisher/Hessian metric is
Cov(X,X^2), and the third derivatives of log Z are minus the corresponding
third joint cumulants because the natural parameters enter as -beta X-eta X^2.

This audit proves, as a polynomial identity with no numerical approximation,
that the 2D Hessian-curvature numerator C satisfies

    det(C) = det(H) - D^2,

where

    D = det(g) = m2*m4 - m3^2 - m2^3

and H is the centered degree-3 moment Gram matrix.  Consequently, whenever
D>0,

    R = (D^2-det(H))/(2 D^2)

under the curvature sign convention used by the number-gas discovery code.
Since H is a moment Gram matrix, det(H)>=0 gives the rigorous structural target
R<=1/2.  The script does not assert R<=0; numerical discovery already shows the
curvature sign is not universal.
"""
from __future__ import annotations

import sympy as sp

mu, m2, m3, m4, m5, m6 = sp.symbols("mu m2 m3 m4 m5 m6", real=True)
central = {0: sp.Integer(1), 1: sp.Integer(0), 2: m2, 3: m3, 4: m4, 5: m5, 6: m6}


def raw(k: int) -> sp.Expr:
    return sp.expand(sum(sp.binomial(k, j) * mu ** (k-j) * central[j] for j in range(k+1)))


M = {k: raw(k) for k in range(7)}


def cumulant3(a: int, b: int, c: int) -> sp.Expr:
    return sp.expand(
        M[a+b+c]
        - M[a] * M[b+c]
        - M[b] * M[a+c]
        - M[c] * M[a+b]
        + 2 * M[a] * M[b] * M[c]
    )


# Fisher/Hessian metric for sufficient statistics X and X^2.
g11 = sp.expand(M[2] - M[1]**2)
g12 = sp.expand(M[3] - M[1]*M[2])
g22 = sp.expand(M[4] - M[2]**2)
D = sp.factor(g11*g22 - g12**2)
expected_D = m2*m4 - m3**2 - m2**3
assert sp.expand(D - expected_D) == 0

# Third Massieu derivatives.  Each parameter derivative contributes a minus sign.
p111 = -cumulant3(1,1,1)
p112 = -cumulant3(1,1,2)
p122 = -cumulant3(1,2,2)
p222 = -cumulant3(2,2,2)

C = sp.Matrix([
    [g11,  g12,  g22],
    [p111, p112, p122],
    [p112, p122, p222],
])

H = sp.Matrix([
    [1,  0,  m2, m3],
    [0,  m2, m3, m4],
    [m2, m3, m4, m5],
    [m3, m4, m5, m6],
])

# Strong identity: all dependence on the mean mu cancels exactly.
detC = sp.factor(C.det())
detH = sp.factor(H.det())
assert sp.expand(detC - (detH - D**2)) == 0
assert mu not in sp.Poly(sp.expand(detC), mu, m2, m3, m4, m5, m6).free_symbols

print("det(g) =", D)
print("det(C) =", detC)
print("det(H) =", detH)
print("PASS: det(C) = det(H)-det(g)^2 exactly; the mean cancels")
print("COROLLARY TARGET: if det(g)>0 and det(H)>=0 then R=(det(g)^2-det(H))/(2 det(g)^2) <= 1/2")
print("BOUNDARY: curvature is not sign-definite; R<=0 would require the stronger det(H)>=det(g)^2")
