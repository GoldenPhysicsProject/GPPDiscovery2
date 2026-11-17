"""RIGOROUS FINITE CERTIFICATE: Chebyshev square-root and Suzuki slope.

At every prime-power q<=N, check with exact integers only:
  (1+sum_{n<=q} Lambda(n)/sqrt(n))^2 < 4 sum_{n<=q} Lambda(n),
  2*(sqrt(q)-1/sqrt(q)) > sum_{n<=q}Lambda(n)/sqrt(n).

Real logs are enclosed by positive rational atanh series, sqrt by isqrt.
D(t) is strictly increasing between prime-power impulses, and G is constant
between them. Hence this covers the COMPLETE interval 0<t<=log N.
It does NOT prove the global criterion, all-width Weil positivity, or RH.

Usage: python certify_suzuki_sqrt_reserve.py 10000000
"""
import sys, time
from math import isqrt

B = 10**12
TERMS = 16
assert 9*B < 4*(2*TERMS+1)*3**(2*TERMS+1)

def ceildiv(a,b):
    return -(-a//b)

def interval_log_ratio(n,q):
    # Computes log(n/q), requiring 1 <= n/q <= 2.
    assert q <= n <= 2*q
    a=n-q
    b=n+q
    zl=B*a//b
    zu=ceildiv(B*a,b)
    pl,pu=zl,zu
    z2l=zl*zl//B
    z2u=ceildiv(zu*zu,B)
    lo=hi=0
    for j in range(TERMS):
        d=2*j+1
        lo+=2*pl//d
        hi+=ceildiv(2*pu,d)
        pl=pl*z2l//B
        pu=ceildiv(pu*z2u,B)
    # z<1/3 after dyadic reduction; the atanh remainder is < B^-1.
    return lo,hi+1

LOG2LO,LOG2HI=interval_log_ratio(2,1)
assert LOG2LO <= 693147180559 <= LOG2HI

def log_interval(n):
    k=n.bit_length()-1
    lo,hi=interval_log_ratio(n,1<<k)
    return lo+k*LOG2LO,hi+k*LOG2HI

def primes_up_to(N):
    flags=bytearray(b'\x01')*(N+1)
    flags[0]=flags[1]=0
    for p in range(2,isqrt(N)+1):
        if flags[p]:
            flags[p*p::p]=b'\x00'*((N-p*p)//p+1)
    return [p for p in range(2,N+1) if flags[p]]

def main(N):
    assert N>=2
    t0=time.monotonic()
    primes=primes_up_to(N)
    events=[]
    for p in primes:
        lo,hi=log_interval(p)
        q=p
        while q<=N:
            events.append((q,lo,hi))
            q*=p
    events.sort()
    psi_lo=0
    V_hi=0
    minD=None
    minGsq=None
    for n,logp_lo,logp_hi in events:
        sqrt_lo=isqrt(n*B*B)
        assert sqrt_lo**2<=n*B*B<(sqrt_lo+1)**2
        psi_lo+=logp_lo
        V_hi+=ceildiv(B*logp_hi,sqrt_lo)
        # Outward interval: 4*psi - (1+V)^2 > 0.
        Gsq_lower=4*psi_lo*B-(B+V_hi)**2
        assert Gsq_lower>0,(n,"G",Gsq_lower)
        if minGsq is None or Gsq_lower<minGsq[0]:
            minGsq=(Gsq_lower,n)
        invsqrt_hi=ceildiv(B*B,sqrt_lo)
        D_lower=2*(sqrt_lo-invsqrt_hi)-V_hi
        assert D_lower>0,(n,"D",D_lower)
        if minD is None or D_lower<minD[0]:
            minD=(D_lower,n)
    print("EXACT INTEGER FINITE CERTIFICATE PASS")
    print("N",N,"prime events",len(events),"primes",len(primes))
    print("smallest D lower bound",minD[0],"/",B,"at n",minD[1])
    print("smallest G squared slack",minGsq[0],"/",B**2,"at n",minGsq[1])
    print("Time",round(time.monotonic()-t0,2),"seconds")
    print("No float input to any certificate decision. No RH claim.")

if __name__=="__main__":
    main(int(sys.argv[1]) if len(sys.argv)>1 else 10000000)
