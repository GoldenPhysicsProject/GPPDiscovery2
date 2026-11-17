"""Numerical primitives shared by all-prime Weil source-diagnostic scripts."""
import math
import numpy as np

CINF = -0.57721566490153286060651209008 - math.log(math.pi) - math.pi/2 - 3*math.log(2)

def mangoldt_sieve(n):
    out=np.zeros(n+1,dtype=np.float64)
    prime=np.ones(n+1,dtype=bool)
    prime[:2]=False
    for p in range(2,math.isqrt(n)+1):
        if prime[p]:
            prime[p*p::p]=False
    for p in np.flatnonzero(prime):
        p=int(p); k=p; lp=math.log(p)
        while k<=n:
            out[k]=lp
            k*=p
    return out

def w(t):
    return math.exp(-t/2)/(-math.expm1(-2*t))

def K(d):
    z=math.exp(-d/2)
    return math.log1p(z)-math.log(-math.expm1(-d/2))+2*math.atan(z)

def box_weil(L, lam):
    from scipy.integrate import quad
    nmax=math.floor(math.exp(L))
    n=np.arange(2,nmax+1,dtype=np.float64)
    ell=np.log(n)
    mask=ell<L
    prime=(2/L)*np.sum(lam[2:nmax+1][mask]/np.sqrt(n[mask])*(L-ell[mask]))
    pole=(8/L)*(math.exp(L/2)+math.exp(-L/2)-2)
    arch=2/L*quad(lambda t:t*w(t),0,L,epsabs=1e-12)[0]+K(L)
    return arch+CINF+pole-prime
