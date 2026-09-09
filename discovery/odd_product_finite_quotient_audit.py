#!/usr/bin/env python3
"""Exact finite odd/even quotient audit for the chamber tanh bridge.

For
    P_N(x) = prod_{j=1}^N (1 + x^2/j^2),
    O_N(x) = prod_{k=0}^{N-1} (1 + x^2/(2k+1)^2),
we have the exact finite identity
    O_N(x) = P_{2N}(x) / P_N(x/2).

Combined with the certified sinh Weierstrass limit
    P_N(x) -> sinh(pi x)/(pi x),
the quotient target is
    O_N(x) -> cosh(pi x/2).

This script audits the finite identity at high precision and the limiting target.
It is discovery evidence only; it does not replace the Lean limit proof.
"""

from mpmath import mp

mp.dps = 80


def P(N, x):
    return mp.fprod(1 + x*x/(j*j) for j in range(1, N + 1))


def O(N, x):
    return mp.fprod(1 + x*x/((2*k + 1)**2) for k in range(N))


def quotient(N, x):
    return P(2*N, x) / P(N, x/2)


def main():
    xs = [mp.mpf('0'), mp.mpf('0.125'), mp.mpf('0.7'), mp.mpf('1.5'), mp.mpf('3')]
    Ns = [4, 16, 64, 256, 1024]
    worst_exact = mp.mpf('0')
    print('finite identity: O_N(x) = P_{2N}(x)/P_N(x/2)')
    for x in xs:
        for N in Ns:
            defect = abs(O(N, x) - quotient(N, x))
            worst_exact = max(worst_exact, defect)
        q = quotient(Ns[-1], x)
        target = mp.cosh(mp.pi*x/2)
        rel = abs(q-target) / max(mp.mpf(1), abs(target))
        print(f'x={mp.nstr(x,8):>8}  N={Ns[-1]:4d}  quotient={mp.nstr(q,28)}  target={mp.nstr(target,28)}  relerr={mp.nstr(rel,8)}')
    print('max finite-identity defect =', mp.nstr(worst_exact, 12))

    # Also audit the equivalent hyperbolic quotient away from x=0:
    # [sinh(pi x)/(pi x)] / [sinh(pi x/2)/(pi x/2)] = cosh(pi x/2).
    worst_hyp = mp.mpf('0')
    for x in xs[1:]:
        lhs = (mp.sinh(mp.pi*x)/(mp.pi*x)) / (mp.sinh(mp.pi*x/2)/(mp.pi*x/2))
        rhs = mp.cosh(mp.pi*x/2)
        worst_hyp = max(worst_hyp, abs(lhs-rhs))
    print('max hyperbolic-quotient defect =', mp.nstr(worst_hyp, 12))


if __name__ == '__main__':
    main()
