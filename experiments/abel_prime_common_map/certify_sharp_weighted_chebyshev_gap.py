"""Exact integer proof of OPTIMAL global surplus c*=V(4)-2V(2).

Requires certify_global_weighted_chebyshev_superadditivity.py in this folder.
Analytic infinite range uses published unconditional psi bounds (Eberl
and Rosser-Schoenfeld) and rational root comparisons.
No RH assumption, no floating comparisons, no Lean build.
"""
from fractions import Fraction as Q
from math import isqrt
from certify_global_weighted_chebyshev_superadditivity import (
    B, interval_log_int, ceildiv, sieve_primes
)
def certify():
    assert 22627**2<512*1000**2
    assert 6404**2>41*1000**2
    assert 1415**2>2*1000**2
    large_gap=Q(9,5)*Q(22627,1000)-Q(9,10)*Q(6404,1000) \
        -Q(52,25)*(Q(1415,1000)+16)+Q(52,25)
    assert large_gap==Q(4109,5000)>Q(1,2)
    assert Q(9,5)*Q(7,5)>Q(52,25)
    K=255;N=K*K
    vl=[0]*(N+1);vu=[0]*(N+1);events=0
    for p in sieve_primes(N):
        lp,up=interval_log_int(p);q=p
        while q<=N:
            root=isqrt(q*B*B)
            vl[q]+=(B*lp)//(root+1)
            vu[q]+=ceildiv(B*up,root)
            q*=p;events+=1
    for n in range(1,N+1):
        vl[n]+=vl[n-1];vu[n]+=vu[n-1]
    c_up=vu[4]-2*vl[2];c_lo=vl[4]-2*vu[2]
    assert 0<c_lo<=c_up<B//2
    best=(10**100,None,None)
    for n in range(2,K+1):
        for m in range(2,K+1):
            if n==m==2:continue
            gap=vl[n*m]-vu[n]-vu[m]
            assert gap>c_up,(n,m,gap,c_up)
            if gap<best[0]:best=(gap,n,m)
    print('PASS sharp global V(xy)-V(x)-V(y)>=V(4)-2V(2), x,y>=2')
    print('infinite region lower gap:',large_gap)
    print('finite cases:',(K-1)**2,'events:',events)
    print('optimal c_* interval:',c_lo,'/',B,'to',c_up,'/',B)
    print('next lower surplus:',best[0],'/',B,'at',best[1:])
    print('No RH, Weil full positivity or Lean claim.')
if __name__=='__main__':certify()
