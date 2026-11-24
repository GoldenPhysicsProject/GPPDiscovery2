"""Exact integer check of the small-prime charge sectors at both fixed angles."""
from math import isqrt
from collections import defaultdict
from fractions import Fraction
from check import prime_factors


def data(limit, half):
    cells = defaultdict(list)
    direct = 0
    for n in range(1, limit+1):
        factors = prime_factors(n)
        if any(k>1 for _,k in factors):
            continue
        base = next((p for p,_ in factors if p>isqrt(limit)),1)
        sign = (-1)**len(factors)
        phase = (-1)**n if half else 1
        local_sign = sign if base==1 else -sign
        cells[base].append(local_sign*phase)
        direct += sign*phase
    small = sum(cells[1])
    large = sum(sum(v) for p,v in cells.items() if p!=1)
    residual_sq = sum(Fraction(sum(v)**2,len(v)) for v in cells.values())
    singles = sum(1 for p in cells if p>limit/2 and p>1)
    assert direct == small-large and residual_sq >= singles
    return small, large, direct, singles


if __name__ == '__main__':
    for limit in (100,1000,10000):
        for half in (False,True):
            print(limit, 'half' if half else 'zero', *data(limit,half))
