#!/usr/bin/env python3
"""Independent high precision tests for exact p=2 activation logarithmic bounds.

The theorem is analytic in first_prime_log_activation_sharpness.md.
Tests use exact rectangle autocorrelation integration and outward finite
precision sanity checks; not a computer-assisted proof of RH.
"""
import mpmath as mp

mp.mp.dps = 65
a = mp.log(2)
w = a / mp.sqrt(2)

for eps in [mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('1e-4'),
            mp.mpf('1e-7')]:
    assert eps > 0 and 2 * eps < a
    H = mp.log(mp.coth(eps / 2))
    # Exact autocorrelation of two normalized disjoint rectangular strips.
    kinetic_local = mp.quad(lambda y: y / mp.sinh(y), [0, eps]) / eps
    kinetic_cross = mp.quad(
        lambda y: (1 - abs(y - a) / eps) / mp.sinh(y),
        [a - eps, a, a + eps]) / 2
    E = H + kinetic_local - kinetic_cross
    q_at_a = mp.mpf(1)
    lower = w / (H + 1)
    witnessed = w * q_at_a / E
    upper = 2 * w / H
    assert H <= E <= H + 1
    assert lower <= witnessed <= upper
    assert E > 0
    print('epsilon:', mp.nstr(eps, 12),
          'H:', mp.nstr(H, 15),
          'rectangular E:', mp.nstr(E, 15),
          'certified analytic sandwich (diagnostic):',
          mp.nstr(lower, 12), '<=',
          mp.nstr(witnessed, 12), '<=',
          mp.nstr(upper, 12))

print('PASS: exact two-strip autocorrelation and sharp 1/log prime activation.')
print('Scope: kinetic-versus-one-prime source; no completed Weil positivity or RH.')
