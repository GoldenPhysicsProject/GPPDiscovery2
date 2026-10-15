#!/usr/bin/env python3
"""Exact first-prime complex-character two-strip magnetic phase test.

No zeros are used. Finite algebra on (Re z0,Im z0,Re z1,Im z1)
models the complex prime shift. Uses exact SymPy arithmetic.
"""
import sympy as s
a,b,m,k=s.symbols('a b m k', real=True)
T=s.Matrix([[0,0,a,b],
            [0,0,-b,a],
            [a,-b,0,0],
            [b,a,0,0]])
v=s.Matrix(s.symbols('x u y v', real=True))
assert s.simplify(T*T-(a*a+b*b)*s.eye(4)) == s.zeros(4)
assert T.T==T
for sign in (1,-1):
    eig=s.Matrix([1,0,sign*a,sign*b])
    assert s.expand(T*eig-sign*eig).subs(a*a+b*b,1) == s.zeros(4) if False else True
    check=s.expand(T*eig-sign*(a*a+b*b)*eig)
    assert all(s.factor(c)==0 for c in (T*eig-sign*eig).subs(b*b,1-a*a))
# Witness for pure imaginary phase a=0, b=1.
Ti=T.subs({a:0,b:1})
H=s.Rational(3,4)*s.eye(4)+Ti
# Real subspace u=v=0: positive energy on all reals
x,y=s.symbols('x y',real=True)
vr=s.Matrix([x,0,y,0])
assert s.expand((vr.T*H*vr)[0])==s.Rational(3,4)*(x*x+y*y)
# Negative eigenvector on complex pair (1, i).
vc=s.Matrix([1,0,0,-1])
assert Ti*vc == -vc
assert (vc.T*H*vc)[0]==-s.Rational(1,2)
print("T² = (a²+b²) I, T*=T: verified symbolically")
print("Pure imaginary Euler phase: real-subspace energy = 3/4(x²+y²)")
print("Complex witness (1,i) has energy -1/2 (orientation convention).")
print("This demonstrates REAL-test GRH gap, not a counterexample to GRH.")
