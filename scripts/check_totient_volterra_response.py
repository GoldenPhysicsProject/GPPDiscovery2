"""Arithmetic scattering response: exact-kernel checks and finite experiments.

No zero ordinates are inputs. Numerical checks are not an RH proof.
Requires mpmath. Run with Python 3; optional --dps and --limit.
"""
import argparse
import json
import mpmath as mp


def kernel(y):
    """Continuous once-smoothed kernel on [0,1], zero outside."""
    if y >= 1:
        return mp.mpf(0)
    return 4*y*mp.acos(y)-2*mp.sqrt(1-y*y)


def totients(limit):
    phi = list(range(limit+1))
    for p in range(2, limit+1):
        if phi[p] == p:
            for n in range(p, limit+1, p):
                phi[n] -= phi[n]//p
    return phi


def mobius(limit):
    mu = [1]*(limit+1)
    prime = [True]*(limit+1)
    for p in range(2, limit+1):
        if prime[p]:
            for n in range(p, limit+1, p):
                prime[n] = False
                mu[n] *= -1
            for n in range(p*p, limit+1, p*p):
                mu[n] = 0
    return mu


def run(dps=60, limit=1000):
    mp.mp.dps = dps
    phi, mu = totients(limit), mobius(limit)
    errors = {}
    # y=cos(theta) removes the integrable endpoint singularity.
    def cosine_transform(w):
        return mp.quad(lambda th: kernel(mp.cos(th))*mp.cos(w*mp.cos(th))*mp.sin(th), [0, mp.pi/2])
    errors['zero_continuum_moment'] = abs(cosine_transform(0))
    for w in [mp.mpf('0.4'), mp.mpf('2.3'), mp.mpf('7')]:
        closed = mp.pi*mp.besselj(1,w)/w+2*mp.pi*(mp.besselj(0,w)-1)/w**2
        errors['cosine_transform_'+str(w)] = abs(cosine_transform(w)-closed)
    for s in [mp.mpf('0.8'), mp.mpf('1.7'), mp.mpc('1.1','0.4')]:
        integral = mp.quad(lambda y: 2*y**(2*s-1)*kernel(y), [0,mp.mpf('.5'),1])
        closed = mp.sqrt(mp.pi)*mp.gamma(s)/mp.gamma(s+mp.mpf('.5'))*(s-mp.mpf('.5'))/(s+mp.mpf('.5'))**2
        errors['laplace_kernel_'+str(s)] = abs(integral-closed)
    for v in [mp.mpf('.2'),mp.mpf('1.3'),mp.mpf('4')]:
        # u=r^2 regularizes the raw response at u=0.
        def integrand(r):
            if not r:
                return 2*mp.exp(-v/2)
            u=r*r
            raw=(2*mp.exp(-u)-1)/mp.sqrt(-mp.expm1(-u))
            return 2*r*mp.exp(-(v-u)/2)*raw
        errors['volterra_'+str(v)] = abs(mp.quad(integrand,[0,mp.sqrt(v)])-kernel(mp.exp(-v/2)))
    rows=[]
    for base in [2,5,10,30,100,300,limit-1]:
        x=mp.mpf(base)+mp.mpf('.37')
        nmax=int(mp.floor(x))
        if nmax>limit:
            continue
        terms=[mp.mpf(phi[n])/n*kernel(mp.mpf(n)/x) for n in range(1,nmax+1)]
        value=mp.fsum(terms)
        # Independent exact divisor regrouping, checked on small windows.
        if base <= 30:
            regrouped=mp.fsum(mp.mpf(mu[d])/d*mp.fsum(kernel(mp.mpf(d*k)/x) for k in range(1,nmax//d+1)) for d in range(1,nmax+1))
            errors['mobius_regroup_'+str(base)]=abs(value-regrouped)
        rows.append({'x':str(x),'response':mp.nstr(value,30),
                     'sqrt_x_times_response':mp.nstr(mp.sqrt(x)*value,20),
                     'sum_absolute_terms':mp.nstr(mp.fsum(abs(a) for a in terms),20)})
    worst=max(errors.values())
    assert worst < mp.mpf(10)**(-min(35,dps//2)), errors
    return {'dps':dps,'limit':limit,'max_identity_error':mp.nstr(worst,8),
            'identity_errors':{k:mp.nstr(v,8) for k,v in errors.items()},
            'samples':rows,'status':'finite numerical checks only; no uniform decay bound'}


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--dps',type=int,default=60)
    parser.add_argument('--limit',type=int,default=1000)
    args=parser.parse_args()
    print(json.dumps(run(args.dps,args.limit),indent=2))
