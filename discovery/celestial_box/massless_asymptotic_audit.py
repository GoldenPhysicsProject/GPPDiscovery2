#!/usr/bin/env python3
"""High-precision audit of the regulated scalar-box m -> 0+ asymptotic.

Starting from the exact reduced dispersion integral already derived in
REGULATED_BOX_DILOG_DERIVATION.md,

    J(-S,-U;m) = 8/(S U) int_0^R atanh(r)/(1-kappa^2 r^2) dr,

this script tests the candidate asymptotic

    J_asym = [2 log(S/m) log(U/m) + log(U/m)^2 - pi^2/3]/(S U).

The statement tested here is discovery-level numerical evidence, not a proof of the
o(1) remainder.  S,U,m are positive and m denotes the common mass-squared regulator.
"""

import mpmath as mp

mp.mp.dps = 80


def regulated_box(S, U, m):
    S, U, m = map(mp.mpf, (S, U, m))
    R = mp.sqrt(U / (U + 4 * m))
    kappa2 = (S * (U + 4 * m) - 4 * m * m) / (S * U)

    def integrand(r):
        return mp.atanh(r) / (1 - kappa2 * r * r)

    # Split near the moving endpoint to stabilize the increasingly sharp boundary layer.
    cuts = [mp.mpf('0'), R / 2, R * mp.mpf('0.9'), R * mp.mpf('0.99'), R]
    return 8 / (S * U) * mp.quad(integrand, cuts)


def asymptotic_box(S, U, m):
    S, U, m = map(mp.mpf, (S, U, m))
    return (
        2 * mp.log(S / m) * mp.log(U / m)
        + mp.log(U / m) ** 2
        - mp.pi ** 2 / 3
    ) / (S * U)


def audit_anchor(S, U, exponents=(3, 4, 5, 6, 7, 8)):
    print(f"\nanchor S={S}, U={U}")
    print(" e       J regulated                         J-J_asym")
    previous = None
    for e in exponents:
        m = mp.power(10, -e)
        exact = regulated_box(S, U, m)
        residual = exact - asymptotic_box(S, U, m)
        ratio = ""
        if previous is not None and residual != 0:
            ratio = f"  ratio={mp.nstr(abs(residual / previous), 8)}"
        print(f"{e:2d}  {mp.nstr(exact, 30):>32}  {mp.nstr(residual, 14):>18}{ratio}")
        previous = residual


def leading_log_audit(S, U, exponents=(6, 8, 10, 12)):
    target = mp.mpf(3) / (mp.mpf(S) * mp.mpf(U))
    print(f"\nleading log^2 coefficient anchor S={S}, U={U}; target={mp.nstr(target, 15)}")
    for e in exponents:
        m = mp.power(10, -e)
        L = mp.log(1 / m)
        quotient = regulated_box(S, U, m) / (L * L)
        print(f"e={e:2d}: J/log(1/m)^2 = {mp.nstr(quotient, 18)}")


if __name__ == "__main__":
    anchors = [(3, 2), (2, 3), (1, 1), (4, 1), (1, 4), (5, 7)]
    for S, U in anchors:
        audit_anchor(S, U)
    for S, U in ((3, 2), (1, 1), (5, 7)):
        leading_log_audit(S, U)
