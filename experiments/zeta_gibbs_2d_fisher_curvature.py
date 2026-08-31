#!/usr/bin/env python3
"""Numerical curvature probe for the genuine two-parameter zeta-Gibbs family.

Z(beta, eta) = sum_{n>=1} exp(-beta log n - eta (log n)^2), eta > 0.

The Fisher metric in (beta, eta) is the covariance matrix of T=(X,X^2),
X=log n.  For a two-dimensional Hessian metric g_ij = psi_ij, the scalar
curvature convention used here is

  R = - det([[psi11, psi12, psi22],
             [psi111,psi112,psi122],
             [psi112,psi122,psi222]]) / (2 det(g)^2).

Because beta and eta enter with minus signs, every third derivative of psi is
minus the corresponding third joint cumulant of (X,X^2).  The determinant has
two third-derivative rows, so the simultaneous sign does not alter the sampled
curvature sign.

This is a discovery probe, not a proof of a global curvature statement.
"""

import mpmath as mp

mp.mp.dps = 50


def raw_log_moments(beta: mp.mpf, eta: mp.mpf, nmax: int = 20000):
    if not eta > 0:
        raise ValueError("eta must be positive")
    z = mp.mpf("0")
    sums = [mp.mpf("0") for _ in range(7)]
    for n in range(1, nmax + 1):
        x = mp.log(n)
        w = mp.exp(-beta * x - eta * x * x)
        z += w
        xp = mp.mpf("1")
        for k in range(1, 7):
            xp *= x
            sums[k] += w * xp
    return z, [None] + [sums[k] / z for k in range(1, 7)]


def fisher_curvature(beta, eta, nmax=20000):
    beta = mp.mpf(beta)
    eta = mp.mpf(eta)
    _, m = raw_log_moments(beta, eta, nmax)

    g11 = m[2] - m[1] ** 2
    g12 = m[3] - m[1] * m[2]
    g22 = m[4] - m[2] ** 2
    detg = g11 * g22 - g12 ** 2

    def k3(a, b, c):
        return (
            m[a + b + c]
            - m[a] * m[b + c]
            - m[b] * m[a + c]
            - m[c] * m[a + b]
            + 2 * m[a] * m[b] * m[c]
        )

    k111 = k3(1, 1, 1)
    k112 = k3(1, 1, 2)
    k122 = k3(1, 2, 2)
    k222 = k3(2, 2, 2)

    h = mp.matrix(
        [
            [g11, g12, g22],
            [-k111, -k112, -k122],
            [-k112, -k122, -k222],
        ]
    )
    scalar_r = -mp.det(h) / (2 * detg ** 2)
    return scalar_r, detg


def convergence_checked(beta, eta):
    r1, d1 = fisher_curvature(beta, eta, 10000)
    r2, d2 = fisher_curvature(beta, eta, 20000)
    assert abs(r1 - r2) < mp.mpf("1e-18")
    assert abs(d1 - d2) < mp.mpf("1e-18")
    assert d2 > 0
    return r2, d2


if __name__ == "__main__":
    samples = [
        ("0", "0.5"),
        ("1", "0.5"),
        ("0", "1"),
        ("1", "1"),
        ("0", "1.5"),
        ("0", "2"),
        ("1", "2"),
        ("0", "3"),
    ]
    saw_negative = False
    saw_positive = False
    for beta, eta in samples:
        r, detg = convergence_checked(beta, eta)
        saw_negative = saw_negative or r < 0
        saw_positive = saw_positive or r > 0
        print(
            f"beta={beta:>3} eta={eta:>3} "
            f"R={mp.nstr(r, 18):>22} det(g)={mp.nstr(detg, 18)}"
        )
    # This is the substantive discovery check: sampled curvature changes sign.
    assert saw_negative and saw_positive
