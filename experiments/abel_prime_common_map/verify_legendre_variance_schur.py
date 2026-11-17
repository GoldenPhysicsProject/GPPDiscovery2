"""Exact rational mock verification of the canonical Legendre Schur algebra.
This 5x5 matrix is NOT the Weil operator; not an RH/ARP certificate.
"""
import sympy as S
A=S.Matrix([[5,1,1,0,0],[1,6,0,1,0],[1,0,8,0,0],
            [0,1,0,9,0],[0,0,0,0,10]])
F=A[:2,:2]
H=(A*A)[:2,:2]
Z=H-F*F
assert Z==S.eye(2)
delta=S.Integer(6)
slow=F-Z/delta
assert slow[0,0]>0 and slow.det()>0
mu=S.Matrix([S.Rational(3,7),-S.Rational(2,5)])
h=S.Matrix([0,0,S.Rational(11,13),-S.Rational(3,8),S.Rational(7,9)])
f=S.Matrix([*mu,*h[2:]])
b=S.Matrix([0,0,*list(A[2:,:2]*mu)])
quadratic=(f.T*A*f)[0]
lower=(mu.T*slow*mu)[0]+delta*((h+b/delta).dot(h+b/delta))
assert quadratic>=lower
print("PASS exact rational H-F² leakage matrix and Schur completion")
print("F",F,"H",H,"Z",Z,"S_safe",slow)
print("excess",quadratic-lower)
print("Toy only, no RH theorem.")
