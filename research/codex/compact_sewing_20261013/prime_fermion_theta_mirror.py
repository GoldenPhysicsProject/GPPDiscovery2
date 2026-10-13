"""Exact prime-fermion Fock and theta-Poisson mirror, independent of RH.

Each n corresponds to fermion orbitals (p,j) from binary digits of v_p(n).
The completed Gaussian theta amplitude is even around s=1/2. This alone
does NOT imply the nontrivial zeros are on the mirror axis.
"""
import math
import sympy as sp
import mpmath as mp
mp.mp.dps=42

def orbitals(n):
    assert n>=1
    return [(int(p),j) for p,k in sp.factorint(n).items()
            for j in range(k.bit_length()) if (k>>j)&1]

for n in range(1,1001):
    S=orbitals(n)
    assert len(S)==len(set(S))
    assert math.prod(p**(2**j) for p,j in S)==n

x=sp.symbols('x')
for J in range(1,10):
    assert sp.cancel(sp.prod(1+x**(2**j) for j in range(J))
                     -(1-x**(2**J))/(1-x))==0

def Xi(s):
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)/2

def Phi(x):
    return mp.nsum(lambda n:mp.exp(-mp.pi*n*n*x),[1,mp.inf])

def Mirror(z):
    I=mp.quad(lambda x:Phi(x)*x**mp.mpf('.25')*
              mp.cosh(z*mp.log(x)/2)/x,[1,3,9,mp.inf])
    return mp.mpf('.5')+(z*z-mp.mpf('.25'))*I

for z in [0,1j*mp.mpf('14.134725141734693790457251983562'),
          mp.mpc('.17','9.5'),mp.mpc('-.17','9.5')]:
    err=abs(Mirror(z)-Xi(mp.mpf('.5')+z))
    print('z',mp.nstr(z,8),'error',mp.nstr(err,6))
    assert err < mp.mpf('1e-33')
print('Prime fermionization and completed theta mirror verified; RH OPEN')
