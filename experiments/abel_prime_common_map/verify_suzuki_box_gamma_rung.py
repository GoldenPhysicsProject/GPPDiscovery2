"""60-digit audit: completed Weil on box = twice full Suzuki screw potential;
prime-continuum subtraction removes the first gamma rung; curvature plastic root.

This script verifies algebra at sampled widths; it does NOT certify RH,
positivity on every interval, or any unbounded number-theoretic assertion.
"""
import math
import mpmath as mp
mp.mp.dps=60
CINF=-mp.euler-mp.log(mp.pi)-mp.pi/2-3*mp.log(2)
C=mp.pi**2+8*mp.catalan

def prime_events(N):
    sieve=bytearray(b'\x01')*(N+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,math.isqrt(N)+1):
        if sieve[p]:
            sieve[p*p::p]=b'\x00'*((N-p*p)//p+1)
    data=[]
    for p in range(2,N+1):
        if sieve[p]:
            logp=mp.log(p)
            n=p
            while n<=N:
                data.append((mp.mpf(n),logp/mp.sqrt(n)))
                n*=p
    return data
events=prime_events(5000)
def triangle(L):
    return mp.fsum(v*(L-mp.log(n)) for n,v in events if mp.log(n)<L)
def Ebox(L):
    return (C-mp.exp(-L/2)*mp.lerchphi(mp.exp(-2*L),2,mp.mpf('0.25')))/2
def pole(L):
    return 16*(mp.cosh(L/2)-1)
def H(L):
    return 4*(mp.exp(L/2)+mp.exp(-L/2)-2)-triangle(L)
def Psi(L):
    return H(L)+CINF*L/2+Ebox(L)/2
def W(L):
    return Ebox(L)+CINF*L+pole(L)-2*triangle(L)
def Ehigh(L):
    # Yukawa box Y=2int_0^L(L-t) exp(-t/2)dt.
    Y=4*L-8+8*mp.exp(-L/2)
    E0=4*L-Y
    return Ebox(L)-E0
def residual(L):
    return triangle(L)-(4*(mp.exp(L/2)-1)-2*L)
def k(t):
    return mp.exp(t/2)-mp.exp(-mp.mpf('2.5')*t)/(1-mp.exp(-2*t))
def Fprime(t):
    return 2*(mp.exp(t/2)-mp.exp(-t/2))+CINF/2+mp.atanh(mp.exp(-t/2))+mp.atan(mp.exp(-t/2))

for L0 in ['.12','.3','.69','.7','1','1.4','2.5','5','8']:
    L=mp.mpf(L0)
    left=W(L)
    right=2*Psi(L)
    cancel=(CINF+4)*L+Ehigh(L)-2*residual(L)
    assert abs(left-right)<mp.mpf('1e-50')
    assert abs(left-cancel)<mp.mpf('1e-50')
    assert Ehigh(L)>=0
    print('L',L0,'Wbox',mp.nstr(left,25),'2Psi',mp.nstr(right,25))
r=mp.findroot(lambda z:z**3-z-1,mp.mpf('1.3'))
tstar=mp.log(r)
assert abs(k(tstar))<mp.mpf('1e-50')
assert k(mp.mpf('.1'))<0<k(mp.mpf('.5'))
print('plastic root:',mp.nstr(r,50),'threshold:',mp.nstr(tstar,50))
print('Cinf+4:',mp.nstr(CINF+4,30))
ns=sorted(set(int(n) for n,v in events))
for n,m in zip(ns[:23],ns[1:24]):
    a=mp.log(n);length=mp.log(mp.mpf(m)/n)
    count=mp.fsum(v for q,v in events if q<=n)
    y=Psi(a);d=Fprime(a)-count;c=k(a)
    assert c>0
    u=max(mp.mpf(0),min(length,-d/c))
    lower=y+d*u+c*u*u/2
    assert lower>0
    print('event',n,'to',m,'parabola bound',mp.nstr(lower,16))
print('PASS exact formula checks and first 23 NUMERICAL event lower bounds; NOT an RH proof.')
