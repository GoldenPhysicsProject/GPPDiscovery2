#!/usr/bin/env python3
"""Exact rational finite occupation source and covariance inverse price."""
from fractions import Fraction

def matrix(x, n):
    return [[x**max(i,j)-x**(i+j) for j in range(1,n+1)] for i in range(1,n+1)]

def precision(x,n):
    P = [[Fraction(0) for j in range(n)] for i in range(n)]
    for k in range(1,n+1):
        P[k-1][k-1] = ((1+x) if k<n else 1)/((1-x)*x**k)
        if k<n:
            P[k-1][k] = P[k][k-1] = -1/((1-x)*x**k)
    return P

def dot(a,b):
    return sum(u*v for u,v in zip(a,b))

def mv(P,v):
    return [dot(row,v) for row in P]

for x in [Fraction(1,7), Fraction(1,2), Fraction(3,4), Fraction(9,10)]:
    for n in [1,2,4,8,16]:
        m=[x**k for k in range(1,n+1)]
        p=mv(precision(x,n),m)
        assert p==[1/(1-x)]+[Fraction(0)]*(n-1)
        assert dot(m,p)==x/(1-x)
        assert mv(matrix(x,n),p)==m
    print(f'x={x}: price={x/(1-x)}, independent of cutoff N; PASS')
