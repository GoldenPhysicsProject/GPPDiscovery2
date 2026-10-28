#!/usr/bin/env python3
"""Exact rational sharp positive local two-boundary prime block.
Checks a finite Gram, NOT complete signed Weil positivity.
"""
from fractions import Fraction

def cov(x,k,l):
    return x**max(k,l)-x**(k+l)

def quadratic(x,n,a,t,L):
    mean=sum(a[k-1]*x**k for k in range(1,n+1))
    return (L*L*x/(1-x))*t*t-2*t*L*mean+sum(
        a[k-1]*a[l-1]*cov(x,k,l) for k in range(1,n+1) for l in range(1,n+1))

count=0
for x in [Fraction(1,7),Fraction(1,2),Fraction(3,4),Fraction(9,10)]:
    for N in [1,2,4,8]:
        for seed in range(7):
            a=[Fraction(((k*7+seed*3)%11)-5,5) for k in range(1,N+1)]
            t=Fraction(seed-3,4)
            L=Fraction(7,3)
            lhs=quadratic(x,N,a,t,L)
            b=a[:]
            b[0]-=t*L/(1-x)
            rhs=sum(b[k-1]*b[l-1]*cov(x,k,l)
                    for k in range(1,N+1) for l in range(1,N+1))
            assert lhs==rhs and lhs>=0,(x,N,seed,lhs,rhs)
            count+=1
        t=Fraction(2)
        a=[t*Fraction(7,3)/(1-x)]+[Fraction(0)]*(N-1)
        assert quadratic(x,N,a,t,Fraction(7,3))==0
print(f'PASS {count} exact positive block tests; 16 sharp null modes')
