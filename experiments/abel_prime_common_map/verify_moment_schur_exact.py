"""Exact rational toy audit for source-moment Schur matrix algebra.

NOT a Weil-form finite certification: check projections, signs,
high-sector coercivity, and the safe/exact Schur ordering only.
"""
import sympy as S
Q=S.Matrix([[5,1,1,0,0],[1,6,0,1,0],[1,0,8,0,0],
            [0,1,0,9,0],[0,0,0,0,10]])
M=S.Matrix([[1,0,0,1,0],[0,1,0,0,1]])
Phi=S.Matrix([[1,0],[0,1],[0,0],[0,0],[0,0]])
assert M*Phi==S.eye(2)
P=S.eye(5)-M.T*(M*M.T).inv()*M
assert P*P==P and M*P==S.zeros(2,5)
B=P*Q*Phi
F=Phi.T*Q*Phi
Z=B.T*B
G=M*M.T
Z_exp=(Q*Phi).T*(Q*Phi)-(M*Q*Phi).T*G.inv()*(M*Q*Phi)
assert Z==Z_exp

delta=S.Integer(6)
U=S.Matrix.hstack(*M.nullspace())
Hgap=U.T*(Q-delta*S.eye(5))*U
assert all(Hgap[:k,:k].det()>0 for k in range(1,4))
Slow=F-Z/delta
assert Slow[0,0]>0 and Slow.det()>0

D=U.T*Q*U
Hcross=U.T*Q*Phi
Sexact=F-Hcross.T*D.inv()*Hcross
assert all((Sexact-Slow)[:k,:k].det()>0 for k in range(1,3))
mu=S.Matrix([S.Rational(3,7),-S.Rational(2,5)])
z=S.Matrix([S.Rational(11,13),-S.Rational(3,8),S.Rational(7,9)])
h=U*z
f=Phi*mu+h
left=(f.T*Q*f)[0]
completed=(mu.T*Slow*mu)[0]+delta*(h+B*mu/delta).dot(h+B*mu/delta)
assert left>=completed
print("PASS exact rational Schur projection identity")
print("low moment F=",F)
print("cross penalty Z=",Z)
print("conservative finite S_safe=",Slow)
print("exact Schur S_exact=",Sexact)
print("positive test gap=",left-completed)
print("MOCK finite matrix; this does not certify any Weil support window.")
