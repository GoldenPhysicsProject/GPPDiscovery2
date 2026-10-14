#!/usr/bin/env python3
"""Zero-independent completed Weil translation-operator check.

Checks exact Archimedean constant and signed prime/pole form on
normalized sharp odd Mellin window. This test has jumps at +/-h,
so it is not C_c^infinity; smooth approximation is a separate issue.
No RH proof and numerical signs are not interval certified.
"""
import mpmath as mp
mp.mp.dps=45
C0=mp.log(4*mp.pi)+mp.euler
Cstar=mp.log(8*mp.pi)+mp.euler+mp.pi/2

def F(h,t):
    t=abs(t)
    if t>=2*h:return mp.mpf(0)
    return (mp.sinh(h-t/2)-(h-t/2)*mp.cosh(t/2))/(mp.sinh(h)-h)

def rate(t,th=mp.mpf(0)):
    factor=2 if th==0 else 4*mp.cosh(th*t)
    return factor*mp.exp(-t/2)/(-mp.expm1(-2*t))

def energy(h,th=mp.mpf(0)):
    N=mp.sinh(h)-h
    factor=1 if th==0 else 2
    def integrand(t):
        if abs(t)<mp.mpf('1e-18'):
            return factor*(mp.cosh(h)-1)/(2*N)
        return rate(t,th)*(1-F(h,t))
    return mp.quad(integrand,[0,mp.mpf('0.01'),1,2*h,mp.inf])

def scalar(th=mp.mpf(0)):
    if th==0:return Cstar
    z=mp.mpf('.25')
    return 2*(C0+mp.digamma(mp.mpf('.5'))-
             (mp.digamma(z+th/2)+mp.digamma(z-th/2))/2)

def prime(h,th=mp.mpf(0)):
    limit=int(mp.floor(mp.exp(2*h)))
    composite=bytearray(limit+1)
    total=mp.mpf(0)
    for p in range(2,limit+1):
        if composite[p]:continue
        for q in range(2*p,limit+1,p):composite[q]=1
        pk=p
        while pk<=limit:
            t=mp.log(pk)
            factor=2 if th==0 else 4*mp.cosh(th*t)
            total+=factor*mp.log(p)/mp.sqrt(pk)*F(h,t)
            if pk>limit//p:break
            pk*=p
    return total

def gram(a,b,h):
    diff=a-b
    return mp.sinh((a+b)*h)/(a+b)-(h if diff==0 else mp.sinh(diff*h)/diff)

def pole(h,th=mp.mpf(0)):
    N=mp.sinh(h)-h
    if th==0:return -2*N
    half=mp.mpf('.5')
    return -2*(gram(half,half+th,h)**2+gram(half,half-th,h)**2)/N

if __name__=="__main__":
    theta=mp.mpf('.25')
    print('zeta constant =',mp.nstr(Cstar,34))
    print('shifted scalar=',mp.nstr(scalar(theta),34))
    for h in map(mp.mpf,['1','2','4']):
        Ez=energy(h)
        Qz=pole(h)+Ez-Cstar-prime(h)
        Et=energy(h,theta)
        Qt=pole(h,theta)+Et-scalar(theta)-prime(h,theta)
        print('h',h,'Arch kinetic',mp.nstr(Ez,18),
              'Arch Weil',mp.nstr(Cstar-Ez,18),
              'full zeta Q',mp.nstr(Qz,18),
              'shifted kinetic',mp.nstr(Et,18),
              'full shifted Q',mp.nstr(Qt,18))
    assert abs(Cstar-mp.mpf('5.372183419225665582232957497449742289'))<mp.mpf('1e-35')
    assert abs(scalar(theta)-mp.mpf('13.43195148413979479185361684'))<mp.mpf('1e-25')
    assert abs(Cstar-energy(mp.mpf(4))-mp.mpf('2.56906850994471947'))<mp.mpf('1e-16')
