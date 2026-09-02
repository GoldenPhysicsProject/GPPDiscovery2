#!/usr/bin/env python3
"""High-precision audit for the two-parameter quadratically confined number gas.

For
    Z(beta, eta) = sum_{n>=2} exp(-beta log n - eta (log n)^2), eta > 0,
this script checks the first/second derivative identities for log Z against
high-precision finite differences and records the compact-parameter domination
used for a future Lean proof of differentiation under the countable sum.

Uniform domination on a rectangle |beta| <= B, eta >= eta0 > 0:
for a,b >= 0 and m = a + 2 b,

 |d_beta^a d_eta^b exp(-beta L - eta L^2)|
   = L^m exp(-beta L - eta L^2)
  <= exp(B^2 / (2 eta0)) L^m exp(-(eta0/2) L^2),   L = log n.

Indeed B L <= (eta0/2)L^2 + B^2/(2 eta0).  The right-hand side is summable:
for any p>1, once L >= 2p/eta0,
    exp(-(eta0/2)L^2) <= exp(-pL) = n^{-p},
so the tail is bounded by const * (log n)^m / n^p.

This gives a parameter-uniform summable majorant for every mixed derivative on
compact subsets of R x (0,infinity), strongly suggesting the clean formal target:
Z is C^infinity there and Hessian(log Z) is Cov(log n, (log n)^2).
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 70


def raw_sums(beta: mp.mpf, eta: mp.mpf, tol=mp.mpf("1e-65")):
    z = mp.mpf("0")
    moments = [mp.mpf("0") for _ in range(7)]
    n = 2
    while True:
        L = mp.log(n)
        w = mp.exp(-beta * L - eta * L * L)
        z += w
        for k in range(7):
            moments[k] += (L ** k) * w
        if n > 2000 and w < tol:
            # The weights are eventually monotone decreasing for eta>0; this is
            # only an audit truncation rule, not part of the analytic proof.
            break
        n += 1
        if n > 2_000_000:
            raise RuntimeError("truncation guard reached")
    return z, moments, n


def logZ(beta, eta):
    z, _, _ = raw_sums(mp.mpf(beta), mp.mpf(eta))
    return mp.log(z)


def analytic_geometry(beta, eta):
    z, M, nstop = raw_sums(mp.mpf(beta), mp.mpf(eta))
    E = [x / z for x in M]
    d_beta = -E[1]
    d_eta = -E[2]
    h_bb = E[2] - E[1] ** 2
    h_be = E[3] - E[1] * E[2]
    h_ee = E[4] - E[2] ** 2
    return {
        "Z": z,
        "d_beta": d_beta,
        "d_eta": d_eta,
        "h_bb": h_bb,
        "h_be": h_be,
        "h_ee": h_ee,
        "det_h": h_bb * h_ee - h_be ** 2,
        "nstop": nstop,
    }


def finite_difference_geometry(beta, eta, h=mp.mpf("1e-5")):
    b = mp.mpf(beta)
    e = mp.mpf(eta)
    f = logZ
    f00 = f(b, e)
    fp0, fm0 = f(b + h, e), f(b - h, e)
    f0p, f0m = f(b, e + h), f(b, e - h)
    return {
        "d_beta": (fp0 - fm0) / (2 * h),
        "d_eta": (f0p - f0m) / (2 * h),
        "h_bb": (fp0 - 2 * f00 + fm0) / h ** 2,
        "h_ee": (f0p - 2 * f00 + f0m) / h ** 2,
        "h_be": (
            f(b + h, e + h)
            - f(b + h, e - h)
            - f(b - h, e + h)
            + f(b - h, e - h)
        ) / (4 * h ** 2),
    }


def domination_certificate(B, eta0, derivative_order, p=mp.mpf("2")):
    B = mp.mpf(B)
    eta0 = mp.mpf(eta0)
    p = mp.mpf(p)
    if eta0 <= 0 or p <= 1:
        raise ValueError("need eta0>0 and p>1")
    m = int(derivative_order)
    return {
        "m": m,
        "prefactor": mp.exp(B * B / (2 * eta0)),
        "log_threshold": 2 * p / eta0,
        "n_threshold": mp.ceil(mp.exp(2 * p / eta0)),
        "tail_shape": f"(log n)^{m} / n^{mp.nstr(p, 8)}",
    }


def main():
    points = [(2, mp.mpf("0.5")), (0, 5), (-5, 10), (1, mp.mpf("0.2"))]
    for beta, eta in points:
        a = analytic_geometry(beta, eta)
        f = finite_difference_geometry(beta, eta)
        print(f"beta={beta}, eta={eta}, truncation n={a['nstop']}")
        for key in ("d_beta", "d_eta", "h_bb", "h_be", "h_ee"):
            err = abs(a[key] - f[key])
            print(f"  {key:7s}: analytic={mp.nstr(a[key], 24)}  fd={mp.nstr(f[key], 24)}  |err|={mp.nstr(err, 8)}")
        print(f"  det Hess(log Z) = {mp.nstr(a['det_h'], 24)}")
        print()

    print("Compact domination example |beta|<=5, eta>=0.2:")
    for m in range(5):
        cert = domination_certificate(5, mp.mpf("0.2"), m)
        print(
            f"  derivative log-power m={m}: prefactor={mp.nstr(cert['prefactor'], 12)}, "
            f"tail valid for log n >= {mp.nstr(cert['log_threshold'], 8)} "
            f"(n >= {cert['n_threshold']}), tail {cert['tail_shape']}"
        )


if __name__ == "__main__":
    main()
