#!/usr/bin/env python3
"""Numerical audit of the 4D MHV two-particle cut identity.

All external momenta are outgoing.  The cut routing is
  p1+p2+l1+l2=0,
  -l1-l2+p3+p4=0.

For the color-ordered gluon cut
  A(1-,2-,l2+,l1+) A((-l1)-,(-l2)-,3+,4+)
we check
  C_s / A_tree = -i s t / [ (l1+p1)^2 (l1-p4)^2 ]
for several real massless COM kinematics.

This script is an audit, not the analytic proof.
"""
import numpy as np


def pmat(p):
    E, px, py, pz = p
    return np.array([[E + pz, px - 1j * py],
                     [px + 1j * py, E - pz]], dtype=complex)


def spinors(p):
    """Factor the rank-one massless bispinor p=lambda*tilde-lambda."""
    M = pmat(p)
    i, j = np.unravel_index(np.argmax(np.abs(M)), M.shape)
    lam = M[:, j].copy()
    if abs(lam[i]) < 1e-13:
        raise RuntimeError("degenerate factorization pivot")
    tlam = np.zeros(2, dtype=complex)
    tlam[j] = 1.0
    tlam[1 - j] = M[i, 1 - j] / lam[i]
    if np.max(np.abs(np.outer(lam, tlam) - M)) > 1e-10:
        raise RuntimeError("spinor factorization failed")
    return lam, tlam


def angle(a, b):
    return a[0] * b[1] - a[1] * b[0]


def parke_taylor(lams):
    """A4(1-,2-,3+,4+) with the first two entries negative."""
    num = angle(lams[0], lams[1]) ** 4
    den = 1.0 + 0j
    for i in range(4):
        den *= angle(lams[i], lams[(i + 1) % 4])
    return 1j * num / den


def mdot(a, b):
    return a[0] * b[0] - np.dot(a[1:], b[1:])


def msq(a):
    return mdot(a, a)


def one_case(theta, phi):
    E = 1.0
    p1 = np.array([-E, 0.0, 0.0, -E])
    p2 = np.array([-E, 0.0, 0.0,  E])
    p3 = np.array([ E, E*np.sin(theta), 0.0, E*np.cos(theta)])
    p4 = np.array([ E,-E*np.sin(theta), 0.0,-E*np.cos(theta)])
    l1 = np.array([ E, E*np.sin(phi), 0.0, E*np.cos(phi)])
    l2 = np.array([ E,-E*np.sin(phi), 0.0,-E*np.cos(phi)])

    assert np.max(np.abs(p1+p2+p3+p4)) < 1e-12
    assert np.max(np.abs(p1+p2+l1+l2)) < 1e-12
    assert np.max(np.abs(-l1-l2+p3+p4)) < 1e-12

    ext = [spinors(p)[0] for p in (p1,p2,p3,p4)]
    ll1, ll2 = spinors(l1)[0], spinors(l2)[0]
    ml1, ml2 = spinors(-l1)[0], spinors(-l2)[0]

    Aext = parke_taylor(ext)
    AL = parke_taylor([ext[0], ext[1], ll2, ll1])
    AR = parke_taylor([ml1, ml2, ext[2], ext[3]])
    lhs = AL * AR / Aext

    s = msq(p1+p2)
    t = msq(p2+p3)
    D1 = msq(l1+p1)
    D2 = msq(l1-p4)
    rhs = -1j * s * t / (D1 * D2)
    return lhs, rhs


def main():
    worst = 0.0
    for theta in (0.5, 0.9, 1.4):
        for phi in (0.3, 0.7, 1.2, 2.0):
            if abs(theta-phi) < 0.05:
                continue
            lhs, rhs = one_case(theta, phi)
            err = abs(lhs-rhs) / max(1.0, abs(rhs))
            worst = max(worst, err)
            assert err < 2e-12, (theta, phi, lhs, rhs, err)
    print("PASS: C_s/A_tree = -i s t/(D1 D2) on all audited MHV cut kinematics")
    print("worst relative error:", worst)


if __name__ == "__main__":
    main()
