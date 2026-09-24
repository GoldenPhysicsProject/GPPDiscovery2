#!/usr/bin/env python3
"""Verify finite half-density zeta/Mobius gauge identities and Schur bounds.

No zero data are used. This is not an RH proof.
"""

from __future__ import annotations
import argparse
import math
import numpy as np


def mobius(n: int) -> int:
    if n == 1:
        return 1
    m = n
    parity = 0
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            parity ^= 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        parity ^= 1
    return -1 if parity else 1


def von_mangoldt(n: int) -> float:
    if n <= 1:
        return 0.0
    for p in range(2, int(math.sqrt(n)) + 2):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return math.log(n)  # n is prime


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def build(X: int):
    S = list(range(1, X + 1))
    idx = {n:i for i,n in enumerate(S)}
    N = len(S)
    Z = np.zeros((N,N))
    M = np.zeros((N,N))
    D = np.zeros((N,N))
    Lam = np.zeros((N,N))
    for n in S:
        i=idx[n]
        D[i,i]=math.log(n)
        for d in divisors(n):
            j=idx[d]
            w=math.sqrt(d/n)
            Z[i,j]=w
            M[i,j]=mobius(n//d)*w
            Lam[i,j]=von_mangoldt(n//d)*w
    return S,Z,M,D,Lam


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--X",type=int,default=80)
    args=ap.parse_args()
    S,Z,M,D,Lam=build(args.X)
    I=np.eye(len(S))
    err_inv=max(np.max(np.abs(M@Z-I)),np.max(np.abs(Z@M-I)))
    err_gauge=np.max(np.abs(M@D@Z-D-Lam))
    L=math.log(args.X)
    taumax=max(len(divisors(n)) for n in S)
    bound=math.sqrt(taumax*(1+L))
    nz=np.linalg.norm(Z,2)
    nm=np.linalg.norm(M,2)
    nl=np.linalg.norm(Lam,2)
    lbound=L*(1+(1+L)*taumax)

    print("X =",args.X,"L =",L)
    print("inverse error =",err_inv)
    print("gauge error   =",err_gauge)
    print("||Z||         =",nz,"bound =",bound)
    print("||M||         =",nm,"bound =",bound)
    print("||Lambda||    =",nl,"bound =",lbound)
    assert err_inv < 1e-12
    assert err_gauge < 1e-12
    assert nz <= bound*(1+1e-12)
    assert nm <= bound*(1+1e-12)
    assert nl <= lbound*(1+1e-12)
    print("PASS")


if __name__=="__main__":
    main()
