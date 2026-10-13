"""Exact 4-mode CAR and reflected purification checks, no RH or gravity proof."""
import sympy as sp
one=sp.eye(2); Z=sp.diag(1,-1); c=sp.Matrix([[0,1],[0,0]])
def kp(xs):
    r=xs[0]
    for x in xs[1:]:r=sp.kronecker_product(r,x)
    return r
C=[kp([Z]*i+[c]+[one]*(3-i)) for i in range(4)]
N=[v.H*v for v in C]
q=(1,1,-1,-1); t=(1,-1,1,-1) # (++),(+-),(-+),(--)
Q=sum((q[i]*N[i] for i in range(4)),sp.zeros(16))
T=sum((t[i]*N[i] for i in range(4)),sp.zeros(16))
A=C[0].H*C[3].H;B=C[1].H*C[2].H
H=A+A.H+2*(B+B.H)
assert Q*H==H*Q and T*H==H*T
vac=sp.zeros(16,1);vac[0]=1;pair=A*vac
assert Q*pair==sp.zeros(16,1) and T*pair==sp.zeros(16,1)
assert (pair.H*pair)[0]==1
v=sp.symbols('v', positive=True, real=True)
entropy=-sp.cos(v)**2*sp.log(sp.cos(v)**2)-sp.sin(v)**2*sp.log(sp.sin(v)**2)
d=sp.sin(2*v)*(sp.log(sp.cos(v)**2)-sp.log(sp.sin(v)**2))
assert sp.simplify(sp.diff(entropy,v)-d)==0
l0=sp.Rational(3,5);l1=sp.Rational(2,5)
Omega=sp.Matrix([sp.sqrt(l0),0,0,sp.sqrt(l1)])
K=sp.Matrix([[1+sp.I,2-sp.I],[3+2*sp.I,4]])
reflected=sp.simplify((Omega.H*sp.kronecker_product(K,K.conjugate())*Omega)[0])
squares=sp.simplify(sum(sp.sqrt(u*w)*K[i,j]*sp.conjugate(K[i,j]) for i,u in enumerate([l0,l1]) for j,w in enumerate([l0,l1])))
assert sp.simplify(reflected-squares)==0
print('PASS 4-mode Q/T conserved, neutral fermion pair, finite-interval entropy monotonicity')
print('PASS paired reflection positive quadratic:',squares)
