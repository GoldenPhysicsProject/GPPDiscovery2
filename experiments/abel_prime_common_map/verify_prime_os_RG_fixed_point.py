"""Numerical audit of positive prime RG kernel K_eps(t,u).

THEOREM in companion research note: K_eps -> 1/(1+t+u) as eps -> 0+
by Euler pole Laurent expansion. Numerical checks are not RH evidence.
"""
import mpmath as mp
mp.mp.dps=75
def h(s):
    return -mp.diff(mp.zeta,s)/mp.zeta(s)
def K(e,t,u):
    return h(1+e*(1+t+u))/h(1+e)
T=[mp.mpf('0'),mp.mpf('.15'),mp.mpf('.5'),mp.mpf('1')]
for es in ['.2','.05','.01','.001','.0001']:
    e=mp.mpf(es)
    err=err1=mp.mpf(0)
    for t in T:
        for u in T:
            r=t+u
            observed=K(e,t,u)
            fixed=1/(1+r)
            first=fixed-mp.euler*e*r/(1+r)
            err=max(err,abs(observed-fixed))
            err1=max(err1,abs(observed-first))
            assert observed>0
    print("epsilon",es,"|K-K*|",mp.nstr(err,14),"first-order residual",mp.nstr(err1,14))
# Exact positive Gram uses exponential integral.
cs=[mp.mpf(1),mp.mpf('-1.5'),mp.mpf('.7')]
ts=T[:3]
q=mp.fsum(cs[i]*cs[j]/(1+ts[i]+ts[j]) for i in range(3) for j in range(3))
qi=mp.quad(lambda x:mp.exp(-x)*mp.fsum(cs[i]*mp.exp(-ts[i]*x) for i in range(3))**2,[0,mp.inf])
assert mp.almosteq(q,qi) and q>0
# Shifted coefficients have exactly the SAME universal fixed point:
theta=mp.mpf('.2')
hth=lambda s:(h(s-theta)+h(s+theta))/2
for es in ['.01','.001','.0001']:
    e=mp.mpf(es)
    r=mp.mpf('1.1')
    observed=hth(1+theta+e*(1+r))/hth(1+theta+e)
    assert abs(observed-1/(1+r))<mp.mpf('.01')
    print("shifted theta=.2 eps",es,"kernel",mp.nstr(observed,16))
print("PASS fixed point and shifted control numerical audit; NO RH CLAIM")
