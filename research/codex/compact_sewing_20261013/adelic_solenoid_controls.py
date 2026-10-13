"""Finite exact controls for additive adelic solenoid multiscale derivation.
Golden Physics Project; Daniel Toupin's compact idelic K insight.
This script is a check, not a proof and not a finite-prime RH truncation.
Full theory: private GPP-bridge/work/codex/2026-10-13_additive_adelic_solenoid_multiscale_trace.md
"""
from fractions import Fraction
from math import factorial, gcd

def shell(q):
    if not q: raise ValueError("mean is excluded")
    j=0
    while True:
        k=q*factorial(j+1)
        if k.denominator==1:return j,k.numerator
        j+=1

def check_shell_inverse():
    qs=sorted({Fraction(k,factorial(j+1)) for j in range(8)
               for k in range(-19,20) if k})
    cs={q:Fraction((13*i+5)%17-8,i+3) for i,q in enumerate(qs)}
    before=sum((c*c for c in cs.values()),Fraction(0))
    after=Fraction(0)
    for q,c in cs.items():
        j,k=shell(q)
        assert k != 0 and Fraction(k)==q*factorial(j+1)
        v=c/k
        assert k*v==c
        after+=v*v
    assert after<=before
    print("Rational shell inverse:",len(qs),"modes, exact inequality PASS",
          "norm2 ratio",float(after/before))

def N(n):
    return sum(gcd(a,b)==1 for a in range(1,n+1)
               for b in range(1,n+1))

def check_dyadic():
    for n in (1,2,4,8,16,32,64,128):
        m=N(n); large=N(2*n)
        assert 36*m>=11*n*n
        assert 9*(large-m)>=2*n*n
        print("dyadic",n,"primitive shell",large-m,
              "lower",Fraction(2*n*n,9))

def check_theta():
    try: import mpmath as mp
    except ImportError:
        print("mpmath unavailable: optional theta check skipped")
        return
    mp.mp.dps=40
    theta=lambda y: mp.jtheta(3,0,mp.exp(-mp.pi*y*y))
    for y in (mp.mpf('0.5'),mp.mpf(1),mp.mpf(2)):
        assert abs(theta(y)-theta(1/y)/y)<mp.mpf('1e-37')
    for s in (mp.mpf('1.6'),mp.mpf(2),mp.mpf(3)):
        def r(y): return (theta(1/y)/y if y<1 else theta(y))-1
        m=mp.quad(lambda y:r(y)*y**(s-1),[0,1,4,mp.inf])
        exact=mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
        assert abs(m-exact)<mp.mpf('1e-20')
        print("theta completed Mellin s=",s,mp.nstr(m,28))

if __name__=="__main__":
    check_shell_inverse()
    check_dyadic()
    check_theta()
