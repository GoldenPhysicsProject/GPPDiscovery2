#!/usr/bin/env python3
"""Jensen/Hardy no-ghost census toy checks, not a proof about zeta zeros."""
import math
import cmath
import numpy as np

a = complex(0.6, 0.2)
moda = abs(a)
theta = 2 * math.pi * (np.arange(65536) + 0.5) / 65536
for r in (0.3, 0.5, 0.8, 1.0):
    w = r * np.exp(1j * theta)
    F = (1 - w / a) * (1 - w / a.conjugate())
    circle_mean = float(np.log(np.abs(F)).mean())
    expected = 0 if r <= moda else 2 * math.log(r / moda)
    err = abs(circle_mean - expected)
    print(f'r={r:.1f}, integral={circle_mean:.17f}, Jensen={expected:.17f}, error={err:.2e}')
    assert err < 3e-12
G = -2 * math.log(moda)
D = 1 - moda ** 4
assert abs(D - (1 - math.exp(-2 * G))) < 1e-15
print('Hardy ghost defect=', D, 'boundary defect=', 1 - math.exp(-2 * G))

for sigma in (0.25, 0.5, 0.75):
    alpha = 2 * sigma - 1
    logR = 20.
    norm = math.sinh(alpha * logR) / (alpha * logR) if alpha else 1.
    print(f'Re s={sigma}: symmetric Haar Cesaro norm at logR=20 is {norm:.12g}')
    if alpha: assert norm > 100
print('PASS: double-zero Jensen-Hardy relation and symmetric off-line Cesaro divergence.')
