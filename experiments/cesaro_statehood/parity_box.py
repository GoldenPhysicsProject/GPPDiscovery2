"""Check the dyadic hyperbola identity against a direct integer sieve."""
from itertools import accumulate
from math import isqrt


def mobius(n):
    mu = [0]+[1]*n
    prime = bytearray([1])*(n+1)
    for p in range(2,n+1):
        if prime[p]:
            prime[2*p::p] = bytes(n//p-1)
            for j in range(p,n+1,p):
                mu[j] *= -1
            for j in range(p*p,n+1,p*p):
                mu[j] = 0
    return mu


def check(n, mu, partial):
    u = isqrt(n)
    q = sum(mu[d]*mu[e]*((n//(d*e)) % 2)
            for d in range(1,u+1) for e in range(1,u+1))
    diff = partial[n]-2*partial[n//2]
    assert q == -2*partial[u]-diff
    return u,q,diff


if __name__ == '__main__':
    mu = mobius(1_000_000)
    partial = list(accumulate(mu))
    for n in range(4,1001):
        check(n,mu,partial)
    for n in (10_000,100_000,1_000_000):
        print(n,*check(n,mu,partial))


def check_prime_phase_average(n):
    from itertools import product
    u = isqrt(n)
    mu = mobius(u)
    primes = [p for p in range(2,u+1) if all(p%k for k in range(2,isqrt(p)+1))]
    masks = [sum(1<<j for j,p in enumerate(primes) if d%p==0) for d in range(u+1)]
    classes = [0]*(1<<len(primes))
    for d in range(1,u+1):
        for e in range(1,u+1):
            classes[masks[d]^masks[e]] += mu[d]*mu[e]*((n//(d*e))%2)
    total = 0
    for twist in range(len(classes)):
        weights = [m*(-1)**((mask&twist).bit_count()) for m,mask in zip(mu,masks)]
        q = sum(weights[d]*weights[e]*((n//(d*e))%2)
                for d,e in product(range(1,u+1),repeat=2))
        total += q*q
    assert total == len(classes)*sum(v*v for v in classes)
    print('prime-sign mean square at', n, '=', sum(v*v for v in classes))


if __name__ == '__main__':
    check_prime_phase_average(225)
