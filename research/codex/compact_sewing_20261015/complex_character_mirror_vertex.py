#!/usr/bin/env python3
"""Complex primitive Dirichlet pair: exact arithmetic charge-conjugation mirror.

Checks C_K V_p C_K=V_p^* and conductor projections on quartic eta_5, bar eta_5.
Linear C_K permutes character labels; it does not conjugate scalar amplitudes.
Golden Physics Project / Daniel Toupin, research derivation Codex 2026-10-15.
No global positivity or RH/GRH theorem.
"""
import sympy as s

# Primitive quartic character modulo 5 with eta(2)=i
q5 = {1:s.Integer(1), 2:s.I, 4:s.Integer(-1), 3:-s.I}
C = s.Matrix([[0,1],[1,0]])
I2 = s.eye(2)
assert C**2 == I2
for p in [2,3,5,7,11,13,17,19]:
    phase = q5.get(p%5, s.Integer(0))
    V = s.diag(phase, s.conjugate(phase))
    E = s.zeros(2) if p == 5 else I2
    assert C*V*C == V.H
    assert V.H*V == E
    assert V*V.H == E
    for k in range(1,6):
        assert C*(V**k)*C == (V.H)**k
    print(f"p={p} eta(p)={phase} CVC=V*=True E_p={list(E.diagonal())}")
print("PASS: exact linear conjugate-character mirror, including p=5 ramification.")
