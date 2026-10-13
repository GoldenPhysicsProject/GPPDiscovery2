"""Reproducible checks of primitive rational counts and modular scattering."""
from math import gcd, log
import mpmath as mp
from sympy import mobius, divisors, totient, factorint

for n in range(1,70):
    count=sum(gcd(abs(a),b)==1 for b in range(1,n+1)
              for a in range(-n,n+1) if max(abs(a),b)==n)
    assert count==(3 if n==1 else 4*int(totient(n)))
    val=sum(int(mobius(d))*log(n//d) for d in divisors(n))
    fac=factorint(n)
    expected=log(next(iter(fac))) if len(fac)==1 else 0
    assert abs(val-expected)<1e-12

mp.mp.dps=50
for w in [mp.mpf('1.31'),mp.mpf('1.87'),mp.mpc('1.21','0.45')]:
    Z=4*mp.zeta(2*w-1)/mp.zeta(2*w)-2
    scat=mp.sqrt(mp.pi)*mp.gamma(w-mp.mpf('.5'))/mp.gamma(w)*mp.zeta(2*w-1)/mp.zeta(2*w)
    rhs=mp.sqrt(mp.pi)*mp.gamma(w-mp.mpf('.5'))/(4*mp.gamma(w))*(Z+2)
    assert abs(scat-rhs)<mp.mpf('1e-45')
print('Finite exact coefficients and 50-digit scattering samples PASS')


F=lambda y:2*mp.exp(-mp.pi*y*y)
for y in [mp.mpf('.35'),mp.mpf('.8'),mp.mpf('2')]:
    recovered=sum(int(mobius(n))*sum(F(n*k*y) for k in range(1,121)) for n in range(1,121))
    assert abs(recovered-F(y))<mp.mpf('1e-45')
print('Gaussian Möbius collapse at three scales PASS')
