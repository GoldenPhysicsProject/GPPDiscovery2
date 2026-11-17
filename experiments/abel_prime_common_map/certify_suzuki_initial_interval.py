"""Outward-rational proof that full Suzuki potential Psi(t)>0 for 0<t<log2.

The interval has no prime kicks. One exact q=3/2 checkpoint and monotonic
gamma curvature suffice. This does NOT prove RH or all prime intervals.
"""
from fractions import Fraction as Q
from math import isqrt
from certify_suzuki_event_parabola import constants,lo,hi,B,ceildiv
from certify_global_weighted_chebyshev_superadditivity import interval_log_ratio

def run():
    ci_lo,ci_hi,C_lo,C_hi=constants()
    # q=3/2: t0=log(3/2), no primes visible on [0,log2].
    q=Q(3,2)
    lq_lo,lq_hi=interval_log_ratio(3,2)
    root_lo=isqrt((3*B*B)//2);root_hi=root_lo+1
    inv_lo=(B*B)//root_hi;inv_hi=ceildiv(B*B,root_lo)
    K=60
    r=Q(4,9)
    S1=sum((r**k/Q(4*k+1) for k in range(K)),Q(0))
    S2=sum((r**k/Q((4*k+1)**2) for k in range(K)),Q(0))
    T1=r**K/(Q(4*K+1)*(1-r))
    T2=r**K/(Q((4*K+1)**2)*(1-r))
    l1_lo,l1_hi=lo(S1),hi(S1+T1)
    l2_lo,l2_hi=lo(S2),hi(S2+T2)
    # F(t)=4(sqrt(q)+1/sqrt(q)-2)+Cinf*t/2+C/4
    #       -4/sqrt(q)*sum_{k>=0}q^(-2k)/(4k+1)^2.
    f_lo=(4*(root_lo+inv_lo-2*B)
          +(ci_lo*lq_hi)//(2*B)+C_lo//4
          -ceildiv(4*inv_hi*l2_hi,B))
    f_hi=(4*(root_hi+inv_hi-2*B)
          +ceildiv(ci_hi*lq_lo,2*B)+ceildiv(C_hi,4)
          -(4*inv_lo*l2_lo)//B)
    d_lo=2*(root_lo-inv_hi)+ci_lo//2+(2*inv_lo*l1_lo)//B
    d_hi=2*(root_hi-inv_lo)+ceildiv(ci_hi,2)+ceildiv(2*inv_hi*l1_hi,B)
    # F''(log q)=sqrt(q)*(1-1/[q(q²-1)]).
    kcoeff=1-Q(1,1)/(q*(q*q-1))
    k_lo=root_lo*kcoeff.numerator//kcoeff.denominator
    k_hi=ceildiv(root_hi*kcoeff.numerator,kcoeff.denominator)
    assert 0<f_lo<=f_hi
    assert d_lo<=d_hi<0
    assert 0<k_lo<=k_hi
    # F(t0)-[F'(t0)]^2/(2F''(t0)) > 0, all exact integers.
    cert=2*k_lo*f_lo-d_lo*d_lo
    assert cert>0
    print('CERTIFIED prime-free Suzuki interval, t0=log(3/2)')
    print('t0:',lq_lo,'to',lq_hi,'/',B)
    print('F(t0):',f_lo,'to',f_hi,'/',B)
    print("F'(t0):",d_lo,'to',d_hi,'/',B)
    print("F''(t0):",k_lo,'to',k_hi,'/',B)
    print('2 F Fpp-Fp^2 certified lower:',cert,'/',B**2)
    print('F(0)=0, Fp(0+)=+infinity, Fpp increases and crosses zero once.')
    print('Fp(t0)<0 => minimum on [0,t0] at an endpoint, both nonnegative.')
    print('Fpp>=Fpp(t0)>0 to log2 => a strictly positive quadratic lower bound.')
    print('Thus Psi_zeta(t)=F(t)>0 for all 0<t<log2; no RH claim.')

if __name__=='__main__':run()
