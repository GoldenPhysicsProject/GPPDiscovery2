#!/usr/bin/env python3
"""Exact rational twistor/Loewner Hankel falsifier; no RH claim.

F_c(z)=cosh(2z)+c*cosh(z), f_c(u)=F_c(sqrt(u)), m_c=f_c'/f_c.
h_n=(-1)^n[u^n]m_c.  Positive Loewner/Pick kernel near zero
requires PSD of [h_(i+j+1)] for all finite index sets.

No packages required: uses Fraction arithmetic, not floating point.
"""
from fractions import Fraction as Q
from math import factorial


def coefficients(c=5, nmax=5):
    c = Q(c)
    a = [Q(4**k+c, factorial(2*k)) for k in range(nmax+2)]
    q = []
    for n in range(nmax+1):
        qn = ((n+1)*a[n+1] -
              sum((a[k]*q[n-k] for k in range(1,n+1)), Q(0))) / a[0]
        q.append(qn)
    return [(-1)**n*q[n] for n in range(nmax+1)]


def determinant3(H):
    a,b,c=H[0]; d,e,f=H[1]; g,h,i=H[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def run():
    h=coefficients(5)
    H=[[h[i+j+1] for j in range(3)] for i in range(3)]
    d1=h[1]
    d2=h[1]*h[3]-h[2]**2
    skip=h[1]*h[5]-h[3]**2
    d3=determinant3(H)
    x=(-h[3]/h[1],Q(0),Q(1))
    witness=h[5]-h[3]**2/h[1]

    assert h == [Q(3,4),Q(13,48),Q(17,120),
                 Q(6001,80640),Q(56473,1451520),
                 Q(6490313,319334400)]
    assert d1 == Q(13,48)>0
    assert d2 == Q(1649,19353600)>0
    assert skip == -Q(7159067,214592716800)<0
    assert d3 == -Q(8255485043,778714050723840000)<0
    assert x == (-Q(6001,21840),Q(0),Q(1))
    assert witness == -Q(7159067,58118860800)<0

    print("h_0..h_5:",h)
    print("first curvature h1:",d1)
    print("consecutive 2x2 determinant:",d2)
    print("skipped-order 2x2 determinant:",skip)
    print("full 3x3 determinant:",d3)
    print("exact negative quadratic witness vector:",x)
    print("w^T H w:",witness)
    print("PASS: positive cosh mixture violates confluent Hankel PSD.")
if __name__=="__main__":
    run()
