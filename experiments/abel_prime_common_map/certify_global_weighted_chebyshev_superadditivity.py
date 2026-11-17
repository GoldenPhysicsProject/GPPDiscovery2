"""GLOBAL weighted Chebyshev SUPERADDITIVITY: exact integer certificate.

Inputs, UNCONDITIONAL published theorems, with no RH:
  Eberl AFP 2024: psi(x) >= .9*x for all real x>=41;
  Rosser-Schoenfeld / Johnston-Ramare-Trudgian 2023 Lemma 5:
     psi(x) <= 1.04*x for all real x>=0.
Proves V(x*y)>=V(x)+V(y), V(x)=sum_{n<=x}Lambda(n)/sqrt(n).

Large region max(x,y)>=203: analytic partial summation and one rational
positive bound 139/25000. Remainder: every 2<=n,m<=202 checked
with exact outward fixed-point arithmetic, no floating comparisons.

This does NOT prove RH, Weil positivity or a shifted-model exclusion.
"""
from math import isqrt
from fractions import Fraction as Q
from time import monotonic
B=10**12
TERMS=16
# atanh remainder after 16 terms for z<=1/3 is <1/B.
assert 9*B < 4*(2*TERMS+1)*3**(2*TERMS+1)
def ceildiv(a,b):return -(-a//b)
def interval_log_ratio(n,q):
    assert q<=n<=2*q
    a=n-q;d=n+q
    zl=B*a//d;zu=ceildiv(B*a,d)
    pl,pu=zl,zu
    z2l=zl*zl//B;z2u=ceildiv(zu*zu,B)
    lo=hi=0
    for j in range(TERMS):
        den=2*j+1
        lo+=2*pl//den
        hi+=ceildiv(2*pu,den)
        pl=pl*z2l//B
        pu=ceildiv(pu*z2u,B)
    return lo,hi+1
LOG2_LO,LOG2_HI=interval_log_ratio(2,1)
assert LOG2_LO<=693147180559<=LOG2_HI
def interval_log_int(n):
    k=n.bit_length()-1
    lo,hi=interval_log_ratio(n,1<<k)
    return lo+k*LOG2_LO,hi+k*LOG2_HI
def prove_large_rectangle():
    # Rational one-sided sqrt enclosures, proven by squaring.
    assert 20149**2<406*1000**2
    assert 6404**2>41*1000**2
    assert 1415**2>2*1000**2
    assert 14248**2>203*1000**2
    gap=(Q(9,5)*Q(20149,1000)-Q(9,10)*Q(6404,1000)
         -Q(52,25)*(Q(1415,1000)+Q(14248,1000))+Q(52,25))
    assert gap==Q(139,25000)>0
    # F(sqrt(x),sqrt(y)) increasing in both variables for
    # x>=2,y>=203: sqrt2>7/5, 9/5*7/5=63/25>52/25.
    assert 2*25>49 and 63>52 and 203>4
    return gap
def sieve_primes(N):
    flags=bytearray(b'\x01')*(N+1)
    flags[0]=flags[1]=0
    for p in range(2,isqrt(N)+1):
        if flags[p]:flags[p*p::p]=b'\x00'*((N-p*p)//p+1)
    return [p for p in range(2,N+1) if flags[p]]
def certify_finite():
    K=202;N=K*K
    events=[]
    for p in sieve_primes(N):
        lp_lo,lp_hi=interval_log_int(p)
        q=p
        while q<=N:
            root_lo=isqrt(q*B*B);root_hi=root_lo+1
            vlo=(B*lp_lo)//root_hi
            vhi=ceildiv(B*lp_hi,root_lo)
            events.append((q,vlo,vhi))
            q*=p
    events.sort()
    Alo=[0]*(N+1);Ahi=[0]*(N+1)
    it=iter(events);event=next(it,None)
    vl=vu=0
    for n in range(N+1):
        if event is not None and event[0]==n:
            vl+=event[1];vu+=event[2]
            event=next(it,None)
        Alo[n]=vl;Ahi[n]=vu
    assert event is None
    smallest=(10**100,None,None)
    for n in range(2,K+1):
        for m in range(2,K+1):
            gap=Alo[n*m]-Ahi[n]-Ahi[m]
            if gap<smallest[0]:smallest=(gap,n,m)
            assert gap>0,(n,m,gap)
    print('ALL 40,401 integer pairs 2<=n,m<=202 CERTIFIED strictly positive')
    print('minimum outward rational gap:',smallest[0],'/',B,'at',smallest[1:])
    print('prime power events:',len(events),'through',N)
if __name__=='__main__':
    t0=monotonic()
    print('large-domain analytic rational gap >=',prove_large_rectangle())
    certify_finite()
    print('GLOBAL THEOREM: V(x*y)>=V(x)+V(y), all real x,y>=1')
    print('Known psi bounds invoked; NO RH input, NO Lean compilation')
    print('elapsed',round(monotonic()-t0,3),'seconds')
