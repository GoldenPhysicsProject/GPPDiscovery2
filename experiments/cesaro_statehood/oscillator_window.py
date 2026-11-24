"""Numerical checks only; the window identities have analytic proofs."""
from math import exp, log, log1p, pi, fsum
from check import mu, prime_factors

even = (1, -4.5, 7, -4.5, 1)
half = (-1, 2.5, 0, -2.5, 1)


def stencil(fn, x, weights=even):
    return fsum(a*fn(x*2**j) for j,a in zip(range(-2,3),weights))


def ell(x):
    return log1p(-exp(-x))


def oscillator(x):
    return fsum(ell(m*x) for m in range(1,int(60/x)+2))


def check(t):
    nmax = int(200/t)
    direct, twisted, tilted, prime = [], [], [], []
    for n in range(1,nmax+1):
        w = stencil(oscillator,n*t)
        term = mu(n)*w
        direct.append(term)
        twisted.append((-1)**n*term)
        tilted.append(log(n*t/(2*pi))*term)
        factors = prime_factors(n)
        if len(factors)==1:
            prime.append(log(factors[0][0])*stencil(ell,n*t))
    b = stencil(ell,t)
    errors = (fsum(direct)-b, fsum(twisted)-stencil(ell,t,half),
              fsum(tilted)-(log(t/(2*pi))*b-fsum(prime)),
              stencil(oscillator,t)-stencil(oscillator,4*pi*pi/t))
    print(t, max(map(abs,errors)))
    assert max(map(abs,errors)) < 1e-9


if __name__=='__main__':
    for t in (0.25,0.7,2.0):
        check(t)
