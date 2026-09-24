#!/usr/bin/env python3
"""Audit the Weyl inverse-square mass budget against zero tables.

This is a numerical discovery script. It assumes the supplied ordinates are
real critical-line zeros and does not prove RH.

Usage:
    python audit_weyl_moment_budget.py --zeros zeta_zeros_100k.txt
    python audit_weyl_moment_budget.py --zeros zeros6.txt --plain
"""

import argparse
import math
import numpy as np
import mpmath as mp


def von_mangoldt(k):
    for p in range(2, k + 1):
        if k % p == 0:
            m = k
            while m % p == 0:
                m //= p
            return mp.log(p) if m == 1 else mp.mpf("0")
    return mp.mpf("0")


def q00(lam, dps=50):
    mp.mp.dps = dps
    lam = mp.mpf(lam)
    L = 2 * mp.log(lam)
    pi = mp.pi

    rho = lambda y: mp.exp(y / 2) / (mp.exp(y) - mp.exp(-y))
    tail = mp.log((mp.exp(L) + 1) / (mp.exp(L) - 1)) / 2

    integ = mp.quad(
        lambda y: (
            mp.exp(y / 2) * 2 * (1 - y / L) - 2
        ) / (mp.exp(y) - mp.exp(-y)),
        [0, L],
    )

    diagR = mp.log(4 * pi) + mp.euler + integ - 2 * tail
    w02 = 32 * mp.sinh(L / 4) ** 2 / L

    K = int(mp.floor(lam**2 + mp.mpf("1e-30")))
    wp = mp.mpf("0")
    for k in range(2, K + 1):
        c = von_mangoldt(k)
        if c:
            y = mp.log(k)
            wp += c / mp.sqrt(k) * 2 * (1 - y / L)

    return L, w02 - diagR - wp


def load_zeros(path, indexed):
    if indexed:
        data = np.loadtxt(path, usecols=[1], dtype=np.float64)
    else:
        data = np.loadtxt(path, dtype=np.float64)
    return np.asarray(data, dtype=np.float64)


def moment(L, zeros):
    return (8.0 / L) * np.sum(
        np.sin(zeros * L / 2.0) ** 2 / zeros**2
    )


def asymptotic_tail(L, T):
    return (
        2.0 / (math.pi * L)
        * (math.log(T / (2 * math.pi)) + 1.0)
        / T
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zeros", required=True)
    ap.add_argument(
        "--plain",
        action="store_true",
        help="input has one ordinate per line instead of index + ordinate",
    )
    ap.add_argument(
        "--lambda-values",
        nargs="*",
        default=["3", "3.6", "4.2"],
    )
    args = ap.parse_args()

    zeros = load_zeros(args.zeros, indexed=not args.plain)
    T = float(zeros[-1])

    print("count =", len(zeros))
    print("first =", repr(float(zeros[0])))
    print("last  =", repr(T))
    print()

    for lam in args.lambda_values:
        Lmp, qmp = q00(lam)
        L = float(Lmp)
        q = float(qmp)
        S = float(moment(L, zeros))
        rem = q - S
        tail = asymptotic_tail(L, T)

        print("lambda =", lam)
        print("L      =", format(L, ".16g"))
        print("Q00    =", format(q, ".17g"))
        print("S_L(T) =", format(S, ".17g"))
        print("S/Q00  =", format(S / q, ".12g"))
        print("remain =", format(rem, ".12g"))
        print("tail~  =", format(tail, ".12g"))
        print("remain-tail =", format(rem - tail, ".12g"))
        print()


if __name__ == "__main__":
    main()
