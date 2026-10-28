#!/usr/bin/env python3
"""Cutoff audit of the sharp prime-source Schur contact price.

No claim of cancellation against gamma/poles or of RH.
Uses only Python standard library, with deterministic sieve.
"""
import math

def primes_up_to(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p]=b'\x00'*(((limit-p*p)//p)+1)
    return [n for n in range(limit+1) if sieve[n]]

def pnt_continuum(X):
    return 2*math.sqrt(X)*(math.log(X)-2)-2*math.sqrt(2)*(math.log(2)-2)

def audit(limit):
    ps=primes_up_to(limit)
    k1=math.fsum(math.log(p)**2/math.sqrt(p) for p in ps)
    k2=math.fsum(math.log(p)**2/p for p in ps)
    rest=math.fsum(math.log(p)**2*(p**(-1.5))/(1-p**(-0.5)) for p in ps)
    total=math.fsum(math.log(p)**2*(p**(-0.5))/(1-p**(-0.5)) for p in ps)
    assert abs((k1+k2+rest)-total)<1e-10*max(1,total)
    return (len(ps),k1,k2,rest,total,pnt_continuum(limit))

for X in (100,1000,10000,100000,1000000):
    count,k1,k2,rest,total,mean=audit(X)
    print(f'P={X:>7d} primes={count:>6d}: k1={k1:>12.3f}, '
          f'PNT_k1={mean:>12.3f}, k2={k2:>9.3f}, '
          f'half_log2={.5*math.log(X)**2:>9.3f}, '
          f'k>=3={rest:>9.5f}, total={total:>12.3f}')
