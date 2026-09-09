#!/usr/bin/env python3
"""High-precision audit for the derivative of the Gamma-square chamber Levy exponent.

For a >= 0 and lambda_n=(2n+1)pi,

  E_a(t) = 2a sum_n log(1+t^2/lambda_n^2) = 2a log cosh(t/2),

hence

  E_a'(t) = sum_n 4 a t/(lambda_n^2+t^2) = a tanh(t/2).

For the N-mode partial derivative D_{a,N}(t), the tail has the rigorous bound

  |E_a'(t)-D_{a,N}(t)|
    <= a |t|/pi^2 * psi_1(N+1/2),

because lambda_n^2+t^2 >= lambda_n^2 and
sum_{n=N}^infty (2n+1)^(-2) = psi_1(N+1/2)/4.

This gives uniform derivative convergence on every compact frequency interval.
"""

import mpmath as mp

mp.mp.dps = 80


def lam(n):
    return (2*n + 1) * mp.pi


def d_partial(a, t, N):
    return mp.fsum(4*a*t / (lam(n)**2 + t**2) for n in range(N))


def d_exact(a, t):
    return a * mp.tanh(t/2)


def d_tail_bound(a, t, N):
    return a * abs(t) / (mp.pi**2) * mp.polygamma(1, N + mp.mpf('0.5'))


def audit_point(a, t, N):
    err = abs(d_exact(a, t) - d_partial(a, t, N))
    bnd = d_tail_bound(a, t, N)
    assert err <= bnd * (1 + mp.mpf('1e-70'))
    return err, bnd


def main():
    tests = [
        (mp.mpf('0.5'), mp.mpf('-7.25'), 4),
        (mp.mpf('1.0'), mp.mpf('0.3'), 8),
        (mp.mpf('1.5'), mp.mpf('3.0'), 16),
        (mp.mpf('2.3'), mp.mpf('9.0'), 32),
    ]
    for a, t, N in tests:
        err, bnd = audit_point(a, t, N)
        print(f'a={a} t={t} N={N}')
        print('  derivative error =', mp.nstr(err, 30))
        print('  rigorous bound   =', mp.nstr(bnd, 30))
        print('  ratio             =', mp.nstr(err/bnd if bnd else 0, 20))

    # Direct high-precision infinite-series check.
    for a, t in [(mp.mpf('1'), mp.mpf('1.7')), (mp.mpf('2.3'), mp.mpf('-4.2'))]:
        s = mp.nsum(lambda k: 4*a*t / (((2*k+1)*mp.pi)**2 + t**2), [0, mp.inf])
        target = d_exact(a, t)
        assert mp.almosteq(s, target)
        print('series identity residual =', mp.nstr(abs(s-target), 20))

    # Compact-uniform consequence: on |t|<=T, replace |t| by T.
    a, T, N = mp.mpf('1.7'), mp.mpf('6'), 20
    uniform = a*T/(mp.pi**2) * mp.polygamma(1, N + mp.mpf('0.5'))
    gridmax = max(abs(d_exact(a, t) - d_partial(a, t, N))
                  for t in [(-T + 2*T*j/200) for j in range(201)])
    assert gridmax <= uniform
    print('compact grid max error =', mp.nstr(gridmax, 30))
    print('compact rigorous bound =', mp.nstr(uniform, 30))

    print('PASS: Levy derivative identity and trigamma tail bound audited.')


if __name__ == '__main__':
    main()
