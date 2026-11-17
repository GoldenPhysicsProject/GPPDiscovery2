"""Exact rational subcertificate for the first-prime negative-index upper bound.

The transcendental inequalities and Hilbert–Schmidt trace argument must be
proved independently (preferably in Lean). This script certifies only
finite rational inequalities using arbitrary-precision integer arithmetic.
"""
from fractions import Fraction as F

R = 180
L = F(18, 25)
rank = 650

A = sum((
    F(16*R*R, (4*k+1)*((4*k+1)**2+4*R*R))
    for k in range(400)
), F(0))
assert A > F(87, 10)

sinh_series_upper = F(9,25) + F(9,25)**3/(6*(1-F(9,25)**2))
assert sinh_series_upper == F(2007,5440)
assert sinh_series_upper < F(3,8)

M_upper = (
    F(2,3)+F(6,5)+F(8,5)+F(21,10)+F(3,2)+F(1)
)
assert M_upper == F(121,15) < F(81,10)

assert L*R == F(648,5)
coefficient = 1 - L*R/(F(3)*(rank+1))
assert coefficient == F(1013,1085)

margin = F(87,10)*coefficient-F(81,10)
assert margin == F(123,5425) > 0

print("PASS: exact rational subcertificate")
print("400-term lower sum exceeds 87/10 by", float(A-F(87,10)))
print("Majorant M bound:", M_upper, "< 81/10")
print("Rank:", rank, "strict rational margin:", margin)
print("Separate analytic obligations: transcendental inequalities, "
      "Fourier tail and Hilbert–Schmidt trace min–max argument.")
