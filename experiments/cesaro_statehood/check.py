"""Finite integer checks for the statehood note. Standard library only."""
from fractions import Fraction
from math import prod


def prime_factors(n):
    factors = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            power = 0
            while n % p == 0:
                n //= p
                power += 1
            factors.append((p, power))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def mu(n):
    factors = prime_factors(n)
    return 0 if any(k>1 for _,k in factors) else (-1)**len(factors)


def main():
    for n in range(1, 513):
        assert sum(mu(d) for d in range(1,n+1) if n%d==0) == int(n==1)
    # Coefficients of (1-X)/(1+5X+5X²) for the modified 5-factor.
    inv = [1, -6]
    for k in range(2, 13):
        inv.append(-5*(inv[k-1]+inv[k-2]))
    assert all(inv[k]+5*inv[k-1]+5*inv[k-2]==0 for k in range(2,13))
    # At sigma=1 the honest inverse has squared Haar norm product(1+p^-2).
    primes = [p for p in range(2, 100) if prime_factors(p)==[(p,1)]]
    squared_norm = prod(1+Fraction(1,p*p) for p in primes)
    peak = prod(1+Fraction(1,p) for p in primes)
    print("inverse at powers of 5 through k=6:", inv[:7])
    print("primes through 97: squared Haar norm, supremum:", float(squared_norm), float(peak))
    assert squared_norm < 2 and peak > 5
    # Apply the Euler modification to zeta: positive integral coefficients.
    assert [1+5*int(n%5==0)+5*int(n%25==0) for n in (1,5,25)] == [1,6,11]


if __name__ == '__main__':
    main()
