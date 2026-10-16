#!/usr/bin/env python3
"""Causal fermion systems: exact mirror degeneracy and arithmetic two-sector action.

Finite-rank operator algebra is exact (SymPy), plus high precision mpmath
tests of the genuine full-N / squarefree-N Euler products.
This DOES NOT verify a completed Weil-form factorization or prove RH.
Original conceptual setting: Golden Physics Project / Daniel Toupin.
"""
import sympy as sp
import mpmath as mp

a, b = sp.symbols("a b", complex=True)
J = sp.diag(1, -1)
O = sp.Matrix([[a,b],[sp.conjugate(b),sp.conjugate(a)]])
M = sp.simplify(J*O*J*O.conjugate().T)
c = a*sp.conjugate(a)-b*sp.conjugate(b)
assert M == c*sp.eye(2)
print("PASS: mirror spin-one closed chain double eigenvalue and L=0.")

# Spin-two direct sum of two independently mirrored channels:
# eigenvalues c1,c1,c2,c2; CFS L=Sum |lambda|^2 -(Sum |lambda|)^2/4.
r1, r2 = sp.symbols("r1 r2", real=True, nonnegative=True)
spin2_L = sp.factor(2*r1*r1+2*r2*r2-(2*r1+2*r2)**2/4)
assert sp.simplify(spin2_L-(r1-r2)**2)==0
print("PASS: spin-two CFS L=(|c1|-|c2|)^2.")

mp.mp.dps=65
sigma=mp.mpf(2)
zeta=mp.zeta
Z1=lambda s: zeta(s)
Z2=lambda s: zeta(s)/zeta(2*s)
K1=lambda u: Z1(sigma+1j*u)/Z1(sigma)
K2=lambda u: Z2(sigma+1j*u)/Z2(sigma)
def action(t,s):
    c1=abs(K1(t-s))**2-abs(K1(t+s))**2
    c2=abs(K2(t-s))**2-abs(K2(t+s))**2
    return (abs(c1)-abs(c2))**2,c1,c2

logzeta2=mp.diff(lambda s:mp.log(mp.zeta(s)),2*sigma,2)
variance_difference=4*logzeta2
assert variance_difference>0
print("Exact variance diff = 4 (log zeta)''(2 sigma) =",
      mp.nstr(variance_difference,35))
for tstr in ("0.10","0.05","0.025","0.01"):
    t=mp.mpf(tstr)
    actual,c1,c2=action(t,t)
    leading=256*logzeta2**2*t**4
    assert actual>0
    print("t=",tstr, "CFS self-action", mp.nstr(actual,23),
          "leading ratio", mp.nstr(actual/leading,16))

# Renormalized critical action at two distinct positive time arguments.
def crit_action(delta,t,s):
    sig=1+mp.mpf(delta)
    A=lambda u: abs(Z1(sig+1j*u)/Z1(sig))**2
    B=lambda u: abs(Z2(sig+1j*u)/Z2(sig))**2
    c1=A(t-s)-A(t+s)
    c2=B(t-s)-B(t+s)
    return (abs(c1)-abs(c2))**2

def limit_action(t,s):
    u=t-s;v=t+s
    d1=abs(zeta(1+1j*u))**2-abs(zeta(1+1j*v))**2
    d2=zeta(2)**2*(abs(zeta(1+1j*u)/zeta(2+2j*u))**2-
                     abs(zeta(1+1j*v)/zeta(2+2j*v))**2)
    return (abs(d1)-abs(d2))**2

t=mp.mpf('.7');s=mp.mpf('1.3')
lim=limit_action(t,s)
print("renormalized off-diagonal predicted limit:",mp.nstr(lim,20))
for d in ("0.1","0.03","0.01","0.003"):
    val=crit_action(d,t,s)/mp.mpf(d)**4
    print("delta",d,"scaled action",mp.nstr(val,20),
          "ratio",mp.nstr(val/lim,16))
print("All exact identities PASS; asymptotics are numerical spot checks only.")
