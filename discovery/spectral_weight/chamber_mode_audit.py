#!/usr/bin/env python3
"""Audit the exact modal-chamber law implied by the Gamma chamber recurrence.

For rho_{k+1}/rho_k = 2((k+1)^2+x^2)/((k+1)(2k+3)), positivity gives
rho_{k+1}>rho_k iff k+1<2x^2, equality iff k+1=2x^2, and decrease
iff k+1>2x^2. Hence the chamber sequence is unimodal for every fixed x.
"""
from fractions import Fraction
import math


def step_factor(k: int, x2: Fraction) -> Fraction:
    kp1 = Fraction(k + 1, 1)
    return 2 * (kp1 * kp1 + x2) / (kp1 * (2 * k + 3))


def relative_rhos(max_k: int, x2: Fraction):
    vals = [Fraction(1, 1)]
    for k in range(max_k):
        vals.append(vals[-1] * step_factor(k, x2))
    return vals


def predicted_modes(x2: Fraction):
    y = 2 * x2
    if y == 0:
        return {0}
    if y.denominator == 1:
        m = y.numerator
        return {m - 1, m}
    return {math.floor(y)}


def observed_modes(max_k: int, x2: Fraction):
    vals = relative_rhos(max_k, x2)
    vmax = max(vals)
    return {k for k, v in enumerate(vals) if v == vmax}


if __name__ == "__main__":
    tests = [
        Fraction(0, 1),       # x^2=0: maximum k=0
        Fraction(1, 8),       # 2x^2=1/4 -> k=0
        Fraction(3, 4),       # 2x^2=3/2 -> k=1
        Fraction(1, 1),       # 2x^2=2 -> tie k=1,2
        Fraction(13, 8),      # 2x^2=13/4 -> k=3
        Fraction(9, 2),       # 2x^2=9 -> tie k=8,9
    ]
    for x2 in tests:
        pred = predicted_modes(x2)
        obs = observed_modes(20, x2)
        print(f"x^2={x2}: predicted={sorted(pred)} observed={sorted(obs)}")
        assert pred == obs

    # Exact sign audit for a broad rational grid.
    for num in range(0, 31):
        x2 = Fraction(num, 7)
        y = 2 * x2
        for k in range(0, 20):
            r = step_factor(k, x2)
            lhs = Fraction(k + 1, 1)
            assert (r > 1) == (lhs < y)
            assert (r == 1) == (lhs == y)
            assert (r < 1) == (lhs > y)

    print("all exact rational mode/sign checks passed")
