#!/usr/bin/env python3
"""Pure exact-integer/rational interval proof certificate for chi4 on h<=log(3)/2.
Every asserted inequality is decided by integers or Fraction, never floats.
Author: Golden Physics Project / Codex, 2026-10-15.
Full analytic ground-state derivation in GPP-bridge work/codex/
2026-10-15_chi4_positive_ground_state_first_prime_window.md.
NOT a proof of Dirichlet GRH.
"""
from fractions import Fraction as F
from math import factorial

Q=10**20
def floor(a,b): return a//b
def ceil(a,b): return -((-a)//b)

class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(self.lo if hi is None else hi)
        assert self.lo<=self.hi
    @classmethod
    def frac(cls,z):
        z=F(z)
        return cls(floor(z.numerator*Q,z.denominator),ceil(z.numerator*Q,z.denominator))
    def __add__(self,y):
        y=iv(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-iv(y)
    def __rsub__(self,y):return iv(y)+-self
    def __mul__(self,y):
        y=iv(y)
        v=(self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi)
        return I(floor(min(v),Q),ceil(max(v),Q))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=iv(y)
        assert y.lo>0
        return self*I(floor(Q*Q,y.hi),ceil(Q*Q,y.lo))
    def __rtruediv__(self,y):return iv(y)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=iv(1);b=self
        while n:
            if n&1:r=r*b
            b=b*b;n//=2
        return r
    def __str__(self):
        def decimal(v):
            sign="-" if v<0 else ""
            v=abs(v)
            return sign+str(v//Q)+"."+str(v%Q).zfill(20)
        return "["+decimal(self.lo)+", "+decimal(self.hi)+"]"

def iv(x):return x if isinstance(x,I) else I.frac(x)

def exp_minus_unit(z):
    assert 0<=z.lo<=z.hi<=Q
    term=iv(1);part=iv(1);upper=None
    for n in range(1,24):
        term=term*z/iv(n)
        part=part-term if n%2 else part+term
        if n==22:upper=part
    # Alternating Maclaurin bounds S23 <= exp(-z) <= S22.
    return I(part.lo,upper.hi)

def exp_minus(z):
    assert z.lo>=0
    t=z/iv(64);assert t.hi<=Q
    return exp_minus_unit(t)**64

def sin(z):
    assert 0<=z.lo<=z.hi<2*Q
    part=iv(0)
    for n in range(14):
        t=z**(2*n+1)/iv(factorial(2*n+1))
        part=part-t if n%2 else part+t
        if n==12:upper=part
        if n==13:lower=part
    return I(lower.lo,upper.hi)

def cos(z):
    assert 0<=z.lo<=z.hi<2*Q
    part=iv(0)
    for n in range(15):
        t=z**(2*n)/iv(factorial(2*n))
        part=part-t if n%2 else part+t
        if n==13:lower=part
        if n==14:upper=part
    return I(lower.lo,upper.hi)

def log_bounds(a,N):
    # log a = 2 atanh((a-1)/(a+1)); geometric bound for positive tail
    y=F(a-1,a+1)
    lower=2*sum((y**(2*n+1)/F(2*n+1) for n in range(N)),F(0))
    tail=2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
    return lower,lower+tail

def atan_bounds(x,N=20):
    # Lower alternating truncation through n=19, upper via next term
    lower=sum(((-1)**n*x**(2*n+1)/F(2*n+1) for n in range(N)),F(0))
    upper=lower+x**(2*N+1)/F(2*N+1)
    return lower,upper

# Exact enclosure of h=(log3)/2, using rational positive atanh series.
lo,hi=log_bounds(3,70)
lo/=2;hi/=2
h=I.frac(lo)+I(0,ceil((hi-lo).numerator*Q,(hi-lo).denominator))
assert 0<h.lo and h.hi < F(55,100)*Q

# All remaining arithmetic constants are bounded by exact rational statements.
atan5=atan_bounds(F(1,5))
atan239=atan_bounds(F(1,239))
pi_lo=16*atan5[0]-4*atan239[1]
pi_hi=16*atan5[1]-4*atan239[0]
assert F(157,50)<pi_lo and pi_hi<F(22,7)
ln2=log_bounds(2,60);ln5=log_bounds(5,110)
ln200_lo=3*ln2[0]+2*ln5[0]
H200=sum((F(1,n) for n in range(1,201)),F(0))
# gamma <= H200 - log 200 < 0.58
assert H200-ln200_lo<F(29,50)
z=F(46,25)
# exp(1.84) > 44/7 > 2pi, so log(2pi) < 1.84
assert sum((z**n/F(factorial(n)) for n in range(8)),F(0))>F(44,7)
# log(2pi)+gamma-pi/2 < 1.84+.58-1.57 = .85
assert F(46,25)+F(29,50)-F(157,100)==F(85,100)

# Kernel: nu_odd(t)=2 sum_j exp(-(3/2+2j)t), and
# ground-state phi(x)=cos(kx), k=19/10, |x|<=h.
k=iv(F(19,10))
assert (k*h).hi<F(11,10)*Q
ck=cos(k*h);sk=sin(k*h)
assert ck.lo>0
N=15;cells=100
a=[iv(F(3,2)+2*j) for j in range(N)]
sign=[aj*ck-k*sk for aj in a]
assert sign[0].hi<0 and all(x.lo>0 for x in sign[1:])
diag=sum((2*k*k/(aj*(aj*aj+k*k)) for aj in a),iv(0))

def boundary(j,grid_index):
    aj=a[j]
    ix=F(grid_index,cells)
    x=h*iv(ix)
    near=exp_minus(aj*h*iv(1-ix))
    far=exp_minus(aj*h*iv(1+ix))
    return (near+far)*sign[j]/((aj*aj+k*k)*cos(k*x))

worst=None;cell=None
for idx in range(cells):
    # b0 decreases with |x|; all bj, j>=1, increase.
    # Infinite tail j>=15 is nonnegative; omitting it lowers the value.
    C=diag+boundary(0,idx+1)+sum((boundary(j,idx) for j in range(1,N)),iv(0))
    if worst is None or C.lo<worst.lo:
        worst=C;cell=idx
    assert C.lo>iv(F(87,100)).hi, (idx,str(C))

# For all real Cc^infty g supported on [-h,h],
# E_odd(g)>=0.87||g||² by the exact nonlocal Picone identity.
# Since c1-log4<.85 and chi4(2)=0:
assert F(87,100)-F(85,100)==F(1,50)
print("Every comparison passed using exact integer/rational interval arithmetic.")
print("h=(log3)/2:",h)
print("worst spatial cell:",cell,"of",cells)
print("lower interval:",worst)
print("Theorem: Q_chi4(g)>0.02||g||² for real smooth support |x|<=(log3)/2.")
print("Scope: first prime-active window only. RH/GRH OPEN.")
