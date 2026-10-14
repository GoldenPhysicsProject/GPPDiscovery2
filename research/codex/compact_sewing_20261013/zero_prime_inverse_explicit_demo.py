"""Numerical demo of classical explicit formula: complete xi zeros reconstruct prime-power Chebyshev psi(x).
Symmetric finite zero sums are only approximations, not an RH proof. Domain x>1 excluding prime powers.
"""
import math,mpmath as mp
from sympy import primerange
mp.mp.dps=26
xs=[2.5,4.5,7.5,10.5,20.5]
def psi(x):
 total=0.
 for p in primerange(2,int(x)+1):
  k=p
  while k<=x:
   total+=math.log(p);k*=p
 return total
ordinates=[mp.im(mp.zetazero(k)) for k in range(1,201)]
def inv(x,m):
 x=mp.mpf(str(x))
 s=mp.fsum(2*mp.re(x**(mp.mpf('.5')+1j*gm)/(mp.mpf('.5')+1j*gm)) for gm in ordinates[:m])
 return x-s-mp.log(2*mp.pi)-mp.mpf('.5')*mp.log(1-x**-2)
for x in xs:
 print(x,psi(x),*[float(inv(x,m)) for m in (20,80,200)])
