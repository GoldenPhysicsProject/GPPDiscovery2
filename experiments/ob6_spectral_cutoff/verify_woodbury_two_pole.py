"""Exact-rational matrix smoke test of 2-pole Woodbury formula.
No analytic positivity or RH result; tests only the universal matrix algebra.
"""
import sympy as s
G=s.diag(12,13,14,15,16,17)
c=s.Matrix([1,2,0,1,-1,0])/3
h=s.Matrix([0,1,2,-1,1,1])/4
U=s.Matrix.hstack(c,h)
J=s.diag(2,-2)
B=G+U*J*U.T
assert all(x>0 for x in B.eigenvals().keys())
W=J.inv()+U.T*G.inv()*U
Bw=G.inv()-G.inv()*U*W.inv()*U.T*G.inv()
assert (Bw-B.inv())==s.zeros(6)
Y=s.Matrix.hstack(s.ones(6,1),s.Matrix([1,2,3,4,5,6]))
M_direct=Y.T*B.inv()*Y
M_gamm=Y.T*G.inv()*Y
V=U.T*G.inv()*Y
M_wood=M_gamm-V.T*W.inv()*V
assert M_direct==M_wood
print('PASS exact 6x6 inverse, pole-rank-two Woodbury, and 2x2 moment Gram')
print('Pole correction signature',J.diagonal())
print('det J^-1+U^*G^-1U',W.det())
print('moment inverse Gram',M_wood)
