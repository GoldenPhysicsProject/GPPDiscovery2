#!/usr/bin/env python3
"""High-precision audit of the exact Gamma half-plane factorization.

Checks on real k:
  H_+(k) H_-(k) = sech(k/2)^2,
  H_-(k) = conjugate(H_+(k)),
  |H_-/H_+| = 1,
and the m-th powers for m=1,...,5.
"""

import mpmath as mp

mp.mp.dps = 80


def hp(z):
    return mp.gamma(mp.mpf("0.5") - 1j * z / (2 * mp.pi)) ** 2 / mp.pi


def hm(z):
    return mp.gamma(mp.mpf("0.5") + 1j * z / (2 * mp.pi)) ** 2 / mp.pi


def main():
    ks = [mp.mpf("0"), mp.mpf("0.125"), mp.mpf("0.3"), mp.mpf("1"), mp.mpf("3"), mp.mpf("7"), mp.mpf("15")]
    tol = mp.mpf("1e-65")
    for k in ks:
        base = mp.sech(k / 2) ** 2
        a = hp(k)
        b = hm(k)
        assert abs(a * b - base) < tol
        assert abs(b - mp.conj(a)) < tol
        assert abs(abs(b / a) - 1) < tol
        for m in range(1, 6):
            assert abs((a ** m) * (b ** m) - mp.sech(k / 2) ** (2 * m)) < tol
        print(f"k={k}: residual={mp.nstr(abs(a*b-base), 8)} phase_mod={mp.nstr(abs(b/a), 30)}")
    print("All Gamma half-plane factor audits passed.")


if __name__ == "__main__":
    main()
