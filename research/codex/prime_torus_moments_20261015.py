"""Exact finite prime-power Haar moment formula diagnostics (floating display only).
Golden Physics Project / Daniel Toupin, Codex October 15 2026.

The identities in the linked private note are *proved by orthogonality*.
This script evaluates finite sums, NOT a proof of RH/GRH or a
Paley-Wiener test-weight estimate.
"""
import math
import sys

def primes_up_to(n):
    s = [True]*(n+1)
    if n >= 0: s[0] = False
    if n >= 1: s[1] = False
    for p in range(2, math.isqrt(n)+1):
        if s[p]:
            for k in range(p*p,n+1,p): s[k]=False
    return (p for p in range(2,n+1) if s[p])

def moments(h,theta=0.,ramified=()):
    X=math.exp(2*h)
    a=[]
    for p in primes_up_to(int(X)):
        if p in ramified: continue
        k=1
        while k*math.log(p) < 2*h:
            value = 2*math.log(p)/p**(k/2)
            value *= math.cosh(theta*k*math.log(p))
            a.append(value)
            k+=1
    mass=sum(a)
    var=sum(q*q for q in a)/2
    return len(a),mass,var

if __name__ == '__main__':
    theta=float(sys.argv[1]) if len(sys.argv)>1 else 0.
    print('theta',theta,'(normalized shifted-product prime weights)')
    for h in (.5,.8,1.2,2.,3.,4.):
        n,A,V=moments(h,theta)
        X=math.exp(2*h)
        bound_factor=(X+1+1/math.log(4))*A*A/2
        print('h=',h,'active n=',n,'comb mass=',A,
              'Haar SD=',math.sqrt(V),'finite-T error bound=',bound_factor,'/T')
