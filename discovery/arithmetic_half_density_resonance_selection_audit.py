#!/usr/bin/env python3
"""Critical half-density resonance audit for exceptional arithmetic channels.

This script isolates an elementary exponent-matching fact behind the paired
primitive/repetition boundary sectors.  It makes no RH, positivity, or
convergence claim.

For the n-th smooth Mobius correction to prime counting, critical half-density
weighting produces the continuum power

    e_n = 1/n - 3/2.

For the m-th prime-repetition channel, the corresponding continuum power is

    r_m = -m/2.

Matching e_n = r_m gives n(3-m)=2.  The only positive-integer solutions are
(n,m)=(1,1) and (2,2).  Thus the n=2 / m=2 logarithmic boundary pairing is the
unique nontrivial secondary resonance; all n>=3 smooth Mobius corrections have
power strictly below -1 and are integrable at infinity at this continuum level.
"""

from fractions import Fraction


def mobius_half_density_exponent(n: int) -> Fraction:
    assert n >= 1
    return Fraction(1, n) - Fraction(3, 2)


def repetition_exponent(m: int) -> Fraction:
    assert m >= 1
    return -Fraction(m, 2)


def matched_m(n: int) -> Fraction:
    assert n >= 1
    return Fraction(3, 1) - Fraction(2, n)


# Exhaustive finite audit far beyond the only possible divisors of 2.
solutions = [
    (n, m)
    for n in range(1, 1001)
    for m in range(1, 10)
    if mobius_half_density_exponent(n) == repetition_exponent(m)
]
assert solutions == [(1, 1), (2, 2)]

# Algebraically, integer matching requires n | 2 because m = 3 - 2/n.
assert matched_m(1) == 1
assert matched_m(2) == 2
for n in range(3, 1001):
    assert matched_m(n).denominator != 1

# n=2 is the unique secondary logarithmic case; n>=3 is integrable at infinity.
assert mobius_half_density_exponent(2) == -1
for n in range(3, 1001):
    assert mobius_half_density_exponent(n) < -1

print("critical half-density exponent matching")
for n in range(1, 7):
    print(
        f"n={n:2d}: e_n={mobius_half_density_exponent(n)!s:>6}, "
        f"matched m={matched_m(n)}"
    )
print("positive-integer resonances:", solutions)
print("verified: n=2/m=2 is the unique nontrivial secondary resonance")
print("verified: every n>=3 smooth Mobius correction has exponent < -1")
