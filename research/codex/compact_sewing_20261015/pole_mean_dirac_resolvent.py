#!/usr/bin/env python3
"""Exact pole/prime-density resolvent & WWIF Dirac four-lift verification.

Zero-independent identities; shifted F_theta is a mandatory negative control.
No RH claim. Derived Oct 15 2026 (Golden Physics Project, Daniel Toupin).
"""
import sympy as s
import mpmath as mp

def verify_clifford():
    X=s.Matrix([[0,1],[1,0]])
    Z=s.diag(1,-1)
    I2=s.eye(2)
    I4=s.eye(4)
    Q=s.kronecker_product(X,I2)
    T=s.kronecker_product(I2,X)
    chi=s.kronecker_product(Z,Z)
    R=Q*T
    G1=Q
    G2=s.I*chi*Q
    assert G1**2==I4 and G2**2==I4
    assert G1*G2+G2*G1==s.zeros(4)
    assert chi*G1+G1*chi==s.zeros(4)
    assert chi*G2+G2*chi==s.zeros(4)
    assert R*G1==G1*R and R*G2==G2*R
    nu,m=s.symbols("nu m",real=True)
    assert s.expand((nu*G1+m*G2)**2)==(nu**2+m**2)*I4
    print("EXACT 4x4 Dirac square and all orientation commutation tests passed")

def F_odd(h,t):
    if not (0 <= t <= 2*h):
        return mp.mpf("0")
    n=mp.sinh(h)-h
    return (mp.sinh(h-t/2)-(h-t/2)*mp.cosh(t/2))/n

def test_window(h,theta):
    norm=mp.sinh(h)-h
    def M(a):
        return 2*mp.quad(lambda t:mp.sinh(t/2)*mp.sinh(a*t),[0,h])/mp.sqrt(norm)
    aplus=mp.mpf(".5")+theta
    aminus=mp.mpf(".5")-theta
    P=-2*(M(aplus)**2+M(aminus)**2)
    ref=4*mp.quad(lambda t:mp.exp(t/2)*mp.cosh(theta*t)*F_odd(h,t),[0,2*h])
    K=2*mp.quad(lambda t:(mp.exp(-aplus*t)+mp.exp(-aminus*t))*F_odd(h,t),[0,2*h])
    assert abs(P-ref-K)<mp.mpf("1e-39")
    print("shifted", "h=",h,"theta=",theta,"pole-minus-mean=",mp.nstr(P-ref,24))

def test_zeta(h):
    n=mp.sinh(h)-h
    P=-2*n
    ref=2*mp.quad(lambda t:mp.exp(t/2)*F_odd(h,t),[0,2*h])
    K=2*mp.quad(lambda t:mp.exp(-t/2)*F_odd(h,t),[0,2*h])
    assert abs(P-ref-K)<mp.mpf("1e-39")
    print("zeta", "h=",h, "pole-minus-mean=",mp.nstr(P-ref,24))

if __name__=="__main__":
    mp.mp.dps=50
    verify_clifford()
    for h in map(mp.mpf,["0.76","2","4"]):
        test_zeta(h)
        test_window(h,mp.mpf("0.25"))
