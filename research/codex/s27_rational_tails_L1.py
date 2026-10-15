"""Exact rational S27 h=1 high-degree tail bounds (no floating-point tail cutoff).

Uses analytic j_d and i_d Bessel amplitude inequalities from Zhu/S27.
Does not certify finite matrix entry construction, Binet envelope or Cholesky.
"""
from fractions import Fraction as Q

def odf(d):
    v=1
    for k in range(1,2*d+2,2):
        v*=k
    return v

def spherical_tail(d,x):
    a=Q(2*(2*d+1)*x**(2*d),odf(d)**2)
    r=Q(x**4,(2*d+1)*(2*d+3)**2*(2*d+5))
    assert r<1
    return a/(1-r)

def modified_tail(d):
    # e^(1/4) <= 4/3; x=L/2=1/2, L=1.
    a=Q(8*(2*d+1),3*4**d*odf(d)**2)
    r=Q(1,16*(2*d+1)*(2*d+3)**2*(2*d+5))
    assert r<1
    return a/(1-r)

for parity,d in [('even',524),('odd',525)]:
    sd=spherical_tail(d,300)
    pd=modified_tail(d)
    assert sd < Q(1,10**(117 if d==524 else 118))
    assert pd < Q(1,10**(3028 if d==524 else 3035))
    print(parity, 'PASS exact rational tails', 'D cutoff',d)
print('These bounds exclude float truncation but not other verifier obligations.')
