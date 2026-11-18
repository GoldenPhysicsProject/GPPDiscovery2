#!/usr/bin/env python3
"""Global circular boundary diagnostics (NOT a zeta spectral or RH proof).
Checks the zero-independent logarithmic Fourier carrier and two-sheet monodromy.
Pure Python standard library, does NOT import or assume zeta zeros.
"""
import math
import cmath

PI = math.pi

def rv_mangoldt_main(T):
    return T / (2 * PI) * (math.log(T / (2 * PI)) - 1)

def inverse_main(n):
    assert n >= 1
    lo = 2 * PI * math.e
    hi = 32.0
    while rv_mangoldt_main(hi) < n:
        hi *= 2
    for _ in range(100):
        m = (lo + hi) / 2
        if rv_mangoldt_main(m) < n:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2

def check_log_carrier():
    prev = 0
    for n in range(1, 10001):
        lam = inverse_main(n)
        assert lam > prev
        assert abs(rv_mangoldt_main(lam) - n) <= 5e-10
        prev = lam
    for T in [100, 1000, 1000000]:
        circle_count = T/(2*PI)
        smooth_count = rv_mangoldt_main(T)
        print('T=',T,'local_circle_count=',circle_count,'smooth_zeta_count=',smooth_count,
              'effective_circumference=',math.log(T/(2*PI)))
    print('PASS: log Dirac invertible monotone smooth spectral count, n=1..10000')

def check_monodromy():
    for delta,gamma,L in [(0.2,14.1,0.7),(-0.3,8.0,1.7),
                          (0.0,14.1,0.7),(0.48,100.0,2.0)]:
        phase = cmath.exp(1j*gamma*L)
        l1=phase*math.exp(delta*L)
        l2=phase*math.exp(-delta*L)
        # M^* J M=J iff conj(l1)*l2=conj(l2)*l1=1
        assert abs(l1.conjugate()*l2-1)<1e-12
        assert abs(l2.conjugate()*l1-1)<1e-12
        if delta == 0:
            assert abs(abs(l1)**2 - 1) < 1e-12
        else:
            assert abs(abs(l1)**2 - 1) > 1e-8
            assert abs(abs(l2)**2 - 1) > 1e-8
        print('delta=',delta,'L=',L,'|M_eigs|=',abs(l1),abs(l2))
    print('PASS: two-face Krein-unitarity vs positive-unitarity obstruction')

if __name__ == '__main__':
    check_log_carrier()
    check_monodromy()
