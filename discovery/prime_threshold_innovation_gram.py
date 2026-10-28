#!/usr/bin/env python3
"""Exact rational checks for the prime-threshold innovation Gram theorem.

The algebraic argument is in prime_threshold_innovation_gram.md. This script
is a finite verification, NOT a proof assistant and NOT a proof of RH.
"""
from fractions import Fraction
from itertools import product

def cov(x, k, ell):
    assert 1 <= k and 1 <= ell
    return x**max(k, ell) - x**(k + ell)

def matmul(A, B):
    assert len(A[0]) == len(B)
    return [[sum(a*b for a,b in zip(row, col)) for col in zip(*B)] for row in A]

def transpose(A):
    return list(map(list, zip(*A)))

def matrices(x, n):
    L = [[x**(k-j) if j <= k else Fraction(0)
          for j in range(1,n+1)] for k in range(1,n+1)]
    d = [(1-x)*x**j for j in range(1,n+1)]
    D = [[d[j] if i==j else Fraction(0) for j in range(n)]
         for i in range(n)]
    C = [[cov(x,k,ell) for ell in range(1,n+1)]
         for k in range(1,n+1)]
    return C,L,D

def determinant(A):
    A=[row[:] for row in A]
    n=len(A)
    det=Fraction(1)
    for j in range(n):
        piv=next((i for i in range(j,n) if A[i][j]!=0),None)
        if piv is None: return Fraction(0)
        if piv!=j:
            A[piv],A[j]=A[j],A[piv]
            det*=-1
        p=A[j][j]
        det*=p
        for i in range(j+1,n):
            r=A[i][j]/p
            for z in range(j+1,n):
                A[i][z]-=r*A[j][z]
            A[i][j]=0
    return det

def precision(x,n):
    assert 0<x<1
    P=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for k in range(1,n+1):
        P[k-1][k-1]=((1+x) if k<n else 1)/((1-x)*x**k)
        if k<n: P[k-1][k]=P[k][k-1]=-1/((1-x)*x**k)
    return P

def run():
    cases=0
    for x,n in product([Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(9,10)],
                       [1,2,3,5,8,13]):
        C,L,D=matrices(x,n)
        assert C==matmul(matmul(L,D),transpose(L)),(x,n,'LDLt')
        assert determinant(C)==(1-x)**n*x**(n*(n+1)//2),(x,n,'det')
        assert matmul(C,precision(x,n)) == [
            [Fraction(int(i==j)) for j in range(n)] for i in range(n)],(x,n,'inverse')
        for k in range(1,n+1):
            for ell in range(1,n+1):
                assert cov(x,k,ell)==(1-x)*sum(x**(k+ell-j)
                    for j in range(1,min(k,ell)+1))
        for seed in range(3):
            a=[Fraction(((j*7+seed*3)%11)-5,3) for j in range(1,n+1)]
            direct=sum(a[k]*a[ell]*C[k][ell] for k in range(n) for ell in range(n))
            squares=(1-x)*sum(x**j*sum(a[k-1]*x**(k-j)
                   for k in range(j,n+1))**2 for j in range(1,n+1))
            assert direct==squares and direct>=0,(x,n,seed,'PSD')
        cases+=1

    # Two independent geometric occupation baths remain positive
    x1,x2,n=Fraction(1,4),Fraction(3,4),8
    A=[[cov(x1,k,ell)+cov(x2,k,ell) for ell in range(1,n+1)]
       for k in range(1,n+1)]
    for seed in range(8):
        a=[Fraction(((k*3+seed*5)%17)-8,7) for k in range(n)]
        assert sum(a[i]*a[j]*A[i][j] for i in range(n) for j in range(n))>=0
    print(f"PASS: {cases} exact-rational LDLt, determinant, inverse, PSD cases; doubled bath control")

if __name__=='__main__':
    run()
