#!/usr/bin/env python3
"""First exponentially small correction to the large-eta zeta-Gibbs Fisher determinant.

For x_n = log n and weights exp(-beta*x_n-eta*x_n^2), the normalized Fisher
2x2 determinant admits the Vandermonde triple sum.  The leading triple is
(1,2,3); the unique next quadratic-cost triple is (1,2,4).
"""

from mpmath import mp

mp.dps = 80


def vandermonde2(xs):
    x, y, z = xs
    return (x-y)**2 * (x-z)**2 * (y-z)**2


def det_ratio(beta, eta, nmax=2000):
    xs = [mp.log(n) for n in range(1, nmax + 1)]
    raw = [mp.e**(-beta*x - eta*x*x) for x in xs]
    Z = mp.fsum(raw)
    ps = [w/Z for w in raw]
    m1 = mp.fsum(p*x for p, x in zip(ps, xs))
    m2 = mp.fsum(p*x**2 for p, x in zip(ps, xs))
    m3 = mp.fsum(p*x**3 for p, x in zip(ps, xs))
    m4 = mp.fsum(p*x**4 for p, x in zip(ps, xs))
    detg = (m2-m1*m1)*(m4-m2*m2) - (m3-m1*m2)**2
    a, b = mp.log(2), mp.log(3)
    L123 = (raw[0]*raw[1]*raw[2]/Z**3) * (a*b*(b-a))**2
    return detg/L123


def first_correction(beta, eta):
    a, b = mp.log(2), mp.log(3)
    Delta = (2*a)**2 - b**2
    C = (mp.mpf(4)/3)**(-beta) * 4*a**4/(b**2*(b-a)**2)
    return 1 + C*mp.e**(-eta*Delta), Delta, C


if __name__ == "__main__":
    beta = mp.mpf(1)
    print("beta =", beta)
    for eta in (10, 15, 20):
        exact = det_ratio(beta, mp.mpf(eta))
        pred, Delta, C = first_correction(beta, mp.mpf(eta))
        print("eta", eta)
        print("  det/L123 =", mp.nstr(exact, 30))
        print("  1+C exp(-eta Delta) =", mp.nstr(pred, 30))
        print("  residual =", mp.nstr(exact-pred, 12))
    print("Delta =", mp.nstr(Delta, 30))
    print("C_beta =", mp.nstr(C, 30))
