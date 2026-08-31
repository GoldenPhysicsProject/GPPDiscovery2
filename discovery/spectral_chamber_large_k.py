#!/usr/bin/env python3
"""Executable audit for chamber unimodality and the fixed-x large-k tail."""

import math


def adjacent_ratio(k: int, x: float) -> float:
    return 2.0 * ((k + 1.0) ** 2 + x * x) / ((k + 1.0) * (2.0 * k + 3.0))


def rho(k: int, x: float) -> float:
    base = 1.0 / math.pi if x == 0.0 else x / math.sinh(math.pi * x)
    product = 1.0
    for j in range(1, k + 1):
        product *= j * j + x * x
    return (2.0 ** (2 * k + 1) / math.factorial(2 * k + 1)) * base * product


def predicted_maximizers(x: float):
    y = 2.0 * x * x
    nearest = round(y)
    if abs(y - nearest) < 1e-12 and nearest >= 1:
        return (nearest - 1, nearest)
    return (math.floor(y),)


def audit_unimodality(x: float, kmax: int = 40):
    values = [rho(k, x) for k in range(kmax + 1)]
    vmax = max(values)
    observed = tuple(k for k, v in enumerate(values) if abs(v - vmax) <= 1e-12 * max(1.0, abs(vmax)))
    predicted = predicted_maximizers(x)
    if observed != predicted:
        raise AssertionError((x, observed, predicted))
    for k in range(kmax):
        lhs = adjacent_ratio(k, x) - 1.0
        rhs = (2.0 * x * x - (k + 1.0)) / ((k + 1.0) * (2.0 * k + 3.0))
        if abs(lhs - rhs) > 1e-13:
            raise AssertionError((k, x, lhs, rhs))


def audit_large_k():
    xs = (0.0, 0.3, 1.0, 3.0)
    ks = (20, 100, 500)
    for x in xs:
        row = []
        for k in ks:
            scaled = rho(k, x) * math.sqrt(math.pi * k)
            row.append((k, scaled))
        print(f"x={x}: " + ", ".join(f"k={k}: {v:.12f}" for k, v in row))


if __name__ == "__main__":
    for x in (0.0, 0.3, 1.0, math.sqrt(1.5), 3.0):
        audit_unimodality(x)
    audit_large_k()
    print("all chamber checks passed")
