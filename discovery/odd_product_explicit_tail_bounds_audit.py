#!/usr/bin/env python3
"""Audit explicit tails for the odd Weierstrass product/log derivative.

For N >= 1 and x real, set

  L_N(x) = sum_{k=N}^inf log(1 + x^2/(2k+1)^2),
  D_N(x) = sum_{k=N}^inf 2x/((2k+1)^2 + x^2).

The decreasing-function integral test gives

  sum_{k=N}^inf 1/(2k+1)^2 <= int_{N-1}^inf du/(2u+1)^2
                                 = 1/(2(2N-1)).

Using log(1+u) <= u for u >= 0 and dropping x^2 from the positive
derominator therefore yields the rigorous global bounds

  0 <= L_N(x) <= x^2/(2(2N-1)),
  |D_N(x)| <= |x|/(2N-1).

Both constants are asymptotically sharp at first order because
N * sum_{k=N}^inf (2k+1)^(-2) -> 1/4, so
N L_N(x) -> x^2/4 and N D_N(x) -> x/2 for fixed x.

This script is discovery evidence / regression checking only.  The displayed
inequalities have elementary analytic proofs, but they are not Lean-certified
until separately formalized in GPPVerify2.
"""

import mpmath as mp

mp.mp.dps = 60


def log_tail(x, n):
    x = mp.mpf(x)
    return mp.nsum(lambda k: mp.log1p(x*x/(2*k+1)**2), [n, mp.inf])


def deriv_tail(x, n):
    x = mp.mpf(x)
    return mp.nsum(lambda k: 2*x/((2*k+1)**2 + x*x), [n, mp.inf])


def log_bound(x, n):
    x = abs(mp.mpf(x))
    return x*x/(2*(2*n-1))


def deriv_bound(x, n):
    x = abs(mp.mpf(x))
    return x/(2*n-1)


def main():
    xs = [mp.mpf('-4'), mp.mpf('-1'), mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2'), mp.mpf('5')]
    ns = [1, 2, 5, 10, 100, 1000]
    worst_log_ratio = mp.mpf('0')
    worst_deriv_ratio = mp.mpf('0')

    for x in xs:
        for n in ns:
            lt = log_tail(x, n)
            dt = deriv_tail(x, n)
            lb = log_bound(x, n)
            db = deriv_bound(x, n)
            if abs(x) > 0:
                assert 0 <= lt <= lb
                assert abs(dt) <= db
                worst_log_ratio = max(worst_log_ratio, lt/lb)
                worst_deriv_ratio = max(worst_deriv_ratio, abs(dt)/db)

    print('all finite-grid bound checks passed')
    print('worst log-tail / bound ratio:', mp.nstr(worst_log_ratio, 20))
    print('worst derivative-tail / bound ratio:', mp.nstr(worst_deriv_ratio, 20))

    # First-order asymptotic constants at representative fixed x.
    for x in [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2')]:
        n = 10000
        print(
            'x=', mp.nstr(x, 6),
            'N*log_tail=', mp.nstr(n*log_tail(x, n), 20),
            'target=', mp.nstr(x*x/4, 20),
            'N*deriv_tail=', mp.nstr(n*deriv_tail(x, n), 20),
            'target=', mp.nstr(x/2, 20),
        )


if __name__ == '__main__':
    main()
