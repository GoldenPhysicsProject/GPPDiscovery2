"""Exact Gaussian-rational test of BC KMS midpoint prime-gradient source identity.

The algebraic proof for ALL n and x is given in
discovery/bc_kms_prime_gradient_all_scale.md. Test with true prime
powers n=4,9,16,25 so n^-1/2 is rational, after factoring out positive
symbolic Lambda(n)=log p. No floating arithmetic anywhere.
"""
from fractions import Fraction as F

def nsq(z):
    return z[0]*z[0]+z[1]*z[1]

def sub(z,t):
    return (z[0]-t[0],z[1]-t[1])

def rprod(z,t):
    return z[0]*t[0]+z[1]*t[1]

def gradient_one(n,u,v):
    # n is prime power with rational n^(-1/2); log(p) positive
    root = {4:2,9:3,16:4,25:5}[n]
    r=F(1,root)
    # KMS midpoint for B=(u-v) mu_n: r * ||u-v||²
    kms=r*nsq(sub(u,v))
    contact=r*(nsq(u)+nsq(v))
    prime_source=-2*r*rprod(u,v)
    assert kms>=0 and kms-contact==prime_source
    return kms,contact,prime_source

def check_all_complex_amplitudes():
    vals=[(F(0),F(0)),(F(1),F(0)),(F(-1),F(0)),
          (F(1),F(1)),(F(2),F(-3)),(F(-4,3),F(7,5))]
    for n in (4,9,16,25):
        for u in vals:
            for v in vals:
                gradient_one(n,u,v)
    print('Exact KMS prime-gradient and full mandatory contact PASS for n=4,9,16,25')


def check_relative_phase():
    u=(F(1),F(0))
    vp=(F(1),F(0))
    vm=(F(-1),F(0))
    for n in (4,9,16,25):
        k_plus,c_plus,s_plus=gradient_one(n,u,vp)
        k_minus,c_minus,s_minus=gradient_one(n,u,vm)
        assert k_plus==0 and k_minus>0
        assert c_plus==c_minus
        assert s_plus<0<s_minus
        # Relative phase is now in the positive gradient, and
        # contact is the same fixed diagonal term.
        print(f'n={n}: KMS edge (same/opposite)={k_plus}/{k_minus}, '
              f'contact={c_plus}, true source={s_plus}/{s_minus}')


def check_finite_cutoff():
    # Discrete log-line surrogate: integer shift labels, exact arithmetic.
    # Every n contributes normalized rational 'r' times gradient and contact.
    f=[(F(1),F(2)),(F(-1),F(0)),(F(3),F(-2)),(F(0),F(1))]
    fnorm=sum(nsq(z) for z in f)
    shiftmap={4:1,9:2,16:3,25:9}
    ktotal=F(0)
    ctotal=F(0)
    stotal=F(0)
    for n,a in shiftmap.items():
        r=F(1,{4:2,9:3,16:4,25:5}[n])
        # All n contribution after separating out symbolic Lambda(n).
        # n=25 jump is longer than support and has source 0.
        ks=2*r*fnorm
        cs=2*r*fnorm
        for i in range(len(f)-a):
            ks-=2*r*rprod(f[i],f[i+a])
        src=-2*r*sum((rprod(f[i],f[i+a]) for i in range(max(len(f)-a,0))),F(0))
        assert ks>=0 and ks-cs==src
        ktotal+=ks
        ctotal+=cs
        stotal+=src
    assert ktotal-ctotal==stotal
    print('Exact multi-grade finite-cutoff renormalization identities PASS')


if __name__=='__main__':
    check_all_complex_amplitudes()
    check_relative_phase()
    check_finite_cutoff()
    print('Positive BC KMS midpoint energies reproduce prime gradient, '
          'NOT the final Weil sign absent divergent counterterm. RH OPEN.')
