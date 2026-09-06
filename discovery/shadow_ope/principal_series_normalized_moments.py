#!/usr/bin/env python3
"""Exact audit of the normalized principal-series digamma moments.

Inputs are the analytically proved raw moments from principal_series_blocks_v2.tex:
    A0 = 1/4, A1 = 1/8, A2 = 1/8.
This script deliberately does not re-prove the integral evaluations.  It verifies,
with exact rational arithmetic, the normalization consequences used by the Lean
formalization in GPPVerify2.
"""

from fractions import Fraction

A0 = Fraction(1, 4)
A1 = Fraction(1, 8)
A2 = Fraction(1, 8)

mean = A1 / A0
second_raw = A2 / A0
variance = second_raw - mean * mean

assert mean == Fraction(1, 2)
assert second_raw == Fraction(1, 2)
assert variance == Fraction(1, 4)
assert variance > 0
assert variance == mean * mean

print(f"A0={A0}, A1={A1}, A2={A2}")
print(f"normalized mean={mean}")
print(f"normalized second raw moment={second_raw}")
print(f"normalized variance={variance}")
print("stddev^2 = mean^2 exactly; the normalized observable is nondegenerate")
