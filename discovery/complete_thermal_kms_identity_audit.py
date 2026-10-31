"""High-precision independent audit of the entire completed Weil thermal/KMS identity.

Uses four nonsmooth but finite logarithmic-kinetic tests f=1_[0,L].
The underlying algebraic identity is proven in complete_thermal_kms_global_identity.md;
this program only verifies its normalization and all contact/pole terms.

NOTE this is not a positive-semidefinite certificate or RH proof.
"""
import math
import mpmath as mp

mp.mp.dps=60


def prime_power_terms(N):
    out=[]
    for p in range(2,N+1):
        if any(p%d==0 for d in range(2,math.isqrt(p)+1)):
            continue
        power=p
        while power<=N:
            out.append((power,p))
            power*=p
    return sorted(out)


def check(Ltxt, X=128):
    L=mp.mpf(Ltxt)
    r=lambda y:(mp.exp(y/2)-1)/(2*mp.sinh(y))
    w=lambda y:mp.exp(y/2)/(2*mp.sinh(y))
    E=mp.quad(lambda y: min(y,L)/mp.sinh(y),[0,L,mp.inf])
    A=mp.quad(lambda y:2*(L-y)*r(y),[0,L])
    G=mp.quad(lambda y:2*min(y,L)*w(y),[0,L,mp.inf])
    R=mp.pi/4+mp.log(2)/2
    Rdirect=mp.quad(r,[0,mp.inf])
    assert abs(R-Rdirect)<mp.mpf('1e-52')
    assert abs(E-A-G+2*R*L)<mp.mpf('1e-52')

    c=mp.log(4*mp.pi)+mp.euler
    kappa=mp.log(8*mp.pi)+mp.euler+mp.pi/2
    assert abs(kappa-c-2*R)<mp.mpf('1e-56')
    pole=8*(mp.exp(L/2)-1)*(1-mp.exp(-L/2))
    S=mp.mpf('0')
    K=mp.mpf('0')
    Psi=mp.mpf('0')
    atoms=[]
    for n,p in prime_power_terms(X):
        aa=mp.log(n)
        weight=mp.log(p)/mp.sqrt(n)
        S-=weight*2*max(L-aa,mp.mpf('0'))
        K+=weight*2*min(L,aa)
        Psi+=weight
        if aa<L:
            atoms.append(n)
    assert abs(K-2*Psi*L-S)<mp.mpf('1e-52')
    direct=E-A+pole-c*L+S
    combined=G+pole-kappa*L+(K-2*Psi*L)
    assert abs(direct-combined)<mp.mpf('1e-51')
    print('L=',Ltxt,' active prime-power atoms=',atoms)
    print('  original completed Q=',mp.nstr(direct,32))
    print('  gamma thermal+BC KMS completed Q=',mp.nstr(combined,32))
    print('  residual=',mp.nstr(direct-combined,5))
    print('  KMS energy positive=',mp.nstr(K,12),
          ' divergent contact at X=',mp.nstr(2*Psi*L,12))


def main():
    for L in ('0.4','0.75','1.2','1.7'):
        check(L)
    print('All-scale completed thermal/KMS equality verified numerically '
          'against original v34 source, including all genuine poles/contact.'
          ' No RH proof.')


if __name__=='__main__':
    main()
