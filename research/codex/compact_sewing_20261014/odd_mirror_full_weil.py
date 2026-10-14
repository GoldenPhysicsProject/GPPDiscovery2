#!/usr/bin/env python3
"""Full finite-support Weil prime+real-place test on a sharp odd window.
Exact formulas, high-precision numerical quadrature. Sharp cutoff means
the test is not C_c^infinity; no RH or globally certified sign is claimed."""
import math
import mpmath as mp
mp.mp.dps=45

def G(a,b,h):
    d=a-b
    return mp.sinh((a+b)*h)/(a+b)-(h if d==0 else mp.sinh(d*h)/d)

def F(t,h):
    t=abs(t)
    if t>2*h: return mp.mpf(0)
    N=mp.sinh(h)-h
    return (mp.sinh(h-t/2)-(h-t/2)*mp.cosh(t/2))/N

def arch(h,theta=mp.mpf(0)):
    N=mp.sinh(h)-h
    limit=(1-mp.cosh(h))/(2*N)+mp.mpf('0.5')
    def fun(t):
        if abs(t)<mp.mpf('1e-24'):return limit
        return 2*(mp.exp(-t/2)*mp.cosh(theta*t)*F(t,h)-mp.exp(-t))/(-mp.expm1(-2*t))
    return mp.log(4*mp.pi)+mp.euler+mp.log(mp.tanh(h))+mp.quad(fun,[0,h,2*h])

def von_mangoldt_prime_powers(h,theta=mp.mpf(0)):
    limit=int(mp.floor(mp.exp(2*h)))
    composite=bytearray(limit+1)
    total=mp.mpf(0)
    for p in range(2,limit+1):
        if composite[p]: continue
        for j in range(2*p,limit+1,p): composite[j]=1
        pk=p
        while pk<=limit:
            t=mp.log(pk)
            total+=2*mp.log(p)/mp.sqrt(pk)*mp.cosh(theta*t)*F(t,h)
            pk*=p
    return total

def row(h,theta=mp.mpf('0.25')):
    half=mp.mpf('0.5'); N=mp.sinh(h)-h
    zr=-2*N
    zw=arch(h)
    zp=von_mangoldt_prime_powers(h)
    zq=zr-zw-zp
    pr=-2*(G(half,half+theta,h)**2+G(half,half-theta,h)**2)/N
    aw=2*arch(h,theta)
    pp=2*von_mangoldt_prime_powers(h,theta)
    print("h=",mp.nstr(h,8))
    print(" zeta P,arch,prime,Q =",*[mp.nstr(x,14) for x in [zr,zw,zp,zq]])
    print(" fake P,arch,prime,Q =",*[mp.nstr(x,14) for x in [pr,aw,pp,pr-aw-pp]])

if __name__=="__main__":
    for h in map(mp.mpf,["0.76","2","4"]):row(h)
