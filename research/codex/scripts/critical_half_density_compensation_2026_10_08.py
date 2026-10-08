#!/usr/bin/env python3
"""Critical half-density compensation and shifted-control probe.

Pure prime arithmetic.  Does not calculate zeta zeros or prove RH.
Run: python research/codex/scripts/critical_half_density_compensation_2026_10_08.py
"""
from math import log, sqrt, sinh
from sympy import primerange

ell = log(2.0)

def H(z):
    if z == 0:
        return ell
    a = ell * z / 2
    return ell * (sinh(a) / a) ** 2

def local_prime_powers(x):
    for p0 in primerange(2, 2*x+1):
        p = int(p0)
        n = p
        while n <= 2*x:
            if n >= x/2:
                h = max(0.0, 1.0-abs(log(n/x))/ell)
                yield (p, n, log(p), h)
            n *= p

print('x, theta, critical correction, shifted excess, split sum, ratio')
for x in (100, 1000, 10000, 100000):
    powers = list(local_prime_powers(x))
    base = sum(lp*h/n for p, n, lp, h in powers)
    old_shift = sum(lp*h/n**1.5 for p, n, lp, h in powers)
    assert base > 0 and old_shift >= 0
    for theta in (0.0, 0.1, 0.3):
        shifted = sum(lp*h*(n**theta+n**(-theta))/n
                      for p, n, lp, h in powers)
        excess = shifted-2*base
        assert excess >= -1e-11
        variance = sum((p**theta-p**(-theta))**2/p
                       for p in primerange(2, x+1))
        predicted = (H(theta)*x**theta+H(-theta)*x**(-theta))
        ratio = (excess/sqrt(log(x)*variance)) if variance else 0
        if theta > 0:
            lower = base*((x/2)**theta+(x/2)**(-theta)-2)
            upper = base*((2*x)**theta+(2*x)**(-theta)-2)
            assert lower-1e-11 <= excess <= upper+1e-11
        print(x, theta, round(shifted, 8), round(excess, 8),
              round(variance, 8), round(ratio, 8),
              'PNT-prediction', round(predicted, 8))
    print('unshifted critical',base,'target',ell,
          'delta=1 correction',old_shift)
