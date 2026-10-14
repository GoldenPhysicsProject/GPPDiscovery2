#!/usr/bin/env python3
"""Exact symbolic q,t four-lift Pauli/Clifford checks and mirror form.

Daniel Toupin's WWIF orientation variables, as recorded in GPP-bridge
work/codex/2026-10-14_four_orientation_pauli_clifford_carrier.md.
Algebra only; this is not a prime/Archimedean intertwiner or RH proof.
"""
import sympy as s

X=s.Matrix([[0,1],[1,0]])
Z=s.diag(1,-1)
I2=s.eye(2)
I4=s.eye(4)
Q=s.kronecker_product(X,I2)
T=s.kronecker_product(I2,X)
D=s.kronecker_product(Z,Z)
Iq=s.I*Q
It=s.I*T
R=Q*T

assert Iq**2==-I4
assert It**2==-I4
assert Iq*It==It*Iq
assert D**2==I4
assert D*Iq+Iq*D==s.zeros(4)
assert D*It+It*D==s.zeros(4)
assert R==-Iq*It
assert R*D==D*R
assert R.eigenvals()=={s.Integer(1):2,s.Integer(-1):2}

a,b,c,d=s.symbols('a b c d', real=True)
v=s.Matrix([a,b,c,d])
reflection=s.expand((v.T*R*v)[0])
decomp=((a+d)**2+(b+c)**2-(a-d)**2-(b-c)**2)/2
assert s.expand(reflection-decomp)==0
print("Q,T commute, Iq^2=It^2=-1, D^2=1 and D anticommutes")
print("R=QT, R commutes with D, signature: 2 positive / 2 negative")
print("Reflection form:",reflection)
print("Internal four lifts not equivalent to four geometric Cayley disks; RH OPEN.")
