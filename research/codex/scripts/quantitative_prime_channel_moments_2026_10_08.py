#!/usr/bin/env python3
"""Numerical Euler one/two-channel moment witnesses (research-only).

For local centered logarithmic prime-power moments b_m=Σ_j r_j**m,
verify the degree defect b1²-b2=2/p and split defects
2*b2-b1²=(4/p)sinh²(theta log p),
b1*b3-b2²=(4/p²)sinh²(theta log p).

All identities are already algebraic; this experiment checks normalization
and compensated coefficient reconstruction, not RH or Weil positivity.
"""
from mpmath import mp
from sympy import primerange

mp.dps = 90
THETAS = ('0', '0.01', '0.125', '0.3085')
worst = mp.mpf('0')
count = 0

for p0 in primerange(2, 10001):
    p = mp.mpf(p0)
    r = 1/mp.sqrt(p)
    q = 1/p
    for t in THETAS:
        theta = mp.mpf(t)
        a = mp.exp(theta*mp.log(p))
        rp, rm = r*a, r/a
        b1, b2, b3 = rp+rm, rp**2+rm**2, rp**3+rm**3
        c1, c2 = (1-q)*b1, (1-q*q)*b2
        defects = (
            b1*b1-b2-2/p,
            2*b2-b1*b1-4/p*mp.sinh(theta*mp.log(p))**2,
            b1*b3-b2*b2-4/(p*p)*mp.sinh(theta*mp.log(p))**2,
            (c1/(1-q))**2-c2/(1-q*q)-2/p,
        )
        err = max(map(abs, defects))
        worst = max(worst, err)
        assert err < mp.mpf('1e-65'), (p0, t, err)
        count += 1

print('PASS', count, 'prime-shift tuples; worst residual',
      mp.nstr(worst, 16))
