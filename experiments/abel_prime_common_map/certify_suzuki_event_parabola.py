"""Exact fixed-point rational certificate for Suzuki interval parabola test.

No RH claim: a finite prime-power range only. The mathematical implication
comes from the explicit full Suzuki potential and positive increasing
inter-event curvature. All acceptance comparisons below use integers.
"""
from math import isqrt
from fractions import Fraction as Q
from time import monotonic
from certify_global_weighted_chebyshev_superadditivity import (
    B, ceildiv, interval_log_int, sieve_primes
)
import sys
MAX_Q=int(sys.argv[1]) if len(sys.argv)>1 else 100_000

def lo(q):return q.numerator*B//q.denominator
def hi(q):return ceildiv(q.numerator*B,q.denominator)
def arctan_interval(x,N=12):
    z=Q(0)
    for k in range(N):
        a=x**(2*k+1)/(2*k+1)
        z+=a if k%2==0 else -a
    e=x**(2*N+1)/(2*N+1)
    return (z,z+e) if N%2==0 else (z-e,z)
def log_via_atanh(x,N=20):
    z=(x-1)/(x+1)
    s=2*sum((z**(2*k+1)/(2*k+1) for k in range(N)),Q(0))
    tail=2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
    return s,s+tail

def constants():
    a5,b5=arctan_interval(Q(1,5))
    a239,b239=arctan_interval(Q(1,239))
    pi_lo=16*a5-4*b239;pi_hi=16*b5-4*a239
    assert pi_lo<Q(22,7) and pi_hi>3
    ln2lo,ln2hi=log_via_atanh(Q(2))
    tlo,tlo_hi=log_via_atanh(pi_lo/2,N=16)
    thi_lo,thi=log_via_atanh(pi_hi/2,N=16)
    lnpi_lo=ln2lo+tlo;lnpi_hi=ln2hi+thi
    assert lnpi_lo < lnpi_hi
    n=100_000
    Hlo=sum(B//k for k in range(1,n+1))
    Hhi=sum(ceildiv(B,k) for k in range(1,n+1))
    lNlo,lNhi=interval_log_int(n)
    lNp1lo,lNp1hi=interval_log_int(n+1)
    gamma_lo=Hlo-lNp1hi; gamma_hi=Hhi-lNlo
    # Alternating Catalan G=sum (-1)^k/(2k+1)^2; even K -> lower sum.
    K=1000
    glo=ghi=0
    for k in range(K):
        den=(2*k+1)**2
        if k%2==0:
            glo+=B//den;ghi+=ceildiv(B,den)
        else:
            glo-=ceildiv(B,den);ghi-=B//den
    ghi+=ceildiv(B,(2*K+1)**2)
    pi_slo=lo(pi_lo);pi_shi=hi(pi_hi)
    lnpi_slo=lo(lnpi_lo);lnpi_shi=hi(lnpi_hi)
    ln2_slo=lo(ln2lo);ln2_shi=hi(ln2hi)
    # C=pi^2+8 Catalan
    C_lo=(pi_slo*pi_slo)//B+8*glo
    C_hi=ceildiv(pi_shi*pi_shi,B)+8*ghi
    # Cinf=-gamma-lnpi-pi/2-3ln2
    ci_lo=-gamma_hi-lnpi_shi-ceildiv(pi_shi,2)-3*ln2_shi
    ci_hi=-gamma_lo-lnpi_slo-(pi_slo//2)-3*ln2_slo
    assert ci_hi<0 and ci_lo<=ci_hi
    print('Cinf outward interval:',ci_lo,'/',B,'to',ci_hi,'/',B)
    print('C=pi²+8Catalan outward interval:',C_lo,'/',B,'to',C_hi,'/',B)
    print('width(Cinf):',(ci_hi-ci_lo)/B,'width(C):',(C_hi-C_lo)/B)
    return ci_lo,ci_hi,C_lo,C_hi

def sums_q(q,terms=16):
    # L1=sum_{k>=0} q^-2k/(4k+1), L2=sum q^-2k/(4k+1)^2.
    # Error bound after K: q^-2K/[(4K+1)^r (1-q^-2)].
    ll1=uu1=ll2=uu2=0
    power=1
    qq=q*q
    for k in range(terms):
        odd=4*k+1
        d=power*odd
        ll1+=B//d;uu1+=ceildiv(B,d)
        d2=d*odd
        ll2+=B//d2;uu2+=ceildiv(B,d2)
        power*=qq
    e1=ceildiv(B*qq, power*(qq-1)*(4*terms+1))
    e2=ceildiv(B*qq, power*(qq-1)*(4*terms+1)**2)
    return ll1,uu1+e1,ll2,uu2+e2

def run():
    tstart=monotonic()
    ci_lo,ci_hi,Clo,Chi=constants()
    events=[]
    for p in sieve_primes(MAX_Q):
        lp_lo,lp_hi=interval_log_int(p)
        q=p
        while q<=MAX_Q:
            events.append((q,lp_lo,lp_hi))
            q*=p
    events.sort()
    Alo=Ahi=Blo=Bhi=0
    worst=(10**100,None)
    for idx,(q,lp_lo,lp_hi) in enumerate(events):
        lq_lo,lq_hi=interval_log_int(q)
        root_lo=isqrt(q*B*B);root_hi=root_lo+1
        inv_lo=(B*B)//root_hi
        inv_hi=ceildiv(B*B,root_lo)
        v_lo=(B*lp_lo)//root_hi
        v_hi=ceildiv(B*lp_hi,root_lo)
        Alo+=v_lo;Ahi+=v_hi
        Blo+=(v_lo*lq_lo)//B
        Bhi+=ceildiv(v_hi*lq_hi,B)
        sum1_lo,sum1_hi,sum2_lo,sum2_hi=sums_q(q)
        # full F(log q), with Ebox/2=C/4 -4 invsqrt * L2(q)
        f_lo=(4*(root_lo+inv_lo-2*B)
             +(ci_lo*lq_hi)//(2*B) + Clo//4
             -ceildiv(4*inv_hi*sum2_hi,B))
        f_hi=(4*(root_hi+inv_hi-2*B)
             +ceildiv(ci_hi*lq_lo,2*B)+ceildiv(Chi,4)
             -(4*inv_lo*sum2_lo)//B)
        y_lo=f_lo-ceildiv(Ahi*lq_hi,B)+Blo
        y_hi=f_hi-(Alo*lq_lo)//B+Bhi
        # derivative F'(log q)-sum v
        d_lo=(2*(root_lo-inv_hi)+ci_lo//2
            +(2*inv_lo*sum1_lo)//B-Ahi)
        d_hi=(2*(root_hi-inv_lo)+ceildiv(ci_hi,2)
            +ceildiv(2*inv_hi*sum1_hi,B)-Alo)
        # exact k(log q)=sqrt(q)*(1-1/[q(q²-1)])
        denom=q*(q*q-1)
        k_lo=root_lo*(denom-1)//denom
        k_hi=ceildiv(root_hi*(denom-1),denom)
        assert y_lo<=y_hi and d_lo<=d_hi and k_lo>0
        # For u>=0, Psi(a+u)>=y+d*u+k*u²/2; true min >= y-d_-²/(2k).
        negative=max(-d_lo,0)
        margin=2*k_lo*y_lo-negative*negative
        if margin<worst[0]:worst=(margin,q)
        if margin<=0:
            print('COUNTEREXAMPLE TO THIS CERTIFICATE OR BAD INTERVAL',q,margin,'y',y_lo,y_hi,'d',d_lo,d_hi)
            return False
        if idx and idx%200000==0:
            print('verified',idx,'events; elapsed',round(monotonic()-tstart,2),'seconds',flush=True)
    print('CERTIFIED event-parabola positive at ALL',len(events),'prime-power events q<=',MAX_Q)
    print('minimum integer polynomial margin:',worst[0],'/10^24 at q=',worst[1])
    print('The initial interval (0, log2) is certified separately by certify_suzuki_initial_interval.py.')
    print('No all-event theorem, no RH proof; elapsed',round(monotonic()-tstart,2),'seconds')
    return True
if __name__=='__main__':
    assert run()
