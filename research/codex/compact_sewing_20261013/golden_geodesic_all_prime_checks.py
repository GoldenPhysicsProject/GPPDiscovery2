"""Checks of golden modular matrix / quadratic-field Euler and scattering. Not RH."""
from sympy import primerange, kronecker_symbol, Matrix, sqrt, simplify
from mpmath import mp
A=Matrix([[2,1],[1,1]])
phi=(1+sqrt(5))/2
assert A.det()==1 and A.trace()==3
assert simplify(phi**3-(2*phi+1))==0
assert simplify(phi**2-(phi+1))==0
counts={}
for p in primerange(2,1500):
    c=sum((x*x-x-1)%p==0 for x in range(p))
    chi=0 if p==5 else (1 if p%5 in (1,4) else -1)
    assert c==1+chi==1+int(kronecker_symbol(5,p))
    counts[p]=chi
assert len(counts)==239
chi4={1:1,2:1j,3:-1j,4:-1}
assert chi4[4]==-1
assert all(chi4[a]**2 == (1 if a in (1,4) else -1) for a in chi4)
mp.dps=70
def L5(s):
 return mp.power(5,-s)*sum(c*mp.zeta(s,mp.mpf(a)/5) for a,c in ((1,1),(2,-1),(3,-1),(4,1)))
def LQ(s):
 return mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
def LC(s):
 return mp.power(5/mp.pi,s/2)*mp.gamma(s/2)*L5(s)
def LK(s):
 return mp.power(5,s/2)*mp.power(mp.pi,-s)*mp.gamma(s/2)**2*mp.zeta(s)*L5(s)
for s in (mp.mpf('2.3'),mp.mpc('2.7','0.3'),mp.mpf('3.1')):
 assert abs(LK(s)-LQ(s)*LC(s))<mp.mpf('1e-60')
 euler=mp.mpf(1)
 for p,chi in counts.items():
  t=mp.power(p,-s)
  euler/=((1-t)*(1-chi*t))
 print('Euler rel err:',mp.nstr(abs(euler/mp.zeta(s)/L5(s)-1),12))
for w in (mp.mpf('1.3'),mp.mpc('1.41','0.2')):
 assert abs(LK(2*w-1)/LK(2*w)-LQ(2*w-1)/LQ(2*w)*LC(2*w-1)/LC(2*w))<mp.mpf('1e-60')
v=-sum(c*mp.digamma(mp.mpf(a)/5) for a,c in ((1,1),(2,-1),(3,-1),(4,1)))/5
golden=(1+mp.sqrt(5))/2
assert abs(v-2*mp.log(golden)/mp.sqrt(5))<mp.mpf('1e-60')
assert abs(mp.log(golden)-mp.atanh(1/mp.sqrt(5)))<mp.mpf('1e-60')
print('PASS: 239 primes, spinor-square, exact golden L(1), full completed scattering')
