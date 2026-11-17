"""Zero-free-data, exact outward rational certificate for the completed F_theta Suzuki control.

F_theta(s) = xi(s-1/4)*xi(s+1/4); Phi_theta = 1/2 L^-1[(Xi_F'/Xi_F)(1/2+z)/z^2].
At t=log(3100), certify Phi_theta(t)<0 using only integers/Fraction.
No zeros, floating point, Arb, or unsafe float enter any acceptance decision.
"""
from fractions import Fraction as Q
from math import isqrt

B = 10**16
Q0 = 3100
GAMMA_N = 220
LOG_TERMS = 27

def ceildiv(a,b): return -((-a)//b)
def floor_q(x): return x.numerator * B // x.denominator
def ceil_q(x): return ceildiv(x.numerator * B, x.denominator)

class I:
    def __init__(self, lo, hi):
        self.lo = int(lo); self.hi = int(hi)
        assert self.lo <= self.hi
    @classmethod
    def rat(cls, a, b=1):
        q=Q(a,b); return cls(floor_q(q),ceil_q(q))
    def __add__(self, o):
        o=conv(o); return I(self.lo+o.lo, self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-conv(o))
    def __rsub__(self,o):return conv(o)+(-self)
    def __mul__(self,o):
        o=conv(o)
        v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v)//B,ceildiv(max(v),B))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0
        return I(B*B//self.hi,ceildiv(B*B,self.lo))
    def __truediv__(self,o):return self*conv(o).inv()
    def __repr__(self):
        return f'[{Q(self.lo,B)}, {Q(self.hi,B)}]'
    def dec(self):
        return (str(self.lo/B),str(self.hi/B))

def conv(x): return x if isinstance(x,I) else I.rat(x)

def log_of_2():
    z=Q(1,3)
    s=2*sum((z**(2*k+1)/(2*k+1) for k in range(LOG_TERMS)),Q(0))
    tail=2*z**(2*LOG_TERMS+1)/(Q(2*LOG_TERMS+1)*(1-z*z))
    return I(floor_q(s),ceil_q(s+tail))

LOG2=log_of_2()

def log_positive_rational(x):
    assert x>0
    z=(x-1)/(x+1)
    assert 0<=z<=Q(1,3), (x,z)
    s=2*sum((z**(2*k+1)/(2*k+1) for k in range(LOG_TERMS)),Q(0))
    tail=2*z**(2*LOG_TERMS+1)/(Q(2*LOG_TERMS+1)*(1-z*z))
    return I(floor_q(s),ceil_q(s+tail))

def log_int(n):
    assert n>0
    k=n.bit_length()-1
    x=Q(n,1<<k)
    return k*LOG2+log_positive_rational(x)

def arctan_interval(x,N=16):
    z=sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(N)),Q(0))
    rem=x**(2*N+1)/(2*N+1)
    return (z,z+rem) if N%2==0 else (z-rem,z)

# Machin pi formula with alternating rational bounds.
a0,a1=arctan_interval(Q(1,5)); b0,b1=arctan_interval(Q(1,239))
PI=I(floor_q(16*a0-4*b1),ceil_q(16*a1-4*b0))
assert PI.lo>3*B and PI.hi<Q(22,7)*B
# log(pi/2) from monotonic endpoint bounds.
LNPI=LOG2+I(log_positive_rational(Q(PI.lo,2*B)).lo,
             log_positive_rational(Q(PI.hi,2*B)).hi)

# Euler constant: H_M - log(M+1) < gamma < H_M - log(M).
M=100000
harmlo=sum(B//k for k in range(1,M+1))
harmhi=sum(ceildiv(B,k) for k in range(1,M+1))
GAMMA=I(harmlo-log_int(M+1).hi,harmhi-log_int(M).lo)

# Exact fourth-root outward enclosure, then reciprocal.
def root4(n):
    x=isqrt(isqrt(n*B**4))
    assert x**4<=n*B**4 < (x+1)**4
    return I(x,x+1)

SQRT2=I(isqrt(2*B*B),isqrt(2*B*B)+1)
# psi(1/8)+psi(3/8) = -2*gamma -8log2 -pi sqrt(2).
C=-GAMMA/2-2*LOG2-(PI*SQRT2)/4-LNPI/2
T=log_int(Q0)
R=root4(Q0)
E1=R.inv()           # q^-1/4
E3=E1*E1*E1         # q^-3/4

def e_neg_b(bnum):
    assert abs(bnum) in (1,3)
    v=E1 if abs(bnum)==1 else E3
    return v if bnum>0 else v.inv()

# J_(bnum/4)(t) = (q^(-bnum/4)-1+(bnum/4)*log q)/(bnum/4)^2.
POLE=I.rat(0)
for bn in [1,-1,3,-3]:
    pole=(e_neg_b(bn)-1+I.rat(bn,4)*T)*I.rat(16,bn*bn)
    POLE+=pole/2

# Gamma: one half of both ladders at a=1/4 and a=3/4.
# j>=GAMMA_N positive tail <= integral from N-1 of 1/(2x+a)^2.
# In suppressed exponential subtractions j>=3:
# sum q^-(2j+a)/(2j+a)^2 <= q^-6/((6+a)^2(1-q^-2)).
G_LO=I.rat(0); G_HI=I.rat(0)
for aa in [1,3]:
    v=E1 if aa==1 else E3
    S=I.rat(0)
    for j in range(GAMMA_N):
        lamnum=8*j+aa
        S+=I.rat(16,lamnum*lamnum)
    subtract=I.rat(0)
    for j in range(3):
        lamnum=8*j+aa
        subtract+=(v*I.rat(1,Q0**(2*j)))*I.rat(16,lamnum*lamnum)
    sub_tail=I.rat(16*Q0*Q0,(Q0**6)*(24+aa)**2*(Q0*Q0-1))
    tail=I.rat(2,8*(GAMMA_N-1)+aa)
    G_LO+=I(S.lo-subtract.hi-sub_tail.hi,S.lo-subtract.hi-sub_tail.hi)/2
    G_HI+=I(S.hi-subtract.lo+tail.hi,S.hi-subtract.lo+tail.hi)/2
G=I(G_LO.lo,G_HI.hi)

# Actual Euler-local Lambda, for all prime powers n < q.
# Lambda(n)*cosh(log(n)/4)/sqrt(n) =
# Lambda(n)*(n^-1/4+n^-3/4)/2.
prime=I.rat(0)
comp=bytearray(Q0+1)
primes=[]
for p in range(2,Q0+1):
    if not comp[p]:
        primes.append(p)
        for k in range(p*p,Q0+1,p):comp[k]=1
num_events=0
for p in primes:
    lp=log_int(p)
    n=p; k=1
    while n<Q0:
        s=root4(n).inv()
        s3=s*s*s
        weight=lp*(s+s3)/2
        ramp=T-k*lp
        assert ramp.lo>=0, ('bad ramp',p,k,n,ramp.lo)
        prime+=weight*ramp
        num_events+=1
        if n>Q0//p:break
        n*=p; k+=1

result=POLE+C*T+G-prime
print('CERTIFICATE: completed F_theta, theta=1/4, t=log(3100)')
print('events',num_events,'prime-count',len(primes),'gamma terms',GAMMA_N)
for name,x in [('pi',PI),('log pi',LNPI),('gamma Euler',GAMMA),
               ('C theta',C),('t',T),('pole',POLE),('gamma tower',G),
               ('prime ramp',prime),('potential',result)]:
    print(name, 'scaled lower/upper:',x.lo,x.hi,'approx:',x.dec())
assert num_events==478
assert result.lo==-254019420779638, 'regression: expected lower endpoint'
assert result.hi==-242214951940130, 'regression: expected upper endpoint'
assert result.hi < 0, 'FAILED to certify negative'
print('PASS: rigorously negative; upper bound <=',Q(result.hi,B))
