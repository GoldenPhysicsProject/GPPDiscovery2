#!/usr/bin/env python3
"""Executable audit for the two-parameter number-Gibbs Fisher determinant.

Model (vacuum included):
    Z(beta, eta) = sum_{n>=1} exp(-beta log n - eta (log n)^2).

For a finite truncation N, the covariance determinant of X=log n and X^2 has
the exact Cauchy-Binet expansion
    det g_N = sum_{i<j<k} p_i p_j p_k V(x_i,x_j,x_k)^2.
Hence the fixed witness (1,2,3) gives the explicit lower bound
    det g_N >= p_1 p_2 p_3 [log2 log3 log(3/2)]^2.
The same formula suggests the countable target after moment convergence.

This script checks the determinant, entropy identity, derivative identities and
fixed-triple lower bound at high precision for representative parameters.
"""

import mpmath as mp

mp.mp.dps = 70


def finite_stats(beta, eta, N):
    xs = [mp.log(n) for n in range(1, N + 1)]
    ws = [mp.e ** (-beta * x - eta * x * x) for x in xs]
    Z = mp.fsum(ws)
    ps = [w / Z for w in ws]
    mus = [mp.fsum(p * x**r for p, x in zip(ps, xs)) for r in range(1, 5)]
    m1, m2, m3, m4 = mus
    g11 = m2 - m1*m1
    g12 = m3 - m1*m2
    g22 = m4 - m2*m2
    det = g11*g22 - g12*g12
    H_direct = -mp.fsum(p * mp.log(p) for p in ps)
    H_thermo = mp.log(Z) + beta*m1 + eta*m2
    return Z, mus, det, H_direct, H_thermo


def witness_bound(beta, eta, Z):
    l2, l3 = mp.log(2), mp.log(3)
    V2 = (l2*l3*(l3-l2))**2
    numerator = mp.e ** (-beta*(l2+l3) - eta*(l2*l2+l3*l3)) * V2
    return numerator / Z**3


def logZ(beta, eta, N):
    return mp.log(mp.fsum(mp.e ** (-beta*mp.log(n) - eta*mp.log(n)**2)
                          for n in range(1, N + 1)))


def check(beta, eta, N):
    Z, mus, det, Hd, Ht = finite_stats(beta, eta, N)
    bound = witness_bound(beta, eta, Z)
    m1, m2, _, _ = mus
    db = mp.diff(lambda b: logZ(b, eta, N), beta)
    de = mp.diff(lambda e: logZ(beta, e, N), eta)
    print(f"beta={beta}, eta={eta}, N={N}")
    print("  det g              =", mp.nstr(det, 30))
    print("  (1,2,3) lower bound=", mp.nstr(bound, 30))
    print("  det/bound          =", mp.nstr(det/bound, 20))
    print("  H direct-thermo    =", mp.nstr(Hd-Ht, 8))
    print("  d_beta logZ + E[X] =", mp.nstr(db+m1, 8))
    print("  d_eta  logZ + E[X2]=", mp.nstr(de+m2, 8))
    assert det > 0
    assert det + mp.mpf('1e-60') >= bound
    assert abs(Hd-Ht) < mp.mpf('1e-55')
    assert abs(db+m1) < mp.mpf('1e-50')
    assert abs(de+m2) < mp.mpf('1e-50')


if __name__ == "__main__":
    tests = [
        (mp.mpf('2.0'), mp.mpf('0.0'), 4000),
        (mp.mpf('1.0'), mp.mpf('0.2'), 1200),
        (mp.mpf('0.0'), mp.mpf('0.7'), 500),
        (mp.mpf('-2.0'), mp.mpf('1.5'), 300),
        (mp.mpf('3.5'), mp.mpf('4.0'), 200),
    ]
    for args in tests:
        check(*args)
    print("all two-parameter number-Gibbs checks passed")
