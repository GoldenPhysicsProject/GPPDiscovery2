#!/usr/bin/env python3
"""High-precision audit of zeta-Gibbs cumulant/Hankel identities on beta>1.

This script is evidence only. The exact argument is the positive von-Mangoldt
prime-power expansion recorded in COMPLETE_MONOTONE_FISHER_HANKEL.md.
"""

import mpmath as mp

mp.mp.dps = 80


def A(beta):
    return mp.log(mp.zeta(beta))


def kappa(beta, r):
    return (-1) ** r * mp.diff(A, beta, r)


def check(beta):
    ks = {r: kappa(beta, r) for r in range(1, 7)}
    hankel2 = ks[2] * ks[4] - ks[3] ** 2
    # derivative identities for the Fisher metric g=kappa_2
    g = ks[2]
    gp = mp.diff(lambda b: kappa(b, 2), beta)
    gpp = mp.diff(lambda b: kappa(b, 2), beta, 2)
    return {
        "beta": beta,
        "kappa": ks,
        "gprime_plus_kappa3": gp + ks[3],
        "gsecond_minus_kappa4": gpp - ks[4],
        "hankel2": hankel2,
        "logconvex_numerator": g * gpp - gp ** 2,
    }


def main():
    betas = [mp.mpf("1.01"), mp.mpf("1.1"), mp.mpf("1.5"), mp.mpf("2"),
             mp.mpf("3"), mp.mpf("5"), mp.mpf("10")]
    worst_d1 = mp.mpf("0")
    worst_d2 = mp.mpf("0")
    for beta in betas:
        out = check(beta)
        ks = out["kappa"]
        assert all(ks[r] > 0 for r in ks)
        assert out["hankel2"] > 0
        assert out["logconvex_numerator"] > 0
        worst_d1 = max(worst_d1, abs(out["gprime_plus_kappa3"]))
        worst_d2 = max(worst_d2, abs(out["gsecond_minus_kappa4"]))
        print(f"beta={mp.nstr(beta, 8)}")
        for r in range(1, 7):
            print(f"  kappa_{r} = {mp.nstr(ks[r], 30)}")
        print(f"  k2*k4-k3^2 = {mp.nstr(out['hankel2'], 30)}")
    print("worst |g' + kappa_3| =", mp.nstr(worst_d1, 10))
    print("worst |g'' - kappa_4| =", mp.nstr(worst_d2, 10))


if __name__ == "__main__":
    main()
