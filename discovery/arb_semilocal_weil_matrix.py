"""Arb enclosure of the actual semilocal Weil matrix in GPP v34 section 6351.

The exact one-sided distribution is Psi = W_{0,2} - W_R - sum W_p.
For q_mn(y) defined by the logarithmic Fourier basis, its matrix is
Q_mn = int_0^L q_mn(y)*(exp(y/2)+exp(-y/2)) dy
     - (log(4*pi)+Euler)/2*q_mn(0)
     - int_0^L [exp(y/2)*q_mn(y)-q_mn(0)]/(2*sinh(y))dy
     + q_mn(0)*atanh(exp(-L))
     - sum_{p^r <= exp(L)} log(p)*p^(-r/2)*q_mn(r*log(p)).

The removable singularity at zero in W_R is evaluated using the entire
functions _1F_1(1;2;z)=(exp(z)-1)/z and sinc(iz)=sinh(z)/z.

Results are finite-support matrix enclosures, not global Weil positivity.
"""

import argparse
from flint import arb, acb, ctx

ctx.prec = 160
I = acb(0, 1)


def qval(m, n, y, L):
    if m == n:
        return 2 * (1-y/L) * (2*arb.pi()*m*y/L).cos()
    return ((2*arb.pi()*m*y/L).sin() - (2*arb.pi()*n*y/L).sin()) / (arb.pi()*(n-m))


def qcomplex(m, n, z, L):
    if m == n:
        return 2 * (1-z/L) * (2*arb.pi()*m*z/L).cos()
    return ((2*arb.pi()*m*z/L).sin() - (2*arb.pi()*n*z/L).sin()) / (arb.pi()*(n-m))


def arch_integrand(m, n, z, L):
    ez = (z/2).exp()
    sinhc = (I*z).sinc()  # sin(i z)/(i z) = sinh(z)/z
    if m == n:
        w = 2*arb.pi()*m/L
        c = (w*z).cos()
        exprel = (z/2).hypgeom_1f1(1, 2)
        cosrel = -w*w*z/2*(w*z/2).sinc()**2
        return (exprel*c/2 + ez*cosrel - ez*c/L) / sinhc
    wm = 2*arb.pi()*m/L
    wn = 2*arb.pi()*n/L
    q_over_z = (wm*(wm*z).sinc()-wn*(wn*z).sinc()) / (arb.pi()*(n-m))
    return ez*q_over_z/(2*sinhc)


def prime_powers(bound):
    """Finite p^r list; `bound` is a mathematically exact integer cutoff."""
    primes = []
    for n in range(2,bound+1):
        if all(n % p for p in primes if p*p <= n):
            primes.append(n)
    powers = []
    for p in primes:
        k = p
        while k <= bound:
            powers.append((p,k))
            k *= p
    return sorted(powers,key=lambda x:x[1])


def real_integral(f, L):
    z = acb.integral(lambda x, analytical: f(x), acb(0), acb(L),
                     rel_tol=1e-25, abs_tol=1e-25,
                     eval_limit=100000)
    # Arb certifies complex integration. The physical integrand is real on
    # [0,L]; its real part is an enclosure of the desired real integral.
    return z.real


def entry(m,n,lam,bound):
    L = 2*lam.log()
    lcomplex = acb(L)
    pole = real_integral(lambda z:qcomplex(m,n,z,lcomplex)*((z/2).exp()+(-z/2).exp()),L)
    arch = real_integral(lambda z:arch_integrand(m,n,z,lcomplex),L)
    qzero = arb(2) if m==n else arb(0)
    arch += (arb(4).log()+arb.pi().log()+arb.const_euler())*qzero/2
    # IMPORTANT: F(u)=0 for u>exp(L), but the -F(1) subtraction in W_R
    # persists to infinity. In additive y, the tail is exactly
    #   -F(1) * integral_L^infinity 1/(2*sinh(y)) dy
    # = -F(1) * atanh(exp(-L)). Omitting this produces spurious negatives.
    arch -= qzero * (arb(1)/(lam*lam)).atanh()
    prime=arb(0)
    for p,k in prime_powers(bound):
        prime += arb(p).log()/arb(k).sqrt() * qval(m,n,arb(k).log(),L)
    return pole-arch-prime, (pole,arch,prime)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--n',type=int,default=0)
    ap.add_argument('--lambda-num',type=int,default=5)
    ap.add_argument('--lambda-den',type=int,default=2)
    ap.add_argument('--require-positive',action='store_true',
                    help='Fail if interval LDL cannot certify this finite test matrix PD')
    args=ap.parse_args()
    assert 0<=args.n<=3
    assert args.lambda_den>0
    lam=arb(args.lambda_num)/args.lambda_den
    assert lam > 1
    lam2_num=args.lambda_num**2
    lam2_den=args.lambda_den**2
    bound=lam2_num//lam2_den
    # Exact integer arithmetic includes every prime power at the endpoint.
    modes=list(range(-args.n,args.n+1))
    M=[]
    for m in modes:
        row=[]
        for n in modes:
            z,parts=entry(m,n,lam,bound)
            row.append(z)
            print(f"m={m:+d},n={n:+d},Q={z}; pole={parts[0]}, arch={parts[1]}, prime={parts[2]}")
        M.append(row)
    from arb_multiwindow_certificates import certify_positive_definite
    try:
        pivots=certify_positive_definite(M)
        print('CERTIFIED matrix positive definite via Arb LDL pivots:', pivots)
    except AssertionError as exc:
        print('LDL cannot certify positive definite:', exc)
        if args.require_positive:
            raise
    print('Scope: exact semilocal matrix formula at finite support and N, not RH')


if __name__=='__main__':
    main()
