#!/usr/bin/env python3
"""Executable audit for the continuous-sech derivative tail and odd cosh product.

This is discovery evidence, not a substitute for the Lean/analytic proofs.
"""

import mpmath as mp

mp.mp.dps = 70
pi = mp.pi

gap = 1 - mp.e ** (-2 * pi)
sharp_coeff = 2 / gap
sharp_tail_mass_c1 = 4 * mp.e ** (-pi) / (pi * gap)

print("sharp coefficient 2/(1-exp(-2*pi)) =", sharp_coeff)
print("tail L1 mass for c=1 =", sharp_tail_mass_c1)


def derivative_kernel_abs(c, t, x):
    if x == 0:
        return mp.mpf("0")
    return abs(c * mp.sin(t * x) / mp.sinh(pi * abs(x)))


def tail_bound(c, x):
    return sharp_coeff * c * mp.e ** (-pi * abs(x))


# Stress both signs and noninteger frequencies on a logarithmic tail grid.
worst = mp.mpf("0")
for c in [mp.mpf("0.1"), mp.mpf("1"), mp.mpf("3.7")]:
    for t in [mp.mpf("-9.3"), mp.mpf("-1.1"), mp.mpf("0.37"), mp.mpf("4.8")]:
        for k in range(401):
            x = mp.mpf("1") + mp.mpf(k) / 20
            for xx in (x, -x):
                ratio = derivative_kernel_abs(c, t, xx) / tail_bound(c, xx)
                worst = max(worst, ratio)
                assert ratio <= 1 + mp.mpf("1e-60")
print("worst sampled derivative-tail ratio =", worst)


def odd_product(t, N):
    p = mp.mpf("1")
    for n in range(N):
        p *= 1 + t * t / (((2 * n + 1) ** 2) * pi * pi)
    return p


def sinh_product(t, N):
    p = mp.mpf("1")
    for j in range(1, N + 1):
        p *= 1 + t * t / ((j * j) * pi * pi)
    return p


for t in [mp.mpf("0"), mp.mpf("0.7"), mp.mpf("2.3"), mp.mpf("-5.1")]:
    for N in [1, 3, 10, 40, 160]:
        lhs = odd_product(t, N)
        rhs_finite = sinh_product(t, 2 * N) / sinh_product(t / 2, N)
        assert mp.almosteq(lhs, rhs_finite)
    approx = odd_product(t, 400)
    exact = mp.cosh(t / 2)
    print("t =", t, "odd-product error =", abs(approx - exact))

print("all executable checks passed")
