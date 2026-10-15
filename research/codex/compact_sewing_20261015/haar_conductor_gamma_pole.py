#!/usr/bin/env python3
"""Nested compact Haar conductor, parity and trivial-pole projectors.

Finite primitive Dirichlet quadratic character sample (conductors 1,3,4,5,7).
The local Haar filtration E_{p,m} has character eigenvalue 1[a_p<=m].
Sum_{m>=0}(I-E_{p,m}) has exact conductor exponent a_p.
The global Haar projection is the trivial-character pole projector, and
U_{-1} supplies gamma parity. This test is exact symbolic/integer algebra,
not an implementation of p-adic Haar integration or a proof of RH/GRH.

Golden Physics Project / Daniel Toupin; Codex 2026-10-15.
"""
import sympy as s
from math import gcd

conductors=(1,3,4,5,7)
primes=(2,3,5,7)

def exponent(n,p):
    k=0
    while n%p==0:
        n//=p
        k+=1
    return k

def chi(f,n):
    if f==1:return s.Integer(1)
    if gcd(f,n)!=1:return s.Integer(0)
    if f==4:return s.Integer(1 if n%4==1 else -1)
    return s.Integer(s.legendre_symbol(n,f))

def local_haar(p,m):
    return s.diag(*[s.Integer(int(m>=exponent(f,p))) for f in conductors])

def main():
    I=s.eye(len(conductors))
    C=s.zeros(len(conductors))
    for p in primes:
        for m in range(5):
            E=local_haar(p,m)
            assert E*E==E and E.H==E
            assert all(E[i,i]<=local_haar(p,m+1)[i,i] for i in range(len(conductors)))
        A=sum((I-local_haar(p,m) for m in range(5)),s.zeros(len(conductors)))
        assert A==s.diag(*[exponent(f,p) for f in conductors])
        C+=s.log(p)*A
    assert all(s.expand_log(C[i,i]-s.log(f),force=True).simplify()==0 for i,f in enumerate(conductors))
    Etriv=s.diag(1,0,0,0,0)
    Uminus=s.diag(*[chi(f,-1) for f in conductors])
    Eodd=(I-Uminus)/2
    Eeven=(I+Uminus)/2
    assert Etriv*Etriv==Etriv
    assert Eodd*Eodd==Eodd and Eeven*Eeven==Eeven
    assert Eodd*Eeven==s.zeros(len(conductors))
    assert Eodd+Eeven==I
    for i,f in enumerate(conductors):
        print("conductor",f,"log conductor=",C[i,i],
              "odd gamma parity=",Eodd[i,i],
              "zeta pole projector=",Etriv[i,i])
    print("PASS: Haar conductor telescope, parity and pole projectors, exact.")

if __name__=="__main__":
    main()
