#!/usr/bin/env python3
"""Verify the exact bridge Q00 = C_L(0).

The formulas are zero-independent. This script does not prove RH.
"""

from __future__ import annotations
import argparse
import mpmath as mp


def von_mangoldt(k: int):
    for p in range(2, k + 1):
        if k % p == 0:
            m = k
            while m % p == 0:
                m //= p
            return mp.log(p) if m == 1 else mp.mpf("0")
    return mp.mpf("0")


def tau_tail(L):
    return mp.mpf("0.5") * mp.log((mp.e**L + 1) / (mp.e**L - 1))


def q00_ccm(L):
    pole = 32 * mp.sinh(L / 4) ** 2 / L

    arch_int = mp.quad(
        lambda u: (
            2 * mp.e**(u / 2) * (1 - u / L) - 2
        ) / (mp.e**u - mp.e**(-u)),
        [0, L],
    )
    wr00 = mp.log(4 * mp.pi) + mp.euler + arch_int - 2 * tau_tail(L)

    K = int(mp.floor(mp.e**L + mp.mpf("1e-30")))
    wp00 = mp.mpf("0")
    for n in range(2, K + 1):
        vm = von_mangoldt(n)
        if vm:
            wp00 += 2 * vm / mp.sqrt(n) * (1 - mp.log(n) / L)

    return pole - wr00 - wp00


def C0_explicit(L):
    h = lambda u: max(mp.mpf("0"), 1 - abs(u) / L)

    pole = mp.quad(
        lambda u: 2 * mp.cosh(u / 2) * h(u),
        [-L, 0, L],
    )

    local = mp.quad(
        lambda u: (
            mp.e**(u / 2) * (h(u) + h(-u)) - 2 * h(0)
        ) / (mp.e**u - mp.e**(-u)),
        [0, L],
    )
    tail = mp.quad(
        lambda u: (
            -2 * h(0)
        ) / (mp.e**u - mp.e**(-u)),
        [L, mp.inf],
    )

    K = int(mp.floor(mp.e**L + mp.mpf("1e-30")))
    prime = mp.mpf("0")
    for n in range(2, K + 1):
        vm = von_mangoldt(n)
        if vm:
            y = mp.log(n)
            prime += vm / mp.sqrt(n) * (h(y) + h(-y))

    return (
        pole
        - (mp.log(4 * mp.pi) + mp.euler) * h(0)
        - local
        - tail
        - prime
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lambda-values", nargs="*", default=["2.5", "3", "3.6", "4.2"])
    ap.add_argument("--dps", type=int, default=60)
    args = ap.parse_args()

    mp.mp.dps = args.dps

    for lam_s in args.lambda_values:
        lam = mp.mpf(lam_s)
        L = 2 * mp.log(lam)
        q = q00_ccm(L)
        c = C0_explicit(L)
        print("lambda =", lam_s)
        print("L      =", mp.nstr(L, 20))
        print("Q00    =", mp.nstr(q, 30))
        print("C_L(0) =", mp.nstr(c, 30))
        print("error  =", mp.nstr(abs(q - c), 8))
        print()


if __name__ == "__main__":
    main()
