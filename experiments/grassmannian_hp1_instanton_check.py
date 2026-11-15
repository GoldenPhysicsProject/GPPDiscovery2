"""Exact symbolic spot checks for the HP1/BPST unit instanton in Gr(2,C4).
The companion note supplies the topological degree-one clutching proof.
Requires sympy.
"""
import itertools
import sympy as sp
x = sp.symbols('x0:4', real=True)
I = sp.I
Q = sp.Matrix([[x[0]+I*x[1], x[2]+I*x[3]],
               [-x[2]+I*x[3], x[0]-I*x[1]]])
D = 1 + sum(t*t for t in x)
assert sp.simplify(Q.conjugate().T*Q-(D-1)*sp.eye(2)) == sp.zeros(2)
assert sp.simplify(Q.det()-(D-1)) == 0
Qd=Q.conjugate().T
A=[(Qd*Q.diff(t)-t*sp.eye(2))/D for t in x]
B=[Q.diff(t) for t in x]
Bd=[Qd.diff(t) for t in x]
F0={}
for i,j in itertools.combinations(range(4),2):
    F0[i,j]=Bd[i]*B[j]-Bd[j]*B[i]
    Fij=A[j].diff(x[i])-A[i].diff(x[j])+A[i]*A[j]-A[j]*A[i]
    for vec in [(0,0,0,0),(1,2,3,4),(2,-1,0,3)]:
        residue=(Fij-F0[i,j]/D**2).subs(dict(zip(x,vec)))
        assert all(sp.simplify(v)==0 for v in residue)
wedge_coeff=sp.zeros(2)
for (i,j),(k,l) in itertools.product(F0,F0):
    if len({i,j,k,l})==4:
        wedge_coeff+=sp.LeviCivita(i,j,k,l)*F0[i,j]*F0[k,l]
assert sp.simplify(wedge_coeff.trace())==48
r=sp.symbols('r',nonnegative=True)
radial=sp.integrate(r**3/(1+r**2)**4,(r,0,sp.oo))
assert radial==sp.Rational(1,12)
assert 48*(2*sp.pi**2)*radial/(8*sp.pi**2)==1
print('PASS: quaternionic matrix identities, six curvature pairs, unit Chern integral')
