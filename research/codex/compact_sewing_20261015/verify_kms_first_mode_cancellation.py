#!/usr/bin/env python3
"""Exact first Archimedean KMS-mode cancellation at the critical half-density.

Covers zeta and shifted F_theta fake. The symbolic identity is zero-independent.
Sharp odd window is a numerical diagnostic (not C_c^infinity).
Golden Physics Project / Daniel Toupin; Codex 2026-10-15.
"""
import mpmath as mp
mp.mp.dps=45
half=mp.mpf('0.5')

def F_h(h,t):
    if not (0<=t<=2*h):
        return mp.mpf(0)
    n=mp.sinh(h)-h
    return (mp.sinh(h-t/2)-(h-t/2)*mp.cosh(t/2))/n

def integrals(h,theta):
    ap=half+theta
    am=half-theta
    f=lambda t:F_h(h,t)
    k=2*mp.quad(lambda t:(mp.exp(-ap*t)+mp.exp(-am*t))*f(t),[0,h,2*h])
    mean=4*mp.quad(lambda t:mp.exp(t/2)*mp.cosh(theta*t)*f(t),[0,h,2*h])
    e0=2*mp.quad(lambda t:(mp.exp(-ap*t)+mp.exp(-am*t))*(1-f(t)),[0,h,2*h])+2*(mp.exp(-ap*2*h)/ap+mp.exp(-am*2*h)/am)
    exact=2*(1/ap+1/am)
    assert abs(k+e0-exact)<mp.mpf('1e-38'), (k,e0,exact)
    return k,e0,exact,mean

def spectral_check(x):
    a=half
    k=1/(x*x+a*a)
    phi=mp.re(mp.digamma(mp.mpf('.25')+x*1j/2)-mp.digamma(mp.mpf('.25')))
    tail=mp.nsum(lambda j:2*x*x/((2*j+a)*((2*j+a)**2+x*x)),[1,mp.inf])
    assert abs(phi+k-4-tail)<mp.mpf('1e-35')
    return phi+k,4+tail

def main():
    for x in map(mp.mpf,['0','.2','1','4','8']):
        lhs,rhs=spectral_check(x)
        print('spectral ξ=',mp.nstr(x,5),
              'E∞+K=',mp.nstr(lhs,26),'4+tail=',mp.nstr(rhs,26))
    for h in map(mp.mpf,['.76','2','4']):
        for theta in map(mp.mpf,['0','.25']):
            k,e0,exact,mean=integrals(h,theta)
            print('h=',mp.nstr(h,6),'theta=',mp.nstr(theta,5),
                  'kernel=',mp.nstr(k,25),'E0=',mp.nstr(e0,25),
                  'K+E0=',mp.nstr(exact,25))
    print('PASS: all identities; no global RH positivity inferred')

if __name__=='__main__':
    main()
