#!/usr/bin/env python3
"""High-precision audit of the normalized celestial spectral weight.

Codex/GPT discovery track only.

For
    rho(lam) = 2 lam / sinh(pi lam)
(the normalized version of P(lam)=pi*lam/sinh(pi*lam)), this checks

    int_R rho(lam) exp(i t lam) dlam = sech(t/2)^2,

and the associated Levy-Khintchine identity

    log sech(t/2)^2
      = int_R (cos(t x)-1) / (|x| sinh(pi |x|)) dx
      = -2 int_0^inf (1-cos(t x))/(x sinh(pi x)) dx.

Hence rho is an infinitely divisible symmetric probability density with Levy
density 1/(|x| sinh(pi |x|)).  Equivalently its convolution semigroup has
characteristic functions sech(t/2)^(2 a), a>0.

This is a discovery/audit script, not a Lean proof.
"""

import mpmath as mp

mp.mp.dps = 70


def rho(lam):
    if lam == 0:
        return mp.mpf(2) / mp.pi
    return 2 * lam / mp.sinh(mp.pi * lam)


def fourier_rho(t):
    f = lambda x: rho(x) * mp.cos(t * x)
    return 2 * mp.quad(f, [0, 1, mp.inf])


def closed_fourier(t):
    return mp.sech(t / 2) ** 2


def levy_log_char(t):
    if t == 0:
        return mp.mpf('0')
    f = lambda x: (1 - mp.cos(t * x)) / (x * mp.sinh(mp.pi * x))
    return -2 * mp.quad(f, [0, 1, mp.inf])


def closed_log_char(t):
    return 2 * mp.log(mp.sech(t / 2))


def sine_over_sinh(t):
    f = lambda x: mp.sin(t * x) / mp.sinh(mp.pi * x)
    return mp.quad(f, [0, 1, mp.inf])


def closed_sine(t):
    return mp.mpf('0.5') * mp.tanh(t / 2)


# Normalization.
norm = 2 * mp.quad(lambda x: rho(x), [0, 1, mp.inf])
assert abs(norm - 1) < mp.mpf('1e-60'), (norm, norm - 1)

# Fourier and Levy identities over a nontrivial sample.
for t in [mp.mpf('0'), mp.mpf('0.125'), mp.mpf('0.7'), mp.mpf('1'), mp.mpf('2.75'), mp.mpf('6')]:
    F = fourier_rho(t)
    Fc = closed_fourier(t)
    assert abs(F - Fc) < mp.mpf('1e-55'), (t, F, Fc, F-Fc)

    L = levy_log_char(t)
    Lc = closed_log_char(t)
    assert abs(L - Lc) < mp.mpf('1e-55'), (t, L, Lc, L-Lc)

    S = sine_over_sinh(t)
    Sc = closed_sine(t)
    assert abs(S - Sc) < mp.mpf('1e-55'), (t, S, Sc, S-Sc)

# Exact low even moments implied by derivatives at the origin.
# E[lambda^2]=1/2 and E[lambda^4]=1 are independently integrated.
m2 = 2 * mp.quad(lambda x: x**2 * rho(x), [0, 1, mp.inf])
m4 = 2 * mp.quad(lambda x: x**4 * rho(x), [0, 1, mp.inf])
assert abs(m2 - mp.mpf('0.5')) < mp.mpf('1e-55')
assert abs(m4 - 1) < mp.mpf('1e-55')

# Semigroup check: phi_a phi_b = phi_{a+b} exactly at the closed-form level.
for t in [mp.mpf('0.3'), mp.mpf('1.4'), mp.mpf('4.2')]:
    for a, b in [(mp.mpf('0.5'), mp.mpf('1.25')), (mp.mpf('1'), mp.mpf('2'))]:
        base = closed_fourier(t)
        lhs = base**a * base**b
        rhs = base**(a+b)
        assert abs(lhs-rhs) < mp.mpf('1e-65')

print('normalized spectral-weight logistic/Levy audit: PASS')
print('normalization =', mp.nstr(norm, 40))
print('E[lambda^2] =', mp.nstr(m2, 40))
print('E[lambda^4] =', mp.nstr(m4, 40))
print('Fourier transform: sech(t/2)^2')
print('Levy density: 1/(|x| sinh(pi |x|))')
