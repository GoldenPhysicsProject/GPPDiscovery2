"""Numerical diagnostics for the prime-threshold Weil relative coupling.

The analytic bound and beta identity are in prime_threshold_running_coupling_2026_11_16.md.
This script is not an RH proof or a machine-checked proof of the inequalities.
"""
import mpmath as mp
mp.mp.dps=60

def weight(d):
    return mp.exp(-d/2)/(-mp.expm1(-2*d))

def kappa(d):
    z=mp.exp(-d/2)
    return mp.log((1+z)/(1-z))+2*mp.atan(z)

def at_first_rung_end(n,p):
    d=mp.log1p(mp.mpf(1)/n)
    v=mp.log(p)/mp.sqrt(n)
    K=kappa(d)
    g=2*v/K
    beta=-d*4*v*weight(d)/K**2
    assert mp.almosteq(beta,-d*weight(d)*g*g/v)
    assert g<2/mp.sqrt(n)
    assert g<1
    return d,K,g,beta

for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(9,3),
            (11,11),(17,17),(101,101),(1024,2),(1009,1009)]:
    d,K,g,beta=at_first_rung_end(n,p)
    print("n=",n,"prime=",p,"d=",mp.nstr(d,10),
          "K=",mp.nstr(K,10),"g=",mp.nstr(g,10),
          "beta=",mp.nstr(beta,10))

for d in map(mp.mpf,["0.1","0.01","0.0001","1e-8"]):
    assert abs(kappa(d)-(mp.log(4/d)+mp.pi/2))<5*d
    assert abs(2*d*weight(d)-1)<5*d

# F_theta (0<theta<1/2) also has a small local coupling;
# this is an essential NEGATIVE CONTROL, showing the rule is not RH-specific.
theta=mp.mpf("0.25")
for p in [5,11,101,1009,10007]:
    d=mp.log1p(mp.mpf(1)/p)
    base=2*mp.log(p)/(mp.sqrt(p)*kappa(d))
    shifted=2*mp.cosh(theta*mp.log(p))*base
    print("deformed n=",p,"theta=",theta,"g_theta=",mp.nstr(shifted,9))
    assert shifted>base

print("PASS: numerical diagnostics only; zero-spectrum discrimination NOT established")
