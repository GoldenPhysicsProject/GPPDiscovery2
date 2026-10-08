#!/usr/bin/env python3
"""Exact finite Fejer Gram stress-test for the pole-subtracted dyadic prime current.

This is an experiment, not an RH proof. No zeros, no extrapolated conclusion.
Usage: python research/codex/scripts/dyadic_pole_gram_probe_2026_10_08.py
Requires numpy. x values up to 50000 by default. Changing x costs O(pi(2x)^2).
"""
from math import ceil, cosh, exp, log, sinh, sqrt
import numpy as np

ELL = log(2.0)
A = 2.0 * (cosh(ELL / 2.0) - 1.0) / (ELL / 4.0)
# Correct expression for H_ell(1/2): 2(cosh(ell/2)-1)/(ell/4)
# equals 8(cosh(ell/2)-1)/ell.
A = 8.0 * (cosh(ELL / 2.0) - 1.0) / ELL
C = 8.0 * cosh(ELL) - 16.0 / ELL * (sinh(ELL) - sinh(ELL / 2.0))


def von_mangoldt_up_to(limit):
    values = np.zeros(limit + 1, dtype=float)
    composite = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        for j in range(p + p, limit + 1, p):
            composite[j] = 1
        power = p
        while power <= limit:
            values[power] = log(p)
            power *= p
    return values


def kernel_continuum(v):
    """Integral_-ell^ell e^(w/2) h_ell(v-w) dw, exact antiderivatives."""
    left = max(-ELL, v - ELL)
    right = min(ELL, v + ELL)
    f1 = lambda w: 2 * exp(w / 2) * (1 - v / ELL + (w - 2) / ELL)
    f2 = lambda w: 2 * exp(w / 2) * (1 + v / ELL - (w - 2) / ELL)
    return f1(v) - f1(left) + f2(right) - f2(v)


def check(x, lam):
    n = np.arange(ceil(x / 2), 2 * x + 1)
    n = n[lam[n] > 0]
    coeff = lam[n] / np.sqrt(n)
    position = np.log(n / x)
    tent = np.maximum(1 - np.abs(position) / ELL, 0)
    linear = float(np.dot(coeff, tent))
    deficit = A * sqrt(x) - linear
    pp = 0.0
    for start in range(0, len(n), 512):
        row = slice(start, start + 512)
        weights = np.maximum(
            1.0 - np.abs(position[row, None] - position[None, :]) / ELL,
            0.0,
        )
        pp += float(np.sum(coeff[row, None] * coeff[None, :] * weights))
    pc = sqrt(x) * float(np.dot(coeff, [kernel_continuum(float(v)) for v in position]))
    energy = pp - 2 * pc + x * C
    if energy < -1e-8:
        raise ArithmeticError("Gram form unexpectedly negative; check implementation")
    return len(n), linear, deficit, energy


def main():
    print("h_ell(0)=1; exact continuum A=", A, "C=", C)
    x_grid = (50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000)
    lam = von_mangoldt_up_to(2 * max(x_grid))
    print("x, prime_powers, S(x), pole_deficit, gram_energy, ratio_sqrtE_to_absDeficit")
    for x in x_grid:
        count, s, deficit, energy = check(x, lam)
        print(x, count, "%.9f" % s, "%+.9f" % deficit,
              "%.9f" % energy,
              "%.6f" % (sqrt(max(energy, 0.0)) / max(abs(deficit), 1e-12)))
        assert deficit * deficit <= energy + 1e-7, "Cauchy/Gram violation"


if __name__ == "__main__":
    main()
