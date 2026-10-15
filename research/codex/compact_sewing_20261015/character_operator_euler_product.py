#!/usr/bin/env python3
"""Exact finite-character K-sector Euler product & Möbius inverse.

Primitive Dirichlet characters of conductor 1,3,4,5,7. Ramified Euler factors
are identity because local Haar partial isometry V_p vanishes. The full
infinite Euler-product convergence theorem holds only for Re s > 1.
No RH or Dirichlet GRH conclusion.

Golden Physics Project / Daniel Toupin, Codex 2026-10-15.
"""
import sympy as s
from math import gcd

conductors=(1,3,4,5,7)

def chi(f,n):
    if f==1: return s.Integer(1)
    if gcd(f,n)!=1: return s.Integer(0)
    if f==4: return s.Integer(1 if n%4==1 else -1)
    return s.Integer(s.legendre_symbol(n,f))

def V(p):
    return s.diag(*[chi(f,p) for f in conductors])

def E(p):
    return s.diag(*[int(f%p != 0) for f in conductors])

def main():
    primes=(2,3,5,7)
    z=s.symbols("z_2 z_3 z_5 z_7")
    I=s.eye(len(conductors))
    inverse=I.copy()
    direct=I.copy()
    for p,zp in zip(primes,z):
        vp=V(p)
        assert vp.H*vp==E(p)==vp*vp.H
        assert vp*vp.H==vp.H*vp
        factor=I-zp*vp
        inverse=inverse*factor
        direct=direct*factor.inv()
    assert all(s.simplify(v)==0 for v in direct*inverse-I)
    assert all(s.simplify(v)==0 for v in inverse*direct-I)
    print("Finite operator Euler product, exact symbolic inverse: PASS")
    for i,f in enumerate(conductors):
        lam=s.prod((1-zp*chi(f,p))**(-1) for p,zp in zip(primes,z))
        assert s.simplify(direct[i,i]-lam)==0
        print("conductor",f, "formal Euler eigenvalue:",lam)
    for m in range(1,120):
        nmat=I
        for p,k in s.factorint(m).items():
            nmat=nmat*(V(p)**k)
        assert nmat==s.diag(*[chi(f,m) for f in conductors])
    print("Euler multiplicativity, conductor-zero selection: PASS")
    print("This is a finite symbolic test; all-prime Re(s)>1 proof is analytical.")

if __name__=="__main__":
    main()
