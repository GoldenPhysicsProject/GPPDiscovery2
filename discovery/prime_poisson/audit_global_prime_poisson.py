#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 60

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if sieve[i]]

def poisson(r, theta):
    return (1-r*r)/(1-2*r*mp.cos(theta)+r*r)

def global_response(a,t):
    s = a + 1j*t
    return 2*mp.re(-mp.diff(mp.zeta, s)/mp.zeta(s))

def prime_poisson_partial(a,t,pmax):
    return mp.fsum([
        mp.log(p)*(poisson(mp.power(p,-a), t*mp.log(p))-1)
        for p in primes_upto(pmax)
    ])

for a,t in [(2.0,10.0),(1.5,2.0),(1.25,5.0)]:
    target = global_response(a,t)
    print(f'\na={a}, t={t}')
    print('target =', mp.nstr(target, 30))
    for pmax in [100,1000,10000,100000]:
        approx = prime_poisson_partial(a,t,pmax)
        err = abs(target-approx)
        print(f'pmax={pmax:6d}  partial={mp.nstr(approx,30)}  err={mp.nstr(err,8)}')
