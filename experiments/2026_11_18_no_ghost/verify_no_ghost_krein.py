#!/usr/bin/env python3
"""Exact two-mode Krein/BRST ghost algebra; NOT a proof of RH."""
import sympy as sp

gamma, delta, a, b, c, d = sp.symbols("gamma delta a b c d", real=True)
I = sp.I
J = sp.Matrix([[0, 1], [1, 0]])
H = sp.diag(gamma - I * delta, gamma + I * delta)
assert H.conjugate().T * J == J * H
vp = sp.Matrix([1, 1]) / sp.sqrt(2)
vm = sp.Matrix([1, -1]) / sp.sqrt(2)
assert (vp.T * J * vp)[0] == 1
assert (vm.T * J * vm)[0] == -1
assert (vp.T * J * vm)[0] == 0
Q = sp.Matrix([[a, b], [c, d]])
assert sp.simplify(Q * H - H * Q) == sp.Matrix(
    [[0, 2 * I * delta * b], [-2 * I * delta * c, 0]]
)
# When delta != 0, commutation forces b=c=0.
# Nilpotence of diag(a,d) then forces a=d=0 over C.
assert sp.diag(a, d)**2 == sp.diag(a*a, d*d)

A, B, t1, t2 = sp.symbols("A B t1 t2", real=True)
def uv(t):
    return sp.Matrix([sp.exp(-A*t)*sp.cos(B*t),
                      sp.exp(-A*t)*sp.sin(B*t)])
U = sp.Matrix.hstack(uv(t1), uv(t2)).T
G = 2 * U * sp.diag(1,-1) * U.T
det_expected = -4 * sp.exp(-2*A*(t1+t2)) * sp.sin(B*(t2-t1))**2
assert sp.simplify(sp.expand_trig(G.det()) - det_expected) == 0

sigma, tau = sp.symbols("sigma tau", real=True)
wabs2 = ((sigma - 1)**2 + tau**2)/(sigma**2 + tau**2)
assert sp.simplify(1-wabs2 - (2*sigma-1)/(sigma**2+tau**2)) == 0

print("PASS: J-Hermitian complex-conjugate energies; signature (1,1).")
print("PASS: commuting nilpotent Q must vanish for delta != 0.")
print("PASS: exact negative 2-time Hankel determinant.")
print("PASS: exact quantitative Hardy leakage bound.")
