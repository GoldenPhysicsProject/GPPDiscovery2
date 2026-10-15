#!/usr/bin/env python3
"""Finite-character model of the compact-idelic prime partial isometries.

Each primitive Dirichlet character η has eigenvalue η(p) at p, equal 0 when
p|conductor and otherwise a root of unity. The exact compact-K operator is
V_p=(Haar average over Z_p^×)(translation by k_p).
Finite sample includes principal conductor 1, quadratic primitive χ_3,
χ_4, χ_5 and χ_7. Matrix equalities are exact SymPy.

Golden Physics Project / Daniel Toupin; Codex 2026-10-15.
This does not establish RH or any Weil positivity.
"""
import sympy as sp
from math import gcd

def chi_quadratic(conductor, n):
    if gcd(conductor,n) != 1: return sp.Integer(0)
    if conductor == 4:
        return sp.Integer(1) if n % 4 == 1 else sp.Integer(-1)
    return sp.Integer(sp.legendre_symbol(n, conductor))

conductors=(1,3,4,5,7)

def chi(f,n):
    return sp.Integer(1) if f==1 else chi_quadratic(f,n)

def prime_vertex(p):
    return sp.diag(*[chi(f,p) for f in conductors])

def haar_projector(p):
    return sp.diag(*[int(f%p!=0) for f in conductors])

def main():
    I=sp.eye(len(conductors))
    for p in (2,3,5,7,11):
        V=prime_vertex(p)
        E=haar_projector(p)
        assert V.H*V == E
        assert V*V.H == E
        assert V*E == V == E*V
        assert V**2 == sp.diag(*[chi(f,p*p) for f in conductors])
        assert E*E == E and E.H == E
        assert V*V.H != I if p in conductors else V*V.H==I
        print(f"p={p:2} V_p diagonal={list(V.diagonal())}  E_p={list(E.diagonal())}")
    for n in range(1,80):
        fac=sp.factorint(n)
        V=I
        for p,k in fac.items():
            V=V*(prime_vertex(p)**k)
        expect=sp.diag(*[chi(f,n) for f in conductors])
        assert V == expect, n
    print("PASS: exact partial isometry, conductor projection and Euler multiplicativity.")
    print("GRH/RH is not implied by these finite arithmetic identities.")

if __name__=="__main__":
    main()
