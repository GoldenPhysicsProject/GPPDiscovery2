"""Quadratic number-Gibbs third-response audit.

For
    w_n(beta, eta) = exp(-beta L_n - eta L_n^2),  L_n = log n,
    Psi(beta, eta) = log sum_{n>=1} w_n,
the exponential-family prediction is that the Hessian is the covariance matrix
of (L, L^2), while every third derivative of Psi is minus the corresponding
third joint cumulant.

This script checks the four independent symmetric third-derivative components
on high-precision finite truncations.  It is discovery support only; the
countable differentiation theorem belongs in GPPVerify2.
"""

import mpmath as mp

mp.mp.dps = 60


def raw_moments(beta, eta, N=5000, max_order=6):
    sums = [mp.mpf("0") for _ in range(max_order + 1)]
    for n in range(1, N + 1):
        L = mp.log(n)
        w = mp.exp(-beta * L - eta * L * L)
        p = mp.mpf("1")
        for r in range(max_order + 1):
            if r:
                p *= L
            sums[r] += w * p
    Z = sums[0]
    return [s / Z for s in sums]


def third_joint_cumulants(m):
    m1, m2, m3, m4, m5, m6 = m[1:7]
    k111 = m3 - 3 * m1 * m2 + 2 * m1**3
    k112 = m4 - m2**2 - 2 * m1 * m3 + 2 * m1**2 * m2
    k122 = m5 - 2 * m2 * m3 - m1 * m4 + 2 * m1 * m2**2
    k222 = m6 - 3 * m2 * m4 + 2 * m2**3
    return k111, k112, k122, k222


def logZ(beta, eta, N=5000):
    return mp.log(mp.fsum(
        mp.exp(-beta * mp.log(n) - eta * mp.log(n)**2)
        for n in range(1, N + 1)
    ))


def check(beta, eta, N=5000):
    m = raw_moments(beta, eta, N=N)
    k111, k112, k122, k222 = third_joint_cumulants(m)

    d111 = mp.diff(lambda b: logZ(b, eta, N), beta, 3)
    d112 = mp.diff(lambda e: mp.diff(lambda b: logZ(b, e, N), beta, 2), eta)
    d122 = mp.diff(lambda b: mp.diff(lambda e: logZ(b, e, N), eta, 2), beta)
    d222 = mp.diff(lambda e: logZ(beta, e, N), eta, 3)

    residuals = (d111 + k111, d112 + k112, d122 + k122, d222 + k222)
    return (k111, k112, k122, k222), residuals


if __name__ == "__main__":
    tests = [
        (mp.mpf("0.7"), mp.mpf("0.3")),
        (mp.mpf("-1.2"), mp.mpf("0.45")),
        (mp.mpf("2.0"), mp.mpf("0.2")),
    ]
    for beta, eta in tests:
        cumulants, residuals = check(beta, eta)
        print(f"beta={beta}, eta={eta}")
        print("third cumulants k111,k112,k122,k222:")
        print(*(mp.nstr(x, 24) for x in cumulants))
        print("third-derivative + cumulant residuals:")
        print(*(mp.nstr(x, 8) for x in residuals))
        assert max(abs(x) for x in residuals) < mp.mpf("1e-40")

    print("PASS: d^3 Psi = - third joint cumulant tensor on all audited truncations")
