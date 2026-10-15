#!/usr/bin/env python3
"""Exact rational L=1, T=300 S27 high-order tail checker.

Inputs still requiring independent Arb verification: M0<=22, beta>=0.8108,
finite block lambda0=4.14e-30, matrix norm error <=9e-33.
The tail bounds themselves use exact fractions, no floating point.
RH and GRH remain open.
"""
from fractions import Fraction as Q
from math import prod


def odd_double_factorial(d):
    return prod(range(1, 2 * d + 2, 2))


def tail(d):
    D = odd_double_factorial(d)
    visible_first = Q(2 * (2 * d + 1) * 300 ** (2 * d), D ** 2)
    visible_ratio = Q(300 ** 4, (2 * d + 1) * (2 * d + 3) ** 2 * (2 * d + 5))
    # exp(1/4) <= 4/3 supplies a rigorous upper bound on i_d(1/2)^2.
    pole_first = Q(8 * (2 * d + 1), 3) * Q(1, 2) ** (2 * d) / D ** 2
    pole_ratio = Q(1, 16 * (2 * d + 1) * (2 * d + 3) ** 2 * (2 * d + 5))
    assert visible_ratio < 1 and pole_ratio < 1
    return visible_first / (1 - visible_ratio), pole_first / (1 - pole_ratio)


def certify():
    for d in (524, 525):
        sd, sp = tail(d)
        assert sd < Q(1, 10 ** 117)
        assert sp < Q(1, 10 ** 3000)
        print(f"d={d}: exact checks S_D<1e-117, S_p<1e-3000 passed")
    for first in (0, 1):
        degs = range(first, first + 2 * 262, 2)
        sa = sum(2 * (2 * d + 1) for d in degs)
        assert sa < 300000
    assert Q(300000, 10 ** 117) < Q(4, 10 ** 112)
    # T/pi <=100, M0<=22, ||p_A||<3; epsilon_B<5e-53.
    b = Q(4400, 10 ** 56) + Q(6, 10 ** 1500)
    assert b < Q(5, 10 ** 53)
    # epsilon_D = (T/pi)*M0*S_D <2.2e-114.
    assert Q(2200, 10 ** 117) < Q(3, 10 ** 114)
    # even block lambda0 minus radius and tail > 4.13e-30.
    assert Q(414, 10 ** 32) - Q(9, 10 ** 33) - b > Q(413, 10 ** 32)
    print("Conditional on stated Arb inputs: even lower bound >4.13e-30.")


if __name__ == "__main__":
    certify()
